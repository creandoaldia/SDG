"""
SDG Localidades — Reader: SAC Atención al Ciudadano
Archivo con registros crudos de atencion ciudadana.
Contiene: hoja 'Mayo SAC_atencion' con datos de atenciones y hoja 'tablas' con resumen.
"""
import pandas as pd
from engine.models import IngestionResult
from engine.ingest.base_reader import BaseReader


class SACReader(BaseReader):
    """Lee el archivo 05. SAC_atencion - Mayo 2026.xlsx"""

    def read(self) -> IngestionResult:
        result = IngestionResult(source_key="sac", success=False)

        try:
            xl = pd.ExcelFile(self.file_path)

            # Hoja principal: datos crudos de atenciones
            if "Mayo SAC_atencion" in xl.sheet_names:
                df = pd.read_excel(xl, sheet_name="Mayo SAC_atencion", dtype=str)
                result.sheets["Mayo SAC_atencion"] = df
                result.row_count += len(df)
            else:
                result.warnings.append("Hoja 'Mayo SAC_atencion' no encontrada en SAC")

            # Hoja de tablas resumen (precalculadas)
            if "tablas" in xl.sheet_names:
                df_raw = pd.read_excel(xl, sheet_name="tablas", header=None, dtype=str)
                df_tab = self.clean_sheet(df_raw, "tablas")
                result.sheets["tablas"] = df_tab
                result.row_count += len(df_tab)

            result.success = len(result.sheets) > 0

        except Exception as e:
            result.errors.append(f"Error leyendo SAC: {str(e)}")

        return result
