# SDG — Ahorros, Optimizaciones y Evidencia

## 1. Evolucion del Pipeline: 4 Versiones

### V0 — Original (Groq-only, REST directa)
- Llamaba directo a `api.groq.com/openai/v1/chat/completions`
- Una sola key (sin rotacion)
- Sin transcript context
- 100 frames extraidos sin escena detectada
- **Problemas**: Key se rate-limita rapido, sin fallback

### V1 — Multi-key Groq
- Agrego rotacion round-robin entre 3 keys
- 100 frames, batches de 5
- Sin ChatGPT
- **Problemas**: Sin fallback a ChatGPT, 3 keys se terminan rate-limitando

### V2 — ChatGPT-first (batch optimizado)
- Primero intenta `opencode run -m openai/gpt-5.4-mini`
- Fallback a gpt-5.5, luego Groq, luego HF
- Prompt en espanol (con pipeline de traduccion)
- 15 frames por batch, 0.1fps
- **Problemas**: 15 frames insuficientes para cobertura total

### V3 — Produccion (ACTUAL) ✅
- **Modelo**: `openai/gpt-5.4-mini` — unico proveedor usado (12/12 segmentos)
- **Frames**: fps=1.0 (1 frame/segundo) — cobertura total
- **Batch**: 100 frames por llamada — optimo entre payload y velocidad
- **Prompt**: En ingles directo — evita pipeline de traduccion
- **Contexto**: Transcripcion incluida en cada batch

## 2. Comparativa de Modelos

| Modelo | Vision | Tiempo 10f | Tiempo 50f | Tiempo 100f | Tokens/img | Recomendado |
|---|---|---|---|---|---|---|
| gpt-4o-mini | NO | - | - | - | - | No disponible via Codex |
| gpt-5.3-codex-spark | NO | - | - | - | - | No disponible |
| **gpt-5.4-mini** | **SI** | **~96s** | **~98s** | **~100-170s** | ~750 | **PRIMARIO** |
| gpt-5.5 | SI | ~105s | ~110s | ~180s | ~1000 | Fallback |
| Groq Llama 4 Scout | SI | ~40s | - | - | ~750 | Fallback (rate-limited) |

**Hallazgo clave**: El tiempo de `opencode run` es casi CONSTANTE
independientemente de si envias 10, 50 o 100 frames. Esto se debe a que el
overhead de arranque (~80s de carga del proyecto OpenCode) domina sobre el
tiempo de inferencia del modelo.

## 3. Ahorro por Prompt en Ingles

| Aspecto | Prompt en espanol | Prompt en ingles | Ahorro |
|---|---|---|---|
| Skills cargadas | input-compressor + english-prompt-compiler + skill-router | Ninguna | 3 skills |
| Tokens de sistema | ~2,000 extra | 0 | ~2,000 tokens |
| Tiempo de carga | ~10-15s extra | 0 | ~10-15s |
| Riesgo de traduccion erronea | Posible | Ninguno | 100% de fidelidad |

**Total ahorrado en 100 batches**: ~200,000 tokens de sistema + ~20 min de tiempo

## 4. Optimizacion de Frames por Batch

| Frames/batch | Tiempo total | Cobertura | Payload cmdline | Recomendado |
|---|---|---|---|---|
| 10 | ~96s | Baja | ~1,100 chars | No (muchas llamadas) |
| 50 | ~98s | Media | ~3,800 chars | Si (segmentos pequenos) |
| **100** | **~100-170s** | **Alta** | **~11,000 chars** | **SI (optimo)** |
| 200 | ~200-300s | Muy alta | ~22,000 chars | Posible (limite Windows ~32k) |

**Optimo**: 100 frames por batch — balance entre tiempo, cobertura y
limite de linea de comandos de Windows (~32,767 chars).

## 5. Token Budget Total

| Concepto | Por batch | Total (100 batches) |
|---|---|---|
| Contexto de proyecto | ~30,000 tokens | ~3,000,000 tokens |
| Imagenes (100 a ~750 c/u) | ~75,000 tokens | ~7,500,000 tokens |
| Prompt + transcript | ~2,000 tokens | ~200,000 tokens |
| Respuesta del modelo | ~1,000 tokens | ~100,000 tokens |
| **Total** | **~108,000 tokens** | **~10,800,000 tokens** |

## 6. Tiempo Real de Procesamiento

| Fase | Duracion | % del total |
|---|---|---|
| Extraccion de frames (12 segmentos) | ~2.5 min | 1% |
| Procesamiento ChatGPT (100 batches) | ~4 horas | 98% |
| Compilacion de documentos | ~1 min | 1% |
| **Total** | **~4 horas** | **100%** |

## 7. Lo que NO funciono (y por que)

| Enfoque | Resultado | Leccion |
|---|---|---|
| Scene detection (threshold 0.3) | Solo 2 frames en 6 min | Excel tiene cambios muy sutiles para deteccion de escenas |
| --pure flag en opencode run | Sin efecto | Spanish Input Pipeline no es un plugin |
| REST API directa con token OAuth | "insufficient quota" | OAuth no es API key |
| gpt-4o-mini via Codex | "model not supported" | Codex no expone este modelo |
| Groq 3 keys paralelas | Todas rate-limited (403/1010) | Rotacion secuencial con cooldown es mejor |
