"""
SDG Localidades — Normalizador de datos
Estandariza localidades, fechas, formatos y nombres de columnas.
"""
import re
import pandas as pd
from engine.models import LOCALIDADES_NORMALIZE


class Normalizer:
    """Normaliza datos de todas las fuentes a un formato común."""

    def normalize(self, df: pd.DataFrame, source: str = "", sheet: str = "") -> pd.DataFrame:
        """
        Normaliza un DataFrame según su fuente y hoja de origen.
        - Estandariza nombres de localidades
        - Limpia espacios y caracteres especiales
        - Normaliza fechas
        - Elimina filas completamente vacías
        """
        if df is None or df.empty:
            return df

        ndf = df.copy()

        # 1. Eliminar filas totalmente vacías
        ndf = ndf.dropna(how='all').reset_index(drop=True)

        # 2. Limpiar strings: espacios, caracteres invisibles
        for col in ndf.columns:
            series = ndf[col]
            # Si hay columnas duplicadas, pandas devuelve DataFrame, no Series
            if isinstance(series, pd.DataFrame):
                series = series.iloc[:, 0]
            if series.dtype == 'object':
                ndf[col] = series.apply(
                    lambda x: self._clean_str(x) if pd.notna(x) else x
                )

        # 3. Normalizar localidades en todas las columnas de texto
        for col in ndf.columns:
            series = ndf[col]
            if isinstance(series, pd.DataFrame):
                series = series.iloc[:, 0]
            if series.dtype == 'object':
                ndf[col] = series.apply(
                    lambda x: self._normalize_locality(x) if pd.notna(x) else x
                )

        return ndf

    def _clean_str(self, value) -> str:
        """Limpia un valor string: espacios, saltos de línea, caracteres especiales."""
        if not isinstance(value, str):
            return value
        value = value.strip()
        value = re.sub(r'\s+', ' ', value)  # Múltiples espacios -> uno
        value = value.replace('\n', ' ').replace('\r', ' ')
        return value

    def _normalize_locality(self, value) -> str:
        """
        Normaliza nombres de localidades a su forma estándar.
        "ciudad bolivar" -> "CIUDAD BOLIVAR"
        "engativa" -> "ENGATIVÁ"
        """
        if not isinstance(value, str):
            return value

        upper_val = value.strip().upper()
        # Remover tildes para comparación
        import unidecode
        upper_clean = unidecode.unidecode(upper_val)

        # Buscar coincidencia exacta primero
        if upper_val in LOCALIDADES_NORMALIZE:
            return LOCALIDADES_NORMALIZE[upper_val]

        # Buscar coincidencia sin tildes
        for key, normalized in LOCALIDADES_NORMALIZE.items():
            if unidecode.unidecode(key.upper()) == upper_clean:
                return normalized

        # Buscar coincidencia parcial (ej: "ALCALDIA LOCAL DE BOSA")
        for key, normalized in LOCALIDADES_NORMALIZE.items():
            if key.upper() in upper_val or upper_clean in unidecode.unidecode(key.upper()):
                return normalized

        return value
