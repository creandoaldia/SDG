"""
SDG Localidades — Calculador de Indicadores
Calcula: calificaciones, porcentajes de participación, promedios,
y los indicadores compuestos que Yesenia genera manualmente.
"""
import pandas as pd


class IndicatorCalculator:
    """
    Calcula indicadores derivados de todas las fuentes.
    """

    def calculate(self, source_key: str, sheet_name: str, df: pd.DataFrame) -> dict:
        """
        Calcula indicadores según la fuente y hoja.
        Retorna dict con los indicadores calculados.
        """
        if df is None or df.empty:
            return {}

        if source_key == "pqrs":
            return self._pqrs_indicators(df, sheet_name)
        elif source_key == "encuestas":
            return self._encuestas_indicators(df, sheet_name)
        elif source_key == "cr":
            return self._cr_indicators(df, sheet_name)
        elif source_key == "ph":
            return self._ph_indicators(df, sheet_name)
        elif source_key == "sac":
            return self._sac_indicators(df, sheet_name)
        elif source_key == "side":
            return self._side_indicators(df, sheet_name)

        return {}

    def _pqrs_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de PQRS."""
        indicators = {}

        # Buscar columnas numéricas para calcular totales
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

        if len(numeric_cols) > 0:
            indicators['totals'] = {}
            for col in numeric_cols[:5]:  # Top 5 columnas numéricas
                indicators['totals'][str(col)] = float(df[col].sum())

        # % de participación: si hay columna de localidad y total
        localidad_col = None
        for col in df.columns:
            if 'localidad' in str(col).lower() or 'etiquetas' in str(col).lower():
                localidad_col = col
                break

        if localidad_col and numeric_cols:
            total_sum = df[numeric_cols[0]].sum()
            if total_sum > 0:
                indicators['participation_pct'] = (
                    df.groupby(localidad_col)[numeric_cols[0]].sum() / total_sum * 100
                ).to_dict()

        return indicators

    def _encuestas_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de encuestas (calificaciones)."""
        indicators = {}

        if sheet == "Nuevo Formato Encuesta":
            # Contar completas vs incompletas
            if 'Tipo' in df.columns:
                completas = len(df[df['Tipo'] == 'Completa'])
                incompletas = len(df[df['Tipo'] == 'Incompleta'])
                indicators['total_encuestas'] = len(df)
                indicators['completas'] = int(completas)
                indicators['incompletas'] = int(incompletas)
                indicators['tasa_completitud'] = round(completas / len(df) * 100, 2) if len(df) > 0 else 0

        return indicators

    @staticmethod
    def _try_float(val):
        """Intenta convertir un valor a float. Retorna None si no es posible."""
        if isinstance(val, (int, float)):
            return float(val)
        if isinstance(val, str):
            val = val.strip().replace(',', '').replace(' ', '')
            try:
                return float(val)
            except ValueError:
                pass
        return None

    def _cr_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de Certificados de Residencia."""
        indicators = {}
        total_row = df[df.iloc[:, 0].astype(str).str.contains('TOTAL', case=False, na=False)]
        if not total_row.empty:
            for i, val in enumerate(total_row.iloc[0]):
                fval = self._try_float(val)
                if fval is not None and fval != 0:
                    indicators[f'total_col_{i}'] = fval
        return indicators

    def _ph_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de Propiedad Horizontal."""
        indicators = {}
        total_row = df[df.iloc[:, 0].astype(str).str.contains('TOTAL', case=False, na=False)]
        if not total_row.empty:
            for i, val in enumerate(total_row.iloc[0]):
                fval = self._try_float(val)
                if fval is not None and fval != 0:
                    indicators[f'total_col_{i}'] = fval
        return indicators

    def _sac_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de SAC."""
        indicators = {}
        for _, row in df.iterrows():
            for cell in row:
                cell_str = str(cell).strip() if pd.notna(cell) else ''
                if 'TOTAL GENERAL' in cell_str.upper():
                    for cell2 in row:
                        fval = self._try_float(cell2)
                        if fval is not None:
                            indicators['total_atenciones'] = fval
                            break
                    break
        return indicators

    def _side_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de SIDE."""
        indicators = {}
        total_row = df[df.iloc[:, 0].astype(str).str.contains('TOTAL', case=False, na=False)]
        if not total_row.empty:
            for i, val in enumerate(total_row.iloc[0]):
                fval = self._try_float(val)
                if fval is not None and fval != 0:
                    indicators[f'total_{i}'] = fval
        return indicators
