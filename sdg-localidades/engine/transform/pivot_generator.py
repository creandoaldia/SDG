"""
SDG Localidades — Generador de Tablas Dinámicas (Q1-Q6)
Genera las 6 preguntas del informe INF Localidades PPT.

COLUMNAS REALES del Excel fuente:
- 'Localidad de los hechos' — formato '17 - LA CANDELARIA'
- 'Dependencia' — 'ALCALDIA LOCAL DE FONTIBON', 'OFICINA DE ATENCION...'
- 'Tipo petición' — 'DERECHO DE PETICION...', 'QUEJA', 'RECLAMO', etc.
- 'Estado petición final' — 'Cerrado - Sin recurso...', 'Solucionado - Por respuesta...'
- 'Estado de la petición' — similar al anterior pero más detallado
- 'Duplicados' — 'False'/'True'
"""
import pandas as pd
import re


class PivotGenerator:
    """
    Genera las tablas dinámicas del informe de localidades.
    Q1: Solicitudes recibidas/ingresadas/registradas por localidad
    Q2: Solicitudes de información recibidas
    Q3: Tiempo de respuesta (solucionado)
    Q4: Solicitudes cerradas
    Q5: Solicitudes trasladadas
    Q6: Solicitudes con información negada
    """

    # Columnas reales en el Excel de PQRS
    COL_LOCALIDAD = 'Localidad de los hechos'
    COL_DEPENDENCIA = 'Dependencia'
    COL_TIPO_PETICION = 'Tipo petición'
    COL_ESTADO_FINAL = 'Estado petición final'
    COL_ESTADO = 'Estado de la petición'
    COL_DUPLICADOS = 'Duplicados'

    def generate_all(self, df: pd.DataFrame) -> dict:
        """Genera todas las tablas dinámicas Q1-Q6."""
        if df is None or df.empty:
            return {}

        # Debug: qué columnas están disponibles
        available = [c for c in [self.COL_LOCALIDAD, self.COL_DEPENDENCIA,
                                 self.COL_TIPO_PETICION, self.COL_ESTADO_FINAL,
                                 self.COL_ESTADO, self.COL_DUPLICADOS]
                    if c in df.columns]

        result = {}

        # Q1: Siempre disponible si hay Localidad de los hechos
        q1 = self._q1_total_solicitudes(df)
        if q1 is not None:
            result['Q1_Total_Solicitudes'] = q1

        q2 = self._q2_solicitudes_informacion(df)
        if q2 is not None:
            result['Q2_Solicitudes_Informacion'] = q2

        q3 = self._q3_tiempo_respuesta(df)
        if q3 is not None:
            result['Q3_Tiempo_Respuesta'] = q3

        q4 = self._q4_cerradas(df)
        if q4 is not None:
            result['Q4_Cerradas'] = q4

        q5 = self._q5_trasladadas(df)
        if q5 is not None:
            result['Q5_Trasladadas'] = q5

        q6 = self._q6_informacion_negada(df)
        if q6 is not None:
            result['Q6_Info_Negada'] = q6

        return result

    def _extract_localidad(self, series: pd.Series) -> pd.Series:
        """
        Extrae el nombre de localidad de valores como '17 - LA CANDELARIA'
        o 'ALCALDIA LOCAL DE FONTIBON'.
        """
        def parse(val):
            if pd.isna(val):
                return None
            val = str(val).strip().upper()
            # Formato 'NN - NOMBRE'
            m = re.match(r'\d+\s*-\s*(.+)', val)
            if m:
                return m.group(1).strip()
            # Formato 'ALCALDIA LOCAL DE XXX'
            m = re.match(r'ALCALDIA LOCAL DE\s+(.+)', val)
            if m:
                return m.group(1).strip()
            # Formato 'OFICINA DE ATENCION...' o 'NIVEL CENTRAL'
            if 'NIVEL CENTRAL' in val:
                return 'NIVEL CENTRAL'
            if 'SUPERCADE' in val:
                return 'SUPERCADES'
            return val
        return series.apply(parse)

    def _find_col(self, df: pd.DataFrame, candidates: list) -> str:
        """Busca una columna por nombre exacto o coincidencia parcial."""
        for col in df.columns:
            col_str = str(col).strip().lower()
            for candidate in candidates:
                if candidate.lower() in col_str:
                    return col
        return None

    def _q1_total_solicitudes(self, df: pd.DataFrame) -> pd.DataFrame:
        """Q1: Número de solicitudes por localidad."""
        if self.COL_LOCALIDAD in df.columns:
            localidad_col = self.COL_LOCALIDAD
        else:
            localidad_col = self._find_col(df, ['localidad', 'dependencia', 'punto'])
        if not localidad_col:
            return None

        # Extraer nombre de localidad y agrupar
        df_copy = df.copy()
        df_copy['_localidad'] = self._extract_localidad(df_copy[localidad_col])
        df_copy = df_copy[df_copy['_localidad'].notna()]

        if df_copy.empty:
            return None

        result = df_copy.groupby('_localidad').size().reset_index()
        result.columns = ['Localidad', 'Total Solicitudes']
        result = result.sort_values('Total Solicitudes', ascending=False).reset_index(drop=True)
        return result

    def _q2_solicitudes_informacion(self, df: pd.DataFrame) -> pd.DataFrame:
        """Q2: Solicitudes de acceso a la información."""
        tipo_col = self.COL_TIPO_PETICION if self.COL_TIPO_PETICION in df.columns else \
                   self._find_col(df, ['tipo petición', 'tipo petic', 'tipopetic'])
        if not tipo_col:
            return None

        localidad_col = self.COL_LOCALIDAD if self.COL_LOCALIDAD in df.columns else \
                        self._find_col(df, ['localidad', 'dependencia', 'punto'])

        mask = df[tipo_col].str.contains('INFORMACION|INFORMACIÓN', case=False, na=False)
        subset = df[mask].copy()
        if subset.empty:
            return None

        if localidad_col:
            subset['_localidad'] = self._extract_localidad(subset[localidad_col])
            subset = subset[subset['_localidad'].notna()]
            result = subset.groupby('_localidad').size().reset_index()
            result.columns = ['Localidad', 'Solicitudes Información']
        else:
            result = pd.DataFrame({'Total': [len(subset)]})

        return result

    def _q3_tiempo_respuesta(self, df: pd.DataFrame) -> pd.DataFrame:
        """Q3: Solicitudes solucionadas/respuesta definitiva."""
        estado_col = self.COL_ESTADO_FINAL if self.COL_ESTADO_FINAL in df.columns else \
                     self.COL_ESTADO if self.COL_ESTADO in df.columns else \
                     self._find_col(df, ['estado petición final', 'estado final', 'estado'])
        if not estado_col:
            return None

        localidad_col = self.COL_LOCALIDAD if self.COL_LOCALIDAD in df.columns else \
                        self._find_col(df, ['localidad', 'dependencia', 'punto'])

        mask = df[estado_col].str.contains('SOLUCIONADO|RESPUESTA DEFINITIVA', case=False, na=False)
        q3 = df[mask].copy()
        if q3.empty:
            return None

        if localidad_col:
            q3['_localidad'] = self._extract_localidad(q3[localidad_col])
            q3 = q3[q3['_localidad'].notna()]
            result = q3.groupby('_localidad').size().reset_index()
            result.columns = ['Localidad', 'Respuestas Definitivas']
            return result
        return None

    def _q4_cerradas(self, df: pd.DataFrame) -> pd.DataFrame:
        """Q4: Solicitudes cerradas."""
        estado_col = self.COL_ESTADO if self.COL_ESTADO in df.columns else \
                     self.COL_ESTADO_FINAL if self.COL_ESTADO_FINAL in df.columns else \
                     self._find_col(df, ['estado de la petición', 'estado petición final', 'estado final'])
        if not estado_col:
            return None

        localidad_col = self.COL_LOCALIDAD if self.COL_LOCALIDAD in df.columns else \
                        self._find_col(df, ['localidad', 'dependencia', 'punto'])
        if not localidad_col:
            return None

        mask = df[estado_col].str.contains('CERRA|SOLUCION', case=False, na=False)
        cerradas = df[mask].copy()
        if cerradas.empty:
            return None

        cerradas['_localidad'] = self._extract_localidad(cerradas[localidad_col])
        cerradas = cerradas[cerradas['_localidad'].notna()]
        result = cerradas.groupby('_localidad').size().reset_index()
        result.columns = ['Localidad', 'Solicitudes Cerradas']
        return result

    def _q5_trasladadas(self, df: pd.DataFrame) -> pd.DataFrame:
        """Q5: Solicitudes trasladadas a otras dependencias."""
        localidad_col = self.COL_LOCALIDAD if self.COL_LOCALIDAD in df.columns else \
                        self._find_col(df, ['localidad', 'dependencia', 'punto'])
        if not localidad_col:
            return None

        dependencia_col = self.COL_DEPENDENCIA if self.COL_DEPENDENCIA in df.columns else \
                          self._find_col(df, ['dependencia'])
        if not dependencia_col:
            return None

        mask = df[dependencia_col].str.contains('OFICINA DE ATENCION|NIVEL CENTRAL', case=False, na=False)
        trasladadas = df[mask].copy()
        if trasladadas.empty:
            return None

        trasladadas['_localidad'] = self._extract_localidad(trasladadas[localidad_col])
        trasladadas = trasladadas[trasladadas['_localidad'].notna()]
        result = trasladadas.groupby('_localidad').size().reset_index()
        result.columns = ['Localidad', 'Solicitudes Trasladadas']
        return result

    def _q6_informacion_negada(self, df: pd.DataFrame) -> pd.DataFrame:
        """Q6: Solicitudes con información negada/rechazada/cancelada."""
        estado_col = self.COL_ESTADO_FINAL if self.COL_ESTADO_FINAL in df.columns else \
                     self.COL_ESTADO if self.COL_ESTADO in df.columns else \
                     self._find_col(df, ['estado petición final', 'estado final'])
        if not estado_col:
            return None

        localidad_col = self.COL_LOCALIDAD if self.COL_LOCALIDAD in df.columns else \
                        self._find_col(df, ['localidad', 'dependencia', 'punto'])
        if not localidad_col:
            return None

        # Buscar estados de negación, rechazo, cancelación o cierre sin respuesta
        mask = df[estado_col].str.contains(
            'NEGAD|RECHAZ|CANCEL|DENEG|NO COMPETENCIA|SIN RECURSO|VENCIMIENTO',
            case=False, na=False
        )
        negadas = df[mask].copy()
        if negadas.empty:
            return None

        negadas['_localidad'] = self._extract_localidad(negadas[localidad_col])
        negadas = negadas[negadas['_localidad'].notna()]
        result = negadas.groupby('_localidad').size().reset_index()
        result.columns = ['Localidad', 'Información Negada']
        return result
