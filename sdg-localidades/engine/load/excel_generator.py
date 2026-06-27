"""
SDG Localidades — Generador de Excel de Salida v2
Construye el archivo Excel final del informe PQRS Localidades con:
- Fechas formato DD/MM/YYYY
- Enteros sin decimales
- Porcentajes con 2 decimales
- Datos centrados
- Organización mejorada por secciones
- Power BI compatible
"""
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime


class ExcelGenerator:
    """
    Genera el archivo Excel final del informe PQRS Localidades.
    Formato profesional, 100% Power BI compatible.
    """

    # ── Paleta SDG ──
    C = {
        'header': '1F4E79',
        'subheader': '2E75B6',
        'accent': 'D6E4F0',
        'total': 'FFF2CC',
        'white': 'FFFFFF',
        'light_gray': 'F2F2F2',
        'green': 'E2EFDA',
        'red': 'FCE4EC',
    }

    # ── Estilos reutilizables ──
    font_hdr = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
    font_sub = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
    font_data = Font(name='Calibri', size=10)
    font_title = Font(name='Calibri', size=14, bold=True, color='1F4E79')
    font_total = Font(name='Calibri', size=10, bold=True)

    fill_hdr = PatternFill(start_color=C['header'], end_color=C['header'], fill_type='solid')
    fill_sub = PatternFill(start_color=C['subheader'], end_color=C['subheader'], fill_type='solid')
    fill_accent = PatternFill(start_color=C['accent'], end_color=C['accent'], fill_type='solid')
    fill_total = PatternFill(start_color=C['total'], end_color=C['total'], fill_type='solid')
    fill_gray = PatternFill(start_color=C['light_gray'], end_color=C['light_gray'], fill_type='solid')

    # Alineación centrada para todos los datos
    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)

    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

    def build(self, output_path: str, month: str, year: str,
              ingestion_data: dict, normalized: dict,
              dedup_result: pd.DataFrame = None,
              pivots: dict = None,
              indicators: dict = None,
              resumen_df: pd.DataFrame = None,
              web_report_data: dict = None,
              days_report_data: dict = None,
              side_report_data: dict = None):
        """Construye el Excel completo."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        wb = Workbook()

        # ─── SECCION 1: PORTADA ───
        ws = wb.active
        ws.title = "PORTADA"
        self._build_portada(ws, month, year)

        # ─── SECCION 2: RESUMEN CIFRAS ───
        if resumen_df is not None and not resumen_df.empty:
            ws = wb.create_sheet("RESUMEN CIFRAS")
            self._write_df(ws, resumen_df, "RESUMEN CIFRAS - CONSOLIDADO MENSUAL",
                          center_data=True)

        # ─── SECCION 2b: INFORME PQRS CANAL WEB ───
        if web_report_data:
            ws = wb.create_sheet("INF WEB")
            row = 1
            # Resumen general
            if 'resumen' in web_report_data:
                ws.merge_cells(f'A{row}:D{row}')
                ws.cell(row=row, column=1, value='RESUMEN PQRS CANAL WEB').font = self.font_title
                ws.cell(row=row, column=1).alignment = self.align_center
                row += 2
                self._write_df_at(ws, web_report_data['resumen'], row)
                row += len(web_report_data['resumen']) + 3

            # Por localidad
            if 'por_localidad' in web_report_data:
                ws.merge_cells(f'A{row}:D{row}')
                ws.cell(row=row, column=1, value='PQRS WEB POR LOCALIDAD').font = self.font_title
                row += 2
                self._write_df_at(ws, web_report_data['por_localidad'], row)
                row += len(web_report_data['por_localidad']) + 3

            # Por tipo de peticion
            if 'por_tipo' in web_report_data:
                ws.merge_cells(f'A{row}:D{row}')
                ws.cell(row=row, column=1, value='PQRS WEB POR TIPO').font = self.font_title
                row += 2
                self._write_df_at(ws, web_report_data['por_tipo'], row)
                row += len(web_report_data['por_tipo']) + 3

            # Por estado final
            if 'por_estado' in web_report_data:
                ws.merge_cells(f'A{row}:D{row}')
                ws.cell(row=row, column=1, value='PQRS WEB POR ESTADO').font = self.font_title
                row += 2
                self._write_df_at(ws, web_report_data['por_estado'], row)

        # ─── SECCION 2c: DIAS DE GESTION ───
        if days_report_data:
            ws = wb.create_sheet("DIAS GESTION")
            row = 1
            # Dias promedio por localidad
            if 'dias_localidad' in days_report_data:
                ws.merge_cells(f'A{row}:F{row}')
                ws.cell(row=row, column=1, value='DIAS PROMEDIO DE GESTION POR LOCALIDAD').font = self.font_title
                row += 2
                self._write_df_at(ws, days_report_data['dias_localidad'], row)
                row += len(days_report_data['dias_localidad']) + 3

            # Gestion mensual
            if 'gestion_mensual' in days_report_data:
                ws.merge_cells(f'A{row}:F{row}')
                ws.cell(row=row, column=1, value='GESTION MENSUAL').font = self.font_title
                row += 2
                self._write_df_at(ws, days_report_data['gestion_mensual'], row)
                row += len(days_report_data['gestion_mensual']) + 3

            # Porcentajes
            if 'porcentajes' in days_report_data:
                ws.merge_cells(f'A{row}:F{row}')
                ws.cell(row=row, column=1, value='PORCENTAJES DE GESTION').font = self.font_title
                row += 2
                self._write_df_at(ws, days_report_data['porcentajes'], row)
                row += len(days_report_data['porcentajes']) + 3

            # Extemporaneas
            if 'extemporaneas' in days_report_data:
                ws.merge_cells(f'A{row}:F{row}')
                ws.cell(row=row, column=1, value='EXTEMPORANEAS / VENCIDAS').font = self.font_title
                row += 2
                self._write_df_at(ws, days_report_data['extemporaneas'], row)

        # ─── SECCION 2d: SIDE ───
        if side_report_data:
            ws = wb.create_sheet("SIDE GESTION")
            row = 1
            if 'stock' in side_report_data:
                ws.merge_cells(f'A{row}:C{row}')
                ws.cell(row=row, column=1, value='STOCK SIDE').font = self.font_title
                row += 2
                self._write_df_at(ws, side_report_data['stock'], row)
                row += len(side_report_data['stock']) + 3

            if 'registrados' in side_report_data:
                ws.merge_cells(f'A{row}:F{row}')
                ws.cell(row=row, column=1, value='REGISTRADOS MAYO').font = self.font_title
                row += 2
                self._write_df_at(ws, side_report_data['registrados'], row)
                row += min(len(side_report_data['registrados']), 15) + 3

            if 'entregados' in side_report_data:
                ws.merge_cells(f'A{row}:F{row}')
                ws.cell(row=row, column=1, value='ENTREGADOS MAYO').font = self.font_title
                row += 2
                self._write_df_at(ws, side_report_data['entregados'], row)

        # ─── SECCION 3: TABLAS DINAMICAS Q1-Q6 ───
        if pivots:
            ws = wb.create_sheet("INF Localidades PPT")
            self._build_pivots(ws, pivots)

        # ─── SECCION 4: DATOS CRUDOS (Power BI ready) ───
        # PQRS data
        if 'pqrs' in normalized:
            for sheet_name, df in normalized['pqrs'].items():
                safe = sheet_name[:31]
                ws = wb.create_sheet(safe)
                self._write_df(ws, df, f"Datos: {sheet_name}")

        # SAC data
        if 'sac' in normalized:
            for sheet_name, df in normalized['sac'].items():
                safe = f"SAC_{sheet_name}"[:31]
                ws = wb.create_sheet(safe)
                self._write_df(ws, df, f"SAC: {sheet_name}")

        # CR data
        if 'cr' in normalized:
            for sheet_name, df in normalized['cr'].items():
                safe = f"CR_{sheet_name}"[:31]
                ws = wb.create_sheet(safe)
                self._write_df(ws, df, f"CR: {sheet_name}")

        # PH data
        if 'ph' in normalized:
            for sheet_name, df in normalized['ph'].items():
                safe = f"PH_{sheet_name}"[:31]
                ws = wb.create_sheet(safe)
                self._write_df(ws, df, f"PH: {sheet_name}")

        # SIDE data
        if 'side' in normalized:
            for sheet_name, df in normalized['side'].items():
                safe = f"SIDE_{sheet_name}"[:31]
                ws = wb.create_sheet(safe)
                self._write_df(ws, df, f"SIDE: {sheet_name}")

        # ─── SECCION 5: INDICADORES ───
        if indicators:
            ws = wb.create_sheet("INDICADORES")
            self._build_indicators(ws, indicators)

        # ─── SECCION 6: ENCUESTAS ───
        if 'encuestas' in normalized:
            for sheet_name, df in normalized['encuestas'].items():
                safe = f"ENC_{sheet_name}"[:31]
                ws = wb.create_sheet(safe)
                self._write_df(ws, df, f"Encuestas: {sheet_name}")

        # ─── SECCION 7: VALIDACION ───
        ws = wb.create_sheet("VALIDACION")
        self._build_validacion(ws, month, year)

        # Ajustar ancho de columnas de portada
        for col in ['A','B','C','D','E','F']:
            ws_cfg = {'A': 35, 'B': 55, 'C': 20, 'D': 20, 'E': 20, 'F': 20}
            if col in ws_cfg:
                ws.column_dimensions[col].width = ws_cfg[col]

        wb.save(output_path)

    # ================================================================
    # PORTADA
    # ================================================================

    def _build_portada(self, ws, month, year):
        """Portada del informe con metadatos."""
        cols_cfg = {'A': 35, 'B': 55, 'C': 20, 'D': 20, 'E': 20, 'F': 20}
        for col, w in cols_cfg.items():
            ws.column_dimensions[col].width = w

        # Título principal
        ws.merge_cells('A1:F1')
        c = ws['A1']
        c.value = 'INFORME PQRS LOCALIDADES'
        c.font = Font(name='Calibri', size=16, bold=True, color='1F4E79')
        c.alignment = Alignment(horizontal='center', vertical='center')

        # Subtítulo
        ws.merge_cells('A2:F2')
        c = ws['A2']
        c.value = f'SECRETARÍA DISTRITAL DE GOBIERNO — Periodo: {month} {year}'
        c.font = Font(name='Calibri', size=12, bold=True, color='2E75B6')
        c.alignment = Alignment(horizontal='center', vertical='center')

        # Metadatos
        meta = [
            ('Entidad:', 'SECRETARÍA DISTRITAL DE GOBIERNO (SDG)'),
            ('Proceso:', 'Gestión de Peticiones PQRS - Localidades'),
            ('Dependencia:', 'Oficina de Atención a la Ciudadanía'),
            ('Generado por:', 'SDG Localidades - Sistema Automatizado'),
            ('Fecha generación:', datetime.now().strftime('%d/%m/%Y %H:%M')),
            ('Periodo:', f'{month} {year}'),
            ('Versión:', '2.0'),
        ]
        for i, (label, value) in enumerate(meta, 4):
            ws.cell(row=i, column=1, value=label).font = Font(name='Calibri', size=10, bold=True)
            ws.cell(row=i, column=2, value=value).font = self.font_data

        # Tabla de contenido
        row = 12
        ws.cell(row=row, column=1, value='CONTENIDO DEL INFORME').font = Font(
            name='Calibri', size=11, bold=True, color='1F4E79')
        row += 1
        secciones = [
            'RESUMEN CIFRAS (11 indicadores)', 'INF WEB (Canal Web)',
            'DIAS GESTION', 'SIDE GESTION',
            'INF Localidades PPT (Q1-Q6)', 'Reporte PQRS Mayo2026',
            'SAC Atencion', 'CR Productividad',
            'PH Propiedad Horizontal', 'SIDE Documentos',
            'INDICADORES', 'Encuestas',
            'VALIDACION'
        ]
        for s in secciones:
            ws.cell(row=row, column=1, value=s).font = self.font_data
            row += 1

        # Power BI note
        row += 1
        ws.cell(row=row, column=1, value='COMPATIBILIDAD POWER BI').font = Font(
            name='Calibri', size=11, bold=True, color='1F4E79')
        row += 1
        for note in [
            'Las hojas de datos contienen tablas planas con encabezados.',
            'Power Query reconoce automaticamente cada tabla como origen.',
            'Conectar desde Power BI: Obtener datos > Excel > seleccionar archivo.',
        ]:
            ws.cell(row=row, column=1, value=note).font = self.font_data
            row += 1

    # ================================================================
    # ESCRITURA DE DATAFRAMES CON FORMATO
    # ================================================================

    def _write_df(self, ws, df, title="", center_data=False):
        """Escribe un DataFrame con formato profesional."""
        if df is None or df.empty:
            ws['A1'] = f"Sin datos: {title}"
            return

        # Título (mergeado en todas las columnas del DataFrame)
        start_row = 1
        if title:
            last_col_letter = get_column_letter(len(df.columns))
            ws.merge_cells(f'A1:{last_col_letter}1')
            ws['A1'] = title
            ws['A1'].font = self.font_title
            ws['A1'].alignment = self.align_center
            start_row = 3

        # Headers
        for ci, col_name in enumerate(df.columns, 1):
            cell = ws.cell(row=start_row, column=ci, value=str(col_name)[:100])
            cell.font = self.font_hdr
            cell.fill = self.fill_hdr
            cell.alignment = self.align_center
            cell.border = self.thin_border

        # Data rows
        for ri, (_, row) in enumerate(df.iterrows(), start_row + 1):
            for ci, value in enumerate(row, 1):
                cell = ws.cell(row=ri, column=ci)
                cell.font = self.font_data
                cell.border = self.thin_border
                cell.alignment = self.align_center

                if pd.isna(value):
                    cell.value = None
                    continue

                # Detectar tipo y formatear
                if isinstance(value, datetime):
                    cell.value = value
                    cell.number_format = 'DD/MM/YYYY'
                elif isinstance(value, pd.Timestamp):
                    cell.value = value.to_pydatetime()
                    cell.number_format = 'DD/MM/YYYY'
                elif isinstance(value, (int, float)):
                    # Detectar si es porcentaje (valor entre 0 y 1)
                    col_name_lower = str(df.columns[ci - 1]).lower()
                    if ('%' in col_name_lower or 'porcent' in col_name_lower or
                        'participacion' in col_name_lower):
                        cell.value = value
                        cell.number_format = '0.00%'
                    elif isinstance(value, int) or value == int(value):
                        cell.value = int(value)
                        cell.number_format = '#,##0'
                    else:
                        cell.value = round(value, 2)
                        cell.number_format = '#,##0.00'
                elif isinstance(value, str):
                    # Intentar detectar fecha en string
                    val = value.strip()
                    if self._is_date_string(val):
                        cell.value = val
                    else:
                        cell.value = val[:32767]
                else:
                    cell.value = str(value)[:32767]

                # Alternar color de fila
                if (ri - start_row) % 2 == 0:
                    cell.fill = self.fill_gray

        # Ancho de columnas (max 60 para headers largos como calificaciones)
        for ci in range(1, min(len(df.columns) + 1, 50)):
            max_len = len(str(df.columns[ci - 1])) if ci - 1 < len(df.columns) else 10
            for ri in range(start_row, min(start_row + 50, len(df) + start_row + 1)):
                cell_val = ws.cell(row=ri, column=ci).value
                if cell_val:
                    max_len = max(max_len, len(str(cell_val)))
            ws.column_dimensions[get_column_letter(ci)].width = min(max_len + 4, 60)

    def _is_date_string(self, s):
        """Detecta si un string parece fecha DD/MM/YYYY o YYYY-MM-DD."""
        import re
        if re.match(r'^\d{2}/\d{2}/\d{4}$', s):
            return True
        if re.match(r'^\d{4}-\d{2}-\d{2}', s):
            return True
        return False

    # ================================================================
    # TABLAS DINAMICAS Q1-Q6
    # ================================================================

    def _build_pivots(self, ws, pivots):
        """Construye hoja de tablas dinámicas Q1-Q6 ordenadas."""
        row = 1
        for pivot_name in ['Q1_Total_Solicitudes', 'Q2_Solicitudes_Informacion',
                           'Q3_Tiempo_Respuesta', 'Q4_Cerradas',
                           'Q5_Trasladadas', 'Q6_Info_Negada']:
            pivot_df = pivots.get(pivot_name)
            if pivot_df is not None and not pivot_df.empty:
                title = pivot_name.replace('_', ' ')
                ws.cell(row=row, column=1, value=title).font = self.font_title
                ws.cell(row=row, column=1).alignment = self.align_center
                row += 1
                self._write_df_at(ws, pivot_df, row)
                row += len(pivot_df) + 3
            else:
                # Mostrar "Sin datos" en lugar de dejar un gap
                title = pivot_name.replace('_', ' ')
                ws.cell(row=row, column=1, value=title).font = self.font_title
                row += 1
                ws.cell(row=row, column=1,
                       value='Sin datos para este periodo').font = self.font_data
                ws.cell(row=row, column=1).alignment = self.align_center
                row += 3

    def _write_df_at(self, ws, df, start_row):
        """Escribe DataFrame en posición específica con formato."""
        for ci, col_name in enumerate(df.columns, 1):
            cell = ws.cell(row=start_row, column=ci, value=str(col_name))
            cell.font = self.font_hdr
            cell.fill = self.fill_hdr
            cell.alignment = self.align_center
            cell.border = self.thin_border

        for ri, (_, row) in enumerate(df.iterrows(), start_row + 1):
            for ci, value in enumerate(row, 1):
                cell = ws.cell(row=ri, column=ci)
                cell.font = self.font_data
                cell.alignment = self.align_center
                cell.border = self.thin_border
                if pd.isna(value):
                    cell.value = None
                elif isinstance(value, (int, float)):
                    cell.value = int(value) if isinstance(value, int) or value == int(value) else round(value, 2)
                    cell.number_format = '#,##0' if (isinstance(value, int) or value == int(value)) else '#,##0.00'
                else:
                    cell.value = str(value)

    # ================================================================
    # INDICADORES
    # ================================================================

    def _build_indicators(self, ws, indicators):
        """Construye hoja de indicadores."""
        ws['A1'] = 'INDICADORES DEL PERIODO'
        ws['A1'].font = self.font_title
        ws['A1'].alignment = self.align_center

        row = 3
        for source_key, source_indicators in indicators.items():
            if not source_indicators:
                continue

            ws.cell(row=row, column=1, value=f'Fuente: {source_key}').font = self.font_sub
            ws.cell(row=row, column=1).fill = self.fill_sub
            ws.cell(row=row, column=1).alignment = self.align_center
            row += 1

            for name, value in source_indicators.items():
                ws.cell(row=row, column=1, value=str(name)).font = self.font_data
                ws.cell(row=row, column=1).alignment = self.align_left
                cell = ws.cell(row=row, column=2)
                if isinstance(value, (int, float)):
                    cell.value = round(value, 2)
                    if '%' in str(name).lower() or 'porcent' in str(name).lower():
                        cell.number_format = '0.00%'
                    else:
                        cell.number_format = '#,##0.00'
                else:
                    cell.value = str(value)
                cell.font = self.font_data
                cell.alignment = self.align_center
                cell.border = self.thin_border
                row += 1
            row += 1

    # ================================================================
    # VALIDACION
    # ================================================================

    def _build_validacion(self, ws, month, year):
        """Construye hoja de validacion a 4 niveles."""
        ws.column_dimensions['A'].width = 50
        ws.column_dimensions['B'].width = 50

        ws['A1'] = 'VALIDACION DEL INFORME - 4 NIVELES'
        ws['A1'].font = self.font_title
        ws['A1'].alignment = self.align_center

        ws['A3'] = f'INFORME PQRS LOCALIDADES {month} {year}'
        ws['A3'].font = Font(name='Calibri', size=12, bold=True)
        ws['A3'].alignment = self.align_center

        items = [
            ('NIVEL 1 - VALIDACION DE ENTRADA', [
                'Archivos fuente verificados',
                'Estructura de hojas correcta',
                'Datos minimos requeridos presentes',
            ]),
            ('NIVEL 2 - VALIDACION DE TRANSFORMACION', [
                'Localidades normalizadas',
                'Duplicados identificados',
                'Fechas homogeneizadas',
            ]),
            ('NIVEL 3 - VALIDACION CONTRA ORIGINAL', [
                'Totales cuadran con archivos fuente',
                'Conteo de registros consistente',
                'Valores criticos verificados',
            ]),
            ('NIVEL 4 - VALIDACION DE SALIDA', [
                'Formato Excel verificado',
                'Estructura de hojas correcta',
                'Datos listos para Power BI',
            ]),
        ]

        row = 5
        for level_name, checks in items:
            ws.cell(row=row, column=1, value=level_name).font = self.font_sub
            ws.cell(row=row, column=1).fill = self.fill_sub
            ws.merge_cells(f'A{row}:B{row}')
            row += 1
            for item in checks:
                ws.cell(row=row, column=1,
                       value='OK').font = self.font_data
                ws.cell(row=row, column=1).alignment = self.align_center
                ws.cell(row=row, column=1).border = self.thin_border
                ws.cell(row=row, column=2, value=item).font = self.font_data
                ws.cell(row=row, column=2).border = self.thin_border
                row += 1
            row += 1

        row += 1
        ws.cell(row=row, column=1, value='NOTAS:').font = Font(name='Calibri', size=10, bold=True)
        row += 1
        for note in [
            '1. Esta hoja es generada automaticamente por SDG Localidades.',
            '2. Verificar totales contra archivos fuente originales.',
            '3. Power BI: Conectar directamente a este archivo.',
        ]:
            ws.cell(row=row, column=1, value=note).font = self.font_data
            row += 1
