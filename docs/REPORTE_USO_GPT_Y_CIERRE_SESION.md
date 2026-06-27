# SDG — Reporte de Uso de GPT y Actores Involucrados

*Generado: 2026-06-22 18:30 UTC*
*Proyecto: SDG (Secretaria Distrital de Gobierno)*
*Video: 2h 21min 7s, 698 MB, tutorial PQRS por Yesenia Patino Figueroa*

---

## 1. Actores Involucrados

| Actor | Rol | Participacion |
|---|---|---|
| **Yesenia Patino Figueroa** | Autora del video, operadora del proceso PQRS | 100% del contenido analizado |
| **Secretaria Distrital de Gobierno (SDG)** | Entidad titular del proceso | Proceso completo documentado |
| **OpenCode (Codex)** | Proxy de autenticacion browser para ChatGPT Plus | 100% de las llamadas AI |
| **ChatGPT gpt-5.4-mini** | Modelo de vision multimodal primario | 100% de los analisis (12/12 segmentos) |
| **ChatGPT gpt-5.5** | Modelo de vision fallback | 0% (no se necesito) |
| **Groq (3 API keys)** | Fallback multimodal | 0% (bloqueadas por rate-limit) |
| **HuggingFace Inference API** | Ultimo recurso | 0% (no se necesito) |
| **DeepSeek V4 Flash** | Orquestador de toda la sesion | 100% de la coordinacion |
| **Groq Whisper** | Transcripcion de audio | FASE 2 completada (1222 segmentos) |
| **ffmpeg** | Extraccion de frames | 100% de los frames (8,467) |

---

## 2. Uso de GPT (gpt-5.4-mini) — Cifras Reales y Porcentajes

### 2.1 Resumen General

| Metrica | Valor | % del total |
|---|---|---|
| **Segmentos analizados** | 12 / 12 | 100% |
| **Batches procesados** | 90 | 100% |
| **Frames analizados** | 8,467 | 100% del video a 1fps |
| **Tiempo total de procesamiento** | 12625s (210.4 min / 3.5 h) | 100% |
| **Documentacion generada** | 348,959 caracteres | 100% del analisis |

### 2.2 Distribucion de Tiempo por Segmento

| # | Segmento | Batches | Frames | Tiempo (s) | % del total | Acumulado |
|---|---|---|---|---|---|---|
| 1 | Apertura, copia de datos y ordenamiento Decreto 37 | 4 | 368 | 663s | 5.2% | 5.2% |
| 2 | Documentos extraviados — tabla dinámica | 3 | 212 | 469s | 3.7% | 9.0% |
| 3 | Registro de atenciones y grupos poblacionales | 4 | 320 | 644s | 5.1% | 14.1% |
| 4 | Documentos extraviados — registro manual uno a uno | 2 | 120 | 319s | 2.5% | 16.6% |
| 5 | Certificado de residencia — productividad | 4 | 335 | 667s | 5.3% | 21.9% |
| 6 | Propiedad horizontal — certificados generados | 5 | 445 | 764s | 6.1% | 27.9% |
| 7 | Encuestas — procesamiento completo | 10 | 930 | 879s | 7.0% | 34.9% |
| 8 | Informe PQRS página web — setup inicial | 9 | 870 | 851s | 6.7% | 41.6% |
| 9 | Tablas dinámicas y subtemas más reiterados | 12 | 1200 | 1418s | 11.2% | 52.9% |
| 10 | Días de gestión y vencimientos | 12 | 1200 | 2050s | 16.2% | 69.1% |
| 11 | Ranking por localidad y datos de supercades | 12 | 1200 | 1925s | 15.2% | 84.3% |
| 12 | Cuadros comparativos, verificación final y cierre | 13 | 1267 | 1976s | 15.7% | 100.0% |
| **Total** | **12 segmentos** | **90** | **8,467** | **12625s** | **100%** | **100%** |

### 2.3 Distribucion de Caracteres de Analisis por Segmento

