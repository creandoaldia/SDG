"""
SDG Localidades — Generador de Informe SIDE (Documentos Extraviados)
Extrae y estructura datos de STOCK, REGISTRADO y ENTREGADO de documentos.
"""
import pandas as pd
import re


class SideReport:

    def _find_sheet(self, sheets: dict, pattern: str) -> str:
        """Busca hoja por patron parcial (case-insensitive)."""
        pl = pattern.lower()
        for sname in sheets:
            if pl in sname.lower():
                return sname
        return None

    def generate(self, ingestion_data: dict) -> dict:
        if 'side' not in ingestion_data:
            return {}
        sheets = ingestion_data['side'].sheets
        result = {}

        # Stock: encontrar hoja por patron parcial (no nombre exacto con fecha)
        stock_key = self._find_sheet(sheets, 'STOCK')
        if stock_key:
            stock_df = sheets[stock_key]
            if stock_df is not None and not stock_df.empty:
                result['stock'] = stock_df

        # Registrados
        reg_key = self._find_sheet(sheets, 'REGISTRADO')
        if reg_key:
            reg_df = sheets[reg_key]
            if reg_df is not None and not reg_df.empty:
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

        # Entregados (excluir DEVUELTO)
        ent_key = self._find_sheet(sheets, 'ENTREGADO')
        if ent_key and 'DEVUELTO' not in ent_key.upper():
            ent_df = sheets[ent_key]
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
