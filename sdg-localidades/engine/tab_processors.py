"""
SDG Localidades — Procesadores individuales por tab
Cada funcion recibe la ruta de un archivo subido desde un tab especifico
y produce un Excel de salida individual usando los mismos readers del pipeline.
"""
import os
import pandas as pd
from typing import Optional

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

# Expectativas de hojas por tipo (para validacion temprana)
EXPECTED_SHEETS = {
    "pqrs": ["Reporte PQRS"],
    "atenciones": ["SAC_atencion", "tablas"],
    "cert-residencia": [],
    "prop-horizontal": [],
    "encuestas": ["Encuesta", "Nuevo Formato"],
    "doc-extraviados": ["STOCK", "REGISTRADO", "ENTREGADO"],
}


def validate_tab_type(tab_type: str) -> bool:
    """Valida que el tipo de tab sea uno de los permitidos."""
    return tab_type in ALLOWED_TAB_TYPES


def validate_file_content(filepath: str, tab_type: str) -> Optional[str]:
    """Valida rapido que el archivo tenga las hojas esperadas para ese tipo."""
    expected = EXPECTED_SHEETS.get(tab_type, [])
    if not expected:
        return None  # Sin validacion especifica

    try:
        xl = pd.ExcelFile(filepath)
        available = set(xl.sheet_names)
        for exp in expected:
            if not any(exp.lower() in s.lower() for s in available):
                continue  # al menos una coincidencia parcial basta
            return None
        # Si ninguna coincide
        return f"El archivo no parece ser de tipo {tab_type}. Hojas esperadas: {', '.join(expected)}"
    except Exception:
        return "No se pudo leer el archivo. Verifica que sea un Excel valido."


def process_tab(tab_type: str, filepath: str, output_dir: str,
                month: str = "MAYO", year: str = "2026") -> dict:
    """
    Procesa un archivo para un tab especifico.
    Retorna dict con resultado y ruta del archivo generado.
    """
    reader_class = READER_MAP.get(tab_type)
    if not reader_class:
        return {"success": False, "error": f"Tipo de tab no valido: {tab_type}"}

    try:
        reader = reader_class(filepath)
        result = reader.read()

        if not result.success:
            return {"success": False, "error": f"Error leyendo archivo: {'; '.join(result.errors)}"}

        normalizer = Normalizer()
        normalized = {}
        for sheet_name, df in result.sheets.items():
            normalized[sheet_name] = normalizer.normalize(df, source=tab_type, sheet=sheet_name)

        # Procesamiento especifico por tipo
        extra_data = {}
        if tab_type == "pqrs":
            dedup = Deduplicator()
            for sname, ndf in normalized.items():
                if "peticion" in sname.lower() or "pqrs" in sname.lower():
                    deduped = dedup.find_duplicates(ndf, id_column="Numero peticion")
                    if deduped is not None:
                        normalized[sname] = deduped
                        extra_data["duplicates"] = int(deduped["_duplicado"].sum()) if "_duplicado" in deduped.columns else 0
                    break
            pivot_gen = PivotGenerator()
            for sname, ndf in normalized.items():
                if "pqrs" in sname.lower():
                    pivots = pivot_gen.generate_all(ndf)
                    extra_data["pivots"] = pivots
                    extra_data["pivot_count"] = len(pivots)
                    break

        elif tab_type == "doc-extraviados":
            side = SideReport()
            side_data = side.generate({"side": result})
            extra_data["side_report"] = side_data
            extra_data["section_count"] = len(side_data)

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

        return {
            "success": True,
            "output_path": output_path,
            "filename": os.path.basename(output_path),
            "rows": row_count,
            "sheets": sheet_count,
            "extra": safe_extra
        }

    except Exception as e:
        return {"success": False, "error": str(e)}
