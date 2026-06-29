"""
SDG Localidades — Reader: BD PQRS Bogotá Te Escucha
Archivo corazón del sistema. Contiene la sábana de datos PQRS (12,900+ filas)
y las hojas derivadas (informe web, seguimiento días, indicadores).

ESTRUCTURA REAL del Excel:
- Filas 0-8: Metadata (título, fecha, usuario, etc.)
- Fila 9: HEADER real con 102 nombres de columna
- Filas 10+: Datos
"""
import pandas as pd
from engine.models import IngestionResult, LOCALIDADES
from engine.ingest.base_reader import BaseReader


class PQRSReader(BaseReader):
    """Lee el archivo BD PQRS BOGOTA TE ESCUCHA MAYO 2026.xlsx"""

    # Hojas de interés con su fila de header conocida (None = auto-detectar)
    SHEETS_CONFIG = {
        "Reporte PQRS Mayo2026":     {"header": 9, "skiprows": None},   # 9 filas metadata
        "INFORME WEB ABRIL":          {"header": None, "skiprows": None},# estructura irregular
        "SEGUIMIENTO DÍAS":           {"header": None, "skiprows": None},# auto-detectar + Etiquetas→Localidad
        "Tabla 10 indicadores_Ajusta": {"header": None, "skiprows": None},# multi-tabla
        "Calificaciones Totales":     {"header": None, "skiprows": None},# estructura irregular
        "CERT RESIDENCIA PROD-MAYO":  {"header": None, "skiprows": None},# auto-detectar header+renombrar
        "CR-TIPO TRAMITE":            {"header": None, "skiprows": None},# auto-detectar header+renombrar
        "CERT.P.HORIZONTAL MAYO":     {"header": None, "multi_table": True},# 2 tablas separadas por fila 26
        "REGISTRO ATENCIONES":        {"header": None, "skiprows": None},# estructura irregular
        "REGISTRADO SIDE":            {"header": 0, "skiprows": None},   # tabla dinámica
        "ENTREGADO SIDE":             {"header": 0, "skiprows": None},   # tabla dinámica
    }

    # Hojas que son tablas dinámicas (no datos crudos) - solo leer como referencia
    PIVOT_ONLY_SHEETS = {
        "CERT RESIDENCIA PROD-MAYO", "CR-TIPO TRAMITE",
        "CERT.P.HORIZONTAL MAYO", "REGISTRO ATENCIONES",
        "REGISTRADO SIDE", "ENTREGADO SIDE",
        "INSC", "ACT", "EXT",
    }

    def read(self) -> IngestionResult:
        result = IngestionResult(source_key="pqrs", success=False)
        try:
            xl = pd.ExcelFile(self.file_path)
            available = set(xl.sheet_names)

            for sheet_name, config in self.SHEETS_CONFIG.items():
                if sheet_name not in available:
                    result.warnings.append(f"Hoja '{sheet_name}' no encontrada en {self.filename}")
                    continue

                # Manejar hojas con múltiples tablas (ej: CERT.P.HORIZONTAL MAYO)
                if config.get("multi_table"):
                    df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)
                    tables = self.detect_tables(df_raw)
                    for idx, table_df in enumerate(tables):
                        if table_df is not None and not table_df.empty and len(table_df.columns) >= 2:
                            sname = f"{sheet_name}" if idx == 0 else f"{sheet_name} ({idx+1})"
                            result.sheets[sname] = table_df
                            result.row_count += len(table_df)
                else:
                    df = self._read_sheet(xl, sheet_name, config)
                    if df is not None and not df.empty:
                        result.sheets[sheet_name] = df
                        result.row_count += len(df)

            result.success = len(result.sheets) > 0
            if result.row_count == 0:
                result.warnings.append(f"Archivo {self.filename} parece vacío o sin hojas esperadas")

        except Exception as e:
            result.errors.append(f"Error leyendo {self.filename}: {str(e)}")

        return result

    def _read_sheet(self, xl: pd.ExcelFile, sheet_name: str, config: dict) -> pd.DataFrame:
        """Lee una hoja según su configuración de header conocida."""
        try:
            header_row = config["header"]
            if header_row is not None:
                # Header conocido — leer directamente
                df = pd.read_excel(xl, sheet_name=sheet_name, header=header_row, dtype=str)
                # Limpiar columnas Unnamed
                df = self._clean_unnamed(df)
                # Limpiar filas completamente vacías
                df = df.dropna(how='all').reset_index(drop=True)
                return df if not df.empty else None
            else:
                # Auto-detectar header para hojas irregulares
                return self._auto_read_sheet(xl, sheet_name)
        except Exception as e:
            result.warnings.append(f"Error leyendo hoja '{sheet_name}': {str(e)}")
            return None

    def _auto_read_sheet(self, xl: pd.ExcelFile, sheet_name: str) -> pd.DataFrame:
        """Auto-detecta estructura para hojas con formato irregular.
        Usa clean_sheet (BaseReader v2) y detect_tables.
        """
        df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)

        # Estrategia 1: clean_sheet con auto-deteccion de headers
        df = self.clean_sheet(df_raw)
        if df is not None and not df.empty and len(df.columns) >= 2:
            return df

        # Estrategia 2: Multi-tabla
        tables = self.detect_tables(df_raw)
        if tables:
            best_table = max(tables, key=lambda t: len(t.columns))
            return best_table if not best_table.empty else None

        # Fallback
        df = df_raw.dropna(how='all').reset_index(drop=True)
        return df if not df.empty else None

        # Fallback: todo como datos crudos
        df = df_raw.dropna(how='all').reset_index(drop=True)
        return df if not df.empty else None

    def _clean_unnamed(self, df: pd.DataFrame) -> pd.DataFrame:
        """Renombra columnas 'Unnamed: N' con el primer valor no-nulo de esa columna si es útil."""
        cols = []
        for col in df.columns:
            col_str = str(col).strip()
            if col_str.startswith("Unnamed:"):
                # Buscar primer valor significativo en esta columna
                first_val = df[col].dropna().iloc[0] if not df[col].dropna().empty else ""
                first_str = str(first_val).strip()[:60] if first_val else ""
                if first_str and not first_str.startswith("Unnamed"):
                    cols.append(first_str)
                else:
                    cols.append(col_str)
            else:
                cols.append(col_str)
        df.columns = cols
        return df
