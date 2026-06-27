"""
SDG Localidades — Generador de RESUMEN CIFRAS v4
Construye la hoja resumen que consolida todos los indicadores del mes.

BASADO EN ANALISIS DE VIDEO (8,467 frames) + DATOS CRUDOS:
- PQRS: pivots Q1/Q4 desde sabana de datos
- CR: hoja Productividad-CR (pivot precalculado por localidad)
- PH: datos crudos BASE-I y BASE-A agregados por Localidad
- SIDE: datos crudos REGISTRADO SIDE agregados por LOCALIDAD
- SAC: datos crudos Mayo SAC_atencion agregados por LOCALIDAD desde columna Punto atención
"""
import pandas as pd
import unidecode
from engine.models import LOCALIDADES


def _norm(s):
    if pd.isna(s):
        return ''
    return unidecode.unidecode(str(s).strip().upper())


class ResumenCifras:

    def build(self, ingestion_data: dict, normalized: dict,
              indicators: dict, pivots: dict) -> pd.DataFrame:
        rows = []
        for localidad in LOCALIDADES:
            row = {'LOCALIDAD': localidad}
            loc_norm = _norm(localidad)

            row['PQRS_GESTIONADAS'] = self._get_pivot_val(pivots, 'Q1_Total_Solicitudes', loc_norm)
            row['PQRS_CERRADAS'] = self._get_pivot_val(pivots, 'Q4_Cerradas', loc_norm)

            cr_data = self._extract_cr(ingestion_data, loc_norm)
            row.update(cr_data)

            # PH: desde datos crudos (BASE-I, BASE-A)
            ph_data = self._extract_ph_raw(ingestion_data, loc_norm)
            row.update(ph_data)

            # SIDE: desde datos crudos (REGISTRADO SIDE)
            side_val = self._extract_side_raw(ingestion_data, loc_norm)
            if side_val is not None:
                row['SIDE_REGISTRADOS'] = side_val

            # SAC: desde datos crudos de atenciones (Mayo SAC_atencion)
            sac_val = self._extract_sac_raw(ingestion_data, loc_norm)
            if sac_val is not None:
                row['ATENCIONES_SAC'] = sac_val

            rows.append(row)

        df = pd.DataFrame(rows).fillna(0)
        for c in df.columns:
            if c != 'LOCALIDAD':
                df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0).astype(int)
        return df

    # ── CR: desde pivot Productividad-CR ──

    def _extract_cr(self, ingestion_data, loc_norm):
        if 'cr' not in ingestion_data:
            return {}
        sheets = ingestion_data['cr'].sheets
        for sname in ['Productividad-CR', 'Hoja1']:
            if sname not in sheets:
                continue
            df = sheets[sname]
            rows_data = [[str(v).strip() for v in r] for _, r in df.iterrows()]
            if len(rows_data) < 2:
                continue
            hdr_idx = None
            for i, row in enumerate(rows_data):
                if any('APROBADO' in c.upper() or 'PENDIENTE' in c.upper() or 'RECHAZADO' in c.upper() for c in row):
                    hdr_idx = i
                    break
            if hdr_idx is None:
                continue
            header = rows_data[hdr_idx]
            col_aprobado = next((i for i, h in enumerate(header) if 'APROBADO' in h.upper()), None)
            col_pendiente = next((i for i, h in enumerate(header) if 'PENDIENTE' in h.upper() and 'APROBADO' not in h.upper()), None)
            col_rechazado = next((i for i, h in enumerate(header) if 'RECHAZADO' in h.upper()), None)
            if col_aprobado is None:
                continue
            for row in rows_data[hdr_idx + 1:]:
                if not row:
                    continue
                first = _norm(row[0])
                if loc_norm in first or first in loc_norm:
                    result = {}
                    if col_aprobado is not None and col_aprobado < len(row):
                        result['CR_APROBADOS'] = self._parse_int(row[col_aprobado])
                    if col_pendiente is not None and col_pendiente < len(row):
                        result['CR_PENDIENTES'] = self._parse_int(row[col_pendiente])
                    if col_rechazado is not None and col_rechazado < len(row):
                        result['CR_RECHAZADOS'] = self._parse_int(row[col_rechazado])
                    return result
        return {}

    # ── PH: desde datos crudos BASE-I y BASE-A ──

    def _extract_ph_raw(self, ingestion_data: dict, loc_norm: str):
        """Cuenta casos PH por localidad desde datos ya cargados en pipeline."""
        result = {}
        if 'ph' not in ingestion_data:
            return result
        sheets = ingestion_data['ph'].sheets

        try:
            # BASE-I: Inscripciones
            if 'BASE-I' in sheets:
                df_i = sheets['BASE-I'].copy()
                # El reader usa header=None, columnas son 0,1,2... buscar "Localidad" en datos
                for col in df_i.columns:
                    mask_localidad = df_i[col].astype(str).str.contains('Localidad', case=False, na=False)
                    if mask_localidad.any():
                        # La fila con "Localidad" es el header real
                        header_idx = mask_localidad.idxmax()
                        df_i.columns = df_i.iloc[header_idx].values
                        df_i = df_i.iloc[header_idx + 1:].reset_index(drop=True)
                        break
                if 'Localidad' in df_i.columns:
                    df_i['_loc'] = df_i['Localidad'].astype(str).apply(_norm)
                    count_i = len(df_i[df_i['_loc'].str.contains(loc_norm, case=False, na=False)])
                    if count_i > 0:
                        result['PH_INSCRIPCIONES'] = count_i

            # BASE-A: Actualizaciones
            if 'BASE-A' in sheets:
                df_a = sheets['BASE-A'].copy()
                for col in df_a.columns:
                    mask_localidad = df_a[col].astype(str).str.contains('Localidad', case=False, na=False)
                    if mask_localidad.any():
                        header_idx = mask_localidad.idxmax()
                        df_a.columns = df_a.iloc[header_idx].values
                        df_a = df_a.iloc[header_idx + 1:].reset_index(drop=True)
                        break
                if 'Localidad' in df_a.columns:
                    df_a['_loc'] = df_a['Localidad'].astype(str).apply(_norm)
                    count_a = len(df_a[df_a['_loc'].str.contains(loc_norm, case=False, na=False)])
                    if count_a > 0:
                        result['PH_ACTUALIZACIONES'] = count_a
        except Exception:
            pass

        return result

    # ── SIDE: desde datos crudos REGISTRADO SIDE ──

    def _extract_side_raw(self, ingestion_data: dict, loc_norm: str):
        """Agrega documentos SIDE por localidad desde datos ya cargados en pipeline."""
        if 'side' not in ingestion_data:
            return None
        sheets = ingestion_data['side'].sheets

        # Buscar hoja REGISTRADO SIDE (puede venir como 'REGISTRADO SIDE' o 'Registrado')
        side_sheet = None
        for sname in sheets:
            if 'registrado' in str(sname).lower():
                side_sheet = sname
                break
        if not side_sheet:
            return None

        try:
            df = sheets[side_sheet].copy()
            if df is None or df.empty:
                return None

            # Encontrar columna LOCALIDAD
            loc_col = None
            total_col = None
            for c in df.columns:
                col_str = str(c).strip().lower()
                if 'localidad' in col_str:
                    loc_col = c
                if c == 'TOTAL' or 'total' in col_str:
                    total_col = c

            if loc_col and total_col:
                df['_loc'] = df[loc_col].astype(str).apply(_norm)
                mask = df['_loc'].str.contains(loc_norm, case=False, na=False)
                subset = df[mask]
                if not subset.empty:
                    total = pd.to_numeric(subset[total_col], errors='coerce').sum()
                    return int(total) if total > 0 else None
            elif loc_col:
                df['_loc'] = df[loc_col].astype(str).apply(_norm)
                mask = df['_loc'].str.contains(loc_norm, case=False, na=False)
                return int(mask.sum()) if mask.sum() > 0 else None
        except Exception:
            pass
        return None

    # ── SAC: desde datos crudos de atenciones ──

    def _extract_sac_raw(self, ingestion_data: dict, loc_norm: str):
        """Cuenta atenciones SAC por localidad desde datos ya cargados en pipeline.
        Columna 'Punto atención' contiene valores como:
        - 'Alcaldía local Engativá' -> localidad
        - 'Nivel central' -> NIVEL CENTRAL
        - 'SuperCade Bosa' -> SUPERCADE
        - 'kennedy' -> localidad (sin prefijo)
        """
        if 'sac' not in ingestion_data:
            return None
        sheets = ingestion_data['sac'].sheets
        if 'Mayo SAC_atencion' not in sheets:
            return None

        try:
            df = sheets['Mayo SAC_atencion'].copy()
            if df is None or df.empty:
                return None

            # Encontrar columna Punto atención (con/sin acentos)
            punto_col = None
            for c in df.columns:
                c_norm = unidecode.unidecode(str(c).lower())
                if 'punto' in c_norm and 'atencion' in c_norm:
                    punto_col = c
                    break

            if not punto_col:
                return None

            # Extraer localidad del punto de atención
            def extract_localidad(punto):
                if pd.isna(punto):
                    return None
                p = str(punto).strip()
                pl = p.lower()
                if 'alcaldia local' in pl:
                    resto = p
                    for prefix in ['ALCALDIA LOCAL DE ', 'ALCALDIA LOCAL ']:
                        idx = resto.upper().find(prefix)
                        if idx >= 0:
                            resto = resto[idx + len(prefix):].strip()
                            break
                    if resto:
                        return resto.title()
                    return None
                if 'supercade' in pl or 'super cade' in pl:
                    return 'SUPERCADES'
                if 'nivel central' in pl:
                    return 'NIVEL CENTRAL'
                return p.title()

            df['_localidad'] = df[punto_col].apply(extract_localidad)
            df = df[df['_localidad'].notna()]

            if df.empty:
                return None

            df['_loc_norm'] = df['_localidad'].apply(_norm)
            mask = df['_loc_norm'].str.contains(loc_norm, case=False, na=False)
            count = int(mask.sum())
            return count if count > 0 else None

        except Exception:
            return None

    # ── Helpers ──

    def _get_pivot_val(self, pivots, pivot_key, loc_norm):
        if pivot_key not in pivots:
            return 0
        q = pivots[pivot_key]
        if q is None or q.empty:
            return 0
        col0 = q.columns[0]
        col1 = q.columns[1] if len(q.columns) > 1 else None
        if col1 is None:
            return 0
        for _, row in q.iterrows():
            first = _norm(row[col0])
            if loc_norm in first or first in loc_norm:
                val = row[col1]
                if pd.notna(val):
                    try:
                        return int(float(str(val)))
                    except:
                        pass
        return 0

    def _parse_int(self, s):
        try:
            return int(float(str(s).replace(',', '.').replace(' ', '')))
        except:
            return 0
