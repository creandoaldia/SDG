"""
SDG Localidades — Reader: Productividad Certificado de Residencia
Contiene tabla dinámica de productividad de CR por localidad.
Nota: Este archivo solo contiene la tabla precalculada, no los datos crudos.
"""
import pandas as pd
from engine.models import IngestionResult
from engine.ingest.base_reader import BaseReader


class CRReader(BaseReader):
    """Lee el archivo MAYO2026_PRODUCTIVIDAD_CR.xlsx"""

    def read(self) -> IngestionResult:
        result = IngestionResult(source_key="cr", success=False)

        try:
            xl = pd.ExcelFile(self.file_path)

            for sheet_name in xl.sheet_names:
                df = pd.read_excel(xl, sheet_name=sheet_name, header=None, dtype=str)
                result.sheets[sheet_name] = df
                # Contar filas con datos (no vacías)
                data_rows = df.dropna(how='all')
                result.row_count += len(data_rows)

            result.success = len(result.sheets) > 0

        except Exception as e:
            result.errors.append(f"Error leyendo CR: {str(e)}")

        return result
