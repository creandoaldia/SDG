# SDG — Hallazgos, Aprendizajes y Lecciones del Proceso

## 1. Modelos multimodales — VERIFICACION COMPLETA

Se probaron exhaustivamente todos los modelos disponibles via ChatGPT Plus (browser auth / Codex):

### Modelos CON vision funcional

| Modelo | Vision | Tiempo promedio | Consumo | Recomendado |
|---|---|---|---|---|
| `openai/gpt-5.4-mini` | SI | ~90-170s por batch | Bajo | **PRIMARIO** |
| `openai/gpt-5.5` | SI | ~105-200s por batch | Medio | Fallback |
| `openai/gpt-5.4` | SI | ND | Medio | Alternativa |
| `openai/gpt-5.4-fast` | SI | ND | Medio | Alternativa rapida |
| `openai/gpt-5.4-mini-fast` | SI | ND | Bajo | Alternativa mini rapida |
| `openai/gpt-5.5-fast` | SI | ND | Medio | Alternativa rapida |
| `openai/gpt-5.5-pro` | SI | ND | Alto | Potencia maxima |

### Modelos SIN vision (via Codex)

| Modelo | Error |
|---|---|
| `openai/gpt-4o-mini` | "model is not supported when using Codex" |
| `openai/gpt-5.3-codex-spark` | "model is not supported" |

### Verificacion de capacidades

Comando usado para verificar:
```
opencode models openai --verbose
```

Campos clave a revisar en la salida JSON:
- `capabilities.input.image`: debe ser `true`
- `capabilities.attachment`: debe ser `true`

## 2. Argumentos de opencode run — ORDEN CRITICO

### INCORRECTO (no funciona):
```
opencode run --format json -m openai/gpt-5.4-mini --file frame.jpg "prompt"
# Error: File not found: "prompt"
```

### CORRECTO (funciona):
```
opencode run --format json -m openai/gpt-5.4-mini "prompt" --file frame.jpg
```

El flag `--file` es de tipo array y consume TODOS los argumentos posicionales
despues de el. El mensaje debe ir SIEMPRE antes de `--file`.

## 3. Scene Detection — NO UTIL PARA EXCEL

Se probo ffmpeg scene detection con threshold 0.3:
```bash
ffmpeg -vf "select='gt(scene,0.3)'" ...
```

**Resultado**: Solo 2 frames detectados en 6 minutos de video.
**Causa**: Los cambios en Excel (cambio de celda seleccionada, scroll, apertura
de menu) tienen muy bajo contraste visual. El scene detection de ffmpeg mide
cambios en los histogramas de color, no cambios semanticos en la interfaz.

**Solucion**: fps fijo a 1.0 (1 frame por segundo). Garantiza capturar cada
cambio de pantalla sin depender de deteccion automatica.

## 4. Prompts en Ingles — AHORRO DE TOKENS

### Problema
El sistema OpenCode tiene un Spanish Input Pipeline que:
1. Detecta que el prompt esta en espanol
2. Carga `input-compressor` + `english-prompt-compiler` 
3. Traduce el prompt a ingles
4. Carga `skill-router` para detectar skills relevantes

Esto agrega ~20-30s de overhead y cientos de tokens por llamada.

### Evidencia
En las primeras pruebas, la salida del analisis mostraba:
```
Skills cargadas: input-compressor, english-prompt-compiler, skill-router
Prompt compilado (EN): ...
```

### Solucion
Escribir el prompt directamente en ingles. El modelo recibe el prompt sin
necesidad de traduccion, ahorrando tiempo y tokens.

## 5. --pure NO EVITA EL PIPELINE DE TRADUCCION

El flag `--pure` de opencode run solo desactiva plugins externos, pero el
Spanish Input Pipeline es parte del system prompt del orquestador, no un
plugin. Por lo tanto `--pure` no tiene efecto en este caso.

## 6. Token Budget Real

Cada llamada a `opencode run` con 100 frames:
- Contexto de proyecto: ~30k tokens (constante)
- 100 imagenes a ~750 tokens c/u = ~75k tokens
- Prompt + transcript: ~2k tokens
- **Total por batch**: ~107k tokens
- **Total 100 batches**: ~10.7M tokens

Considerando que ChatGPT Plus tiene limites de uso, el procesamiento completo
consume una parte significativa del presupuesto mensual. Esto debe considerarse
para futuros procesamientos de video.

## 7. Tiempos de Procesamiento

| Tipo de batch | Tiempo tipico | Notas |
|---|---|---|
| Primer batch de segmento | ~160-200s | Carga el proyecto OpenCode |
| Batch siguiente (mismo segmento) | ~140-170s | Contexto parcialmente cacheado |
| Batch final (frames restantes) | ~90-130s | Menos frames |
| Batch con frames repetitivos | ~60-90s | Modelo detecta rapido que no hay cambios |
