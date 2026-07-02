"""
SDG Localidades — Reader: Resumen SIDE
Sistema de Información de Documentos Extraviados.
3 hojas: STOCK (inventario), REGISTRADO (nuevos registros), ENTREGADO (entregas).

CADA HOJA TIENE ESTRUCTURA DISTINTA — NO USAR clean_sheet generico.
- STOCK: tabla simple 2 columnas -> clean_sheet funciona bien
- REGISTRADO SIDE: cabecera combinada (fila 0 titulo + columnas, fila 1 subtipo)
- ENTREGADO SIDE: DOS tablas (ENTREGADOS + DEVUELTOS) en una misma hoja
"""
import pandas as pd
from engine.models import IngestionResult
from engine.ingest.base_reader import BaseReader


class SIDEWriter(BaseReader):
    """Lee el archivo Resumen SIDE Mayo 2026.xlsx"""

    def read(self) -> IngestionResult:
        result = IngestionResult(source_key="side", success=False)

        try:
            xl = pd.ExcelFile(self.file_path)
        except Exception as e:
            result.errors.append(f"Error abriendo archivo SIDE: {str(e)}")
            return result

        for sheet_name in xl.sheet_names:
            try:
                df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)
                sheet_lower = sheet_name.lower().strip()

                if 'stock' in sheet_lower:
                    df = self.clean_sheet(df_raw, sheet_name)

                elif 'registrado' in sheet_lower:
                    df = self._read_registrado(df_raw)

                elif 'entregado' in sheet_lower:
                    # Tabla 1: ENTREGADOS
                    df_ent = self._read_entregado(df_raw)
                    if df_ent is not None and not df_ent.empty:
                        result.sheets[f"{sheet_name}"] = df_ent
                        result.row_count += len(df_ent)

                    # Tabla 2: DEVUELTOS (via detect_tables, excluida de metricas)
                    tables = self.detect_tables(df_raw)
                    for tbl in tables:
                        if tbl is not None and not tbl.empty and len(tbl.columns) >= 2:
                            first_col = tbl.iloc[:, 0].astype(str).str.upper()
                            if first_col.str.contains('DEVUELTO').any():
                                result.sheets[f"{sheet_name} (DEVUELTO)"] = tbl
                                result.row_count += len(tbl)
                                break

                    continue  # Ya se agregaron las hojas manualmente
                else:
                    df = self.clean_sheet(df_raw, sheet_name)

                if df is not None and not df.empty:
                    result.sheets[sheet_name] = df
                    result.row_count += len(df)

            except Exception as e:
                result.errors.append(f"Error en hoja '{sheet_name}' de SIDE: {str(e)}")
                continue  # No abortar por una hoja fallida

        result.success = len(result.sheets) > 0
        if result.errors:
            result.warnings.append(f"{len(result.errors)} hoja(s) con errores, {len(result.sheets)} hoja(s) ok")

        return result

    def _read_registrado(self, df_raw: pd.DataFrame) -> pd.DataFrame:
        """
        Lee REGISTRADO SIDE con estructura correcta.
        Fila 0: titulo + nombres de columna (LOCALIDAD, ORIGEN, ..., TOTAL)
        Fila 1: 'Tipo de Documento', 'Total', ... (subtotales por tipo de documento)
        Filas 2+: Datos reales
        """
        if df_raw.empty or len(df_raw) < 3:
            return df_raw

        row0 = df_raw.iloc[0].tolist()
        row1 = df_raw.iloc[1].tolist()
        ncols = len(df_raw.columns)

        columns = []
        for i in range(ncols):
            if i == 0:
                col = str(row1[i]).strip() if pd.notna(row1[i]) else 'Tipo de Documento'
            elif i == 1:
                col = str(row1[i]).strip() if pd.notna(row1[i]) else 'Total'
            elif i == 21:
                col = str(row1[i]).strip() if pd.notna(row1[i]) else 'FUNCIONARIO'
            elif i == 22:
                col = str(row1[i]).strip() if pd.notna(row1[i]) else 'SIDE'
            else:
                col = str(row0[i]).strip() if pd.notna(row0[i]) else f'Col_{i}'
            if not col or col.upper() in ('NAN', 'NONE', ''):
                col = f'Col_{i}'
            columns.append(col[:80])

        df = df_raw.iloc[2:].copy().reset_index(drop=True)
        df.columns = columns

        # Limpiar filas vacias al inicio/final
        while len(df) > 0 and df.iloc[-1].isna().all():
            df = df.iloc[:-1].reset_index(drop=True)
        while len(df) > 0 and df.iloc[0].isna().all():
            df = df.iloc[1:].reset_index(drop=True)

        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].apply(
                    lambda x: x.strip() if isinstance(x, str) else x
                )

        return df.reset_index(drop=True)

    def _read_entregado(self, df_raw: pd.DataFrame) -> pd.DataFrame:
        """
        Lee ENTREGADO SIDE - solo la primera tabla (ENTREGADOS).
        Fila 0: titulo + nombres (MES, FECHA, TIPO DOCUMENTO, ...)
        Fila 1: 'Tipo de Documento', 'Total', + datos
        Filas 2-12: Datos de entrega
        Fila 13: 'TOTAL', 23, ... (resumen)
        Fila 14: separador
        Fila 15+: 'DEVUELTO SIDE Mayo 2026' (segunda tabla, excluida aqui)
        """
        if df_raw.empty or len(df_raw) < 2:
            return df_raw

        row0 = df_raw.iloc[0].tolist()
        row1 = df_raw.iloc[1].tolist()
        ncols = len(df_raw.columns)

        columns = []
        for i in range(ncols):
            v0 = str(row0[i]).strip() if pd.notna(row0[i]) else ''
            v1 = str(row1[i]).strip() if pd.notna(row1[i]) else ''
            if i <= 1:
                col = v1 if v1 else (v0 if v0 else f'Col_{i}')
            else:
                col = v0 if v0 else (v1 if v1 else f'Col_{i}')
            if not col or col.upper() in ('NAN', 'NONE', ''):
                col = f'Col_{i}'
            columns.append(col[:80])

        # Truncar antes de DEVUELTO (segunda tabla)
        end_idx = len(df_raw)
        for i in range(1, len(df_raw)):
            row_vals = [str(x).strip().upper() for x in df_raw.iloc[i].tolist() if pd.notna(x)]
            if any('DEVUELTO' in v for v in row_vals):
                end_idx = i
                break

        df = df_raw.iloc[1:end_idx].copy().reset_index(drop=True)
        if df.empty:
            return df_raw

        df.columns = columns

        while len(df) > 0 and df.iloc[-1].isna().all():
            df = df.iloc[:-1].reset_index(drop=True)
        while len(df) > 0 and df.iloc[0].isna().all():
            df = df.iloc[1:].reset_index(drop=True)

        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].apply(
                    lambda x: x.strip() if isinstance(x, str) else x
                )

        return df.reset_index(drop=True)
