# SDG — Secretaría Distrital de Gobierno

Automatización del proceso de generación de informes PQRS Localidades para la SDG.
Sistema híbrido: interfaz web local + backend ETL, datos NUNCA salen del PC.

## Estado del proyecto

```
FASE 0: Setup del proyecto                               [COMPLETADO]
FASE 1: Extracción de audio                              [COMPLETADO]
FASE 2: Transcripción Groq Whisper                       [COMPLETADO] - 1222 segmentos, 63,912 chars
FASE 3: Segmentación del contenido                       [COMPLETADO] - 12 segmentos
FASE 4: Análisis multimodal del video                    [COMPLETADO] - 8,467 frames, 0 fallos
FASE 5: Ingeniería inversa de Excel fuente               [COMPLETADO] - 7 archivos mapeados
FASE 6: Automatización - sdg-localidades (Flask local)   [COMPLETADO] - Puerto 5000
Otros 7 subproductos                                     [PENDIENTE]
```

## Estructura del proyecto

```
projects/SDG/
├── assets/                          # Archivos fuente originales
│   ├── video/                       # Video tutorial MP4 (698 MB)
│   ├── excel/                       # Bases de datos Excel (2 originales)
│   └── docs/                        # Documentación del proceso (DOCX)
├── data/                            # Datos generados durante el análisis
│   ├── audio/                       # Audio extraído + chunks
│   ├── transcript/                  # Transcripciones (VTT, JSON, TXT)
│   ├── segments/                    # Segmentación del contenido
│   └── analysis/                    # Análisis multimodal por segmento (12 JSONs)
├── src/                             # Scripts del pipeline de análisis
│   ├── transcribe_chunks.py         # Transcripción con Groq Whisper
│   └── analyze_segment.py           # Análisis multimodal v3 (SSIM, batch, slim prompt)
├── docs/                            # Documentación generada del análisis
│   ├── DOCUMENTACION_COMPLETA.md    # Análisis completo (365 KB)
│   ├── RESUMEN_EJECUTIVO.md         # Métricas y resumen
│   ├── HALLAZGOS_Y_APRENDIZAJES.md  # Hallazgos técnicos
│   ├── GROQ_ROLLING_ROBIN.md        # Patrón multi-key rotation
│   ├── AHORROS_Y_OPTIMIZACIONES.md  # Evidencia de optimizaciones
│   ├── OPTIMIZACIONES_v3_Y_EVOLUCION.md  # Optimización v3 (SSIM, batch, res)
│   ├── MEJORES_PRACTICAS.md         # Guía de mejores prácticas
│   ├── REPORTE_USO_GPT_Y_CIERRE_SESION.md  # Uso de GPT y punto de reanudación
│   └── ESTADO_DEL_PROYECTO.md       # Estado y próximos pasos
├── sdg-localidades/                 # ⚡ SISTEMA DE AUTOMATIZACIÓN
│   ├── engine/                      # Pipeline ETL completo
│   │   ├── ingest/                  # 6 lectores de archivos fuente
│   │   ├── transform/               # 5 módulos de transformación
│   │   └── load/                    # Generación Excel + validación 4 niveles
│   ├── webapp/                      # Interfaz Flask + Tailwind + SSE
│   ├── input/                       # Archivos fuente para procesar (7 Excel)
│   ├── output/                      # Excel generado por el sistema
│   ├── INICIAR.bat                  # Launcher Windows (doble clic)
│   ├── INICIAR.ps1                  # Launcher PowerShell
│   └── requirements.txt             # Dependencias Python
├── subproductos/                    # Automatizaciones independientes (pendiente)
├── protocol.md                      # Protocolo de análisis
└── README.md                        # Este archivo
```

## Sistema de Automatización: sdg-localidades

Aplicación web local que replica el proceso manual de 2h21min en minutos.

### Arquitectura

```
Usuario arrastra archivos → Interfaz Web (Flask + Tailwind)
                                    ↓
                            API REST / SSE
                                    ↓
                          Pipeline ETL (engine/)
                                    ↓
                         Excel de salida listo
```

### Archivos fuente que procesa (7)

| Archivo | Origen |
|---------|--------|
| BD PQRS BOGOTA TE ESCUCHA | Base principal - 12,911 peticiones |
| BASE DATOS PPT LOCALIDADES | Encuestas PPT (1M+ filas RAW) |
| SAC_atencion | Atención al Ciudadano |
| Resumen SIDE | Datos SIDE |
| PRODUCTIVIDAD_CR | Certificados de residencia |
| PRODUCTIVIDAD_PH | Propiedad horizontal |
| REPORTE PRODUCTIVIDAD ENCUESTAS | Encuestas de satisfacción |

### Pipeline ETL (engine/)

