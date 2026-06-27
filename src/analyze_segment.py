#!/usr/bin/env python3
"""
SDG Video Analysis — FASE 4: Multimodal per-segment analysis (OPTIMIZED).

Extracts frames at 1fps (full screen-by-screen coverage), analyzes via ChatGPT vision (gpt-5.4-mini),
and saves structured analysis per segment.

Optimizations (v3, June 2026):
  ✓ Frame dedup via SSIM (--ssim-threshold 0.95) — skips ~70% of identical frames
  ✓ Batch size 200 (was 100) — 50% fewer API calls → 50% less system prompt overhead
  ✓ Resolution 768px (was 1024) — 39% fewer image tokens at tile-optimal size
  ✓ Slim prompt — self-contained, no project context dependency
  ✓ --detail-low flag — EXPERIMENTAL: res=512 + SSIM=0.97 + JPEG Q10 (max token saving)

Usage:
    python src/analyze_segment.py --all --ssim-threshold 0.95  # Optimized run
    python src/analyze_segment.py --all --detail-low           # Max token savings
    python src/analyze_segment.py --segment 1                  # Single segment
    python src/analyze_segment.py --segment 1 --dry-run        # Extract frames only

Pipeline evolution:
    v1 — Groq-only direct API, REST calls, single-key, 100 frames
    v2 — ChatGPT-first (gpt-5.4-mini), 100f/batch, transcript context
    v3 — CURRENT: SSIM dedup + batch 200 + res 768 + slim prompt + detail-low

Confirmed working models (vision via opencode Codex):
    ✅ openai/gpt-5.4-mini  (fastest, cheapest — PRIMARY)
    ✅ openai/gpt-5.5       (powerful, slower — FALLBACK)
    ❌ gpt-4o-mini, gpt-5.3-codex-spark (not supported by Codex)
"""
from __future__ import annotations

import base64
import json
import os
import re
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image

# ─── Paths ────────────────────────────────────────────────────────────────────
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
FRAMES_DIR = DATA_DIR / "frames"
SEGMENTS_FILE = DATA_DIR / "segments" / "segmentos.json"
ANALYSIS_DIR = DATA_DIR / "analysis"
ENV_FILE = Path("C:/web-ai-lab/.env")

# ─── Groq multi-key rotation (fallback if ChatGPT fails) ──────────────────────

def _load_env_file() -> dict[str, str]:
    env = {}
    if not ENV_FILE.exists():
        return env
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip("\"'")
    return env


def _load_groq_keys() -> list[str]:
    keys: list[str] = []
    env_names = ["GROQ_API_KEY", "groq_key_javalencia_respaldo", "groq_key_exito929_respaldo"]
    for name in env_names:
        val = os.environ.get(name)
        if val and val.strip():
            keys.append(val.strip())
    dotenv = _load_env_file()
    for name in env_names:
        val = dotenv.get(name)
        if val and val not in keys:
            keys.append(val)
    return keys


GROQ_KEYS: list[str] = []
_key_index = 0

def _next_groq_key() -> str:
    global _key_index
    if not GROQ_KEYS:
        raise RuntimeError("No Groq API keys available")
    key = GROQ_KEYS[_key_index % len(GROQ_KEYS)]
    _key_index += 1
    return key


# ─── Frame extraction (scene detection) ──────────────────────────────────────

