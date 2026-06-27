#!/usr/bin/env python3
"""
Transcribe all audio chunks via Groq Whisper, merge with absolute timestamps.

Usage:
    python src/transcribe_chunks.py

Output:
    data/transcript/transcript_completo.json  (full segments with timestamps)
    data/transcript/transcript_completo.txt   (plain text)
"""
from __future__ import annotations

import json
import os
import sys
import io
import mimetypes
import ssl
import time
import uuid
import urllib.error
from pathlib import Path
from urllib.request import Request, urlopen

# ─── Config ───────────────────────────────────────────────────────────────────
PROJECT_DIR = Path(__file__).resolve().parents[1]
CHUNKS_DIR = PROJECT_DIR / "data" / "audio" / "chunks"
OUT_DIR = PROJECT_DIR / "data" / "transcript"
CHUNK_DURATION_SEC = 900  # 15 min per chunk

# Groq API
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_MODEL = "whisper-large-v3"
MAX_ATTEMPTS = 3

CHUNKS = sorted(CHUNKS_DIR.glob("chunk_*.mp3"))


# ─── API call ─────────────────────────────────────────────────────────────────

def _build_multipart(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    boundary = f"----WAFLE{uuid.uuid4().hex}"
    eol = b"\r\n"
    buf = io.BytesIO()
    for name, value in fields.items():
        buf.write(f"--{boundary}".encode()); buf.write(eol)
        buf.write(f'Content-Disposition: form-data; name="{name}"'.encode()); buf.write(eol)
        buf.write(eol); buf.write(str(value).encode()); buf.write(eol)
    mimetype = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    buf.write(f"--{boundary}".encode()); buf.write(eol)
    buf.write(f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"'.encode()); buf.write(eol)
    buf.write(f"Content-Type: {mimetype}".encode()); buf.write(eol); buf.write(eol)
    buf.write(file_path.read_bytes()); buf.write(eol)
    buf.write(f"--{boundary}--".encode()); buf.write(eol)
    return buf.getvalue(), boundary


def transcribe_chunk(api_key: str, audio_path: Path, chunk_index: int) -> list[dict]:
    """Transcribe one chunk, return segments with absolute timestamps."""
    fields = {
        "model": GROQ_MODEL,
        "response_format": "verbose_json",
        "temperature": "0",
    }
    body, boundary = _build_multipart(fields, audio_path)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "User-Agent": "wafle-sdg/1.0",
    }
    context = ssl.create_default_context()
    offset = chunk_index * CHUNK_DURATION_SEC

    for attempt in range(MAX_ATTEMPTS):
        req = Request(GROQ_ENDPOINT, data=body, headers=headers, method="POST")
        try:
            with urlopen(req, timeout=600, context=context) as resp:
                payload = resp.read().decode("utf-8", errors="replace")
            data = json.loads(payload)
            segments = []
            for seg in data.get("segments") or []:
                text = (seg.get("text") or "").strip()
                if not text:
                    continue
                segments.append({
                    "start": round(float(seg.get("start", 0)) + offset, 2),
                    "end": round(float(seg.get("end", 0)) + offset, 2),
                    "text": text,
                    "chunk": chunk_index,
                })
            if not segments:
                full = (data.get("text") or "").strip()
                if full:
                    segments.append({
                        "start": float(offset),
                        "end": float(offset + CHUNK_DURATION_SEC),
                        "text": full,
                        "chunk": chunk_index,
                    })
            return segments
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:200] if exc.fp else ""
            print(f"  HTTP {exc.code}: {detail}", file=sys.stderr)
            if 400 <= exc.code < 500 and exc.code != 429:
                raise SystemExit(f"Chunk {chunk_index}: request failed: {exc.code} {detail}")
            if attempt < MAX_ATTEMPTS - 1:
                delay = 2 ** (attempt + 1)
                print(f"  Retrying in {delay}s...", file=sys.stderr)
                time.sleep(delay)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            print(f"  Network error: {exc}", file=sys.stderr)
            if attempt < MAX_ATTEMPTS - 1:
                delay = 2 ** (attempt + 1)
                print(f"  Retrying in {delay}s...", file=sys.stderr)
                time.sleep(delay)

    raise SystemExit(f"Chunk {chunk_index}: failed after {MAX_ATTEMPTS} attempts")


# ─── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("ERROR: GROQ_API_KEY not set", file=sys.stderr)
        return 1

    if not CHUNKS:
        print(f"ERROR: No chunks found in {CHUNKS_DIR}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total_chunks = len(CHUNKS)
    all_segments: list[dict] = []

    print(f"Transcribiendo {total_chunks} chunks con Groq {GROQ_MODEL}...", file=sys.stderr)
    print(f"Progreso: chunk X/{total_chunks}", file=sys.stderr)

    for i, chunk_path in enumerate(CHUNKS):
        size_mb = chunk_path.stat().st_size / (1024 * 1024)
        print(f"[{i+1}/{total_chunks}] {chunk_path.name} ({size_mb:.1f} MB)...", file=sys.stderr)
        segments = transcribe_chunk(api_key, chunk_path, i)
        all_segments.extend(segments)
        print(f"  → {len(segments)} segmentos (total acumulado: {len(all_segments)})", file=sys.stderr)
        # Small delay to avoid rate limiting
        time.sleep(1.0)

    # Sort by start time (paranoid merge)
    all_segments.sort(key=lambda s: s["start"])

    # Build full text
    full_text_parts = []
    for seg in all_segments:
        mm, ss = divmod(int(seg["start"]), 60)
        hh, mm = divmod(mm, 60)
        ts = f"{hh:02d}:{mm:02d}:{ss:02d}"
        full_text_parts.append(f"[{ts}] {seg['text']}")

    # Save JSON
    json_path = OUT_DIR / "transcript_completo.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"segments": all_segments, "total_segments": len(all_segments)}, f, ensure_ascii=False, indent=2)
    print(f"\nJSON guardado: {json_path} ({len(all_segments)} segmentos)", file=sys.stderr)

    # Save TXT
    txt_path = OUT_DIR / "transcript_completo.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(full_text_parts))
    print(f"TXT guardado: {txt_path} ({len(full_text_parts)} líneas)", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
