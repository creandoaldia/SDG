"""
SDG Localidades — Generador de Informe PQRS Canal Web
Filtra la sabana de datos PQRS por Canal='WEB' y genera un resumen
estructurado: por localidad, por tipo de peticion, estado de gestion.
"""
import pandas as pd


class WebReport:
    """
    Genera el informe de PQRS del canal web a partir de los datos
    ya cargados en el pipeline (no re-lectura de archivos).
    """

    # Columnas esperadas en el DataFrame de PQRS
    COL_CANAL = 'Canal'
    COL_LOCALIDAD = 'Localidad de los hechos'
    COL_TIPO = 'Tipo petición'
    COL_ESTADO_FINAL = 'Estado petición final'
    COL_ESTADO = 'Estado de la petición'
    COL_TIPO_REPORTE = 'Tipo reporte'

    def generate(self, ingestion_data: dict) -> dict:
        """
        Genera tablas del informe web.
        Retorna dict con DataFrames: 'resumen', 'por_localidad', 'por_tipo', 'por_estado'.
        """
        if 'pqrs' not in ingestion_data:
            return {}

        sheets = ingestion_data['pqrs'].sheets
        df_raw = sheets.get('Reporte PQRS Mayo2026')
        if df_raw is None or df_raw.empty:
            return {}

        # Filtrar solo canal WEB
        if self.COL_CANAL not in df_raw.columns:
            return {}

        web = df_raw[df_raw[self.COL_CANAL].str.upper() == 'WEB'].copy()
        if web.empty:
            return {}

        result = {}

        # --- 1. Resumen general ---
        total = len(web)
        gestionados = len(web[web[self.COL_TIPO_REPORTE].str.upper() == 'GESTIONADOS']) \
            if self.COL_TIPO_REPORTE in web.columns else 0
        pendientes = total - gestionados
        result['resumen'] = pd.DataFrame([
            {'Indicador': 'Total PQRS WEB', 'Valor': total},
            {'Indicador': 'Gestionados', 'Valor': gestionados},
            {'Indicador': 'Pendientes', 'Valor': pendientes},
            {'Indicador': '% Gestion', 'Valor': round(gestionados / total * 100, 1) if total > 0 else 0},
        ])

        # --- 2. Por localidad ---
        if self.COL_LOCALIDAD in web.columns:
            loc = web[self.COL_LOCALIDAD].value_counts().reset_index()
            loc.columns = ['Localidad', 'PQRS WEB']
            loc['Localidad'] = loc['Localidad'].str.replace(r'^\d+\s*-\s*', '', regex=True).str.strip()
            result['por_localidad'] = loc.sort_values('PQRS WEB', ascending=False).reset_index(drop=True)

        # --- 3. Por tipo de peticion ---
        if self.COL_TIPO in web.columns:
            tipo = web[self.COL_TIPO].value_counts().reset_index()
            tipo.columns = ['Tipo Petición', 'Cantidad']
            result['por_tipo'] = tipo

        # --- 4. Por estado final ---
        estado_col = self.COL_ESTADO_FINAL if self.COL_ESTADO_FINAL in web.columns else \
                     self.COL_ESTADO if self.COL_ESTADO in web.columns else None
        if estado_col:
            est = web[estado_col].value_counts().reset_index()
            est.columns = ['Estado Final', 'Cantidad']
            result['por_estado'] = est

        return result
