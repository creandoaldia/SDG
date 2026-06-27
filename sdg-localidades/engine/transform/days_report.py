"""
SDG Localidades — Generador de Informe de Días de Gestión
Extrae y estructura los datos de seguimiento de días desde la
hoja SEGUIMIENTO DÍAS del archivo PQRS.
NOTA: El reader lee con header=0, la columna 0 tiene etiquetas.
"""
import pandas as pd
import re


class DaysReport:

    def generate(self, ingestion_data: dict) -> dict:
        if 'pqrs' not in ingestion_data:
            return {}

        sheets = ingestion_data['pqrs'].sheets
        df = sheets.get('SEGUIMIENTO DÍAS')
        if df is None or df.empty:
            return {}

        # El DataFrame tiene header=0. Col0=etiqueta, Col1-12=meses
        cols = list(df.columns)
        # La primera columna real es la etiqueta (nombre de localidad/indicador)
        label_col = cols[0]
        # Columnas de meses: las que son nombres de mes
        month_cols = [c for c in cols if str(c).upper() in
                      ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO',
                       'JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']]

        result = {}
        data = df.values.tolist()

        # Sección 1: Días promedio por localidad (primeras ~24 filas)
        dias_loc = []
        for row in data:
            label = str(row[0]).strip() if pd.notna(row[0]) else ''
            if not label:
                continue
            is_loc = ('ALCALDIA LOCAL' in label.upper() or 'OFICINA' in label.upper())
            if not is_loc:
                continue
            if 'TOTAL DIAS' in label.upper():
                continue
            loc = re.sub(r'^ALCALDIA LOCAL DE\s+', '', label, flags=re.IGNORECASE).strip()
            loc = re.sub(r'^OFICINA\s+', '', loc, flags=re.IGNORECASE).strip()
            if loc:
                entry = {'Dependencia': loc.title()}
                for ci, mc in enumerate(month_cols[:5]):  # Ene-May
                    val = row[cols.index(mc)] if mc in cols else ''
                    entry[mc.title()] = self._to_float(val)
                dias_loc.append(entry)
        if dias_loc:
            result['dias_localidad'] = pd.DataFrame(dias_loc)

        # Sección 2: Gestión mensual (buscar keywords específicas)
        gestion_keywords = ['GESTIÓN EXTEMPORÁNEA', 'GESTION EXTEMPORANEA',
                            'GESTIÓN OPORTUNA', 'GESTION OPORTUNA',
                            'PENDIENTES EN TÉRMINOS', 'PENDIENTES EN TERMINOS',
                            'PENDIENTES VENCIDOS']
        gestion_items = []
        for row in data:
            label = str(row[0]).strip() if pd.notna(row[0]) else ''
            for kw in gestion_keywords:
                if kw in label.upper():
                    entry = {'Indicador': label}
                    for ci, mc in enumerate(month_cols[:5]):
                        val = row[cols.index(mc)] if mc in cols else ''
                        entry[mc.title()] = self._to_int(val)
                    # Última columna con dato (total acumulado)
                    total_col = cols[-1] if len(row) > len(month_cols) else None
                    if total_col and str(total_col).strip():
                        entry['Total'] = self._to_int(row[-1])
                    gestion_items.append(entry)
                    break
        if gestion_items:
            result['gestion_mensual'] = pd.DataFrame(gestion_items)

        # Sección 3: Porcentajes
        pct_keywords = ['PORCENTAJE DE DESCONGESTIÓN', 'PORCENTAJE DE DESCONGESTION',
                        'EXTEMPORANEIDAD', 'OPORTUNIDAD']
        pct_items = []
        for row in data:
            label = str(row[0]).strip() if pd.notna(row[0]) else ''
            for kw in pct_keywords:
                if kw in label.upper():
                    entry = {'Indicador': label}
                    for ci, mc in enumerate(month_cols[:5]):
                        val = row[cols.index(mc)] if mc in cols else ''
                        entry[mc.title()] = self._to_pct(val)
                    pct_items.append(entry)
                    break
        if pct_items:
            result['porcentajes'] = pd.DataFrame(pct_items)

        # Sección 4: Extemporáneas-vencidas / Oportunas-en términos
        extra_keywords = ['EXTEMPORANEAS-VENCIDAS', 'EXTEMPORANEAS VENCIDAS',
                          'OPORTUNAS-EN TÉRMINOS', 'OPORTUNAS EN TERMINOS']
        extra_items = []
        for row in data:
            label = str(row[0]).strip() if pd.notna(row[0]) else ''
            for kw in extra_keywords:
                if kw in label.upper():
                    entry = {'Indicador': label}
                    for ci, mc in enumerate(month_cols[:5]):
                        val = row[cols.index(mc)] if mc in cols else ''
                        entry[mc.title()] = self._to_int(val)
                    extra_items.append(entry)
                    break
        if extra_items:
            result['extemporaneas'] = pd.DataFrame(extra_items)

        return result

    @staticmethod
    def _to_float(val):
        try:
            return round(float(str(val).replace(',', '.')), 2)
        except:
            return None

    @staticmethod
    def _to_int(val):
        try:
            return int(float(str(val).replace(',', '.')))
        except:
            return None

    @staticmethod
    def _to_pct(val):
        try:
            return round(float(str(val).replace(',', '.')) * 100, 1)
        except:
            return None
