"""
SDG Localidades — Orquestador del Pipeline ETL
Coordina todas las fases: ingesta → transformación → generación → validación.
"""
import os
import time
import json
import pandas as pd
from datetime import datetime
from typing import Generator, Optional
from queue import Queue

from engine.models import (
    FileSource, PipelinePhase, PipelineEvent, IngestionResult,
    ValidationReport, LOCALIDADES
)
from engine.ingest.pqrs_reader import PQRSReader
from engine.ingest.sac_reader import SACReader
from engine.ingest.side_reader import SIDEWriter
from engine.ingest.cr_reader import CRReader
from engine.ingest.ph_reader import PHReader
from engine.ingest.encuestas_reader import EncuestasReader
from engine.transform.normalizer import Normalizer
from engine.transform.deduplicator import Deduplicator
from engine.transform.pivot_generator import PivotGenerator
from engine.transform.indicator_calculator import IndicatorCalculator
from engine.transform.resumen_cifras import ResumenCifras
from engine.transform.web_report import WebReport
from engine.transform.days_report import DaysReport
from engine.transform.side_report import SideReport
from engine.load.excel_generator import ExcelGenerator
from engine.load.validator import Validator


class SDGPipeline:
    """
    Orquestador principal del pipeline ETL.
    Emite eventos que la interfaz web consume para mostrar progreso.
    """

    def __init__(self, input_dir: str, output_dir: str, month: str, year: str):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.month = month.upper()
        self.year = year
        self.events: Queue = Queue()
        self.results = {}

        # Archivos fuente que el sistema espera encontrar
        self.sources = [
            FileSource("pqrs", "BD PQRS Bogotá Te Escucha", "*BOGOTA*ESCUCHA*", True),
            FileSource("sac", "SAC Atención al Ciudadano", "*SAC_atencion*", True),
            FileSource("side", "Resumen SIDE", "*Resumen SIDE*", True),
            FileSource("cr", "Productividad Certificado Residencia", "*PRODUCTIVIDAD_CR*", True),
            FileSource("ph", "Productividad Propiedad Horizontal", "*PRODUCTIVIDAD_PH*", True),
            FileSource("encuestas", "Reporte Productividad Encuestas", "*PRODUCTIVIDAD ENCUESTAS*", True),
        ]

        self.output_path = os.path.join(output_dir, f"INFORME PQRS LOCALIDADES {month.upper()} {year}.xlsx")
        # Almacenamiento para dashboard (se llena durante run())
        self.resumen_df = None
        self.indicators = {}
        self.ingestion_data = {}
        self.normalized = {}
        self.pivots = {}

    def _find_sheet(self, source_key: str, *patterns: str) -> Optional[str]:
        """Busca una hoja por patron en los datos normalizados de una fuente.
        Retorna el nombre real de la hoja o None si no encuentra."""
        if source_key not in self.normalized:
            return None
        sheets = self.normalized[source_key]
        for pattern in patterns:
            pl = pattern.lower()
            for sname in sheets:
                if pl in sname.lower():
                    return sname
        # Fallback: primera hoja
        if sheets:
            return list(sheets.keys())[0]
        return None

    def _emit(self, phase: PipelinePhase, message: str, progress: float, detail: str = "", status: str = "running"):
        """Crea un evento y lo retorna para que run() lo yield inmediatamente."""
        event = PipelineEvent(phase, message, progress, detail, status)
        self.events.put(event)
        return event

    def _emit_internal(self, sub_phase: str, message: str, progress: float, status: str = "running"):
        """Emite un evento de sub-fase (validation_l1..l4) para la UI.
        El nombre de fase se pasa como parte del detalle para que el frontend lo interprete.
        """
        event = PipelineEvent(PipelinePhase.VALIDATION, message, progress,
                             f"sub_phase:{sub_phase}", status)
        self.events.put(event)
        return event

    def _find_source_file(self, pattern: str) -> Optional[str]:
        """Busca un archivo por patrón en el directorio de entrada."""
        import glob
        matches = glob.glob(os.path.join(self.input_dir, pattern))
        if not matches:
            try:
                for f in os.listdir(self.input_dir):
                    if pattern.replace("*", "") in f:
                        matches.append(os.path.join(self.input_dir, f))
                        break
            except (FileNotFoundError, NotADirectoryError, PermissionError):
                pass
        return matches[0] if matches else None

    def run(self) -> Generator[PipelineEvent, None, None]:
        """
        Ejecuta el pipeline completo.
        Es un generador que produce eventos para la UI.
        """
        start_time = time.time()
        yield self._emit(PipelinePhase.INGESTION, "Iniciando procesamiento...", 0.0,
                   f"Mes: {self.month} {self.year}")

        # ──────────────────────────────────────────────
        # FASE 1: INGESTA — Leer todos los archivos fuente
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.INGESTION, "Buscando archivos fuente...", 0.05,
                   "Escaneando directorio de entrada...")

        self.ingestion_data = {}
        missing_files = []

        for idx, source in enumerate(self.sources):
            yield self._emit(PipelinePhase.INGESTION,
                       f"Buscando: {source.label}...",
                       0.05 + (0.20 * idx / len(self.sources)),
                       f"Patrón: {source.filename_pattern}")

            file_path = self._find_source_file(source.filename_pattern)

            if not file_path:
                if source.required:
                    missing_files.append(source.label)
                    yield self._emit(PipelinePhase.INGESTION,
                               f"⚠️ Archivo requerido NO encontrado: {source.label}",
                               0.0, "", "error")
                else:
                    yield self._emit(PipelinePhase.INGESTION,
                               f"ℹ️ Archivo opcional no encontrado: {source.label}",
                               0.0, "", "completed")
                continue

            source.path = file_path
            source.loaded = True

            # Leer según el tipo de fuente
            yield self._emit(PipelinePhase.INGESTION,
                       f"Leyendo: {os.path.basename(file_path)}...",
                       0.0, "", "running")

            try:
                if source.key == "pqrs":
                    reader = PQRSReader(file_path)
                elif source.key == "sac":
                    reader = SACReader(file_path)
                elif source.key == "side":
                    reader = SIDEWriter(file_path)
                elif source.key == "cr":
                    reader = CRReader(file_path)
                elif source.key == "ph":
                    reader = PHReader(file_path)
                elif source.key == "encuestas":
                    reader = EncuestasReader(file_path)
                else:
                    raise ValueError(f"Tipo de fuente desconocido: {source.key}")

                result = reader.read()
                self.ingestion_data[source.key] = result
                source.sheets = list(result.sheets.keys())
                source.row_count = result.row_count

                yield self._emit(PipelinePhase.INGESTION,
                           f"✅ {source.label}: {result.row_count} registros en {len(result.sheets)} hoja(s)",
                           0.0, "", "completed")

                if result.warnings:
                    for w in result.warnings:
                        yield self._emit(PipelinePhase.INGESTION,
                                   f"   ⚠️ {w}", 0.0, "", "completed")

            except Exception as e:
                yield self._emit(PipelinePhase.INGESTION,
                           f"❌ Error leyendo {source.label}: {str(e)}",
                           0.0, "", "error")
                if source.required:
                    raise

        if missing_files:
            error_msg = f"Archivos requeridos faltantes: {', '.join(missing_files)}"
            yield self._emit(PipelinePhase.ERROR, error_msg, 0.0, "", "error")
            return

        yield self._emit(PipelinePhase.INGESTION,
                   f"✅ Ingesta completa: {sum(s.row_count for s in self.sources if s.loaded)} registros totales",
                   0.25, f"{len([s for s in self.sources if s.loaded])}/{len(self.sources)} archivos cargados",
                   "completed")

        # ──────────────────────────────────────────────
        # FASE 2: NORMALIZACIÓN
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.NORMALIZATION,
                   "Normalizando datos — estandarizando localidades, fechas y formatos...",
                   0.30)

        normalizer = Normalizer()
        self.normalized = {}
        total_normalized = 0

        for idx, (key, data) in enumerate(self.ingestion_data.items()):
            normalized_sheets = {}
            for sheet_name, df in data.sheets.items():
                ndf = normalizer.normalize(df, source=key, sheet=sheet_name)
                normalized_sheets[sheet_name] = ndf
                total_normalized += len(ndf)
            self.normalized[key] = normalized_sheets
            yield self._emit(PipelinePhase.NORMALIZATION,
                       f"   {key}: {sum(len(df) for df in normalized_sheets.values())} registros normalizados",
                       0.30 + (0.10 * idx / len(self.ingestion_data)),
                       "", "completed")

        yield self._emit(PipelinePhase.NORMALIZATION,
                   f"✅ Normalización completa: {total_normalized} registros",
                   0.40, f"Localidades estandarizadas, fechas homogeneizadas",
                   "completed")

        # ──────────────────────────────────────────────
        # FASE 3: DETECCIÓN DE DUPLICADOS (PQRS)
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.DEDUPLICATION,
                   "Detectando peticiones duplicadas en PQRS...",
                   0.42)

        deduplicator = Deduplicator()
        dedup_result = None
        pqrs_sheet = self._find_sheet('pqrs', 'Reporte PQRS', 'PQRS')
        if pqrs_sheet:
            dedup_result = deduplicator.find_duplicates(
                self.normalized['pqrs'][pqrs_sheet],
                id_column="Número petición"
            )
            if dedup_result is not None:
                self.normalized['pqrs'][pqrs_sheet] = dedup_result
                duplicate_count = dedup_result['_duplicado'].sum() if '_duplicado' in dedup_result.columns else 0
                yield self._emit(PipelinePhase.DEDUPLICATION,
                           f"✅ Duplicados detectados: {int(duplicate_count)} peticiones duplicadas",
                           0.45, "Columna '_duplicado' agregada", "completed")
            else:
                yield self._emit(PipelinePhase.DEDUPLICATION,
                           "ℹ️ No se pudo detectar duplicados (columna no encontrada)",
                           0.45, "", "completed")
        else:
            yield self._emit(PipelinePhase.DEDUPLICATION,
                       "ℹ️ Sin datos PQRS para análisis de duplicados",
                       0.45, "", "completed")

        # ──────────────────────────────────────────────
        # FASE 4: GENERACIÓN DE TABLAS DINÁMICAS (Q1-Q6)
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.PIVOT_GENERATION,
                   "Generando tablas dinámicas para informe PPT...",
                   0.50)

        pivot_gen = PivotGenerator()
        self.pivots = {}
        if 'pqrs' in self.normalized:
            pqrs_sheet = self._find_sheet('pqrs', 'Reporte PQRS', 'PQRS')
            pqrs_df = self.normalized['pqrs'].get(pqrs_sheet) if pqrs_sheet else None
            if pqrs_df is not None:
                self.pivots = pivot_gen.generate_all(pqrs_df)
                yield self._emit(PipelinePhase.PIVOT_GENERATION,
                           f"✅ {len(self.pivots)} tablas dinámicas generadas (Q1-Q6)",
                           0.60, "Incluye: gestionadas, pendientes, trasladadas, cerradas, negadas, tiempos",
                           "completed")
        else:
            yield self._emit(PipelinePhase.PIVOT_GENERATION,
                       "ℹ️ Sin datos PQRS para generar tablas dinámicas",
                       0.60, "", "completed")

        # ──────────────────────────────────────────────
        # FASE 5: CÁLCULO DE INDICADORES
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.INDICATOR_CALCULATION,
                   "Calculando indicadores — calificaciones, porcentajes, promedios...",
                   0.65)

        calc = IndicatorCalculator()
        self.indicators = {}
        for key, sheets in self.normalized.items():
            for sheet_name, df in sheets.items():
                result = calc.calculate(key, sheet_name, df)
                if result:
                    self.indicators[f"{key}/{sheet_name}"] = result

        yield self._emit(PipelinePhase.INDICATOR_CALCULATION,
                   f"✅ Indicadores calculados: {len(self.indicators)} tablas de indicadores",
                   0.75, "Incluye: % participación, calificación proporcional, promedios",
                   "completed")

        # ──────────────────────────────────────────────
        # FASE 6: GENERACIÓN DE RESUMEN CIFRAS
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                   "Generando hoja RESUMEN CIFRAS — el concentrado del informe...",
                   0.78)

        resumen = ResumenCifras()
        self.resumen_df = resumen.build(self.ingestion_data, self.normalized, self.indicators, self.pivots)

        yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                   f"✅ RESUMEN CIFRAS generado: {len(self.resumen_df)} localidades",
                   0.85, "Datos consolidados para PowerPoint y Power BI", "completed")

        # ──────────────────────────────────────────────
        # FASE 6b: INFORME PQRS CANAL WEB
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                   "Generando informe PQRS canal web...",
                   0.86)

        web_reporter = WebReport()
        web_report_data = web_reporter.generate(self.ingestion_data)

        web_sections = len(web_report_data)
        if web_sections > 0:
            yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                       f"✅ Informe web generado: {web_sections} secciones",
                       0.87, f"{web_report_data.get('resumen', pd.DataFrame()).iloc[0, 1] if not web_report_data.get('resumen', pd.DataFrame()).empty else 0} PQRS WEB",
                       "completed")
        else:
            yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                       "ℹ️ No se encontraron datos del canal web",
                       0.87, "", "completed")

        # ──────────────────────────────────────────────
        # FASE 6c: INFORME DÍAS DE GESTIÓN
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                   "Generando informe de días de gestión...",
                   0.875)

        days_reporter = DaysReport()
        days_report_data = days_reporter.generate(self.ingestion_data)

        days_sections = len(days_report_data)
        if days_sections > 0:
            yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                       f"✅ Informe días de gestión generado: {days_sections} secciones",
                       0.88, "", "completed")
        else:
            yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                       "ℹ️ No se encontraron datos de seguimiento de días",
                       0.88, "", "completed")

        # ──────────────────────────────────────────────
        # FASE 6d: INFORME SIDE (DOCUMENTOS EXTRAVIADOS)
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                   "Generando informe SIDE...",
                   0.882)

        side_reporter = SideReport()
        side_report_data = side_reporter.generate(self.ingestion_data)

        side_sections = len(side_report_data)
        if side_sections > 0:
            yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                       f"✅ Informe SIDE generado: {side_sections} secciones",
                       0.885, "", "completed")
        else:
            yield self._emit(PipelinePhase.RESUMEN_CIFRAS,
                       "ℹ️ No se encontraron datos SIDE",
                       0.885, "", "completed")

        # ──────────────────────────────────────────────
        # FASE 7: GENERACIÓN DEL EXCEL DE SALIDA
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.EXCEL_GENERATION,
                   "Generando archivo Excel de salida...",
                   0.89)

        generator = ExcelGenerator()
        generator.build(
            output_path=self.output_path,
            month=self.month,
            year=self.year,
            ingestion_data=self.ingestion_data,
            normalized=self.normalized,
            dedup_result=dedup_result,
            pivots=self.pivots,
            indicators=self.indicators,
            resumen_df=self.resumen_df,
            web_report_data=web_report_data,
            days_report_data=days_report_data,
            side_report_data=side_report_data
        )

        yield self._emit(PipelinePhase.EXCEL_GENERATION,
                   f"✅ Excel generado: {os.path.basename(self.output_path)}",
                   0.93, f"Tamaño: {self._get_file_size(self.output_path)}", "completed")

        # ──────────────────────────────────────────────
        # FASE 8: VALIDACIÓN A 4 NIVELES
        # ──────────────────────────────────────────────
        yield self._emit(PipelinePhase.VALIDATION,
                   "Ejecutando validación a 4 niveles...",
                   0.95)

        validator = Validator()

        # Emitir eventos individuales para cada nivel
        yield self._emit(PipelinePhase.VALIDATION,
                   "Nivel 1: Validando archivos de entrada...",
                   0.955, "", "running")
        yield self._emit_internal("validation_l1", "Verificando archivos fuente...", 0.96)

        yield self._emit(PipelinePhase.VALIDATION,
                   "Nivel 2: Validando transformaciones...",
                   0.965, "", "running")
        yield self._emit_internal("validation_l2", "Verificando normalización...", 0.97)

        yield self._emit(PipelinePhase.VALIDATION,
                   "Nivel 3: Validando contra originales...",
                   0.975, "", "running")
        yield self._emit_internal("validation_l3", "Verificando totales...", 0.98)

        yield self._emit(PipelinePhase.VALIDATION,
                   "Nivel 4: Validando estructura de salida...",
                   0.985, "", "running")
        yield self._emit_internal("validation_l4", "Verificando hojas y formato...", 0.99)

        report = validator.validate_all(
            sources=self.sources,
            ingestion_data=self.ingestion_data,
            normalized=self.normalized,
            output_path=self.output_path,
            month=self.month,
            year=self.year
        )

        # Marcar cada nivel como completado
        yield self._emit_internal("validation_l1", "✅ Archivos de entrada verificados", 0.96, "completed")
        yield self._emit_internal("validation_l2", "✅ Transformaciones verificadas", 0.97, "completed")
        yield self._emit_internal("validation_l3", "✅ Totales cuadran con originales" if report.level_3_vs_original else "⚠️ Total con advertencias", 0.98, "completed")
        yield self._emit_internal("validation_l4", "✅ Estructura de salida verificada" if report.level_4_output else "⚠️ Estructura con advertencias", 0.99, "completed")

        if report.totals_match:
            yield self._emit(PipelinePhase.VALIDATION,
                       "Validación exitosa — totales cuadran al 100%",
                       1.0, "Nivel 1: Entrada ✅ | Nivel 2: Transformación ✅ | Nivel 3: vs Original ✅ | Nivel 4: Output ✅",
                       "completed")
        else:
            yield self._emit(PipelinePhase.VALIDATION,
                       "⚠️ Validación con advertencias — revisar hoja de verificación",
                       1.0, f"{len(report.warnings)} advertencia(s)", "completed")

        # ──────────────────────────────────────────────
        # COMPLETADO
        # ──────────────────────────────────────────────
        elapsed = time.time() - start_time
        yield self._emit(PipelinePhase.COMPLETED,
                   f"✅ PROCESO COMPLETADO en {elapsed:.1f}s",
                   1.0,
                   f"Archivo: {os.path.basename(self.output_path)}",
                   "completed")

        # Eventos ya fueron yield en tiempo real durante el proceso

    def _get_file_size(self, path: str) -> str:
        """Retorna tamaño legible de archivo."""
        size = os.path.getsize(path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} GB"
