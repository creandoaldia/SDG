"""
SDG Localidades — Generador de RESUMEN CIFRAS v5
Construye la hoja resumen con el mismo formato que Yesenia usa en su PPT:
11 columnas: LOCALIDAD, PQRS GESTIONADAS, PQRS PENDIENTES, DOC.EXT.,
ORIENTACIONES, CERT. PROPIEDAD HORIZONTAL, CERT. RESIDENCIA,
ENCUESTAS DEL PERIODO, ENCUESTAS CON RESPUESTA COMPLETA,
CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN,
% PARTICIPACIÓN DE PERCEPCIÓN Y SATISFACCIÓN X LOCALIDAD

Cambios clave v5:
- PQRS contadas por DEPENDENCIA (no Localidad de los hechos)
  usando la columna 'Tipo reporte' para separar gestionadas/pendientes
- CR total (no desglosado)
- PH total (no desglosado)
- Encuestas incluidas con calificaciones
- Nombres de columnas exactamente como Yesenia los usa
"""
import pandas as pd
import unidecode
from engine.models import LOCALIDADES


def _norm(s):
    if pd.isna(s):
        return ''
    return unidecode.unidecode(str(s).strip().upper())


# Mapeo de Dependencia -> LOCALIDAD (nombre normalizado)
DEP_TO_LOCALIDAD = {
    "ALCALDIA LOCAL DE ANTONIO NARINO": "ANTONIO NARINO",
    "ALCALDIA LOCAL DE BARRIOS UNIDOS": "BARRIOS UNIDOS",
    "ALCALDIA LOCAL DE BOSA": "BOSA",
    "ALCALDIA LOCAL DE CANDELARIA": "CANDELARIA",
    "ALCALDIA LOCAL DE CHAPINERO": "CHAPINERO",
    "ALCALDIA LOCAL DE CIUDAD BOLIVAR": "CIUDAD BOLIVAR",
    "ALCALDIA LOCAL DE ENGATIVA": "ENGATIVA",
    "ALCALDIA LOCAL DE FONTIBON": "FONTIBON",
    "ALCALDIA LOCAL DE KENNEDY": "KENNEDY",
    "ALCALDIA LOCAL DE MARTIRES": "MARTIRES",
    "ALCALDIA LOCAL DE PUENTE ARANDA": "PUENTE ARANDA",
    "ALCALDIA LOCAL DE RAFAEL URIBE": "RAFAEL URIBE URIBE",
    "ALCALDIA LOCAL DE SAN CRISTOBAL": "SAN CRISTOBAL",
    "ALCALDIA LOCAL DE SANTA FE": "SANTA FE",
    "ALCALDIA LOCAL DE SUBA": "SUBA",
    "ALCALDIA LOCAL DE SUMAPAZ": "SUMAPAZ",
    "ALCALDIA LOCAL DE TEUSAQUILLO": "TEUSAQUILLO",
    "ALCALDIA LOCAL DE TUNJUELITO": "TUNJUELITO",
    "ALCALDIA LOCAL DE USAQUEN": "USAQUEN",
    "ALCALDIA LOCAL DE USME": "USME",
}

# Mapeo inverso: localidad normalizada -> prefijo en Dependencia
# Dependencias no-locales se mapean asi:
# "OFICINA DE ATENCION A LA CIUDADANIA" -> "NIVEL CENTRAL"
# "DEPENDENCIAS NIVEL CENTRAL" -> "NIVEL CENTRAL"
# "OFICINA ASUNTOS DISCIPLINARIOS" -> "NIVEL CENTRAL"


