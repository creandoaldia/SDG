"""
SDG Localidades — Procesadores individuales por tab
Cada funcion recibe la ruta de un archivo subido desde un tab especifico
y produce un Excel de salida individual usando los mismos readers del pipeline.
Incluye callback de progreso y métricas reales para dashboard (Juicio: DASH-003).
"""
import os
import pandas as pd
from typing import Optional, Callable

from engine.models import IngestionResult
from engine.ingest.pqrs_reader import PQRSReader
from engine.ingest.sac_reader import SACReader
from engine.ingest.side_reader import SIDEWriter
from engine.ingest.cr_reader import CRReader
from engine.ingest.ph_reader import PHReader
from engine.ingest.encuestas_reader import EncuestasReader
from engine.transform.normalizer import Normalizer
from engine.transform.deduplicator import Deduplicator
from engine.transform.pivot_generator import PivotGenerator
from engine.transform.side_report import SideReport
from engine.load.tab_excel_writer import TabExcelWriter


# ── Reader Factory (compartido con pipeline.py) ──
READER_MAP = {
    "pqrs": PQRSReader,
    "atenciones": SACReader,
    "cert-residencia": CRReader,
    "prop-horizontal": PHReader,
    "encuestas": EncuestasReader,
    "doc-extraviados": SIDEWriter,
}

ALLOWED_TAB_TYPES = set(READER_MAP.keys())

# Expectativas de hojas por tipo (con matching parcial — Juicio: TABHANDLER-002)
EXPECTED_SHEETS = {
    "pqrs": ["Reporte PQRS"],
    "atenciones": ["SAC_atencion", "tablas"],
    "cert-residencia": ["CERT RESIDENCIA PROD", "CR-TIPO TRAMITE"],
    "prop-horizontal": ["CERT.P.HORIZONTAL"],
    "encuestas": ["Encuesta", "Nuevo Formato"],
    "doc-extraviados": ["STOCK", "REGISTRADO", "ENTREGADO"],
}


def validate_tab_type(tab_type: str) -> bool:
    """Valida que el tipo de tab sea uno de los permitidos."""
    return tab_type in ALLOWED_TAB_TYPES


def validate_file_content(filepath: str, tab_type: str) -> Optional[str]:
    """Valida rapido que el archivo tenga las hojas esperadas para ese tipo.
    Usa matching parcial (case-insensitive) para soportar sufijos de mes."""
    expected = EXPECTED_SHEETS.get(tab_type, [])
    if not expected:
        return None  # Sin validacion especifica

    try:
        xl = pd.ExcelFile(filepath)
        available = set(xl.sheet_names)
        # Matching parcial: cada expected debe aparecer en al menos un sheet
        for exp in expected:
            exp_lower = exp.lower()
            if not any(exp_lower in s.lower() for s in available):
                return f"El archivo no parece ser de tipo {tab_type}. Hojas esperadas: {', '.join(expected)}"
        return None
    except Exception:
        return "No se pudo leer el archivo. Verifica que sea un Excel valido."