```
1. INGESTA       → 6 readers específicos por archivo
2. NORMALIZACIÓN → Estandariza localidades, fechas, formatos
3. DUPLICADOS    → Detecta PQRS duplicados (fórmula =A[n]=A[n+1])
4. TABLAS DINÁMICAS → Q1-Q6 para informe PPT
5. INDICADORES   → % participación, calificación proporcional
6. RESUMEN CIFRAS → Concentrado por localidad
7. EXCEL OUTPUT  → Formato profesional, Power BI compatible
8. VALIDACIÓN    → 4 niveles: entrada, transformación, vs original, verificación
```

### Cómo usar

```bash
cd sdg-localidades
# Opción 1: Doble clic en INICIAR.bat (Windows)
# Opción 2: PowerShell
.\INICIAR.ps1
# Opción 3: Manual
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python webapp\app.py
# Abrir http://localhost:5000
```

## Pipeline de análisis de video (completado)

### Modelo primario
- **gpt-5.4-mini** vía ChatGPT Plus / Codex — único modelo mini con visión funcional
- **8,467 frames** a 1fps, **100 batches**, 0 fallos
- **~10.8M tokens** (~75% imágenes, ~28% contexto proyecto)

### Optimización v3 aplicada
- SSIM frame dedup (79% reducción en segmentos con pocos cambios)
- Batch size: 100 → 200
- Resolución: 1024 → 768px (tile-optimal)
- Prompt inline delgado

### Proveedores verificados

| Modelo | Visión | Estado |
|--------|--------|--------|
| openai/gpt-5.4-mini | ✅ SÍ | PRIMARIO |
| openai/gpt-5.5 | ✅ SÍ | Fallback |
| Groq Llama 4 Scout | ❌ Bloqueado | Rate-limit (403) |
| HuggingFace Inference API | ❓ Potencial | No verificado |

## Decisiones de arquitectura

| Decisión | Opción elegida | Alternativas descartadas |
|----------|---------------|-------------------------|
| Tipo de app | Flask local (localhost:5000) | ❌ .exe PyInstaller (frágil, antivirus bloquea) |
| Datos | NUNCA salen del PC | ❌ Web hosteada (riesgo legal Ley 1581/2012) |
| Frontend | Tailwind + SSE progreso en vivo | ❌ React/Vue (overhead innecesario) |
| Servidor WSGI | Waitress | ❌ Flask dev server (producción) |
| Compatibilidad | Power BI ready (tablas planas) | — |

## Próximos pasos

1. ✅ Probar sdg-localidades con datos reales Mayo 2026
2. ✅ Pipeline produce Excel con validación 4 niveles OK
3. ✅ Validado contra Excel manual de Yesenia (Q1 20/20 localidades OK)
4. 🔲 Implementar otros 7 subproductos en `subproductos/`
5. 🔲 Documentación visual para Yesenia (guía de uso con capturas)
6. 🔲 Probar interfaz web: INICIAR.bat → http://localhost:5000

## Bugs corregidos (sesión 26-jun)

| Bug | Síntoma | Causa | Fix |
|-----|---------|-------|-----|
| Readers sin pandas | SAC, CR, PH, SIDE, Encuestas retornaban 0 filas | Faltaba `import pandas as pd` en cada reader | Agregado import |
| Columnas Unnamed | PQRS con 102 columnas llamadas `Unnamed: N` | El Excel tiene 9 filas de metadatos antes del header real | PQRSReader `header=9` |
| PivotGenerator sin datos | Q1-Q6 generaban 0 tablas | Buscaba keywords en columnas `Unnamed:` | Reesecrito con col. reales |
| Normalizer crash | AttributeError en columnas duplicadas | pandas devuelve DataFrame vs Series | Fix isinstance check |
| ResumenCifras en 0 | CR, PH, SIDE, Encuestas todo en cero | Extractor generico no manejaba cada formato | v3 con extractores específicos + unidecode |
| PH/SIDE en 0 | Inscripciones y registros sin datos | Usaba pivots mal formateados | v4 con datos crudos (BASE-I, BASE-A, REGISTRADO SIDE) |
| SAC buscaba hoja incorrecta | Warning `REGISTRO ATENCIONES` y solo 39 registros | Buscaba hoja que existe en PQRS, no en SAC | Ahora lee `Mayo SAC_atencion` (4,367 registros) |
| SSE sin progreso | UI no mostraba avance, botón girando siempre | Pipeline yieldaba eventos al final | yield inmediato tras cada `_emit()` |

## Validación contra Excel de Yesenia

Q1 (Total Solicitudes por Localidad): **20/20 localidades coinciden 100%** ✅

| Localidad | Fuente | Generado | Diff |
|-----------|--------|----------|------|
| BOSA | 244 | 244 | 0 ✅ |
| SUBA | 159 | 159 | 0 ✅ |
| KENNEDY | 157 | 157 | 0 ✅ |
| CIUDAD BOLIVAR | 133 | 133 | 0 ✅ |
| ENGATIVÁ | 133 | 133 | 0 ✅ |
| ... | ... | ... | ... |
| SUMAPAZ | 6 | 6 | 0 ✅ |

**RESUMEN CIFRAS**: 21/22 localidades con datos consolidados.
**Validación 4 niveles**: ✅ PASA - totales cuadran al 100%.