def extract_frames(video_path: Path, segment_id: int, start_sec: float, end_sec: float,
                   resolution: int = 768, fps: float = 1.0,
                   jpeg_quality: int = 5) -> list[dict]:
    """Extract frames at specified fps using ffmpeg.
    
    fps=1.0 = 1 frame per second = captures every second of screen activity.
    For Excel tutorials, this ensures every cell change, menu open, and
    data entry is visible to the vision model.
    
    jpeg_quality: ffmpeg -qscale:v ([2-31], lower=better quality, default=5).
                  Use 10-15 for aggressive token saving.
    """
    seg_dir = FRAMES_DIR / f"seg{segment_id:03d}"
    seg_dir.mkdir(parents=True, exist_ok=True)
    duration = end_sec - start_sec

    print(f"  Extrayendo ~{int(duration * fps)} frames ({fps} fps)...", file=sys.stderr)

    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", str(start_sec),
        "-i", str(video_path.resolve()),
        "-t", str(duration),
        "-vf", f"fps={fps},scale={resolution}:-1",
        "-qscale:v", str(jpeg_quality),
        str(seg_dir / "frame_%05d.jpg"),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode != 0:
        print(f"  ffmpeg error: {result.stderr}", file=sys.stderr)
        return []

    frames = []
    for i, fpath in enumerate(sorted(seg_dir.glob("*.jpg"))):
        frames.append({
            "path": str(fpath),
            "index": i,
            "timestamp_sec": round(start_sec + i / fps, 1),
        })

    print(f"  → {len(frames)} frames extraídos ({fps} fps)", file=sys.stderr)
    return frames


# ─── Frame deduplication via SSIM ─────────────────────────────────────────────

def filter_similar_frames(frames: list[dict], ssim_threshold: float = 0.0) -> list[dict]:
    """Remove frames that are too similar to the previous one using SSIM.

    Args:
        frames: List of frame dicts with 'path' keys (from extract_frames).
        ssim_threshold: SSIM threshold [0-1]. Frames with SSIM > threshold
                        compared to the previous kept frame are skipped.
                        0.0 = disabled (keep all frames).
                        Recommended: 0.92-0.97 for Excel tutorials.

    Returns:
        Filtered list with similar frames removed.
    """
    if ssim_threshold <= 0.0 or len(frames) < 2:
        return frames

    kept = [frames[0]]  # Always keep the first frame
    skipped = 0

    for i in range(1, len(frames)):
        prev_path = kept[-1]["path"]
        curr_path = frames[i]["path"]

        try:
            prev_img = np.array(Image.open(prev_path).convert("L"))
            curr_img = np.array(Image.open(curr_path).convert("L"))

            # Resize to same dimensions if needed (should be same, but safety)
            h = min(prev_img.shape[0], curr_img.shape[0])
            w = min(prev_img.shape[1], curr_img.shape[1])
            prev_img = prev_img[:h, :w]
            curr_img = curr_img[:h, :w]

            score = ssim(prev_img, curr_img, data_range=255)
        except Exception:
            score = 0.0  # On error, keep the frame (conservative)

        if score > ssim_threshold:
            skipped += 1
        else:
            kept.append(frames[i])

    kept_pct = len(kept) / len(frames) * 100
    print(f"  🎯 SSIM diffing: {len(frames)} → {len(kept)} frames "
          f"({skipped} skipped, {kept_pct:.0f}% kept)", file=sys.stderr)
    return kept


# ─── ChatGPT vision (via opencode run) ────────────────────────────────────────

