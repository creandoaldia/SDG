# SDG — Mejores Practicas, Metodologia y Razones

## Como se hizo y por que

### Pipeline final de analisis multimodal

```
Video MP4 (698MB, 2h21min)
    |
    v
[1] Extraer frames a 1fps con ffmpeg
    |   - fps=1.0: 1 frame por segundo
    |   - scale=1024:-1: resolucion moderada
    |   - qscale:v=5: calidad JPEG alta
    |   - POR QUE: Garantiza capturar CADA cambio de pantalla
    |
    v
[2] Dividir en batches de 100 frames
    |   - POR QUE: Limite practico entre payload (~11k chars cmdline)
    |     y velocidad (~2min por batch)
    |
    v
[3] Enviar cada batch a ChatGPT vision via opencode run
    |   opencode run --format json -m openai/gpt-5.4-mini \
    |     "prompt en ingles" --file frame1.jpg ... --file frame100.jpg
    |   - POR QUE: opencode run es la UNICA forma de usar ChatGPT
    |     Plus (browser auth) con vision. No se puede llamar a la
    |     REST API directamente con tokens OAuth.
    |
    v
[4] Parsear respuesta JSON (ultimo evento "text")
    |   - POR QUE: opencode run --format json emite multiples eventos.
    |     El ultimo evento type:"text" contiene la respuesta real.
    |
    v
[5] Guardar analisis como JSON estructurado
    |   - Incluye: segment_id, frames, batches, proveedor, timestamp
    |
    v
[6] Limpiar frames temporales
    |   - POR QUE: 8,467 frames a ~25KB c/u = ~200MB de espacio
    |     en disco. Se eliminan tras analisis.
    |
    v
[7] Compilar documentacion completa
```

### Por que gpt-5.4-mini y no otro modelo

**Razon 1**: Es el unico modelo "mini" con vision disponible via Codex.
gpt-4o-mini (logicamente el mas economico) NO esta disponible en Codex.

**Razon 2**: Es mas rapido que gpt-5.5 (~90-170s vs ~105-200s por batch).

**Razon 3**: Consume menos tokens que gpt-5.5 por imagen procesada.

**Razon 4**: OpenCode lo reporta con `input.image: true` y `attachment: true`.

### Por que opencode run y no REST API directa

El token OAuth de ChatGPT Plus (browser auth) NO tiene los permisos
necesarios para llamar a la REST API de OpenAI:
- `api.openai.com/v1/chat/completions` → "insufficient_quota"
- `api.openai.com/v1/responses` → "Missing scopes: api.responses.write"

La UNICA forma de usar ChatGPT Plus con vision es a traves de
`opencode run` que utiliza el proxy interno Codex.

### Por que 1fps y no scene detection

El video es un tutorial de Excel donde los cambios son:
- Seleccion de celdas (cambia el borde, no el color general)
- Scroll en la hoja (cambia el contenido, no el histograma)
- Apertura de menus (cambios pequenos en la interfaz)
- Alternar entre ventanas (cambios mas grandes)

Scene detection de ffmpeg mide cambios en el histograma de color,
que no detecta estos cambios semanticos. fps=1.0 es simple, predecible
y garantiza cobertura total.

## Lo que NO se debe hacer

### 1. NO usar REST API directa con OAuth
```python
# MALO
import requests
token = leer_auth_json()["openai"]["access"]
requests.post("https://api.openai.com/v1/chat/completions",
              headers={"Authorization": f"Bearer {token}"})
# Error: insufficient_quota
```

### 2. NO poner --file antes del mensaje
```bash
# MALO
opencode run --file frame.jpg "prompt"
# Error: File not found: "prompt"

# BIEN
opencode run "prompt" --file frame.jpg
```

### 3. NO confiar en scene detection para UI/Excel
```bash
# MALO: solo captura 2 frames en 6 min
ffmpeg -vf "select='gt(scene,0.3)'"

# BIEN: captura cada segundo
ffmpeg -vf "fps=1.0,scale=1024:-1"
```

### 4. NO saturar Groq con requests paralelos
```python
# MALO: 3 keys en paralelo = todas rate-limited en segundos
with ThreadPoolExecutor(3):
    for key in keys:
        submit(llamar_groq, key)

# BIEN: secuencial con cooldown
for key in keys:
    llamar_groq(key)
    time.sleep(1)
```

### 5. NO asumir que todos los modelos OpenAI funcionan
Siempre verificar primero:
```bash
opencode models openai --verbose
```
Revisar: `capabilities.input.image: true`

## Checklist para futuros analisis de video

- [ ] Verificar modelos disponibles: `opencode models PROVIDER --verbose`
- [ ] Verificar capacidades: `input.image`, `attachment`
- [ ] Probar con 1 frame antes de procesar todo el video
- [ ] Estimar tiempo total: `duracion_video_segundos / 100 * 120s`
- [ ] Verificar espacio en disco: `duracion_video_segundos * 25KB * 2`
- [ ] Usar prompt en ingles (evita pipeline de traduccion)
- [ ] Poner mensaje ANTES de --file
- [ ] Parsear ultimo evento "text" del JSON de salida
- [ ] Limpiar frames despues de analizar
- [ ] Guardar analisis como JSON estructurado con timestamp
- [ ] Compilar documentacion al finalizar
