"""
SDG Localidades — Reader: Productividad Propiedad Horizontal
Contiene tablas de productividad PH por localidad.
3 hojas: INSC (inscripciones), ACT (actualizaciones), RESUMEN (generados+validados).
"""
import pandas as pd
from engine.models import IngestionResult
from engine.ingest.base_reader import BaseReader


class PHReader(BaseReader):
    """Lee el archivo MAYO2026_PRODUCTIVIDAD_PH.xlsx"""

    def read(self) -> IngestionResult:
        result = IngestionResult(source_key="ph", success=False)

        try:
            xl = pd.ExcelFile(self.file_path)

            for sheet_name in xl.sheet_names:
                df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)
                df = self.clean_sheet(df_raw, sheet_name)
                result.sheets[sheet_name] = df
                data_rows = df.dropna(how='all')
                result.row_count += len(data_rows)

            result.success = len(result.sheets) > 0

        except Exception as e:
            result.errors.append(f"Error leyendo PH: {str(e)}")

        return result