class ResumenCifras:

    # Columnas exactas del formato Yesenia
    COLUMNS = [
        'LOCALIDAD',
        'PQRS GESTIONADAS',
        'PQRS PENDIENTES',
        'DOC.EXT.',
        'ORIENTACIONES',
        'CERT. PROPIEDAD HORIZONTAL',
        'CERT. RESIDENCIA',
        'ENCUESTAS DEL PERIODO',
        'ENCUESTAS CON RESPUESTA COMPLETA',
        'CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS',
        '% PARTICIPACIÓN DE PERCEPCIÓN Y SATISFACCIÓN X LOCALIDAD'
    ]

    def build(self, ingestion_data: dict, normalized: dict,
              indicators: dict, pivots: dict) -> pd.DataFrame:
        # --- 1. PQRS: contar por Dependencia usando Tipo reporte ---
        pqrs_data = self._count_pqrs_by_dependencia(ingestion_data)

        # --- 2. SIDE: total DOC.EXT. por localidad ---
        side_data_raw = self._count_side_all(ingestion_data)

        # --- 3. ORIENTACIONES (SAC) ---
        sac_data = self._extract_sac_all(ingestion_data)

        # --- 4. CR total ---
        cr_data = self._extract_cr_total(ingestion_data)

        # --- 5. PH total ---
        ph_data = self._extract_ph_total(ingestion_data)

        # --- 6. Encuestas ---
        enc_data = self._extract_encuestas(ingestion_data)

        # --- 7. Armar fila por localidad ---
        rows = []
        total_gestionadas = 0
        total_pendientes = 0
        total_enc_completas = 0

        for localidad in LOCALIDADES:
            loc_norm = _norm(localidad)
            row = {'LOCALIDAD': localidad}

            # PQRS
            row['PQRS GESTIONADAS'] = pqrs_data.get(loc_norm, {}).get('gestionadas', 0)
            row['PQRS PENDIENTES'] = pqrs_data.get(loc_norm, {}).get('pendientes', 0)

            # SIDE (DOC.EXT.)
            row['DOC.EXT.'] = side_data_raw.get(loc_norm, 0)

            # SAC (ORIENTACIONES)
            row['ORIENTACIONES'] = sac_data.get(loc_norm, 0)

            # PH total
            row['CERT. PROPIEDAD HORIZONTAL'] = ph_data.get(loc_norm, 0)

            # CR total
            row['CERT. RESIDENCIA'] = cr_data.get(loc_norm, 0)

            # Encuestas
            enc_info = enc_data.get(loc_norm, {})
            row['ENCUESTAS DEL PERIODO'] = enc_info.get('total', 0)
            row['ENCUESTAS CON RESPUESTA COMPLETA'] = enc_info.get('completas', 0)
            row['CALIFICACIÓN DE PERCEPCIÓN Y SATISFACCIÓN DE ENCUESTAS'] = enc_info.get('calificacion', 0.0)
            row['% PARTICIPACIÓN DE PERCEPCIÓN Y SATISFACCIÓN X LOCALIDAD'] = enc_info.get('participacion', 0.0)

            total_gestionadas += row['PQRS GESTIONADAS']
            total_pendientes += row['PQRS PENDIENTES']
            total_enc_completas += enc_info.get('completas', 0)

            rows.append(row)

        df = pd.DataFrame(rows, columns=self.COLUMNS)

        # Calcular % participación global
        for i, row_data in enumerate(rows):
            completas = row_data['ENCUESTAS CON RESPUESTA COMPLETA']
            if total_enc_completas > 0:
                pct = (completas / total_enc_completas) * 100
            else:
                pct = 0.0
            df.at[i, '% PARTICIPACIÓN DE PERCEPCIÓN Y SATISFACCIÓN X LOCALIDAD'] = round(pct, 2)

        # Llenar NaN con 0 y convertir tipos numericos
        df = df.fillna(0)
        for c in df.columns:
            if c == 'LOCALIDAD':
                continue
            if 'CALIFICACIÓN' in c or '% PARTICIPACIÓN' in c:
                df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0.0).round(2)
            else:
                df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0).astype(int)

        return df

    # ═══════════════════════════════════════════════════════════════
    # PQRS: contar por Dependencia, separar por Tipo reporte
    # ═══════════════════════════════════════════════════════════════

    def _count_pqrs_by_dependencia(self, ingestion_data: dict) -> dict:
        """
        Cuenta PQRS por Dependencia (columna 'Dependencia').
        Separa GESTIONADAS/PENDIENTES usando columna 'Tipo reporte'.
        """
        if 'pqrs' not in ingestion_data:
            return {}

        sheets = ingestion_data['pqrs'].sheets
        df = sheets.get('Reporte PQRS Mayo2026')
        if df is None or df.empty:
            return {}

        if 'Dependencia' not in df.columns or 'Tipo reporte' not in df.columns:
            return {}

        result = {}
        df = df.copy()
        df['_dep_upper'] = df['Dependencia'].astype(str).str.strip().str.upper()
        df['_tipo_reporte'] = df['Tipo reporte'].astype(str).str.strip().str.upper()

        # Agrupar por Dependencia
        for dep, group in df.groupby('_dep_upper'):
            # Mapear dependencia a localidad
            loc_norm = self._dep_to_loc_norm(dep)
            if loc_norm is None:
                continue

            if loc_norm not in result:
                result[loc_norm] = {'gestionadas': 0, 'pendientes': 0}

            gestionadas = len(group[group['_tipo_reporte'] == 'GESTIONADOS'])
            pendientes = len(group[group['_tipo_reporte'] == 'PENDIENTE'])

            result[loc_norm]['gestionadas'] += gestionadas
            result[loc_norm]['pendientes'] += pendientes

        return result

    def _dep_to_loc_norm(self, dep_upper: str) -> str:
        """Mapea nombre de Dependencia a localidad normalizada."""
        # Coincidencia exacta con DEP_TO_LOCALIDAD
        if dep_upper in DEP_TO_LOCALIDAD:
            return _norm(DEP_TO_LOCALIDAD[dep_upper])

        # OFICINA DE ATENCION A LA CIUDADANIA -> NIVEL CENTRAL
        if 'OFICINA DE ATENCION' in dep_upper or 'OFICINA ASUNTOS' in dep_upper:
            return _norm('NIVEL CENTRAL')

        # DEPENDENCIAS NIVEL CENTRAL -> NIVEL CENTRAL
        if 'NIVEL CENTRAL' in dep_upper:
            return _norm('NIVEL CENTRAL')

        return None

    # ═══════════════════════════════════════════════════════════════
    # SIDE: DOC.EXT. (total documentos extraviados)
    # ═══════════════════════════════════════════════════════════════

    def _count_side_all(self, ingestion_data: dict) -> dict:
        """Cuenta documentos SIDE por localidad desde datos crudos.
        Busca 'LOCALIDAD' en los datos y suma TOTAL por localidad.
        Solo procesa filas de sub-total (col0=tipo documento), saltando
        filas de detalle (col0=NaN) y la fila 'Total general'.
        """
        if 'side' not in ingestion_data:
            return {}
        sheets = ingestion_data['side'].sheets
        result = {}

        # Palabras a ignorar en columna 0
        SKIP_WORDS = {'TOTAL GENERAL', 'TOTAL', 'STOCK', 'TIPO DE DOCUMENTO',
                      'NAN', 'REGISTRADO SIDE', 'ENTREGADO SIDE'}

        for sname in sheets:
            df = sheets[sname].copy()
            if df is None or df.empty:
                continue

            rows_data = df.values.tolist()

            # Encontrar LOCALIDAD y TOTAL en filas
            loc_col_idx = None
            total_col_idx = None
            for i, row in enumerate(rows_data):
                for j, cell in enumerate(row):
                    cell_str = str(cell).strip().upper() if pd.notna(cell) else ''
                    if cell_str == 'LOCALIDAD':
                        loc_col_idx = j
                    if cell_str == 'TOTAL':
                        total_col_idx = j

            if loc_col_idx is None:
                continue

            # Contar: solo filas con tipo documento en col0 y localidad valida
            for row in rows_data:
                if loc_col_idx >= len(row):
                    continue
                # col0 debe tener un valor (tipo de documento), no NaN
                col0 = str(row[0]).strip().upper() if len(row) > 0 and pd.notna(row[0]) else ''
                if not col0 or col0 in SKIP_WORDS:
                    continue

                loc_val = str(row[loc_col_idx]).strip() if pd.notna(row[loc_col_idx]) else ''
                if not loc_val or loc_val.upper() == 'NAN':
                    continue

                loc_norm = _norm(loc_val)
                matched = self._match_locality(loc_norm)
                if matched is None:
                    continue

                # Sumar valor de columna TOTAL si existe
                if total_col_idx is not None and total_col_idx < len(row):
                    cell_total = row[total_col_idx]
                    if pd.notna(cell_total):
                        val = pd.to_numeric(cell_total, errors='coerce')
                        if pd.notna(val) and val > 0:
                            result[matched] = result.get(matched, 0) + int(val)
                            continue
                result[matched] = result.get(matched, 0) + 1

        return result

    # ═══════════════════════════════════════════════════════════════
    # SAC: ORIENTACIONES
    # ═══════════════════════════════════════════════════════════════

    def _extract_sac_all(self, ingestion_data: dict) -> dict:
        """Cuenta atenciones SAC (ORIENTACIONES) por localidad."""
        if 'sac' not in ingestion_data:
            return {}
        sheets = ingestion_data['sac'].sheets
        if 'Mayo SAC_atencion' not in sheets:
            return {}
        try:
            df = sheets['Mayo SAC_atencion'].copy()
            if df is None or df.empty:
                return {}

            punto_col = None
            for c in df.columns:
                c_norm = unidecode.unidecode(str(c).lower())
                if 'punto' in c_norm and 'atencion' in c_norm:
                    punto_col = c
                    break
            if not punto_col:
                return {}

            result = {}

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
                    return resto.title() if resto else None
                if 'supercade' in pl or 'super cade' in pl:
                    return 'SUPERCADES'
                if 'nivel central' in pl:
                    return 'NIVEL CENTRAL'
                return p.title()

            df['_localidad'] = df[punto_col].apply(extract_localidad)
            df = df[df['_localidad'].notna()]
            df['_loc_norm'] = df['_localidad'].apply(_norm)

            for _, row in df.iterrows():
                loc_norm = row['_loc_norm']
                matched = self._match_locality(loc_norm)
                if matched:
                    result[matched] = result.get(matched, 0) + 1
            return result
        except Exception:
            return {}

    # ═══════════════════════════════════════════════════════════════
    # CR: total CERT. RESIDENCIA
    # ═══════════════════════════════════════════════════════════════

    def _extract_cr_total(self, ingestion_data: dict) -> dict:
        """Suma todos los CR (aprobados + pendientes + rechazados) por localidad."""
        if 'cr' not in ingestion_data:
            return {}
        result = {}
        for loc_norm in [_norm(l) for l in LOCALIDADES]:
            cr_data = self._extract_cr(ingestion_data, loc_norm)
            total = (cr_data.get('CR_APROBADOS', 0) +
                     cr_data.get('CR_PENDIENTES', 0) +
                     cr_data.get('CR_RECHAZADOS', 0))
            if total > 0:
                result[loc_norm] = total
        return result

    # ── CR: extract (reuse original logic) ──

    def _extract_cr(self, ingestion_data, loc_norm):
        """Original CR extraction - returns dict with CR_APROBADOS, _PENDIENTES, _RECHAZADOS."""
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
                    r = {}
                    if col_aprobado is not None and col_aprobado < len(row):
                        r['CR_APROBADOS'] = self._parse_int(row[col_aprobado])
                    if col_pendiente is not None and col_pendiente < len(row):
                        r['CR_PENDIENTES'] = self._parse_int(row[col_pendiente])
                    if col_rechazado is not None and col_rechazado < len(row):
                        r['CR_RECHAZADOS'] = self._parse_int(row[col_rechazado])
                    return r
        return {}

    # ═══════════════════════════════════════════════════════════════
    # PH: total CERT. PROPIEDAD HORIZONTAL
    # ═══════════════════════════════════════════════════════════════

    def _extract_ph_total(self, ingestion_data: dict) -> dict:
        """Suma PH inscripciones + actualizaciones por localidad."""
        result = {}
        for loc_norm in [_norm(l) for l in LOCALIDADES]:
            ph_data = self._extract_ph_raw(ingestion_data, loc_norm)
            total = (ph_data.get('PH_INSCRIPCIONES', 0) +
                     ph_data.get('PH_ACTUALIZACIONES', 0))
            if total > 0:
                result[loc_norm] = total
        return result

    # ── PH: extract (reuse original logic) ──

    def _extract_ph_raw(self, ingestion_data: dict, loc_norm: str):
        """Original PH extraction."""
        result = {}
        if 'ph' not in ingestion_data:
            return result
        sheets = ingestion_data['ph'].sheets
        try:
            if 'BASE-I' in sheets:
                df_i = sheets['BASE-I'].copy()
                for col in df_i.columns:
                    mask_localidad = df_i[col].astype(str).str.contains('Localidad', case=False, na=False)
                    if mask_localidad.any():
                        header_idx = mask_localidad.idxmax()
                        df_i.columns = df_i.iloc[header_idx].values
                        df_i = df_i.iloc[header_idx + 1:].reset_index(drop=True)
                        break
                if 'Localidad' in df_i.columns:
                    df_i['_loc'] = df_i['Localidad'].astype(str).apply(_norm)
                    count_i = len(df_i[df_i['_loc'].str.contains(loc_norm, case=False, na=False)])
                    if count_i > 0:
                        result['PH_INSCRIPCIONES'] = count_i
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

    # ═══════════════════════════════════════════════════════════════
    # ENCUESTAS: total, completas, calificación promedio
    # ═══════════════════════════════════════════════════════════════

    def _extract_encuestas(self, ingestion_data: dict) -> dict:
        """
        Extrae datos de encuestas por localidad.
        Columnas relevantes:
        - 'Localidad donde realiza el servicio'
        - 'Tipo' -> 'Completa' / 'Incompleta'
        - '1. En una escala de 1 a 5... ¿Qué tan satisfecho esta con el servicio recibido?'
          (o similar columna de calificación)
        """
        if 'encuestas' not in ingestion_data:
            return {}
        sheets = ingestion_data['encuestas'].sheets
        df = sheets.get('Nuevo Formato Encuesta')
        if df is None or df.empty:
            return {}

        # Encontrar columna de localidad
        loc_col = None
        calif_col = None
        for c in df.columns:
            c_str = unidecode.unidecode(str(c).lower())
            if 'localidad' in c_str and ('servicio' in c_str or 'realiza' in c_str):
                loc_col = c
            if 'escala' in c_str and 'satisfecho' in c_str:
                calif_col = c

        if not loc_col:
            return {}

        result = {}
        tipo_col = 'Tipo' if 'Tipo' in df.columns else None

        df = df.copy()
        df['_loc'] = df[loc_col].astype(str).apply(_norm)

        for loc_norm in [_norm(l) for l in LOCALIDADES]:
            subset = df[df['_loc'].str.contains(loc_norm, case=False, na=False)]
            if subset.empty:
                continue

            total_enc = len(subset)
            completas = len(subset[subset[tipo_col] == 'Completa']) if tipo_col else total_enc

            # Calificación promedio
            calif_prom = 0.0
            if calif_col and calif_col in subset.columns:
                calif_vals = pd.to_numeric(subset[calif_col], errors='coerce').dropna()
                if not calif_vals.empty:
                    calif_prom = round(calif_vals.mean(), 2)

            result[loc_norm] = {
                'total': total_enc,
                'completas': completas,
                'calificacion': calif_prom,
                'participacion': 0.0  # se calcula globalmente despues
            }

        return result

    # ═══════════════════════════════════════════════════════════════
    # Helpers
    # ═══════════════════════════════════════════════════════════════

    def _match_locality(self, loc_norm: str) -> str:
        """Busca coincidencia de loc_norm contra lista de LOCALIDADES."""
        for loc in [_norm(l) for l in LOCALIDADES]:
            if loc_norm in loc or loc in loc_norm:
                return loc
        return None

    def _parse_int(self, s):
        try:
            return int(float(str(s).replace(',', '.').replace(' ', '')))
        except:
            return 0
