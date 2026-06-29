"""
SDG Localidades — Reader: Reporte Productividad Encuestas
Contiene datos crudos de encuestas de percepción y satisfacción (5,400+ filas).
Es la fuente más valiosa para automatización porque tiene datos a nivel individual.
"""
import pandas as pd
from engine.models import IngestionResult
from engine.ingest.base_reader import BaseReader


class EncuestasReader(BaseReader):
    """Lee el archivo REPORTE PRODUCTIVIDAD ENCUESTAS MAYO 2026.xlsx"""

    def read(self) -> IngestionResult:
        result = IngestionResult(source_key="encuestas", success=False)

        try:
            xl = pd.ExcelFile(self.file_path)

            for sheet_name in xl.sheet_names:
                if sheet_name == "Nuevo Formato Encuesta":
                    df = pd.read_excel(xl, sheet_name=sheet_name, header=0, dtype=str)
                else:
                    df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)
                    df = self.clean_sheet(df_raw, sheet_name)

                result.sheets[sheet_name] = df
                result.row_count += len(df)

            result.success = len(result.sheets) > 0

        except Exception as e:
            result.errors.append(f"Error leyendo Encuestas: {str(e)}")

        return result
