"""
SDG Localidades — Reader base para archivos fuente.
"""
import os
import pandas as pd
from typing import Optional
from engine.models import IngestionResult


class BaseReader:
    """
    Clase base para todos los readers de archivos fuente.
    Cada reader especializado hereda de esta clase.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)

    def read(self) -> IngestionResult:
        """
        Lee el archivo y retorna un IngestionResult.
        Debe ser implementado por cada subclase.
        """
        raise NotImplementedError("Cada reader debe implementar read()")

    def read_sheet(self, sheet_name: str, header_row: int = 0,
                   skip_rows: int = 0, usecols: Optional[list] = None) -> pd.DataFrame:
        """
        Lee una hoja específica del Excel con pandas.
        Maneja errores de encoding, tipos mixtos, etc.
        """
        try:
            df = pd.read_excel(
                self.file_path,
                sheet_name=sheet_name,
                header=header_row,
                skiprows=skip_rows,
                usecols=usecols,
                dtype=str  # Leer todo como string para evitar inferencias erróneas
            )
            # Limpiar nombres de columnas
            df.columns = [str(c).strip() if c is not None else f"col_{i}"
                         for i, c in enumerate(df.columns)]
            return df
        except Exception as e:
            # Fallback: intentar sin dtype=str
            df = pd.read_excel(
                self.file_path,
                sheet_name=sheet_name,
                header=header_row,
                skiprows=skip_rows,
                usecols=usecols
            )
            return df
