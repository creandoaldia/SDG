"""
SDG Localidades — Generador de Informe SIDE (Documentos Extraviados)
Extrae y estructura datos de STOCK, REGISTRADO y ENTREGADO de documentos.
"""
import pandas as pd
import re


class SideReport:

    def generate(self, ingestion_data: dict) -> dict:
        if 'side' not in ingestion_data:
            return {}
        sheets = ingestion_data['side'].sheets
        result = {}

        # Stock: simple tabla de tipo de documento vs total
        stock_df = sheets.get('STOCK 31052026')
        if stock_df is not None and not stock_df.empty:
            result['stock'] = stock_df

        # Registrados: limpiar primeras filas
        reg_df = sheets.get('REGISTRADO SIDE')
        if reg_df is not None and not reg_df.empty:
            # Primera fila es título, buscar header real
            data = reg_df.values.tolist()
            for i, row in enumerate(data):
                if any('Tipo de Documento' in str(c) for c in row):
                    headers = [str(c).strip() for c in row]
                    df_clean = reg_df.iloc[i:].copy()
                    df_clean.columns = headers + list(df_clean.columns[len(headers):])
                    df_clean = df_clean.iloc[1:].reset_index(drop=True)
                    df_clean = df_clean.dropna(how='all').reset_index(drop=True)
                    result['registrados'] = df_clean
                    break

        # Entregados
        ent_df = sheets.get('ENTREGADO SIDE')
        if ent_df is not None and not ent_df.empty:
            data = ent_df.values.tolist()
            for i, row in enumerate(data):
                if any('Tipo de Documento' in str(c) for c in row):
                    headers = [str(c).strip() for c in row]
                    df_clean = ent_df.iloc[i:].copy()
                    df_clean.columns = headers + list(df_clean.columns[len(headers):])
                    df_clean = df_clean.iloc[1:].reset_index(drop=True)
                    df_clean = df_clean.dropna(how='all').reset_index(drop=True)
                    result['entregados'] = df_clean
                    break

        return result
