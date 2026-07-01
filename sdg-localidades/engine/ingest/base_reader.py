"""
SDG Localidades — Reader base para archivos fuente v2
Ofrece limpieza post-lectura: deteccion de headers, "Etiquetas de fila",
columnas Unnamed, deteccion de tablas multiples, normalizacion general.
"""
import os
import re
import pandas as pd
from typing import Optional


class BaseReader:
    """
    Clase base para todos los readers de archivos fuente.
    Cada reader especializado hereda de esta clase.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)

    def read(self) -> 'IngestionResult':
        raise NotImplementedError("Cada reader debe implementar read()")

    def read_sheet(self, sheet_name: str, header_row: int = 0,
                   skip_rows: int = 0, usecols: Optional[list] = None) -> pd.DataFrame:
        """Lee una hoja especifica del Excel con pandas."""
        try:
            df = pd.read_excel(
                self.file_path, sheet_name=sheet_name,
                header=header_row, skiprows=skip_rows,
                usecols=usecols, dtype=str
            )
            df.columns = [str(c).strip() if c is not None else f"col_{i}"
                         for i, c in enumerate(df.columns)]
            return df
        except Exception:
            df = pd.read_excel(
                self.file_path, sheet_name=sheet_name,
                header=header_row, skiprows=skip_rows, usecols=usecols
            )
            return df

    # ═══════════════════════════════════════════════════════════════
    # LIMPIEZA POST-LECTURA (core)
    # ═══════════════════════════════════════════════════════════════

    def clean_sheet(self, df: pd.DataFrame, sheet_name: str = '') -> pd.DataFrame:
        """
        Limpia y normaliza un DataFrame leido de una hoja Excel.
        Aplica en orden:
        1. Elimina filas/columnas totalmente vacias
        2. Renombra 'Etiquetas de fila' -> 'Localidad'
        3. Si columnas son 0,1,2... -> auto-detecta headers
        4. Si primeras filas son titulos -> busca header real
        5. Elimina columnas 'Unnamed: N' sin datos
        6. Elimina filas totalmente NaN residuales
        """
        if df is None or df.empty:
            return df

        df = df.copy()

        # ── 1. Eliminar filas/columnas vacias ──
        # Solo eliminar filas vacias al INICIO y FINAL, preservando
        # las filas vacias INTERMEDIAS que separan multiples tablas.
        while len(df) > 0 and df.iloc[0].isna().all():
            df = df.iloc[1:].reset_index(drop=True)
        while len(df) > 0 and df.iloc[-1].isna().all():
            df = df.iloc[:-1].reset_index(drop=True)
        if df.empty:
            return df
        # Conservar filas vacias intermedias (separadores de tablas)
        # Columnas totalmente vacias solo al inicio
        non_empty_cols = [c for c in df.columns if not df[c].dropna().empty]
        if non_empty_cols and len(non_empty_cols) < len(df.columns):
            df = df[non_empty_cols]

        if df.empty or len(df.columns) == 0:
            return df

        # ── 2. Renombrar 'Etiquetas de fila' -> 'Localidad' ──
        cols = list(df.columns)
        renamed = False
        for i, c in enumerate(cols):
            c_str = str(c).strip().upper()
            if 'ETIQUETAS' in c_str or c_str == 'ETIQUETAS DE FILA' or c_str == 'ETIQUETAS DE COLUMNA':
                cols[i] = 'Localidad'
                renamed = True
        if renamed:
            df.columns = cols

        # ── 3. Si columnas son numericas -> auto-detect ──
        if self._all_numeric_cols(df):
            df = self._auto_detect_headers(df)

        # ── 4. Si primeras filas son titulos (PRODUCTIVIDAD, etc.) ──
        if len(df) > 0:
            df = self._find_real_header(df)

        # ── 5. Eliminar columnas 'Unnamed: N' SIN datos ──
        unnamed_cols = [c for c in df.columns
                       if str(c).strip().startswith('Unnamed:') or str(c).strip().startswith('Unnamed:')]
        for c in unnamed_cols:
            if df[c].dropna().empty:
                df = df.drop(columns=[c])

        # ── 6. Post-limpieza: renombrar si quedo algo ──
        cols = list(df.columns)
        for i, c in enumerate(cols):
            c_str = str(c).strip().upper()
            if 'ETIQUETAS' in c_str:
                cols[i] = 'Localidad'
            # 'NAN' string como nombre de columna
            if c_str == 'NAN' or c_str == 'NONE' or c_str == '':
                cols[i] = f'Columna {i+1}'
        df.columns = cols

        return df.reset_index(drop=True)

    # ═══════════════════════════════════════════════════════════════
    # HELPERS DE DETECCION
    # ═══════════════════════════════════════════════════════════════

    def _all_numeric_cols(self, df: pd.DataFrame) -> bool:
        """Verifica si todos los nombres de columna son numericos (0,1,2...)."""
        for c in df.columns:
            try:
                int(str(c).strip())
            except (ValueError, TypeError):
                return False
        return True

    def _auto_detect_headers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cuando las columnas son 0,1,2..., busca la mejor fila para
        promover a encabezados reales.
        """
        best_row, best_score = 0, 0
        for i in range(min(30, len(df))):
            row = df.iloc[i]
            vals = [str(v).strip() for v in row if pd.notna(v)]
            text_count = sum(1 for v in vals if len(v) > 2
                           and not v.replace('.', '').replace(',', '').replace('-', '').isdigit()
                           and v.upper() not in ('NAN', 'NONE', '', 'TOTAL'))
            filled = row.notna().sum()
            score = filled * (2 if text_count >= 2 else 1)
            if score > best_score:
                best_score = score
                best_row = i

        if best_score >= 3:
            new_cols = []
            has_meaningful = False
            for v in df.iloc[best_row]:
                vv = str(v).strip()[:100] if pd.notna(v) else ''
                if vv and vv.upper() not in ('NAN', 'NONE', '', 'TOTAL'):
                    new_cols.append(vv)
                    has_meaningful = True
                else:
                    new_cols.append(f'Columna {len(new_cols) + 1}')
            if has_meaningful:
                ndf = df.iloc[best_row + 1:].reset_index(drop=True)
                ndf.columns = new_cols
                # Post-fix: si col0 quedo como "Columna 1" pero sus datos
                # son nombres de localidad -> renombrar a "Localidad"
                if len(ndf) > 0 and len(new_cols) > 0 and 'localidad' not in new_cols[0].lower():
                    first_vals = ndf.iloc[:10, 0].fillna('').astype(str).str.upper().tolist()
                    localidad_count = sum(
                        1 for v in first_vals
                        if 'ALCALDIA' in v or 'OFICINA' in v or 'LOCALIDAD' in v
                    )
                    if localidad_count >= 2:
                        new_cols[0] = 'Localidad'
                        ndf.columns = new_cols
                return ndf

        return df

    def _find_real_header(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Si las primeras filas contienen titulos (PRODUCTIVIDAD DE..., etc.),
        busca la fila que tiene 'LOCALIDAD' o 'APROBADO' o 'PENDIENTE'
        y la promueve a header.
        """
        for i in range(min(15, len(df))):
            row_vals = [str(v).strip().upper() for v in df.iloc[i] if pd.notna(v)]
            has_localidad = any('LOCALIDAD' in v for v in row_vals)
            has_aprobado = any('APROBADO' in v for v in row_vals)
            has_pendiente = any('PENDIENTE' in v for v in row_vals)
            has_tipo_doc = any('TIPO DE DOCUMENTO' in v or 'TIPO DOCUMENTO' in v for v in row_vals)

            is_header = has_localidad or (has_aprobado and has_pendiente) or has_tipo_doc

            # Tambien detectar: primera columna con codigo numerico tipo "1 - NOMBRE"
            if not is_header and i > 0:
                first_val = str(df.iloc[i, 0]).strip() if pd.notna(df.iloc[i, 0]) else ''
                if re.match(r'^\d+\s*-\s*\w', first_val):
                    is_header = True

            if is_header:
                new_cols = [str(v).strip()[:100] if pd.notna(v) else f'Col_{j}'
                           for j, v in enumerate(df.iloc[i])]
                df.columns = new_cols
                df = df.iloc[i + 1:].reset_index(drop=True)
                break

        return df

    # ═══════════════════════════════════════════════════════════════
    # DETECCION DE TABLAS MULTIPLES
    # ═══════════════════════════════════════════════════════════════

    def detect_tables(self, df_raw: pd.DataFrame) -> list:
        """
        Detecta multiples tablas separadas por filas vacias en una hoja.
        Retorna lista de DataFrames (cada uno ya limpiado con clean_sheet).
        """
        tables = []
        data = df_raw.values.tolist()

        in_table = False
        table_start = None

        for i, row in enumerate(data):
            filled = sum(1 for c in row if pd.notna(c) and str(c).strip())
            if not in_table and filled >= 2:
                has_text = any(
                    len(str(c).strip()) > 3
                    and not str(c).strip().replace('.', '').replace(',', '').replace('-', '').isdigit()
                    for c in row if pd.notna(c)
                )
                if has_text:
                    in_table = True
                    table_start = i
            elif in_table and filled == 0:
                if table_start is not None and i - table_start >= 2:
                    tbl = df_raw.iloc[table_start:i].copy().reset_index(drop=True)
                    tbl = self.clean_sheet(tbl)
                    if tbl is not None and not tbl.empty and len(tbl.columns) >= 2:
                        tables.append(tbl)
                in_table = False
                table_start = None

        # Cerrar ultima tabla
        if in_table and table_start is not None and len(df_raw) - table_start >= 2:
            tbl = df_raw.iloc[table_start:].copy().reset_index(drop=True)
            tbl = self.clean_sheet(tbl)
            if tbl is not None and not tbl.empty and len(tbl.columns) >= 2:
                tables.append(tbl)

        return tables