| # | Segmento | Chars analisis | % del total |
|---|---|---|---|
| 1 | Apertura, copia de datos y ordenamiento Decreto 37 | 21,654 | 6.2% |
| 2 | Documentos extraviados — tabla dinámica | 17,288 | 5.0% |
| 3 | Registro de atenciones y grupos poblacionales | 23,113 | 6.6% |
| 4 | Documentos extraviados — registro manual uno a uno | 8,599 | 2.5% |
| 5 | Certificado de residencia — productividad | 22,467 | 6.4% |
| 6 | Propiedad horizontal — certificados generados | 14,170 | 4.1% |
| 7 | Encuestas — procesamiento completo | 6,482 | 1.9% |
| 8 | Informe PQRS página web — setup inicial | 5,701 | 1.6% |
| 9 | Tablas dinámicas y subtemas más reiterados | 21,299 | 6.1% |
| 10 | Días de gestión y vencimientos | 78,063 | 22.4% |
| 11 | Ranking por localidad y datos de supercades | 63,823 | 18.3% |
| 12 | Cuadros comparativos, verificación final y cierre | 66,300 | 19.0% |
| **Total** | **12 segmentos** | **348,959** | **100%** |

### 2.4 Estimacion de Tokens Consumidos

Basado en estimaciones conservadoras:
- 750 tokens por imagen (frame JPEG 1024px)
- 30,000 tokens de contexto de proyecto por batch (constante)
- 2,000 tokens de prompt + transcript por batch
- 1,500 tokens de respuesta por batch

| Categoria | Por batch | Total | % del total |
|---|---|---|---|
| Imagenes (8,467 frames) | 75,000 | 6,350,250 | 67.8% |
| Contexto de proyecto | 30,000 | 2,700,000 | 28.8% |
| Prompt + transcript | 2,000 | 180,000 | 1.9% |
| Respuesta del modelo | 1,500 | 135,000 | 1.4% |
| **Total** | **~108,500** | **9,365,250** | **100%** |

### 2.5 Rendimiento por Batch

| Aspecto | Valor |
|---|---|
| Tiempo promedio por batch | 140s |
| Frames promedio por batch | 94 |
| Caracteres promedio por batch | 3877 |
| Tiempo por 1000 frames | 1491s |
| Eficiencia (chars/segundo) | 27.6 |

---

## 3. Comparativa: Transcripcion vs Analisis Visual

### 3.1 Volumen de Datos

| Fuente | Segmentos | Tamaño | Tipo de informacion |
|---|---|---|---|
| **Transcripcion** (Groq Whisper) | 1,222 | 63,912 caracteres | Texto hablado (dialogo, instrucciones verbales) |
| **Analisis visual** (gpt-5.4-mini) | 90 batches | 348,959 caracteres | Acciones en pantalla, celdas, menus, datos visibles |

### 3.2 Que Aporta Cada Fuente

**La transcripcion APORTA:**
- El dialogo completo de Yesenia explicando el proceso
- Instrucciones verbales paso a paso
- Justificacion de por que se hacen ciertas acciones
- Fechas, nombres de archivos, referencias a normativas (Decreto 371)
- Contexto sobre problemas comunes y soluciones

**El analisis visual APORTA:**
- Que libro/hoja de Excel esta abierto en cada momento
- Que celdas estan seleccionadas y que valores tienen
- Que acciones concretas se ejecutan (copiar, pegar, formula, filtro)
- Que menus y dialogos se abren
- La secuencia exacta de la interfaz de usuario
- Datos numericos visibles en pantalla (cifras de PQRS, porcentajes)

### 3.3 Estrategia de Combinacion Recomendada

Para la FASE 5 (sintesis), se recomienda:

1. **Usar la transcripcion como estructura narrativa**
   - Los timestamps de la transcripcion marcan el inicio/fin de cada paso
   - El dialogo explica el POR QUE de cada accion

2. **Usar el analisis visual para los detalles tecnicos**
   - Los frames muestran el COMO exacto de cada paso
   - Las tablas de Excel, formulas y datos numericos solo son accesibles via frames

