# SDG — Secretaría Distrital de Gobierno
## Documentación Completa del Proceso PQRS

*Generado: 2026-06-22T19:30:43Z*
*Video analizado: 2h 21min 7s | 12 segmentos | ~8,467 frames a 1fps*

---

## Segmento 1: Apertura, copia de datos y ordenamiento Decreto 371

| Campo | Valor |
|---|---|
| **Duración** | 0:00 - 6:08 |
| **Descripción** | Copia datos de Secretaría General a Excel PPT Localidades, inserta columna duplicados, ordena por Decreto 371, actualiza tablas dinámicas |
| **Frames analizados** | 368 |
| **Batches** | 4 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 663s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped by identical screen states:

- **Frames 1–2**: Microsoft Teams title slide for **“Trabajar Informes PQRS Localidades y sitio WEB”**. Date shown: **2026-06-08 19:46 UTC**. Recorded/organized by **Yesenia Patino Figueroa**.

- **Frames 3–4**: Black Teams screen with centered profile avatar and name **Yesenia Patino Figueroa**.

- **Frames 5–9**: Teams in browser (`teams.microsoft.com/v2/`), waiting room / screen share state. Visible text: **“Esperando a que se unan otros usuarios…”** and sharing banner **“teams.microsoft.com está compartiendo tu pantalla”** with **“Dejar de compartir”**. Small previews show Excel windows.

- **Frames 10–27**: Excel workbook **“INFORME PORS SECRETARIA DE GOBIERNO MAYO 2026 - Excel”**. Sheet visible: **Hoja1**.  
  - Top-left report text:
    - **Gestión de Peticiones**
    - **Fecha de generación de reporte: 2026-06-01**
    - **Fecha Inicial: 2026-05-01**
    - **Fecha Final: 2026-05-31**
    - **Tipo de estado: Al periodo**
  - Table headers visible include **Número petición**, **Sector**, **Tipo de Entidad**, **Entidad**, **Tema**, **Subtema**, **Función**, **Estado**, **Punto**, **Canal**, etc.  
  - Sample visible values: **SECRETARIA DISTRITAL DE GOBIERNO**, **OFICINA DE ATENCION A LA CIUDADANIA**, **WEB SERV**, **DERECHO**, **QUEJA**.  
  - Selection/cursor moves within the table; no major content change yet.

- **Frames 28–55**: Switch to workbook **“BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel”**. Bottom tabs visible: **CERT RESIDENCIA PROD-ABRIL**, **CERT.P.HORIZONTAL ABRIL**, **REGISTRADO SIDE**, **Reporte PQRS Mayo2026**, **INF Localidades PPT**, **RESUMEN CIFRAS**.  
  - Active sheet: **Reporte PQRS Mayo2026**.  
  - Same PQRS table shown; rows and columns are being reviewed.  
  - Later in this block, the view is scrolled farther down / farther right, showing later rows and status-like values such as **Recibida**, **Registrada**, **PERIODO ACTUAL**, **Pendiente 0-3**, **PENDIENTE**.

- **Frames 56–60**: A new column has been inserted between **Número petición** and **Sector**.  
  - New header visible: **Duplicado**.  
  - Action: preparing a duplicate-flag column.  
  - Sheet remains **Reporte PQRS Mayo2026**.

- **Frames 61–67**: Still in the same workbook/sheet, now clearly on the table with **Duplicado** inserted.  
  - The user is preparing the logic for duplication detection.  
  - No dialog yet; focus remains on the data grid.

- **Frames 68–82**: Excel **Sort** dialog (**“Ordenar”**) is open.  
  - Sort levels visible:
    1. **Ordenar por: Número petición** → **De menor a mayor**
    2. **Luego por: Dependencia hija / Dependencia** → **A a Z**
    3. **Luego por: Transacción entidad** → **De mayor a menor**
  - User clicks through the dropdown list to choose the third field.  
  - Frame 82: **Aceptar** is clicked to apply the sort.

- **Frames 83–95**: Sort applied; back to the worksheet.  
  - The table is now reordered.  
  - Column **Duplicado** remains in place.  
  - Visible petition numbers repeat in grouped blocks, consistent with sorting.  
  - Workbook still **BASE DATOS PPT LOCALIDADES MAYO 2026** / sheet **Reporte PQRS Mayo2026**.

- **Frames 96–100**: User starts entering the duplicate-check formula in the new **Duplicado** column.  
  - The formula being typed is the adjacent-row comparison used to mark duplicates, consistent with **`=A10=A11`** (or equivalent row-to-row petition comparison).  
  - Intended result: **TRUE** = duplicated, **FALSE** = unique.  
  - The formula is not yet filled down across the column in these frames.

If you want, I can turn this into a cleaner **shot-by-shot timeline table** with columns: **frame(s) / workbook / selected cells / action / visible text**.

[Batch 2 - gpt-5.4-mini]
I grouped near-identical frames; the visible state changes only at the transitions below.

### Frames 101–116
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026` → tab `Reporte PQRS Mayo2026`
- **Selected/edited range:** duplicate-check column **B**; active cell around `B11/B12`
- **Action:** inserting/using a **duplicate flag** column
- **Visible values:**  
  - Title: `Gestión de Peticiones`
  - Report dates: `Fecha de generación de reporte: 2026-06-01`, `Fecha Inicial: 2026-05-01`, `Fecha Final: 2026-05-31`, `Tipo de estado: Al periodo`
  - Headers include: `Número petición`, `Duplicado`, `Sector`, `Tipo de Entidad`, `Tipo de Dependencia`, `Tema`, `Categoria`, `Subtema`, `Funcionario`, `Estado`, `Punto`, `Canal`, `Tipo petic`, `Estado pe`, `Estado de`, `Asunto`
  - Duplicate column shows **`FALSO` / `VERDADERO`**
  - Formula bar shows a comparison formula like **`=A10=A11`** (duplicate test)
  - Rows visible with values like `GOBIERNO ENTIDAD DE SECRETARIA DISTRITAL DE GOBIERNO`, `OFICINA DE ATENCION A LA CIUDADANIA`, `SANDRA V`, `Activo`, `WEB`, `DERECHO`, `Notificado`, `Cerrado`
- **Open windows/menus:** Excel ribbon; Teams sharing banner (`teams.microsoft.com está compartiendo tu pantalla`); speaker bubble `Yesenia Patino Figueroa`

### Frames 117–132
- **Workbook/sheet:** same workbook → tab `INF Localidades PPT`
- **Selected/edited range:** pivot table area around `B14` and the pivot fields pane
- **Action:** viewing the **first pivot table** and opening **Change Data Source** for refresh
- **Visible values:**  
  - Slide title: `PREGUNTA No. 1`
  - Prompt: `Número de solicitudes recibidas, ingresadas y registradas.`
  - Pivot rows: `ALCALDIA LOCAL DE ANTONIO NARIÑO`, `BARRIOS UNIDOS`, `BOSA`, `CANDELARIA`, `CHAPINERO`, `CIUDAD BOLIVAR`, `ENGATIVA`, `FONTIBON`, `KENNEDY`, `MARTIRES`, `PUENTE ARANDA`, `RAFAEL URIBE`, `SAN CRISTOBAL`, `SANTA FE`, `SUBA`, `SUMAPAZ`, `TUNJUELITO`, `USAQUEN`, `USME`
  - **Total general: 1678**
  - Fields pane shows checked fields like `Número petición`, `Dependencia`, `Tipo de ingreso`, `Periodo`
- **Open windows/menus:** `Campos de tabla dinámica`; later `Cambiar origen de datos de tabla dinámica`

### Frames 133–136
- **Workbook/sheet:** back to `Reporte PQRS Mayo2026`
- **Selected/edited range:** source-data range in the **Change Pivot Data Source** dialog; sheet scroll is deep into the dataset
- **Action:** selecting/confirming the pivot source range
- **Visible values:**  
  - Dialog title: `Cambiar origen de datos de tabla dinámica`
  - Source field points to a range beginning on the report sheet (starts around `Reporte PQRS Mayo2026!$A$10...`)
  - Sheet is scrolled to rows around **12884–12913**
  - Late columns visible: `BZ`, `CA`, `CB`, `CC`, `CD`, `CE`, etc.
  - Values visible include `Recibida`, `Registrado`, `Por el distrito`, `PERIODO ACTUAL`, `Pendiente 0-3`, `PENDIENTE`
- **Open windows/menus:** the pivot source dialog remains open

### Frames 137–142
- **Workbook/sheet:** `INF Localidades PPT`
- **Selected/edited range:** pivot table for Q1, then moving downward to Q2
- **Action:** refreshed pivots / navigating between questions
- **Visible values:**  
  - Q1 still shows **Total general 1678**
  - Q2 title appears: `Número de Solitudes de Información Recibidas`
  - Q2 filter shows `Tipo de ingreso` and `Tipo petición: SOLICITUD DE ACCESO A LA INFORMACION`
  - Example locality counts visible: `ALCALDIA LOCAL DE BOSA 4`, `CANDELARIA 4`, `CIUDAD BOLIVAR 2`, etc.
- **Open windows/menus:** `Campos de tabla dinámica`

### Frames 143–156
- **Workbook/sheet:** `INF Localidades PPT`
- **Selected/edited range:** pivot tables for Q2 and Q3
- **Action:** navigating the questions and reviewing calculated values
- **Visible values:**  
  - Q2 total visible: **15**
  - Q3 title: `Cuál es el tiempo de respuesta de cada Solicitud`
  - Q3 filters: `Tipo de ingreso`, `Estado petición final: Solucionado - Por respuesta definitiva`
  - Q3 table compares `PERIODO ACTUAL` vs `PERIODO ANTERIOR`
- **Open windows/menus:** pivot fields pane stays open; no modal dialog

### Frames 157–168
- **Workbook/sheet:** same workbook, `INF Localidades PPT`
- **Selected/edited range:** Q3 → Q4 → Q5
- **Action:** reviewing later KPI pivots
- **Visible values:**  
  - Q4 title: `Número de solicitudes cerradas`
  - Q4 total general visible: **914**
  - Q5 title: `Número de solicitudes trasladadas`
  - Q5 total general visible: **82**
  - Q5 locality counts visible: `ALCALDIA LOCAL DE BOSA 24`, `CANDELARIA 3`, `CIUDAD BOLIVAR 3`, `FONTIBON 13`, `KENNEDY 15`, `MARTIRES 3`, `PUENTE ARANDA 1`, `RAFAEL URIBE 1`, `SAN CRISTOBAL 7`, `SUBA 17`, `TUNJUELITO 1`, `USME 2`
- **Open windows/menus:** pivot fields pane; no dialog

### Frames 169–193
- **Workbook/sheet:** alternating between `Reporte PQRS Mayo2026` and `INF Localidades PPT`
- **Selected/edited range:** pivot source dialog over the data sheet; then pivots on the report sheet
- **Action:** continuing pivot refresh / source confirmation
- **Visible values:**  
  - Source dialog again: `Cambiar origen de datos de tabla dinámica`
  - Data sheet shows the same large records table with duplicate flags and many columns
  - Pivot sheet shows Q4/Q5 still in view
- **Open windows/menus:** repeated pivot source dialog, `Campos de tabla dinámica`

### Frames 194–200
- **Workbook/sheet:** `INF Localidades PPT`
- **Selected/edited range:** Q6 area and the chart on `DIAPOSITIVA No. 3`
- **Action:** viewing the last KPI and the chart output
- **Visible values:**  
  - Q6 title: `Cuál es el número de Solicitudes en las que se negó la información`
  - Q6 total general visible: **128**
  - Chart label: `GRAFICA No. 1 - DIAPOSITIVA No. 3`
  - Bar chart categories and counts visible:
    - `DERECHO DE PETICION DE INTERES GENERAL` — **114**
    - `DERECHO DE PETICION DE INTERES PARTICULAR` — **8**
    - `QUEJA` — **3**
    - `RECLAMO` — **3**
- **Open windows/menus:** pivot fields pane; chart visible; Teams sharing banner still present

If you want, I can turn this into a **clean frame-by-frame table** with one row per transition.

[Batch 3 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped where the screen state is unchanged:

| Frames | Visible workbook / sheet | Selection / edit area | Action | Readable values / text | Open menus / dialogs |
|---|---|---|---|---|---|
| 201-202 | **BASE DATOS PPT LOCALIDADES MAYO 2026**; tab **INF Localidades** | Name box shows **B188**; pivot table area on the left | Inspecting a pivot summary | Pivot counts by petition type; **Total general 128**. Readable rows include **DERECHO DE PETICION DE INTERES GENERAL 114**, **DERECHO DE PETICION DE INTERES PARTICULAR 8**, **QUEJA 3**, **RECLAMO 2**, **SOLICITUD DE ACCESO A LA INFORMACION 1** | Right pane **Campos de tabla dinámica**; Teams share overlay visible |
| 203-204 | Same workbook; tab **Reporte PQRS Mayo2026** | Name box shows **A10**; source data table behind dialog | Changing pivot source | Data table headers visible: **Número petición, Duplicados, Sector, Tipo de entidad, Entidad, Tipo de dependencia, Dependencia** | Dialog **Cambiar origen de datos de tabla dinámica** open |
| 205-211 | Same workbook; back on **INF Localidades** | Name box shows **B210** | Pivot refresh / review | Updated pivot shows **Total general 95**; rows readable as **DERECHO DE PETICION DE INTERES GENERAL 80**, **DERECHO DE PETICION DE INTERES PARTICULAR 12**, **CONSULTA 1**, **SOLICITUD DE ACCESO A LA INFORMACION 1**, **RECLAMO 1** | **Campos de tabla dinámica** pane open; chart centered; Teams overlay still present |
| 212-231 | Same workbook; scrolled to **DIAPOSITIVA No. 4** / **Certificados de Propiedad Horizontal** | Pivot/chart area and locality table | Reviewing the next report block | Locality table and chart visible; totals and bars for the same petition categories; lower section title **Certificados de Propiedad Horizontal** appears, with filter **Subtema: LEY 675 CERTIFICADO DE PROPIEDAD HORIZONTAL** | Right pivot pane remains open; chart and pivot table visible together |
| 232-244 | Same workbook; tab **RESUMEN CIFRAS** | Large summary grid, starting around row 4 | Switching to the summary sheet | Big matrix by locality. Columns include **PQRS GESTIONADAS N.1**, **PQRS PENDIENTES N.2**, **DOC.EXT. N.3**, **ORIENTACIONES No. 4**, **CERT. PROPIEDAD No. 5**, **CERT. RESIDENCIA No. 6**, **ENCUESTAS DEL PERIODO**, **ENCUESTAS CON RESPUESTA COMPLETA**, **CALIFICACIÓN…**, **% PARTICIPACIÓN…**. Totals row visible: **9.534 / 1.203 / 591 / 3.120 / 470 / 7.941 / 5.220 / 3.819** | No dialog; just sheet navigation |
| 245-255 | Same **RESUMEN CIFRAS** sheet | Same table, different horizontal position | Horizontal review / inspection | Same locality rows and totals remain visible; no data entry apparent | None |
| 256-267 | Same workbook; **RESUMEN CIFRAS** visible but mostly blank in the viewed region | Empty-looking grid area | Scrolling / repositioning view | Only headers / grid lines visible in the current viewport | None |
| 268-275 | Back to **INF Localidades PPT** | Yellow pivot table selected | Reviewing locality pivot | Title **Solicitudes Gestionadas y Solicitudes en Trámite**; filters show **Tipo de ingreso (Todas)** and **Periodo PERIODO ACTUAL**. Total row shows **9431** and **1168**. Locality counts visible, e.g. **ANTONIO NARIÑO 9 / 29**, **BARRIOS UNIDOS 13 / 19**, **BOSA 166 / 59**, **CANDELARIA 113 / 34**, etc. | **Campos de tabla dinámica** pane on the right |
| 276-280 | Same sheet | Hover/selection over pivot cells | Inspecting a cell value | Tooltip shows **Cuenta de Número petición**, value **13**, for **ALCALDÍA LOCAL DE BARRIOS UNIDOS** | Tooltip over selected pivot cell |
| 281-285 | Same sheet | Selection stays in the yellow pivot table | Continued inspection | Same locality counts remain visible; no data change | None |
| 286-287 | Same sheet | Selected pivot range | Context action / possible copy/sort attempt | No new values; same table visible | Right-click context menu open: **Cortar, Copiar, Opciones de pegado, Insertar celdas…, Eliminar…, Borrar contenido, Ordenar, Filtrar, Obtener datos de Tabla/Rango…, Formato de celdas…** |
| 288-297 | Same sheet | Pivot range highlighted again | Navigation after closing menu | Same yellow locality summary remains; no edit executed | Context menu closed; pivot pane still on right |
| 298-300 | Same sheet | Hover on the pivot table | Final inspection | Tooltip again shows a cell value in the locality summary; frame 300 highlights **CANDELARIA** with value **13** in the managed-count column | Pivot fields pane still open; Teams overlay still visible |

### What this segment shows overall
- The user is **refreshing and validating pivot tables** after copying the monthly PQRS source data into the workbook.
- The workflow includes **changing the pivot source**, **reviewing the summary sheets**, and **checking locality-level totals**.
- No explicit data entry is visible in these frames; this is mostly **navigation, refresh, inspection, and pivot interaction**.

If you want, I can turn this into a **clean narrated timeline** for the whole 6:40–6:08 segment.

[Batch 4 - gpt-5.4-mini]
A continuación, por frame:

- **301** — Excel **BASE DATOS PQR LOCALIDADES MAYO 2026**. Hoja **INF Localidades PPT**. Selección en la tabla dinámica (name box **A209**; fórmula/barra muestra **ALCALDIA LOCAL DE CANDELARIA**). Acción: revisión de la tabla dinámica “**Solicitudes Gestionadas y Solicitudes en Trámite**”. Valores visibles: total general **9431** gestionados y **1168** pendientes. Pane derecho **Campos de tabla dinámica** abierto; barra de Teams compartiendo pantalla visible.

- **302** — Misma vista que 301. Misma hoja **INF Localidades PPT**. Sin cambio relevante; tabla dinámica y panel de campos abiertos.

- **303** — Misma vista que 301. Sin cambio visible.

- **304** — Misma vista que 301. Sin cambio visible.

- **305** — Misma vista que 301. Sin cambio visible.

- **306** — Misma vista que 301. Sin cambio visible.

- **307** — Misma vista que 301. Sin cambio visible.

- **308** — Misma vista que 301. Sin cambio visible.

- **309** — Misma vista que 301. Sin cambio visible.

- **310** — Misma vista que 301. Sin cambio visible.

- **311** — Misma vista que 301. Sin cambio visible.

- **312** — Cambio a hoja **RESUMEN CIFRAS**. Excel **BASE DATOS PQR LOCALIDADES MAYO 2026**. Se ve la tabla “**DIAPOSITIVA No. 3**”. Selección en **A7** (barra muestra **CANDELARIA**). Acción: visualización de resumen consolidado. Valores visibles: **ANtonio Nariño 9/29**, **Barrios Unidos 13/19**, **Bosa 166/59**, **Candelaria 113/34**, **Chapinero 18/23**, **Ciudad Bolívar 37/26**, **Engativá 41/37**, **Fontibón 55/59**, **Kennedy 69/46**, **Mártires 7/7**, **Puente Aranda 21/10**, **Rafael Uribe 49/35**, **San Cristóbal 52/28**. Barra de Teams visible.

- **313** — Misma hoja **RESUMEN CIFRAS**, desplazada hacia abajo. Se ven filas **Ciudad Bolívar, Engativá, Fontibón, Kennedy, Mártires, Puente Aranda, Rafael Uribe, San Cristóbal, Santa Fe, Suba, Sumapaz, Teusaquillo, Tunjuelito, Usaquén, Usme**. Acción: revisión/scroll del resumen.

- **314** — Misma hoja, más abajo. Se ven filas **Mártires → Usme** y comienza la sección inferior con **NIVEL CENTRAL**, **SUPERCADES**, **EN BLANCO**. Acción: scroll.

- **315** — Misma hoja, parte inferior visible. Se alcanzan a ver **NIVEL CENTRAL**, **SUPERCADES**, **EN BLANCO** y **TOTAL GENERAL**. Acción: inspección del cierre de la tabla.

- **316** — Misma hoja, fondo inferior. Visible **TOTAL GENERAL 947** en una columna y **671** en la otra. Acción: verificación de totales.

- **317** — Misma vista que 316. Sin cambio visible.

- **318** — Misma vista que 316. Sin cambio visible.

- **319** — Misma vista que 316. Sin cambio visible.

- **320** — Misma hoja **RESUMEN CIFRAS**. Parte inferior de la tabla, con selección/cursor en zona media-baja. Se mantiene el total **947 / 671**. Acción: inspección de celdas inferiores.

- **321** — Misma vista que 320. Sin cambio visible.

- **322** — Misma vista que 320. Sin cambio visible.

- **323** — Misma vista que 320. Sin cambio visible.

- **324** — Misma vista que 320. Sin cambio visible.

- **325** — Misma vista, cursor sobre la parte inferior de la tabla. Acción: revisión de filas finales.

- **326** — Misma vista que 325. Sin cambio visible.

- **327** — Misma vista que 325. Sin cambio visible.

- **328** — Misma vista que 325. Sin cambio visible.

- **329** — Misma vista que 325. Sin cambio visible.

- **330** — Misma vista que 325. Sin cambio visible.

- **331** — Misma vista que 325. Sin cambio visible.

- **332** — Misma vista que 325. Sin cambio visible.

- **333** — Misma vista que 325. Sin cambio visible.

- **334** — Misma vista que 325. Sin cambio visible.

- **335** — Misma vista que 325. Sin cambio visible.

- **336** — Misma vista que 325. Sin cambio visible.

- **337** — Misma vista que 325. Sin cambio visible.

- **338** — Misma vista que 325. Sin cambio visible.

- **339** — Misma vista que 325. Sin cambio visible.

- **340** — Misma hoja, parte inferior visible. Acción: inspección de totales y filas finales.

- **341** — Misma hoja. Se aprecia la barra de estado con agregados de selección (promedio/recuento/suma). Acción: revisión de un valor seleccionado en la tabla.

- **342** — Misma vista que 341. Sin cambio visible.

- **343** — Misma vista que 341. Sin cambio visible.

- **344** — Misma hoja **RESUMEN CIFRAS**. Se ve claramente **NIVEL CENTRAL** con valor **8484** en la columna gestionadas. Acción: revisión de celda en la fila de control.

- **345** — Misma vista que 344. Sin cambio visible.

- **346** — Misma vista que 344. Sin cambio visible.

- **347** — Misma vista que 344. Sin cambio visible.

- **348** — Misma vista que 344. Sin cambio visible.

- **349** — Misma hoja, parte inferior. Se ve **TOTAL GENERAL 9.431** en la columna gestionadas. Acción: verificación de total acumulado.

- **350** — Misma vista que 349. Se ve **9.431** y **1.168** en la fila **TOTAL GENERAL**. Acción: verificación de totales.

- **351** — Misma hoja. Aparece tooltip de pivot: **“Cuenta de Número petición”**, **Value: 84**, **Row: DEPENDENCIAS NIVEL CENTRAL**, **Column: PENDIENTE**. Acción: inspección de celda de tabla dinámica.

- **352** — Misma vista que 351. Sin cambio visible.

- **353** — Misma vista que 351. Sin cambio visible.

- **354** — Misma vista que 351. Sin cambio visible.

- **355** — Misma vista que 351. Sin cambio visible.

- **356** — Misma vista que 351. Sin cambio visible.

- **357** — Misma vista que 351. Sin cambio visible.

- **358** — Misma vista que 351. Sin cambio visible.

- **359** — Misma vista que 351. Sin cambio visible.

- **360** — Misma vista que 351. Sin cambio visible.

- **361** — Misma hoja. Se ve **NIVEL CENTRAL 8484** y la parte inferior de la tabla. Acción: validación del dato del resumen.

- **362** — Misma vista que 361. Sin cambio visible.

- **363** — Misma vista que 361. Sin cambio visible.

- **364** — Misma vista que 361. Sin cambio visible.

- **365** — Misma hoja. Se observa edición/selección en la celda inferior del resumen; aparece **497** en la fila **NIVEL CENTRAL** (zona de la columna siguiente a 8484). Acción: corrección/verificación manual de valor.

- **366** — Misma hoja. La fila inferior muestra **TOTAL GENERAL** con **1.168** en la columna de pendientes. Acción: confirmación del total final.

- **367** — Misma vista que 366. Sin cambio visible.

- **368** — Misma hoja. Parte inferior con **NIVEL CENTRAL**, **SUPERCADES**, **EN BLANCO** y **TOTAL GENERAL**; se mantienen visibles **9.431** y **1.168**. Acción: cierre de la revisión del resumen.

Si quieres, te lo convierto ahora en una **tabla CSV/Excel-friendly** con columnas: `frame, workbook, sheet, selection, action, values, windows`.

---

## Segmento 2: Documentos extraviados — tabla dinámica

| Campo | Valor |
|---|---|
| **Duración** | 6:08 - 9:40 |
| **Descripción** | Inserta tabla dinámica en registro CIDE, filtra 'no aplica', mueve/copia hoja a PQR localidades |
| **Frames analizados** | 212 |
| **Batches** | 3 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 469s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
I verified the frames. Here’s the exact screen-by-screen readout, grouped where the view is effectively the same:

| Frames | Workbook / sheet | Selection / action | Visible data | Menus / windows |
|---|---|---|---|---|
| 1–3 | **BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel** / **RESUMEN CIFRAS** | Viewing the summary sheet; active cell changes in the lower table (e.g. B25/D25/D23 as the screen shifts slightly) | Table titled **DIAPOSITIVA No. 3**. Headers: **ALCALDÍA LOCAL**, **PQRS GESTIONADAS N.1**, **PQRS PENDIENTES N.2**, **DOC.EXT. N.3**, **ORIENTACIONES No.4**, **CERT. PROPIEDAD No.5**, **CERT. RESIDENCIA No.6**, **ENCUESTAS DEL PERIODO**, **ENCUESTAS CON RESPUESTA COMPLETA**, **CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS**, **% PARTICIPACIÓN...**. Bottom totals visible: **TOTAL GENERAL 9.431** and **1.168**. | Excel ribbon visible; Teams share bar on top-right (“Dejar de compartir / Ocultar”). |
| 4–6 | Same workbook / **RESUMEN CIFRAS** | Horizontal/vertical scroll to different column groups | Localities visible in rows (e.g. **BOSA, CANDELARIA, CHAPINERO, CIUDAD BOLÍVAR, ENGATIVÁ, FONTIBÓN, KENNEDY, MARTÍRES, PUENTE ARANDA, RAFAEL URIBE, SAN CRISTÓBAL, SUBA, SUMAPAZ**). Many cells still blank. | Same Excel + Teams share bar. |
| 7–10 | Same workbook / **RESUMEN CIFRAS** | Left-side columns shown again; no new edit yet | Counts visible in **PQRS GESTIONADAS** / **PQRS PENDIENTES**: **ANTONIO NARIÑO 9 / 29**, **BARRIOS UNIDOS 13 / 19**, **BOSA 166 / 59**, **CANDELARIA 113 / 34**, **CHAPINERO 18 / 23**, **CIUDAD BOLÍVAR 37 / 26**, **ENGATIVÁ 41 / 37**, **FONTIBÓN 55 / 59**, **KENNEDY 69 / 46**, **MÁRTIRES 7 / 7**, **PUENTE ARANDA 21 / 10**, **RAFAEL URIBE 49 / 35**, **SAN CRISTÓBAL 52 / 28**, **SUBA 70 / 75**, **SUMAPAZ 6 / 3**. | Same Excel + Teams share bar. |
| 11–18 | Same workbook / **RESUMEN CIFRAS** | Scrolled right to later columns; mostly empty cells | Headers in view: **DOC.EXT.**, **ORIENTACIONES**, **CERT. PROPIEDAD**, **CERT. RESIDENCIA**, **ENCUESTAS DEL PERIODO**, **ENCUESTAS CON RESPUESTA COMPLETA**, **CALIFICACIÓN...**, **% PARTICIPACIÓN...**. No values entered yet in these columns. | Same Excel + Teams share bar. |
| 19–30 | Same workbook / **RESUMEN CIFRAS** | Continued horizontal inspection of the same table | Same summary table; right-side columns remain blank in most rows. The screen is being positioned for data entry / verification. | Same Excel + Teams share bar. |
| 31–36 | Same workbook / **RESUMEN CIFRAS** | Editing starts in the **ANTONIO NARIÑO** row | A value appears under **ENCUESTAS DEL PERIODO** for Antonio Nariño: first visible as **6**, then corrected/updated to **65**. | Excel active; share bar still present. |
| 37–44 | Same workbook / **RESUMEN CIFRAS** | Further cell edits in the same row | **ENCUESTAS CON RESPUESTA COMPLETA** becomes **60** for Antonio Nariño. | Same. |
| 45–48 | Same workbook / **RESUMEN CIFRAS** | Another cell edit in the Antonio Nariño row | **CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS** shows **4,5**. | Same. |
| 49–50 | Same workbook / **RESUMEN CIFRAS** | Final value typed for the row | **% PARTICIPACIÓN DE PERCEPCIÓN Y SATISFACCIÓN X LOCALIDAD** shows **85%**. | Same. |
| 51–66 | Same workbook / **RESUMEN CIFRAS** | Verification pass; no visible new edits | The filled Antonio Nariño row is now visible across the right-side columns: **65**, **60**, **4,5**, **85%**. | Same. |
| 67–69 | Same workbook / **RESUMEN CIFRAS** | Cell/range selection changes; status bar calculation visible | Excel status bar shows aggregate stats for the selected cells (e.g. **Promedio 62,5 / Suma 125 / Recuento 2** when **65** and **60** are selected). | Same. |
| 70–79 | Same workbook / **RESUMEN CIFRAS** | Scroll back to left/mid columns; inspection of loaded data | Left/mid table values remain the same; no new numbers entered. | Same. |
| 80 | File Explorer | Switch away from Excel | Explorer opens in **REPORTES SDQS SECRETARIA GENERAL** folder. | Windows File Explorer open. |
| 81 | File Explorer | Navigate to parent folder | Folder **SECGOB** visible. | File Explorer. |
| 82 | File Explorer | Browse folders list | Shows folders like **ACTAS**, **ACTIVOS DE LA INFORMACIÓN**, **BASE ATENCIÓN COMUNITADOR**, **BASE DOCUMENTOS EXTRAVIADOS**, **BASE ENCUENTAS DE PERCEPCIÓN**, etc. | File Explorer. |
| 83 | File Explorer | Select folder | **BASE DOCUMENTOS EXTRAVIADOS** highlighted. | File Explorer. |
| 84 | File Explorer | Enter folder | Inside **BASE DOCUMENTOS EXTRAVIADOS**; year folders visible (**2020–2026**). | File Explorer. |
| 85 | File Explorer | Select year folder | **2026** highlighted. | File Explorer. |
| 86 | File Explorer | Open 2026 folder | Files visible including **Resumen SIDE Abril 2026**, **Resumen SIDE Enero 2026**, **Resumen SIDE Febrero 2026**, **Resumen SIDE Marzo 2026**, **Resumen SIDE Mayo 2026**. | File Explorer. |
| 87 | File Explorer | Select workbook | **Resumen SIDE Mayo 2026** highlighted. | File Explorer. |
| 88–91 | Back to Excel | Return to the summary workbook / active selection moves again | **BASE DATOS PPF LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** reappears; left columns with PQRS counts visible again. | Excel + Teams share bar. |
| 92–95 | **Resumen SIDE Mayo 2026** (shown as **Vista protegida**) / **REGISTRADO SIDE** | Workbook opens; table view loaded | Left pivot-style table: **Tipo de Documento / Total**. Readable totals: **Cédula de ciudadanía 1538**, **Cédula de extranjería 3**, **Libreta Militar 13**, **Licencia de conducción 78**, **Licencia de Tránsito 36**, **Pasaporte 3**, **Permiso Protección Temporal 1**, **Tarjeta de conducción servicio militar 2**, **Tarjeta de identidad 42**, **Tarjeta Profesional 7**, **Total general 1723**. Right side shows detail table with headers like **Año**, **Mes**, **LOCALIDAD**, **ORIGEN**, **RADICADO**, **FECHA RADICADO**. | Protected View banner: **“VISTA PROTEGIDA”** with **Habilitar edición**. Excel tabs visible: **STOCK 31052026**, **REGISTRADO SIDE**, **ENTREGADO SIDE**. |
| 96–100 | Same workbook / **REGISTRADO SIDE** | Horizontal scroll to the far right; cell selection in helper area | A second table is visible with headers like **LICENCIA DE TRÁNSITO**, **PASAPORTE**, **R PROTECCIÓN**, **TARJETA DE CONDUCTA**, **TARJETA DE IDENTIDAD**, **TARJETA PROFESIONAL**, **TOTAL**. Readable top values include **73**, **4**, **15**, **4**, **339**, **10**, **2579**. Far-right helper columns contain text like **S VALE** and **NA GUZ** plus comma-separated lists in the formula bar (e.g. **3418, 28, 29, 32, 33, 34, 35, 44, 47, 49**). | Excel still in protected view / normal view mix; tabs **STOCK 31052026**, **REGISTRADO SIDE**, **ENTREGADO SIDE** visible. |

Main transition points:
- **Frames 1–79:** summary workbook **BASE DATOS PPF LOCALIDADES MAYO 2026**, sheet **RESUMEN CIFRAS**, with progressive data entry and verification.
- **Frames 80–87:** Windows Explorer navigation to locate the source workbook in **BASE DOCUMENTOS EXTRAVIADOS → 2026 → Resumen SIDE Mayo 2026**.
- **Frames 92–100:** source workbook opens as **Resumen SIDE Mayo 2026**, sheet **REGISTRADO SIDE**, showing the document-type totals and detailed records.

[Batch 2 - gpt-5.4-mini]
Aquí va el análisis por secuencia de frames.

### 101–107
- **Libro/hoja:** `Resumen SIDE Mayo 2026 - Excel`, hoja activa `REGISTRADO SIDE`.
- **Selección:** se ve la tabla origen en columnas aprox. `R:U` y filas 1–24; no hay diálogo abierto.
- **Acción:** revisión de la tabla base antes de crear la dinámica.
- **Datos visibles:** encabezados `PROTECCIÓN`, `TARJETA DE CONDUCTA`, `TARJETA DE IDENTIDAD`, `TARJETA PROFESIONAL`, `TOTAL`; valores como `2579`, `497`, `30`, `70`, `58`, `1723`.
- **Ventanas:** barra de Teams compartiendo pantalla; sin modales de Excel.

### 108
- **Libro/hoja:** mismo libro, `REGISTRADO SIDE`.
- **Selección:** rango de datos resaltado para origen de tabla dinámica.
- **Acción:** se abre **Insertar > Crear tabla dinámica**.
- **Datos:** el rango fuente empieza en `REGISTRADO SIDE!$D$1...` (visible parcialmente).
- **Ventanas:** diálogo **Crear tabla dinámica**.

### 109–121
- **Libro/hoja:** `Resumen SIDE Mayo 2026 - Excel`, `REGISTRADO SIDE`.
- **Selección:** en el diálogo se fija el **rango de tabla** y la **ubicación** en hoja existente.
- **Acción:** configuración de la tabla dinámica.
- **Datos/rango:** fuente visible como `REGISTRADO SIDE!$D$1:$U$23` (aprox.); ubicación `REGISTRADO SIDE!$X$3`.
- **Ventanas:** diálogo **Crear tabla dinámica**; barra de carga momentánea.

### 122–123
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** celda de salida `X3` para la tabla dinámica.
- **Acción:** la tabla dinámica queda creada, vacía.
- **Datos:** panel derecho **Campos de tabla dinámica** visible.
- **Ventanas:** panel de campos a la derecha + placeholder de tabla dinámica.

### 124–128
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** tabla dinámica en `X3`; panel de campos activo.
- **Acción:** se empieza a construir la dinámica.
- **Datos:** todavía sin resultados; se ve el área vacía “Para generar un informe…”.
- **Ventanas:** panel **Campos de tabla dinámica**.

### 129–133
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** campo `LOCALIDAD` en el panel; lista de campos desplazada.
- **Acción:** se arrastra `LOCALIDAD` a **Filas**.
- **Datos:** aparecen etiquetas de fila.
- **Ventanas:** panel de campos + lista de campos con scroll.

### 134
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** tabla dinámica ya poblada.
- **Acción:** se agrega `Suma de TOTAL` a **Valores**.
- **Datos visibles:**  
  - `CANDELARIA 96`  
  - `ENGATIVÁ 98`  
  - `FONTIBÓN 48`  
  - `KENNEDY 18`  
  - `MÁRTIRES 70`  
  - `N/A 2579`  
  - `NIVEL CENTRAL 693`  
  - `SANTA FE 15`  
  - `SUBA 19`  
  - `TEUSAQUILLO 666`  
  - `Total general 4302`
- **Ventanas:** panel de campos sigue abierto.

### 135–147
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** abre el filtro desplegable de **Etiquetas de fila / LOCALIDAD**.
- **Acción:** filtrado manual de localidades.
- **Datos:** lista con checks de `CANDELARIA`, `ENGATIVÁ`, `FONTIBÓN`, `KENNEDY`, `MÁRTIRES`, `N/A`, `NIVEL CENTRAL`, `SANTA FE`, `SUBA`, `TEUSAQUILLO`; se ve scroll dentro del filtro.
- **Ventanas:** menú desplegable de filtro con búsqueda y casillas.

### 148–152
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** filtro cerrado; tabla dinámica visible.
- **Acción:** resultado filtrado/estabilizado.
- **Datos visibles:** la dinámica sigue mostrando la suma por localidad; gran total sigue visible.
- **Ventanas:** panel de campos a la derecha; Teams sigue superpuesto.

### 153–160
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** clic derecho en la pestaña de hoja `REGISTRADO SIDE`.
- **Acción:** se abre el menú contextual de hoja.
- **Datos:** no cambian valores; es operación de hoja.
- **Ventanas:** menú contextual con opciones tipo `Insertar`, `Eliminar`, `Cambiar nombre`, `Mover o copiar`, `Ver código`, `Proteger hoja`, `Color de pestaña`.

### 161–170
- **Libro/hoja:** mismo libro/hoja.
- **Selección:** opción **Mover o copiar...**.
- **Acción:** se prepara traslado de la hoja a otro libro.
- **Datos:** en el diálogo aparece como destino `BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx`.
- **Ventanas:** diálogo **Mover o copiar** con lista de hojas destino.

### 171
- **Libro/hoja:** mismo diálogo.
- **Selección:** casilla **Crear una copia**.
- **Acción:** se confirma que no se mueve, sino que se duplica la hoja.
- **Ventanas:** diálogo **Mover o copiar**.

### 172–173
- **Libro/hoja:** cambia al libro destino `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`.
- **Selección:** pestaña `REGISTRADO SIDE (2)` / copia recién creada.
- **Acción:** se crea la copia en el nuevo libro.
- **Datos:** la hoja copiada aparece disponible junto a otras pestañas (`CERT.P.HORIZONTAL. ABRIL`, `REGISTRADO SIDE`, `Reporte PQRS Mayo2026`, `INF Localidades PPT`, `RESUMEN CIFRAS`).
- **Ventanas:** cambio de libro visible.

### 174–176
- **Libro/hoja:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, hoja `REGISTRADO SIDE`.
- **Selección:** área de tabla dinámica en columna `X`.
- **Acción:** se ve otra tabla dinámica ya resumida.
- **Datos visibles:**  
  - `NIVEL CENTRAL 38`  
  - `TEUSAQUILLO 546`  
  - `CHAPINERO 7`  
  - `Total general 591`
- **Ventanas:** sin diálogo; solo la hoja activa.

### 177–183
- **Libro/hoja:** misma copia.
- **Selección:** clic derecho en otra pestaña de hoja.
- **Acción:** aparece menú contextual; luego un aviso de **Eliminar** y un cursor de espera.
- **Datos:** no cambia contenido visible.
- **Ventanas:** menú contextual + confirmación de eliminación de hoja (`Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?`).

### 184
- **Libro/hoja:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, pestaña `REPORTE PQRS Mayo2026`.
- **Selección:** tabla de datos crudos en columnas muy avanzadas (`BY: CW` aprox.), filas `12884+`.
- **Acción:** vista de reporte detallado, no tabla dinámica.
- **Datos visibles:** estados como `Recibida`, `Por el distrito`, `Registrada`, `PERIODO ACTUAL`, `Pendiente 0-3`, `PENDIENTE PENDIENTE`; también `false/true`.
- **Ventanas:** hoja de datos sin modales.

### 185–191
- **Libro/hoja:** vuelve a `REGISTRADO SIDE`.
- **Selección:** menú contextual sobre la pestaña de hoja otra vez.
- **Acción:** navegación entre hojas / posible preparación de mover o renombrar.
- **Datos:** mismos resúmenes visibles, sin cambio en celdas.
- **Ventanas:** menú contextual de hoja.

### 192–195
- **Libro/hoja:** `REGISTRADO SIDE`.
- **Selección:** celda `X2` en el área de la tabla dinámica.
- **Acción:** edición de texto en esa celda.
- **Datos:** se escribe progresivamente `MAY`, luego `MAYO 2`, luego `MAYO 2026`; Excel muestra una fecha/formato en la barra de fórmula como `1/05/2026`.
- **Ventanas:** edición directa de celda, sin diálogos.

### 196–200
- **Libro/hoja:** `REGISTRADO SIDE`.
- **Selección:** sigue en `X2`.
- **Acción:** Excel autoformatea el contenido a `may-26`.
- **Datos:** el texto visible cambia de `MAYO 2026` a `may-26`.
- **Ventanas:** no hay diálogo; solo la hoja con la celda editada.

Si quieres, te lo convierto ahora en **tabla CSV/JSON por frame** para que lo uses directo en anotación o transcripción técnica.

[Batch 3 - gpt-5.4-mini]
Here’s the frame-by-frame readout.

**Frames 00201–00207**
- **Workbook/sheet:** `Resumen SIDE Mayo 2026 - Excel`, sheet **REGISTRADO SIDE** active. Other tabs visible: `STOCK 31052026`, `ENTREGADO SIDE`.
- **Selection:** active cell shown as **Y14** (blank cell below/right of the pivot table).
- **Action:** no edit visible; just cursor movement/loading. Frame 00207 shows the pointer near the **red X (close)** button.
- **Visible data:** pivot table with **Etiquetas de fila / Suma de TOTAL**:
  - CANDELARIA 96
  - ENGATIVA 98
  - FONTIBON 48
  - KENNEDY 18
  - MARTIRES 70
  - NIVEL CENTRAL 693
  - SANTA FE 15
  - SUBA 19
  - TEUSAQUILLO 666
  - **Total general 1723**
  Left side also shows a source table with `TOTAL 2579` and rows like `5 VALE`, `N4 GUZ`, and numeric codes.
- **Windows/menus:** Excel window open; Teams screen-sharing banner visible (`Dejar de compartir` / `Ocultar`); participant pane with **Yesenia Patino Figueroa**.

**Frame 00208**
- **Workbook/sheet:** switched to `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, sheet **REGISTRADO SIDE** active.
- **Selection:** active cell shown as **X20**.
- **Action:** workbook/window switch; no data edit visible.
- **Visible data:** same pivot table and same values as above.
- **Windows/menus:** Excel still open; Teams sharing banner remains.

**Frame 00209**
- **Workbook/sheet:** same as 00208.
- **Selection:** still **X20**.
- **Action:** no visible change.
- **Visible data:** same pivot table; same left-side source data.
- **Windows/menus:** same Excel + Teams overlay.

**Frame 00210**
- **Workbook/sheet:** same as 00208.
- **Selection:** still **X20**.
- **Action:** no visible change.
- **Visible data:** same pivot table and source table.
- **Windows/menus:** same Excel + Teams overlay.

**Frame 00211**
- **Workbook/sheet:** **File Explorer** (not Excel).
- **Selection:** file **`Resumen SIDE Mayo 2026`** selected.
- **Action:** browsing the folder, likely preparing to move/copy/open a file.
- **Visible data:** folder `2026` under `BASE DOCUMENTOS EXTRAVIADOS`; file list includes:
  - `Resumen SIDE Abril 2026`
  - `Resumen SIDE Enero 2026`
  - `Resumen SIDE Febrero 2026`
  - `Resumen SIDE Marzo 2026`
  - `Resumen SIDE Mayo 2026`
- **Windows/menus:** Explorer window open; Teams share banner still visible.

**Frame 00212**
- **Workbook/sheet:** same File Explorer window.
- **Selection:** file list focus remains in the same area; the highlight shifts toward **`Resumen SIDE Febrero 2026`** while the list is unchanged.
- **Action:** browsing/selecting another monthly file.
- **Visible data:** same 2026 folder and same five `Resumen SIDE` files.
- **Windows/menus:** Explorer open; Teams share banner still visible.

**Transition notes**
- **00207 → 00208:** Excel workbook title changes from `Resumen SIDE Mayo 2026` to `BASE DATOS PPT LOCALIDADES MAYO 2026`.
- **00210 → 00211:** hard switch from Excel to **File Explorer**.

---

## Segmento 3: Registro de atenciones y grupos poblacionales

| Campo | Valor |
|---|---|
| **Duración** | 9:40 - 15:00 |
| **Descripción** | Abre archivo atenciones 2026, trae registro con grupos poblacionales, ordena A-Z, maneja Ciudad Bolívar duplicada, separa nivel central y supercades |
| **Frames analizados** | 320 |
| **Batches** | 4 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 644s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Grouped by identical consecutive frames.

- **Frames 1–3:** File Explorer.  
  - Path: `Documentos > SECGOB > BASE DOCUMENTOS EXTRAVIADOS > 2026` then back up to `SECGOB`.  
  - Visible files/folders: `Resumen SIDE Abril 2026`, `Resumen SIDE Enero 2026`, `Resumen SIDE Febrero 2026`, `Resumen SIDE Marzo 2026`, `Resumen SIDE Mayo 2026`.  
  - Action: navigating folders / locating source file.

- **Frames 4–8:** File Explorer inside `BASE ORIENTACIONES SIACTUA > 2026`.  
  - Visible year folders: `2020`, `2021`, `2022`, `2023`, `2024`, `2025`, `2026`.  
  - Frame 8 highlights a report file list, including `05. SAC_atencion - Mayo 2026`.  
  - Action: locating the May 2026 attendance workbook.

- **Frames 9–11:** Excel workbook `BASE DATOS PPT LOCALES MAYO 2026 - Excel`, sheet **`REGISTRADO SIDE`**.  
  - Active cell shown: **`X20`**.  
  - Visible pivot summary for **`may-26`**:
    - Candelaria **96**
    - Engativá **98**
    - Fontibón **48**
    - Kennedy **18**
    - Mártires **70**
    - Nivel Central **693**
    - Santa Fe **15**
    - Suba **19**
    - Teusaquillo **666**
    - **Total general 1723**
  - Left-side raw codes/data visible in columns V/W/X (e.g. `3418`, `29,32,33,35,44,47,49` etc.).
  - Action: reviewing summary data after opening the workbook.

- **Frames 12–15:** Excel workbook `05. SAC_atencion - Mayo 2026` in **Protected View**, sheet **`tablas`**.  
  - Yellow banner: **“VISTA PROTEGIDA”** with **“Habilitar edición”**.  
  - Visible pivot tables:
    - **Registros por servidor**
    - **Registros por punto de atención**
    - **Registros por Asunto**
    - **Registros por Asunto / Canal de atención**
    - **Registros por Atención Preferencial**
  - Readable counts:
    - Canal de atención: `Presencial 3653`, `Telefónica 670`, `Virtual 5`, **Total general 4328**
    - Attention preference includes `Ninguna 2582`, `Persona Mayor 650`, `Persona con discapacidad física 36`, `...`
  - Frame 15: sheet is loading / hourglass, no data editable yet.
  - Action: opening and inspecting the prebuilt pivot tables.

- **Frames 16–20:** Same Excel workbook, **`tablas`**, with **PivotTable Fields** pane open on the right.  
  - Fields visible: `Punto de atención`, `Nombre completo ciudadano`, `Grupo etario`, `Identidad de Género`, `Sexo`, `Orientación sexual`, `Fecha de atención`.  
  - Row/Values area visible; pivot layout being adjusted, not direct cell editing.  
  - Action: configuring pivot-table fields.

- **Frames 21–24:** Back to `BASE DATOS PPT LOCALES MAYO 2026 - Excel`, sheet **`REGISTRADO SIDE`**.  
  - Same `may-26` summary remains visible.  
  - Bottom tabs visible: `Calificaciones Totales`, `REGISTRO ATENCIONES`, `CERT RESIDENCIA PROD-ABRIL`, `CERT.P.HORIZONTAL ABRIL`, `REGISTRADO SIDE`, `Reporte PQRS Mayo2026`, `INF Localid...`  
  - Action: tab switching / returning to the summary sheet.

- **Frames 25–40:** Excel workbook `05. SAC_atencion - Mayo 2026`, sheet **`REGISTRO ATENCIONES`**.  
  - Frame 25/26 active cell: **`C16`**.  
  - Frame 33 active cell: **`D5`** with formula bar showing **“Alcaldía local Engativá”**.  
  - Frame 34 active cell: **`G6`** with formula bar showing **“Ledy Viviana Ramírez Gomez”**.  
  - Frame 36 active cell: **`J6`** with formula bar showing **“Persona con discapacidad visual”**.  
  - Pivot tables visible:
    - **Registros por servidor**
      - Jairo Humberto Riano Ruge **383**
      - Diana Forero Coronel **334**
      - Margarita Martínez Peralta **177**
      - Luz Ginette Montes Fajardo **154**
      - Yenny Patricia Rodríguez González **149**
      - etc.
    - **Registros por punto de atención**
      - Nivel central **650**
      - Alcaldía local Engativá **375**
      - Alcaldía local Barrios Unidos **261**
      - Alcaldía local Ciudad Bolívar **211**
      - Alcaldía local Kennedy **204**
      - Alcaldía local Tunjuelo **150**
      - Alcaldía local Suba **139**
      - Alcaldía local Usaquén **129**
      - SuperCade Manitas **110**
      - Alcaldía local Fontibón **76**
    - **Punto/Servidor**
      - Alcaldía local Antonio Nariño **53**
      - Jennifer Andrea Martínez Cubides **35**
      - Ledy Viviana Ramírez Gomez **18**
      - Alcaldía local Barrios Unidos **261**
      - Margarita Martínez Peralta **256**
      - Alcaldía local Bosa **76**
      - etc.
    - **Atención Preferencial**
      - Ninguna **2582**
      - Persona Mayor **650**
      - Persona con discapacidad física **36**
      - Persona con discapacidad intelectual-cognitiva **26**
      - Comunidad Afro **14**
      - Víctimas del conflicto armado **13**
      - Persona con discapacidad múltiple **12**
      - Persona con discapacidad visual **11**
      - Persona con discapacidad mental-psicosocial **11**
      - Comunidad indígena **3**
      - Campesino campesina **3**
  - Open pane/dialog: **Campos de tabla dinámica** on the right.  
  - Action: inspecting and rearranging pivot-table fields; no formula editing visible.

- **Frames 41–98:** Chrome / Teams meeting page, **not Excel**.  
  - Visible page: `teams.microsoft.com` tab titled **“Trabajar Informes…”**.  
  - Main text: **“Esperando a que se unan otros usuarios...”**  
  - Banner: **“Grabación y transcripción”** enabled.  
  - Top controls hovered repeatedly:
    - microphone (`Silenciar micrófono`)
    - audio options (`Abrir opciones de audio`)
    - share/stop sharing (`Dejar de compartir`)
  - Screen-share notice: **“teams.microsoft.com está compartiendo tu pantalla”** with button **“Dejar de compartir”**.  
  - Action: temporarily leaving Excel / monitoring the call; no workbook visible.

- **Frame 99:** Windows task switcher / alt-tab.  
  - Previews of open Excel windows visible:
    - `BASE DATOS PPT LOCALID...`
    - `INFORME PQRS SEC...`
    - `05. SAC_atencion - Mayo 2...`
  - Action: switching back to Excel.

- **Frame 100:** Excel returns, sheet **`tablas`** in `05. SAC_atencion - Mayo 2026`.  
  - Same pivot-table dashboard visible again.  
  - Action: back to the reporting workbook.

If you want, I can turn this into a **frame-by-frame table with columns: frame # / workbook / sheet / selection / action / values / windows**.

[Batch 2 - gpt-5.4-mini]
Aquí va el análisis, agrupando las tomas casi idénticas por cambio real de pantalla/acción:

- **Frames 101–104**
  - **Libro/hoja:** `05_SAC_Atencion - Mayo 2026.xlsx`, hoja **`tablas`**.
  - **Selección:** cursor dentro del área de tablas dinámicas; se ve una celda activa sobre el bloque central/derecho.
  - **Acción:** revisión de tablas dinámicas ya construidas.
  - **Datos visibles:**
    - **Registros por servidor:** Jairo Humberto Riano Ruge **364 (8.4%)**, Diana Forero Coronel **337 (7.8%)**, Luz Ginette Montes Fajardo **283 (6.5%)**.
    - **Registros por punto de atención:** Nivel central **843 (19.5%)**, Alcaldía local Engativá **362 (8.4%)**, Usaquén **316 (7.3%)**, Kennedy **311 (7.2%)**, Ciudad Bolívar **293 (6.8%)**, Bosa **261 (6.0%)**.
    - **Registros por Asunto:** Certificado de Residencia **2049**, información punto de atención y CDI **587**, Código nacional de seguridad y convivencia ciudadana **554**, información general sin competencia de la SDG **401**, Oficina jurídica **233**.
    - **Registros por Canal de atención:** Presencial **3653**, Telefónica **670**, Virtual **5**, Total **4328**.
  - **Ventanas/menús:** panel **Campos de tabla dinámica** abierto en 102–103; barra de Teams compartiendo pantalla con botón **“Dejar de compartir”**.

- **Frames 103–104**
  - **Libro/hoja:** mismo libro, misma hoja `tablas`.
  - **Selección:** una celda del pivot de **Registros por Asunto**.
  - **Acción:** inspección de un elemento del pivot; en la barra de fórmula se ve el texto **“Información general sin competencia de la SDG”**.
  - **Ventanas:** panel de campos de tabla dinámica sigue abierto.

- **Frames 105–118**
  - **Libro/hoja:** mismo libro, hoja `tablas`.
  - **Selección:** se mueve la vista hacia la derecha; el cursor cambia de posición, pero no hay edición clara.
  - **Acción:** navegación visual por la hoja para revisar el bloque de **Registros por Atención Preferencial** y el extremo derecho de los pivots.
  - **Datos visibles:** en **Atención preferencial** se alcanza a leer:
    - Ninguna **2582**
    - Persona Mayor **650**
    - Persona con discapacidad física **36**
    - Persona con discapacidad intelectual-cognitiva **24**
    - Comunidad Afro **16**
    - Víctimas del conflicto armado **13**
  - **Ventanas:** Teams sigue compartiendo pantalla.

- **Frames 119–120**
  - **Libro/hoja:** `05_SAC_Atencion - Mayo 2026.xlsx`, hoja `tablas`.
  - **Selección:** panel **Campos de tabla dinámica** vuelve a mostrarse a la derecha.
  - **Acción:** revisión de campos disponibles para el pivot.
  - **Campos visibles:** `Punto de atención`, `Nombre completo ciudadano`, `Grupo etario`, `Identidad de Género`, `Sexo`, `Orientación sexual`, `Fecha de atención`, `Atención preferencial`, `Canal de atención`.
  - **Ventanas:** paneo de pivots + Teams.

- **Frames 121–125**
  - **Libro/hoja:** misma hoja `tablas`.
  - **Selección:** clic derecho sobre la pestaña **`tablas`**.
  - **Acción:** aparece el menú contextual de hoja.
  - **Menú visible:** `Insertar...`, `Eliminar`, `Cambiar nombre`, `Mover o copiar...`, `Ver código`, `Proteger hoja...`, `Color de pestaña`, `Ocultar`, `Mostrar...`, `Seleccionar todas las hojas`.
  - **Ventanas:** diálogo **Mover o copiar** empieza a abrirse.

- **Frames 126–129**
  - **Libro/hoja:** diálogo **Mover o copiar** activo.
  - **Selección:** lista de libros destino y hoja destino.
  - **Acción:** preparación para copiar/mover la hoja `tablas`.
  - **Detalles visibles:** destino con el archivo **`BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx`**; lista de hojas objetivo muestra opciones como **`Registros atenciones`**, **`tabla`** y **`(mover al final)`**.
  - **Ventanas:** modal de Excel en primer plano.

- **Frames 130–145**
  - **Libro/hoja:** cambia al libro **`BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`**, hoja **`REGISTRO ATENCIONES`**.
  - **Selección:** pestañas inferiores visibles; luego se abre menú contextual sobre la pestaña `REGISTRO ATENCIONES`.
  - **Acción:** se intenta gestionar la hoja (renombrar/mover/eliminar/copy), y aparece aviso de borrado.
  - **Ventanas/diálogos:**
    - Menú contextual de hoja.
    - Confirmación de Excel: **“Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?”**
    - Botones **Eliminar** / **Cancelar**.
  - **Datos visibles:** otra disposición de pivots con localidades y grupos poblacionales.

- **Frames 146–147**
  - **Libro/hoja:** mismo libro, hoja **`CERT RESIDENCIA PROD-ABRIL`**.
  - **Selección:** ninguna edición; vista general del dashboard.
  - **Acción:** cambio de pestaña a un resumen de productividad.
  - **Datos visibles:**
    - Tabla **PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA VALIDOS**
    - Gráfico de barras con localidades como **SUBA**, **TUNJUELITO**, **KENNEDY**, etc.
  - **Ventanas:** sin diálogo; solo workbook y hoja.

- **Frames 148–151**
  - **Libro/hoja:** vuelve a **`REGISTRO ATENCIONES`**.
  - **Selección:** pivots de localidades visibles; cursor sobre el bloque central.
  - **Acción:** revisión previa a ordenar/filtrar.
  - **Ventanas:** panel de campos de tabla dinámica a la derecha.

- **Frames 152–177**
  - **Libro/hoja:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, hoja `REGISTRO ATENCIONES`.
  - **Selección:** se abre el desplegable de filtro del campo **`Punto de atención`**.
  - **Acción:** preparación para **ordenar de A a Z** / filtrar los puntos de atención.
  - **Menú visible:**
    - `Ordenar de A a Z`
    - `Ordenar de Z a A`
    - `Más opciones de ordenación...`
    - `Filtros de etiqueta`
    - `Filtros de valor`
    - buscador con lista de checkbox.
  - **Lista visible:** aparecen localidades/alcaldías como **Alcaldía local Antonio Nariño**, **Bosa**, **Candelaria**, **Chapinero**, **Ciudad Bolívar**, **Engativá**, etc.
  - **Ventanas:** el menú desplegable ocupa el centro; Teams sigue abajo.

- **Frames 178–200**
  - **Libro/hoja:** misma hoja `REGISTRO ATENCIONES`.
  - **Selección:** pivot ya reordenado.
  - **Acción:** el orden del pivot por **Punto de atención** queda **alfabético**.
  - **Datos visibles del orden resultante:**
    - **Alcaldía local Antonio Nariño** **61**
    - **Alcaldía local Bosa** **264**
    - **Alcaldía local Candelaria** **61**
    - **Alcaldía local Chapinero** **63**
    - **Alcaldía local Ciudad Bolívar** **93**
    - **Alcaldía local Engativá** **362**
    - **Alcaldía local Fontibón** **89**
    - **Alcaldía local Kennedy** **311**
    - **Alcaldía local Santa Fe** **59**
    - **Alcaldía local Suba** **113**
  - **Ventanas:** ya no está el menú desplegable; se ve la tabla ordenada y la interfaz de Excel normal.

Si quieres, te lo convierto en una **línea de tiempo exacta frame por frame** con formato tipo `frame_00101 → acción`, `frame_00102 → acción`, etc.

[Batch 3 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped where the screen is unchanged:

### Frames 201–210
- **Workbook:** `BASE DATOS PPT LOCALIDADES MAYO 2026` (Excel)
- **Sheet:** `REGISTRO ATENCIONES` (active)
- **Selection/range:** pivot-table area; no clear edit range, cursor hovering across the center/right tables
- **Action:** verifying the pivot tables / reading the existing summary
- **Visible data:**  
  - `Registros por servidor`
  - `Registros por punto de atención`
  - `Registros por Asunto`
  - `Registros por Atención Preferencial`
- **Windows/menus:** Excel PivotTable field pane (`Campos de tabla dinámica`) open on the right; Teams sharing bar visible (`Dejar de compartir`)

### Frames 211–227
- **Workbook:** same
- **Sheet:** `RESUMEN CIFRAS` (active)
- **Selection/range:** summary table `A3:J27`; editing starts in **ORIENTACIONES / No. 4** column (around `E4:E9`)
- **Action:** typing/pasting locality totals into the summary table
- **Visible data:**  
  - `ANTONIO NARIÑO 9 / 29`
  - `BARRIOS UNIDOS 13 / 19`
  - `BOSA 166 / 59`
  - `CANDELARIA 113 / 34`
  - `CHAPINERO 18 / 23`
  - `CIUDAD BOLIVAR 37 / 26`
  - ORIENTACIONES values entered: `61, 264, 61, 45, 63, 293`
- **Important edit:** `CIUDAD BOLIVAR` ORIENTACIONES is manually corrected from `293` → `293+2` → `295`
- **Windows/menus:** right-click context menu opens on the selected cell around frames 213–214

### Frames 228–241
- **Workbook:** same
- **Sheet:** `REGISTRO ATENCIONES` (active again)
- **Selection/range:** pivot-table cells in the center tables; hover/inspect behavior, no new sheet edit
- **Action:** checking the pivot outputs again
- **Visible data:** same pivot blocks; locality rows and counts remain visible
- **Windows/menus:** PivotTable field pane still open; Teams share bar still visible

### Frames 242–249
- **Workbook:** same
- **Sheet:** `RESUMEN CIFRAS`
- **Selection/range:** lower half of the summary table, around rows `17–27`; active cell near `E25` (`SUPERCADES / ORIENTACIONES`)
- **Action:** continuing manual data entry / correction
- **Visible data:**  
  - `SANTA FE 68 / 32`
  - `SUBA 70 / 75`
  - `SUMAPAZ 6 / 3`
  - `TEUSAQUILLO 22 / 10`
  - `TUNJUELITO 40 / 30`
  - `USAQUEN 46 / 59`
  - `USME 45 / 50`
  - `NIVEL CENTRAL 8484 / 497 / 843`
  - `SUPERCADES 0 / 0 / 406`
  - `EN BLANCO 0 / 0`
  - `TOTAL GENERAL 9.431 / 1.168 / 3.485`
- **Windows/menus:** brief context menu appears again while editing the cell

### Frames 250–253
- **Workbook:** same
- **Sheet:** `RESUMEN CIFRAS`
- **Selection/range:** cell `E12` (row `KENNEDY`, ORIENTACIONES)
- **Action:** manual correction of a typed arithmetic-like entry
- **Visible data/formula-like text:** `311+1` → corrected to `312`
- **Note:** this is visible as typed cell content, not a real Excel formula display
- **Windows/menus:** no extra dialog; just the edited cell

### Frames 254–300
- **Workbook:** same
- **Sheet:** alternates between `RESUMEN CIFRAS` and `REGISTRO ATENCIONES`
- **Selection/range:** mostly verification; no new broad edits visible
- **Action:** confirming totals after the corrections
- **Visible data:**  
  - `RESUMEN CIFRAS` final ORIENTACIONES total shows `4.328`
  - `EN BLANCO` remains `0`
  - lower rows stay consistent with the prior values
- **Windows/menus:** Teams share bar remains; PivotTable field pane appears whenever `REGISTRO ATENCIONES` is shown

### Main transition points
- **201 → 211:** switch from pivot-view sheet `REGISTRO ATENCIONES` to the summary sheet `RESUMEN CIFRAS`
- **228 → 242:** return to `RESUMEN CIFRAS` lower section
- **250 → 254+:** correction of `KENNEDY` value completes, then totals are rechecked

If you want, I can turn this into a strict **CSV-style frame log** next.

[Batch 4 - gpt-5.4-mini]
Here’s the frame-by-frame readout:

**301–304**  
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026` / `RESUMEN CIFRAS`
- **Selection/action:** static view, no clear edit selection
- **Visible data:** summary table headed **“DIAPOSITIVA No. 3”** with columns like `ALCALDÍA LOCAL`, `PQRS GESTIONADAS N. 1`, `PQRS PENDIENTES N. 2`, `DOC.EXT. N. 3`, `ORIENTACIONES No. 4`, `CERT. PROPIEDAD No. 5`, `CERT. RESIDENCIA No. 6`
- **Read values:**  
  `SANTA FE 68 / 32 / 59`  
  `SUBA 70 / 75 / 180`  
  `SUMAPAZ 6 / 3 / 3`  
  `TEUSAQUILLO 22 / 10 / 251`  
  `TUNJUELITO 40 / 30 / 167`  
  `USAQUEN 46 / 59 / 316`  
  `USME 45 / 50 / 112`  
  `NIVEL CENTRAL 8484 / 497 / 843`  
  `SUPERCADES 0 / 0 / 406`  
  `EN BLANCO 0 / 0 / 0`  
  `TOTAL GENERAL 9.431 / 1.168 / 4.328`
- **Open windows:** Excel only, with Teams share bar at bottom

**305**  
- **Workbook/sheet:** same workbook / `REGISTRO ATENCIONES`
- **Selection/action:** dashboard view, likely reviewing pivot tables
- **Visible data:** multiple pivots/tables; left side shows names and percentages, center/right show grouped summaries
- **Open windows:** Excel with `REGISTRO ATENCIONES` tab active

**306**  
- **Workbook/sheet:** same workbook / `REGISTRO ATENCIONES`
- **Selection/action:** cell **F34** selected; formula bar shows **4328**
- **Visible data:** pivot tables plus right-side **“Campos de tabla dinámica”**
- **Open windows:** Excel field list open on the right

**307**  
- **Workbook/sheet:** same workbook / `REGISTRO ATENCIONES`
- **Selection/action:** still on the pivot dashboard, inspecting the same data
- **Visible data:** `Total general 4328` remains visible
- **Open windows:** Excel + pivot field panel

**308**  
- **Workbook/sheet:** same workbook / `REGISTRO ATENCIONES`
- **Selection/action:** no visible edit; still reviewing pivots
- **Visible data:** same tables and field list
- **Open windows:** Excel + pivot field panel

**309**  
- **Workbook/sheet:** same workbook / `REGISTRO ATENCIONES`
- **Selection/action:** unchanged from 306–308
- **Visible data:** pivot summary still centered on `4328`
- **Open windows:** Excel + field list

**310**  
- **Workbook/sheet:** not readable because **Alt-Tab switcher** is open
- **Selection/action:** switching windows
- **Visible windows/thumbnails:**  
  `BASE DATOS PPT LOCALIDA...`  
  `05_SAC_atencion - Mayo 202...`  
  `teams.microsoft.com...`  
  `(2) Trabajar Informes PQRS...`  
  `2026 - Explorador de archivos`  
  `INFORME PQRS SECRETARIA...`  
  `20260602ActaReuniónSIGPar...`  
  `ANALISIS INFORME PQRS RE...`
- **Open windows:** Windows task switcher overlay

**311**  
- **Workbook/sheet:** `05_SAC_atencion - Mayo 202...` / `tablas`
- **Selection/action:** cell **E5** selected; formula bar shows **“Alcaldía local Engativá”**
- **Visible data:** three pivot tables:
  - **Registros por servidor**
  - **Registros por punto de atención**
  - **Registros por Asunto**
- **Read values:** in the left pivot, top visible rows include  
  `Jairo Humberto Riano Ruge 365 (8.4%)`  
  `Diana Forero Coronel 334 (7.8%)`  
  `Luz Gi... Montes Fajardo 283 (6.5%)`
  - right-side `Registros por Asunto` shows items like `Certificado de Residencia`, `Información punto de atención y CDI`, `Código nacional de seguridad y convivencia ciudadana`, `Oficina jurídica`, `Propiedad horizontal`, `Subsidios`, `Documentos extraviados`, `Ventas ambulantes - RVI`
  - `Total general 4328` is visible
- **Open windows:** Excel + `Campos de tabla dinámica` panel

**312**  
- **Workbook/sheet:** Windows **Alt-Tab switcher**
- **Selection/action:** switching back to the Excel workbook
- **Visible windows/thumbnails:** `05_SAC_atencion - Mayo 202...` is highlighted
- **Open windows:** task switcher overlay

**313**  
- **Workbook/sheet:** `05_SAC_atencion - Mayo 202...` / `tablas`
- **Selection/action:** returned to the pivot dashboard
- **Visible data:** same pivot tables as frame 311
- **Open windows:** Excel + pivot field panel

**314**  
- **Workbook/sheet:** same workbook / `tablas`
- **Selection/action:** reviewing the middle pivot table
- **Visible data:** `Registros por punto de atención` and the `Campos de tabla dinámica` pane
- **Open windows:** Excel + field list

**315**  
- **Workbook/sheet:** same workbook / `tablas`
- **Selection/action:** still inspecting pivots; no obvious change
- **Visible data:** same dashboard, same `Total general 4328`
- **Open windows:** Excel + field list

**316**  
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026` / `REGISTRO SIDE`
- **Selection/action:** cell **X20** shown in the name box; pivot summary being reviewed
- **Visible data:** pivot for **may-26** with `Etiquetas de fila` and `Suma de TOTAL`
- **Read values:**  
  `CANDELARIA 96`  
  `ENGATIVA 98`  
  `FONTIBON 48`  
  `KENNEDY 18`  
  `MARTIRES 70`  
  `NIVEL CENTRAL 693`  
  `SANTA FE 15`  
  `SUBA 19`  
  `TEUSAQUILLO 666`  
  `Total general 1723`
- **Other visible text:** left raw list includes codes like `5 VALE`, `5 GUZ` and numbers such as `3418`, `3443`, `3450`, `3452`, `3453`, `3458`, `3454/3456`, `3457`, `3424`, `3463`, `3468`, `3487`, `3488`, `3474`, `3476`, `3499`, `3507`, `3510`, `3514/3517`, `3518`
- **Open windows:** Excel; sheet tabs visible

**317**  
- **Workbook/sheet:** same workbook / `REGISTRO SIDE`
- **Selection/action:** same pivot view, no visible change
- **Visible data:** same `may-26` summary and `Total general 1723`
- **Open windows:** Excel

**318**  
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026` / `RESUMEN CIFRAS`
- **Selection/action:** back to the summary sheet
- **Visible data:** same `DIAPOSITIVA No. 3` table
- **Open windows:** Excel + Teams share bar

**319**  
- **Workbook/sheet:** same workbook / `RESUMEN CIFRAS`
- **Selection/action:** same summary table, no visible edit
- **Visible data:** `TOTAL GENERAL` row still shows `9.431`, `1.168`, `4.328`
- **Open windows:** Excel

**320**  
- **Workbook/sheet:** same workbook / `RESUMEN CIFRAS`
- **Selection/action:** cell **E17** selected; formula bar shows **59**
- **Visible data:** same row set (`SANTA FE`, `SUBA`, `SUMAPAZ`, etc.) and same summary totals
- **Open windows:** Excel with Teams sharing banner

If you want, I can turn this into a **clean timeline with inferred user actions** (sort, switch workbook, inspect pivot, return to summary).

---

## Segmento 4: Documentos extraviados — registro manual uno a uno

| Campo | Valor |
|---|---|
| **Duración** | 15:00 - 17:00 |
| **Descripción** | Copia manual de datos de documentos extraviados por localidad, verificación por Candelaria/La Candelaria |
| **Frames analizados** | 120 |
| **Batches** | 2 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 319s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped by the actual screen states:

### 1) Frames 00001–00009
- **Workbook:** `BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel`
- **Sheet:** `RESUMEN CIFRAS`
- **Visible content:** slide-style table titled **“DIAPOSITIVA No. 3”**
- **Action:** review/navigation only; no data entry yet
- **Selected cells:** cursor moves around blank cells in the middle of the table; no clear range fill
- **Visible values:** locality rows such as:
  - Antonio Nariño **61**
  - Barrios Unidos **264**
  - Bosa **61**
  - Candelaria **45**
  - Chapinero **63**
  - Ciudad Bolívar **295**
  - Engativá **362**
  - Fontibón **133**
  - Kennedy **312**
  - Mártires **60**
  - Puente Aranda **58**
  - Rafael Uribe **95**
  - San Cristóbal **182**
- **Windows/menus:** Excel ribbon; Teams screen-sharing bar at bottom-right

### 2) Frames 00010–00017
- **Workbook:** same
- **Sheet:** `REGISTRADO SIDE`
- **Action:** inspecting a PivotTable summary
- **Selected cells/range:** PivotTable area around `Etiquetas de fila / Suma de TOTAL`
- **Visible values in PivotTable:**
  - Candelaria **96**
  - Engativá **98**
  - Fontibón **48**
  - Kennedy **18**
  - Mártires **70**
  - Nivel Central **693**
  - Santa Fe **15**
  - Suba **19**
  - Teusaquillo **666**
  - **Total general: 1723**
- **Windows/menus:** `Campos de tabla dinámica` pane open on the right; Teams overlay still visible

### 3) Frames 00018–00040
- **Workbook:** same
- **Sheet:** `RESUMEN CIFRAS`
- **Action:** manual one-by-one typing into **DOC.EXT** column
- **Edited range:** mostly column **D** on locality rows
- **Entered values visible across the sequence:**
  - Candelaria **96**
  - Engativá **98**
  - Fontibón **48**
  - Kennedy **18**
  - Mártires **70**
  - Santa Fe **15**
  - Suba **19**
  - Teusaquillo **666**
  - Tunjuelito **30**
  - Usaquén **59**
  - Usme **50**
  - Nivel Central **693**
  - Supercades **406**
  - En Blanco **0**
- **Notes:** this is clearly manual entry, not formula-driven
- **Windows/menus:** Excel only; Teams sharing control remains visible

### 4) Frames 00041–00062
- **Workbook:** same
- **Sheets:** quick tab switching between `REGISTRADO SIDE` and `RESUMEN CIFRAS`
- **Action:** verification pass; no new numbers added
- **Selected cells:** still around the DOC.EXT column and lower rows
- **Visible values:** same locality counts as above, with the lower summary row coming into view
- **Transition:** horizontal/scroll repositioning to show more of the table and totals

### 5) Frames 00063–00100
- **Workbook:** same
- **Sheet:** `RESUMEN CIFRAS`
- **Action:** scroll down to the lower rows and final totals
- **Visible lower rows:**
  - Puente Aranda **58**
  - Rafael Uribe **95**
  - San Cristóbal **182**
  - Santa Fe **59**
  - Suba **180**
  - Sumapaz **3**
  - Teusaquillo **251**
  - Tunjuelito **167**
  - Usaquén **316**
  - Usme **112**
  - Nivel Central **843**
  - Supercades **406**
  - En Blanco **0**
- **Final totals visible:**
  - **9.431**
  - **1.168**
  - **1.723**
  - **4.328**
- **Windows/menus:** Excel ribbon; Teams “Dejar de compartir” overlay still present

### Key takeaways
- The segment is **manual verification/entry of “documentos extraviados” by locality**.
- The user is **not using formulas** here; they’re typing counts one by one.
- The important validation point is the Candelaria / Engativá / Fontibón / Kennedy / Mártires / Santa Fe / Suba / Teusaquillo counts, then the lower summary totals.

If you want, I can turn this into a **timestamped shot list** next.

[Batch 2 - gpt-5.4-mini]
Here’s the on-screen sequence, frame by frame.

| Frame(s) | Workbook / sheet | Selection / edit | What’s happening | Visible data / text | Open UI |
|---|---|---|---|---|---|
| 101 | `BASE DATOS PPF LOCALIDADES MAYO 2026` / `RESUMEN CIFRAS` | Active cell appears to be `F24` | Viewing the summary table, no edit | `DIAPOSITIVA No. 3`; rows like `RAFAEL URIBE`, `SAN CRISTOBAL`, `SANTA FE`, `SUBA`, `SUMAPAZ`, `TEUSAQUILLO`, `USAQUEN`, `USME`, `NIVEL CENTRAL`, `SUPERCADES`, `EN BLANCO`, `TOTAL GENERAL`. Visible values include `TEUSAQUILLO 22 / 10 / 666 / 251`, `NIVEL CENTRAL 8484 / 497 / 693 / 843`, `TOTAL GENERAL 9.431 / 1.168 / 1.723 / 4.328` | Excel ribbon (Home), Teams share bar, user avatar on right |
| 102 | same / `RESUMEN CIFRAS` | No clear change visible | Same sheet, horizontally scrolled to the left side of the table | Rows `ANTONIO NARIÑO`, `BARRIOS UNIDOS`, `BOSA`, `CANDELARIA`, `CHAPINERO`, `CIUDAD BOLIVAR`, `ENGATIVA`, `FONTIBON`, `KENNEDY`, `MARTIRES`, `PUENTE ARANDA`, `RAFAEL URIBE`, `SAN CRISTOBAL`, `SANTA FE`; values like `9`, `29`, `0`, `61`, `113`, `34`, `96`, `45`, `41`, `37`, `98`, `362` | same |
| 103 | same / `RESUMEN CIFRAS` | No clear change visible | Same sheet, scrolled right to the `ORIENTACIONES` / certificate columns | Visible headers: `ALCALDÍA LOCAL`, `ORIENTACIONES No. 4`, `CERT. PROPIEDAD No. 5`, `CERT. RESIDENCIA No. 6`, `ENCUESTAS DEL PERIODO`, `ENCUESTAS CON RESPUESTA COMPLETA`, `CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS`, `% PARTICIPACIÓN...` | same |
| 104 | same / `RESUMEN CIFRAS` | Active cell appears to be `C4` with value `29` | Still viewing the same table, small scroll/selection change | `ANTONIO NARIÑO 29 / 0 / 61`, `BARRIOS UNIDOS 19 / 0 / 264`, `BOSA 59 / 0 / 61`, `CANDELARIA 34 / 96 / 45`, `ENGATIVA 37 / 98 / 362`, `FONTIBON 59 / 48 / 133`, `KENNEDY 46 / 18 / 312`, `MARTIRES 7 / 70 / 60` | same |
| 105–110 | same / `RESUMEN CIFRAS` | No distinct edit visible | Continued horizontal navigation on the same summary sheet | Same locality summary, same workbook; no new values entered | same |
| 111 | same workbook / `REGISTRADO SIDE` | Pivot-table area active; no precise cell legible | Sheet switch from summary to registered-data pivot | Center pivot shows `may-26`, `Suma de TOTAL`, with `CANDELARIA 96`, `ENGATIVA 98`, `FONTIBON 48`, `KENNEDY 18`, `MARTIRES 70`, `NIVEL CENTRAL 693`, `SANTA FE 15`, `SUBA 19`, `TEUSAQUILLO 666`, `Total general 1723` | Pivot table fields pane visible at right; Teams bar |
| 112 | same / `REGISTRADO SIDE` | Active cell `Y12`, formula/value `666` | Inspecting the pivot result cell for `TEUSAQUILLO` | Same pivot table; `TEUSAQUILLO 666`, `Total general 1723` | PivotTable Fields pane on right |
| 113 | same / `REGISTRADO SIDE` | Same pivot area | Still on the pivot summary | Same values as 111/112 | same |
| 114 | same workbook / `REPORTE PQRS Mayo2026` | Active cell `A10`; formula bar shows header text `Número petición` | Sheet switch to a raw data report | Large table with rows around `12884–12914`; visible statuses like `Recibida`, `Registrado`, `Por el distrito`, `Por el ciudadano`, `PERIODO ACTUAL`, `PENDIENTE 0-3`, `GESTIONA PENDIENTE` | PivotTable Fields pane still open on right |
| 115 | same / `REPORTE PQRS Mayo2026` | Same area | Continued view of the raw PQRS data table | Same row block, same status columns | same |
| 116 | same workbook / `REGISTRADO SIDE` | Active cell again around `Y12` | Return to the locality pivot summary | Same pivot values: `CANDELARIA 96`, `ENGATIVA 98`, `FONTIBON 48`, `KENNEDY 18`, `MARTIRES 70`, `NIVEL CENTRAL 693`, `SANTA FE 15`, `SUBA 19`, `TEUSAQUILLO 666`, `Total general 1723` | PivotTable Fields pane |
| 117 | same / `REGISTRADO SIDE` | Same pivot | No data change | Same pivot table | same |
| 118 | same / `REGISTRADO SIDE` | Same pivot | Same view | Same pivot table and right-side field list (`LOCALIDAD`, `ORIGEN`, `RADICADO`, etc.) | same |
| 119 | same workbook / `REGISTRO ATENCIONES` | No clear cell edit visible | Sheet switch to attention-registration analytics | Pivot/summary tables with colored percentage bars; left table of localities and counts; right table titled `Registros por Atención Preferencial` | PivotTable Fields pane on right; Teams banner |
| 120 | same / `REGISTRO ATENCIONES` | Active cell appears to be `F34`; formula/value `4328` | Still on attention-registration sheet, focused on pivot totals | `Total general 4328`; right-side pivot field list includes `Punto de atención`, `Nombre completo ciudadano`, `Grupo etario`, `Identidad de Género`, `Sexo`, `Orientación sexual`, `Fecha de atención`, `Atención preferencial`, `Canal de atención` | PivotTable Fields pane open |

### Key transition
- The sequence moves from `RESUMEN CIFRAS` → `REGISTRADO SIDE` → `REPORTE PQRS Mayo2026` → back to `REGISTRADO SIDE` → `REGISTRO ATENCIONES`.
- No formula entry is visible in these frames; this looks like manual verification / navigation of pivot summaries and raw report tabs, not data editing.

---

## Segmento 5: Certificado de residencia — productividad

| Campo | Valor |
|---|---|
| **Duración** | 17:00 - 22:35 |
| **Descripción** | Abre archivo Visage, trae productividad CR (aprobados, pendientes, rechazados, cerrados), reordena, copia a resumen, valida 6863 certificados |
| **Frames analizados** | 335 |
| **Batches** | 4 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 667s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Grouped by visual changes; identical frames are noted together.

| Frames | Visible workbook / sheet | Selection / range | Action | Visible values / text | Other windows |
|---|---|---|---|---|---|
| 1–4 | Excel: **“BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel”**. Active tab appears to be **REGISTRO ATENCIONES**. Other visible tabs: **CERT RESIDENCIA PROD-ABRIL**, **CERT.P.HORIZONTAL ABRIL**, **REGISTRADO SIDE**, **Reporte PQRS Ma…** | Active cell shown as **F34**; the selected pivot value is the **Total general** cell | Reviewing/editing a **pivot table**; PivotTable Fields pane is open on the right | Clear visible total: **4328**. The right summary table is **“Registros por Atención Preferencial”**. Legible items include **Ninguna**, **Persona Mayor**, **Persona con discapacidad física**, **Persona con discapacidad intelectual-cognitiva**, **Cuidador Activo**, **Víctima de conflicto armado**, **Persona con discapacidad múltiple**, **Persona con discapacidad visual**, **Persona con discapacidad auditiva**, **Comunidad indígena**. Another pivot summarizes localities/service points and percentages | Excel ribbon visible (Archivo, Inicio, Insertar, Disposición de página, Fórmulas, Datos, Revisar, Vista, Ayuda, Acrobat, Analizar tabla dinámica, Diseño). Teams screen-sharing bar at bottom (“Dejar de compartir”) |
| 5 | Windows Explorer in **Documentos > SECGOB > BASE ORIENTACIONES SIACTUA > 2026** | File row selected: **05_SAC_atencion - Mayo 2026** | Choosing/opening the May 2026 SAC file | File list shows **01 Atenciones Enero 2026**, **02_SAC_atencion - Febrero 2026**, **03_SAC_atencion - Marzo 2026**, **04_SAC_atencion - Abril 2026**, **05_SAC_atencion - Mayo 2026** | Explorer preview pane on the right; Teams share bar still visible |
| 6 | Windows Explorer in **Documentos > SECGOB** | Folder **BASE ORIENTACIONES SIACTUA** highlighted | Navigating folders | Many folders visible (e.g. **ACCIONES RACIONALIZACION EMERGENCIA SANITARIA**, **ACTAS**, **ACTIVOS DE LA INFORMACIÓN**, **BASE ATENCIÓN COMUTADOR**, **BASE CERTIFICADOS DE RESIDENCIA**, etc.) | Preview pane says no preview available |
| 7–9 | Same Explorer window in **SECGOB** | Highlight moves among nearby folders; readable selections include **BASE ATENCIÓN COMUTADOR** and **BASE DATOS PARA PUBLICACIÓN ATRIBUTOS DE LA INFORMACIÓN** | Browsing through base folders | Folder list remains the same; no file opened yet | Same Explorer + Teams share bar |
| 10–11 | Explorer inside **BASE CERTIFICADOS DE RESIDENCIA** | Frame 10: folder **2024** selected. Frame 11: folder **2026** selected | Entering the 2026 subfolder | Visible year folders: **2020, 2021, 2022, 2023, 2024, 2025, 2026**. Also visible files: **2025 10 03 Hoja de Vida Indicadores-Certificado Residencia_SAC**, **2025 10 03 Hoja de Vida Indicadores-Propiedad Horizontal_SAC**, **base certificados de residencia 2019**, **PPT 20224600733043** | Explorer only |
| 12–13 | Explorer in **BASE CERTIFICADOS DE RESIDENCIA > 2026** | Frame 12: list focus on **ENERO 2026-PRODUCTIVIDAD-CR** area. Frame 13: same folder, same file list | Viewing monthly productivity files | Readable files: **ABRIL2026_PRODUCTIVIDAD_CR**, **ABRIL2026_PRODUCTIVIDAD_PH**, **ENERO 2026-PRODUCTIVIDAD-CR**, **ENERO 2026-PRODUCTIVIDAD-PH**, **FEBRERO 2026_PRODUCTIVIDAD_PH**, **FEBRERO 2026_PRODUCTIVIDAD_CR**, **MARZO 2026_PRODUCTIVIDAD_CR**, **MARZO 2026_PRODUCTIVIDAD_PH** | No workbook opened yet |
| 14–98 | No spreadsheet visible; **Teams call/avatar screen** | None | No visible Excel/file action | Only the centered avatar **“Yesenia Patino Figueroa”** on a black background | No workbook, no Explorer, no menus; static screen |
| 99–100 | Explorer back in **BASE CERTIFICADOS DE RESIDENCIA > 2026** | Bottom row selected: **MAYO2026_PRODUCTIVIDAD_PH** (highlighted row at the bottom) | Returning to May 2026 productivity file list | Same monthly files as above, now including **MAYO2026_PRODUCTIVIDAD_CR** and **MAYO2026_PRODUCTIVIDAD_PH** | Teams share bar still present |

Short takeaway: the sequence shows the user moving from an Excel pivot-summary workbook into Windows folders, then into the 2026 productivity files for certificate residency, with a long intervening Teams-only screen where no spreadsheet content is visible.

[Batch 2 - gpt-5.4-mini]
Here’s the frame-by-frame readout.

**101–103**
- **Workbook/sheet:** Windows File Explorer, folder `Documents > SECGOB > BASE CERTIFICADOS DE RESIDENCIA > 2026`
- **Selection:** file list only; no Excel range
- **Action:** locating the source file to open
- **Visible values:** files like `ABRIL2026_PRODUCTIVIDAD_CR`, `ENERO 2026-...`, `FEBRERO 2026-...`, `MARZO 2026-...`, `MAYO2026_PRODUCTIVIDAD_CR`, `MAYO2026_PRODUCTIVIDAD_PH`
- **Windows:** Explorer + Teams share bar + user avatar preview

**104–108**
- **Workbook/sheet:** `MAYO2026_PRODUCTIVIDAD_CR` (Protected View), sheet `PROD. TIPO T`
- **Selection:** sheet grid visible; no obvious multi-cell selection
- **Action:** viewing the “productividad por tipo de trámite” table/chart; protected view banner shows `Habilitar edición`
- **Visible data:** table for CR productivity by trámite type; chart title `PRODUCTIVIDAD DE CERTIFICADO DE RESIDENCIA - TIPO DE TRAMITE - VIGENCIA 1 AL 31 MAYO 2026`
  - `Proyectos locales` ~44.64%
  - `Requisitos laborales` ~22.43%
  - `Trámites legales` ~15.79%
  - `Trámite de estudio` ~9.01%
  - `Trámite de subsidios` ~6.25%
  - `Personas privadas de la libertad` ~1.04%
  - `Trámite ante el ministerio de rel exteriores` ~0.81%
- **Windows:** yellow protected-view bar; hourglass cursor appears in 107–108

**109–110**
- **Workbook/sheet:** same CR productivity workbook, same sheet view
- **Selection:** cursor moves within sheet; no major range change
- **Action:** normal editable view of same table/chart
- **Visible data:** same type-of-trámite table and bar chart as 104–108
- **Windows:** Excel ribbon visible; no dialog

**111–119**
- **Workbook/sheet:** `MAYO2026_PRODUCTIVIDAD_CR`, sheet `Productividad-CR`
- **Selection:** active cell visible around the table; sheet tab `Productividad-CR` highlighted
- **Action:** viewing locality-level CR productivity; likely preparing copy/move
- **Visible data:** table columns `Aprobado`, `Pendiente`, `Rechazado`, `Cerrado (Supera Subsanaciones)`, `Total general`, `%`
  - totals row: `6863`, `72`, `2544`, `817`, `13253`, `100.000%`
  - chart title `PRODUCTIVIDAD DE CERTIFICADO DE RESIDENCIA`
- **Windows:** standard Excel only

**120–125**
- **Workbook/sheet:** same CR productivity workbook
- **Selection/action:** taskbar hover previews appear; no sheet edit
- **Visible data:** still the locality productivity table/chart in background
- **Windows:** Windows app switch previews show other Excel files

**126–130**
- **Workbook/sheet:** `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026`, sheet `Hoja1`
- **Selection:** grid/data table; no special range
- **Action:** viewing PQRS report data
- **Visible data:** report header
  - `SECRETARIA DISTRITAL DE GOBIERNO`
  - `Fecha de generación de reporte: 2026-06-01`
  - `Fecha Inicial: 2026-05-01`
  - `Fecha Final: 2026-05-31`
  - `Tipo de estado: Al periodo`
  - table columns include `Número`, `Sector`, `Tipo de`, `Entidad`, `Tema`, `Estado`, `Canal`, `Asunto`, etc.
- **Windows:** Excel only

**131**
- **Workbook/sheet:** same PQRS workbook
- **Selection/action:** hourglass cursor; transition
- **Visible data:** report table still visible
- **Windows:** no new dialog

**132–137**
- **Workbook/sheet:** back to `MAYO2026_PRODUCTIVIDAD_CR`
- **Selection/action:** app switch / preview hover; no edit
- **Visible data:** CR productivity table/chart in background
- **Windows:** Excel thumbnails for other workbooks

**138–139**
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026`, sheet `REGISTRO ATENCIONES`
- **Selection:** pivot area + field list pane on right
- **Action:** inspecting pivot tables / fields
- **Visible data:** pivot blocks and `Campos de tabla dinámica`
  - visible pivot includes `Total general 4328`
  - another pivot `Registros por Atención Preferencial` with `Total general 3366`
- **Windows:** PivotTable Fields pane open

**140–146**
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026`, sheet `CERT RESIDENCIA PROD-ABRIL`
- **Selection:** table rows/cells in locality summary
- **Action:** viewing April residence validation productivity
- **Visible data:** table `PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA VALIDADOS ABRIL 2026`
  - columns: `Aprobado`, `Cerrada por desistimiento`, `Cerrado (Supera Subsanaciones)`, `Pendiente`, `Rechazado`, `Total general`, `%`
  - total row: `7941`, `3529`, `957`, `11`, `3004`, `15454`, `100%`
  - chart `PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA ABRIL 2026`
  - top localities: `Suba 12.42%`, `Tunjuelito 12.16%`, `Kennedy 11.02%`, `Ciudad Bolívar 9.27%`, `Bosa 8.13%`
- **Windows:** standard Excel

**147**
- **Workbook/sheet:** Windows task switcher
- **Selection/action:** switching apps
- **Visible data:** thumbnails of Excel windows and browser/app windows
- **Windows:** Alt-Tab style overlay

**148–153**
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026`, sheet `CERT RESIDENCIA PROD-MAYO`
- **Selection:** table cells on locality productivity
- **Action:** reviewing/confirming May residence productivity
- **Visible data:** locality table and chart (same structure as 140, but for May)
- **Windows:** Excel only

**154–167**
- **Workbook/sheet:** right-click on sheet tabs, then `Mover o copiar` dialog
- **Selection/action:** context menu on sheet tab (`Insertar`, `Eliminar`, `Cambiar nombre`, `Mover o copiar...`, `Ver código`, `Proteger hoja`, `Color de pestaña`, `Ocultar`, `Mostrar`)
- **Action:** moving/copying the sheet into another workbook/sheet
- **Visible data:** dialog `Mover o copiar`
  - destination workbook list includes `[NUEVO LIBRO]` and `BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx`
  - checkbox `Crear una copia`
- **Windows:** Excel context menu + modal dialog

**168**
- **Workbook/sheet:** Excel delete confirmation
- **Selection/action:** confirmation dialog
- **Visible data:** `Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?`
  - buttons `Eliminar` / `Cancelar`
- **Windows:** modal delete warning

**169–183**
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026`, sheet `CERT RESIDENCIA PROD-MAYO` (or copied productivity sheet)
- **Selection:** cells in the `CERTIFICADOS DE PH GENERADOS` table
- **Action:** reviewing/generated productivity and formulas
- **Visible data:** table `PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS - ABRIL 2026`
  - columns: `Localidad`, `Inscripción realizada`, `Actualización realizada`, `Extinción realizada`, `Certificados Generados`, `%`
  - total row: `19`, `451`, `0`, `470`, `100%`
  - chart title `PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS - ABRIL 2026`
- **Formula visible (183):** percentage formula shown in formula bar, `=E8/$E$26` style logic (row value divided by total-general cell)
- **Windows:** Excel only

**184–200**
- **Workbook/sheet:** same PH-generated productivity sheet
- **Selection/action:** editing/inspecting cells and chart data points
- **Visible data:** same PH table and chart
  - example row values visible:
    - `Usaquén 6 / 88 / 0 / 94 / 20.00%`
    - `Suba 0 / 81 / 0 / 81 / 17.23%`
    - `Fontibón 3 / 66 / 0 / 69 / 14.68%`
    - `Teusaquillo 3 / 48 / 0 / 51 / 10.85%`
    - `Chapinero 3 / 42 / 0 / 44 / 9.36%`
  - chart tooltip at the end shows `Series 1 Point "CIUDAD BOLIVAR" Valor: 9.817%`
- **Windows:** no extra dialog; chart tooltip is the only overlay

If you want, I can turn this into a **clean timeline table with timestamps + inferred actions** next.

[Batch 3 - gpt-5.4-mini]
Grouped by identical screen states.

| Frames | Workbook / sheet | Selection / action | Visible data / dialogs |
|---|---|---|---|
| 201-209 | `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel` / `CERT RESIDENCIA PROD-MAYO` | Viewing the productivity pivot table and bar chart; no edit yet | Table shows `Aprobados`, `Pendiente`, `Rechazado`, `Cerrado (Super Subsanaciones)`, `Total general`, `%`. Total general = `6863`, `72`, `2544`, `817`, `13253`, `100,000%`. Chart title: `PRODUCTIVIDAD DE CERTIFICADO DE RESIDENCIA VIGENCIA 1 AL 31 MAYO 2026`. |
| 210-214 | same | Cursor moves over the pivot table; preparing to reorder | No data change yet. |
| 215-220 | same | `Ordenar` dialog opens; sort configuration being adjusted | Dialog shows `Ordenar por`, `Ordenar según: Valores de celda`, `Orden: A a Z / De menor a mayor`; buttons `Agregar nivel`, `Eliminar nivel`, `Copiar nivel`, `Opciones...`, `Aceptar`, `Cancelar`. |
| 221-225 | same | Sort applied to row labels | Pivot rows reorder alphabetically by locality: `ANTONIO NARIÑO`, `BARRIOS UNIDOS`, `BOSA`, `CANDELARIA`, `CHAPINERO`, `CIUDAD BOLÍVAR`, `ENGATIVÁ`, `FONTIBÓN`, `KENNEDY`, etc. Chart updates to match the new order. |
| 226-229 | same | Cursor moves around the totals row / chart area | Table still shows the same totals and percentages; no value change. |
| 230-232 | same | Slight repositioning/scrolling on the same sheet | Same productivity table and chart, still on `CERT RESIDENCIA PROD-MAYO`. |
| 233-236 | `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel` / `DIAPOSITIVA No. 3` | Switching to the summary sheet and filling column `CERT. RESIDENCIA No. 6` | Visible rows include `ANTONIO NARIÑO 45`, `BARRIOS UNIDOS 143`, `BOSA 609`, `CANDELARIA 36`, `CHAPINERO 179`, `CIUDAD BOLÍVAR 713`, `ENGATIVÁ 434`, `FONTIBÓN 537`, `KENNEDY 677`, `LOS MÁRTIRES 60`, `PUENTE ARANDA 134`, `RAFAEL URIBE URIBE 387`, `SAN CRISTÓBAL 306`, `SANTA FE 102`, `SUBA 902`, `SUMAPAZ 20`, `TEUSAQUILLO 235`, `TUNJUELITO 491`, `USAQUÉN 310`, `USME 543`, `NIVEL CENTRAL 497`, `SUPERCADES 0`, `EN BLANCO 0`, `TOTAL GENERAL 6.863`. Right-click context menu is open in the next frame. |
| 237-255 | `MAYO2026_PRODUCTIVIDAD_CR - Excel` / `Productividad-CR` | Back to the source productivity workbook; checking formulas/totals | Formula bar shows `=SUMA(G19:G25)` on the total area. Table still has total `6863` and the same productivity breakdown. Tabs visible: `Hoja1`, `Hoja3`, `Sheet1`, `Productividad-CR`, `PROD. TIPO T`. |
| 256-268 | same | Minor cursor movement across the totals row and table | No content change; productivity table and chart remain visible. |
| 269 | app switcher / Alt-Tab | Switching windows | Thumbnails show multiple open windows, including the productivity workbook, the base-data workbook, Teams screen share, File Explorer, and a document/PDF window. |
| 270-273 | `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel` / `DIAPOSITIVA No. 3` | Back on the summary sheet; lower rows visible | Lower part of the table shows `SUBA 902`, `SUMAPAZ 20`, `TEUSAQUILLO 235`, `TUNJUELITO 491`, `USAQUÉN 310`, `USME 543`, `NIVEL CENTRAL 497`, `SUPERCADES 0`, `EN BLANCO 0`, `TOTAL GENERAL 1.168 / 1.723 / 4.328 / - / 6.863 / - / -`. |
| 274-299 | `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel` / `CERT RESIDENCIA PROD-MAYO` | Back to the productivity sheet; chart object gets selected | The bar chart is selected (handles visible). Table still shows the same CR productivity values and total `6863`. No data edits visible. |
| 300 | same | `Ordenar` dialog opens again | Sort dialog shows `Etiquetas de fila`, `Valores de celda`, `A a Z`; same reorder workflow being revisited. |

Key transitions:
- Source data is copied from `Productividad-CR` into `DIAPOSITIVA No. 3`.
- The locality rows are sorted alphabetically in the productivity pivot.
- The key validation number stays `6863` certificates.

[Batch 4 - gpt-5.4-mini]
Here’s the frame-by-frame readout.

### Frames 00301–00307
**Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, sheet `CERT RESIDENCIA PROD-MAYO`  
**Selected/modified:** sort dialog over the CR table; sorting field set to `%`  
**Action:** configuring sort for the CR productivity table  
**Visible data:** table titled `PRODUCTIVIDAD DE CERTIFICADO DE RESIDENCIA VIGENCIA 1 AL 31 MAYO 2026`; columns `Etiquetas de fila`, `Aprobados`, `Pendiente`, `Rechazado`, `Cerrado (Supera Subsanaciones)`, `Total general`, `%`  
**Dialog/windows:** Excel `Ordenar` dialog open; dropdown for `Ordenar por` shows fields like `Aprobados`, `Pendiente`, `Rechazado`, `Cerrado...`, `Total general`, `%`  
- **00301–00303:** dropdown list open  
- **00304:** `%` selected, order shown as `De menor a mayor`  
- **00305–00306:** order dropdown open with `De menor a mayor` / `De mayor a menor` / `Lista personalizada`  
- **00307:** cursor on `Aceptar`

### Frames 00308–00323
**Workbook/sheet:** same workbook, same sheet `CERT RESIDENCIA PROD-MAYO`  
**Selected/modified:** no dialog; table now sorted  
**Action:** sorted CR table is displayed with chart on the right  
**Visible data (top rows after sort):**
- `SUBA` — `902`, `12`, `345`, `118`, `1710`, `12,903%`
- `KENNEDY` — `677`, `5`, `276`, `98`, `1344`, `10,141%`
- `CIUDAD BOLIVAR` — `713`, `3`, `287`, `65`, `1334`, `9,817%`
- `TUNJUELITO` — `491`, `7`, `195`, `51`, `1134`, `8,557%`
- `BOSA` — `609`, `8`, `204`, `69`, `1110`, `8,375%`
- `FONTIBON` — `537`, `2`, `193`, `57`, `938`, `7,078%`
- `USME` — `543`, `2`, `204`, `69`, `932`, `7,032%`
- `ENGATIVÁ` — `434`, `5`, `169`, `54`, `883`, `6,663%`
- `RAFAEL URIBE URIBE` — `387`, `13`, `145`, `49`, `716`, `5,403%`
- `SAN CRISTOBAL` — `306`, `2`, `119`, `36`, `561`, `4,233%`
- `TEUSAQUILLO` — `235`, `2`, `66`, `24`, `416`, `3,139%`
- `CHAPINERO` — `179`, `2`, `82`, `43`, `385`, `2,905%`
- `BARRIOS UNIDOS` — `143`, `2`, `72`, `18`, `308`, `2,324%`
- `PUENTE ARANDA` — `134`, `1`, `48`, `10`, `249`, `1,879%`
- `SANTA FE` — `102`, `2`, `49`, `13`, `206`, `1,554%`
- `LOS MARTIRES` — `60`, `1`, `26`, `9`, `125`, `0,943%`
- `ANTONIO NARIÑO` — `45`, `0`, `18`, `5`, `97`, `0,732%`
- `CANDELARIA` — `36`, `0`, `13`, `5`, `80`, `0,604%`
- `SUMAPAZ` — `20`, `2`, `4`, `3`, `32`, `0,241%`
- `Total general` — `6863`, `72`, `2544`, `817`, `13253`, `100,000%`
**Dialogs/windows:** chart on right titled `PRODUCTIVIDAD DE CERTIFICADO DE RESIDENCIA VIGENCIA 1 AL 31 MAYO 2026`; Teams sharing overlay visible (`teams.microsoft.com está compartiendo tu pantalla`)  
- **00308:** sort applied; table order updated  
- **00309–00323:** same sorted view, cursor moves around table/chart

### Frames 00324–00325
**Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, sheet `CERT.P.HORIZONTAL ABRIL`  
**Selected/modified:** table area on left, chart on right  
**Action:** switched from CR sheet to PH productivity sheet  
**Visible data:** `PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS / ABRIL 2026`  
Columns: `Localidad`, `Inscripción realizada`, `Actualización realizada`, `Extinción realizada`, `Certificados Generados`, `%`  
Readable values:
- `CANDELARIA` — `0`, `1`, `0`, `1`, `0,21%`
- `LOS MARTIRES` — `0`, `2`, `0`, `2`, `0,43%`
- `RAFAEL URIBE URIBE` — `0`, `2`, `0`, `2`, `0,43%`
- `TUNJUELITO` — `0`, `3`, `0`, `3`, `0,64%`
- `PUENTE ARANDA` — `2`, `1`, `0`, `3`, `0,64%`
- `CIUDAD BOLIVAR` — `0`, `5`, `0`, `5`, `1,06%`
- `USME` — `0`, `6`, `0`, `6`, `1,28%`
- `ANTONIO NARIÑO` — `0`, `7`, `0`, `7`, `1,49%`
- `BARRIOS UNIDOS` — `1`, `6`, `0`, `7`, `1,49%`
- `SAN CRISTOBAL` — `0`, `12`, `0`, `12`, `2,55%`
- `SANTA FE` — `1`, `11`, `0`, `12`, `2,55%`
- `BOSA` — `0`, `13`, `0`, `13`, `2,77%`
- `ENGATIVÁ` — `0`, `17`, `0`, `17`, `3,62%`
- `KENNEDY` — `0`, `41`, `0`, `41`, `8,72%`
- `CHAPINERO` — `3`, `41`, `0`, `44`, `9,36%`
- `TEUSAQUILLO` — `3`, `48`, `0`, `51`, `10,85%`
- `FONTIBON` — `3`, `66`, `0`, `69`, `14,68%`
- `SUBA` — `0`, `81`, `0`, `81`, `17,23%`
- `USAQUEN` — `6`, `88`, `0`, `94`, `20,00%`
- `Total general` — `19`, `451`, `0`, `470`, `100%`
**Dialogs/windows:** same workbook, chart on right titled `PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS / ABRIL 2026`  
- **00324:** PH sheet visible  
- **00325:** taskbar hover/preview over Excel windows

### Frame 00326
**Workbook/sheet:** `MAYO2026_PRODUCTIVIDAD_CR - Excel`, sheet `Productividad-CR`  
**Selected/modified:** cell `F1` (visible name box shows `F1`) / no editing visible  
**Action:** CR workbook reopened or switched into focus  
**Visible data:** same CR table and chart as above; totals visible:
- `Aprobados 6863`
- `Pendiente 72`
- `Rechazado 2544`
- `Cerrado (Supera Subsanaciones) 817`
- `Total general 13253`
- `% 100,000%`
**Dialogs/windows:** Excel workbook with tabs `Hoja1`, `Hoja3`, `Sheet1`, `Productividad-CR`, `PROD. TIPOT`

### Frames 00327–00332
**Workbook/sheet:** same `MAYO2026_PRODUCTIVIDAD_CR - Excel`, same sheet  
**Selected/modified:** close button / save prompt  
**Action:** closing workbook; Excel asks to save changes  
**Visible data:** CR table and chart dimmed behind dialog  
**Dialog/windows:** Microsoft Excel save confirmation:
`¿Desea guardar los cambios efectuados en 'MAYO2026_PRODUCTIVIDAD_CR.xlsm'?`
Buttons: `Guardar`, `No guardar`, `Cancelar`
- **00327:** cursor at top-right close `X`
- **00328–00332:** save dialog remains open, cursor moves over `Guardar` / dialog fades slightly during interaction

### Frames 00333–00334
**Workbook/sheet:** back to `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, sheet `CERT.P.HORIZONTAL ABRIL`  
**Selected/modified:** same PH sheet/table  
**Action:** returned to PH productivity sheet after window switch  
**Visible data:** same PH table and chart as 00324  
**Dialogs/windows:** Teams overlay still visible; bottom taskbar thumbnails appear
- **00333:** PH sheet in Excel
- **00334:** taskbar hover showing File Explorer thumbnails

### Frame 00335
**Window:** File Explorer  
**Path visible:** `Documents > SECGOB > BASE CERTIFICADOS DE RESIDENCIA > 2026`  
**Selected/modified:** file selection in the folder list  
**Action:** browsing the output directory / verifying generated files  
**Visible files:**  
- `ABRIL2026_PRODUCTIVIDAD_CR`
- `ABRIL2026_PRODUCTIVIDAD_PH`
- `ENERO 2026-PRODUCTIVIDAD-CR`
- `ENERO 2026-PRODUCTIVIDAD-PH`
- `FEBRERO 2026_PRODUCTIVIDAD_PH`
- `FEBRERO 2026_PRODUCTIVIDAD_CR`
- `MARZO 2026_PRODUCTIVIDAD_CR`
- `MARZO 2026_PRODUCTIVIDAD_PH`
- `MAYO2026_PRODUCTIVIDAD_CR`
- `MAYO2026_PRODUCTIVIDAD_PH`

### Main transition notes
- **CR sheet → PH sheet:** frame `00324`
- **CR workbook close/save prompt:** frames `00327–00332`
- **Excel → File Explorer folder check:** frame `00335`

If you want, I can turn this into a clean chronological log table with columns: `frame`, `sheet`, `action`, `data`, `UI`.

---

## Segmento 6: Propiedad horizontal — certificados generados

| Campo | Valor |
|---|---|
| **Duración** | 22:35 - 30:00 |
| **Descripción** | Mismo ejercicio con PH: inscripción, actualización, extensión, copia certificados generados, valida 809 certificados |
| **Frames analizados** | 445 |
| **Batches** | 5 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 764s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Skills cargadas: `input-compressor`, `english-prompt-compiler`, `skill-router`

### Prompt in English
Analyze the attached frames from segment “Propiedad horizontal — certificados generados (part 1/5)” (minute 22:35–30:00). For each frame, identify the Excel workbook and sheet, selected cells/ranges, the action being performed, visible values/data, and any open menus/dialogs/windows. Be exact and ignore non-relevant overlay content.

### Notes
- Assumptions: consecutive identical frames can be grouped if nothing changes.
- Safety constraints: none.
- Missing critical inputs: none.

### Análisis por estado/frame
| Frames | Libro/hoja visible | Selección / rango | Acción | Datos visibles | Menús / ventanas |
|---|---|---|---|---|---|
| 1 | Explorador de archivos en carpeta `2026` | — | Revisar archivos fuente | Archivos como `ABRIL2026_PRODUCTIVIDAD_CR`, `ABRIL2026_PRODUCTIVIDAD_PH`, `MAYO2026_PRODUCTIVIDAD_CR`, `MAYO2026_PRODUCTIVIDAD_PH` | Teams compartiendo pantalla |
| 2-4 | `BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel`, hoja `CERT.P.HORIZONTAL ABRIL` | Sin selección clara | Visualizar tabla/gráfico | Tabla “PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS / ABRIL 2026”. Total: `19`, `451`, `0`, `470`, `100%`. Gráfico con Usaquén `20.00%`, Suba `17.23%`, Fontibón `14.68%`, Teusaquillo `10.85%`, Chapinero `9.36%`, Kennedy `8.72%`, Engativá `3.62%`, Bosa `2.77%`, etc. | Teams compartiendo pantalla |
| 5-14 | `MAYO2026_PRODUCTIVIDAD_PH [Vista protegida] - Excel`, hoja `RESUMEN` | Sin selección visible | Revisar resumen PH generado | Tabla “PRODUCTIVIDAD DE CERTIFICADOS DE PROPIEDAD HORIZONTAL / CERTIFICADOS VALIDADOS VIGENCIA MAYO 2026”. Totales: `1631`, `486`, `33`, `274`, `8`, `2432`, `100%`. Gráfico de localidades (Usaquén, Suba, Teusaquillo, etc.) | Teams + panel de participante a la derecha |
| 15-16 | `MAYO2026_PRODUCTIVIDAD_PH`, hoja `ACT` | Sin selección visible | Ver otra tabla resumen | Totales: `788`, `1548`, `446`, `8`, `263`, `3053`, `100%` | Teams |
| 17-21 | `MAYO2026_PRODUCTIVIDAD_PH`, hoja `INS` | Sin selección visible | Ver tabla de inscripción | “INSCRIPCION VIGENCIA MAYO 2026”. Totales: `21`, `83`, `40`, `33`, `11`, `188`, `100%` | Teams |
| 22 | `MAYO2026_PRODUCTIVIDAD_PH`, hoja `RESUMEN` | Pivot en vista | Configurar/inspeccionar tabla dinámica | Panel de campos: `Estado de la solicitud` y `Localidad` marcados. Columnas visibles: `Actualizacion Generada`, `Aprobado`, `Cerrada por desistimiento`, `Cerrado (Supera Subsanaciones)`, `Devuelto`, `En trámite`, `Para subsanar`, `Subsanado`, `(en blanco)`, `Total general`. Totales visibles: `788`, `0`, `8`, `263`, `3`, `1326`, `446`, `219`, `3035` | “Campos de tabla dinámica” abierto |
| 23-39 | `BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel`, hoja `CERT.P.HORIZONTAL ABRIL` | Sin selección clara | Volver a la tabla original | Misma tabla de PH generados de abril: total `470`, con `19` inscripciones, `451` actualizaciones, `0` extinciones | Teams |
| 40-49 | `BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel`, hoja `RESUMEN` | Pestaña `RESUMEN` activa | Preparar mover/copiar hoja | Tabla “CERTIFICADOS GENERADOS VIGENCIA MAYO 2026”. Total: `21`, `788`, `0`, `809`, `100%`. Gráfico con Usaquén `36.218%`, Suba `13.597%`, Teusaquillo `12.979%`, Chapinero `12.237%`, Engativá `8.72%`, Kennedy `6.18%`, Fontibón `4.69%`, Bosa `2.34%`, Santa Fe `2.34%`, etc. | Clic derecho en pestaña `RESUMEN`; menú contextual con `Eliminar`, `Cambiar nombre`, `Mover o copiar...`, `Ver código`, `Proteger hoja`, etc. |
| 50-55 | Mismo libro | — | Abrir diálogo de mover/copiar | Lista de hojas destino: `BASE-I`, `BASE-A`, `INS`, `ACT`, `RESUMEN` | Diálogo `Mover o copiar` con `Crear una copia` |
| 56-57 | Vuelta a `RESUMEN` | Sin cambio visible | Retornar a la hoja | Misma tabla y gráfico, sin edición visible | Teams |
| 58-88 | Mismo libro, pestaña `RESUMEN` | Pestaña | Preparar eliminación / cambio de nombre | Sin cambio de datos | Menú contextual repetido sobre la pestaña |
| 89 | Excel confirmación | — | Confirmar borrado de hoja | Mensaje: “Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?” | Diálogo `Eliminar / Cancelar` |
| 90-91 | `BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel`, hoja `REGISTRADO SIDE` | Celda seleccionada `Y12` con valor `666` | Revisar pivote por localidad | Pivot con `LOCALIDAD` y `Sum de TOTAL`: `CANDELARIA 96`, `ENGATIVÁ 98`, `FONTIBÓN 48`, `KENNEDY 18`, `MARTIRES 70`, `NIVEL CENTRAL 693`, `SANTA FE 15`, `SUBA 19`, `TEUSAQUILLO 666`, `Total general 1723` | Panel “Campos de tabla dinámica” abierto |
| 92-100 | Vuelta a `CERT.P.HORIZONTAL ABRIL` / `CERT.P.HORIZONTAL MAYO` | Se mueve el foco por celdas/pestañas | Navegación sin edición visible | Misma tabla de PH generados; no se aprecian fórmulas nuevas | Teams |

No vi fórmulas legibles en estos frames.

[Batch 2 - gpt-5.4-mini]
Here’s the frame analysis, grouped by identical spans.

### Frames 101–104
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, tab **CERT.P.HORIZONTAL MAYO**
- **Selection:** pivot table area around **E6**; formula bar shows **`=SUMA(B6:D6)`**
- **Action:** reviewing the pivot table / chart, no edit yet
- **Values visible:** total **809** certificates; columns **Inscripción realizada**, **Actualización realizada**, **Extinción realizada**, **Certificados Generados**, **%**
  - USAQUEN **293 / 36.218%**
  - SUBA **110 / 13.597%**
  - TEUSAQUILLO **105 / 12.979%**
  - FONTIBON **98 / 12.237%**
  - KENNEDY **50 / 6.180%**
  - CHAPINERO **38 / 4.697%**
  - BOSA **19 / 2.349%**
  - ENGATIVÁ **17 / 2.101%**
  - PUENTE ARANDA **15 / 1.854%**
  - TUNJUELITO **13 / 1.607%**
  - SANTA FE and SAN CRISTOBAL **10 / 1.236%**
  - CANDELARIA **9 / 1.112%**
  - BARRIOS UNIDOS **7 / 0.865%**
  - USME **6 / 0.742%**
  - ANTONIO NARIÑO **4 / 0.494%**
  - CIUDAD BOLÍVAR **3 / 0.371%**
  - LOS MARTIRES **1 / 0.124%**
  - RAFAEL URIBE URIBE **0 / 0.000%**
- **Windows/menus:** no dialog open; chart on the right mirrors the same ranking

### Frames 105–112
- **Workbook/sheet:** same workbook, **CERT.P.HORIZONTAL MAYO**
- **Selection:** sort dialog over the table
- **Action:** sorting the pivot by **row labels**
- **Menus/dialogs:** Excel **Ordenar** dialog open
  - field dropdown shows: **Etiquetas de fila**, **Inscripción realizada**, **Actualización realizada**, **Extinción realizada**, **Certificados Generados**, **%**
  - sort field set to **Etiquetas de fila**
  - order set to **A a Z / De menor a mayor**
- **Values:** no data changed yet in the sheet; just preparing the sort

### Frames 113–129
- **Workbook/sheet:** same workbook, **CERT.P.HORIZONTAL MAYO**
- **Selection:** table itself after sorting
- **Action:** sort applied
- **Values visible:** rows now alphabetized:
  **ANTONIO NARIÑO, BARRIOS UNIDOS, BOSA, CANDELARIA, CHAPINERO, CIUDAD BOLÍVAR, ENGATIVÁ, FONTIBON, KENNEDY, LOS MARTIRES, PUENTE ARANDA, RAFAEL URIBE URIBE, SAN CRISTOBAL, SANTA FE, SUBA, SUMAPAZ, TEUSAQUILLO, TUNJUELITO, USAQUEN, USME**
- **Windows/menus:** sort dialog closed
- **Chart:** still visible on the right and still ordered by values (USAQUEN at top)

---

### Frames 130–145
- **Workbook/sheet:** same workbook, tab **RESUMEN CIFRAS**
- **Selection:** active in the summary table, mostly around **column F** (CERT. PROPIEDAD / CERT. RESIDENCIA area)
- **Action:** reviewing / filling the summary sheet
- **Visible table title:** **DIAPOSITIVA No. 3**
- **Visible columns:**  
  **ALCALDÍA LOCAL**, **PQRS PENDIENTES N. 2**, **DOC.EXT. N. 3**, **ORIENTACIONES No. 4**, **CERT. PROPIEDAD No. 5**, **CERT. RESIDENCIA No. 6**, **ENCUESTAS DEL PERIODO**, **ENCUESTAS CON RESPUESTA COMPLETA**, **CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS**
- **Values visible (examples):**
  - SUBA: **75 / 19 / 180 / 110 / 902**
  - SUMAPAZ: **3 / 0 / 3 / 0 / 20**
  - TEUSAQUILLO: **10 / 666 / 251 / 105 / 235**
  - TUNJUELITO: **30 / 0 / 167 / 13 / 491**
  - USAQUEN: **59 / 0 / 316 / 293 / 310**
  - USME: **50 / 0 / 112 / 6 / 543**
  - NIVEL CENTRAL: **497 / 693 / 843 / 0 / 0**
  - SUPERCADES: **0 / 0 / 406 / 0 / 0**
  - EN BLANCO: **0 / 0 / 0 / 0 / 0**
- **Totals visible:**  
  **1.168**, **1.723**, **4.328**, **809**, **6.863**
- **Windows/menus:** no dialog; just the spreadsheet

### Frames 146–150
- **Workbook/sheet:** same, **RESUMEN CIFRAS**
- **Selection:** lower portion of the same table
- **Action:** scrolling to inspect the lower rows and totals
- **Values visible:** same summary data; bottom totals still show **6.863** in the total row
- **Windows/menus:** none

### Frames 151–157
- **Workbook/sheet:** same, **RESUMEN CIFRAS**
- **Selection:** a cell/range in the table is right-clicked
- **Action:** context menu opened, likely preparing copy/paste or sort
- **Windows/menus:** Excel right-click menu open with:
  - **Cortar**
  - **Copiar**
  - **Opciones de pegado**
  - **Pegado especial**
  - **Buscar inteligente**
  - **Insertar celdas copiadas...**
  - **Eliminar...**
  - **Borrar contenido**
  - **Ordenar**
  - **Obtener datos de Tabla/Rango...**
  - **Insertar comentario**
  - **Formato de celda...**
  - **Elegir de la lista desplegable...**
  - **Definir nombre...**
  - **Vínculo**
- **Values:** same summary table in background

### Frames 158–160
- **Workbook/sheet:** same workbook in background
- **Action:** Windows task-switch / Explorer previews briefly appear at the bottom
- **Windows/menus:** thumbnail previews from File Explorer/task switcher overlay Excel
- **Values:** no sheet change, no data change

### Frames 161–170
- **Workbook/sheet:** back on **RESUMEN CIFRAS**
- **Selection:** **F27** / total area; formula bar shows **`=SUMA(F4:F26)`**
- **Action:** verifying totals in the summary sheet
- **Values visible:**  
  - total row shows **B27 = 1.168**
  - **C27 = 1.723**
  - **D27 = 4.328**
  - **F27 = 809**
  - **E27 = 6.863**
- **Windows/menus:** none
- **Note:** the column F values are filled for the locality rows; the sheet is being validated against the 809 total

---

### Frames 171–173
- **Workbook/sheet:** back to **CERT.P.HORIZONTAL MAYO**
- **Selection:** around **G7** in the pivot table/chart area
- **Action:** preparing another sort / review on the pivot
- **Values:** same 809-certificate pivot and percentage chart
- **Windows/menus:** none

### Frames 174–178
- **Workbook/sheet:** same, **CERT.P.HORIZONTAL MAYO**
- **Selection:** Excel **Ordenar** dialog open again
- **Action:** sort setup
- **Windows/menus:** sort dialog shows:
  - column field dropdown
  - **Etiquetas de fila**
  - order **De menor a mayor**
- **Values:** no data changed yet

### Frames 179–187
- **Workbook/sheet:** same, **CERT.P.HORIZONTAL MAYO**
- **Selection:** sorted pivot table visible
- **Action:** sort applied / reviewed
- **Values visible:** alphabetical row order again; chart still shows value ranking with **USAQUEN 36.218%** at the top
- **Windows/menus:** no dialog

### Frames 188–200
- **Workbook/sheet:** returns to **RESUMEN CIFRAS**
- **Selection:** lower rows / totals area
- **Action:** final verification scroll through the summary sheet
- **Values visible:** same totals and row values, no new edits
- **Windows/menus:** none

If you want, I can turn this into a **clean timestamped shot list** next.

[Batch 3 - gpt-5.4-mini]
Frames 201-202:
- Excel workbook: **“BASE DATOS PQR LOCALIDADES MAYO 2026 - Excel”**
- Visible sheet/tab: **RESUMEN CIFRAS** (active)
- Selected cell: **G2** (shown in the name box)
- Action: **viewing/reviewing** a summary table; no formula or edit visible
- Visible data: title **“DIAPOSITIVA No. 3”** and columns for **ALCALDÍA LOCAL, PQRS PENDIENTES N. 2, DOC. EXT. N. 3, ORIENTACIONES No. 4, CERT. PROPIEDAD No. 5, CERT. RESIDENCIA No. 6, ENCUESTAS DEL PERIODO, ENCUESTAS CON RESPUESTA COMPLETA, CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS**
- Readable rows include:
  - **ANTONIO NARIÑO**: 29, 0, 61, 4, 45
  - **BARRIOS UNIDOS**: 19, 0, 264, 7, 143
  - **BOSA**: 59, 0, 61, 19, 609
  - **CANDELARIA**: 34, 96, 45, 9, 36
  - **CHAPINERO**: 23, 0, 63, 38, 179
  - **CIUDAD BOLIVAR**: 26, 0, 295, 3, 713
  - **ENGATIVÁ**: 37, 98, 362, 17, 434
  - **FONTIBÓN**: 59, 48, 133, 99, 537
  - **KENNEDY**: 46, 18, 312, 50, 677
  - **MÁRTIRES**: 7, 70, 60, 1, 60
  - **PUENTE ARANDA**: 10, 0, 58, 15, 134
  - **RAFAEL URIBE**: 35, 0, 95, 0, 387
  - **SAN CRISTÓBAL**: 28, 0, 182, 0, 306
- Open UI/windows:
  - **Excel Data ribbon** open
  - **Teams screen-sharing banner**: “teams.microsoft.com está compartiendo tu pantalla” with **Dejar de compartir**
  - Participant thumbnail on the right: **Yesenia Patino Figueroa**

Frame 203 onward (same visual state repeated through 300):
- Screen switches to a **black Teams placeholder view**
- Only visible content: centered circular avatar + name **“Yesenia Patino Figueroa”**
- No Excel workbook, no sheet, no cells, no menus, no dialogs visible
- No action visible; it looks like the feed is on a participant/meeting placeholder screen

Transition note:
- There is a clear transition from the Excel table view in **202-202** to the black Teams placeholder in **203**.

[Batch 4 - gpt-5.4-mini]
All frames in this batch are identical.

- **Visible app/window:** likely a video call tile (Teams/Zoom-style), not Excel
- **Workbook/sheet:** none visible
- **Cells/ranges:** none visible
- **Action:** no observable action; static screen / participant avatar
- **Visible data/text:** `Yesenia Patino Figueroa`
- **Menus/dialogs:** none

**Transition:** none across the frames; the image stays unchanged.

So: there is **no Excel content to read in these frames**.

[Batch 5 - gpt-5.4-mini]
All visible frames are identical: **no Excel workbook is on screen**.

- **Visible UI/window:** a black full-screen video-call placeholder (likely Teams/meeting), with a centered circular profile photo.
- **Text visible:** `Yesenia Patiño Figueroa`
- **Workbook/sheet:** none visible
- **Selected cells/ranges:** none
- **Action being performed:** none visible; this looks like a static participant tile / camera-off screen
- **Menus/dialogs:** none

**Transition:** no change across the frames shown; they appear frozen on the same screen.

---

## Segmento 7: Encuestas — procesamiento completo

| Campo | Valor |
|---|---|
| **Duración** | 30:00 - 45:30 |
| **Descripción** | Reporte mensual de encuestas, respuestas completas vs incompletas, calificación, porcentaje, tabla por canales (virtual, presencial, telefónico) |
| **Frames analizados** | 930 |
| **Batches** | 10 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 879s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
All frames in seg007 appear identical.

- **Visible app/window:** not Excel; looks like a **Teams/meeting placeholder** or video-call tile
- **Visible content:** centered circular profile photo with the name **“Yesenia Patiño Figueroa”**
- **Workbook/sheet:** **none visible**
- **Selected cells/ranges:** **none**
- **Action being performed:** **no observable Excel action**
- **Menus/dialogs:** **none**

**Text read:** `Yesenia Patiño Figueroa`

**Transition:** none across the frames; it’s a static screen.

If you want, I can also format this as a **frame-by-frame log** with timestamps, but the content would repeat for every frame.

[Batch 2 - gpt-5.4-mini]
All the frames you provided are visually identical: a black screen with a centered circular profile photo and the name **“Yesenia Patino Figueroa”** underneath.

So, for **every frame (00101–00200)**:

1. **Excel workbook/sheet visible:** **None**
2. **Selected/modified cells/ranges:** **None visible**
3. **Action being performed:** **No Excel action visible**
4. **Values/data visible:** Only the name **Yesenia Patino Figueroa**
5. **Menus/dialogs/windows open:** **None visible** — this looks like a profile/meeting tile or placeholder screen, not Excel

**Transition note:** No screen change is visible across the frames; they appear to be the same static image repeated.

If you want, send the actual Excel frames and I’ll do the same level of exact frame-by-frame extraction.

[Batch 3 - gpt-5.4-mini]
All provided frames are identical.

- **Visible app/window:** a video-call style placeholder screen, likely **Teams/Zoom**, not Excel.
- **Visible content:** centered circular profile photo with the name **“Yesenia Patino Figueroa”** below it.
- **Workbook/sheet:** **none visible**
- **Selected/modified cells/ranges:** **none**
- **Action performed:** **no visible spreadsheet action**
- **Values/data readable:** only the name **Yesenia Patino Figueroa**
- **Menus/dialogs/windows:** no Excel menus, no dialogs, no table, no formulas

**Transition note:** no screen change across the frames; they remain on the same static call/avatar screen.

[Batch 4 - gpt-5.4-mini]
All frames `frame_00301.jpg` through `frame_00400.jpg` appear identical.

1. **Workbook/sheet visible:** None. No Excel workbook, file name, or tab is visible.
2. **Cells/ranges selected:** None.
3. **Action being performed:** No spreadsheet action visible; it looks like a static avatar/call screen.
4. **Values/data visible:** Only the name **“Yesenia Patino Figueroa”** under a centered circular profile photo.
5. **Menus/dialogs/windows open:** None. No Excel, Teams, or other UI panels visible.

**Transition note:** No visible transition between frames; the screen stays the same throughout this segment.

[Batch 5 - gpt-5.4-mini]
All frames shown here are effectively identical.

- **Visible app/window:** likely a video-call/meeting tile, not Excel
- **Workbook/sheet:** **none visible**
- **Selected cells/ranges:** **none**
- **Action:** no detectable spreadsheet action
- **Visible data/text:** only the profile name **“Yesenia Patino Figueroa”**
- **Menus/dialogs/windows:** none visible

**Transition:** no screen change across the frames you provided; they all show the same black screen with a centered circular avatar.

If you want, I can turn this into a per-frame table, but the content would be the same for each frame.

[Batch 6 - gpt-5.4-mini]
All shown frames (`frame_00501.jpg`–`frame_00600.jpg`) are effectively identical.

1. **Excel workbook/sheet visible:** None.
2. **Selected/modified cells/ranges:** None visible.
3. **Action being performed:** No spreadsheet action visible; static screen.
4. **Values/data visible:** Only the name **“Yesenia Patino Figueroa”** under a centered circular profile image.
5. **Menus/dialogs/windows open:** None visible; this looks like a **Teams/meeting placeholder or profile tile**, not Excel.

**Text read:** “Yesenia Patino Figueroa”  
**Formula read:** None  
**Transition between frames:** None detected; the screen is static throughout.

[Batch 7 - gpt-5.4-mini]
All frames shown (frame_00601–frame_00700) are the same static screen.

- No Excel workbook or sheet is visible
- No selected cells, ranges, formulas, or edits visible
- No menus/dialogs/windows from Excel, Teams, or Visage visible
- Visible content: black background, centered circular profile photo, name label “Yesenia Patino Figueroa”
- No visual transition across frames

So: this segment does **not** show spreadsheet processing on-screen; it looks like a paused/idle call screen.

[Batch 8 - gpt-5.4-mini]
No hay Excel en estas capturas.

**Frames 00701–00800:** todos muestran la **misma pantalla estática**:
- **Ventana/app visible:** fondo negro con un **avatar circular** centrado y el nombre **“Yesenia Patiño Figueroa”** debajo.
- **Workbook/sheet:** **ninguno visible**.
- **Celdas/rangos:** **ninguno**.
- **Acción:** **ninguna**; no se ve edición, selección ni navegación.
- **Valores/texto leído:** solo **“Yesenia Patiño Figueroa”**.
- **Menús/diálogos:** **ninguno**.
- **Transición entre frames:** **no hay cambio**; es la misma imagen repetida.

Si quieres, puedo hacer el análisis de un segmento que sí contenga la hoja de Excel.

[Batch 9 - gpt-5.4-mini]
All shown frames are the same static screen:

- **Visible app/window:** not Excel; just a black screen with a centered circular profile photo and the name **“Yesenia Patino Figueroa”**.
- **Workbook/sheet:** **none visible**.
- **Selected cells/ranges:** **none**.
- **Action being performed:** no visible spreadsheet action; this looks like a video-call/avatar placeholder screen.
- **Visible data/text:** only **“Yesenia Patino Figueroa”**.
- **Menus/dialogs/windows:** none.

**Transition:** no change across the frames provided; they are visually identical.

[Batch 10 - gpt-5.4-mini]
All shown frames are effectively identical.

**Visible content in each frame (00901–00930):**
1. **Workbook/sheet:** none visible
2. **Selected cells/ranges:** none visible
3. **Action:** no Excel action visible; static screen
4. **Values/data:** only the name **“Yesenia Patiño Figueroa”** is readable
5. **Menus/dialogs/windows:** a black screen with a centered circular profile photo; no Excel, Teams, or Visage UI controls visible

**Transition:** none. No frame change is observable; this looks like the same idle/placeholder screen repeated.

So: **there is no analyzable Excel content in these frames**.

---

## Segmento 8: Informe PQRS página web — setup inicial

| Campo | Valor |
|---|---|
| **Duración** | 45:30 - 60:00 |
| **Descripción** | Duplica mes anterior, copia sábana de datos, agrega columna duplicados, elimina hojas anteriores, renombra |
| **Frames analizados** | 870 |
| **Batches** | 9 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 851s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
All provided frames are identical: a black screen with a centered circular profile photo labeled **“Yesenia Patino Figueroa”**.

- **Workbook/sheet:** none visible
- **Selected cells/ranges:** none visible
- **Action:** no Excel action visible
- **Values/data:** only the name text under the avatar
- **Menus/dialogs/windows:** none visible

**Transition:** no change across frames; it stays on the same static black profile screen.

[Batch 2 - gpt-5.4-mini]
I can’t identify any Excel activity in these frames.

All frames from `frame_00101.jpg` to `frame_00200.jpg` show the same static screen:
- black background
- centered circular profile image
- visible name text: `Yesenia Patino Figueroa`

So for each frame:
1. **Workbook/sheet:** none visible
2. **Cells/ranges:** none visible
3. **Action:** none visible
4. **Values/data:** only `Yesenia Patino Figueroa`
5. **Menus/dialogs/windows:** none visible

No transitions, formulas, or Excel UI elements appear in the provided frames.

[Batch 3 - gpt-5.4-mini]
I can’t extract any Excel activity from these frames.

**What’s visible in every frame (00201–00300):**
- A black screen
- Centered circular profile photo
- Name text: **“Yesenia Patino Figueroa”**

**Requested Excel details:**
- **Workbook/sheet:** not visible
- **Selected cells/ranges:** none visible
- **Action:** none visible
- **Values/data:** only the name above
- **Menus/dialogs/windows:** none visible

**Transition note:** no screen change; the frames appear static and identical.

If you want, send the frames where Excel is actually on screen and I’ll do the full frame-by-frame breakdown.

[Batch 4 - gpt-5.4-mini]
All provided frames from `frame_00301.jpg` through `frame_00400.jpg` are identical.

- **Visible app/window:** a black screen with a centered circular profile photo and the name **“Yesenia Patiño Figueroa”** beneath it.
- **Workbook/sheet:** **none visible**.
- **Cells/ranges:** **none visible**.
- **Action:** no Excel action detectable; this looks like an idle/avatar screen (likely Teams/meeting placeholder or similar), not a spreadsheet view.
- **Values/formulas:** **none visible**.
- **Menus/dialogs/windows:** no Excel menus, dialogs, or ribbons visible.

**Transition:** no visual transition across the sampled frames; the screen remains unchanged throughout.

[Batch 5 - gpt-5.4-mini]
No Excel content is visible in these frames.

- **Visible UI**: a black screen with a centered circular profile photo and the label **“Yesenia Patino Figueroa”**.
- **Workbook/sheet**: **none visible**
- **Selected cells/ranges**: **none visible**
- **Action being performed**: **none detectable from the frames**
- **Values/text in cells**: **none**
- **Menus/dialogs/windows**: **none** (no Excel, Teams, or other app UI visible)

**Transition note:** all provided frames appear identical; no screen change occurs across the sequence.

If you want, send the correct frame set from the Excel segment and I’ll analyze it frame by frame.

[Batch 6 - gpt-5.4-mini]
I can’t extract the requested Excel details from these frames.

What’s actually visible in every frame you provided:
- A black screen
- Centered circular portrait/avatar
- Name text: “Yesenia Patino Figueroa”
- No Excel workbook, no sheet tabs, no cells, no menus, no dialogs

So for all shown frames:
1. Workbook/sheet: not visible
2. Selected ranges: none visible
3. Action: none visible
4. Values/data: only the name text above
5. Open windows: looks like a video-call/avatar placeholder, not Excel

Transition: none — the frames are visually identical.

If you want, send the actual Excel frames from that segment and I’ll do the frame-by-frame analysis.

[Batch 7 - gpt-5.4-mini]
All provided frames (frame_00601.jpg through frame_00700.jpg) show the same screen:

- **Visible app/window:** a black screen, likely a video-call/meeting placeholder, with a centered circular profile photo and the name **“Yesenia Patino Figueroa”** below it.
- **Workbook/sheet:** **none visible**
- **Selected cells/ranges:** **none**
- **Excel actions:** **none visible**
- **Values/text in cells:** **none**
- **Menus/dialogs/windows:** no Excel, no visible sheet tabs, no ribbons, no dialogs; just the profile-placeholder screen
- **Transition/change across frames:** **no visible change** across the sequence

So, based on these frames, there is **no observable Excel activity** to analyze.

[Batch 8 - gpt-5.4-mini]
All shown frames (frame_00701.jpg through frame_00800.jpg) are identical:

1. **Visible workbook/sheet:** none. No Excel workbook or sheet is visible.
2. **Selected/modified cells:** none. No grid, ranges, or cursor selection appears.
3. **Action:** no Excel action visible. The screen is a static meeting/avatar view.
4. **Values/data:** only the name **“Yesenia Patiño Figueroa”** is readable under the avatar.
5. **Open windows/menus:** no Excel/Teams menus or dialogs are visible; just a black screen with a centered circular profile photo.

**Transition:** no screen change across the frames; all frames show the same static image.

[Batch 9 - gpt-5.4-mini]
All frames shown (00801–00870) are visually identical:

- **Workbook/sheet:** none visible
- **Selected cells/ranges:** none
- **Action:** none; no Excel interaction on screen
- **Values/data:** only the centered name **“Yesenia Patiño Figueroa”** under a circular profile photo
- **Menus/dialogs/windows:** none; just a black screen with a centered profile/avatar, likely a Teams/meeting placeholder

**Transition:** no visible change between frames.  
**Conclusion:** this segment does **not** show the Excel setup steps described in the context; it appears to be a static inactive/placeholder screen.

---

## Segmento 9: Tablas dinámicas y subtemas más reiterados

| Campo | Valor |
|---|---|
| **Duración** | 60:00 - 80:00 |
| **Descripción** | Actualiza TODAS las tablas dinámicas (distribución por sexo, grupo poblacional, subtemas, peticiones trasladadas), verificación de clasificación incorrecta |
| **Frames analizados** | 1200 |
| **Batches** | 12 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 1418s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
I verified the frames. They are all the same static screen:

- Visible UI: black screen with a centered circular avatar/photo and the label **“Yesenia Patino Figueroa”**.
- App/window: looks like a **Teams/meeting avatar placeholder**, not Excel.
- Excel workbook/sheet: **not visible** in any attached frame.
- Cells/ranges/actions/formulas: **none visible**.
- Menus/dialogs/windows: **none visible** beyond the avatar screen.
- Transitions: **no observable change** across the frame set.

So I can’t truthfully extract workbook/sheet/cell activity from these images. If you upload the actual Excel frames, I can analyze them precisely.

[Batch 2 - gpt-5.4-mini]
Los frames adjuntos **no muestran Excel**.  
**Todos los frames de `frame_00101.jpg` a `frame_00200.jpg` son idénticos**:

1. **Workbook/sheet visible:** ninguno.
2. **Selección/celdas:** ninguna.
3. **Acción:** ninguna acción de Excel; solo pantalla estática.
4. **Datos visibles:** avatar circular centrado con el nombre **“Yesenia Patiño Figueroa”** debajo.
5. **Ventanas abiertas:** parece una ventana de **Teams/llamada** o visor de participante con fondo negro; no hay menús, diálogos ni hojas de cálculo visibles.

**Transición entre frames:** no hay cambio perceptible; es la misma pantalla repetida.  
Si quieres, puedo hacer una segunda pasada solo para detectar si hay frames distintos fuera de este bloque.

[Batch 3 - gpt-5.4-mini]
All shown frames in seg009 (frame_00201.jpg–frame_00300.jpg) are visually identical.

1. Workbook/sheet visible: none.
2. Selected ranges: none.
3. Action being performed: no Excel action visible; this is a static video-call/placeholder screen.
4. Values/data visible: profile name text: “Yesenia Patino Figueroa”.
5. Open menus/dialogs/windows: none. No Excel, Teams controls, or other dialogs are visible.

Screen state: black background with a centered circular avatar/photo and the name below it; no transitions or content changes across these frames.

[Batch 4 - gpt-5.4-mini]
All provided frames are identical.

- **Visible content:** black screen with a centered circular profile photo and the name **“Yesenia Patino Figueroa”** below it.
- **Workbook/sheet:** **none visible**
- **Cells/ranges:** **none visible**
- **Action:** no Excel action can be identified; this looks like a **Teams/meeting avatar placeholder**, not an Excel screen
- **Menus/dialogs/windows:** none visible
- **Text read:** “Yesenia Patino Figueroa”
- **Transition:** none across frames

If you meant an Excel segment, these frames are the wrong source.

[Batch 5 - gpt-5.4-mini]
No hay Excel visible en estas capturas.

**Frames 00401–00500:** todos muestran la misma pantalla, sin cambios.

1. **Workbook/sheet visible:** ninguno.  
2. **Celdas/rangos seleccionados:** ninguno.  
3. **Acción:** ninguna acción de Excel identificable.  
4. **Valores/texto visible:** solo el nombre **“Yesenia Patino Figueroa”** bajo una foto circular.  
5. **Menús/ventanas:** parece una pantalla de **Teams/llamada** o perfil, con fondo negro; no hay menús de Excel, diálogos ni hoja visible.

**Transición:** no se observa transición entre frames; el contenido es estático e idéntico.

Si quieres, puedo seguir con otro segmento donde sí aparezca la hoja de Excel.

[Batch 6 - gpt-5.4-mini]
All provided frames (`frame_00501.jpg` to `frame_00600.jpg`) are the same static screen.

1. **Workbook/sheet visible:** none. This is **not Excel**; it looks like a Teams/meeting avatar screen.
2. **Selected cells/ranges:** none.
3. **Action being performed:** no visible spreadsheet action; static presence/placeholder screen.
4. **Visible data/text:** centered circular profile photo with the name **“Yesenia Patino Figueroa”** below it.
5. **Menus/dialogs/windows:** no Excel menus, dialogs, or other windows visible.

**Transition:** none across the frames; no visual change detected.

[Batch 7 - gpt-5.4-mini]
These frames are all the same static Teams/meeting tile.

- **Visible window:** Microsoft Teams/meeting-style black screen with a centered circular profile photo.
- **Visible text:** `Yesenia Patino Figueroa`
- **Workbook/sheet:** **No Excel workbook visible**
- **Selected cells/ranges:** **None**
- **Actions:** **None visible** (no copy/paste/sort/filter/formulas)
- **Menus/dialogs/windows:** Only the meeting/avatar view; no Excel, no dialogs

**Transition:** No screen change across the provided frames — they are identical.

[Batch 8 - gpt-5.4-mini]
All provided frames (frame_00701.jpg–frame_00800.jpg) are the same static screen.

- **Visible app/window:** a black screen with a centered circular profile photo and the name **“Yesenia Patiño Figueroa”** underneath.
- **Workbook/sheet:** **none visible**
- **Selected cells/ranges:** **none visible**
- **Actions:** **none visible**; no copy/paste/filter/sort/formula editing can be seen.
- **Values/data:** only the displayed name above; no Excel data readable.
- **Menus/dialogs/windows:** no Excel, Teams meeting grid, or other dialog is visible beyond this avatar screen.

**Transition:** none between frames; no content change detected across the sequence.

If you want, I can also format this as a per-frame log, but it would repeat the same observation for every frame.

[Batch 9 - gpt-5.4-mini]
All shown frames (frame_00801.jpg through frame_00900.jpg) are visually identical and **do not show Excel**.

1. **Workbook/sheet visible:** none visible.
2. **Selected cells/ranges:** none.
3. **Action being performed:** none visible; this looks like a static call/avatar placeholder screen.
4. **Values/data readable:** only the name **“Yesenia Patiño Figueroa”** under the centered profile image.
5. **Menus/dialogs/windows open:** no Excel menus, dialogs, or sheets visible; no other UI controls visible.

**Transition:** none across the provided frames. They all remain on the same black screen with the centered circular portrait.

If you want, send the actual Excel frames from this segment and I’ll extract the sheet/tab/cell-level actions precisely.

[Batch 10 - gpt-5.4-mini]
Grouped by identical/near-identical screen states.

### 00901–00978
- **Visible app/window:** Microsoft Teams meeting screen only.
- **Workbook/sheet:** none.
- **Selection/range:** none.
- **Action:** waiting in meeting / idle screen.
- **Visible text:** centered profile circle with **“Yesenia Patino Figueroa”**.
- **Menus/windows:** black background, no Excel/PDF open.

### 00979–00985
- **Visible app/window:** Teams in browser (`teams.microsoft.com/v2/`).
- **Workbook/sheet:** none.
- **Selection/range:** none.
- **Action:** meeting view while sharing screen; waiting for attendees.
- **Visible text:** **“Esperando a que se unan otros usuarios…”**
- **Other UI:** bottom banner **“teams.microsoft.com está compartiendo tu pantalla”** and blue **“Dejar de compartir”** button; right-side participant tile with Yesenia’s avatar/name.

### 00986–00988
- **Visible app/window:** Adobe Acrobat.
- **File:** PDF tab/title starts **“2020602ActaReuniónSGL…”**
- **Workbook/sheet:** none.
- **Selection/range:** none.
- **Action:** reading a meeting-minutes PDF.
- **Readable text in PDF:** **“DESARROLLO Y CONCLUSIONES DE LA REUNION”** and lower section **“COMPROMISOS DE LA REUNION”**
- **Menus/windows:** Acrobat left tools panel (“Todas las herramientas”) open.

### 00989
- **Visible app/window:** Excel.
- **Workbook:** **“BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel”**
- **Sheet/tab:** tab visible/active appears to be **“TD COMPL-INCOMPL”**.
- **Selection/range:** pivot table area on left highlighted; no exact cell address fully legible.
- **Action:** reviewing pivot-table totals.
- **Visible data:** two side-by-side summary tables titled **“DIAPOSITIVA No. 3”** / **“TOTAL ENCUESTAS COMPLETAS + INCOMPLETAS DE MAYO 2026”**.
- **Menus/windows:** Excel ribbon open on **Datos**.

### 00990–00994
- **Visible app/window:** Excel.
- **Workbook:** **“REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-010 [Grupo] - Excel”**
- **Sheet/tab:** bottom tabs include **“TD COMPL-INCOMPL”**, **“Encuestas F010 actual”** (and another partially visible tab).
- **Selection/range:** active cell moves within the left pivot table; exact address not fully readable.
- **Action:** navigating totals in the pivot table.
- **Readable values (left table):**
  - **Antonio Nariño:** 28
  - **Barrios Unidos:** 307 complete, 1 incomplete, **308 total**
  - **Bosa:** 54
  - **Chapinero:** 55 / 1 / 56
  - **Ciudad Bolívar:** 327
  - **Engativá:** 88 / 1 / 89
  - **Fontibón:** 100 / 1 / 101
  - **Kennedy:** 66
  - **La Candelaria:** 50
  - **Mártires:** 57
  - **Nivel Central:** 529
  - **Puente Aranda:** 47
- **Visible totals at bottom:** **3918** complete, **1550** incomplete, **5465** total.
- **Menus/windows:** Excel ribbon visible, PivotTable-style layout.

### 00995–00997
- **Visible app/window:** same Excel workbook.
- **Selection/range:** selection shifts to the **“Total general”** column in the left pivot table; visible highlighted vertical block.
- **Action:** likely checking/copying totals.
- **Visible data:** same totals; right-side table unchanged.
- **Menus/windows:** same Excel view.

### 00998–01000
- **Visible app/window:** same Excel workbook.
- **Selection/range:** selection moves into the **right pivot table** around the locality list / lower rows.
- **Action:** navigating summary breakdowns.
- **Visible data (right table labels):** localities plus categories like **Supercade 20 de Julio, Supercade Américas, Supercade Bosa, Supercade CAD 30, Supercade Engativá, Supercade Mántas, Supercade Suba, Nivel Central, Teléfono Antonio Nariño, Teléfono Barrios Unidos**.
- **Menus/windows:** Excel ribbon still on **Datos**; no dialog boxes open.

If you want, I can turn this into a **strict frame-by-frame table** with one row per frame number.

[Batch 11 - gpt-5.4-mini]
Here’s the frame log, grouped where the screen is unchanged.

### 01001
- **Workbook / sheet:** `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-1010 (Grupo)` — tab `TD COMPL-INCOMPL`
- **Selection / action:** no clear active cell; just viewing pivot tables
- **Visible data:**  
  - `TOTAL ENCUESTAS COMPLETAS + INCOMPLETAS DE MAYO 2026`  
  - rows visible include `Antonio Nariño 28`, `Barrios Unidos 307 / 1 / 308`, `Bosa 54`, `Chapinero 55 / 1 / 56`, `Ciudad Bolívar 327`, `Tunjuelito 422 / 3 / 425`, `Usaquén 159 / 1 / 160`, `(en blanco) 1540`, `Total general 3915 / 1550 / 5465`
- **Windows/dialogs:** Excel + Teams share bar (`Dejar de compartir`, `Ocultar`)

### 01002–01005
- **Workbook / sheet:** `BASE DATOS PPF LOCALIDADES MAYO 2026 - Excel` — sheet showing `DIAPOSITIVA No. 3`
- **Selection / action:** table view only; no obvious edit yet
- **Visible data:** columns for `ALCALDÍA LOCAL`, `PQRS PENDIENTES N.2`, `DOC.EXT. N.3`, `ORIENTACIONES No.4`, `CERT. PROPIEDAD No.5`, `CERT. RESIDENCIA No.6`, `ENCUESTAS DEL PERIODO`
  - examples: `ANTONIO NARIÑO 29 / 0 / 61 / 4 / 45 / 28`, `BARRIOS UNIDOS 19 / 0 / 264 / 7 / 143 / 308`, `BOSA 59 / 0 / 61 / 19 / 609 / 54`
- **Windows/dialogs:** Excel only, Teams share bar remains

### 01006–01017
- **Workbook / sheet:** same `BASE DATOS PPF LOCALIDADES MAYO 2026`
- **Selection / action:** column/range around **`H`** is highlighted; the view scrolls downward to the totals
- **Visible data:** bottom totals become visible: `1168`, `1723`, `4328`, `809`, `6863`, `5465`; rows like `NIVEL CENTRAL 497 / 693 / 843 / 0 / 0 / 529`, `SUPERCADES 0 / 0 / 406 / 0 / 0 / 139`, `EN BLANCO 0 / 0 / 0 / 0 / 0 / 1540`, `TOTAL GENERAL 1168 / 1723 / 4328 / 809 / 6863 / 5465`
- **Windows/dialogs:** Excel only; no dialog

### 01018
- **Workbook / sheet:** back to `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-1010 (Grupo)` — `TD COMPL-INCOMPL`
- **Selection / action:** pivot-table view restored
- **Visible data:** same complete/incomplete summary tables as 01001
- **Windows/dialogs:** Excel + Teams share bar

### 01019–01031
- **Workbook / sheet:** same report workbook, still on summary tables
- **Selection / action:** no visible data entry; cursor/viewport moves slightly
- **Visible data:** repeated pivot-table totals; no new numbers
- **Windows/dialogs:** Excel only

### 01032–01041
- **Workbook / sheet:** report workbook, locality-summary sheet with headers:
  - `ORIENTACIONES No.4`
  - `CERT. PROPIEDAD No.5`
  - `CERT. RESIDENCIA No.6`
  - `ENCUESTAS DEL PERIODO`
  - `ENCUESTAS CON RESPUESTA COMPLETA`
  - `CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS`
- **Selection / action:** viewport shifts; no obvious edit
- **Visible data:** same locality rows (`ANTONIO NARIÑO`, `BARRIOS UNIDOS`, `BOSA`, etc.)
- **Windows/dialogs:** Excel only

### 01042
- **Workbook / sheet:** `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-1010` — tab `Calificaciones Totales`
- **Selection / action:** overview sheet with tables + chart
- **Visible data:**  
  - `Tabla 6` and `Tabla 7`
  - pie chart titled `Lugar donde se recibe el servicio`
  - visible numbers include `3093`, `89`, `723`, `3915`
  - summary score boxes show `4,9` and `4,5`
  - scale legend: `UNO A TRES ACEPTABLE`, `TRES A CUATRO ADECUADO`, `CUATRO A CIN SATISFACTORIO`
- **Windows/dialogs:** Excel only

### 01043–01059
- **Workbook / sheet:** same `Calificaciones Totales`
- **Selection / action:** horizontal scrolling across the lower tables
- **Visible data:** three channel sections appear:
  - `Calificación de Localidades Canal Virtual`
  - `Calificación Canal Presencial`
  - `Calificación Canal Telefónico`
  - visible score blocks: `4,0`, `5,0`, `4,8`
- **Windows/dialogs:** Excel only

### 01060–01079
- **Workbook / sheet:** same `Calificaciones Totales`
- **Selection / action:** formula bar becomes active around a row-29 cell; then a Windows **Alt+Tab** task switcher appears
- **Visible data:** no new table data beyond the channel tables
- **Windows/dialogs:**  
  - Excel formula bar visible with a partially legible formula-like expression
  - at 01079, task switcher shows multiple windows: `BASE DATOS PPT LOCALI...`, `REPORTE ENCUESTAS MA...`, `Trabajar informes PQR...`, Teams share window, File Explorer, `ANALISIS INFORME PORS...`

### 01080
- **Workbook / sheet:** back to `BASE DATOS PPF LOCALIDADES MAYO 2026` — `DIAPOSITIVA No. 3`
- **Selection / action:** returning to the locality table
- **Visible data:** same rows and columns as earlier
- **Windows/dialogs:** Excel only

### 01081–01083
- **Workbook / sheet:** same base-data sheet
- **Selection / action:** **right-click context menu** opens on a cell in the `CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS` area; then values are pasted/fill-applied
- **Visible data:** first visible filled values in that column become:
  - `ANTONIO NARIÑO -> 4,5`
  - `BARRIOS UNIDOS -> 5,0`
  - `BOSA -> 4,9`
  - formula bar shows a more precise value around `4,51190476190476`
- **Windows/dialogs:** Excel context menu in Spanish (`Cortar`, `Copiar`, `Pegado especial`, `Insertar celdas copiadas`, `Eliminar`, `Borrar contenido`, etc.)

### 01084–01100
- **Workbook / sheet:** same base-data sheet
- **Selection / action:** the pasted values remain visible; light navigation/selection changes only
- **Visible data:** the same `4,5 / 5,0 / 4,9` entries stay in place
- **Windows/dialogs:** Excel only; no new modal windows

If you want, I can turn this into a strict **frame-by-frame CSV-style report** next.

[Batch 12 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped where the screen is unchanged.

| Frames | Workbook / sheet | Selected cell/range | Action | Readable values / text | Menus / windows |
|---|---|---|---|---|---|
| 1101–1105 | **BASE DATOS PPT LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | **K4** (rightmost % column) | Right-click, then formula/value entry for % participation | Rows shown: Antonio Nariño `61, 4, 45, 28, 28, 4,5`; Barrios Unidos `264, 7, 143, 308, 307, 5,0`; Bosa `61, 19, 609, 54, 54, 4,9`. Rightmost column becomes `90%`, `99,4%`, `98,0%`. Formula bar shows a raw decimal around `90,238095...` before formatting. | Excel context menu open in 1103/1104; Teams sharing bar visible; alt-tab window switcher visible in 1101. |
| 1106–1115 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / **Calificaciones Totales** | Active cell in the middle/right tables (exact address not fully legible) | Editing/calculating summary tables | Three side-by-side tables visible: red/green dashboard tables for canal presencial, virtual y telefónico. No major value change visible yet. | Same workbook; Teams share bar persists. |
| 1116–1117 | **BASE DATOS PPT LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | Cells in the **“Encuestas con respuesta completa”** column | Paste/fill of complete-response counts | New visible values appear: `55`, `327`, `88`, `100`, `66` in the complete-response column for rows like Chapinero, Ciudad Bolívar, Engativá, Fontibón, Kennedy. | Excel right-click menu open in 1116; then closed. |
| 1118 | Alt-tab switcher | — | Window switch | Shows multiple open windows: report workbook, base data workbook, Teams, Explorer, analysis docs. | Windows app switcher overlay. |
| 1119–1125 | **BASE DATOS PPT LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | Rightmost % column, several rows | Formula results copied/finalized | Right-side percentages visible across more rows: `96%`, `97,2%`, `98,9%`, `97%`, plus earlier `90%`, `99,4%`, `98,0%`. | Mostly clean grid; occasional cursor repositioning. |
| 1126–1131 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / summary/dashboard sheet | Middle table / right table | Continued formula editing / review | Dashboard tables remain visible; no new obvious data change. | Some frames show a cell context menu; Teams sharing bar still present. |
| 1132–1143 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / summary/dashboard sheet | A cell in the middle/right table | Editing a formula tied to totals/percentages | Formula bar shows arithmetic-style entries; one raw decimal appears around `4,926666...` in the base-data counterpart. | Context menu open in several frames; same Teams overlay. |
| 1144–1149 | **BASE DATOS PPT LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | Selected cell in the % column (e.g. K7/K13 region) | Formatting/calculation validation | Raw decimal in formula bar around `98,533333...`; displayed as `98,5%`. Right column shows formatted percentages. | Right-click menu appears and disappears. |
| 1150–1160 | **BASE DATOS PPT LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | Lower rows (Fontibón → Usme) | Scroll down and continue filling | Rows visible: Fontibón `133, 99, 537, 101, 100`; Kennedy `312, 50, 677, 66, 66`; Martíres `60, 1, 60, 97, 97`; Puente Aranda `58, 15, 134, 47, 47`; Rafael Uribe `95, 0, 387, 408, 407`; San Cristóbal `182, 10, 306, 194, 193`; Santa Fe `59, 10, 102, 59, 59`; Suba `180, 110, 902, 182, 182`; Sumapaz `3, 0, 20, 1, 1`; Teusaquillo `251, 105, 235, 83, 83`; Tunjuelito `167, 13, 491, 425, 422`; Usaquén `316, 293, 410, 160, 159`; Usme `112, 6, 543, 522, 522`. | Context menu appears again around 1152; alt-tab overlay appears again in 1160. |
| 1161–1176 | **BASE DATOS PPT LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | Lower rows and totals area | Fill/verify remaining rows and percentages | Lower section now shows more computed % values like `97%`, `99,2%`, `99,4%`, `98,9%`; totals rows begin appearing. | Repeated right-click/context-menu and data-entry states. |
| 1177–1188 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / summary/dashboard sheet | Middle/right tables | Review of calculated summaries | Summary tables and sheet tabs visible; no major new values beyond ongoing verification. | Excel context menu in several frames. |
| 1189–1192 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / **Calificaciones Totales** | Summary table area / chart area | Jump to final summary sheet | Top-left summary table shows: Canal Presencial `3093`, calificación `5,0`, proporcional `3,9`, `79%`; Canal Virtual `99`, `4,0`, `0,1`, `3%`; Canal Telefónico `723`, `4,8`, `0,9`, `18%`; total encuestas `3915`. Second table: Nivel Central `529`, Localidades `3247`, SuperCADES `139`, Totales `3915`. Scores shown: `4,9` and `4,5`. Pie chart titled **“Lugar donde se recibe el servicio”** with legend **Nivel Central / Localidades / SuperCADES**. | Same workbook; chart visible; bottom tabs include `Tabla 10 indicadores_Ajustado`, `Calificaciones x AL`, `Grupos de Valor`, `Calificaciones Totales`. |
| 1193–1200 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / **Calificaciones Totales** | Summary cells around C14/C15 and nearby tables | Formula review / totals check | Formula bar shows `=SUMA(AA29:AA48)` and later `=SUMA(AA50:AA56)`; status bar reflects aggregate values. The summary layout and chart remain unchanged. | Excel only; no new dialogs. |

### Key transitions
- **1101 → 1102**: alt-tab from window switcher to the base-data workbook.
- **1102 → 1105**: right-click/formula result is formatted into percentage values.
- **1117 → 1119**: complete-response counts are propagated, then percentages are recalculated.
- **1160 → 1161**: switch back from the app switcher to the base-data sheet scrolled lower.
- **1188 → 1189**: jump to the final summary sheet with the pie chart and totals.

If you want, I can turn this into a stricter **frame-by-frame CSV-style log** next.

---

## Segmento 10: Días de gestión y vencimientos

| Campo | Valor |
|---|---|
| **Duración** | 80:00 - 100:00 |
| **Descripción** | Monitoreo días de gestión, extemporáneas, oportunas, pendientes vencidas, porcentaje de descongestión, resaltado de casos que sobrepasan términos legales |
| **Frames analizados** | 1200 |
| **Batches** | 12 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 2050s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Here’s a frame-by-frame analysis, grouped where the screen is visually unchanged.

| Frames | Workbook / sheet | Selection / edit target | Action | Visible data | Open menus / windows |
|---|---|---|---|---|---|
| 1–5 | **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / **Calificaciones Totales** | Active cell around the lower score table (name box shows **D15** in one shot; another shot shows **C15**) | Reviewing/filling the totals sheet; no obvious structural change | Table 6/7 visible: **Canal Virtual, Canal Presencial, Canal Telefónico**; score boxes show **4,9** and **4,5**; pie chart titled **“Lugar donde se recibe el servicio”** | Excel + Teams sharing banner (“teams.microsoft.com está compartiendo su pantalla”, **Dejar de compartir**) |
| 6–12 | **BASE DATOS PPF LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** | Active cell moves in the summary table, later around the SuperCADES row | Inspecting/validating locality summary data | Table with **ALCALDÍA LOCAL**, **ORIENTACIONES**, **CERT. PROPIEDAD**, **CERT. RESIDENCIA**, **ENCUESTAS DEL PERIODO**, **ENCUESTAS CON RESPUESTA COMPLETA**, **CALIFICACIÓN**; visible rows include **SUMAPAZ, TEUSAQUILLO, TUNJUELITO, USAQUEN, USME, NIVEL CENTRAL, SUPERCADES, EN BLANCO** | Right-click Excel context menu appears in frames 10–11 (Cut/Copy/Paste/Insert/Delete/Filter/Sort/etc.); frame 12 shows Windows task switcher (Alt-Tab style) |
| 13–34 | Same workbook / same sheet | Cell focus stays in the locality summary and lower area | Continued validation of values; no visible structural change | Same locality table; visible values include **139** for SuperCADES in one row and **5,0** / **100%** on the right; blank row shows **0** | Teams overlay remains; mostly static Excel screen |
| 35–43 | **BASE DATOS PPT/PPF LOCALIDADES MAYO 2026** / **RESUMEN CIFRAS** then horizontal scroll into **DIAPOSITIVA No. 3** data sheet | Selection shifts across the table; later the view is scrolled horizontally | Horizontal navigation across a large data table | Main table shows columns like **PQRS GESTIONADAS N.1**, **PQRS PENDIENTES N.2**, **DOC. EXT. N.3**, **ORIENTACIONES No.4**, **CERT. PROPIEDAD No.5**, **CERT. RESIDENCIA No.6**; rows include **ANTONIO NARIÑO, BARRIOS UNIDOS, BOSA, CANDELARIA, CHAPINERO, CIUDAD BOLIVAR, ENGATIVÁ, FONTIBÓN, KENNEDY, MARTIRES, PUENTE ARANDA, RAFAEL URIBE, SAN CRISTOBAL, SANTA FE** | Excel only; no dialog, just worksheet scrolling |
| 44–49 | Same locality workbook / pivot sheets | Focus in pivot-table area on the right and lower panels | Pivot-table inspection and filtering | Left pivot table shows **total general 4328**; another small pivot section titled **“Registros por Atención Preferencial”** is visible; filter fields on the right include items like **Punto de atención**, **Nombre completo ciudadano**, **Género**, **Sexo**, **Fecha de atención** | PivotTable Fields pane open on the right |
| 50–52 | **MAYO2026_PRODUCTIVIDAD_PH** / **RESUMEN** | Active cell in the blank lower area under the summary table (around **G27**) | Reviewing productivity summary | Table titled **“PRODUCTIVIDAD DE CERTIFICADOS DE PROPIEDAD HORIZONTAL / CERTIFICADOS GENERADOS VIGENCIA MAYO 2026”**; right-side bar chart shows **USAQUÉN 36,218%**, **SUBA 13,597%**, **TEUSAQUILLO 12,979%**, **FONTIBÓN 12,237%**, **KENNEDY 6,180%**, etc.; total general **809** | Excel only |
| 53–57 | Same workbook / same sheet | Pivot/field focus in the middle-right block | Checking another pivot summary | Right-side block shows categories like **Proyectos locales**, **Propiedad horizontal**, **Subsidios**, **Documentos extraídos**, etc.; another box titled **“Registros por Atención Preferencial”** with **total general 3366** is visible | Pivot table field pane still open |
| 58–62 | Same workbook / same sheet | No obvious edit target; cursor moving near the right-side summary | Navigating / preparing to close | Same productivity chart and tables | Alt-Tab/app switcher appears again in frames 62–63 |
| 63–66 | Same workbook, then close flow | — | Closing the workbook | — | Excel save confirmation dialog appears: **“¿Desea guardar los cambios…”** with buttons **Guardar / No guardar / Cancelar** |
| 67–83 | Back to **REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010** / **Calificaciones Totales** | Same lower table area, active cell around the SuperCADES row | Returning to the completed report and verifying final values | Same chart **“Lugar donde se recibe el servicio”** and tables; visible values stay at **139** and **5,0 / 100%** for SuperCADES, blank row remains **0** | Teams share banner persists; no dialogs |
| 84–89 | Windows File Explorer | File list selection moves through folders | Switching from Excel to folder navigation | Explorer path moves through **Documentos > SECGOB > BASE ENCUESTAS DE PERCEPCION > 2026** | Explorer windows only |
| 90–92 | File Explorer: **INFORMES DE PQRS** → **NIVEL CENTRAL** | Folder selected: **NIVEL CENTRAL** | Opening folder hierarchy | File/folder list includes **INFORME PQRS ANUAL**, **INFORMES PQRS LOCALIDADES**, **NIVEL CENTRAL**, **INFORME CONSOLIDADO…**, **PQRS Excel**, **Proyecto de respuesta…**, **PUNTOS DE ATENCION PRESENCIAL…** | Explorer preview pane on right |
| 93–95 | File Explorer: **NIVEL CENTRAL > PAGINA DE GOBIERNO > 2026** | Folder **2026** selected | Drilling down into year folders | Year folders visible: **2020, 2021, 2022, 2023, 2024, 2025, 2026** plus a compressed file **PDF INF PQRS WEB SECGOB** | Explorer only |
| 96–100 | File Explorer inside **2026** | File selection moves to April file | Opening monthly PQRS spreadsheets | Files listed: **BD PQRS BOGOTA TE ESCUCHA ABRIL 2026**, **ENERO 2026**, **FEBRERO 2026**, **MARZO 2026** | Explorer only |

### Key transition notes
- **Frame 10–12**: right-click menu appears, then app-switcher overlay.
- **Frames 63–66**: workbook close/save confirmation dialog.
- **Frame 84 onward**: clear transition from Excel to File Explorer navigation.
- The repeated **Teams sharing banner** is visible across most Excel frames; it is not part of the workbook content.

### Readable content that matters most
- **SuperCADES** row gets filled/confirmed as **139** surveys with **5,0** score → **100%**.
- The locality summary table shows the report is being finalized for **PQR Localidades**.
- The productivity workbook shows **USAQUÉN** as the largest share (**36,218%**) in the horizontal property certificate report.

[Batch 2 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen is effectively unchanged. I only transcribe what’s legible.

- **101–104** — **File Explorer** in `SEGCOB > INFORMES DE PQRS > NIVEL CENTRAL > PAGINA DE GOBIERNO > 2026`.
  - Visible workbook files: `BD PQRS BOGOTA TE ESCUCHA ABRIL 2026`, `... ENERO 2026`, `... FEBRERO 2026`, `... MARZO 2026`.
  - **Selected:** `BD PQRS BOGOTA TE ESCUCHA ABRIL 2026`.
  - Right preview pane shows an Excel preview with a report/table and a circular profile image.
  - No Excel edit yet; just file selection.
  - Teams sharing overlay is visible.

- **105–106** — **Rename in File Explorer**.
  - The selected file enters inline rename mode.
  - Name changes from `BD PQRS BOGOTA TE ESCUCHA ABRIL 2026` to `BD PQRS BOGOTA TE ESCUCHA ABRIL 2026 - copia`.
  - Action: file duplication/rename in progress.

- **107–109** — **Copied file selected**.
  - The renamed copy is highlighted.
  - Preview pane still shows the Excel/report preview.
  - No other UI change.

- **110–118** — **Inline rename continues**.
  - The filename text is edited from `... ABRIL 2026 - copia` toward `... MAYO 2026`.
  - Intermediate text states are visible: `MAY`, `MAYO 202`, then `MAYO 2026`.
  - Action: finishing the month rename.

- **119–125** — **Renamed file highlighted**.
  - File now reads `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`.
  - Still in File Explorer, same folder, same preview pane.
  - No sheet open yet.

- **126** — **File Explorer preview pane clears**.
  - Selected file remains `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`.
  - Right preview area is blank/idle.

- **127–128** — **Excel workbook opens**: `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010`.
  - **Selected sheet:** `Calificaciones Totales`.
  - Visible content:
    - `Tabla 6.` and `Tabla 7.` with scores.
    - Readable values include `4.9` and `4.5`.
    - Pie chart titled **“Lugar donde se recibe el servicio”**.
  - This is a reporting/calculation sheet, not a data-entry grid.

- **129** — **Loading/transition**.
  - Mostly blank white/gray Excel view with hourglass.
  - Likely workbook/sheet loading.

- **130–141** — **Workbook:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`.
  - **Selected sheet:** `INFORME WEB ABRIL`.
  - Visible title block: **“CAPITULO 6. SUBTEMAS MAS REITERADOS Y/O BARRERAS DE ACCESO”**.
  - Right side: `Tabla No. 3` and `Gráfica No. 3`.
  - Yellow security banner at top: active content disabled, with **Habilitar contenido**.
  - **132–133:** Excel warning dialog appears:
    - Circular reference warning: *“Hay una o varias referencias circulares...”*
    - Buttons: **Aceptar**, **Ayuda**.
  - **134–141:** dialog dismissed; sheet remains visible.
  - Some row labels are legible, but many subtheme values are too blurred to trust.

- **142–149** — **Same workbook, another sheet view**: `Reporte PQRS Abril2026`.
  - Large PQRS data table scrolled far right / deep rows.
  - Visible row numbers around **13556+**.
  - Readable values include repeated statuses like:
    - `Activo`
    - `WEB`
    - `WEB SERV`
    - `DERECHO`
    - `Notificado`
    - `Cerrado`
    - `Pendiente`
  - This is a dense operational dataset, not a summary sheet.

- **150–155** — **PQRS report sheet with header block**.
  - Top-left report header:
    - `Gestión de Peticiones`
    - `Fecha de generación de reporte: 2026-05-05`
    - `Fecha Inicial: 2026-04-01`
    - `Fecha Final: 2026-04-30`
    - `Tipo de estado: Al periodo`
  - Table headers visible:
    - `Número petición`
    - `Duplicado`
    - `Sector`
    - `Entidad`
    - `Tema`
    - `Categoria`
    - `Subtema`
    - `Funcionario`
    - `Estado`
    - `Canal`
    - `Tipo pet`
    - `Asunto`
    - `Proceso`
  - Sample readable row content includes:
    - `GOBIERNO`
    - `SECRETARIA DISTRITAL DE GOBIERNO`
    - `Oficina de ATENCION A LA CIUDADANIA`
    - `Activo`
    - `WEB`
    - `WEB SERV`
    - `DERECHO`
    - `Notificado`
    - `Cerrado`

- **156–159** — **Blank grid / sheet switch**.
  - No data visible, just Excel grid and bottom tabs.
  - `Reporte PQRS Abril2026` remains in the tab strip.
  - **159** shows a Windows taskbar hover preview of another app/window.

- **160–166** — **Excel Backstage / Home screen**.
  - Title bar still: `BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`.
  - Left menu shows:
    - `Inicio`
    - `Nuevo`
    - `Abrir`
    - `Información`
    - `Guardar`
    - `Guardar como`
    - `Imprimir`
    - `Exportar`
    - `Publicar`
    - `Cerrar`
  - Recent files list includes:
    - `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`
    - `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010`
    - `REPORTE ENCUESTAS ABRIL 2026 FORMATO SAC-F010`
    - `MAYO2026_PRODUCTIVIDAD_PH`
    - `MAYO2026_PRODUCTIVIDAD_CR`
    - `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026`
    - `BASE DATOS PPT LOCALIDADES MAYO 2026`

- **167–169** — **Back to blank worksheet view**.
  - Tab strip still shows `Reporte PQRS Abril2026`.
  - No data; just grid.

- **170** — **Workbook:** `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026 - Excel`.
  - A blank/partially loaded sheet view.
  - Formula bar shows `Número petición`.
  - Indicates the report structure is being accessed or prepared.

- **171–173** — **Same workbook, report table visible**.
  - Header block again:
    - `Gestión de Peticiones`
    - `Fecha de generación de reporte: 2026-06-01`
    - `Fecha Inicial: 2026-05-01`
    - `Fecha Final: 2026-05-31`
    - `Tipo de estado: Al periodo`
  - Large table begins at row 10 with the same PQRS structure.
  - Readable examples:
    - `GOBIERNO`
    - `SECRETARIA DISTRITAL DE GOBIERNO`
    - `OFICINA DE ATENCION A LA CIUDADANIA`
    - `Activo`
    - `WEB`
    - `DERECHO`
    - `QUEJA`
  - Sheet tab visible as `Hoja1`.

- **174–182** — **Grid/loading states**.
  - Mostly blank worksheet views with hourglass icons.
  - Same workbook/tabs, no new content.

- **183–186** — **Report table visible again; sheet-tab context menu opened**.
  - Right-click menu on a sheet tab appears with:
    - `Insertar`
    - `Eliminar`
    - `Cambiar nombre`
    - `Mover o copiar...`
    - `Ver código`
    - `Proteger hoja`
    - `Color de pestaña`
    - `Ocultar`
    - `Mostrar...`
    - `Seleccionar todas las hojas`
  - This matches a **sheet duplication/rename** action.

- **187–191** — **Back on the report table**.
  - No dialog; same table visible.
  - Likely after choosing a tab action.

- **192–193** — **Cell right-click menu**.
  - Context menu over a cell shows:
    - `Cortar`
    - `Copiar`
    - paste options
    - `Pegar especial`
    - `Insertar`
    - `Eliminar`
    - `Borrar contenido`
    - `Formato de celdas...`
    - `Ancho de columna...`
    - `Ocultar`
    - `Mostrar`
  - This is a cell-level edit operation, not sheet-tab editing.

- **194–195** — **Excel large-operation warning dialog**.
  - Dialog title: **Operación grande**
  - Message warns the action affects many cells and may take time.
  - Buttons: **Aceptar**, **Cancelar**
  - Checkbox: **No mostrar nuevamente**
  - Strong sign of a bulk paste/fill/delete.

- **196–200** — **Back to report table; header edit visible**.
  - The header row is visible again.
  - Active cell / formula bar shows the column label transitioning to **`Duplicados`**.
  - This suggests the table header is being corrected/edited.
  - Other visible headers remain:
    - `Número petición`
    - `Sector`
    - `Entidad`
    - `Tipo de`
    - `Tema`
    - `Estado`
    - `Canal`

If you want, I can turn this into a strict CSV-style per-frame log next.

[Batch 3 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped by visible state:

### Frames 201–204
- **Workbook / sheet:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026 - Excel` → `Reporte PQRS Mayo2026`
- **Selection:** around **A10** / header row of the main table
- **Action:** preparing a **sort** from the **Datos** tab
- **Visible data:** report header:
  - `Gestión de Peticiones`
  - `Fecha de generación de reporte: 2026-06-01`
  - `Fecha Inicial: 2026-05-01`
  - `Fecha Final: 2026-05-31`
  - `Tipo de estado: Al periodo`
  - table columns include `Número petición`, `Duplicado`, `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`, `Tema`, `Categoría subtema`, `Subtema`, `Funcionario`, `Estado del Usuario`, `Punto atención`
- **Open windows/menus:** Excel ribbon; by frame 204 the **Datos** tab is active

### Frames 205–218
- **Workbook / sheet:** same workbook, same sheet
- **Selection:** sort dialog on top of the table
- **Action:** configuring **multi-level sort**
- **Dialog visible:** Excel **Ordenar** modal
- **Sort fields visible:**
  - **Ordenar por:** `Número petición` → `Valores de celda` → `De menor a mayor`
  - **Luego por:** `Dependencia hija`
  - **Luego por:** `Comunes`
  - later the third key is changed to **`Transacción entidad`**
- **Menus visible:** dropdown lists for choosing sort columns; options shown include `Tema`, `Categoría subtema`, `Subtema`, `Funcionario`, `Estado del Usuario`, `Punto atención`, `Canal`, `Tipo petición`, `Estado de la petición inicial`, `Tipo de la petición`, `Transacción entidad`
- **Action detail:** user is selecting the third sort key from the dropdown and adjusting order

### Frame 219
- **Workbook / sheet:** same workbook, `Reporte PQRS Mayo2026`
- **Selection:** back in the table, focused in the data area around **column B** (`Duplicado`)
- **Action:** sort appears to have been **applied**
- **Visible data:** rows show `FALSO` / `VERDADERO` in `Duplicado`; table remains on the same report
- **Open windows:** no modal; worksheet only

### Frames 220–248
- **Workbook / sheet:** same workbook, `Reporte PQRS Mayo2026`
- **Selection:** moving through the data table, mostly around **B11:B14** / `Duplicado`
- **Action:** browsing the sorted table; no visible dialog
- **Visible data:** repeated `FALSO` / `VERDADERO`, rows with petition numbers like `8,6E+08`, `9,4E+08`, etc.; entities such as `GOBIERNO ENTIDAD SECRETARIA DISTRITAL DE GOBIERNO`, `OFICINA DE ATENCION A LA CIUDADANIA`
- **Open windows:** Excel worksheet only; Teams share bar still visible at bottom center

### Frames 249–250
- **Workbook / sheet:** Excel **Backstage/File view**
- **Selection:** none (not on worksheet)
- **Action:** opened the **Archivo** view / recent files screen
- **Visible text:** `Buenas tardes`, `Nueva`, `Recientes`
- **Open windows:** Excel backstage left menu (`Inicio`, `Nuevo`, `Abrir`, `Información`, etc.)

### Frames 251–260
- **Workbook / sheet:** back to `BD PORS BOGOTA TE ESCUCHA MAYO 2026 - Excel`
- **Sheet:** a blue-header data sheet titled **`ESPACIO PUBLICO`** is visible
- **Selection:** sheet tab / sheet-level interaction, not a cell edit
- **Action:** right-clicked a **sheet tab** and opened the context menu
- **Context menu items visible:** `Insertar...`, `Eliminar`, `Cambiar nombre`, `Mover o copiar...`, `Ver código`, `Proteger hoja...`, `Color de pestaña`, `Ocultar`, `Mostrar...`, `Seleccionar todas las hojas`
- **Dialog visible:** Excel confirmation:
  - `Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?`
  - buttons `Eliminar` / `Cancelar`
- **Visible data on sheet:** table with headers like `Número petición`, `Duplicado`, `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`, `Tema`, `Categoría subtema`, `Subtema`, `Funcionario`, `Estado del Usuario`, `Punto atención`
- **Action detail:** user is **deleting a sheet**

### Frames 261–268
- **Workbook / sheet:** same workbook, sheet **`INFORME WEB ABRIL`**
- **Selection:** sheet area, no dialog
- **Action:** viewing a summary/report section
- **Visible title:** `CAPITULO 6. SUBTEMAS MÁS REITERADOS Y/O BARRERAS DE ACCESO`
- **Visible data:** pivot-style table of subthemes and counts, with items like:
  - `LEY 1801 DE 2016 CODIGO NACIONAL DE SEGURIDAD Y CONVIVENCIA`
  - `TRASLADO`
  - `MANTENIMIENTO DE VIAS INTERNAS DE LA LOCALIDAD`
  - other repeated subthemes / access barriers
- **Visible totals:** numbers such as `2.568`, `36.758`, `4.664`, `938`, and `59,487` are readable in the summary area
- **Open windows:** worksheet only; no modal dialog

### Frames 269–300
- **Workbook / sheet:** same workbook, sheet **`SEGUIMIENTO DÍAS`**
- **Selection:** starts around **S54** (frame 269), later moves to **F2**, **B28**, **B36** and nearby summary cells
- **Action:** horizontal navigation / inspection of monthly follow-up tables and charts
- **Visible sections:**
  - table with rows:
    - `Gestión Extemporánea`
    - `Gestión Oportuna`
    - `Pendientes en términos`
    - `Pendientes vencidos`
  - months `ENERO`, `FEBRERO`, `MARZO`, `ABRIL`, later `MAYO` onward
  - charts titled **`Seguimiento Gestión PQRS`** and **`Seguimiento Días de Gestión`**
- **Visible numbers in the summary block:**
  - `496`, `716`, `670`, `686`
  - `7.071`, `7.838`, `10.325`, `11.524`
  - `966`, `1.152`, `1.407`, `1.139`
  - `239`, `228`, `244`, `227`
  - totals like `7.567`, `8.554`, `10.995`, `12.210`
  - another total line `8.772`, `9.934`, `12.646`, `13.576`
- **Percent rows visible:**
  - `Porcentaje de Descongestión`: `86%`, `86%`, `87%`, `90%`
  - `Extemporaneas vencidas`: `735`, `944`, `914`, `913`
  - `Oportunas en términos`: `8.037`, `8.990`, `11.732`, `12.663`
  - `PORCENTAJE EXTEMPORANEIDAD`: `8%`, `10%`, `7%`, `7%`
  - `PORCENTAJE OPORTUNIDAD`: `81%`, `79%`, `82%`, `85%`
- **Formula visible:** `=B33/B34` in the percentage block (frame 294)
- **Other visible table while scrolling:** locality rows such as
  - `ALCALDIA LOCAL DE ANTONIO NARINO`
  - `ALCALDIA LOCAL DE BARRIOS UNIDOS`
  - `ALCALDIA LOCAL DE BOSA`
  - `ALCALDIA LOCAL DE CANDELARIA`
  - `ALCALDIA LOCAL DE CHAPINERO`
  - `ALCALDIA LOCAL DE CIUDAD BOLIVAR`
  - `ALCALDIA LOCAL DE ENGATIVA`
  - `ALCALDIA LOCAL DE FONTIBON`
  - `ALCALDIA LOCAL DE KENNEDY`
  - `ALCALDIA LOCAL DE MARTIRES`
  - `ALCALDIA LOCAL DE PUENTE ARANDA`
  - `ALCALDIA LOCAL DE RAFAEL URIBE`
  - `ALCALDIA LOCAL DE SAN CRISTOBAL`
  - `ALCALDIA LOCAL DE SANTA FE`
  - `ALCALDIA LOCAL DE SUBA`
  - `ALCALDIA LOCAL DE SUMAPAZ`
  - `ALCALDIA LOCAL DE TEUSAQUILLO`
  - `ALCALDIA LOCAL DE TUNJUELITO`
  - `ALCALDIA LOCAL DE USAQUEN`
  - `ALCALDIA LOCAL DE USME`
  - `DEPENDENCIAS NIVEL CENTRAL`
  - `OFICINA ASUNTOS DISCIPLINARIOS`
  - `OFICINA DE ATENCION A LA CIUDADANIA`
- **Open windows:** worksheet only; Teams sharing bar still visible

### Notable transitions
- **204 → 205:** opened the **Sort** dialog
- **218 → 219:** sort dialog closed; table returns with reordered rows
- **248 → 249:** switched to **Excel backstage**
- **260 → 261:** moved to **INFORME WEB ABRIL**
- **268 → 269:** moved to **SEGUIMIENTO DÍAS** and began inspecting monthly tables/charts

If you want, I can turn this into a strict **CSV-style frame log** next.

[Batch 4 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped by exact screen state.

### 1) Frames 00301–00336  
**Workbook:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026 - Excel`  
**Sheet:** `SEGUIMIENTO DÍAS`  
**Selection:** cell `B39` is shown in the name box; no clear edit range  
**Action:** browsing the monthly PQRS monitoring sheet; later frames scroll downward to the chart area  
**Visible data:**  
- `Gestión Extemporánea`: `496`, `716`, `670`, `686`  
- `Gestión Oportuna`: `7.071`, `7.838`, `10.325`, `11.524`  
- `Pendientes en términos`: `966`, `1.152`, `1.407`, `1.139`  
- `Pendientes vencidos`: `239`, `228`, `244`, `227`  
- `Porcentaje de Descongestión`: `86%`, `86%`, `87%`, `90%`  
- `Extemporaneas-vencidas`: `735`, `944`, `914`, `913`  
- `Oportunas-en términos`: `8.037`, `8.990`, `11.732`, `12.663`  
- `PORCENTAJE EXTEMPORANEIDAD`: `8%`, `10%`, `7%`, `7%`  
- `PORCENTAJE OPORTUNIDAD`: `81%`, `79%`, `82%`, `85%`  
- summary totals at right: `2.568`, `36.758`, `4.664`, `938`, and overall `59.487`  
**Menus/windows:** Excel ribbon + Teams sharing bar (`teams.microsoft.com está compartiendo tu pantalla`)

### 2) Frames 00337–00346  
**Workbook:** same  
**Sheet:** `Reporte PQRS Mayo2026` / tab navigation across certificate-related sheets  
**Selection:** `G19` is shown in one frame; formula bar displays `ALCALDIA LOCAL DE FONTIBON`  
**Action:** viewing detailed PQRS records and switching tabs  
**Visible data:**  
- report header: `Gestión de Peticiones`  
- `Fecha de generación de reporte: 2026-06-01`  
- `Fecha Inicial: 2026-05-01`  
- `Fecha Final: 2026-05-31`  
- `Tipo de estado: Al periodo`  
- detailed table columns include `MES`, `FECHA`, `TIPO DOCUMENTO`, `CANTIDAD`, `ACUSE`, `CASO`, `PLANILLA`  
**Menus/windows:** Excel; Teams sharing bar  
**Transition:** tab clicks move through `CERT.P.HORIZONTAL ABRIL`, `CERT RESIDENCIA PROD-ABRIL`, and `CR-TIPO TRAMITE`

### 3) Frames 00347–00349  
**Workbook:** same  
**Sheet:** `CERT RESIDENCIA PROD-ABRIL`  
**Selection:** `E17` visible in name box  
**Action:** viewing a locality productivity table and its chart  
**Visible data:**  
- table header: `PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA VALIDADOS`  
- columns: `Aprobado`, `Cerrada por desistimiento`, `Cerrado (Supera Subsanaciones)`, `Pendiente`, `Rechazado`, `Total general`, `%`  
- localities visible include `SUMAPAZ`, `LOS MARTIRES`, `ANTONIO NARIÑO`, `CANDELARIA`, `SANTA FE`, `BARRIOS UNIDOS`, `PUENTE ARANDA`, `CHAPINERO`, `TEUSAQUILLO`, `RAFAEL URIBE URIBE`, `SAN CRISTOBAL`, `FONTIBON`, `USME`, `ENGATIVA`, `USAQUEN`, `BOSA`, `CIUDAD BOLIVAR`, `KENNEDY`, `TUNJUELITO`, `SUBA`  
- chart title: `PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA - ABRIL 2026`  
**Menus/windows:** Excel only

### 4) Frames 00350–00352  
**Workbook:** same  
**Sheet:** `CR-TIPO TRAMITE`  
**Selection:** not clearly changing  
**Action:** viewing the certificate productivity breakdown by trámite type  
**Visible data:**  
- title: `PRODUCTIVIDAD CERTIFICADO DE RESIDENCIA - TIPO DE TRÁMITE VIGENCIA ABRIL 2026`  
- columns include `Personas privadas de la libertad`, `Trámite ante el ministerio de rel exteriores`, `Trámite de subsidios`, `Trámite de estudio`, `Trámites legales`, `Requisitos laborales`, `Proyectos locales`, `Total general`  
- pie chart on right  
**Menus/windows:** Excel only

### 5) Frames 00353–00354  
**Workbook:** same  
**Sheet:** `Tabla 10 indicadores_Ajustado`  
**Selection:** `F58` visible  
**Action:** viewing the citizen perception/satisfaction indicators table  
**Visible data:**  
- title: `Tabla 10. indicadores` / `Encuesta percepción y satisfacción ciudadana 2022 SAC-F010`  
- grouped indicators: `Efectividad`, `Accesibilidad`, `Oportunidad`  
- visible scores include `4.7`, `4.6`, `4.9`, `5.0`  
**Menus/windows:** Excel only

### 6) Frame 00355  
**Workbook:** same  
**Sheet:** `Calificaciones Totales`  
**Selection:** not clearly visible  
**Action:** consolidation/score summary sheet open  
**Visible data:** locality score blocks with green/yellow formatting; visible values around `4.5`, `4.3`, `4.8` and a total row  
**Menus/windows:** Excel only

### 7) Frame 00356  
**Workbook:** same  
**Sheet:** `REGISTRADO SIDE`  
**Selection:** `V3` visible  
**Action:** viewing monthly registered document counts  
**Visible data:**  
- title: `REGISTRADO SIDE Abril 2026`  
- `Cédula de ciudadanía 379`  
- `Cédula de extranjería 2`  
- `Libreta Militar 2`  
- `Licencia de conducción 34`  
- `Licencia de Tránsito 3`  
- `Pasaporte 1`  
- `Permiso Protección Temporal 10`  
- `Tarjeta de conducta servicio militar 1`  
- `Tarjeta de identidad 157`  
- `Tarjeta Profesional 1`  
- `Total general 591`  
**Menus/windows:** Excel only

### 8) Frames 00359–00364  
**Workbook:** same  
**Sheet:** `ENTREGADO SIDE`  
**Selection:** `V3` still shown in one frame; later selection moves inside the detailed table  
**Action:** viewing delivered/returned SIDE data  
**Visible data:**  
- left summary: `DEVUELTO SIDE Abril 2026`  
- `Cédula de ciudadanía 764`  
- `Cédula de extranjería 13`  
- `Contraseña cédula de ciudadanía 0`  
- `Libreta Militar 12`  
- `Licencia de conducción 197`  
- `Licencia de Tránsito 80`  
- `Pasaporte 22`  
- `Permiso Protección Temporal 114`  
- `Tarjeta de conducta servicio militar 59`  
- `Tarjeta de identidad 42`  
- `Tarjeta Profesional 0`  
- `TOTAL 1303`  
- right-side detail table with `MES`, `FECHA`, `TIPO DOCUMENTO`, `CANTIDAD`, `ACUSE`, `CASO`, `PLANILLA`  
**Menus/windows:** Excel only, plus Teams share bar

### 9) Frames 00366–00374  
**Workbook:** same  
**Sheet:** `REGISTRO ATENCIONES`  
**Selection:** `E30` visible in one frame  
**Action:** pivot-table style review of attention records; fields pane open on the right  
**Visible data:**  
- left list of names with counts, e.g. `Diana Forero Coronel 334`, `Margarita Martinez Peralta 260`, `Luz Ginette Montes Fajardo 177`, `Yenny Patricia Rodriguez González 154`, `Danna Lucia Quintero Cifuentes 149`, `Blanca Florinda Sierra Velasquez 145`  
- total at bottom visible as `3120`  
- right pivot categories include localities like `Alcaldía local Engativá`, `Alcaldía local Ciudad Bolívar`, `Alcaldía local Fontibón`, etc.  
**Menus/windows:** `Campos de tabla dinámica` pane visible; Excel

### 10) Frames 00375–00380  
**Workbook:** same  
**Sheet:** `INFORME WEB ABRIL`  
**Selection:** pivot cell `B9` visible in one frame  
**Action:** reviewing web PQRS report sections and charts  
**Visible data:**  
- chapter header: `CAPÍTULO 6. SUBTEMAS MÁS REITERADOS Y/O BARRERAS DE ACCESO`  
- highlighted row about `ESPACIO PÚBLICO / INVASIÓN DEL ESPACIO PÚBLICO`  
- later pivot table: `TOTAL PETICIONES RECIBIDAS POR SECRETARÍA DE GOBIERNO`  
- visible counts include `VERDADERO 1972`, `FALSO 716`, `Total general 2788`  
- charts: `Gráfica No. 1 Total Peticiones del Mes`, `Distribución PQRS por Sexo`  
**Menus/windows:** Excel + Teams share bar; `Campos de tabla dinámica` pane visible in some frames

### 11) Frames 00383–00387  
**Workbook:** same  
**Sheet:** still `INFORME WEB ABRIL`  
**Selection:** pivot cell remains active  
**Action:** user opens `Analizar tabla dinámica` and clicks `Actualizar`  
**Visible data:** ribbon tab `Analizar tabla dinámica` open; dropdown under `Actualizar` visible  
**Menus/windows:** Excel ribbon dropdown

### 12) Frames 00388–00400  
**Workbook:** same  
**Sheet:** same underlying report  
**Selection:** unchanged behind dialog  
**Action:** refresh/update attempt fails  
**Visible dialog:** Excel warning modal  
- `El nombre de campo de tabla dinámica no es válido...`  
- button `Aceptar`  
**Cause:** pivot table refresh on invalid/missing field header  
**Menus/windows:** Excel modal error on top of the sheet; Teams share bar still visible in background

If you want, I can turn this into a **timestamped log** or a **CSV-style frame table** next.

[Batch 5 - gpt-5.4-mini]
Grouped by identical screen state; many frames are repeats.

| Frames | Workbook / sheet | Selection / edit | Action | Values visible | Open menus / dialogs |
|---|---|---|---|---|---|
| 00401–00403 | **BD PQRS BOGOTA TE ESCUCHA MAYO 2026**; dashboard sheet (pivot dashboard, tabs include **Reporte PQRS Mayo2026** / **INFORME WEB ABRIL**) | No clear cell selection; right pivot pane visible | Inspecting pivot dashboard | Charts/tables for **Total Peticiones del Mes** and related KPIs | Center modal: **“El nombre de campo de tabla dinámica no es válido”**; right pane **“Campos de tabla dinámica”** |
| 00404–00408 | Same workbook; dashboard | Chart object / plot area selected | Hovering/selecting chart elements; preparing source refresh | Chart titles and bars for **Total Peticiones del Mes** | Tooltip/dialog for **“Cambiar origen de datos”** appears over chart |
| 00409–00414 | Same workbook; active tab **Reporte PQRS Mayo2026** | Large raw-data range visible around rows **12884+**; dialog source box active | **Changing pivot table source range** | Data columns visible: **Número petición, Duplicado, Sector, Tipo de entidad, Tipo de Dependencia, Tema, Categoría, Subtema, Funcionario, Estado del…, Punto ate…, Canal, Tipo petic…, Estado pe…, Asunto, Proceso de Tr…** | Modal **“Cambiar origen de datos de tabla dinámica”** with source range field and **Aceptar / Cancelar** |
| 00415–00419 | Same workbook; sheet **INFORME WEB ABRIL** | Dashboard cells and chart objects visible | Returning to dashboard after source-change dialog | Top-left pivot: **TOTAL PETICIONES RECIBIDAS POR SECRETARIA DE GOBIERNO**; chart **“Gráfica No. 1 Total Peticiones del Mes”** with **VERDADERO / FALSO**; right info box **“DESCONGESTIÓN - SOLO INFORMATIVO”** with yellow highlighted metrics like **Gestión Externa** and **Gestión Oportuna** | Teams sharing bar at bottom (**Dejar de compartir / Ocultar**); pivot field pane still open |
| 00420–00429 | Same workbook; dashboard | Chart plot area / axis selected | Selecting or dragging chart element | Tooltips show **“Área de trazado”** and **“Eje horizontal (valor)”**; bar chart labels **VERDADERO / FALSO** remain visible | No new dialog; normal pivot pane and dashboard |
| 00440–00455 | Same workbook; sheet **INFORME WEB ABRIL** | Lower dashboard sections visible; no obvious cell edit | Scrolling through report sections | Sections visible: **Distribución de PQRS por sexo**, **por grupo poblacional**, **por identidad ciudadana**, and later **por condición poblacional**; charts and small summary tables visible | Right pane **Campos de tabla dinámica** persists; Teams share bar still present |
| 00456–00465 | Same workbook; same sheet | Lower report tables/charts | Continued inspection of report breakdowns | Identity table rows readable: **Cédula de ciudadanía, Cédula de extranjería, NIT, Permiso por Protección Temporal, Tarjeta identidad, Pasaporte, No especifica**; sex/group breakdown charts show totals in the ~2.7k range | No modal; just dashboard + pivot pane |
| 00494–00497 | Same workbook; sheet **INFORME WEB ABRIL** | **Cell E81** selected (name box shows **E81**) | Reviewing pivot-derived formula | Formula bar shows an **IMPORTARDATOSDINAMICOS** / GETPIVOTDATA-style formula, e.g. fetching **“Número petición”** filtered by **“Tipo de documento” = “Cédula de ciudadanía”** | Pivot pane open on right; no dialog |
| 00498–00500 | Same workbook; same sheet | Blank central area / lower tables; no new edit | Idle inspection / end of segment | Same lower dashboard tables remain visible | No new window; Teams share bar remains |

**Main transition:** the video moves from an Excel pivot error / source-refresh attempt to the raw data sheet, then back to the dashboard sheet where the report sections are reviewed and formulas are checked.

[Batch 6 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen is effectively the same.

| Frame range | Workbook / sheet | Selected cells / range | Action | Readable data | Open menus / dialogs |
|---|---|---|---|---|---|
| 00501–00517 | **BD PQRS BOGOTA E ESCUCHA MAYO 2026 - Excel** / **INFORME WEB ABRIL** | Active cell in the left pivot area, around **B81–B84** | Reviewing / editing a pivot-based report | Pivot sections: **“DISTRIBUCIÓN DE PQRS POR GRUPO POBLACIONAL”**, **“DISTRIBUCIÓN DE PQRS POR IDENTIDAD CIUDADANA”**, **“DISTRIBUCIÓN DE PQRS POR CONDICIÓN POBLACIONAL”**. Formula bar shows **IMPORTARDATOSDINAMICOS / GETPIVOTDATA** with fields like **“Número petición”**, **“Tipo de documento”**, **“Cédula de ciudadanía”**, **“Cédula de Extranjería”**, **“NIT”**, **“Permiso por Protección Temporal”**, **“Tarjeta de identidad”**. Totals visible: **278** and **269**. | Teams screen-share banner: **“teams.microsoft.com está compartiendo tu pantalla”** with **Dejar de compartir / Ocultar** |
| 00518–00524 | Same workbook / same sheet | Pivot-table cell selection shifts in the left summary area | Scrolling down into the interaction chapter | New section: **“CAPÍTULO 2. CANALES DE INTERACCIÓN”**. Channel chart title: **“Canales de Interacción”**. Visible labels: **TELEFONO**, **DIRECTO-PERSONALMENTE**, **BUZÓN**, **CORREO ELECTRÓNICO**, **VENTANILLA CDD**, **WEB**. WEB and VENTANILLA CDD are the largest bars. | Right pane opens: **Campos de tabla dinámica** |
| 00525–00580 | Same workbook / same sheet | Active cell changes within the pivot region, roughly **B81 / B84 / B86 / B100 / B123** depending on frame | Checking / editing pivot outputs and formulas | The lower pivot table shows columns like **Canal**, **Total**, **% Peticiones**; overall total visible around **278**. The formula bar keeps changing between GETPIVOTDATA lookups for different document types / categories. | Teams banner remains; pivot field pane remains open |
| 00581–00592 | Same workbook | Focus shifts to the pivot tools / source selection | Opening pivot settings | Ribbon switches to **Analizar tabla dinámica**. | Modal dialog appears: **“Cambiar origen de datos de tabla dinámica”** |
| 00593–00595 | **Reporte PQRS Mayo2026** sheet (raw data) | Active cell shows around **A10** | Selecting / confirming the pivot source range | Large raw dataset visible with many columns and rows. Readable row values include repeated status-like values such as **Recibida**, **Registrada**, **Pendiente**, **Cerrado**, and channels like **WEB** / **WEB SERVICE**. The table looks like the underlying source for the pivot report. | Pivot source dialog stays centered; **Campos de tabla dinámica** still on the right |
| 00596–00600 | Back to **INFORME WEB ABRIL** | Active cell shifts around **B100–B123** in the lower pivot/chart area | Verifying the updated chart and table | Channel distribution chart remains visible and centered. The summary table at left still shows channel totals and percentages. The dominant channels remain **WEB** and **VENTANILLA CDD**, followed by **CORREO ELECTRÓNICO**, **BUZÓN**, **DIRECTO-PERSONALMENTE**, and **TELÉFONO**. | Teams banner still present; pivot field pane still open |

### Main transitions
- **First state:** summary pivots + GETPIVOTDATA formulas.
- **Second state:** scroll down to **Canales de Interacción** chart.
- **Third state:** open **pivot source** dialog and switch to **Reporte PQRS Mayo2026** raw data.
- **Fourth state:** return to the report sheet and verify the updated pivot/chart.

If you want, I can turn this into a **strict per-frame log** next.

[Batch 7 - gpt-5.4-mini]
I’m reading this as one continuous Excel editing session, so I grouped identical frames and called out each visible transition.

- **Frames 601–602**
  - **Workbook/tab:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`, tab **INFORME WEB ABRIL**
  - **Selection:** pivot chart area / no clear cell edit
  - **Action:** reviewing pivot dashboard
  - **Visible data:** **Canales de Interacción** table/chart; total general **2619**; rows include **WEB**, **VENTANILLA CDI**, **CORREO ELECTRONICO**, **DIRECTO-PERSONALMENTE**, **BUZON**, **TELEFONO**
  - **Windows:** PivotChart Fields pane on the right; Teams sharing bar at bottom

- **Frames 603–604**
  - **Workbook/tab:** same workbook, tab **Reporte PQRS Mayo2026**
  - **Selection:** data range behind dialog
  - **Action:** changing pivot table source
  - **Visible data:** raw table with columns like **Tipo de entidad**, **Sector**, **Dependencia**, **Tema**, **Estado del trámite**, etc.
  - **Windows:** **Cambiar origen de datos de tabla dinámica** dialog

- **Frames 605–613**
  - **Workbook/tab:** same workbook, back on **INFORME WEB ABRIL**
  - **Selection:** dashboard area around section **CAPÍTULO 2. CANALES DE INTERACCIÓN**
  - **Action:** navigating/reviewing pivot results
  - **Visible data:** same channel totals; chart titled **Canales de Interacción**
  - **Windows:** Pivot fields pane on right; Teams bar remains visible

- **Frames 614–615**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** cell **B139** (name box shows **B139**)
  - **Action:** formula/result review
  - **Visible formula:** `=SUMA(B13:B138)`
  - **Visible data:** total value **2619** highlighted in yellow

- **Frames 616–621**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** within the **WEB** row / left pivot table area
  - **Action:** inspecting the pivot table
  - **Visible data:** channel table with totals and % of petitions
  - **Windows:** no new dialog; same right-side pivot fields pane

- **Frame 622**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** right-clicked cell/range in the table
  - **Action:** context menu opened
  - **Windows:** Excel context menu with **Cortar, Copiar, Pegado especial, Insertar celdas copiadas, Eliminar, Borrar contenido, Filtrar, Ordenar**

- **Frames 623–625**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** blank cell/range below the chart
  - **Action:** moving focus / preparing edit
  - **Windows:** no new dialogs; Teams bar still visible

- **Frames 626–630**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** pivot chart selected (resize handles visible)
  - **Action:** chart editing / chart object selected
  - **Visible data:** **Canales de Interacción**
  - **Windows:** **Campos de gráfico dinámico** pane on the right

- **Frames 631–634**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** scrolled down; section **CAPÍTULO 3. TIPOLOGÍAS O MODALIDADES** and **Tipos de Petición**
  - **Action:** reviewing next dashboard section
  - **Visible data:** chart/table with rows like **FELICITACION**, **SUGERENCIA**, **SOLICITUD DE COPIA**, **CONSULTA**, **DENUNCIA POR ACTOS DE CORRUPCIÓN**, **SOLICITUD DE ACCESO A LA INFORMACIÓN**, **RECLAMO**, **QUEJA**, **DERECHO DE PETICIÓN DE INTERÉS PARTICULAR**, **DERECHO DE PETICIÓN DE INTERÉS GENERAL**
  - **Windows:** dashboard continues below with another chart section

- **Frames 635–638**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** chart selected again
  - **Action:** source/field review for the pivot chart
  - **Windows:** **Cambiar origen de datos de tabla dinámica** dialog reappears

- **Frames 639–642**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** cell **C164** (name box shows **C164**)
  - **Action:** editing/reviewing a pivot value
  - **Visible formula/value:** formula bar shows a long decimal/percentage-like value; total visible nearby **269**
  - **Visible data:** **Tipos de Petición** chart with bars for the categories above

- **Frames 643–646**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** section **4. SOLICITUDES DE INFORMACIÓN**
  - **Action:** reviewing the table and donut/pie chart
  - **Visible data:** highlighted rows include **Solicitud de acceso a la información** and **Solicitudes de información recibidas**
  - **Windows:** chart 5 visible; no dialog

- **Frames 647–648**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** donut chart selected
  - **Action:** chart object manipulation
  - **Windows:** chart resize handles visible; PivotFields pane on the right

- **Frames 649–650**
  - **Workbook/tab:** **Reporte PQRS Mayo2026**
  - **Selection:** source data range behind dialog
  - **Action:** changing pivot source again
  - **Windows:** **Cambiar origen de datos de tabla dinámica** dialog over raw worksheet grid

- **Frames 651–656**
  - **Workbook/tab:** back to **INFORME WEB ABRIL**
  - **Selection:** donut chart / chart title area
  - **Action:** editing chart text; floating mini formatting toolbar appears
  - **Visible data:** top red bubble shows **113**; inner yellow bubble shows **29** (or close to that)
  - **Windows:** chart edit handles + mini font toolbar

- **Frames 657–672**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** same chart and nearby blank cells
  - **Action:** continued chart text/shape editing and repositioning
  - **Visible data:** same two-bubble chart; no new sheet change
  - **Windows:** Teams sharing bar stays present

- **Frames 673–676**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** section **Tabla No. 1. Peticiones gestionadas por rango de días**
  - **Action:** reviewing date-range pivot table
  - **Visible data:** columns like **0-3**, **1-5**, **6-30**, **Más de 30**, **(en blanco)**, **Total general**
  - **Windows:** Pivot fields pane on right with filters like **Estado petición final**, **Gestión en rango días**, **Tipo petición**, **Estado que recibe**

- **Frames 677–681**
  - **Workbook/tab:** **Reporte PQRS Mayo2026**
  - **Selection:** source data behind dialog
  - **Action:** source-range change / pivot maintenance
  - **Windows:** **Cambiar origen de datos de tabla dinámica** dialog

- **Frames 682–688**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** lower dashboard area
  - **Action:** reviewing **Tabla No. 2. Días de gestión a solicitudes trasladadas a otras entidades**
  - **Visible data:** many rows by entity, mostly **1** day in the average column
  - **Windows:** Pivot fields pane on right

- **Frames 689–691**
  - **Workbook/tab:** **Reporte PQRS Mayo2026**
  - **Selection:** raw data grid
  - **Action:** source-data dialog open again
  - **Windows:** **Cambiar origen de datos de tabla dinámica**

- **Frames 692–700**
  - **Workbook/tab:** **INFORME WEB ABRIL**
  - **Selection:** section **Tabla No. 3. Sistemas más reiterados y/o barreras de acceso**
  - **Action:** reviewing the summary table and highlighted items
  - **Visible data:** highlighted row **ESPACIO PÚBLICO INVASIÓN OCUPACIÓN...**; right-side summary box shows **Tabla No. 3** totals; overall totals around **1576** visible in the section
  - **Windows:** Pivot fields pane remains open; no new modal

If you want, I can turn this into a **clean CSV-style log per frame number**.

[Batch 8 - gpt-5.4-mini]
Prompt compilado (EN): “Analyze this Excel screenshot sequence and report workbook, sheet, selections, actions, values, and open dialogs; note transitions and read visible cell text/formulas.”  
Skills loaded: input-compressor, english-prompt-compiler, skill-router.

- **Frames 701-704**: Workbook **“BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel”**. Sheet looks like **“INFORME WEB ABRIL”**. Active cell around **B280/B300** in a pivot report. Visible action: **viewing/adjusting a PivotTable**; no content edit yet. Visible text: **“Tabla No. 2 DÍAS DE GESTIÓN A SOLICITUDES TRASLADADAS A OTRAS ENTIDADES”**, **“CAPITULO 6. SUBTEMAS MÁS RETIRADOS Y/O BARRERAS DE ACCESO”**. Right pane open: **Campos de tabla dinámica** with fields like **Número petición, Duplicado, Sector, Tipo de entidad, Entidad, Dependencia, Dependencia hija, Tema**; filters/values areas visible. Teams overlay visible.

- **Frame 705**: Same workbook. Dialog open: **“Cambiar origen de datos de tabla dinámica”**. Action: **changing the PivotTable source range**. Buttons **Aceptar / Cancelar** visible. Source points to **“Reporte PQRS Mayo2026”** (range text partially unreadable).

- **Frames 706-707**: Sheet **“Reporte PQRS Mayo2026”** visible. Name box shows **A10**. Same **Change PivotTable Data Source** dialog still open. Action: **confirming/selecting the source table/range** for the pivot. Grid shows raw report columns (e.g. **Número petición, Duplicado, Sector, Tipo de entidad, Dependencia**).

- **Frames 708-709**: Back to the report sheet. Name box around **B300**. Pivot report and chart visible again. Action: **returning from source dialog to the report view**. No obvious value change. Teams sharing banner still present.

- **Frames 710-713**: Same workbook/sheet. Left table shows **subthemes** and counts; highlighted row readable as **“ESPACIO PÚBLICO INVASION OCUPACION DE ANTEJARDINES INVASION DEL ESPAC…”** with count around **673** and percentage around **6.05%**. Upper-right summary table titled **“Tabla No. 3”** with columns **SUBTEMA / Total / Porcentaje**. Chart title: **“Total Subtemas más Reiterados”**. Visible chart labels include **382** and later **872 / 1572 / 2866**. Action: **reviewing pivot chart totals**.

- **Frames 714-720**: Same sheet, same report. The bar chart is more fully visible; the red horizontal bars and labels stabilize. Readable categories/values include **LEY 1801 DE 2016 CÓDIGO NACIONAL DE SEGURIDAD Y CONVIVENCIA**, **TRASLADO A ENTIDADES DISTRITALES**, **MANTENIMIENTO DE VÍAS INTERNAS DE LA LOCALIDAD**. Action: **scrolling/resizing/repositioning the chart area**. No data entry visible.

- **Frames 721-729**: Active cell changes among **H299 / B300 / B302**. The left pivot table remains; the chart on the right stays on **“Total Subtemas más Reiterados”**. Visible values in chart/table include **382**, **613**, **872**, **1572**, **2866**. Action: **hovering/inspecting pivot data; no structural edit**.

- **Frames 730-732**: View scrolls left to the underlying table. Formula bar/selected value shows **12904** at the bottom total row (**“Total general”**). Action: **navigating the raw data table / checking totals**. Chart becomes partly offscreen.

- **Frames 733-739**: Back to the chart view. The same pivot/chart pair is visible with the summary table above it. Readable totals still include **2866, 1572, 872** and the single-bar label **382** in some frames. Action: **continuing validation of the report totals**.

- **Frames 740-759**: Same workbook/sheet, mostly unchanged. Pivot table on the left, chart on the right, Teams sharing banner across the bottom center. Action: **inspection only**; no visible content update.

- **Frames 760-764**: **Right-click context menu** open over a worksheet cell/chart area. Menu items visible: **Cortar, Copiar, Opciones de pegado, Pegado especial, Borrar contenido, Ordenar, Obtener datos de Tabla/Rango..., Insertar comentario, Formato de celdas..., Definir nombre..., Vínculo**. Action: **opening context menu for a pivot/worksheet cell**.

- **Frame 765**: Hover tooltip visible over a pivot cell. Readable text: **“Cuenta de Número petición”**, **Valor: 70**, **Fila: PLANEACION LOCAL PLAN DE DESARROLLO**, **Columna: Cuenta de Número petición**. Action: **hover inspection of a pivot value**.

- **Frames 766-800**: Context menu is closed. The same report remains on screen: left-side subtheme table, right-side chart **“Total Subtemas más Reiterados”**, upper summary table **“Tabla No. 3”**. Readable values remain around **12904 total general**, and chart labels like **382 / 872 / 1572 / 2866**. Teams sharing banner persists. Action: **final visual verification; no new edit visible**.

If you want, I can turn this into a **frame-by-frame CSV/table** next.

[Batch 9 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen is effectively unchanged:

- **Frames 801–808**: Excel workbook **“BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel”**. A **pivot/report sheet** is open (tab text partly clipped; looks like the report/pivot area, not Hoja1). **Cell A306 → B306** appears selected across the sequence. The **“Campos de tabla dinámica”** pane is open on the right. Visible pivot content includes a table/chart about subthemes and a summary block (“**Total peticiones por subtemas**”/similar). A **Teams screen-sharing bar** is visible at the bottom.

- **Frames 809–810**: Same workbook, now on **sheet “Hoja1”**. Excel is in **Table Design** mode. A structured table starts at **A1** with headers like **Número petición, Duplicados, Sector, Tipo de entidad, Entidad, Tipo de dependencia, Dependencia, Dependencia hija, Tema, Categoría subtema, Subtema, Funcionario, Estado del Usuario, Punto atención**. No dialog open.

- **Frames 811–817**: Same table on **Hoja1**, slightly scrolled. Rows show values like **GOBIERNO**, **ENTIDADES DISTRI…**, **SECRETARIA**, **WEB SERVICE**, **ESCRITO**, **E-MAIL**. The table remains selected; no separate menu dialog.

- **Frames 818–823**: A **filter dropdown** is open on the header **“Categoría subtema”** (or nearby subtema header). The dropdown shows the search box and checkbox list; **“POSIBLES ACTOS DE CORRUPCIÓN”** is visible/selected. This is the filtering step.

- **Frames 824–826**: The filter is applied. The table is now showing filtered rows and the view is shifted right enough to expose columns like **Canal, Tipo petición, Estado petición inicial, Estado petición final, Estado de la petición, Asunto**. Values visible include **WEB SERVICE, ESCRITO, E-MAIL, QUEJA**, and status text like **“Registro”**, **“En trámite”**, **“Solucionado”**. Teams sharing overlay still present.

- **Frames 827–835**: Horizontal scroll moves farther right. More columns are visible: **Proceso de calidad, Trámite o servicio, Es trámite, Adjunto**. Repeated values include **MISIONAL**, **PROCESO ESTRATÉGICO**, **true/false**. Some rows show long text in **Asunto** such as **“SOLICITO…”** and **“RESPUESTA…”**.

- **Frames 836–839**: Same filtered table. The visible area is still the right side of the dataset; the formula bar shows long subject text (partially clipped). Rows include repeated petition records and status text like **“Por resp…”**.

- **Frames 840–845**: Same sheet and filter state. The active row/cell changes slightly, but there is **no structural change**. The table continues showing **Estado de la petición**, **Asunto**, and right-side flags.

- **Frames 846–850**: Same filtered table; right-side columns still in view. The Teams bar and participant bubble remain visible. No new dialog.

- **Frames 851–856**: Same state. Table continues to show petition rows with **false/true** values in flag columns and statuses like **“Solucionado - Por resp…”**.

- **Frames 857–869**: Same table, still on **Hoja1**. The visible area stays on the right half of the table. Some rows show phrases like **“ACUERDO 523…”** and repeated **MISIONAL** labels. No new window or menu.

- **Frames 870–879**: Horizontal scroll goes even farther right. Columns such as **Adjunto, Tiene procedencia, Entidad procedencia, Radicado de…** become visible. Many cells show **true/false**; the table remains filtered.

- **Frames 880–895**: Same rightmost table view, with minor row/selection movement only. No dialog; same workbook and sheet.

- **Frames 896–899**: Horizontal scroll moves back left. Now columns like **Funcionario, Estado del Usuario, Punto atención, Canal, Tipo petición** are visible again. Rows still show **GOBIERNO / ENTIDADES DISTRI… / SECRETARIA** and **WEB SERVICE / ESCRITO / E-MAIL**.

- **Frame 900**: The view is further left again, showing the table from **Sector** through **Tipo petición**. Active cell appears around **F5** (formula bar text is partially clipped but begins with **“Puede Consolidar…”**). This is the clearest “reset” back to the raw data columns.

**Open windows throughout**:  
- **Excel** workbook above  
- **Teams screen-sharing overlay** (“Dejar de compartir”)  
- **PivotTable Fields pane** only in the early pivot frames  
- **Filter dropdown** only around the category-subtheme filter frames

If you want, I can turn this into a **strict CSV-style frame log** next.

[Batch 10 - gpt-5.4-mini]
Here’s the frame-by-frame screen analysis, grouped by unique visual state (many frames are duplicates or near-duplicates):

### 1) Frames 00901–00916
- **Workbook/sheet:** `BD PQRS BOGOTA E ESCUCHA MAYO 2026 - Excel`, active sheet **`Hoja1`**
- **Selection:** one cell in the main table, near the upper-left area of the visible grid; the name box changes between `J5`, `J4`, `K5`-type positions as the view updates.
- **Action:** reviewing a structured Excel table; no obvious typing, just navigation/inspection.
- **Visible data:** columns like `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`, `Tema`, `Categoría subtema`, `Subtema`, `Funcionario`, `Estado del usuario`, `Punto atención`, `Canal`, `Tipo petición`. Rows show values such as:
  - `GOBIERNO`
  - `ENTIDADES DISTRI...`
  - `SECRETARIA`
  - `Puede Consolidar`
  - `Trasl. ALCALDIA LOCAL DE SANTA FE / KENNEDY / SAN CRISTOBAL / USME / SUBA / USAQUEN...`
  - `Activo`
  - `WEB SERVICE`, `ESCRITO`, `WEB`, `E-MAIL`
- **Menus/windows:** Excel ribbon on **`Diseño de tabla`**; Teams sharing overlay on the right with the avatar and button **`Dejar de compartir`**.

### 2) Frames 00917–00918
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** the view is horizontally scrolled right; the active cell is in the status columns.
- **Action:** inspection of status fields / data validation.
- **Visible data:** columns now include:
  - `Tipo de dependencia`
  - `Tema`
  - `Categoría subtema`
  - `Subtema`
  - `Funcionario`
  - `Estado del usuario`
  - `Punto atención`
  - `Canal`
  - `Tipo petición`
  - `Estado petición inicial`
  - `Estado petición final`
  - `Estado de la petición`
  - `Asunto`
  - `Proceso de calidad`
- **Readable cell text:** formula bar shows **`Solucionado - Por respuesta definitiva`** in one frame; another frame shows **`MISIONAL`**.
- **Menus/windows:** same Excel ribbon + Teams sharing overlay.

### 3) Frame 00919
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** a cell in the `Asunto` / status area.
- **Action:** reviewing a specific record.
- **Readable text in formula bar / row subject:**  
  **`SOLICITUD PRESTAMO 7 CARPAS X3 PARA EL DIA SABADO 13 DE JUNIO DE 2026 DE 11 AM A 7 PM.`**
- **Menus/windows:** same Excel/Teams overlay.

### 4) Frames 00920–00935
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** various cells in the right-side columns (`Estado de la petición`, `Asunto`, `Proceso de calidad`, etc.).
- **Action:** horizontal scrolling / record review; no modal dialog.
- **Visible data:** repeated table rows with statuses like:
  - `Registro - con preclasificación`
  - `En trámite - Por asignación`
  - `Solucionado - Por respuesta...`
  - `Solicitado`
  - booleans `true` / `false`
- **Menus/windows:** Excel ribbon remains on **`Diseño de tabla`**; Teams share overlay persists.

### 5) Frames 00936–00938
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** now farther right, showing columns like:
  - `Es trámite`
  - `Adjunto`
  - `Tiene procedencia`
  - `Entidad proceden...`
- **Action:** inspection of flags/booleans.
- **Visible values:** many cells show `true` / `false`.
- **Menus/windows:** same Excel + Teams sharing overlay.

### 6) Frames 00939–00948
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** still in the right-side table columns.
- **Action:** continued review of the same dataset.
- **Visible values:** row-level flags and status text remain visible; no obvious edits.
- **Menus/windows:** same.

### 7) Frame 00949
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** a cell whose formula bar shows a subject/record title.
- **Readable text:** **`INFORMACION ESTERILIZACION DE ANIMALES`**
- **Action:** moving through specific requests/subjects.
- **Menus/windows:** same Excel/Teams overlay.

### 8) Frame 00950
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row focused.
- **Readable text:** **`SOLICITUD CERTIFICADO LABORAL`**
- **Action:** record inspection.
- **Menus/windows:** same.

### 9) Frames 00951–00956
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** similar right-side table; current row changes.
- **Action:** inspecting different request subjects.
- **Visible text includes:** repeated table entries and subject rows; no dialog.
- **Menus/windows:** same.

### 10) Frame 00957
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Solicitud de ayuda con esta vía carrera 128 # 142 sabana de tibabuyes`** (partially clipped, but clearly about road assistance on Carrera 128 / 142, Sabana de Tibabuyes).
- **Action:** review of a request subject.
- **Menus/windows:** same.

### 11) Frame 00958
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`SOLICITUD DE ESTUDIOS Y DISEÑOS PARA LA INTERVENCION DE LA VIA UBICADA EN LA CALLE 92 ENTRE LAS CARRERAS 15 ESTE Y 20 ESTE`**
- **Action:** reviewing a road-infrastructure request.
- **Menus/windows:** same.

### 12) Frame 00959
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`SOLICITUD CERTIFICACION CONTRACTUAL CON FUNCIONES ESPECIFICAS Y/O OBLIGACIONES - CONTRATO DE PRESTACION DE SERVICIOS NO. 294/2025`**
- **Action:** inspection of a contract-certificate request.
- **Menus/windows:** same.

### 13) Frame 00960
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`TRASLADO POR COMPETENCIA`**
- **Action:** inspecting a transfer-by-competence record.
- **Menus/windows:** same.

### 14) Frame 00961
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`APOYO DE GESTION`**
- **Action:** inspecting another request type.
- **Menus/windows:** same.

### 15) Frame 00962
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Derecho de Petición / Solicitud de reparación y mantenimiento de andenes.`**
- **Action:** request review.
- **Menus/windows:** same.

### 16) Frame 00963
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`POR MEDIO DE LA PRESENTE LA ADMINISTRACION DE LA COPROPIEDAD SE PERMITE SOLICITAR DE MANERA RESPETUOSA LA INTERVENCION Y REPARACION DE LA VIA UBICADA SOBRE LA CARRERA 32A`**
- **Action:** reviewing a long formal request.
- **Menus/windows:** same.

### 17) Frame 00964
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** continues the previous long request about road intervention/reparation.
- **Action:** same review.
- **Menus/windows:** same.

### 18) Frame 00965
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** continues the same long road-intervention request.
- **Action:** same review.
- **Menus/windows:** same.

### 19) Frames 00966–00968
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** long infrastructure request remains on screen.
- **Action:** same review.
- **Menus/windows:** same.

### 20) Frames 00969–00970
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Solicitud de estudios y diseños para la intervención de la vía ubicada en la calle 92 entre las carreras 15 este y 20 este`** remains visible / revisited.
- **Action:** inspection of this specific request entry.
- **Menus/windows:** same.

### 21) Frame 00971
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`APOYO DE GESTION`** again.
- **Action:** review of record type.
- **Menus/windows:** same.

### 22) Frame 00972
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Derecho de Petición? Solicitud de reparación y mantenimiento de andenes.`**
- **Action:** row review.
- **Menus/windows:** same.

### 23) Frame 00973
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Derecho de Petición? Solicitud de reparación y mantenimiento de andenes.`** (same topic, slight scroll)
- **Action:** same review.
- **Menus/windows:** same.

### 24) Frame 00974
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** same road/sidewalk maintenance issue.
- **Action:** same review.
- **Menus/windows:** same.

### 25) Frame 00975
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** same request thread.
- **Action:** same review.
- **Menus/windows:** same.

### 26) Frame 00976
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`TRASLADO POR COMPETENCIA`** again.
- **Action:** navigation through the list.
- **Menus/windows:** same.

### 27) Frame 00977
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`URGENTE ARREGLAR PAVIMENTO DE LA CALLE 151 CON CARRERA 20 ES APROVECHAR QUE EL IDU ESTA ARREGLANDO LA CALLE 152...`**
- **Action:** review of urgent road-repair request.
- **Menus/windows:** same.

### 28) Frames 00978–00983
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** continuation of the urgent road-pavement request.
- **Action:** same review.
- **Menus/windows:** same.

### 29) Frame 00984
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Bogotá Lunes Mayo 18 2026 ... Solicito dar solucion al problema causado por Falta de mantenimiento del espacio...`** (partially visible)
- **Action:** review of a formal maintenance complaint.
- **Menus/windows:** same.

### 30) Frames 00985–00990
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** the same maintenance complaint remains visible across frames.
- **Action:** continued inspection.
- **Menus/windows:** same.

### 31) Frame 00991
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** same complaint thread.
- **Action:** same review.
- **Menus/windows:** same.

### 32) Frame 00992
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`SE SOLICITA LA INTERVENCION DE LA CALLE 137A CON CARRERA 45 Y CARRERA 46A EN EL BARRIO SAN JOSE SPRING VIA PRINCIPAL...`**
- **Action:** inspection of an infrastructure intervention request.
- **Menus/windows:** same.

### 33) Frame 00993
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`REPORTAR UN CRATER / HUECO CADA VEZ ES MAS PROFUNDO Y AFECTA LA MOVILIDAD, CRA 68I CL 18 SUR #32 BOGOTA`**
- **Action:** road defect report review.
- **Menus/windows:** same.

### 34) Frame 00994
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** continues the crater/hole report.
- **Action:** same review.
- **Menus/windows:** same.

### 35) Frames 00995–00996
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** same road defect report thread.
- **Action:** same review.
- **Menus/windows:** same.

### 36) Frame 00997
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`QUEJA FORMAL POR PROBLEMA DE ALCANTARILLADO Y MALOS OLORES`**
- **Action:** complaint review.
- **Menus/windows:** same.

### 37) Frame 00998
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** **`Bogotá Viernes, Mayo 15 2026 - 17:10 Señores IDU Cordial saludo Solicito dar mantenimiento vial dado que se presenta un hueco desde hace más de dos años...`** (partially visible)
- **Action:** review of a long maintenance request.
- **Menus/windows:** same.

### 38) Frames 00999–01000
- **Workbook/sheet:** same workbook, **`Hoja1`**
- **Selection:** subject row.
- **Readable text:** the maintenance/vial complaint continues.
- **Action:** final frames show the same dataset and review state.
- **Menus/windows:** same Excel window, same Teams overlay.

### Overall
- **Main workbook:** `BD PQRS BOGOTA E ESCUCHA MAYO 2026 - Excel`
- **Active tab throughout:** mostly **`Hoja1`**
- **Main action:** horizontal navigation through a large PQRS table; reviewing and validating request subjects, statuses, and routing flags.
- **No clear formula editing** is visible; the formula bar mostly shows plain text values from the selected cell.
- **Overlay:** Teams screen-sharing bar/button **`Dejar de compartir`** stays visible in many frames.
- **Other visible sheet tabs:** `Tabla 10 indicadores_Ajustado`, `Calificaciones Totales`, `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, `SEGUIMIENTO...`

If you want, I can turn this into a stricter CSV-style frame log.

[Batch 11 - gpt-5.4-mini]
Grouped by continuous span; frames within a span are near-identical except for cursor/hover changes.

| Frames | Workbook / sheet | Selection / action | Visible data / menus |
|---|---|---|---|
| 01001-01004 | Workbook title: **“BD PQRS Bogotá e Escucha Mayo 2026”** (partly clipped). Sheet **Hoja1**. | Name box changes **T26 → T30 → T34**. Scrolling/navigating table rows. | Table headers: **Punto atención, Canal, Tipo petición, Estado petición inicial, Estado petición final, Estado de la petición, Asunto, Proceso de calidad, Trámite o servicio, Es trámite, Adjunto, Tiene procedencia, Entidad proceden...**. Rows show values like **WEB SERVICE / WEB / ESCRITO**, **DERECHO DE PETICIÓN**, **QUEJA**, **Solucionado - Por respuesta definitiva**, **true/false**. Formula bar shows long text tied to the selected row. |
| 01005-01010 | Same workbook, **Hoja1**. | Name box changes **T36 → T38**; row navigation continues. | Formula bar text changes to items like **“TRASLADO DE RESPUESTA AL RADICADO 20261120075192”**, **“RESTAURACION ADQUIN PARQUE BOLSILLO URBANIZACION PALERMO”**, **“JORNADA RENDICION DE CUENTAS”**. Same Teams sharing banner at bottom. |
| 01011-01013 | Same workbook, **Hoja1**. | **Right-click sheet tab** open. | Context menu on sheet tab: **Insertar…, Eliminar, Cambiar nombre, Mover o copiar…, Ver código, Proteger hoja…, Color de pestaña, Ocultar, Mostrar…, Seleccionar todas las hojas**. Then delete confirmation dialog: **“Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?”** with **Eliminar / Cancelar**. |
| 01014-01016 | Same workbook; transition to report area, tab visible as **INFORME WEB ABRIL**. | Pivot table/chart tools active; name box shows **B306**. Hovering chart area. | Ribbon switches to **Analizar tabla dinámica**. Tooltip appears: **“Área del gráfico / Eje Horizontal (Valor)”**. Right pane **Campos de tabla dinámica** open. Report sheet shows a pivot chart and summary area. |
| 01017-01027 | Report sheet **INFORME WEB ABRIL**. | View centered on chart. | Chart title: **“Total Subtemas más Retirados”**. Readable bar values: **613, 780, 872, 1572, 2860**. Labels include **ESPACIO PÚBLICO INVASIÓN OCUPACIÓN DE ANTEJARDINES…**, **INFORMACIÓN DE TRÁMITES Y SERVICIOS**, **MANTENIMIENTO DE VÍAS INTERNAS DE LA LOCALIDAD**, **TRASLADO A ENTIDADES DISTRITALES**, **LEY 1801 DE 2016 CÓDIGO NACIONAL DE SEGURIDAD Y CONVIVENCIA**. Bottom Teams bar still visible. |
| 01028-01033 | Same report sheet. | Scrolling within the report. | Green section header: **“CAPÍTULO 6 SUBTEMAS MÁS RETIRADOS Y/O BARRERAS DE ACCESO”**. Left side shows a long ranked list; right side shows a small summary table and the bar chart. |
| 01034-01039 | Same report sheet. | Cursor/selection moves down the ranked list. | Highlighted row changes across items like **MANTENIMIENTO DE VÍAS INTERNAS DE LA LOCALIDAD** and nearby subthemes. Bottom tabs visible: **Tabla 10 indicadores_Ajustado, Calificaciones Totales, REGISTRADO SIDE, ENTREGADO SIDE, Reporte PQRS Mayo2026, INFORME WEB ABRIL**. |
| 01040-01042 | Transition to source-data editing view. | **PivotTable source change** in progress. | Dialog: **“Cambiar origen de datos de tabla dinámica”**. Underlying raw sheet shows the source table. |
| 01043-01044 | Raw data sheet (source table for the report). | Cell focus near **A10**. | Visible columns include **Número petición, Duplicados, Sector, Tipo de Entidad, Tipo de Dependencia, Dependencia, Tema, Subtema, Funcionario, Estado de…, Punto ate…, Canal, Tipo peti…, Estado…, Asunto, Proceso de…**. Rows show values like **GOBIERNO**, **SECRETARÍA DISTRITAL DE GOBIERNO**, **Oficina de atención a la ciudadanía**, **WEB SERVICE**, **DERECHO**. |
| 01045-01047 | Same raw sheet. | Source dialog closes; pivot tooling remains. | Right pane **Campos de tabla dinámica** visible again. The grid is a structured source table with many status fields such as **Activo, Notificado, Cerrado, En trámite**. |
| 01048-01053 | Back to report sheet **INFORME WEB ABRIL**. | Selection on the report table (name box around **A385/A398** depending frame). | Yellow total cell shows **12904** and **100.00%** in the summary box. Top list includes **LEY 1801 DE 2016 CÓDIGO NACIONAL DE SEGURIDAD Y CONVIVENCIA**, **ESPACIO PÚBLICO…**, **MANTENIMIENTO DE VÍAS INTERNAS DE LA LOCALIDAD**. |
| 01054-01060 | Same report sheet. | Scroll lower in the long list. | A lower **Total general** row is visible with **4933** and **100.00%**. The small summary table and chart remain on the right. |
| 01061-01067 | Same report sheet. | Cell around **C405** selected; formula visible. | Formula bar shows a **percentage calculation based on a row value divided by the absolute total** (visible form like **`=I397*100/$I$404`**). This is consistent with a percent-of-total field. |
| 01068-01073 | Same report sheet. | Selection shifts around **A397/A401**. | Left ranked list stays highlighted in orange/yellow on the current row. Right summary table unchanged. |
| 01074-01076 | Same report sheet. | **Right-click on a pivot/value cell**. | Context menu open with **Copiar, Opciones de pegado, Pegado especial, Insertar celdas copiadas…, Eliminar…, Borrar contenido, Filtrar, Ordenar, Obtener datos de Tabla/Rango…, Formato de celdas…, Definir nombre…, Vínculo**. Mini formatting toolbar appears above. |
| 01077-01082 | Same report sheet. | Context menu closes; paste options badge remains. | No structural change; still on the pivot/report area with the Teams overlay at bottom. |
| 01083-01091 | Same report sheet. | **Fill color palette** opened from the ribbon. | Color picker shows theme and standard colors; cursor hovers over swatches. Left list row remains highlighted. |
| 01092-01096 | Same report sheet. | Palette closes; selection unchanged. | Report table and chart remain stable; no new dialog. |
| 01097-01100 | Same report sheet **INFORME WEB ABRIL**. | Scrolled to the **bottom of the long subtheme list**. | Many low-count rows visible, then a blank white lower area. This is the end of the section; no new dialog. |

### Key transitions
- **Hoja1** record table → **sheet-tab delete attempt** → **report sheet / pivot chart**.
- **Pivot source change** dialog → back to the **raw data sheet** → back to **INFORME WEB ABRIL** report.
- Later frames focus on **editing/formatting pivot summary cells** and **percentage formulas**.

[Batch 12 - gpt-5.4-mini]
Workbook: **“BD PORS BOGOTA TE ESCUCHA MAYO 2026 - Excel”**

**Frames 01101–01108**
- Same sheet/workbook view, pivot-table area with **Campos de tabla dinámica** open on the right.
- Selection moves through cells around **B553 / B585 / B615 / B634 / B613**.
- Action: navigating a PivotTable and opening **Analyze PivotTable → Cambiar origen de datos**.
- Open dialogs: PivotTable Fields pane; then **Cambiar origen de datos de tabla dinámica**.

**Frames 01109–01111**
- Switched to sheet **“Reporte PQRS Mayo2026”**.
- Cell/area at **A10** visible; horizontal scroll moves to far-right columns (**…CW** area).
- Action: viewing raw source data / verifying records.
- Visible data: long table with columns like **Duplicados, Sector, Tipo de entidad, Dependencia, Estado, Asunto, Proceso**.

**Frames 01112–01118**
- Back to sheet **“INFORME WEB ABRIL”**.
- Pivot report **“Tabla No 5 PETICIONES TRASLADADAS POR NO COMPETENCIA”** visible.
- Action: inspecting pivot output and percentage box.
- Open pane: **Campos de tabla dinámica**.
- Visible yellow box: **“Cuadro informativo para calcular el porcentaje de traslados”** with **TOTAL PETICIONES = 10737** and **PORCENTAJE TRASLADADAS** (percentage shown but not fully legible).

**Frames 01119–01125**
- Same report sheet, same table.
- Action: clicking within the yellow summary box / pivot values.
- Visible numbers: **10737** remains in the total box; bottom tab bar still shows **INFORME WEB ABRIL** active.
- No major layout change, just cursor movement and pivot interaction.

**Frames 01126–01128**
- Same workbook/sheet, scrolled downward.
- Action: reviewing lower rows and the table totals.
- Visible bottom total row around **2786** in the main table.
- Right pane still shows PivotTable fields.

**Frames 01129–01135**
- Filter dropdown opened for **PERIODO ACTUAL**.
- Action: filtering by period/status.
- Dropdown values visible:
  - **(Todos)**
  - **PERIODO ACTUAL**
  - **PERIODO ANTERIOR**
- Another filter search shows text being typed: **“trasl”**.
- Options visible under that search include variants of **Solucionado por traslado** / similar transfer states.

**Frames 01136–01142**
- Same report sheet, lower section now visible.
- Action: scrolling to totals and checking the summary box.
- Visible yellow box again with **TOTAL PETICIONES = 10737** and transfer percentage.
- Bottom of table shows **Total general** and a percentage ending at **100.0%**.

**Frames 01143–01149**
- Same sheet with the period filter opened again.
- Action: toggling between **PERIODO ACTUAL / PERIODO ANTERIOR**.
- No structural change; pivot remains active.

**Frames 01150–01157**
- Same sheet, filter list now shows multiple status options.
- Action: selecting/deselecting filter items.
- Visible dropdown items include:
  - **Cerrado - Por no competencia**
  - **Solucionado - Por asignación**
  - **Solucionado - Por traslado DADIE**
  - **Solucionado - Registrar**
  - **Solucionado por asignar - Traslad…**
  - **(en blanco)**
- Cursor is inside the multi-select filter dialog.

**Frames 01158–01160**
- Same table, formula bar/value area visible.
- Action: hovering over a pivot value cell.
- Visible tooltip/value around a row shows **“Cuenta de Número petición”** and a specific row value.
- Yellow summary box still present at right.

**Frames 01161–01167**
- Scrolling downward through the report.
- Action: moving toward the next section and the blank lower area of the sheet.
- Visible end of the current table and a large blank region below.

**Frames 01168–01170**
- New section appears: **“Tabla No 6 SUBTEMA VEEDURÍAS CIUDADANAS”**.
- Below it: **“Tabla No 7 PETICIONES CERRADAS O EN TRÁMITE PERIODO ACTUAL”**.
- Action: checking pivot breakdown by subtema/estado.
- Filter dialog shows **Estado petición final** with **PERIODO ACTUAL**.

**Frames 01171–01176**
- Switched again to **“Reporte PQRS Mayo2026”**.
- Action: reopening **Cambiar origen de datos de tabla dinámica**.
- Raw data grid visible behind the dialog; rows include many records and status columns.
- In 01175, data is on a different region of the raw sheet, with more columns visible (contacts/status fields).

**Frames 01177–01183**
- Back to the report sheet, Table 7 area.
- Action: reviewing the closed/in-tramite summary and right-side yellow matrix.
- Visible yellow table titled roughly:
  - **CAPITULO 7 PETICIONES CERRADAS O EN TRÁMITE PERIODO…**
  - **RESPUESTA TOTAL**
- The right matrix lists localities (e.g. **ALCALDÍA…**) with counts/percentages.

**Frames 01184–01188**
- PivotTable Fields pane visible again.
- Action: changing table layout/fields; dialog **Cambiar origen de datos** pops up over the pivot.
- Field selection includes **Dependencia** checked in the right pane.

**Frames 01189–01199**
- Same Table 7 section.
- Action: selecting a block of pivot cells / summary region.
- A large grey highlighted range spans the main table area.
- Right pane still shows PivotTable fields.
- Bottom status bar shows changing selection stats (count/sum/average).

**Frame 01200**
- Same sheet, but scrolled so the current table is partly above view.
- Action: continuing to navigate through the report and pivot sections.
- The active sheet remains **INFORME WEB ABRIL**.

If you want, I can turn this into a **CSV-style frame log** with one line per frame number.

---

## Segmento 11: Ranking por localidad y datos de supercades

| Campo | Valor |
|---|---|
| **Duración** | 100:00 - 120:00 |
| **Descripción** | Ranking de PQRS por localidad, datos de supercades (20 de Julio, Américas, Bosa, etc.), orientaciones y encuestas por punto |
| **Frames analizados** | 1200 |
| **Batches** | 12 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 1925s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Verificado.

**Libro:** `BO PQRS BOGOTA E ESCUCHA MAYO 2026 - Excel`  
**Tabs visibles:** `Tabla 10 indicadores_Ajustado`, `Calificaciones Totales`, `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, `SEGUIMIENTO DIAS`

### Resumen por tramo
- **F01-F02:** hoja **`INFORME WEB ABRIL`**. Se ve una tabla dinámica a la izquierda y, a la derecha, un bloque amarillo tipo gráfico/tabla con título de **Capítulo 7**. Está seleccionada el área del gráfico/objeto; panel **Campos de tabla dinámica** abierto. Teams muestra “está compartiendo tu pantalla”.
- **F03:** clic derecho sobre el área amarilla; aparece menú contextual de Excel con **Cortar, Copiar, Opciones de pegado, Pegado especial, Eliminar, Borrar contenido, Análisis rápido, Filtrar, Ordenar, Obtener datos de Tabla/Rango, Insertar comentario, Formato de celdas, Elegir de la lista desplegable, Definir nombre, Vínculo**.
- **F04-F10:** mismo libro/hoja, misma composición. El cursor se mueve dentro del área del gráfico/tabla derecha; en la barra de fórmulas se alcanzan a ver valores como **29** y **15** en algunos cuadros. Sin cambio estructural.
- **F11-F25:** pantalla casi idéntica; sigue la tabla dinámica izquierda, el bloque amarillo derecho y el panel de campos. No se ve cambio de rango, solo navegación.
- **F26:** cambia la vista hacia una zona inferior del reporte; se alcanza a ver más del cuerpo del informe con tablas de capítulos y filas de localidades.
- **F27-F34:** hoja **`INFORME WEB ABRIL`** con tablas grandes:
  - **Tabla No. 7 / 8** de **peticiones cerradas o en trámite**.
  - **Tabla No. 9** de **tiempo promedio de respuesta por tipología y dependencia (días)**.
  - Se ven localidades como **Antonio Nariño, Barrios Unidos, Bosa, Candelaria, Chapinero, Ciudad Bolívar, Engativá, Fontibón, Kennedy, Mártires, Puente Aranda, Rafael Uribe, San Cristóbal, Santa Fe, Suba, Sumapaz, Teusaquillo, Tunjuelito, Usaquén, Usme**.
- **F35-F36:** cambia a hoja **`Reporte PQRS Mayo2026`**. Aparece el diálogo **“Cambiar origen de datos de tabla dinámica”** sobre una hoja de datos crudos con muchas columnas (BA, BB, etc.). Se está ajustando el origen de la tabla dinámica.
- **F37-F44:** vuelve a **`INFORME WEB ABRIL`**; se ve la tabla grande con filas de localidades y el panel de campos. Selección sobre celdas de la tabla dinámica.
- **F45-F49:** diálogo **“Buscar y reemplazar”**. Se usa para limpiar valores; el campo **Reemplazar con:** muestra **0**. Luego aparece confirmación de Excel.
- **F50:** mensaje de Excel: **“Ya está. Hemos hecho 8 reemplazos.”**
- **F51-F56:** regreso a la tabla amarilla/resaltada; se sigue trabajando sobre el bloque de **Capítulo 7**.
- **F57-F68:** misma hoja con tablas de capítulos; el foco está en la zona de **tabla 7/8/9** y en el panel de campos. Se ve selección de celdas en el informe.
- **F69-F70:** se ve la **Tabla No. 9** y varias celdas resaltadas en amarillo dentro del bloque de tiempos de respuesta.
- **F71-F76:** selección horizontal sobre columnas de días y luego apertura del **selector de color de relleno** (paleta de colores). Acción: quitar/cambiar resaltado amarillo.
- **F77-F80:** vuelve el diálogo **“Cambiar origen de datos de tabla dinámica”** y después la hoja de datos crudos; se está reajustando el rango fuente.
- **F81-F82:** sigue la hoja de datos crudos con el mismo diálogo abierto.
- **F83-F100:** regreso a **`INFORME WEB ABRIL`**; la vista baja a la **Tabla No. 9** y a la sección **“CANT. PQRS GESTIONADAS EN TIEMPO PROMEDIO DE RESPUESTA POR TIPOLOGÍA Y DEPENDENCIA (CANTIDAD DE PQRS)”**.  
  - Se ven columnas de tipología: **CONSULTA, DENUNCIA POR ACTOS DE CORRUPCIÓN, DERECHO DE PETICIÓN DE INTERÉS GENERAL, DERECHO DE PETICIÓN DE INTERÉS PARTICULAR, QUEJA, RECLAMO, SOLICITUD DE ACCESO A LA INFORMACIÓN**.
  - Hay celdas seleccionadas dentro de la tabla dinámica; en algunos frames se muestran tooltips de pivote como **“Promedio de Días gestión”** con valor y etiqueta de localidad/columna.
  - La barra inferior sigue mostrando **Teams compartiendo pantalla**.

### Menús / ventanas abiertas
- **Excel**
  - Menú contextual (F03)
  - **Buscar y reemplazar** (F45-F49)
  - **Cambiar origen de datos de tabla dinámica** (F35-F36, F77-F82)
  - Selector de **color de relleno** (F75)
- **Teams**
  - Barra “está compartiendo tu pantalla”
  - Panel lateral con participante **Yesenia Patiño Figueroa**

Si quieres, te lo convierto ahora en una **tabla frame por frame (01–100)**.

[Batch 2 - gpt-5.4-mini]
Here’s the frame-by-frame analysis, grouped by visible state changes:

### Frames 101–140
**Workbook:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`  
**Sheet:** selected tab is truncated in the capture as `INF...`  
**Open UI:** PivotTable Fields pane on the right; Excel ribbon visible

**What’s happening:**
- The user is working inside a PivotTable report titled **`Tabla No 9. TIEMPO PROMEDIO DE RESPUESTA POR TIPOLOGIA Y DEPENDENCIA (DIAS)`**.
- The selected cell keeps moving within the pivot table; the Name Box shows references like **E900, E897, E893, E880, H878, H882, G892, H894** across the sequence.
- At **frames 108–109**, the **Fill Color** palette is opened from the ribbon.
- Yellow fill is then applied to specific cells/ranges in the pivot table, apparently to mark values being reviewed.

**Visible fields/headers:**
- `CONSULTA`
- `DENUNCIA POR ACTOS DE CORRUPCION`
- `DERECHO DE PETICION DE INTERES GENERAL`
- `DERECHO DE PETICION DE INTERES PARTICULAR`
- `QUEJA`
- `RECLAMO`
- `SOLICITUD DE ACCESO A LA INFORMACION`
- `SOLICITUD DE COPIA`
- `SUGERENCIA`
- `FELICITACION`

**Readable values seen in the formula bar / cells:**
- `1,56529680365297`
- `11,5`
- `9,33333333333333`
- `17,3076923076923`
- `13,375`

**Action:** cell selection + formatting; no visible copy/paste, insert, or sort dialog.

---

### Frames 141–164
**Screen transition:** Excel → Chrome/Teams

**Visible window:** Microsoft Teams in Chrome  
**Open UI:** meeting controls, share banner, recording/transcription popup

**What’s happening:**
- The screen switches to a Teams meeting page with the message:
  - **`Esperando a que se unan otros usuarios...`**
- A banner indicates screen sharing:
  - **`teams.microsoft.com está compartiendo tu pantalla`**
- A pop-up appears for:
  - **`Grabación y transcripción`**
- Hover tooltip appears over the mic button:
  - **`Reactivar audio del micrófono`**

**Action:** no spreadsheet editing visible; just meeting/waiting-room state and control hover.

---

### Frames 165–200
**Workbook:** same Excel file  
**Sheet:** same truncated `INF...` tab  
**Open UI:** PivotTable Fields pane still visible

**What’s happening:**
- Back in Excel, the pivot table is now scrolled further right.
- The **`Total general`** column is visible on the far right.
- Yellow-highlighted cells continue to be applied across the table, especially in the right-side columns.
- The selection keeps moving cell-by-cell through the pivot table; this looks like a validation pass over values above thresholds.

**Visible headers now include:**
- `SOLICITUD DE ACCESO A LA INFORMACION`
- `SOLICITUD DE COPIA`
- `SUGERENCIA`
- `FELICITACION`
- `Total general`

**Action:** continued highlighting/review of pivot-table values; still no visible insert/sort/copy dialog.

---

### Overall
This segment is mostly:
1. **Excel pivot-table review**
2. **Yellow highlighting of flagged values**
3. **Brief switch to Teams waiting/share state**
4. **Return to Excel for more validation**

If you want, I can turn this into a **strict frame-by-frame table** for all 100 frames.

[Batch 3 - gpt-5.4-mini]
Grouped by near-identical stretches:

### Frames 00201–00206
- **Workbook:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026` (Excel)
- **Sheet:** pivot-report sheet; visible tab cluster includes `Tabla 10 indicadores_Ajustado`, `Calificaciones Totales`, `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, `SEGUIMIENTO DÍAS`
- **Selection:** active cell around **J897** / nearby pivot cells
- **Action:** inspecting a pivot table, not editing text
- **Visible data:** pivot table with yellow bars; headers include categories like **Derecho de petición de interés particular**, **Queja**, **Reclamo**, **Solicitud de acceso a la información**, **Solicitud de copia**, **Sugerencia**, **Felicitación**
- **Menus/windows:** right pane **“Campos de tabla dinámica”** open with fields like `Número petición`, `Duplicados`, `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`, `Tema`

### Frames 00207–00209
- **Window:** Microsoft Teams in browser
- **Screen:** meeting waiting room: **“Esperando a que se unan otros usuarios…”**
- **Other UI:** recording/transcription banner visible; screen-sharing overlay present
- **Action:** transition away from Excel, no spreadsheet edit visible

### Frames 00210–00215
- **Workbook:** same Excel file
- **Sheet:** same report sheet, likely `INFORME WEB ABRIL`
- **Selection:** pivot cells shift while scrolling horizontally
- **Action:** navigating the report; no clear typing
- **Visible data:** top totals row and yellow-highlighted response bars; some labels show **15 DÍAS**
- **Menus/windows:** `Campos de tabla dinámica` still visible on the right

### Frames 00216–00218
- **Workbook:** same
- **Sheet:** report section titled **“Tabla No. 9. TIEMPO PROMEDIO DE RESPUESTA POR TIPOLOGÍA Y DEPENDENCIA (DÍAS)”**
- **Selection:** pivot cell focus moves across the table
- **Action:** viewing/validating the pivot
- **Visible data:** locality rows like `ALCALDÍA LOCAL DE ...`; columns include:
  - `DENUNCIA POR ACTOS DE CORRUPCIÓN`
  - `DERECHO DE PETICIÓN DE INTERÉS GENERAL`
  - `DERECHO DE PETICIÓN DE INTERÉS PARTICULAR`
  - `QUEJA`
  - `RECLAMO`
  - `SOLICITUD DE ACCESO A LA INFORMACIÓN`
  - `SOLICITUD DE COPIA`
  - `SUGERENCIA`
  - `FELICITACIÓN`
- **Menus/windows:** same pivot field pane on the right

### Frames 00219–00230
- **Workbook:** same
- **Sheet:** same report table
- **Selection:** horizontal scroll continues; active cell moves through numeric cells in the pivot
- **Action:** reviewing day values and totals
- **Visible data:** many small day counts in cells; several yellow bars highlight higher values
- **Menus/windows:** no new dialog; still the pivot field pane

### Frames 00231–00245
- **Workbook:** same
- **Sheet:** same report, now showing more locality rows and totals
- **Selection:** focus moves through rows such as `ALCALDÍA LOCAL DE ANTONIO NARIÑO`, `BOSA`, `CHAPINERO`, etc.
- **Action:** checking row values in the pivot; likely preparing to change source / validate output
- **Visible data:** totals row visible at bottom; hover tooltips begin to appear in later frames
- **Menus/windows:** right pivot pane remains open

### Frames 00246–00255
- **Workbook:** same
- **Sheet:** same pivot report
- **Selection:** active cell moves across the middle of the table
- **Action:** **format/inspection step**; the color palette is opened in later frames
- **Visible data:** pivot rows and totals remain; yellow fills are visible in some cells
- **Menus/windows:** at **00248–00255** the Excel **fill color palette** is open from the Home ribbon, suggesting the user is about to remove/change fill formatting

### Frames 00256–00258
- **Workbook:** same
- **Sheet/tab context:** PivotTable tools active (`Analizar tabla dinámica`)
- **Action:** **changing the PivotTable data source**
- **Dialog:** **“Cambiar origen de datos de tabla dinámica”**
- **Visible controls:** radio button for selecting table/range, range field populated, `Aceptar` / `Cancelar`
- **Meaning:** user is re-pointing the pivot to a different source range

### Frames 00259–00260
- **Workbook:** switch to raw data sheet, tab **`Reporte PQRS Mayo2026`**
- **Action:** selecting the source table/range for the pivot
- **Visible data:** raw dataset with columns like:
  - `Nro`
  - `Duplicados`
  - `Sector`
  - `Tipo de Entidad`
  - `Tipo de Dependencia`
  - `Dependencia`
  - `Dependencia hija`
  - `Tema`
  - `Categoría`
  - `Subtema`
  - `Funcionario`
  - `Estado`
  - `Punto ate`
  - `Canal`
  - `Tipo pet`
  - `Estado pe`
  - `Asunto`
- **Values:** many rows show `FALSO`, `VERDADERO`, government entities, emails, and IDs
- **Dialog:** source-range dialog still open over the grid

### Frames 00261–00262
- **Workbook:** back to pivot/report view
- **Action:** source change appears accepted or dialog dismissed
- **Visible data:** pivot table refreshed; totals and yellow bars still present

### Frames 00263–00267
- **Workbook:** same
- **Action:** hovering over pivot cells
- **Tooltips:** show `Cuenta de Número petición` and row-level labels such as locality names
- **Meaning:** user is validating specific pivot values after the source change

### Frames 00268–00279
- **Workbook:** same report
- **Sheet:** `INFORME WEB ABRIL` / pivot report section
- **Action:** continued scrolling through locality rows and response-time columns
- **Visible data:** same typology headers; multiple locality names listed in the leftmost rows

### Frames 00280–00287
- **Workbook:** same
- **Sheet:** lower pivot section titled **“CANT. PQRS GESTIONADAS EN TIEMPO PROMEDIO DE RESPUESTA POR TIPOLOGÍA Y DEPENDENCIA (CANTIDAD DE PQRS)”**
- **Action:** checking the count table below the time table
- **Visible data:** same typology columns; bottom totals row visible
- **Meaning:** this is the count companion table to the days table

### Frames 00288–00300
- **Workbook:** same
- **Action:** final validation of the lower pivot table; cell focus moves near the bottom totals
- **Visible data:** tooltip at one point shows **`Cuenta de Número petición`** with **value 49** for the `SOLICITUD DE ACCESO A LA INFORMACIÓN` column on the `Total general` row
- **Menus/windows:** no new dialog; pivot field pane remains on the right
- **End state:** report remains open on the pivot sheet, with the lower table and totals visible

If you want, I can turn this into a **strict per-frame CSV-style log** next.

[Batch 4 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped where the screen state is effectively the same.

### Frames 00301–00302
- **Workbook / sheet:** `BD PQRS BOGOTA E ESCUCHA MAYO 2026` → `INFORME WEB ABRIL`
- **Selection / edit:** no clear cell edit; just the sheet view.
- **Action:** viewing the report overview.
- **Visible data:** upper summary table with yellow-highlighted bars; lower left mini-table titled **“Promedio días de gestión”**.
- **Open windows:** Excel + Teams share banner (“teams.microsoft.com está compartiendo tu pantalla”).

### Frames 00303–00314
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** scrolling through the report; focus moves to the large pivot tables.
- **Action:** reviewing/adjusting pivot output for **“Tabla No. 10. Distribución PQRS por Localidades y Nivel Central”** and **“Tabla No. 9. Tiempo promedio de respuesta por tipología y dependencia (días)”**.
- **Visible data:** locality rows like **ALCALDÍA LOCAL DE USAQUÉN, SUMAPAZ, TUNJUELITO, USME, etc.**  
  Readable totals include values such as **2923**, **1392**, **4095** in the summary areas.
- **Open windows:** Excel + Teams share banner.

### Frames 00315–00318
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** pivot table is active; the **“Campos de tabla dinámica”** pane is open on the right.
- **Action:** configuring the pivot layout.
- **Visible data:** field list shows items like **Número petición, Duplicado, Sector, Tipo de entidad, Entidad, Tipo de dependencia, Dependencia, Dependencia hija, Tema**.
- **Open windows:** Excel pivot field pane + Teams banner.

### Frames 00319–00328
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** focus remains on the pivot table area; highlighted cells in the report.
- **Action:** continuing pivot adjustment / review of response-time tables.
- **Visible data:** yellow bars in the response-time matrix; the report keeps the same locality rows and typology columns.
- **Open windows:** Excel pivot field pane + Teams banner.

### Frames 00329–00334
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** lower report area active.
- **Action:** reviewing **“CANT. PQRS GESTIONADAS EN TIEMPO PROMEDIO DE RESPUESTA…”** and the locality-by-tipology matrix.
- **Visible data:** typology headers visible: **QUEJA, RECLAMO, SOLICITUD DE ACCESO A LA INFORMACIÓN, SOLICITUD DE COPIA, SUGERENCIA, FELICITACIÓN**.
- **Open windows:** Excel + Teams banner.

### Frames 00335–00336
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** right-click/context menu opened.
- **Action:** formatting operation on selected cells (likely fill/clear formatting).
- **Visible data:** context menu with **cut/copy/paste** options and color palette.
- **Open windows:** Excel context menu + Teams banner.

### Frames 00337–00345
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** a block of cells in the lower table is selected.
- **Action:** editing/formatting the pivot output.
- **Visible data:** selected grey block in the lower matrix; yellow-highlighted bars remain in the typology table above.
- **Open windows:** Excel + Teams banner.

### Frames 00346–00353
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** a cell near the bottom of the report is active.
- **Action:** formula/update work in the lower summary table.
- **Visible data:** formula bar shows a sum-style formula, readable as **`=B970+C970`** (exact cell visible as an active cell around row 970).
- **Open windows:** Excel + Teams banner.

### Frames 00354–00366
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** continued navigation through the same report block.
- **Action:** reviewing filtered pivot outputs and summary rows.
- **Visible data:** repeated locality list and typology counts; totals row remains visible.
- **Open windows:** Excel + Teams banner.

### Frames 00367–00369
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** lower table active.
- **Action:** moving through the report, no major UI change.
- **Visible data:** the response-time matrix and totals row remain in view.
- **Open windows:** Excel + Teams banner.

### Frames 00370–00378
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** top-left report area active.
- **Action:** navigating to the **“Tabla No. 8. PETICIONES CERRADAS EN TRÁMITE PERIODOS ANTERIORES”** and then to **“Tabla No. 9. TIEMPO PROMEDIO…”**.
- **Visible data:** pivot summaries with locality rows and percentage columns.
- **Open windows:** Excel + Teams banner.

### Frames 00379–00383
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** filter area active on the pivot table.
- **Action:** switching between **periods** / reviewing **“Tabla No. 8”** and **“Tabla No. 7”** views.
- **Visible data:** titles:
  - **Tabla No. 8. PETICIONES CERRADAS EN TRÁMITE PERIODOS ANTERIORES**
  - **Tabla No. 7. PETICIONES CERRADAS EN TRÁMITE PERIODO ACTUAL**
- **Open windows:** Excel pivot field pane + Teams banner.

### Frames 00384–00393
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** pivot filter dropdown opened for **PERIODO ACTUAL**.
- **Action:** preparing to filter the status/period selection.
- **Visible data:** dropdown list on the left with checkboxes; top-left filter says **PERIODO ACTUAL**.
- **Open windows:** Excel filter dropdown + pivot field pane + Teams banner.

### Frames 00394–00397
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** same filter dropdown, now with search text entered.
- **Action:** filtering the dropdown list by typing **`def`**.
- **Visible data:** list narrows to items like **“Solucionado - Por respuesta definitiva”**; buttons **ACEPTAR** / **Cancelar** visible.
- **Open windows:** Excel filter dialog + Teams banner.

### Frames 00398–00400
- **Workbook / sheet:** same workbook, same sheet.
- **Selection / edit:** filtered results now applied.
- **Action:** confirming the filter and recalculating the pivot table.
- **Visible data:** table updates to show **100.0%**-style columns and locality rows; large selected range remains active in the upper table.
- **Open windows:** Excel + Teams banner.

### Key transition points
- **00315:** pivot field pane appears.
- **00335:** right-click formatting menu opens.
- **00346:** visible formula entry/update (`=B970+C970`).
- **00379:** switch to the “peticiones cerradas” tables.
- **00394–00397:** filter dropdown search and selection.
- **00398–00400:** filtered pivot recalculates.

[Batch 5 - gpt-5.4-mini]
Usando el workbook **“BD PQRS BOGOTA E ESCUCHA MAYO 2026”** y la hoja **“INFORME WEB ABRIL”**.

**Resumen por tramos de frames (escenas casi idénticas agrupadas):**

- **00401–00402**
  - **Visible:** Tabla dinámica **“Tabla No. 7. Peticiones cerradas o en trámite periodo actual”**.
  - **Selección:** bloque gris dentro de la tabla/pivote.
  - **Acción:** solo visualización/posible selección de rango.
  - **Datos legibles:** **Total general = 3623**. Localidades como Antonio Nariño, Barrios Unidos, Bosa, etc.
  - **Ventanas:** cinta de Excel; barra de Teams compartiendo pantalla; avatar “Yesenia Patiño Figueroa”.

- **00403–00407**
  - **Visible:** misma hoja; se abre el panel derecho **“Campos de tabla dinámica”**.
  - **Selección:** pivote con campos como **Número petición, Duplicado, Sector, Tipo de entidad, Entidad, Tipo de dependencia, Dependencia, Dependencia hija, Tema**.
  - **Acción:** ajuste/revisión de campos de la tabla dinámica.
  - **Ventanas:** panel de campos abierto a la derecha.

- **00408–00416**
  - **Visible:** parte inferior con **Tabla No. 9** y **Tabla No. 10**; también aparece **Tabla No. 11 Localidades y Nivel Central**.
  - **Selección:** celdas/rangos en los pivotes inferiores; en varias tomas se ven barras amarillas de formato condicional.
  - **Acción:** scroll hacia abajo y revisión de resultados/formatos.
  - **Datos legibles:**  
    - **Tabla No. 9:** “Tiempo promedio de respuesta por tipología y dependencia (días)”.  
    - Tipologías visibles: **Consulta, Denuncia por actos de…, Derecho de petición de interés…, Queja, Reclamo, Solicitud de acceso a la información, Solicitud de copia**.
  - **Ventanas:** Teams sigue superpuesto.

- **00417–00423**
  - **Visible:** filtro desplegable de **“Estado petición final”**.
  - **Selección:** lista con casillas; se ve **“Seleccionar varios elementos”** activado.
  - **Acción:** filtrado múltiple y luego clic en **“ACEPTAR”**.
  - **Opciones visibles:** **Cerrado - Por no competencia**, **Cerrado por vencimiento de término**, **Por aclarar - por solicitud aclaración**, **Solucionado - Por asignación**, **Solucionado - Por respuesta definitiva**, **Solucionado - Por traslado**, **Solucionado - Registro con precisión**.
  - **Ventanas:** cuadro de filtro de Excel abierto.

- **00424–00434**
  - **Visible:** tablas inferiores ya con el filtro aplicado; reaparecen **Tabla 10** y **Tabla 11**.
  - **Selección:** celdas en la zona de la tabla de distribución y totales.
  - **Acción:** scroll y validación de datos resultantes.
  - **Datos legibles:** vuelve a verse **Total general = 3623** en la tabla superior; la tabla 11 muestra meses en filas.

- **00435–00440**
  - **Visible:** otra vez el filtro de **Estado petición final**.
  - **Selección:** mismo modo multiselección.
  - **Acción:** revisión y confirmación del filtro con **ACEPTAR**.
  - **Ventanas:** lista de estados abierta; el puntero está sobre el botón de aceptar.

- **00441–00459**
  - **Visible:** tablas **8, 9 y 10** combinadas por scroll.
  - **Selección:** rangos de pivote y una zona resaltada en amarillo en la Tabla 9.
  - **Acción:** navegación por los reportes; validación visual de tiempos y distribución.
  - **Datos legibles:**  
    - **Tabla No. 8:** “Peticiones cerradas o en trámite periodos anteriores”.  
    - **Tabla No. 10:** “Distribución PQRS por localidades y Nivel Central”.
  - **Ventanas:** sin diálogos nuevos; Teams sigue visible.

- **00460–00463**
  - **Visible:** zona de la **Tabla No. 10** y parte de la **Tabla No. 11**.
  - **Selección:** se ve un clic derecho / menú contextual de Excel con opciones de pegado.
  - **Acción:** copiar/pegar o edición de celdas en el pivote.
  - **Ventanas:** menú contextual abierto en **00461**; luego desaparece y queda la selección en la tabla.

- **00464–00475**
  - **Visible:** **Tabla No. 9** con barras amarillas, y debajo **Tabla No. 10**.
  - **Selección:** celdas del pivote inferior.
  - **Acción:** scroll final y revisión de resultados.
  - **Datos legibles:** columnas de días (3, 5, 10, 15, etc.) y más marcas amarillas en tiempos que superan el umbral.
  - **Ventanas:** no hay nuevos diálogos; sigue la barra de Teams.

**Notas generales del segmento**
- Libro: **BD PQRS BOGOTA E ESCUCHA MAYO 2026**
- Hoja activa repetida: **INFORME WEB ABRIL**
- Se observa trabajo en pivotes, filtros y validación de tiempos/estados.
- La barra de Teams (**“Dejar de compartir”**) está presente en casi todos los frames.
- El contenido del audio coincide con: filtro de **Estado petición final**, selección de múltiples estados, y revisión de tiempos por tipología resaltando los que exceden el límite.

Si quieres, te lo convierto ahora en **tabla frame-por-frame** con una fila por imagen.

[Batch 6 - gpt-5.4-mini]
Veo el mismo libro y dos estados principales repetidos; agrupo los frames casi idénticos para no inventar diferencias.

### Estado 1 — `INFORME WEB ABREL`
**Frames 00501–00543**
1. **Workbook / sheet visible**
   - Libro: **`BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`**
   - Hoja activa: **`INFORME WEB ABREL`**
   - Otras pestañas visibles: `Tab 10 indicadores_Ajustado`, `Calificaciones Totales`, `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `SEGUIMIENTO DIAS`.

2. **Selección / modificación**
   - Se ve una **selección en la tabla dinámica inferior izquierda**, sobre el bloque de totales de **Tabla No. 10. Distribución PQRS por Localidad y Nivel Central**.
   - Después la selección se mueve sobre la zona derecha/lateral de la **Tabla No. 11**.
   - Hay indicios de **actualización de tabla dinámica** y de navegación por celdas; no se ve un rango exacto legible en todos los frames.

3. **Acción**
   - El usuario está **ajustando/validando la tabla dinámica**, moviéndose por los campos y totales.
   - Audio contextual: está **cambiando “nivel central”**, limpiando ceros/vacíos y preparando la validación por tiempos de gestión.

4. **Datos visibles**
   - En el resumen izquierdo se distinguen:
     - **`Cuenta de Número petición: 3623`**
     - **`Suma de Días gestión: 8007`**
   - En la Tabla No. 11 se ve el encabezado:
     - **`Mes`**
     - **`Peticiones periodo actual`**
     - **`PQRS Duplicadas`**
     - **`Suma de días gestión`**
     - **`Promedio de días`**
   - Se alcanzan a ver meses: **Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre**.
   - También aparece el total general al pie, pero en varios frames está parcialmente tapado por el overlay de Teams.

5. **Menús / ventanas**
   - Overlay de Teams: **`teams.microsoft.com está compartiendo tu pantalla`**
   - Botones: **`Dejar de compartir`**, **`Ocultar`**
   - En algunos frames se ve el puntero en espera / actualización de Excel.

---

### Estado 2 — panel de campos de tabla dinámica
**Frames 00544–00578**
1. **Workbook / sheet visible**
   - Mismo libro: **`BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`**
   - Sigue la hoja **`INFORME WEB ABREL`**

2. **Selección / modificación**
   - La selección se ubica en celdas de la tabla de meses, alrededor de **`G984` / `G989`** según el cuadro de nombre visible.
   - Se ve el rango activo dentro de la zona de la **Tabla No. 11**.

3. **Acción**
   - Se está **cambiando el origen de datos de la tabla dinámica**.
   - Se ve la intención de **actualizar/reconstruir la pivot** con el rango correcto.
   - Audio contextual: seleccionar todo hasta **USME**, reemplazar ceros por vacíos, y luego refrescar.

4. **Datos visibles**
   - Continúan visibles los meses y columnas de gestión.
   - El resumen izquierdo sigue mostrando:
     - **`Cuenta de Número petición`**
     - **`Suma de Días gestión`**
   - En algunos frames, el año/periodo y filtros aparecen como **`PERIODO ACTUAL`** y **`LOCAIDADES Y NIVEL CENTRAL`**.

5. **Menús / ventanas**
   - A la derecha aparece el panel **`Campos de tabla dinámica`**.
   - Campos visibles con checks:
     - **`Número petición`**
     - **`Duplicado`**
     - **`Sector`**
     - **`Tipo de entidad`**
     - **`Entidad`**
     - **`Tipo de dependencia`**
     - **`Dependencia`**
     - **`Dependencia hija`**
     - **`Tema`**
   - También se abre el diálogo **`Cambiar origen de datos de tabla dinámica`**.
   - Se alcanza a leer que la tabla/origen apunta a **`Reporte PQRS Mayo2026!...`**.

---

### Estado 3 — regreso al dashboard `Reporte PQRS Mayo2026`
**Frames 00580–00600**
1. **Workbook / sheet visible**
   - Mismo libro.
   - Hoja activa cambia a **`Reporte PQRS Mayo2026`**.

2. **Selección / modificación**
   - No hay una celda única estable; se ve el dashboard y luego scroll hacia las tablas inferiores.
   - Más abajo vuelve a aparecer la tabla de localidad/nivel central.

3. **Acción**
   - Se visualiza el **panel resumen** y luego el usuario baja a revisar datos de la pivot.
   - Audio contextual: validación de **tiempos de gestión** y resaltado de los que superan el límite legal.

4. **Datos visibles**
   - Gráficas visibles:
     - **`Gráfica No. 1 Total Peticiones del Mes`**
     - **`Gráfica No. 2 Distribución PQRS por Sexo`**
   - Filtros/tabla resumen a la izquierda:
     - **`Periodo: PERIODO ACTUAL`**
     - **`Tipo de ingreso`**
     - **`Total general: 2685`** (visible en la primera tabla)
   - Más abajo se ve:
     - **`Tabla No. 10. Distribución PQRS por Localidad y Nivel Central`**
     - **`Tabla No. 11 Localidades y Nivel Central`**
   - En la tabla de meses se distinguen valores en filas de enero–mayo, pero varios números quedan borrosos o tapados por el overlay de Teams.

5. **Menús / ventanas**
   - Sigue visible el overlay de Teams.
   - En algunos frames aparece el cursor de espera de Excel.
   - La barra inferior muestra la hoja activa **`Reporte PQRS Mayo2026`**.

---

### Cambios de pantalla detectados
- **Sí**: del dashboard `INFORME WEB ABREL` con Tabla 10/11 y panel de campos, luego al diálogo de **origen de tabla dinámica**, y finalmente al dashboard **`Reporte PQRS Mayo2026`** con gráficas y tabla resumen.
- El patrón general es: **ajuste de pivot → cambio de origen → refresco/validación → revisión del reporte final**.

[Batch 7 - gpt-5.4-mini]
Verificado. Resumo por estado visible del Excel:

| Frames | Libro / hoja | Selección / rango | Acción | Datos visibles | Ventanas / menús |
|---|---|---|---|---|---|
| 00601–00611 | **BD PQRS BOGOTA E ESCUCHA MAYO 2026** / **INFORME WEB ABRIL** | Celdas de pivots y gráfico inferior (sin rango exacto legible) | Revisión de reporte y desplazamiento vertical | Tabla **“Tabla No. 11 Localidades y Nivel Central”**; gráfico **“Participación por Localidad”**. Se leen barras como **San Cristóbal 163**, **Usme 141**, **Bosa 129**, **Usaquén 128**, **Kennedy 123**, **Engativá 119**. | Ribbon normal de Excel; banner de Teams “Dejar de compartir”. |
| 00612–00614 | Misma hoja | Pivot activo; panel lateral abierto | Se abre / usa **Campos de tabla dinámica** | Lista de campos: **Número petición, Duplicado, Sector, Tipo de entidad, Entidad, Tipo de dependencia, Dependencia, Dependencia hija, Tema**. | Pestaña **Analizar tabla dinámica**; panel **Campos de tabla dinámica**. |
| 00615–00616 | Misma hoja | Origen de la tabla dinámica | **Cambiar origen de datos de tabla dinámica** | Se ve el cuadro de diálogo para cambiar el rango de origen. | Modal **Cambiar origen de datos de tabla dinámica**. |
| 00617–00622 | **REPORTE PQRS Mayo2026** | Celda dentro del pivot / lista de localidades | Cambio a la hoja de datos y apertura de **Buscar y reemplazar** | Tabla base con columnas de PQRS; se ve el filtro/pivot y el cuadro de búsqueda. | **Buscar y reemplazar** abierto. |
| 00623–00639 | Misma hoja | Campo de búsqueda del reemplazo | **Reemplazar todos** | Se escribe `ALCALDIA LOCAL DE ...` y Excel confirma: **“Ya está. Hemos hecho 20 reemplazos.”** | Modal de reemplazo + popup de confirmación de Excel. |
| 00640–00643 | Misma hoja | Pivot de localidades / gráfico a la derecha | Resultado del reemplazo y refresco visual | La tabla de localidades se reordena visualmente; el gráfico de barras sigue a la derecha. | Cierre del popup; tabla dinámica visible. |
| 00644–00649 | Misma hoja | Selección en columna del pivot (menú contextual sobre **Columna E**) | **Ordenar** | Diálogo: **Columna E**, **valores de celda**, **De menor a mayor**. | Cuadro **Ordenar** abierto; luego se acepta y la tabla se reordena. |
| 00650–00655 | Parte inferior del informe | Pivot inferior / área de tabla | Desplazamiento hacia la sección baja del reporte | Se ve la tabla **“Tabla No. 12 PARTICIPACIÓN POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO”**. | Continúa el banner de Teams; sin modal. |
| 00656–00660 | Misma sección | Celda **C1051** (visible en el cuadro de nombre) | Selección de valor / porcentaje | En la barra de fórmulas aparece un valor tipo porcentaje/decimal: **0,568128900065195** (legible parcialmente). | Panel de campos de tabla dinámica a la derecha. |
| 00661–00667 | Misma sección | Bloque completo de la tabla 12 | Revisión de la tabla ya poblada | Encabezados visibles: **ALCALDÍA LOCAL**, **PETICIONES RECIBIDAS POR LOCALIDAD DE LOS HECHOS**, **PORCENTAJE DE PARTICIPACIÓN**, **CERT. RESIDENCIA**, **PROPIEDAD HORIZONTAL**, **ORIENTACIÓN**, **ENCUESTAS**, **DOC EXT.**. Total visible: **80,731** y **100.0%**. | Hoja con tabla dinámica y panel derecho abierto. |
| 00668–00670 | Misma hoja | Zona inferior izquierda | Desplazamiento / validación de totales | Continúa la tabla de participación por localidad. | Sin cambio de ventana. |
| 00671–00700 | Parte baja del informe / nueva sección | Pivots de **Punto atención** / **SUPERCADE** | Revisión de la sección de **estrato / supercades** | Se ve **“CAPITULO 11. PARTICIPACIÓN POR ESTRATO”** y pivots con filas como **SUPERCADE CAD**, **SUPERCADE AME**, **SUPERCADE BOSA**, etc. | En 00691–00693 reaparece **Cambiar origen de datos de tabla dinámica** sobre la hoja de datos crudos. |

### Lectura funcional del segmento
- Están **limpiando y reordenando** la base del reporte PQRS.
- Primero ajustan la **fuente del pivot**.
- Luego hacen **reemplazos masivos** (20 reemplazos).
- Después **ordenan** el ranking.
- Finalmente validan la sección de **participación por localidad** y la de **supercades/estrato**.

Si quieres, te lo convierto ahora en una **tabla frame-by-frame estricta** (una fila por cada JPG).

[Batch 8 - gpt-5.4-mini]
I grouped near-identical frames. Here’s the exact readout by state:

### 1) Frames 00701–00711
- **Workbook**: `BD PQRS BOGOTA Y ESCUCHA MAYO 2026 - Excel`
- **Sheet**: `Reporte PQRS Mayo2026`
- **Selection / action**: `Cambiar origen de datos de tabla dinámica` dialog open; source range field active. Later, a **pivot filter dropdown** for **“Punto atención”** is open.
- **Visible data**: filter options include `SUPERCADES CALLE 13`, `SUPERCADES CAD`, `SUPERCADES ENGATIVA`, plus locality-like items such as `ALCALDÍA LOCAL DE BOSA`, `KENNEDY`, etc.
- **Windows open**: Excel + Teams sharing banner (`teams.microsoft.com está compartiendo tu pantalla`, button `Dejar de compartir`).

### 2) Frames 00712–00716
- **Workbook**: same
- **Sheet**: same report sheet
- **Selection / action**: dialog closed; user is clicking within the pivot/report area. A pivot tooltip is visible.
- **Visible value**: tooltip shows **`Valor: 162`** for **`(en blanco) - SUPERCADES CAD`** in **`Cuenta de Número petición`**.
- **Windows open**: Excel only, Teams banner still present.

### 3) Frames 00717–00735
- **Workbook / sheet**: same workbook, same reporting area
- **Selection / action**: focus moves across blank cells and report cells; no major UI change.
- **Visible state**: same pivot/report layout, with the active cell in the lower/central area and the sheet still on the PQRS report.

### 4) Frames 00736–00743
- **Workbook**: same
- **Sheet**: `INFORME WEB ABRIL`
- **Selection / action**: user is selecting the big locality table and its source range.
- **Visible data**:
  - Title: **`Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`**
  - Localities visible: `USAQUEN`, `CHAPINERO`, `SANTA FE`, `SAN CRISTOBAL`, `USME`, `TUNJUELITO`, `BOSA`, `KENNEDY`, `FONTIBON`, `ENGATIVA`, `SUBA`, `BARRIOS UNIDOS`, `TEUSAQUILLO`, `LOS MARTIRES`, `ANTONIO NARIÑO`, `PUENTE ARANDA`, `LA CANDELARIA`, `RAFAEL URIBE URIBE`, `CIUDAD BOLIVAR`, `SUMAPAZ`, `NIVEL CENTRAL`.
  - Left pivot total shows **`10,599`** and **`100.00%`**.
- **Windows open**: Excel + Teams banner.

### 5) Frames 00744–00749
- **Workbook / sheet**: `INFORME WEB ABRIL`
- **Selection / action**: large grey selection block over the right-side table; looks like the user is expanding/copying/filling the matrix.
- **Visible state**: same locality table; no dialog.

### 6) Frames 00750–00773
- **Workbook / sheet**: `INFORME WEB ABRIL`
- **Action**: scrolling down through the report.
- **Visible sections**:
  - **`CAPITULO 11. PARTICIPACION POR ESTRATO`**
    - Pivot table with **`Total general 824`**
    - Pie chart titled **`PETICIONES POR ESTRATO`**
  - **`CAPITULO 12. CALIDAD DEL REQUERENTE`**
    - Pivot/table plus pie chart titled **`Peticiones por Calidad del Requirente`**
    - **`Total general 2718`** visible in the table section
    - Categories visible include `Establecimiento comercial`, `Jurídica`, `Natural`, and `(en blanco)`
- **Windows open**: Excel + Teams banner.

### 7) Frames 00777–00780
- **Workbook / sheet**: `INFORME WEB ABRIL`
- **Action**: **PivotTable Fields** pane open on the right.
- **Visible fields**: `Número petición`, `Duplicados`, `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`.
- **Layout areas visible**: `Filtros`, `Columnas`, `Filas`, `Valores`.
- **Current pivot setup**: row field shows **`Estrato de los hechos`**, values show **`Total`**.
- **Charts visible**: `PETICIONES POR ESTRATO` pie chart.

### 8) Frames 00781–00800
- **Workbook**: same workbook
- **Sheet transition**: back to `Reporte PQRS Mayo2026` / underlying source data
- **Action**: `Cambiar origen de datos de tabla dinámica` dialog opens again; then the raw data grid is visible.
- **Visible source fields**: `Duplicados`, `Sector`, `Tipo de Entidad`, `Dependencia`, `Dependencia hija`, `Tema`, `Subtema`, `Funcionario`, `Estado`, `Punto ate...`
- **Visible row data**: examples include `GOBIERNO ENTIDAD SECRETARIA DISTRITAL DE GOBIERNO`, `OFICINA DE ATENCION A LA CIUDADANIA`, `SANDRA V`, status `Activo`, and values like `WEB`.
- **Meaning**: they’re changing/confirming the pivot source range so the report refreshes with the updated data.

### Overall transition
- The segment moves from **editing pivot source/filtering “Punto atención”** → to **report validation on `INFORME WEB ABRIL`** → to **scrolling charts/tables by estrato and requerente quality** → back to **source-data / pivot source range**.

If you want, I can turn this into a **frame-by-frame table with timestamps**.

[Batch 9 - gpt-5.4-mini]
Here’s the frame analysis, by visible screen state:

### 1) Frames 00801–00804
- **Workbook/sheet:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026.xlsx` — sheet appears to be `INFORME WEB ABRIL`
- **Selection:** a single cell inside the pivot table at left, under `CAPITULO 1.2 CALIDAD DEL REQUIRENTE`; exact address is unreadable
- **Action:** inspecting a pivot table / changing focus inside the pivot
- **Visible data:**  
  - `Tipo de Petición` rows like `Establecimiento comercial`, `Jurídica`, `Natural`, `Sin banco?` / similar, with a `Total general` row  
  - another small pivot in the center titled `CAPITULO 1.2 CALIDAD DEL REQUIR...`
  - a pie chart on the right titled `Peticiones por Calidad del Requirente`
- **Open windows/panels:** Excel + pivot field list on the right; Teams sharing banner on top-right

### 2) Frames 00805–00813
- **Workbook/sheet:** same workbook/sheet
- **Selection:** on cells inside the middle pivot table and then the chart area; later focus shifts to the right-side pivot field list
- **Action:** moving through pivot/chart elements, likely preparing or checking chart-linked values
- **Visible data:** pie chart labels include `Natural` (~84.3%) and `Jurídica` (~7.7%); other slice labels are visible but small
- **Open windows/panels:** right pivot field list with checkboxes (`Número petición`, `Duplicados`, `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`, `Tema`)
- **Transition:** 00805 switches from the pivot value cell to the chart view

### 3) Frames 00814–00830
- **Workbook/sheet:** same workbook/sheet
- **Selection:** lower-left area around `CAPITULO 3.1 ATENCIONES POR GRUPO POBLACIONAL`; selection box expands around the pivot table region
- **Action:** selecting or navigating the lower pivot table / chart area
- **Visible data:**  
  - lower table heading `CAPITULO 3.1 ATENCIONES POR GRUPO POBLACIONAL (Tomado del registro de atenciones ciudadanas)`
  - rows like `Servidor` / `Cuenta de Atención preferencial`
- **Open windows/panels:** pivot field list changes to show `Atención preferencial` and `Canal de atención` fields
- **Transition:** cursor moves across the lower table; no obvious value edit, just inspection/navigation

### 4) Frames 00831–00844
- **Screen:** Excel backstage/home screen
- **Workbook context:** no sheet visible; Excel recent files list
- **Action:** likely closing or switching workbooks
- **Visible data:** recent documents like:
  - `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026`
  - `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`
  - `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010`
  - `REPORTE ENCUESTAS ABRIL 2026 FORMATO SAC-F010`
- **Open windows/panels:** Excel start screen only

### 5) Frames 00845–00846
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx` — sheet `RESUMEN CIFRAS`
- **Selection:** no editable cell; modal dialog is blocking the sheet
- **Action:** opening a workbook with external links warning; user is deciding whether to update links
- **Visible dialog:** Excel warning about external links:
  - “Este libro contiene vínculos a uno o más fuentes externas…”
  - buttons: `Actualizar`, `No actualizar`, `Ayuda`
- **Visible data:** top summary table with columns:
  - `ALCALDÍA LOCAL`
  - `PQRS GESTIONADAS N.1`
  - `PQRS PENDIENTES N.2`
  - `DOC. EXT. N.3`
  - `ORIENTACIONES No.4`
  - `CERT. PROPIEDAD No.5`
  - `CERT. RESIDENCIA No.6`
  - `ENCUESTAS DEL PERIODO`
  - `ENCUESTAS CON RESPUESTA COMPLETA`
- **Transition:** user hovers/clicks around `No actualizar`

### 6) Frames 00847–00853
- **Workbook/sheet:** same workbook; sheet tab `CERT RESIDENCIA PROD-MAYO` becomes active
- **Selection:** table cells in the locality summary
- **Action:** reviewing certificate counts by locality
- **Visible data:** locality rows and counts, including:
  - `ANTONIO NARIÑO` 9
  - `BARRIOS UNIDOS` 13
  - `BOSA` 166
  - `CANDELARIA` 113
  - `CHAPINERO` 18
  - `CIUDAD BOLIVAR` 37
  - `ENGATIVÁ` 41
  - `FONTIBON` 55
  - `KENNEDY` 69
  - `MARTIRES` 7
  - `PUENTE ARANDA` 21
  - `RAFAEL URIBE` 49
  - `SAN CRISTOBAL` 52
- **Open windows/panels:** Excel sheet only; link-warning dialog disappears after 00846

### 7) Frames 00854–00858
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx` — sheet `CERT.P.HORIZONTAL MAYO`
- **Selection:** table on left, then chart area on right
- **Action:** viewing productivity of horizontal property certificates by locality
- **Visible data:**  
  - title: `PRODUCTIVIDAD DE CERTIFICADOS DE PROPIEDAD HORIZONTAL / CERTIFICADOS GENERADOS VIGENCIA MAYO 2026`
  - totals visible: `Inscripción realizada = 21`, `Actualización realizada = 788`, `Extinción realizada = 0`, `Certificados Generados = 809`, `% = 100%`
  - bar chart ranking localities, with readable values:
    - `USAQUÉN` 36.218%
    - `SUBA` 13.597%
    - `TEUSAQUILLO` 12.979%
    - `FONTIBÓN` 12.237%
    - `KENNEDY` 6.180%
    - `CHAPINERO` 4.697%
    - `BOSA` 2.349%
    - `ENGATIVÁ` 2.101%
    - `PUENTE ARANDA` 1.854%
    - `TUNJUELITO` 1.607%
    - `SANTA FE` 1.236%
    - `SAN CRISTÓBAL` 1.236%
    - `CANDELARIA` 1.112%
    - `BARRIOS UNIDOS` 0.865%
    - `USME` 0.742%
    - `ANTONIO NARIÑO` 0.494%
    - `CIUDAD BOLIVAR` 0.371%
    - `LOS MÁRTIRES` 0.124%
    - `RAFAEL URIBE` 0.000%
- **Open windows/panels:** standard Excel view, no modal dialog

### 8) Frames 00859–00890
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx` — sheet `REGISTRO ATENCIONES`
- **Selection:** cells in the large ranked table on the left, then the lower-right pivot area
- **Action:** inspecting/working through multiple pivot tables; probably preparing a report on attendance/attention types
- **Visible data:**  
  - left table: ranked names with counts and percentages (top row readable: `Ledy Jhoana Mayux Acuna` 269, `6.2%`; many more names follow)
  - middle/right top table: category list with total `4328`
  - right top categories readable:
    - `Proyectos locales`
    - `Propiedad horizontal`
    - `Subsidios`
    - `Documentos extraviados`
    - `Ventas ambulantes - RIV`
    - `Proyectos distritales`
    - `Oficina infraestructura`
    - `Sisbén`
    - `Certificado adulto mayor`
    - `Vivienda unifamiliar`
    - `Malla vial`
  - lower-right pivot `Registros por Atención Preferencial` with total `3366`
    - rows include `Ninguna`, `Persona Mayor`, `Persona con discapacidad física`, `Persona con discapacidad intelectual-cognitiva`, `Comunidad Afro`, `Víctimas de conflicto armado`, `Persona con discapacidad múltiple`, `Persona con discapacidad visual`, `Persona con discapacidad mental-psicosocial`, `Comunidad indígena`, `Campesino campesina`, `Persona con discapacidad auditiva`
- **Open windows/panels:** pivot field list on the right; `Canal de atención` is checked, `Atención preferencial` is used as the row field, `Registros` as the value field
- **Transition:** repeated cell focus changes inside the lower pivot, but no actual data edit is visible

### 9) Frames 00891–00896
- **Screen:** Excel home/start screen again
- **Action:** switching/closing workbook and returning to recent files
- **Visible data:** same recent documents list as before
- **Open windows/panels:** Excel backstage only

### 10) Frames 00897–00900
- **Workbook/sheet:** `05. SAC_atencion - Mayo 2026.xlsx` — sheet `tablas`
- **Selection:** cells inside the pivot tables; 00900 shows the mouse near the window close button, not a data cell
- **Action:** reviewing multiple summary pivots; final frame suggests the workbook may be about to be closed
- **Visible data:** four main pivots:
  - `Registros por servidor`
  - `Registros por punto de atención`
  - `Registros por Asunto`
  - `Registros por Atención Preferencial`
- **Open windows/panels:** right-side pivot field list with `Canal de atención` checked; Teams sharing banner still visible
- **Transition:** 00900 is a UI-hover moment over the red close button

If you want, I can turn this into a **timestamped report** with one line per frame for direct annotation.

[Batch 10 - gpt-5.4-mini]
Grouped by identical screen states:

- **00901** — **Workbook:** `BASE DATOS PPT LOCALIDADES MAYO 2026` / **sheet:** `REGISTRO ATENCIONES`. **Selection:** active cell around `I25`. **Action:** reviewing pivot tables. **Visible data:** locality totals with a `Total general` of **4328**; attention-preference pivot showing **Ninguna 2582**, **Persona Mayor 360**, **Persona con discapacidad física 66**, **intelectual-cognitiva 24**, **Comunidad Afro 16**, **Víctima del conflicto armado 13**, **múltiple 12**, **visual 11**, **mental-psicosocial 11**, **indígena 3**, **campesino 3**, **auditiva 1**; right-side PivotTable Fields pane open. **Window:** Excel + Teams sharing bar.

- **00902–00907** — **Workbook:** same file, but Excel **Backstage/Home** view. **Selection:** none (no worksheet visible). **Action:** browsing **Recientes** / switching files. **Visible data:** recent workbooks listed, including `BASE DATOS PPT LOCALIDADES MAYO 2026`, `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026`, `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`, `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010`, `MAYO2026_PRODUCTIVIDAD_PH`, `MAYO2026_PRODUCTIVIDAD_CR`, `Resumen SIDE Mayo 2026`. **Window:** Excel start/backstage navigation on the left (`Inicio`, `Nuevo`, `Abrir`, etc.).

- **00908–00909** — **Workbook:** `Resumen SIDE Mayo 2026` / **sheet:** `REGISTRADO SIDE`. **Selection:** active cell around `Y14` (visible in name box). **Action:** reviewing summary table. **Visible data:** pivot/table with `Etiquetas de fila` and `Suma de TOTAL`; locality rows include **Candelaria 96**, **Engativá 98**, **Fontibón 48**, **Kennedy 18**, **Mártires 70**, **Nivel central 693**, **Santa Fe 15**, **Suba 19**, **Teusaquillo 666**; `Total general` **1723**. **Window:** Excel + Teams share bar.

- **00910–00916** — **Workbook:** `Resumen SIDE Mayo 2026` / **sheet:** `ENTREGADO SIDE`. **Selection:** moves within the summary block (`G1`, then total rows like `B14/B15` area). **Action:** checking formulas/totals and the detailed registry list. **Visible data:**  
  - Top-left section `ENTREGADO SIDE Mayo 2026`: **Cédula de ciudadanía 20**, **Licencia de conducción 3**, `TOTAL 23`.  
  - Lower section `DEVUELTO SIDE Mayo 2026`: **Cédula de ciudadanía 1269**, other doc types at 0, `TOTAL 1269`.  
  - Right table columns: `MES`, `FECHA`, `TIPO DOCUMENTO`, `N° DOCUMENTO`, with May 2026 rows and citizen names/IDs.  
  - One frame shows formula bar `=SUMA(B3:B13)` for the total row.  
  **Window:** Excel only, Teams share bar still present.

- **00917** — **Workbook:** back to `BASE DATOS PPT LOCALIDADES MAYO 2026` / **sheet:** `REGISTRO ATENCIONES`. **Selection:** still in pivot area. **Action:** reviewing the same locality-attention pivot and filter pane. **Visible data:** `Total general 4328` and the attention-preference table/pivots again. **Window:** Excel + PivotTable Fields pane + Teams share bar.

- **00918–00935** — **Workbook:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026` / **sheet:** `INFORME WEB ABRIL`. **Selection:** not clearly on an editable cell; mostly chart/report area. **Action:** scrolling through the report. **Visible data:**  
  - `CAPITULO 11. ATENCIONES POR GRUPO POBLACIONAL` with pivot `Atención preferencial | Registros`, `Total general` **3366**.  
  - `Documentos Extraviados Mayo` and a note like `Entregados a la Ciudad...` in the upper-left section.  
  - Repeated report content as the scroll settles.  
  **Window:** Excel report view, no dialogs.

- **00936–00941** — Same workbook/sheet, further down the report. **Action:** viewing charts/tables for **quality of requester** and **estrato**. **Visible data:**  
  - `CAPITULO 12. CALIDAD DEL REQUIERENTE` with a pie chart `Peticiones por Calidad del Requirente`.  
  - `CAPITULO 11. PARTICIPACION POR ESTRATO` with a pie chart `PETICIONES POR ESTRATO`.  
  - Tables show categories like `Establecimiento comercial`, `Jurídica`, `Natural`, and a totals row at **100%**.  
  **Window:** Excel report only.

- **00942–00955** — Same workbook/sheet, scrolled to the locality table. **Action:** reviewing the big locality participation table, not editing. **Visible data:**  
  - Header: `Tabla No. 12. PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`.  
  - Columns visible: `ALCALDIA LOCAL`, `PETICIONES RECIBIDAS POR LOCALIDAD DE LOS HECHOS`, `PORCENTAJE DE`, `PARTICIPACION`, `CÓD. RESIDENCIA`, `PROPIEDAD HORIZONTAL`, `...`, `ENCUESTAS`.  
  - Left summary block shows locality counts and `Total general` around **9039** / **100.00%**.  
  - Bottom red total row in the large table shows **10,539** and **100%**.  
  **Window:** Excel report view with Teams share bar.

- **00956–01000** — **Screen change:** Excel disappears; the screen becomes a **black Teams/meeting participant tile**. **Visible content:** centered circular avatar of **Yesenia Patino Figueroa** with name label. **Selection/ranges:** none. **Action:** no spreadsheet action visible; this is a transition away from Excel.

If you want, I can also turn this into a strict **frame-by-frame table with one row per frame number**.

[Batch 11 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped by visible state because most frames are identical.

### Frames 01001–01093
1. **Visible workbook/sheet**: None visible.  
2. **Selected cells/ranges**: None visible.  
3. **Action**: No spreadsheet interaction visible; only a black/idle screen with a centered profile avatar.  
4. **Values/data**: Only the profile name **“Yesenia Patino Figueroa”** is readable.  
5. **Menus/dialogs/windows**: None of Excel is visible.

### Transition at frame 01094
- Screen changes from idle/avatar-only to a **browser-based Microsoft Teams meeting** with a shared screen.

### Frames 01094–01100
1. **Visible workbook/sheet**: Excel is **not directly visible**. Only bottom thumbnails/previews of several Excel files appear, including:
   - **“REPORTE ENCUESTAS MAY…”**
   - **“BD PQRS BOGOTA ESC…”**
   - **“INFORME PQRS SECRETAR…”**
   - **“BASE DATOS PPT LOCALD…”**
   - **“Resumen SIDE Mayo 2026…”**
   Sheet/tab names are **not readable**.
2. **Selected cells/ranges**: No cell selection can be read from these frames.
3. **Action**: The shared screen appears to be in a **Teams meeting**, waiting for participants; no active Excel edit is visible.
4. **Values/data**:
   - Main on-screen text: **“Esperando a que se unan otros usuarios…”**
   - A Teams notice mentions recording/transcription started.
   - Right-side participant tile shows **Yesenia Patino Figueroa**.
5. **Menus/dialogs/windows**:
   - **Microsoft Teams in Chrome**
   - Top meeting controls visible
   - Browser tabs visible
   - Bottom Windows taskbar visible

### Important note
The audio transcript suggests Excel work is happening, but in these specific frames the workbook content is **not legible enough** to identify:
- exact workbook name/sheet,
- selected ranges,
- formulas,
- or cell values.

If you want, I can continue with a **more granular OCR-style pass** on the next segment where the Excel grid is actually visible.

[Batch 12 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen is unchanged.

- **1101–1104** — **Workbook:** `Resumen SIDE Mayo 2026 - Excel`; **sheet:** `ENTREGADO SIDE`. **Action:** viewing a summary sheet, active cell is **B29** with formula bar showing `=SUMA(B18:B28)`. **Data:** left summary shows `DEVUELTO SIDE Mayo 2026` with `Cédula de ciudadanía = 1269`, all other doc types `0`, `TOTAL = 1269`; bottom table shows `MAYO | 29/05/2026 | Cédula de Ciudadanía | 1269 | Registraduría Nacional del Estado Civil | 20264600308711`. **UI:** no dialog open.

- **1105** — **Workbook:** `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026 - Excel`; **sheet:** `Hoja1`. **Action:** switched to a PQRS raw-data sheet. **Data:** table headed `Gestión de Peticiones`, with columns like `Número`, `Sector`, `Entidad`, `Tema`, `Estado`, etc.; rows show government entities and statuses such as `Pendiente`, `En trámite`, `Solucionado`. **UI:** plain grid, no dialog.

- **1106** — **Transition frame** while switching between workbooks/sheets; same PQRS table is fading out.

- **1107–1108** — **Workbook:** `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC- F010 - Excel`; **sheet:** `Calificaciones Totales`. **Action:** viewing survey summary/score dashboard. **Data:** tables `Tabla 6` and `Tabla 7` visible; headline scores **4,9** and **4,5**; chart title `Lugar donde se recibe el servicio`. **UI:** on 1108 a hover tooltip appears near the taskbar preview: `ANÁLISIS INFORME PQRS...`.

- **1109–1115** — **Workbook:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`. **Sheet:** locality-ranking / indicators sheet (name box shows **H1042**). **Action:** viewing the locality participation table. **Data:** title `Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`; visible filters `Tipo de ingreso [Todas]` and `Periodo ACTUAL`; right table includes localities like `01 - USAQUEN`, `02 - CHAPINERO`, `03 - SANTA FE`, etc.; bottom total row shows **10.539** and **100%**. **UI:** hover/transition over sheet tabs, no modal.

- **1116–1120** — **Workbook:** same `BD PQRS...`; **sheet:** `ENTREGADO SIDE` (name box **V3**). **Action:** reviewing the April delivery sheet. **Data:** left table `DEVUELTO SIDE Abril 2026` with totals: `Cédula de ciudadanía 764`, `Cédula de extranjería 13`, `Libreta Militar 12`, `Licencia de conducción 197`, `Licencia de Tránsito 80`, `Pasaporte 22`, `Permiso Protección Temporal 114`, `Tarjeta de conducta servicio militar 59`, `Tarjeta de identidad 42`, `TOTAL 1303`; right table lists April records with columns `MES`, `FECHA`, `TIPO DOCUMENTO`, `CANTIDAD`, `ENTIDAD GENERADORA`, `ACUSE`, `CASO`, `PLANILLA`. **UI:** no dialog yet.

- **1121** — **Action:** right-click on the sheet tab area. **UI:** context menu opens with options like `Insertar...`, `Eliminar`, `Cambiar nombre`, `Mover o copiar...`, `Ver código`, `Proteger hoja...`, `Color de pestaña`, `Ocultar`, `Mostrar...`.

- **1122–1133** — **Action:** opening `Mover o copiar` dialog. **UI:** sheet-copy/move modal visible, with workbook/sheet destination list expanded; options include sheets such as `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, etc. This is sheet reorganization, not cell editing.

- **1142** — **Action/UI:** another right-click on a sheet tab; context menu open again, indicating more sheet management.

- **1143–1144** — **UI:** Excel confirmation dialog: `Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?` Buttons `Eliminar` / `Cancelar`. Cursor is on `Eliminar` in 1144.

- **1145** — **Workbook:** same PQRS workbook, but now on a summary tab with horizontal scroll far right. **Sheet:** `REGISTRADO SIDE`-type summary view. **Data:** left total block shows **2579**; central pivot-like table `Etiquetas de fila / Suma de TOTAL` lists `CANDELARIA 96`, `ENGATIVA 98`, `FONTIBON 48`, `KENNEDY 18`, `MARTIRES 70`, `NIVEL CENTRAL 693`, `SANTA FE 15`, `SUBA 19`, `TEUSAQUILLO 666`, `Total general 1723`. **UI:** no modal.

- **1146–1152** — **Action:** back to `ENTREGADO SIDE` / same workbook, then blank cell movement and tab switching. **UI:** no dialog; cursor just moves across the sheet area.

- **1153** — **Workbook:** same, title bar shows `JESUS VALENCIA` (visible in the window title area). **Sheet:** `REGISTRADO SIDE Abrl 2026`. **Action:** viewing registration summary. **Data:** left block `Tipo de Documento / Total`; right table columns `Año`, `Mes`, `Localidad`, `Origen`, `Radicado`, `Fecha radicado`; visible rows include `N/A / STOCK`, `NIVEL CENTRAL / TRANSPORTE MASIVO`, `CHAPINERO / UNIVERSIDAD PEDAGOGICA NACIONAL`, `TEUSAQUILLO / CENTRAL DE SEGURIDAD CONSULTAS INTERNACIONAL`; `Total general 591`. **Selected cell:** **Y14**.

- **1154** — **Action:** right-click on the tab again; context menu open.

- **1155–1156** — **UI:** delete confirmation dialog reappears (`Eliminar` / `Cancelar`), then cursor moves onto `Eliminar`.

- **1157** — **Sheet:** back on `ENTREGADO SIDE`. **Action:** summary totals visible again; no dialog.

- **1158–1160** — **Sheet:** `REGISTRADO SIDE` horizontal-scrolled summary. **Data:** same pivot block with `CANDELARIA 96`, `ENGATIVA 98`, `FONTIBON 48`, `KENNEDY 18`, `MARTIRES 70`, `NIVEL CENTRAL 693`, `SANTA FE 15`, `SUBA 19`, `TEUSAQUILLO 666`, `Total general 1723`. **UI:** no modal.

- **1161–1165** — **Action/UI:** `Mover o copiar` dialog opened again; destination list expanded. This appears to be another sheet duplication/move operation, with visible workbook/tab names including `REPORTE ENCUESTAS MAYO 2026...`, `BD PQRS BOGOTA TE ESCUCHA MAYO 2026...`, `BASE DATOS PPT LOCALIDADES...`, `Resumen SIDE Mayo 2026.xlsx`.  

- **1166–1170** — **Sheet:** returns to `ENTREGADO SIDE`. **Action:** just sheet navigation; no dialog.

- **1171** — **Workbook/sheet:** `Reporte PQRS Mayo2026`. **Action:** viewing a long table of locality/route records. **Data:** rows around `12884+` with many `false/true`, `Pendiente`, `Registrado`, `Por el ciudadano`, `Por el distrito`, etc. **UI:** no modal.

- **1172** — **Workbook/sheet:** `INFORME WEB ABRIL`. **Action:** jump to the formatted report sheet; top of the page shows `Tabla No. 12 PARTICIPACION POR LOCALIDAD...` and related report blocks.  

- **1173–1174** — **Sheet:** `INFORME WEB ABRIL`. **Action:** viewing the locality participation table; the same red/green table spans columns across the page. **UI:** cursor over chart areas; no dialog.

- **1175–1178** — **Action:** minor navigation/hover around the same report sheet; bottom shows tab strip with `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, `SEGUIMIENTO DÍAS`. **UI:** no modal.

- **1179–1182** — **Action:** still in `INFORME WEB ABRIL`, now near the section with `CAPITULO 11. PARTICIPACION POR ESTRATO`. **Data:** left table/pivot and right chart `PETICIONES POR ESTRATO` visible; another block below for `CAPITULO 12 CALIDAD DEL REQUIERENTE`. **UI:** no modal.

- **1183–1186** — **Sheet:** `INFORME WEB ABRIL`, scrolled lower. **Data:** `CAPITULO 12 CALIDAD DEL REQUIERENTE` shows categories `Establecimiento comercial`, `Jurídica`, `Natural`; pie chart `Peticiones por Calidad del Requirente` shows **Natural overwhelmingly dominant (~92%)**, **Jurídica ~7%**, **Establecimiento comercial <1%**. Below, `Documentos Extraviados Mayo` is visible, and then `CAPITULO 13 ATENCIONES POR GRUPO POBLACIONAL`. **UI:** no dialog.

- **1187–1190** — **Sheet:** same report, scrolled around `CAPITULO 11 PARTICIPACION POR ESTRATO`. **Data:** pivot table and pie chart `PETICIONES POR ESTRATO` visible; chart labels are partially legible, but the distribution clearly shows multiple strata with one dominant slice and smaller slices. **UI:** no modal.

- **1191–1194** — **Sheet:** same report, scroll position shifts slightly; `CAPITULO 12 CALIDAD DEL REQUIERENTE` is again visible alongside the left-side summary table. **UI:** no dialog.

- **1195–1200** — **Sheet:** `INFORME WEB ABRIL`, horizontally scrolled to `Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`. **Data:** rows for `01 - USAQUEN`, `02 - CHAPINERO`, `03 - SANTA FE`, `04 - SAN CRISTOBAL`, `05 - USME`, `06 - TUNJUELITO`, `07 - BOSA`, `08 - KENNEDY`, `09 - FONTIBON`, `10 - ENGATIVA`, `11 - SUBA`, `12 - BARRIOS UNIDOS`, `13 - TEUSAQUILLO`, `14 - LOS MARTIRES`, `15 - ANTONIO NARIÑO`, `16 - PUENTE ARANDA`, `17 - LA CANDELARIA`, `18 - RAFAEL URIBE URIBE`, `19 - CIUDAD BOLIVAR`, `20 - SUMAPAZ`. **Columns:** `ALCALDIA LOCAL`, `PETICIONES RECIBIDAS POR LOCALIDAD DE LOS HECHOS`, `PORCENTAJE DE PARTICIPACION`, `CC. RESIDENCIA`, `PROPIEDAD HORIZONTAL`, `ORIENTACION`, `ENCUESTAS`. **Footer:** `TOTAL GENERAL 10.539 / 100%`. **UI:** tooltips like `Área del gráfico [x]` and `Fila: 1030` appear while hovering.

If you want, I can turn this into a **clean narrative summary** of the whole segment instead of frame-by-frame detail.

---

## Segmento 12: Cuadros comparativos, verificación final y cierre

| Campo | Valor |
|---|---|
| **Duración** | 120:00 - 141:07 |
| **Descripción** | Comparativo periodo actual vs anterior, verificación de cifras totales, documentos extraviados entregados, cierre y grabación |
| **Frames analizados** | 1267 |
| **Batches** | 13 |
| **Proveedor** | gpt-5.4-mini |
| **Tiempo total** | 1976s |

### Análisis frame-by-frame

[Batch 1 - gpt-5.4-mini]
Below is a frame-by-frame analysis, grouped where the screen is effectively unchanged.

### Frames 1–3
- **Workbook:** `BD PORS BOGOTA E ESCUCHA MAYO 2026 - Excel`
- **Visible sheet/tab area:** several tabs visible (`REPORTE ENCUESTAS MAY...`, `BD PQRS BOGOTA TE ESC...`, `INFORME PQRS SECRETAR...`, `BASE DATOS PPT LOCALID...`, `Resumen SIDE Mayo 2026...`)
- **Selection:** name box shows `A1150` / active cell context changes but no meaningful edit visible
- **Action:** browsing workbook; no clear data entry
- **Data visible:** left pivot/table of localities and counts; center table titled `Tabla No. 12 ...`; bottom totals and sheet thumbnails
- **Windows:** normal Excel window; no dialog

### Frame 4
- **Workbook:** `BASE DATOS PPT LOCALID... - Excel`
- **Sheet:** `REGISTRO ATENCIONES` (pivot table view)
- **Selection:** a pivot cell in the left table area
- **Action:** viewing pivot table / field list
- **Data visible:** locality counts and a pivot summary; right pane `Campos de tabla dinámica`
- **Windows:** PivotTable Fields pane open on the right

### Frame 5
- **Workbook:** same
- **Sheet:** `REGISTRO SIDE`
- **Selection:** cell around `Y12`
- **Action:** viewing another pivot summary
- **Data visible:** month `may-26`, locality list, total `1723`
- **Windows:** PivotTable Fields pane still open

### Frame 6
- **Workbook:** same
- **Sheet:** `Reporte PQRS Mayo2026`
- **Selection:** raw data region (around row 12884)
- **Action:** inspecting source rows / status data
- **Data visible:** columns with status text like `Recibida`, `Registrada`, `PENDIENTE`
- **Windows:** no dialog; normal grid

### Frames 7–14
- **Workbook:** same
- **Sheet:** `RESUMEN CIFRAS`
- **Selection:** starts near `B3`, then moves across cells in the summary table (notably column `G`)
- **Action:** comparing/reading totals in the summary table
- **Data visible (key rows):**
  - `ANTONIO NARIÑO` → `9 | 29 | 0 | 61 | 4 | 45 | 28 | 28`
  - `BARRIOS UNIDOS` → `13 | 19 | 0 | 264 | 7 | 143 | 308 | 307`
  - `BOGOTA/BOSA/...` rows continue
  - `SUBA` → `70 | 75 | 19 | 180 | 110 | 902 | 182 | 182`
  - `SUMAPAZ` → `6 | 3 | 0 | 3 | 0 | 20 | 1 | 1`
  - `TEUSAQUILLO` → `22 | 10 | 666 | 251 | 105 | 235 | 83 | 83`
  - `TUNJUELITO` → `40 | 30 | 0 | 167 | 13 | 491 | 425 | 422`
  - `USAQUEN` → `46 | 59 | 0 | 316 | 293 | 310 | 160 | 159`
  - `USME` → `45 | 50 | 0 | 112 | 6 | 543 | 522 | 522`
  - `NIVEL CENTRAL` → `8484 | 497 | 693 | 843 | 0 | 0 | 529 | 529`
  - `SUPERCADES` → `0 | 0 | 0 | 406 | 0 | 0 | 139 | 139`
  - `EN BLANCO` → `0 | 0 | 0 | 0 | 0 | 0 | 1540 | 0`
  - `TOTAL GENERAL` → `9431 | 1168 | 1723 | 4328 | 809 | 6863 | 5465 | 3915`
- **Windows:** no dialog; just the worksheet

### Frames 15–23
- **Workbook:** same
- **Sheet:** `INFORME WEB ABREL`
- **Selection:** chart/data region on the right; later a narrow vertical pasted range
- **Action:** copying/pasting data for chart or comparison table; right-click context menu appears
- **Data visible:** table titled `Tabla No. 12: PARTICIPACIÓN POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`
- **Menus/dialogs:**
  - Frame 21: right-click context menu (`Cortar`, `Copiar`, paste options)
  - Frame 22: paste options/clipboard popup
- **Screen change:** from summary table to web report table with chart area

### Frames 24–32
- **Workbook:** same
- **Sheet:** back to `RESUMEN CIFRAS`
- **Selection:** cells in the summary area, mostly around column `G` / totals rows
- **Action:** checking copied values against totals
- **Data visible:** same locality table and totals
- **Windows:** normal sheet

### Frame 33
- **Window:** Windows Alt+Tab switcher
- **Action:** switching between open Excel files/windows
- **Visible thumbnails:** multiple Excel workbooks and Explorer windows
- **Windows:** app switch overlay

### Frames 34–38
- **Workbook:** same summary workbook
- **Sheet:** `RESUMEN CIFRAS`
- **Selection:** moves through the summary table and totals
- **Action:** verification of values before moving data
- **Data visible:** same `DIAPOSITIVA No. 3` table, totals row still visible

### Frames 39–45
- **Workbook:** same
- **Sheet:** `INFORME WEB ABREL`
- **Selection:** a narrow vertical list on the far right (grey selected range)
- **Action:** pasting/building the source column for the chart or report
- **Menus/dialogs:** paste popup / clipboard badge visible
- **Data visible:** right-side numeric series aligned to locality names

### Frames 46–52
- **Workbook:** same
- **Sheet:** `INFORME WEB ABREL`
- **Selection:** same right-side narrow numeric column
- **Action:** continuing paste/adjustment of the extracted series
- **Data visible:** values like `61, 264, 61, 45, 63, 38, 295...` in the right-side strip

### Frames 53–54
- **Workbook:** same
- **Sheet-tab area:** bottom tabs
- **Action:** right-click on a sheet tab / sheet management
- **Menu:** sheet tab context menu appears (insert/delete/rename/move/copy/tab color/hide/show)

### Frames 55–63
- **Workbook:** same
- **Sheet:** alternating between `RESUMEN CIFRAS` and `INFORME WEB ABREL`
- **Selection:** moving across table cells and the right-side data strip
- **Action:** cross-checking the summary table against the web report data
- **Data visible:** totals and locality rows remain unchanged

### Frames 64–75
- **Workbook:** same
- **Sheet:** `INFORME WEB ABREL`
- **Selection:** right-side vertical pasted list
- **Action:** paste operations continue
- **Menus/dialogs:** repeated paste options menu (`Pegar`, `Pegar valores`, other paste options)
- **Data visible:** the right-side list now shows more complete values for localities

### Frames 76–83
- **Workbook:** same
- **Sheet:** `INFORME WEB ABREL`
- **Selection:** same far-right numeric range, slightly shifted
- **Action:** finalizing that pasted column / chart source data
- **Data visible:** the numeric strip is fully populated

### Frames 84–95
- **Workbook:** same
- **Sheet:** `INFORME WEB ABREL`
- **Selection:** right-side strip and then sheet-tab area
- **Action:** sheet-level cleanup and tab management
- **Menus/dialogs:** frame 95 shows the sheet-tab context menu with:
  - `Insertar...`
  - `Eliminar`
  - `Cambiar nombre`
  - `Mover o copiar...`
  - `Ver código`
  - `Proteger hoja...`
  - `Color de pestaña`
  - `Ocultar`
  - `Mostrar...`
  - `Seleccionar todas las hojas`

### Frames 96–98
- **Workbook:** different file: `PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS ABRIL 2026`
- **Sheet tabs visible:** `CERT.P.HORIZONTAL ABRIL`, `CERT RESIDENCIA PROD-ABRIL`, `CR-TIPO TRAMITE`, `REGISTRO ATENCIONES`, `Tabla 10 indicadores_Ajustado`, `Calificaciones Totales`
- **Action:** navigating to a sheet-tab context menu, preparing to delete a sheet
- **Data visible:** left table of localities + right bar chart titled `PRODUCTIVIDAD CERTIFICADOS DE PH GENERADOS / ABRIL 2026`

### Frame 99
- **Workbook:** same productivity workbook
- **Action:** delete action invoked on a worksheet
- **Menu/dialog:** sheet tab context menu / delete workflow in progress
- **Screen:** same chart + table view

### Frame 100
- **Workbook:** same
- **Dialog:** Excel confirmation
- **Text:** `Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?`
- **Buttons:** `Eliminar` / `Cancelar`
- **Action:** final confirmation before deleting the selected sheet

If you want, I can turn this into a clean **shot list with timestamps + inferred workflow steps**.

[Batch 2 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen state is effectively the same.

### 101–106
- **Workbook/sheet:** `BD PQRS BOGOTA TE ESCUCHA MAYO 2026 - Excel`, sheet `CERT RESIDENCIA PROD-ABRIL`
- **Selection / edit:** no stable cell selection visible; sheet-tab right-click menu is open, then a delete confirmation modal appears
- **Action:** preparing to **delete a worksheet**
- **Visible data:** left table titled **“PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA VALIDOS / ABRIL 2026”**; right chart **“PRODUCTIVIDAD CERTIFICADOS DE RESIDENCIA / ABRIL 2026”**
- **Menus/dialogs:** sheet-tab context menu; Excel warning dialog: **“Microsoft Excel eliminar permanentemente esta hoja. ¿Desea continuar?”** with **Eliminar / Cancelar**

### 107–108
- **Workbook/sheet:** same workbook, sheet `CR-TIPO TRAMITE`
- **Selection / edit:** no cell range clearly selected; sheet-tab menu remains open in 108
- **Action:** viewing a **type-of-trámite** summary, likely before another move/delete action
- **Visible data:** table + 3D pie chart titled **“PRODUCTIVIDAD CERTIFICADO DE RESIDENCIA - TIPO DE TRAMITE / VIGENCIA ABRIL 2026”**
- **Visible categories:** `Personas privadas de la libertad`, `Trámite ante el ministerio de rel exteriores`, `Trámite de estudio`, `Trámite de subsidios`, `Trámites legales`, `Requisitos laborales`, `Proyectos locales`
- **Menus/dialogs:** sheet-tab context menu

### 109–111
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, sheet `DIAPOSITIVA No. 3`
- **Selection / edit:** table area visible; no clear single-cell selection
- **Action:** reviewing / copying locality metrics
- **Visible data:** columns **`PQRS GESTIONADAS N.1`**, **`PQRS PENDIENTES N.2`**, **`DOC.EXT. N.3`**, **`ORIENTACIONES No.4`**, **`CERT. PROPIEDAD No.5`**, **`CERT. RESIDENCIA No.6`**, **`ENCUESTAS DEL PERIODO`**, **`ENCUESTAS CON RESPUESTA COMPLETA`**
- **Visible rows:** `ANTONIO NARIÑO`, `BARRIOS UNIDOS`, `BOSA`, `CANDELARIA`, `CHAPINERO`, `CIUDAD BOLÍVAR`, `ENGATIVÁ`, etc.
- **Menus/dialogs:** none

### 112–115
- **Workbook/sheet:** `MAYO2026_PRODUCTIVIDAD_CR - Excel`, sheet `Productividad-CR`
- **Selection / edit:** main table is active; no modal
- **Action:** reviewing May residence productivity figures
- **Visible data:** table titled **“PRODUCTIVIDAD DE CERTIFICADO DE RESIDENCIA / VIGENCIA 1 AL 31 MAYO 2026”**
- **Chart labels visible:** `SUBA`, `KENNEDY`, `CIUDAD BOLÍVAR`, `TUNJUELITO`, `BOSA`, `FONTIBÓN`, `USME`, `ENGATIVÁ`, `USAQUÉN`
- **Menus/dialogs:** none

### 116–122
- **Workbook/sheet:** same workbook, switching among `CERT RESIDENCIA PROD-MAYO`, `CERT.P.HORIZONTAL MAYO`, `CR-TIPO TRAMITE`
- **Selection / edit:** right-click on sheet tabs; later a move/copy operation is in progress
- **Action:** **moving/copying worksheets** between sheets/workbooks
- **Visible data:** property-horizontal productivity table/chart appears when `CERT.P.HORIZONTAL MAYO` is active
- **Menus/dialogs:** **“Mover o copiar”** dialog with destination sheet list and **Crear una copia** checkbox; buttons **Aceptar / Cancelar**
- **Other:** Excel sheet-tab context menu appears repeatedly

### 123–129
- **Workbook/sheet:** same workbook set, mostly `CERT RESIDENCIA PROD-MAYO` / `CERT.P.HORIZONTAL MAYO` / `CR-TIPO TRAMITE`
- **Selection / edit:** sheet-tab context menu and copy/move state continue
- **Action:** continuing **sheet reorganization**
- **Visible data:** residence and property-horizontal productivity tables/charts remain visible
- **Menus/dialogs:** sheet-tab context menu; move/copy dialog persists in some frames

### 130–140
- **Workbook/sheet:** `Resumen SIDE Mayo 2026 - Excel`, sheet `REGISTRADO SIDE`
- **Selection / edit:** a grid area is active; no modal
- **Action:** reviewing registered-side records
- **Visible data:** left side shows a list of people/names with counts; right side shows locality blocks like `Alcaldía local Engativá`, `Barrios Unidos`, `Ciudad Bolívar`, `Kennedy`, `Usaquén`, etc.
- **Menus/dialogs:** none

### 141–146
- **Window:** Excel **Backstage / Archivo > Recientes**
- **Action:** switching workbooks
- **Visible items:** recent files list includes  
  `Resumen SIDE Mayo 2026`,  
  `05. SAC_atencion - Mayo 2026`,  
  `BASE DATOS PPT LOCALIDADES MAYO 2026`,  
  `INFORME PQRS SECRETARIA DE GOBIERNO MAYO 2026`,  
  `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`,  
  `REPORTE ENCUESTAS MAYO 2026 FORMATO SAC-F010`,  
  `MAYO2026_PRODUCTIVIDAD_PH`,  
  `MAYO2026_PRODUCTIVIDAD_CR`
- **Menus/dialogs:** none

### 147–153
- **Workbook/sheet:** `MAYO2026_PRODUCTIVIDAD_CR - Excel`, sheet `Productividad-CR`
- **Selection / edit:** formula cell visible
- **Action:** checking/reading formula totals
- **Visible formula:** **`=SUMA(G19:G25)`** in **H25**
- **Visible chart/table:** residence productivity table + horizontal bar chart
- **Visible percentages on chart:** `Proyectos locales 44.643%`, `Requisitos laborales 22.436%`, `Trámites legales 15.793%`, `Trámite de estudio 9.016%`, `Trámite de subsidios 6.258%`, `Personas privadas de la libertad 1.045%`, `Trámite ante el ministerio de rel exteriores 0.808%`
- **Menus/dialogs:** none

### 154–160
- **Workbook/sheet:** same workbook
- **Selection / edit:** right-click sheet-tab menu and move/copy flow
- **Action:** continuing worksheet management
- **Menus/dialogs:** **Mover o copiar** dialog again; destination workbook list visible; **Crear una copia** checkbox visible

### 161–172
- **Workbook/sheet:** same workbook / same chart-table view
- **Selection / edit:** tab context menu and hover states on the sheet tabs
- **Action:** organizing sheets and likely confirming copy/move
- **Menus/dialogs:** sheet-tab context menu; occasional tooltip over chart area (e.g. **“Área de trazado”**)

### 173–179
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 - Excel`, sheet `Tabla 10 indicadores_Ajustado`
- **Selection / edit:** indicator table active
- **Action:** reviewing SAC-F010 indicators and totals
- **Visible table title:** **“Tabla 10. indicadores / Encuesta percepción y satisfacción ciudadana 2022 SAC-F010”**
- **Visible sections:** `Efectividad`, `Accesibilidad`, `Oportunidad`
- **Visible score box:** **“Regla de tres simple”** with values around **4.9 / 4.0 / 4.8** and percentages including **100%** and **95%**
- **Menus/dialogs:** sheet-tab context menu and move/copy dialog appear in some frames

### 180–184
- **Workbook/sheet:** back to `MAYO2026_PRODUCTIVIDAD_CR - Excel` and then indicator sheet again
- **Action:** switching between productivity workbook and indicator workbook
- **Menus/dialogs:** one Excel **save changes** confirmation appears:
  - **“¿Desea guardar los cambios efectuados en MAYO2026_PRODUCTIVIDAD_CR.xlsx?”**
  - buttons **Guardar / No guardar / Cancelar**

### 185
- **Window:** Windows task switcher / Alt-Tab style overview
- **Action:** selecting among open Excel windows
- **Visible thumbnails:** multiple workbooks including `BD PQRS...`, `MAYO2026_PRODUCTIVIDAD_CR`, `BASE DATOS PPT LOCALIDADES...`, `REPORTE ENCUESTAS MAYO...`, `INFORME PQRS...`, file explorer windows

### 186–187
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026`, sheet `CERT.P.HORIZONTAL MAYO`
- **Selection / edit:** none obvious
- **Action:** reviewing property-horizontal productivity by locality
- **Visible data:** bar chart with top percentages:
  - `USAQUÉN 36.218%`
  - `SUBA 13.597%`
  - `TUNJUELITO 12.979%`
  - `FONTIBÓN 12.237%`
  - `KENNEDY 6.180%`
  - `CHAPINERO 4.697%`
- **Menus/dialogs:** none

### 188–190
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026`, sheet `Tabla 10 indicadores_Ajustado` / `Calificaciones Totales`
- **Selection / edit:** same indicator table; sheet-tab context menu appears
- **Action:** navigating indicator sheets and tab management
- **Menus/dialogs:** sheet-tab context menu with options like **Insertar**, **Eliminar**, **Cambiar nombre**, **Mover o copiar**, **Ver código**, **Ocultar**, **Mostrar**

### 191–193
- **Workbook/sheet:** same indicator workbook
- **Selection / edit:** move/copy dialog active
- **Action:** copying/moving one of the indicator sheets
- **Menus/dialogs:** **Mover o copiar** dialog with destination workbook list and **Crear una copia** checkbox

### 194–200
- **Workbook/sheet:** indicator workbook, `Tabla 10 indicadores_Ajustado` / `Calificaciones Totales`
- **Selection / edit:** tab context menu continues; later a delete confirmation appears
- **Action:** final tab cleanup / deletion attempt
- **Visible data:** green indicator table remains visible beneath dialogs
- **Menus/dialogs:** Excel warning dialog:
  - **“Microsoft Excel eliminar permanentemente esta hoja. ¿Desea continuar?”**
  - buttons **Eliminar / Cancelar**

If you want, I can turn this into a **clean JSON timeline** with one object per frame range.

[Batch 3 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen is effectively the same.

**Workbook throughout:** `BD PORS BOGOTA E ESCUCHA MAYO 2026 - Excel`  
**Main sheets seen:** `Tabla 10 indicadores_Ajustado`, `Calificaciones Totales`, `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, `SEGUIMIENTO DIAS`

---

### Frames 201–204
- **Sheet:** `Tabla 10 indicadores_Ajustado`
- **Action:** sheet-tab management / delete confirmation
- **Visible dialog:** `Microsoft Excel eliminará permanentemente esta hoja. ¿Desea continuar?` with buttons **Eliminar** / **Cancelar**
- **Data visible:** `Tabla 10. indicadores` with the table `Encuesta percepción y satisfacción ciudadana 2022 SAC-F010`; columns for `Peso`, `Indicador`, `Variables`, `ID de la pregunta`, scores 1–5, `Número de encuestas`, `Calificación Promedio`, `Puntaje Item`, etc.
- **Menus:** right-click sheet-tab context menu appears in 203/204 with `Insertar`, `Eliminar`, `Cambiar nombre`, `Mover o copiar`, `Ver código`, `Proteger hoja`, `Color de pestaña`, `Ocultar`, `Mostrar`
- **Selection:** no clear cell edit; focus is on sheet-tab actions

---

### Frames 205–211
- **Sheet:** `Calificaciones Totales`
- **Action:** reviewing/calculating totals; right-clicking the sheet tab
- **Selection:** visible active-cell area around `Y24` / later `Q33` (name box changes across frames)
- **Data visible:** locality scoring tables; one table shows `Calificación Canal Virtual Localidades`, another `Calificación Canal Presencial`, and `Calificación Canal Telefónico`
- **Menus:** sheet-tab context menu repeatedly open (`Insertar`, `Eliminar`, `Cambiar nombre`, `Mover o copiar`, etc.)
- **Notable values:** column blocks and green summary cells show totals around `4.0`, `4.5`, `4.7` depending on the section

---

### Frames 212–215
- **Sheet:** `Tabla 10 indicadores_Ajustado`
- **Action:** verification of `Tabla 10` and “regla de tres” conversion
- **Selection:** around the main table; right-side yellow box is in view
- **Data visible:**
  - `Tabla 10. indicadores`
  - `Encuesta percepción y satisfacción ciudadana 2022 SAC-F010`
  - Right-side box: `Regla de tres simple`
  - visible values: `4.9 -> 100%`, `4.6 -> 100%`, `4.8 -> 95%`
- **Menus/dialogs:** none in 215; in 212–213 the sheet-tab menu is open again
- **Action context:** looks like the user is checking whether the indicator score maps correctly to the percentage

---

### Frames 216–218
- **Frame 216**
  - **Sheet:** `SEGUIMIENTO DIAS`
  - **Action:** viewing the monthly tracking table and chart
  - **Data visible:** `Porcentaje de Descongestión`, `Gestión Extemporánea`, `Gestión Oportuna`, `Pendientes en términos`, `Pendientes vencidos`
- **Frame 217**
  - **Sheet:** `REGISTRADO SIDE`
  - **Action:** summary table review
  - **Data visible:** `Etiquetas de fila` / `Suma de TOTAL`
  - **Readable totals:** `Candelaria 96`, `Engativá 98`, `Fontibón 48`, `Kennedy 18`, `Mártires 70`, `Nivel Central 693`, `Santa Fe 15`, `Suba 19`, `Teusaquillo 666`, `Total general 1723`
- **Frame 218**
  - **Sheet:** `ENTREGADO SIDE`
  - **Action:** document delivery/return summary
  - **Data visible:** `DEVUELTO SIDE Mayo 2026`
  - **Readable total:** `TOTAL 1269`
  - Looks like a table by document type: `Cédula de ciudadanía`, `Cédula de extranjería`, `Contraseña cédula ciudadanía`, `Libreta Militar`, etc.

---

### Frames 219–227
- **Sheet:** `INFORME WEB ABRIL` → later `SEGUIMIENTO DIAS`
- **Action:** scrolling through report dashboards and charts
- **Data visible:**
  - `Tabla No. 12 PARTICIPACIÓN POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`
  - `Participación por Localidad` horizontal bar chart
  - `Porcentaje de Descongestión`, `Gestión Oportuna`, `Pendientes en términos`, `Pendientes vencidos`
- **Notable visuals:** several pivot-style charts and tables, mostly report summary views
- **Transitions:** 219–220 still on report table; 221–227 move into the tracking dashboard and the locality bar chart

---

### Frames 228–236
- **Sheet:** `INFORME WEB ABRIL`
- **Action:** detailed PQRS timing analysis
- **Data visible:**
  - `TIEMPO PROMEDIO DE RESPUESTA POR TIPOLOGÍA Y DEPENDENCIA (DÍAS)`
  - category headers like `DENUNCIA POR ACTOS DE...`, `DERECHO DE PETICIÓN`, `QUEJA`, `RECLAMO`, `SOLICITUD DE ACCESO A LA INFORMACIÓN`, `SOLICITUD DE COPIA`, `SUGERENCIA`, `FELICITACIÓN`
  - lower section: `Tabla No. 11 Localidades y Nivel Central`
- **Notable values:** yellow bars indicate response times; readable totals include `30 DÍAS`, `5 DÍAS`, `10 DÍAS` on the header row
- **Selection:** the user is moving around the report, not editing a clear single cell range

---

### Frames 237–247
- **Sheet:** `SEGUIMIENTO DIAS`
- **Action:** navigating and likely pasting/copying month values into the tracking table
- **Data visible:** monthly columns `ENERO`, `FEBRERO`, `MARZO`, `ABRIL`, `MAYO`, `JUNIO`, etc.
- **Notable chart:** bar chart on the right with monthly totals
- **Menus:** frame 239 shows a right-click context menu on a cell with options like `Cortar`, `Copiar`, `Opciones de pegado`, `Pegado especial...`, `Eliminar`, `Borrar contenido`, etc.
- **Selection:** visible focus around `MAYO` column and nearby cells; cursor moves through the grid as if populating the month values

---

### Frames 248–259
- **Sheet:** mostly `INFORME WEB ABRIL`
- **Action:** moving between report sections, then opening PivotTable field settings
- **Data visible:** repeated blocks of `CANT. PQRS GESTIONADAS EN TIEMPO PROMEDIO DE RESPUESTA...`
- **Frame 259:** `Campos de tabla dinámica` panel open on the right
  - checkboxes visible: `Número petición`, `Duplicado`, `Sector`, `Tipo de entidad`, `Entidad`, `Tipo de dependencia`, `Dependencia`, `Dependencia hija`, `Tema`
  - pivot areas visible: `Filtros`, `Columnas`, `Filas`, `Valores`
- **Action:** configuring the pivot source/fields for report generation

---

### Frame 260
- **OS view:** Alt-Tab switcher
- **Action:** window switching
- **Visible windows:** several Excel files/thumbnails, including:
  - `BASE DATOS PPT LOCALIDADES MAYO...`
  - `BD PORS BOGOTA E ESCUCHA MAYO...`
  - `REPORTE ENCUESTAS MAYO 2026...`
  - `INFORME PQRS SECRETARIA DE GOBIER...`
  - `Reporte PQRS Mayo2026`
  - `ANALISIS INFORME PQRS RED QUEJAS...`

---

### Frames 261–264
- **Workbook:** `BASE DATOS PPT LOCALIDADES MAYO 2026` / same reporting family
- **Action:** back to PivotTable configuration
- **Dialog/panel:** `Campos de tabla dinámica` still open
- **Data visible:** pivot tables and chart placeholders; one section shows `Tipo de ingreso`, `Tipo reporte`, `Estado petición final`
- **Transition:** the user is still adjusting the data source/fields for the report dashboard

---

### Frames 265–278
- **Sheet:** `SEGUIMIENTO DIAS`
- **Action:** navigating the monthly tracking grid and chart, likely copying values between months/rows
- **Data visible:** `Gestión Extemporánea`, `Gestión Oportuna`, `Pendientes en términos`, `Pendientes vencidos`
- **Right-side chart:** vertical bars with monthly totals
- **Selection:** visible cell focus moves across `MAYO`, `JUNIO`, and adjacent cells; no obvious formula edit shown
- **Menus:** frame 267 shows a cell right-click context menu again

---

### Frames 279–287
- **Sheet:** `INFORME WEB ABRIL`
- **Action:** PivotTable/chart maintenance and source updates
- **Data visible:**
  - `Total Peticiones del Mes`
  - `DESCONGESTIÓN - SOLO INFORMATIVO`
  - yellow summary cells for `Gestión Extemporánea` / `Gestión Oportuna`
- **Menus/ribbon:** `Analizar tabla dinámica` ribbon visible; commands like `Cambiar origen de datos`
- **Frame 285–287:** the user opens the pivot source change workflow

---

### Frames 288–300
- **Workbook/sheet:** `Reporte PQRS Mayo2026`
- **Action:** changing PivotTable data source
- **Dialog:** `Cambiar origen de datos de tabla dinámica`
  - option selected: `Seleccionar una tabla o rango`
  - field `Tabla o rango:` contains a reference into `Reporte PQRS Mayo2026`
- **Data visible in background:** raw PQRS data table with columns such as `Núm.`, `Duplicados`, `Sector`, `Tipo de Entidad`, `Entidad`, `Tipo de Dependencia`, `Dependencia`, `Tema`, `Subtema`, `Funcionario`, `Estado`, `Punto`, `Canal`, `Tipo pet`, `Estado`, `Asunto`, `Proceso`
- **Action context from audio fits here:** copying/moving source data so the web/report workbook can be updated with the correct locality structure and totals
- **Frames 293–300:** repeated attempts to confirm/edit the source range while the modal stays open

---

If you want, I can turn this into a **clean table with columns: frame range / sheet / action / evidence**.

[Batch 4 - gpt-5.4-mini]
Grouped log by contiguous near-identical frames.

- **301–309**: `BD PORS BOGOTA TE ESCUCHA MAYO 2026 - Excel` → sheet **INFORME WEB ABRIL**. Pivot-table view titled **“DESCONGESTIÓN - SOLO INFORMATIVO”** with the **Campos de tabla dinámica** pane open. Visible yellow notes/values include **653**, **10908**, **1129**, **214** and **90%**.  
- **310–314**: same workbook, switched to sheet **Reporte PQRS Mayo2026**. Raw data table visible; **“Cambiar origen de datos de tabla dinámica”** dialog open, indicating the pivot source is being changed to the PQRS sheet/range.  
- **315–329**: back on **INFORME WEB ABRIL**. User is pasting/verifying summary figures; a long **`IMPORTARDATOSDINAMICOS(...)`** formula is visible in the formula bar. Yellow summary cells show **653**, **10908**, **1129**, **214**, and the desegregation summary.  
- **330–338**: sheet **SEGUIMIENTO DÍAS**. Monthly summary table visible with rows like **Gestión Extemporánea**, **Gestión Oportuna**, **Pendientes en términos**, **Pendientes vencidos**. Readable values include **496 / 716 / 670 / 686 / 653**, **7.071 / 7.838 / 10.325 / 11.524 / 10.908**, **966 / 1.152 / 1.407 / 1.139 / 1.129**, **239 / 228 / 244 / 227 / 214**.  
- **339–347**: still **SEGUIMIENTO DÍAS**. Summary totals on the right show **3.221**, **47.666**, **5.793**, **1.152**. Formula bar shows **`=SUMA(B28:M28)`**. The chart **“Seguimiento Gestión PQRS”** is visible below.  
- **348–352**: chart area shifts right; the line chart **“Porcentaje de descongestión”** is being centered/selected.  
- **353–360**: same chart, now clearly visible with line values around **86%**, **86%**, **87%**, **90%**, **90%**.  
- **361–379**: the line chart is actively selected and moved; tooltip appears on the May point, showing the series point around **90%**.  
- **380–385**: right-click context menu on the chart series/point. Options visible: **Eliminar serie**, **Restablecer para hacer coincidir el estilo**, **Cambiar tipo de gráfico de series**, **Seleccionar datos**, **Agregar línea de tendencia**, **Formato de etiqueta de datos**, **Formato de punto de datos**. Formula bar shows a **`SERIES('SEGUIMIENTO DÍAS'!$B$35:$F$35, 'SEGUIMIENTO DÍAS'!$B$36:$F$36, 1)`**-type chart formula.  
- **386–400**: **Formato de etiqueta...** pane opens on the right for the chart labels. Options shown: **Value from cells**, **Series name**, **Category name**, **Value**, **Show leader lines**, **Legend key**, separator, and label position (**Center / Right / Above**).

**Throughout**: Teams screen-share bar is visible at the bottom: **“teams.microsoft.com está compartiendo tu pantalla”** with **Dejar de compartir** / **Ocultar**.  

If you want, I can turn this into a strict **one-line-per-frame 00301–00400 log** next.

[Batch 5 - gpt-5.4-mini]
I verified the frames. Same workbook throughout: **“BD PORS BOGOTA TE ESCUCHA MAYO 2026”** in **Excel**, active sheet **“SEGUIMIENTO DÍAS”**. No workbook/sheet switch. Teams screen-sharing banner is visible the whole time.

### Frame analysis
- **401-412**:  
  - **Selection**: chart data label/point on the top-right of the line chart (May point) is selected; no worksheet range is actively edited.  
  - **Action**: formatting chart labels.  
  - **Visible data**: chart titled **“Porcentaje de descongestión”** with line across **ENERO, FEBRERO, MARZO, ABRIL, MAYO**; values shown near points around **86%, 86%, 87%, 90%, 90%**. Left table shows month headers **MAYO, JUNIO, JULIO, AGOSTO, SEPTIEMBRE, OCTUBRE, NOVIEMBRE, DICIEMBRE** and visible numbers like **653, 10.908, 1.129, 214, 11.561, 12.904, 867, 12.037, 7%, 85%**, plus **#DIV/0!** in several cells. Totals near the chart include **3.221, 47.666, 5.793, 1.152, 59.487**.  
  - **Open window**: right pane **“Formato de etiqueta…”** with label options and checkboxes.

- **413**:  
  - **Selection**: chart **series** selected.  
  - **Action**: switching from label formatting to series formatting.  
  - **Visible formula**: chart series formula appears in the formula bar (`=SERIES(...)`), referencing **SEGUIMIENTO DÍAS** ranges.  
  - **Open window**: right pane **“Formato de serie de…”**.

- **414-418**:  
  - **Selection**: specific **data point** at the top-right of the line chart.  
  - **Action**: formatting the point itself.  
  - **Open window**: right pane **“Formato de punto…”** with **Sombra / Iluminado / Bordes suaves / Formato 3D**.

- **419-423**:  
  - **Selection**: same chart point, now right-clicked.  
  - **Action**: context menu open on chart point.  
  - **Menu items visible**: **Eliminar serie**, **Restablecer para hacer coincidir el estilo**, **Cambiar tipo de gráfico de series**, **Seleccionar datos**, **Agregar línea de tendencia**, **Formato de etiqueta de datos…**, **Formato de punto de datos…**.

- **424-427**:  
  - **Selection**: chart point remains selected; context menu gone.  
  - **Action**: hovering over the chart area.  
  - **Open window**: no major pane change visible; chart still active.

- **428**:  
  - **Selection**: chart object selected; a single worksheet cell on the right becomes active (**W41** visible with green border).  
  - **Action**: focus shifts away from the context menu, likely preparing another formatting change.  
  - **Open window**: right pane **“Formato de forma”**.

- **429-430**:  
  - **Selection**: same chart object / active cell area.  
  - **Action**: no visible content change beyond chart focus.  
  - **Open window**: **“Formato de forma”** remains.

- **431-436**:  
  - **Selection**: chart data label near the May point.  
  - **Action**: reopening label formatting.  
  - **Open window**: right pane **“Formato de etiquet…”**; label position controls visible.

- **437-449**:  
  - **Selection**: data label settings.  
  - **Action**: choosing label placement.  
  - **Open window**: label position options visible: **Centro, Izquierda, Derecha, Encima, Debajo**.  
  - **Chart**: May label remains clustered near the top-right point.

- **450-456**:  
  - **Selection**: label number formatting section.  
  - **Action**: adjusting numeric display for data labels.  
  - **Open window**: **“Número”** section with **Posiciones decimales**, separator option, and negative number examples.

- **457-463**:  
  - **Selection**: number format dropdown opened.  
  - **Action**: choosing format type.  
  - **Dropdown items visible**: **General, Número, Moneda, Contabilidad, Fecha, Hora, Porcentaje, Fracción, Científico, Texto, Especial, Personalizado**.

- **464-470**:  
  - **Selection**: number format selection changes (hovering/selecting **Personalizado** then back to general/number controls).  
  - **Action**: refining how label values appear.  
  - **Open window**: same label formatting pane, number section still active.

- **471-476**:  
  - **Selection**: numeric formatting field.  
  - **Action**: decimal-place adjustment continues.  
  - **Open window**: number section with decimals field and negative-number styles.

- **477-481**:  
  - **Selection**: label position options revisited.  
  - **Action**: fine-tuning label placement after number-format edits.  
  - **Open window**: same **Formato de etiqueta** pane.

- **482-485**:  
  - **Selection**: chart still active; no pane change.  
  - **Action**: chart remains selected after formatting edits.  
  - **Visible result**: labels cluster more tightly around the May point.

- **486-490**:  
  - **Selection**: chart point/series active; cell **W41** visible to the right.  
  - **Action**: mouse moves over the chart; no new menu.  
  - **Chart**: the line remains at roughly **86% → 86% → 87% → 90% → 90%**.

- **491-500**:  
  - **Selection**: same chart, with cursor moving between the March/April region and the higher May point.  
  - **Action**: final hover/selection adjustments on the chart.  
  - **Open windows**: none new; Excel stays on the same sheet with the Teams sharing bar at the bottom.

If you want, I can turn this into a **frame-by-frame CSV-style log** next.

[Batch 6 - gpt-5.4-mini]
Here’s the frame-by-frame read, grouped where the screen is effectively the same.

### Workbook / sheet
- **Workbook:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026`
- **Visible tabs:** `REGISTRADO SIDE`, `ENTREGADO SIDE`, `Reporte PQRS Mayo2026`, `INFORME WEB ABRIL`, `SEGUIMIENTO DÍAS`

### Frames 00501–00525
- **Sheet:** `SEGUIMIENTO DÍAS`
- **Selected object:** the line chart **“Porcentaje de descongestión”** is selected (handles visible; later the chart title and data labels are editable).
- **Action:** chart selection / inspection, no typing visible.
- **Visible data:**
  - Line chart values around **ENERO 86%**, **FEBRERO 86%**, **MARZO 87%**, **ABRIL 89.9%**, **MAYO 89.0%**.
  - Left tables show months and values like **653**, **10,908**, **1,129**, **214**, totals like **11,561**, **12,904**, and multiple `#DIV/0!` cells in the monthly rows.
- **Open UI:** Excel chart tools; Teams sharing bar at bottom (`Dejar de compartir`).

### Frames 00526–00542
- **Sheet:** still `SEGUIMIENTO DÍAS`
- **Selected object/range:** cells in the percentage rows and the chart area below; formula bar shows percentage formulas like:
  - `=+G33/G34`
  - `=+E33/E34`
  - `=+B33/B34`
- **Action:** reviewing/calculating percentages and charting them.
- **Visible data:**
  - Table section with rows like:
    - **Gestión Externa**
    - **Gestión Oportuna**
    - **Pendientes en términos**
    - **Pendientes vencidos**
  - Another chart below: **“Seguimiento Días de Gestión”** with bars labeled **6**, **6**, **5**, **5**, **3**.
- **Open UI:** Excel chart object plus Teams bar.

### Frames 00543–00546
- **Sheet:** switched to `INFORME WEB ABRIL`
- **Selected cell/range:** pivot-style cell around **W23** / related summary area.
- **Action:** right-click / inspect pivot output.
- **Visible data:**
  - Pivot/table titled **“DE DESCONGESTIÓN - SOLO INFORMATIVO”**
  - Another pivot block at right with fields like **Tipo de ingreso**, **Tipo reporte**, **Pendiente en términos**, **Pendiente vencidos**, **Total general**.
  - Formula bar shows a pivot lookup formula:
    - `#IMPORTADATOSDINAMICOS("Número petición", $V$5, "Tipo de pendiente", "Pendiente en términos")`
- **Open UI:** Excel context menu is open (Cut, Copy, Paste options, Paste Special, Insert copied cells, Delete content, Filter, Sort, Format Cells, Define name, Hyperlink).

### Frames 00547–00600
- **Sheet:** `INFORME WEB ABRIL`
- **View:** scrolled far down to rows around **1000–1056**
- **Selected cell/range:** a cell in the large locality table, with the name box showing selections like **H1056**, **N1042**, **W1043**, etc. (selection shifts as scrolling continues).
- **Action:** navigating / comparing locality totals, likely preparing copy-paste from one structure to another.
- **Visible table:**
  - Header: **“Tabla No. 12 PARTICIPACIÓN POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO”**
  - Columns:
    - **ALCALDÍA LOCAL**
    - **PETICIONES RECIBIDAS POR LOCALIDAD DE LOS HECHOS**
    - **PORCENTAJE**
    - **PARTICIPACIÓN**
    - **CERT. RESIDENCIA**
    - **PROPIEDAD HORIZONTAL**
    - **ORIENTACIONES**
    - **ENCUESTAS**
    - **DOC EXT.**
  - Right-side locality list visible: **ANTONIO NARIÑO**, **BARRIOS UNIDOS**, **BOSA**, **CANDELARIA**, **CHAPINERO**, **CIUDAD BOLÍVAR**, **ENGATIVÁ**, **FONTIBÓN**, **KENNEDY**, **MÁRTIRES**, **PUENTE ARANDA**, **RAFAEL URIBE**, **SAN CRISTÓBAL**, **SANTA FE**, **SUBA**, **TEUSAQUILLO**, **TUNJUELITO**, **USAQUÉN**, **LA CUN…**, **NVL CENTRAL**, **SUPERCADE**, **EN BLANCO**.
  - Bottom total bar shows **TOTAL GENERAL 10,359** and **100%**.
- **Open UI:** repeated right-click context menu + mini formatting toolbar; some frames show the menu open, some closed.
- **Screen behavior:** several horizontal/vertical scroll jumps; the right-side summary block stays fixed while the left table shifts.

### Notable screen transitions
- **00501→00526:** same workbook, but focus moves from the top chart area to the lower comparative tables.
- **00542→00543:** clear sheet switch from `SEGUIMIENTO DÍAS` to `INFORME WEB ABRIL`.
- **00546→00547:** major vertical scroll down to the deep rows of the locality participation table.
- **00575+:** right-click menu appears again, confirming active cell editing/copying workflow.

### Overall action
The user is **verifying and transferring reporting data** between the “localidades” structure and the “web” structure, checking totals, percentages, and pivot outputs before closing the report.

[Batch 7 - gpt-5.4-mini]
Most frames are near-identical, so I grouped identical states by range.

1) **00601–00605**
- **Workbook/sheet:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026 - Excel`, sheet **INFORME WEB ABRIL**
- **Selection:** cell around **N1045** (visible name box), formula bar shows **36**
- **Action:** idle review of the report table
- **Visible data:** headers like **ALCALDIA LOCAL**, **CERT. RESIDENCIA**, **PROPIEDAD HORIZONTAL**, **ORIENTACIONES**, **ENCUESTAS**, **DOC. EXT.**; right-side locality list with counts
- **Open UI:** Excel only

2) **00606–00607**
- **Workbook/sheet:** same Excel workbook, **INFORME WEB ABRIL**
- **Selection:** same general row area in the main table
- **Action:** **right-click context menu opened**
- **Visible menu items:** **Cortar**, **Copiar**, **Opciones de pegado**, **Pegado especial...**, **Insertar celdas copiadas...**, **Eliminar...**, **Borrar contenido**, **Filtro**, **Ordenar**, **Formato de celdas...**, **Definir nombre...**, **Vínculo**
- **Open UI:** Excel context menu

3) **00608–00611**
- **Workbook/sheet:** same
- **Selection:** name box shows **N1046**; formula bar shows **179**
- **Action:** selection moves across the report; likely positioning/copying data between rows
- **Visible data:** the same locality comparison table; highlighted row in the left block and the right-side list
- **Open UI:** Excel only

4) **00612–00613**
- **Workbook/sheet:** same
- **Selection:** same area
- **Action:** **right-click context menu opened again**
- **Open UI:** Excel context menu

5) **00614–00617**
- **Workbook/sheet:** same
- **Selection:** name box shows **N1047**; formula bar shows **713**
- **Action:** continued row-by-row navigation/editing in the report
- **Visible data:** same table; a horizontal highlight spans part of the row
- **Open UI:** Excel only

6) **00618–00619**
- **Workbook/sheet:** same
- **Selection:** same region
- **Action:** **right-click context menu opened**
- **Open UI:** Excel context menu

7) **00620–00631**
- **Workbook/sheet:** same
- **Selection:** moves through rows around **N1048–N1050**
- **Action:** repeated **copy/paste / context-menu** workflow; likely transferring items into the report
- **Visible data:** same table structure; right-side locality count block stays visible
- **Open UI:** alternating Excel sheet and context menu

8) **00632–00645**
- **Workbook/sheet:** same
- **Selection:** moves through rows around **N1050–N1052**
- **Action:** repeated **right-click / paste-special / copy** workflow
- **Visible values read on-screen:** formula bar values include **434**, **537**, **677**, **387**, **134**
- **Open UI:** Excel + context menu

9) **00646–00691**
- **Workbook/sheet:** same
- **Selection:** continues down to rows around **N1053–N1059**
- **Action:** same copy/paste adjustment process; occasional menu opens and close
- **Visible values read on-screen:** **45**, **306**, **387**, **60**, **134**
- **Open UI:** Excel only, with intermittent context menus

10) **00692–00700**
- **Screen transition:** **Excel -> Chrome/Teams**
- **Visible page:** Microsoft Teams meeting page, tab title **“Trabajar Inform…”**
- **Action:** meeting in waiting state
- **Visible text:** **“Esperando a que se unan otros usuarios…”**
- **Open UI:** Teams browser window with recording/transcription notice and meeting controls

**Overall:** this segment is the user copying/comparing report rows in the **INFORME WEB ABRIL** sheet, using repeated right-click paste/copy actions, then switching to Teams to continue/close the session.

[Batch 8 - gpt-5.4-mini]
All shown frames are the same Teams screen, not Excel.

- **Workbook/sheet:** none visible
- **Selected cells/ranges:** none visible
- **Action:** no Excel action visible; this is a Microsoft Teams meeting/viewer page
- **Data/values visible:** only UI text like “Esperando a que se unan otros usuarios…”, the participant name “Yesenia Patino Figueroa”, and the sharing banner
- **Open windows/menus:** Chrome/Teams web page, recording/transcription notice, screen-sharing bar, participant panel

**Transition:** no screen change across the frames; they appear static/identical.

So I **cannot verify any workbook filename, tab name, formulas, or cell edits** from these frames.

[Batch 9 - gpt-5.4-mini]
### Prompt in English
Analyze the provided frames from the segment “Comparative tables, final verification, and close (part 9/13)” and describe, for each visible change, the Excel workbook/sheet, selected ranges/cells, actions performed, readable values, and any open menus/windows. Be exact, use OCR when text is visible, and note transitions between Teams and Excel.

### Notes
- Assumptions: the frame sequence is mostly a continuous screen recording with repeated static frames.
- Safety constraints: do not invent unreadable cell text; mark uncertain text as partial.
- Missing critical inputs: none.

Loaded skills: `input-compressor`, `english-prompt-compiler`, `skill-router`, `document-reader`.

## Análisis de los frames

**Transición general**
- **Frames 00801–00830:** Microsoft Teams en navegador, pantalla compartida en estado de espera (“Esperando a que se unan otros usuarios…”). No hay Excel visible.
- **Frame 00831 en adelante:** transición clara a **Excel**.

### 1) Frames 00831–00846
- **Workbook visible:** `BD PQRS BOGOTA ... MAYO 2026 - Excel`
- **Sheet activa:** `INFORME WEB ABRIL`
- **Zona visible:** hoja con una tabla grande comparativa; a la derecha hay un bloque auxiliar de datos por localidad.
- **Selección/celda:** se ve el cursor sobre celdas del bloque central; en varias tomas el **Name Box** muestra celdas como `H1045`, `N1055`, `E1052`, `H1052`, `H1061`.
- **Acción:** revisión/copia de datos entre filas; el usuario está navegando y preparando contenido para moverlo.
- **Valores legibles:** aparecen valores en la barra de fórmulas como `306`, `102`, `20`, `902`, `235`, `491`, `543`, `310`. En una celda porcentual se ve `0,2358713086104202%` (aprox.).
- **Ventanas abiertas:** Excel solo; abajo sigue visible la barra de Teams “Dejar de compartir”.

### 2) Frames 00847–00848
- **Workbook/sheet:** misma sesión, misma hoja `INFORME WEB ABRIL`.
- **Acción:** clic derecho sobre una celda/rango.
- **Menú abierto:** menú contextual de Excel con opciones visibles como:
  - Cortar
  - Copiar
  - Opciones de pegado
  - Pegado especial
  - Borrar contenido
  - Insertar
  - Eliminar
  - Ordenar
  - Filtrar
  - Formato de celdas
  - Vínculo
- **Interpretación:** preparación para copiar/pegar o limpiar contenido.

### 3) Frames 00849–00856
- **Workbook/sheet:** igual.
- **Selección/celda:** el cursor sigue sobre el bloque central de la tabla; se alternan selecciones en filas alrededor de `1047–1058`.
- **Acción:** navegación por celdas y revisión de valores; no se ve escritura directa.
- **Datos visibles:** aparecen cifras sueltas en la barra de fórmulas y celdas; el bloque derecho de resumen por localidades sigue visible.
- **Ventanas:** sin diálogos; solo Excel.

### 4) Frames 00857–00858
- **Workbook/sheet:** igual.
- **Acción:** nuevo clic derecho.
- **Menú contextual:** reaparece el menú de Excel con opciones de copiar/pegar, cortar, borrar contenido, filtrar, ordenar, formato de celdas, etc.
- **Interpretación:** el usuario está manipulando rangos, probablemente copiando valores.

### 5) Frames 00859–00862
- **Workbook/sheet:** igual.
- **Selección/celda:** el Name Box cambia a celdas como `N1057`, `N1058`, `H1061`.
- **Valores legibles:** `20`, `235`, `543`, `310` aparecen en la barra de fórmulas o celda activa.
- **Acción:** navegación y verificación de cifras.
- **Ventanas:** solo Excel.

### 6) Frames 00863–00866
- **Workbook/sheet:** igual.
- **Acción:** clic derecho otra vez sobre el bloque central.
- **Menú abierto:** menú contextual de Excel visible.
- **Interpretación:** operaciones repetidas de copiar/pegar o limpieza de celdas.

### 7) Frames 00867–00873
- **Workbook/sheet:** igual.
- **Zona visible:** tabla principal + bloque derecho de resumen.
- **Selección:** se mueve hacia el bloque derecho; parece seleccionarse una fila/celda dentro del resumen.
- **Acción:** revisión de totales/porcentajes.
- **Valores:** siguen visibles números de resumen y porcentajes; una celda activa muestra `0,2358713086104202%` en uno de los frames cercanos.

### 8) Frames 00874–00875
- **Workbook/sheet:** igual.
- **Acción:** clic derecho otra vez.
- **Menú contextual:** visible con las mismas opciones.
- **Interpretación:** probablemente copiando o reemplazando contenido.

### 9) Frames 00876–00892
- **Workbook/sheet:** igual.
- **Selección/celda:** el cursor recorre el bloque central; el Name Box cambia entre celdas cercanas a `H1042`, `H1047`, `N1060`, etc.
- **Acción:** verificación de cifras y posicionamiento.
- **Datos legibles:** siguen apareciendo valores aislados como `310`, `543`, `491`, `609`.
- **Estructura visible:** tabla comparativa con filas por localidad y un bloque de cifras a la derecha.
- **Ventanas:** Excel sin diálogos adicionales.

### 10) Frames 00893–00895
- **Workbook/sheet:** igual.
- **Acción:** clic derecho nuevamente.
- **Menú contextual:** vuelve a aparecer.
- **Interpretación:** repetición de la misma operación de edición sobre el rango seleccionado.

### 11) Frames 00896–00900
- **Workbook/sheet:** igual.
- **Selección/celda:** vuelve a verse el rango central sin menú abierto; Name Box muestra celdas como `N1061`.
- **Acción:** revisión final de valores.
- **Datos legibles:** `543` aparece en la barra de fórmulas en una de estas tomas.
- **Ventanas:** Excel + barra inferior de Teams “Dejar de compartir”.

## Resumen operativo del segmento
- El usuario **trabaja en Excel** sobre la hoja **`INFORME WEB ABRIL`** del libro **`BD PQRS BOGOTA ... MAYO 2026`**.
- La actividad visible es de **copiar/revisar/mover celdas** en un cuadro comparativo.
- Se ven **múltiples clics derechos** con menú contextual abierto.
- No se observan fórmulas complejas escritas; sí **valores numéricos y porcentuales** siendo revisados.
- La transición principal fue **Teams (espera) → Excel (edición de tabla)**.

[Batch 10 - gpt-5.4-mini]
Here’s the frame-by-frame readout, grouped where the screen state is effectively the same.

### 00901–00929
- **Workbook/sheet:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026` → `INFORME WEB ABRIL`
- **Selection/modification:** right-click context menu over a single cell in the lower-right data area; active cell moves around the summary block (`H1046`, `N1062`, `M1063`-type positions visible in the name box across frames).
- **Action:** navigating/copying/pasting within the table; no full paste yet, but the Excel context menu shows `Cortar`, `Copiar`, `Pegado especial`, `Insertar celdas copiadas`, `Eliminar`, `Borrar contenido`, `Filtrar`, `Ordenar`.
- **Visible data:** large table with headers like `CERT. RESIDENCIA`, `PROPIEDAD HORIZONTAL`, `ORIENTACIONES`, `ENCUESTAS`, `DOC EXT.`; bottom `TOTAL GENERAL` row visible.
- **Open menus/windows:** Excel right-click menu + floating mini toolbar.

### 00930–00931
- **Window:** Chrome/Teams meeting page (`teams.microsoft.com`)
- **Selection/modification:** none in Excel; this is a full screen switch.
- **Action:** meeting waiting state.
- **Visible text:** `Esperando a que se unan otros usuarios...`, sharing bar `Dejar de compartir`, notice `Grabación y transcripción`.
- **Open menus/windows:** Teams call controls at top, screen-share bar at bottom.

### 00932–00933
- **Window:** Windows Alt-Tab switcher
- **Selection/modification:** app switching only.
- **Action:** selecting a different window.
- **Visible thumbnails:** Excel workbook, Teams, File Explorer, reports/documents.

### 00934–00935
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 [Grupo]` → `Calificaciones Totales`
- **Selection/modification:** a cell in the central comparison table is active; the view is on the three side-by-side comparison blocks.
- **Action:** verifying/calculating locality scores across channels.
- **Visible data:**  
  - Left table: `Calificación de Localidades Canal Virtual`
  - Center: `Calificación Canal Presencial`
  - Right: `Calificación Canal Telefónico`
  - Readable values include `Antonio Nariño 269`, `Barrios Unidos 258`, `Bosa 185`, `Chapinero 169`, `Ciudad Bolívar 164`, `Engativá 174`
  - Score blocks show `4.0`, `5.0`, `4.8`, `4.9`
  - `Total general 4328` visible
- **Open menus/windows:** none besides Excel.

### 00936–00937
- **Workbook/sheet:** same workbook → `REGISTRO ATENCIONES`
- **Selection/modification:** PivotTable field pane open on the right.
- **Action:** configuring pivot fields / checking grouped counts.
- **Visible data:** pivot table `Registros por Atención Preferencial`, `Total general 4328`
- **Open menus/windows:** `Campos de tabla dinámica` pane with checkboxes like `Punto de atención`, `Nombre completo ciudadano`, `Grupo etario`, `Identidad de Género`, `Sexo`, `Orientación sexual`, `Fecha de atención`, `Atención preferencial`, `Canal de atención`.

### 00938–00942
- **Workbook/sheet:** same workbook → `REGISTRO ATENCIONES`
- **Selection/modification:** active cell moves inside the pivot/summary area (name box changes, e.g. around `E27`, `F27`, `AD46`-type positions).
- **Action:** checking formulas/fields; likely adjusting the pivot or verifying a calculated cell.
- **Visible data:** same pivot content; total remains `4328`.
- **Formula:** formula bar shows a multiplication/sum formula, but the exact text is not fully legible.
- **Open menus/windows:** PivotTable field pane still open.

### 00943–00947
- **Workbook/sheet:** back to `BD PORS BOGOTA TE ESCUCHA MAYO 2026` → `INFORME WEB ABRIL`
- **Selection/modification:** cursor over lower rows near the main table; one cell is active in the lower middle/right area.
- **Action:** navigating to the target rows for copy/verification.
- **Visible data:** same table header `Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`; chart placeholder label `Área del gráfico`.
- **Open menus/windows:** none.

### 00948–00950
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026 [Grupo]` → `Calificaciones Totales`
- **Selection/modification:** active cell in the right-side comparison table; then Alt-Tab appears at 00950.
- **Action:** horizontal verification of the comparative columns.
- **Visible data:** score blocks still around `4.8` / `4.9`; right-side percentages around `99%` and `100%`.
- **Open menus/windows:** 00950 shows Alt-Tab switcher.

### 00951–00959
- **Workbook/sheet:** `BD PORS BOGOTA TE ESCUCHA MAYO 2026` → `INFORME WEB ABRIL`
- **Selection/modification:** active cell moves across the lower table / blank area beside the summary.
- **Action:** continued checking of the same locality table.
- **Visible data:** same headers (`CERT. RESIDENCIA`, `PROPIEDAD HORIZONTAL`, `ORIENTACIONES`, `ENCUESTAS`, `DOC EXT.`); `Área del gráfico` label persists.
- **Open menus/windows:** none.

### 00960–00967
- **Workbook/sheet:** same workbook → `INFORME WEB ABRIL`
- **Selection/modification:** view shifts horizontally to the right side of the sheet.
- **Action:** scrolling/positioning to inspect the later columns and totals.
- **Visible data:** full title line `Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`; left columns still show the locality list and percentages.
- **Open menus/windows:** none.

### 00968–00987
- **Workbook/sheet:** same workbook → `INFORME WEB ABRIL`
- **Selection/modification:** active cell moves along the right-side table; no block selection.
- **Action:** continued review/verification of values.
- **Visible data:** same comparative table and totals; no new dialog.
- **Open menus/windows:** none.

### 00988–01000
- **Workbook/sheet:** back to `BASE DATOS PPT LOCALIDADES MAYO 2026 [Grupo]` → `Calificaciones Totales`
- **Selection/modification:** cells in the central/right comparison tables are selected while the sheet is horizontally scrolled.
- **Action:** final verification of computed totals and percentages.
- **Visible data:**  
  - left/center/right locality tables
  - values like `723`
  - score blocks `4.8`, `4.9`, `5.0`
  - rightmost percentages `99%`, `100%`
  - formula bar at 01000 shows a `SUMA(...)`-style formula with range references, but not fully legible
- **Open menus/windows:** none.

If you want, I can turn this into a cleaner **timecoded narration** for the full segment.

[Batch 11 - gpt-5.4-mini]
I grouped the identical-looking frames into 3 screen states.

### A) `BASE DATOS PPT LOCAIDADES MAYO 2026` → `Calificaciones Totales`
**Frames:** 01001, 01004, 01005, 01007, 01013, 01014, 01016, 01017, 01019, 01027, 01040, 01041, 01058, 01059, 01080, 01081, 01082, 01084, 01085, 01089, 01091, 01092, 01095, 01098, 01099, 01100

- **Workbook/sheet:** Excel workbook `BASE DATOS PPT LOCAIDADES MAYO 2026`, active sheet `Calificaciones Totales`.
- **Selection/action:** active cell moves within the yellow/green comparison tables; row-by-row verification/editing, not a dialog or sort/filter.
- **Visible data:** comparison blocks with locality names and scores like `4.8`, `4.9`, `5.0`; percentages `64.3%`, `13.5%`, `11%`, `9.8%`, `6.1%`; right-side locality list with `97%–100%`; chart placeholder text `Título del gráfico` / `Área del gráfico`.
- **Open windows/menus:** Teams screen-sharing bar (`teams.microsoft.com está compartiendo tu pantalla`), `Dejar de compartir`, and the participant tile `Yesenia Patino Figueroa`.

---

### B) `BD PQRS BOGOTA TE ESCUCHA MAYO 2026` → `INFORME WEB ABRIL`
**Frames:** 01002, 01003, 01006, 01008, 01009, 01010, 01011, 01012, 01015, 01018, 01020, 01021, 01022, 01023, 01024, 01025, 01026, 01028, 01029, 01030, 01031, 01032, 01033, 01034, 01035, 01036, 01037, 01038, 01039, 01042, 01043, 01044, 01045, 01046, 01047, 01048, 01049, 01050, 01051, 01052, 01053, 01054, 01055, 01056, 01057

- **Workbook/sheet:** Excel workbook `BD PQRS BOGOTA TE ESCUCHA MAYO 2026`, active sheet `INFORME WEB ABRIL`.
- **Selection/action:** reviewing totals in the main table; in several frames the active cell is around `K1063:K1071`; in `01035–01039` the pivot-table pane is open and the pivot summary is selected around `A1064`; in `01050` the formula bar clearly shows `=SUMA(K1042:K1070)`.
- **Visible data/text:**
  - Table title: `Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO`
  - Headers: `ALCALDIA LOCAL`, `PETICIONES RECIBIDAS POR LOCALIDAD DE LOS HECHOS`, `PORCENTAJE DE PARTICIPACION`, `CERT. RESIDENCIA`, `PROPIEDAD HORIZONTAL`, `ORIENTACIONES`, `ENCUESTAS`, `DOC EXT.`
  - Bottom total row shows `TOTAL GENERAL` and `100%`; the first total is visibly `81,539`.
  - Pivot summary on the left in some frames: `Cuenta de Número petición`, filter `PERIODO ACTUAL`, `SUPERCADES`.
- **Open windows/menus:** Teams share bar on all frames; in `01035–01039` the right-side `Campos de tabla dinámica` pane is open with fields like `Número petición`, `Duplicado`, `Sector`, `Tipo de entidad`, `Entidad`, `Dependencia`, `Tema`, plus areas `Filtros`, `Columnas`, `Filas`, `Valores`.
- **Transition notes:** `01008` is the Windows app switcher/task view; `01034–01039` and `01045–01050` show the pivot-table/field-list verification phase.

---

### C) `BASE DATOS PPT LOCAIDADES MAYO 2026` → final comparison sheet (`CERT RESIDENCIA PROD-MAYO` visible)
**Frames:** 01060, 01061, 01062, 01063, 01064, 01065, 01066, 01067, 01068, 01069, 01070, 01071, 01072, 01073, 01074, 01075, 01076, 01077, 01078, 01079, 01083, 01086, 01087, 01088, 01090, 01093, 01094, 01096, 01097

- **Workbook/sheet:** Excel workbook `BASE DATOS PPT LOCAIDADES MAYO 2026`; active tab appears to be `CERT RESIDENCIA PROD-MAYO` (neighbor tabs `Calificaciones Totales` and `CERT.P.HORIZONTL MAYO` are visible).
- **Selection/action:** row-by-row formula entry/checking in the highlighted comparison tables; active cell moves through rows around `A29`, `A30`, later other rows in the same block.
- **Visible data/text:**
  - Left block headers: `Calificación obtenida`, `Aporte a la Calificación Total`, `Calificación Canal Presencial Localidades`
  - Middle block headers: `Porcentaje de Percepción y Satisfacción`, `Número de encuestas realizadas`, `Localidad`, `Calificación obtenida`, `Aporte a la Calificación Total`, `Calificación Localidades`
  - Right block: `Localidad` + percentages (mostly `97%–100%`)
  - Repeated visible values: `723`, `4.8`, `4.9`, `5.0`, and percentage ladder `64.3%`, `13.5%`, `11%`, `9.8%`, `6.1%`
  - Localities visible include `Amazonia`, `Barrios Unidos`, `Bosa`, `Chapinero`, `Ciudad Bolívar`, `Engativá`, `Fontibón`, `Kennedy`, `La Candelaria`, `Los Mártires`, `Puente Aranda`, `Rafael Uribe Uribe`, `San Cristóbal`, `Santa Fe`, `Suba`, `Teusaquillo`, `Tunjuelito`, `Usaquén`, `Nivel Central`
  - `01073–01076` show the chart placeholder text `Área del gráfico`
- **Open windows/menus:** Teams share bar persists; `01078` is the Windows task switcher showing multiple Excel workbooks, Explorer, a browser/meeting window, and a document window.
- **Formula note:** the exact row formulas are visible only partially, but they are row-sum style additions feeding the comparison table.

If you want, I can turn this into a strict frame-by-frame CSV-style log next.

[Batch 12 - gpt-5.4-mini]
Grouped, because most frames are near-duplicates.

### 1) Workbook: `BD PQRS BOGOTA TE ESCUCHA MAYO 2026.xlsx`
**Sheet:** `INFORME WEB ABRIL`

- **Visible content:** green/red table titled `Tabla No. 12 PARTICIPACION POR LOCALIDAD...`
- **Columns visible:** `ALCALDIA LOCAL`, `PETICIONES RECIBIDAS...`, `PORCENTAJE DE PARTICIPACION`, `CERT. RESIDENCIA`, `PROPIEDAD HORIZONTAL`, `ORIENTACIONES`, `ENCUESTAS`, `DOC. EXT.`
- **Action:** user is selecting/moving through the `ORIENTACIONES` column and adjacent cells, likely preparing copy/paste or checking totals.
- **Selected range / cell:** active cell moves around the `K` column area; one frame clearly shows formula bar with `=SUMA(K1042:K1070)`. Other frames show name box changing around `K1063`, `K1064`, `K1065`, `K1069`, `K1070`, `K1071`.
- **Visible values:** a left side panel shows `Cuenta de Número petición?` with a list of decimal values; table rows show localities and totals, but most cell values are too small to read reliably.
- **Open UI:** Excel ribbon (`Inicio`, `Insertar`, `Fórmulas`, `Datos`, etc.) + Teams sharing bar at bottom (`Dejar de compartir`, `Ocultar`).

### 2) Workbook: `BASE DATOS PPT LOCALIDADES MAYO 2026.xlsx`
**Sheet:** `Calificaciones Totales`

- **Visible content:** two large comparison tables with yellow/green highlighted columns.
- **Headers visible:** `Calificación obtenida`, `Aporte a la Calificación total`, `Calificación Canal Presencial Localidades`, `Número de encuestas realizadas`, `Localidad`, and a right-side table with `Porcentaje de Percepción y Satisfacción`.
- **Visible localities:** `Antonio Nariño`, `Barrios Unidos`, `Bosa`, `Chapinero`, `Ciudad Bolívar`, `Engativá`, `Fontibón`, `Kennedy`, `La Candelaria`, `Los Mártires`, `Puente Aranda`, `Rafael Uribe Uribe`, `San Cristóbal`, `Santa Fe`, `Suba`, `Sumapaz`, `Teusaquillo`, `Tunjuelito`, `Usaquén`, `Nivel Central`.
- **Visible values:** aggregate scores like `5.0`, `4.9`, `4.8`; counts like `723` and `3915`; percentages such as `64.3%`, `13.5%`, and many `0.x%` entries.
- **Action:** selecting/adjusting cells in the right-side score tables, likely copying values to build the comparative sheet.
- **Selected range / cell:** name box changes around `AA53`, `AA27`, `AA29`, `AA49`; selection is in the right-side columns near the chart/table area.
- **Open UI:** Excel + Teams sharing bar at bottom. One frame shows tooltip `Área del gráfico`, meaning the cursor is over a chart object.

### 3) Window transition
- **Frames show Alt+Tab / task switcher**
- Open windows visible:
  - `BD PQRS BOGOTA TE ESCUCHA...`
  - `BASE DATOS PPT LOCALIDADES...`
  - `REPORTE ENCUESTAS MAYO 2026...`
  - `INFORME PQRS SECRETARIA DE G...`
  - `2026 - Explorador de archivos`
  - `Descargas - Explorador de archivos`
  - `ANALISIS INFORME PQRS RED QU...`
  - Teams sharing window
- **Meaning:** user is switching between workbooks/files while transferring or verifying data.

### Overall read of the segment
This is a **manual data migration / comparison / verification** phase: copying locality-based metrics from `BASE DATOS PPT LOCALIDADES` into the web-report workbook, checking totals, and confirming chart-linked ranges.

[Batch 13 - gpt-5.4-mini]
Here’s the frame-by-frame readout, exact where legible and marked when not.

### 01201–01202
- **Workbook/sheet:** `BASE DATOS PPT LOCALIDADES MAYO 2026` / **Calificaciones Totales**
- **Selection:** active cell appears to be **AA29**; formula bar shows a sum-like formula (too small to confirm fully).
- **Action:** reviewing a totals sheet; no visible typing.
- **Visible data:** locality score tables with yellow percentage column and green subtotal bands; one large locality list on the right.
- **Windows/menus:** Excel only.

### 01203–01205
- **Workbook/sheet:** same workbook, **REGISTRO ATENCIONES**
- **Selection:** a pivot-table cell is active (green outline); exact address not legible.
- **Action:** inspecting pivot tables / pivot fields.
- **Visible data:**  
  - Left pivot lists people/names with counts.  
  - Center table: **Registros por Atención Preferencial** with rows like *Ninguna, Persona Mayor, Persona con discapacidad física, intelectual-cognitiva, visual, psicosocial*, etc.
- **Windows/menus:** **Campos de tabla dinámica** pane open on the right.

### 01206
- **Transition:** Alt+Tab app switcher opens.
- **Visible windows:** multiple Excel workbooks, Teams share window, Explorer folders, and a document/PDF preview.
- **Action:** switching applications.

### 01207–01245
- **Workbook:** `BD PQRS BOGOTA T ESCUCHA MAYO 2026`
- **Sheet:** **INFORME WEB ABRIL**
- **Selection:** active cell moves through the report table; exact addresses mostly not legible. In some frames the formula bar shows a `SUMA(...)` over a locality range.
- **Action:** comparing/copying locality-level totals into the report table; no obvious dialog.
- **Visible data / structure:** main table titled **“Tabla No. 12 PARTICIPACION POR LOCALIDAD DE LOS REQUERIMIENTOS REGISTRADOS DURANTE EL PERIODO”** with columns:
  - **ALCALDIA LOCAL**
  - **PETICIONES RECIBIDAS POR LOCALIDAD DE LOS HECHOS**
  - **PORCENTAJE DE PARTICIPACIÓN**
  - **CERT. RESIDENCIA**
  - **PROPIEDAD HORIZONTAL**
  - **ORIENTACIONES**
  - **ENCUESTAS**
  - **DOC. EXT.**
- **Visible locality rows:** Usaquén, Chapinero, Santa Fe, San Cristóbal, Usme, Tunjuelito, Bosa, Kennedy, Fontibón, Engativá, Suba, Barrios Unidos, Teusaquillo, Los Mártires, Antonio Nariño, Puente Aranda, La Candelaria, Rafael Uribe Uribe, Ciudad Bolívar, Sumapaz.
- **Visible totals:** total general **10,539** and **100.00%**; category totals visible include roughly **6,983** (cert. residencia), **803** (propiedad horizontal), **4,328** (orientaciones). Far-right total is visible but too small to read confidently.
- **Windows/menus:** Teams floating bar appears: **“Dejar de compartir / Ocultar”**.

### 01246–01251
- **Workbook/sheet:** same workbook, still **INFORME WEB ABRIL**
- **Action:** scrolling down through report sections.
- **Visible sections:**
  - **CAPITULO 11. PARTICIPACION POR ESTRATO**
  - Pie chart titled **“GRAFICA No. 1 PARTICIPACION POR ESTRATO”**
  - **CAPITULO 13. ATENCIONES POR GRUPO POBLACIONAL (Tomado del registro de atenciones ciudadanas)**
- **Visible data:** stratification table (Estrato 1–6) and a group-population list including *Ninguna, Persona Mayor, Persona con discapacidad física, intelectual-cognitiva, visual, psicosocial, múltiple, comunidad afro*, etc.
- **Windows/menus:** Excel + Teams share bar.

### 01252–01259
- **Workbook/sheet:** same report workbook, **INFORME WEB ABRIL**
- **Action:** viewing summary charts and pivot blocks.
- **Visible data:**  
  - Left pivot: **TOTAL PETICIONES RECIBIDAS...**
  - Filters: **Tipo de ingreso**, **Periodo ACTUAL**
  - Charts:
    - **Gráfica No. 1 Total Peticiones del Mes**
    - horizontal bars for **VERDADERO / FALSO**
    - another bar chart with **Propia / Por el ciudadano**
  - Lower section: **DISTRIBUCIÓN DE PQRS POR SEXO**
  - Another section: **CAPITULO 11. TIPOLOGÍA O MODALIDADES**
- **Windows/menus:** Excel only plus Teams share bar.

### 01260–01267
- **Transition:** Excel view disappears.
- **Visible window:** black Teams-style placeholder with centered circular avatar and name **Yesenia Patiño Figueroa**.
- **Action:** end/transition state; no spreadsheet visible.

If you want, I can turn this into a **CSV-style frame log** next.

---
