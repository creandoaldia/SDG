# Patron Groq Rolling-Robin para Multi-Key Rotation

## Problema Original

Groq impone limites de tasa (rate limits) en su API gratuita. Cuando se
procesan multiples solicitudes con imagenes grandes, las claves individuales
se bloquean rapidamente (HTTP 403 error code 1010 = "account frozen/rate
limited").

## Solucion: Rolling-Robin con Multi-Key

El patron Rolling-Robin distribuye las solicitudes entre N claves API,
rotando en cada intento para maximizar el rendimiento antes de alcanzar
los limites de cada clave.

## Implementacion Generica (Python)

```python
import os, time, urllib.request, urllib.error, json, ssl
from pathlib import Path

# --- Configuracion ---
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
MAX_RETRIES = 6  # 2 rotaciones completas de 3 keys
RATE_LIMIT_COOLDOWN = 60  # segundos antes de reintentar una key rate-limited

# --- Carga de claves ---
def load_groq_keys() -> list[str]:
    """
    Carga todas las GROQ API keys desde variables de entorno y .env.
    Soportadas: GROQ_API_KEY, groq_key_javalencia_respaldo, groq_key_exito929_respaldo
    """
    keys = []
    env_names = ["GROQ_API_KEY", "groq_key_javalencia_respaldo", "groq_key_exito929_respaldo"]

    # 1. Variables de entorno
    for name in env_names:
        val = os.environ.get(name)
        if val and val.strip():
            keys.append(val.strip())

    # 2. Archivo .env
    env_file = Path(".env")
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if "=" not in line or line.startswith("#"):
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip("\"'")
            if k in env_names and v and v not in keys:
                keys.append(v)

    return keys


# --- Rolling-Robin ---
class GroqRollingRobin:
    """
    Rotacion round-robin de claves Groq con soporte para:
      - Multiples claves
      - Rate limit detection y rotacion
      - Cooldown entre reintentos
      - Timeout y fallos de red

    Uso:
        groq = GroqRollingRobin()
        respuesta = groq.call(model="meta-llama/llama-4-scout-17b-16e-instruct",
                              messages=[...])
    """

    def __init__(self, keys: list[str] | None = None):
        self.keys = keys or load_groq_keys()
        self.index = 0
        self.cooldowns: dict[str, float] = {}  # key -> timestamp de cooldown

    def _next_key(self) -> str:
        """Retorna la siguiente clave disponible (round-robin)."""
        if not self.keys:
            raise RuntimeError("No Groq API keys available")

        # Intentar hasta encontrar una clave no en cooldown
        for _ in range(len(self.keys)):
            key = self.keys[self.index % len(self.keys)]
            self.index += 1

            # Verificar cooldown
            if key in self.cooldowns:
                if time.time() < self.cooldowns[key]:
                    continue  # Aun en cooldown, probar siguiente
                else:
                    del self.cooldowns[key]  # Cooldown expirado

            return key

        # Todas las claves en cooldown, esperar y reintentar
        time.sleep(5)
        return self._next_key()

    def call(self, model: str, messages: list[dict],
             max_tokens: int = 2048, temperature: float = 0,
             timeout: int = 180) -> str | None:
        """
        Realiza una llamada a Groq con rolling-robin.

        Args:
            model: Model ID (ej: "meta-llama/llama-4-scout-17b-16e-instruct")
            messages: Lista de mensajes en formato OpenAI
            max_tokens: Max tokens de respuesta
            temperature: Temperatura (default 0 para precision)
            timeout: Timeout por llamada

        Returns:
            Texto de respuesta o None si todos fallan
        """
        body = json.dumps({
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }).encode()

        for attempt in range(len(self.keys) * 2):  # 2 rotaciones completas
            key = self._next_key()
            masked = key[:12] + "..."

            req = urllib.request.Request(
                GROQ_ENDPOINT, data=body,
                headers={
                    "Authorization": f"Bearer {key}",
                    "Content-Type": "application/json",
                },
                method="POST",
            )

            try:
                with urllib.request.urlopen(req, timeout=timeout,
                                            context=ssl.create_default_context()) as resp:
                    data = json.loads(resp.read().decode())
                    return data["choices"][0]["message"]["content"]

            except urllib.error.HTTPError as exc:
                if exc.code == 429:
                    print(f"  Rate limit (429) con {masked}, cooldown...")
                    self.cooldowns[key] = time.time() + 60
                    time.sleep(2)
                    continue
                elif exc.code == 403:
                    err_body = exc.read().decode()[:200]
                    # 403 error code 1010 = key bloqueada/rate-limited
                    if "1010" in err_body:
                        print(f"  Key bloqueada (403/1010): {masked}")
                        self.cooldowns[key] = time.time() + 300  # 5 min cooldown
                        time.sleep(1)
                        continue
                    raise  # Otro error 403, no recuperable
                elif exc.code == 400:
                    err_body = exc.read().decode()[:200]
                    if "image" not in err_body.lower() and "vision" not in err_body.lower():
                        continue  # Reintentar con otra key
                    raise  # Error de la solicitud, no de la key
                else:
                    print(f"  HTTP {exc.code} con {masked}, rotando...")
                    time.sleep(1)
                    continue

            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                print(f"  Network error: {exc}, rotando...")
                time.sleep(2)
                continue

        return None  # Todos los intentos fallaron

    def call_vision(self, model: str, system_prompt: str,
                    user_prompt: str, frames: list[dict],
                    batch_size: int = 5,
                    max_tokens: int = 2048) -> str | None:
        """
        Envia frames a un modelo multimodal (vision) con rolling-robin.

        Args:
            model: Model ID del modelo vision
            system_prompt: Prompt del sistema
            user_prompt: Prompt del usuario
            frames: Lista de dicts con clave 'path'
            batch_size: Max frames por solicitud
            max_tokens: Max tokens de respuesta

        Returns:
            Texto combinado de analisis o None
        """
        import base64

        all_descriptions = []

        for batch_start in range(0, len(frames), batch_size):
            batch = frames[batch_start:batch_start + batch_size]
            content = [{"type": "text", "text": user_prompt}]

            for f in batch:
                with open(f["path"], "rb") as img:
                    b64 = base64.b64encode(img.read()).decode()
                content.append({
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{b64}", "detail": "high"},
                })

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content},
            ]

            desc = self.call(model, messages, max_tokens=max_tokens)
            if desc:
                all_descriptions.append(desc)
            else:
                break  # Si un batch falla, detener

        return "\n\n".join(all_descriptions) if all_descriptions else None


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Cargar claves
    keys = load_groq_keys()
    print(f"Claves Groq disponibles: {len(keys)}")

    # Uso basico: texto
    groq = GroqRollingRobin(keys)
    respuesta = groq.call(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": "Hola, respondeme en 3 palabras"}],
    )
    if respuesta:
        print(f"Respuesta: {respuesta}")

    # Uso vision (con frames)
    # respuesta = groq.call_vision(
    #     model="meta-llama/llama-4-scout-17b-16e-instruct",
    #     system_prompt="Eres un analista experto.",
    #     user_prompt="Describe estas imagenes.",
    #     frames=[{"path": "frame_00001.jpg"}],
    # )
```

## Lecciones Aprendidas

### 1. Rate limiting es agresivo
Groq bloquea las claves rapidamente cuando se envian multiples solicitudes
con imagenes grandes. Con 3 keys, se lograron ~60 solicitudes antes de que
todas fueran bloqueadas (403 error code 1010).

### 2. Imagenes grandes = mas rate limiting
Cada frame de 1024px genera ~28KB de base64. 20 frames por batch = ~560KB
de payload. Groq procesa esto pero cuenta contra el rate limit.

### 3. Cooldown entre intentos
Incluso con rotacion, es CRITICO agregar delays (`time.sleep(1)`) entre
intentos para no saturar las claves.

### 4. Deteccion de 403 vs 429
- **429**: Rate limit temporal (esperar 60s)
- **403 error code 1010**: Key bloqueada permanentemente o por periodo
  prolongado (esperar 5+ minutos o regenerar la key)

### 5. No usar todas las claves a la vez
Con 3 keys, rotar secuencialmente (no en paralelo) para maximizar la
vida util de cada clave antes del rate limit.

## Alternativa Recomendada

Para nuevos proyectos, considerar:
1. **ChatGPT gpt-5.4-mini via opencode run** como primario (sin rate limits
   visibles, mas rapido, mejor calidad de analisis)
2. **Groq rolling-robin** solo como fallback cuando ChatGPT no este disponible
3. **HuggingFace Inference API** como ultimo recurso