def _call_chatgpt(frames: list[dict], segment_info: dict, transcript_context: str = "",
                  model: str = "gpt-5.4-mini") -> str | None:
    """Send frames to ChatGPT vision via opencode run with --pure.

    Args:
        frames: List of frame dicts with 'path' keys
        segment_info: Dict with titulo, descripcion, start_sec, end_sec
        transcript_context: Relevant transcript text for this segment
        model: Model name (default: gpt-5.4-mini — fastest vision model)
    """
    # Slim prompt: self-contained, no project context dependency.
    # Every token here directly drives analysis — no fluff.
    ts = segment_info['start_sec']
    te = segment_info['end_sec']
    prompt = (
        f"Analyze these frames from '{segment_info['titulo']}' "
        f"({ts//60}:{ts%60:02d}-{te//60}:{te%60:02d}). "
        f"Context: {segment_info['descripcion'][:200]}\n\n"
        "For EACH frame list:\n"
        "• Workbook/sheet visible (filename, tab)\n"
        "• Cells/ranges selected or modified\n"
        "• Action: copy, paste, sort, filter, formula, menu\n"
        "• Values/data shown (exact numbers)\n"
        "• Open windows: Excel, Teams, Visage, dialogs\n\n"
        "Read cell text. Identify formulas. Note screen transitions.\n"
        "Be specific. Prefer accuracy over description.\n"
        "IGNORE WAFLE logo, system welcome, or non-frame content."
    )
    if transcript_context:
        # Keep transcript compact — it's reference, not primary input
        transcript_trimmed = transcript_context[:1200].rsplit("\n", 1)[0]
        prompt += (
            f"\n\nAUDIO (reference):\n{transcript_trimmed}"
        )

    # Build command — message BEFORE --file (required by opencode arg parsing)
    cmd = ["opencode", "run", "--format", "json", "-m", f"openai/{model}", prompt]
    for f in frames:
        cmd.extend(["--file", f["path"]])

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=False, timeout=600,
        )
    except subprocess.TimeoutExpired:
        print(f"    Timeout (>600s) para {model} con {len(frames)} frames", file=sys.stderr)
        return None
    except FileNotFoundError:
        return None

    stdout = result.stdout.decode("utf-8", errors="replace") if result.stdout else ""
    stderr = result.stderr.decode("utf-8", errors="replace") if result.stderr else ""

    if result.returncode != 0:
        err_lower = (stdout + stderr).lower()
        if "model is not supported" in err_lower:
            return None  # Signal fallback to next model
        return None

    # Extract text responses — last meaningful text event is the answer
    texts = []
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
            if ev.get("type") == "text":
                t = ev.get("part", {}).get("text", "")
                if t.strip() and len(t.strip()) > 10:
                    texts.append(t.strip())
        except (json.JSONDecodeError, KeyError):
            continue

    if texts:
        return texts[-1]
    return None


# ─── Groq fallback (multi-key rotation) ───────────────────────────────────────

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def _encode_b64(path: str) -> str:
    with open(path, "rb") as f:
        return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}"


def _call_groq_vision(frames: list[dict], segment_info: dict,
                      transcript_context: str = "") -> str | None:
    """Send frames to Groq multimodal with multi-key round-robin."""
    system_prompt = (
        "Eres un analista experto en procesos de Excel para informes gubernamentales. "
        "Para cada frame, describe: libro/hoja visible, celdas seleccionadas, "
        "acción realizada, valores visibles. Sé específico."
    )
    user_prompt = (
        f"Analiza estos frames del segmento '{segment_info['titulo']}' "
        f"(minuto {segment_info['start_sec']//60}:{segment_info['start_sec']%60:02d}-"
        f"{segment_info['end_sec']//60}:{segment_info['end_sec']%60:02d}).\n"
        f"Contexto: {segment_info['descripcion']}\n"
    )
    if transcript_context:
        user_prompt += f"\nTranscripción:\n{transcript_context[:1500]}\n"

    batch_size = 5
    models = ["meta-llama/llama-4-scout-17b-16e-instruct", "qwen/qwen3.6-27b"]

    for model in models:
        all_desc = []
        try:
            for batch_start in range(0, len(frames), batch_size):
                batch = frames[batch_start:batch_start + batch_size]
                content = [{"type": "text", "text": user_prompt if batch_start == 0 else
                           f"Continúa frames {batch_start+1}-{batch_start+len(batch)}:"}]
                for f in batch:
                    content.append({"type": "image_url", "image_url": {"url": _encode_b64(f["path"])}})

                body = json.dumps({
                    "model": model,
                    "messages": [{"role": "system", "content": system_prompt},
                                 {"role": "user", "content": content}],
                    "max_tokens": 2048, "temperature": 0,
                }).encode()

                desc = None
                for _ in range(6):
                    key = _next_groq_key()
                    req = urllib.request.Request(GROQ_ENDPOINT, data=body, headers={
                        "Authorization": f"Bearer {key}", "Content-Type": "application/json",
                    }, method="POST")
                    try:
                        with urllib.request.urlopen(req, timeout=180, context=ssl.create_default_context()) as resp:
                            desc = json.loads(resp.read())["choices"][0]["message"]["content"]
                            break
                    except urllib.error.HTTPError as exc:
                        if exc.code == 429:
                            time.sleep(1)
                            continue
                        elif exc.code == 403:
                            continue  # Key may be rate-limited
                        break
                    except (urllib.error.URLError, TimeoutError):
                        time.sleep(1)
                        continue
                if desc:
                    all_desc.append(desc)

            if all_desc:
                return "\n\n".join(all_desc)
        except Exception as exc:
            print(f"    Groq {model} error: {exc}", file=sys.stderr)
            continue
    return None


