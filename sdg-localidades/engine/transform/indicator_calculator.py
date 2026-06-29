"""
SDG Localidades — Calculador de Indicadores
Calcula: calificaciones, porcentajes de participacion, promedios,
y los indicadores compuestos que Yesenia genera manualmente.
"""
import pandas as pd


class IndicatorCalculator:
    """
    Calcula indicadores derivados de todas las fuentes.
    """

    def calculate(self, source_key: str, sheet_name: str, df: pd.DataFrame) -> dict:
        """
        Calcula indicadores segun la fuente y hoja.
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

        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

        if len(numeric_cols) > 0:
            for col in numeric_cols[:5]:
                indicators[f'Total {str(col)}'] = float(df[col].sum())

        # % de participacion
        localidad_col = None
        for col in df.columns:
            if 'localidad' in str(col).lower() or 'etiquetas' in str(col).lower():
                localidad_col = col
                break

        if localidad_col and numeric_cols:
            total_sum = df[numeric_cols[0]].sum()
            if total_sum > 0:
                indicators['Participacion por localidad'] = (
                    df.groupby(localidad_col)[numeric_cols[0]].sum() / total_sum
                ).to_dict()

        return indicators

    def _encuestas_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de encuestas (calificaciones)."""
        indicators = {}

        if sheet == "Nuevo Formato Encuesta":
            if 'Tipo' in df.columns:
                completas = len(df[df['Tipo'] == 'Completa'])
                incompletas = len(df[df['Tipo'] == 'Incompleta'])
                indicators['Total encuestas del periodo'] = len(df)
                indicators['Encuestas completas'] = int(completas)
                indicators['Encuestas incompletas'] = int(incompletas)
                indicators['Tasa de completitud (%)'] = round(
                    completas / len(df) * 100, 2
                ) if len(df) > 0 else 0

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
        """Indicadores de Certificados de Residencia con nombres descriptivos."""
        indicators = {}
        total_row = df[df.iloc[:, 0].astype(str).str.contains('TOTAL', case=False, na=False)]
        if not total_row.empty:
            # Obtener nombres de columna de la fila de encabezados
            # Buscar fila de encabezados (generalmente la primera fila con texto significativo)
            header_labels = self._find_column_labels(df)
            total_values = total_row.iloc[0]

            for i, val in enumerate(total_values):
                fval = self._try_float(val)
                if fval is not None and fval != 0:
                    # Usar nombre descriptivo si existe
                    label = header_labels[i] if i < len(header_labels) and header_labels[i] else f'Columna {i+1}'
                    indicators[f'CR - {label}'] = fval
        return indicators

    def _ph_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de Propiedad Horizontal con nombres descriptivos."""
        indicators = {}
        total_row = df[df.iloc[:, 0].astype(str).str.contains('TOTAL', case=False, na=False)]
        if not total_row.empty:
            header_labels = self._find_column_labels(df)
            total_values = total_row.iloc[0]

            for i, val in enumerate(total_values):
                fval = self._try_float(val)
                if fval is not None and fval != 0:
                    label = header_labels[i] if i < len(header_labels) and header_labels[i] else f'Columna {i+1}'
                    indicators[f'PH - {label}'] = fval
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
                            indicators['SAC - Total atenciones'] = fval
                            break
                    break
        return indicators

    def _side_indicators(self, df: pd.DataFrame, sheet: str) -> dict:
        """Indicadores de SIDE con nombres descriptivos."""
        indicators = {}
        total_row = df[df.iloc[:, 0].astype(str).str.contains('TOTAL', case=False, na=False)]
        if not total_row.empty:
            header_labels = self._find_column_labels(df)
            total_values = total_row.iloc[0]

            for i, val in enumerate(total_values):
                fval = self._try_float(val)
                if fval is not None and fval != 0:
                    label = header_labels[i] if i < len(header_labels) and header_labels[i] else f'Columna {i+1}'
                    indicators[f'SIDE - {label}'] = fval
        return indicators

    def _find_column_labels(self, df: pd.DataFrame) -> list:
        """
        Encuentra etiquetas de columna desde la primera fila con texto significativo
        o desde los nombres de columna del DataFrame.
        Retorna una lista de etiquetas.
        """
        # Intentar desde nombres de columna (si no son numericos)
        col_names = list(df.columns)
        if col_names:
            all_str = all(isinstance(c, str) for c in col_names)
            if all_str:
                # Verificar si los nombres tienen sentido (no numericos)
                try:
                    [int(c) for c in col_names]
                    # Son numericos -> buscar en datos
                    pass
                except ValueError:
                    # Tienen nombres de texto -> usarlos
                    return col_names

        # Buscar la primera fila que parezca un encabezado
        for i in range(min(5, len(df))):
            row = df.iloc[i]
            labels = []
            meaningful = 0
            for val in row:
                v = str(val).strip() if pd.notna(val) else ''
                if v and v.upper() not in ('NAN', '', 'NONE'):
                    labels.append(v)
                    if len(v) > 2:  # Palabra significativa
                        meaningful += 1
                else:
                    labels.append(f'Columna {len(labels) + 1}')
            if meaningful >= 2:
                return labels

        # Fallback: nombres genericos
        return [f'Columna {i+1}' for i in range(len(df.columns))]
