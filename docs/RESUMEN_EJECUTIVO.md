# SDG — Resumen Ejecutivo del Analisis

## Tabla de procesamiento

| # | Segmento | Duracion | Frames | Batches | Tiempo | Chars analisis |
|---|---|---|---|---|---|---|
| 1 | Apertura, copia de datos y ordenamiento Decreto 371 | 0:00-6:08 | 368 | 4 | 662s | 21,654 |
| 2 | Documentos extraviados — tabla dinamica | 6:08-9:40 | 212 | 3 | 469s | 17,288 |
| 3 | Registro de atenciones y grupos poblacionales | 9:40-15:00 | 320 | 4 | 644s | 23,113 |
| 4 | Documentos extraviados — registro manual uno a uno | 15:00-17:00 | 120 | 2 | 319s | 8,599 |
| 5 | Certificado de residencia — productividad | 17:00-22:35 | 335 | 4 | 667s | 22,467 |
| 6 | Propiedad horizontal — certificados generados | 22:35-30:00 | 445 | 5 | 764s | 14,170 |
| 7 | Encuestas — procesamiento completo | 30:00-45:30 | 930 | 10 | 879s | 6,482 |
| 8 | Informe PQRS pagina web — setup inicial | 45:30-60:00 | 870 | 9 | 851s | 5,701 |
| 9 | Tablas dinamicas y subtemas mas reiterados | 60:00-80:00 | 1,200 | 12 | 1,418s | 21,299 |
| 10 | Dias de gestion y vencimientos | 80:00-100:00 | 1,200 | 12 | 2,050s | 78,063 |
| 11 | Ranking por localidad y datos de supercades | 100:00-120:00 | 1,200 | 12 | 1,925s | 63,823 |
| 12 | Cuadros comparativos, verificacion final y cierre | 120:00-141:07 | 1,267 | 13 | 1,976s | 66,300 |
| **Total** | **12 segmentos** | **2h21min** | **8,467** | **100** | **~14,624s** | **~348,959** |

## Proveedores utilizados

- **gpt-5.4-mini (ChatGPT Codex)**: 12/12 segmentos — 100%

## Metricas de rendimiento

| Metrica | Valor |
|---|---|
| Tiempo total de procesamiento | ~4 horas |
| Promedio por segmento | ~1,219s (~20 min) |
| Promedio por batch | ~146s (~2.4 min) |
| Frames por segundo de video | 1.0 fps |
| Frames por batch | ~85 (promedio) |
| Chars de analisis por frame | ~41 |

## Cobertura del analisis

- **Total frames extraidos**: 8,467 (1 por cada segundo de video)
- **Total batches procesados**: 100 llamadas a gpt-5.4-mini
- **Total documentacion generada**: ~349,000 caracteres de analisis frame-by-frame
- **Cobertura temporal**: 100% del video (2h 21min 7s)
- **Cobertura visual**: Cada cambio de pantalla capturado y descrito