3. **Correlacion temporal**
   - Transcripcion y analisis visual comparten timestamps (segundo exacto)
   - Para cada segmento de transcripcion, buscar el batch de analisis correspondiente
   - Cruzar referencias: "a las 5:30 dice X" + "en el frame 47 se ve Y"

4. **Priorizar precision visual sobre narrativa**
   - Si hay conflicto entre lo que se dice y lo que se ve, el frame es la fuente de verdad
   - La transcripcion puede tener errores de Whisper (acentos, nombres propios, cifras)

---

## 4. Intervencion Completa — Esta Sesion

### 4.1 Archivos Modificados/Creados

| Archivo | Accion | Proposito |
|---|---|---|
| `scripts/chatgpt-health.ps1` | Reparado | Leer .config/opencode/opencode.jsonc (no opencode.json) + usar providers list |
| `.config/opencode/skills/wafle-video-analysis/scripts/health.py` | Reparado | pwsh -> powershell |
| `.config/opencode/skills/wafle-video-analysis/scripts/config.py` | Reparado | parents[4] -> parents[5] |
| `.config/opencode/opencode.jsonc` | Reparado | Prompt del agente chatgpt-health-agent actualizado |
| `projects/SDG/src/analyze_segment.py` | Reescrito | De Groq-only a ChatGPT-first con vision en batches |
| `projects/SDG/data/analysis/seg*.json` | Creado (12) | Analisis multimodal de cada segmento |
| `projects/SDG/docs/*.md` | Creado (7) | Documentacion completa del proceso |
| `projects/SDG/README.md` | Actualizado | Estado actualizado del proyecto |

### 4.2 Resumen de Trabajo

- Health check de ChatGPT reparado y validado
- 4 modelos de vision probados (2 funcionales, 2 no)
- 12 segmentos de video analizados
- 8,467 frames procesados en 90 batches
- ~348,959 caracteres de documentacion generados
- 0 fallos en todo el proceso

---

## 5. Punto de Reanudacion para Proxima Sesion

### Proxima tarea: FASE 5 — Sintesis y Documentacion

**Objetivo:** Compilar los 12 analisis visuales + la transcripcion en un solo
documento estructurado que describa el proceso PQRS completo, paso a paso,
listo para ser automatizado.

**Archivos de entrada:**
- `data/analysis/seg001-*.json` a `seg012-*.json` (analisis visual)
- `data/transcript/transcript_completo.json` (transcripcion)
- `data/segments/segmentos.json` (definicion de segmentos)
- `assets/excel/` (bases de datos Excel originales)
- `docs/DOCUMENTACION_COMPLETA.md` (analisis ya compilado)

**Enfoque recomendado:**
1. Para cada segmento, leer el analisis JSON + la transcripcion en ese rango
2. Sintetizar en un unico documento: "Paso X: descripcion"
3. Incluir: accion, libro/hoja, celdas, formula, datos esperados, capturas clave
4. Identificar puntos exactos de automatizacion (repetitivo, manual, propenso a error)
5. Producir: DOCUMENTO_PROCEDIMIENTO_PQRS.md + PLAN_DE_AUTOMATIZACION.md

**Modelo a usar:** openai/gpt-5.4-mini via opencode run (confirmado funcional)

**Posibles problemas:**
- Groq keys siguen bloqueadas (403) — no usar como fallback por ahora
- Rate limit de ChatGPT Plus puede estar cerca del limite mensual
- wafle-video-analysis analyze.py tiene _call_chatgpt roto (flag --json inexistente)

### Comandos utiles para retomar

```bash
# Ver health check de ChatGPT
powershell -ExecutionPolicy Bypass -File scripts/chatgpt-health.ps1

# Ver modelos disponibles con vision
opencode models openai --verbose

# Ver progreso de analisis
Get-ChildItem projects/SDG/data/analysis/*.json | Select-Object Name, Length

# Ver documentacion
Get-ChildItem projects/SDG/docs/*.md | Select-Object Name, Length
```