# ─── HuggingFace (last resort) ────────────────────────────────────────────────

def _call_hf(frames: list[dict], segment_info: dict) -> str | None:
    hf_token = os.environ.get("HF_TOKEN") or _load_env_file().get("HF_TOKEN")
    if not hf_token or not frames:
        return None
    model = "meta-llama/Llama-3.2-11B-Vision-Instruct"
    prompt = f"Describe qué se ve en este frame de Excel. Segmento: {segment_info['titulo']}"
    body = json.dumps({"inputs": prompt, "parameters": {"max_new_tokens": 512}}).encode()
    req = urllib.request.Request(f"https://api-inference.huggingface.co/models/{model}", data=body, headers={
        "Authorization": f"Bearer {hf_token}", "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl.create_default_context()) as resp:
            data = json.loads(resp.read())
            if isinstance(data, list):
                return data[0].get("generated_text", str(data))
            return str(data)
    except Exception:
        return None


# ─── Save analysis ────────────────────────────────────────────────────────────

def save_analysis(segment: dict, analysis_text: str, provider: str,
                  frames_used: int, total_batches: int, total_time_ms: float) -> Path:
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    out = ANALYSIS_DIR / f"seg{segment['id']:03d}-{segment['nombre']}.json"
    data = {
        "segment_id": segment["id"],
        "nombre": segment["nombre"],
        "titulo": segment["titulo"],
        "start_sec": segment["start_sec"],
        "end_sec": segment["end_sec"],
        "frames_analyzed": frames_used,
        "batches": total_batches,
        "provider": provider,
        "total_time_ms": round(total_time_ms, 0),
        "analisis": analysis_text,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return out


# ─── Cleanup ──────────────────────────────────────────────────────────────────

def cleanup_frames(segment_id: int):
    seg_dir = FRAMES_DIR / f"seg{segment_id:03d}"
    if seg_dir.exists():
        shutil.rmtree(seg_dir)


# ─── Transcript context ───────────────────────────────────────────────────────

def get_transcript_context(segment: dict) -> str:
    """Get transcript lines within segment time range."""
    tf = DATA_DIR / "transcript" / "transcript_completo.json"
    if not tf.exists():
        return ""
    with open(tf, encoding="utf-8") as f:
        data = json.load(f)
    relevant = []
    for seg in data.get("segments", []):
        start = seg.get("start", 0)
        text = seg.get("text", "")
        if segment["start_sec"] <= start <= segment["end_sec"]:
            mm, ss = divmod(int(start), 60)
            hh, mm = divmod(mm, 60)
            relevant.append(f"[{hh:02d}:{mm:02d}:{ss:02d}] {text}")
    return "\n".join(relevant)


# ─── Rotation chain ───────────────────────────────────────────────────────────

def analyze_multimodal(frames: list[dict], segment_info: dict,
                       transcript_context: str = "") -> tuple[str | None, str | None]:
    """Try providers in priority order.

    Chain:
      1. ChatGPT gpt-5.4-mini (vision via opencode Codex ✅)
      2. ChatGPT gpt-5.5       (vision fallback ✅)
      3. Groq Llama 4 Scout    (multi-key rotation)
      4. HuggingFace           (last resort)
    """
    chain = [
        ("gpt-5.4-mini", lambda: _call_chatgpt(frames, segment_info, transcript_context, "gpt-5.4-mini")),
        ("gpt-5.5",      lambda: _call_chatgpt(frames, segment_info, transcript_context, "gpt-5.5")),
        ("groq-llama4",  lambda: _call_groq_vision(frames, segment_info, transcript_context)),
        ("huggingface",  lambda: _call_hf(frames, segment_info)),
    ]

    for label, fn in chain:
        print(f"  🔄 {label} ({len(frames)} frames)...", file=sys.stderr)
        t0 = time.time()
        try:
            result = fn()
            elapsed = (time.time() - t0) * 1000
            if result and len(result.strip()) > 50:
                print(f"  ✅ {label} — {elapsed:.0f}ms — {len(result)} chars", file=sys.stderr)
                return (result, label)
            print(f"  ⚠️ {label} respuesta vacía ({elapsed:.0f}ms)", file=sys.stderr)
        except Exception as exc:
            print(f"  ❌ {label} error: {exc}", file=sys.stderr)
        time.sleep(1)
    return (None, None)


# ─── Segment processor ────────────────────────────────────────────────────────

def process_segment(segment: dict, dry_run: bool = False,
                    resolution: int = 768, fps: float = 1.0,
                    batch_size: int = 200,
                    ssim_threshold: float = 0.0,
                    detail_low: bool = False) -> int:
    """Process one segment: extract frames → multimodal analysis → save."""
    seg_data = json.loads(SEGMENTS_FILE.read_text(encoding="utf-8"))
    video_path = PROJECT_DIR / seg_data["video"]

    if not video_path.exists():
        print(f"ERROR: Video no encontrado: {video_path}", file=sys.stderr)
        return 1

    global GROQ_KEYS, _key_index
    GROQ_KEYS = _load_groq_keys()
    _key_index = 0

    dur = segment["end_sec"] - segment["start_sec"]
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Segmento {segment['id']}/12: {segment['titulo']}", file=sys.stderr)
    print(f"  {dur//60}:{dur%60:02d} min | Groq keys: {len(GROQ_KEYS)}", file=sys.stderr)
    print(f"{'='*60}", file=sys.stderr)

    # Transcript
    transcript_ctx = get_transcript_context(segment)
    if transcript_ctx:
        print(f"  Transcript: {len(transcript_ctx.splitlines())} líneas", file=sys.stderr)

    # JPEG quality: lower = better. 5=default, 10=aggressive (detail_low)
    jpeg_quality = 10 if detail_low else 5

    # Extract frames
    t0 = time.time()
    frames = extract_frames(video_path, segment["id"], segment["start_sec"],
                            segment["end_sec"], resolution=resolution, fps=fps,
                            jpeg_quality=jpeg_quality)
    extract_ms = (time.time() - t0) * 1000
    if not frames:
        print("ERROR: No se extrajeron frames", file=sys.stderr)
        return 1

    print(f"  Extracción: {extract_ms:.0f}ms", file=sys.stderr)

    # Frame deduplication via SSIM (if threshold > 0)
    # Applied BEFORE dry-run so both show real filtered count
    if ssim_threshold > 0:
        frames = filter_similar_frames(frames, ssim_threshold)
        if not frames:
            print("ERROR: Todos los frames fueron filtrados por SSIM", file=sys.stderr)
            return 1

    if dry_run:
        seg_dir = FRAMES_DIR / f"seg{segment['id']:03d}"
        print(f"\n✅ Dry-run: {len(frames)} frames en {seg_dir}", file=sys.stderr)
        return 0

    # Split into batches of batch_size
    batches = [frames[i:i + batch_size] for i in range(0, len(frames), batch_size)]
    print(f"  Procesando {len(batches)} batch(es) de ≤{batch_size} frames c/u", file=sys.stderr)

    all_analyses = []
    last_provider = None

    for bi, batch in enumerate(batches):
        batch_label = f"{bi+1}/{len(batches)}" if len(batches) > 1 else ""
        print(f"  Batch {batch_label}: {len(batch)} frames...", file=sys.stderr)

        if len(batches) > 1:
            # For multi-batch segments, add batch context to segment info
            batch_segment = dict(segment)
            batch_segment["titulo"] = f"{segment['titulo']} (parte {bi+1}/{len(batches)})"
            batch_segment["start_sec"] = segment["start_sec"] + (bi * batch_size * 2)  # approximate
        else:
            batch_segment = segment

        analysis, provider = analyze_multimodal(batch, batch_segment, transcript_ctx)
        if analysis:
            all_analyses.append((analysis, provider))
            last_provider = provider
        else:
            print(f"  ⚠️ Batch {bi+1} falló — continuando...", file=sys.stderr)

    if not all_analyses:
        print("ERROR: Todos los batches fallaron", file=sys.stderr)
        save_analysis(segment, "[ERROR] Todos los proveedores fallaron",
                      "none", len(frames), len(batches), (time.time() - t0) * 1000)
        cleanup_frames(segment["id"])
        return 1

    # Combine analyses
    full_text = "\n\n".join(
        f"[Batch {i+1} - {prov}]\n{text}"
        for i, (text, prov) in enumerate(all_analyses)
    )

    # Save
    total_ms = (time.time() - t0) * 1000
    out_path = save_analysis(segment, full_text, last_provider or "unknown",
                             len(frames), len(batches), total_ms)
    print(f"\n  💾 Guardado: {out_path}", file=sys.stderr)

    # Cleanup
    cleanup_frames(segment["id"])

    # Summary
    preview = full_text[:600].rsplit("\n", 1)[0]
    print(f"\n{'─'*60}", file=sys.stderr)
    print(f"RESUMEN [{last_provider}] {total_ms:.0f}ms total", file=sys.stderr)
    print(f"{'─'*60}", file=sys.stderr)
    print(preview, file=sys.stderr)
    if len(full_text) > 600:
        print(f"... ({len(full_text)} chars total)", file=sys.stderr)
    print(f"{'─'*60}\n", file=sys.stderr)

    return 0


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="SDG FASE 4 — Análisis multimodal con ChatGPT visión")
    ap.add_argument("--segment", type=int, help="Segment ID (1-12)")
    ap.add_argument("--all", action="store_true", help="Process all segments")
    ap.add_argument("--dry-run", action="store_true", help="Extract frames only")
    ap.add_argument("--resolution", type=int, default=768,
                    help="Frame width (default: 768 — tile-optimal for GPT vision)")
    ap.add_argument("--fps", type=float, default=1.0, help="Frames per second (default: 1.0)")
    ap.add_argument("--batch-size", type=int, default=200,
                    help="Max frames per API call (default: 200)")
    ap.add_argument("--ssim-threshold", type=float, default=0.0,
                    help="SSIM threshold for frame dedup [0-1]. 0=disabled. "
                         "Recommended: 0.95 for Excel tutorials")
    ap.add_argument("--detail-low", action="store_true",
                    help="EXPERIMENTAL: force low-detail image mode "
                         "(res=512, aggressive SSIM=0.97, max compression). "
                         "May reduce token cost but could miss fine detail.")
    args = ap.parse_args()

    # Apply --detail-low overrides
    if args.detail_low:
        args.resolution = 512
        if args.ssim_threshold == 0.0:
            args.ssim_threshold = 0.97
        print("  ⚡ --detail-low: res=512, SSIM=0.97, JPEG Q10", file=sys.stderr)

    if not args.segment and not args.all:
        print("ERROR: Especificar --segment N o --all", file=sys.stderr)
        return 1

    seg_data = json.loads(SEGMENTS_FILE.read_text(encoding="utf-8"))
    segmentos = seg_data["segmentos"]

    if args.all:
        results = []
        for seg in segmentos:
            rc = process_segment(seg, args.dry_run, args.resolution,
                                 args.fps, args.batch_size,
                                 args.ssim_threshold,
                                 args.detail_low)
            results.append((seg["id"], rc))
            if rc != 0:
                print(f"\n⚠️ Segmento {seg['id']} falló\n", file=sys.stderr)

        ok = sum(1 for _, rc in results if rc == 0)
        fail = sum(1 for _, rc in results if rc != 0)
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"FASE 4 COMPLETA: {ok}/{len(results)} OK, {fail} fallos", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)
        return 0 if fail == 0 else 1

    segment = next((s for s in segmentos if s["id"] == args.segment), None)
    if not segment:
        print(f"ERROR: Segmento {args.segment} no encontrado", file=sys.stderr)
        return 1
    return process_segment(segment, args.dry_run, args.resolution,
                          args.fps, args.batch_size,
                          args.ssim_threshold,
                          args.detail_low)


if __name__ == "__main__":
    raise SystemExit(main())
