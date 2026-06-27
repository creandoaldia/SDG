"""
SDG Localidades — Detector de duplicados
Implementa la misma lógica que Yesenia usa manualmente:
ordenar por N° petición y marcar filas consecutivas iguales.
"""
import pandas as pd


class Deduplicator:
    """
    Detecta peticiones duplicadas en la sábana PQRS.
    La lógica replica exactamente lo que Yesenia hace en el video:
    1. Ordenar por N° petición
    2. Insertar columna Duplicados
    3. Fórmula: =A[n]=A[n+1]
    """

    def find_duplicates(self, df: pd.DataFrame, id_column: str = "Número petición") -> pd.DataFrame:
        """
        Marca duplicados en el DataFrame.
        Retorna el DataFrame con columna '_duplicado' agregada.
        """
        if df is None or df.empty:
            return df

        # Buscar la columna de ID (puede tener diferentes nombres)
        id_col = self._find_id_column(df, id_column)
        if id_col is None:
            return df

        result = df.copy()

        # Ordenar por el ID
        try:
            # Intentar orden numérico
            result[id_col] = pd.to_numeric(result[id_col], errors='ignore')
            result = result.sort_values(by=id_col).reset_index(drop=True)
        except Exception:
            # Fallback: orden string
            result = result.sort_values(by=id_col).reset_index(drop=True)

        # Marcar duplicados: comparar cada fila con la siguiente
        # Yesenia usa: =A[n]=A[n+1] que da TRUE si son iguales
        result['_duplicado'] = result[id_col] == result[id_col].shift(-1)

        # La primera ocurrencia de un duplicado NO se marca (solo la segunda+)
        # Para replicar exactamente: FALSE en la primera, TRUE en las repetidas
        # Ya que shift(-1) compara actual con siguiente:
        # Si A[1]=A[2]=A[3], entonces A[1] compara con A[2] -> TRUE
        # Pero Yesenia marca la segunda aparición como duplicado
        # Así que necesitamos: comparar con anterior
        result['_duplicado'] = result[id_col] == result[id_col].shift(1)

        # Marcar el primer elemento de cada grupo también
        # Si A[1]=A[2], queremos que A[2] sea TRUE (duplicado de A[1])
        # y A[1] sea FALSE (es el original)
        # shift(1) ya hace esto: A[1] compara con NA -> FALSE,
        # A[2] compara con A[1] -> TRUE

        return result

    def _find_id_column(self, df: pd.DataFrame, preferred: str) -> str:
        """Encuentra la columna de ID de petición."""
        if preferred in df.columns:
            return preferred

        alternatives = ["Número petición", "NUMERO PETICION", "No. petición",
                        "PETICION", "ID", "RADICADO", "N° petición"]
        for alt in alternatives:
            for col in df.columns:
                if alt.lower() in str(col).lower():
                    return col

        return df.columns[0] if len(df.columns) > 0 else None
