"""
SDG Localidades — Modelos de datos
Define las estructuras de datos utilizadas en todo el pipeline ETL.
"""
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class PipelinePhase(Enum):
    """Fases del pipeline de procesamiento."""
    IDLE = "idle"
    INGESTION = "ingestion"
    NORMALIZATION = "normalization"
    DEDUPLICATION = "deduplication"
    PIVOT_GENERATION = "pivot_generation"
    INDICATOR_CALCULATION = "indicator_calculation"
    RESUMEN_CIFRAS = "resumen_cifras"
    EXCEL_GENERATION = "excel_generation"
    VALIDATION = "validation"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class FileSource:
    """Representa un archivo fuente que el sistema debe procesar."""
    key: str                    # Identificador único: 'pqrs', 'sac', 'side', 'cr', 'ph', 'encuestas'
    label: str                  # Nombre legible: "BD PQRS Bogotá Te Escucha"
    filename_pattern: str       # Patrón para identificar el archivo: "*PQRS*MAYO*"
    required: bool = True       # Si es obligatorio para generar el informe
    loaded: bool = False
    path: Optional[str] = None
    sheets: list = field(default_factory=list)
    row_count: int = 0


@dataclass
class PipelineEvent:
    """Evento emitido durante el pipeline para actualizar la UI."""
    phase: PipelinePhase
    message: str
    progress: float             # 0.0 - 1.0
    detail: str = ""
    status: str = "running"     # 'running', 'completed', 'error'


@dataclass
class IngestionResult:
    """Resultado de la ingesta de un archivo fuente."""
    source_key: str
    success: bool
    sheets: dict = field(default_factory=dict)  # sheet_name -> DataFrame
    row_count: int = 0
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


@dataclass
class ValidationReport:
    """Reporte de validación a 4 niveles."""
    level_1_input: bool = False        # Validación de archivos de entrada
    level_2_transform: bool = False    # Validación de transformaciones
    level_3_vs_original: bool = False  # Validación contra datos originales
    level_4_output: bool = False       # Hoja de verificación en el output
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    totals_match: bool = False


# Constantes del sistema
LOCALIDADES = [
    "ANTONIO NARIÑO", "BARRIOS UNIDOS", "BOSA", "CANDELARIA",
    "CHAPINERO", "CIUDAD BOLIVAR", "ENGATIVÁ", "FONTIBÓN",
    "KENNEDY", "MÁRTIRES", "PUENTE ARANDA", "RAFAEL URIBE URIBE",
    "SAN CRISTÓBAL", "SANTA FE", "SUBA", "SUMAPAZ",
    "TEUSAQUILLO", "TUNJUELITO", "USAQUÉN", "USME",
    "NIVEL CENTRAL", "SUPERCADES"
]

# Mapeo de nombres normalizados (con/variaciones)
LOCALIDADES_NORMALIZE = {
    "ANTONIO NARIÑO": "ANTONIO NARIÑO",
    "ANTONIO NARINO": "ANTONIO NARIÑO",
    "BARRIOS UNIDOS": "BARRIOS UNIDOS",
    "BOSA": "BOSA",
    "LA CANDELARIA": "CANDELARIA",
    "CANDELARIA": "CANDELARIA",
    "CHAPINERO": "CHAPINERO",
    "CIUDAD BOLIVAR": "CIUDAD BOLIVAR",
    "CIUDAD BOLÍVAR": "CIUDAD BOLIVAR",
    "ENGATIVÁ": "ENGATIVÁ",
    "ENGATIVA": "ENGATIVÁ",
    "FONTIBÓN": "FONTIBÓN",
    "FONTIBON": "FONTIBÓN",
    "KENNEDY": "KENNEDY",
    "LOS MARTIRES": "MÁRTIRES",
    "LOS MÁRTIRES": "MÁRTIRES",
    "MÁRTIRES": "MÁRTIRES",
    "MARTIRES": "MÁRTIRES",
    "PUENTE ARANDA": "PUENTE ARANDA",
    "RAFAEL URIBE URIBE": "RAFAEL URIBE URIBE",
    "RAFAEL URIBE": "RAFAEL URIBE URIBE",
    "SAN CRISTOBAL": "SAN CRISTÓBAL",
    "SAN CRISTÓBAL": "SAN CRISTÓBAL",
    "SANTA FE": "SANTA FE",
    "SUBA": "SUBA",
    "SUMAPAZ": "SUMAPAZ",
    "TEUSAQUILLO": "TEUSAQUILLO",
    "TUNJUELITO": "TUNJUELITO",
    "USAQUÉN": "USAQUÉN",
    "USAQUEN": "USAQUÉN",
    "USME": "USME",
    "NIVEL CENTRAL": "NIVEL CENTRAL",
    "SUPERCADES": "SUPERCADES",
    "SUPERCADE": "SUPERCADES",
}
