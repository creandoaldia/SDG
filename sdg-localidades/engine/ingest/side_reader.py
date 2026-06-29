"""
SDG Localidades — Reader: Resumen SIDE
Sistema de Información de Documentos Extraviados.
3 hojas: STOCK (inventario), REGISTRADO (nuevos registros), ENTREGADO (entregas).
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

            for sheet_name in xl.sheet_names:
                df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)
                df = self.clean_sheet(df_raw, sheet_name)
                result.sheets[sheet_name] = df
                result.row_count += len(df)

            result.success = len(result.sheets) > 0

        except Exception as e:
            result.errors.append(f"Error leyendo SIDE: {str(e)}")

        return result
