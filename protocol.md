# SDG Analysis Protocol

## Pipeline de Procesamiento del Video

Este proyecto procesa un video tutorial (2h21min) que muestra el proceso manual
de generación de informes PQRS para la Secretaría Distrital de Gobierno.

### Principios de procesamiento

1. **Fase por fase** — Se procesa un segmento a la vez para no saturar recursos
2. **Frames temporales** — Los frames se extraen, analizan y eliminan por segmento
3. **ChatGPT browser primero** — Se intenta ChatGPT Plus como multimodal primario
4. **Degradación controlada** — Si ChatGPT falla, rotación a Groq → HuggingFace → MiniMax 3
5. **Progreso guardado** — Cada segmento genera un archivo JSON/MD en data/analysis/
6. **Modelos multimodales**: Se usa primero ChatGPT via browser auth, luego Groq, luego HuggingFace, y como último recurso MiniMax 3 de opencode-go

### Rotación de modelos

| Prioridad | Provider | Modelo | Propósito |
|-----------|----------|--------|-----------|
| 1° | ChatGPT Plus (browser) | gpt-4o-mini | Análisis multimodal de frames |
| 2° | Groq | Llama 4 Scout 17B | Análisis multimodal fallback |
| 3° | Groq | Qwen3.6-27B | Segundo fallback |
| 4° | HuggingFace | Inference API | Tercer fallback |
| 5° (último) | MiniMax 3 (opencode-go) | Solo si todos fallan | Último recurso |

### Verificación de degradación
Antes de cambiar a MiniMax 3, verificar:
- ChatGPT: health-check con chatgpt-health.ps1
- Groq: verificar GROQ_API_KEY, test /models endpoint
- HuggingFace: verificar HF_TOKEN

Solo pasar a MiniMax 3 si TODOS los anteriores fallaron.