def process_tab(tab_type: str, filepath: str, output_dir: str,
                month: str = "MAYO", year: str = "2026",
                progress_callback: Optional[Callable[[float, str], None]] = None) -> dict:
    """
    Procesa un archivo para un tab especifico.
    Retorna dict con resultado, ruta del archivo generado, y summary con métricas reales.

    Args:
        progress_callback: Callable(progress: 0.0-1.0, message: str) for UI updates
    """
    def _progress(p: float, msg: str = ''):
        if progress_callback:
            progress_callback(p, msg)

    reader_class = READER_MAP.get(tab_type)
    if not reader_class:
        return {"success": False, "error": f"Tipo de tab no valido: {tab_type}"}

    try:
        _progress(0.1, 'Leyendo archivo...')
        reader = reader_class(filepath)
        result = reader.read()

        if not result.success:
            return {"success": False, "error": f"Error leyendo archivo: {'; '.join(result.errors)}"}

        _progress(0.3, 'Normalizando datos...')
        normalizer = Normalizer()
        normalized = {}
        for sheet_name, df in result.sheets.items():
            normalized[sheet_name] = normalizer.normalize(df, source=tab_type, sheet=sheet_name)

        # Procesamiento especifico por tipo
        extra_data = {}
        summary = {'total': result.row_count, 'sheets': len(result.sheets)}

        if tab_type == "pqrs":
            _progress(0.5, 'Detectando duplicados...')
            dedup = Deduplicator()
            for sname, ndf in normalized.items():
                if "peticion" in sname.lower() or "pqrs" in sname.lower():
                    deduped = dedup.find_duplicates(ndf, id_column="Numero peticion")
                    if deduped is not None:
                        normalized[sname] = deduped
                        dups = int(deduped["_duplicado"].sum()) if "_duplicado" in deduped.columns else 0
                        extra_data["duplicates"] = dups
                        summary['duplicados'] = dups
                        # Extraer gestionadas/pendientes reales si la columna existe
                        if "gestionada" in ' '.join(ndf.columns).lower():
                            try:
                                gest_col = [c for c in ndf.columns if 'gestion' in c.lower()][0]
                                summary['gestionadas'] = int(ndf[gest_col].notna().sum())
                                summary['pendientes'] = max(0, result.row_count - summary['gestionadas'])
                            except (IndexError, Exception):
                                summary['gestionadas'] = result.row_count
                                summary['pendientes'] = 0
                        else:
                            summary['gestionadas'] = result.row_count
                            summary['pendientes'] = 0
                    break

            _progress(0.7, 'Generando tablas dinámicas...')
            pivot_gen = PivotGenerator()
            for sname, ndf in normalized.items():
                if "pqrs" in sname.lower():
                    pivots = pivot_gen.generate_all(ndf)
                    extra_data["pivots"] = pivots
                    extra_data["pivot_count"] = len(pivots)
                    summary['pivot_count'] = len(pivots)
                    break

        elif tab_type == "doc-extraviados":
            _progress(0.5, 'Generando reporte SIDE...')
            side = SideReport()
            side_data = side.generate({"side": result})
            extra_data["side_report"] = side_data
            extra_data["section_count"] = len(side_data)
            # Extraer métricas reales del SideReport
            summary['secciones'] = len(side_data)
            summary['stock'] = 0
            summary['registrados'] = 0
            summary['entregados'] = 0
            for section in side_data:
                if 'stock' in str(section).lower():
                    summary['stock'] += 1
                if 'registrado' in str(section).lower():
                    summary['registrados'] += 1
                if 'entregado' in str(section).lower():
                    summary['entregados'] += 1
            # Si no hay breakdown por nombre, usar counts reales
            for sname, ndf in normalized.items():
                sname_lower = sname.lower()
                if 'stock' in sname_lower:
                    summary['stock'] = len(ndf)
                elif 'registrado' in sname_lower:
                    summary['registrados'] = len(ndf)
                elif 'entregado' in sname_lower:
                    summary['entregados'] = len(ndf)

        elif tab_type == "encuestas":
            _progress(0.5, 'Analizando encuestas...')
            # Extraer completas vs total de las hojas normalizadas
            total_encuestas = result.row_count
            completas = 0
            for sname, ndf in normalized.items():
                # Buscar columna que indique completitud
                for col in ndf.columns:
                    col_lower = str(col).lower()
                    if 'completa' in col_lower or 'respondio' in col_lower or 'estado' in col_lower:
                        try:
                            completas = int(ndf[col].notna().sum())
                        except Exception:
                            pass
                        break
            summary['total'] = total_encuestas
            summary['completas'] = completas or max(0, total_encuestas)

        _progress(0.9, 'Generando Excel...')
        # Generar Excel individual
        writer = TabExcelWriter()
        output_path = os.path.join(output_dir, f"INFORME_{tab_type.upper()}_{month}_{year}.xlsx")
        writer.write(tab_type, result, normalized, extra_data, output_path, month, year)

        row_count = result.row_count
        sheet_count = len(result.sheets)

        # Extraer solo datos serializables (no DataFrames)
        safe_extra = {}
        for k, v in extra_data.items():
            if isinstance(v, (int, float, str, bool, list, dict)):
                safe_extra[k] = v
            else:
                safe_extra[k] = str(type(v).__name__)

        _progress(1.0, 'Completado')

        return {
            "success": True,
            "output_path": output_path,
            "filename": os.path.basename(output_path),
            "rows": row_count,
            "sheets": sheet_count,
            "extra": safe_extra,
            "summary": summary,  # Métricas reales para dashboard
        }

    except Exception as e:
        return {"success": False, "error": str(e)}
