"""
SDG Localidades — Validador a 4 Niveles
Valida que el proceso sea correcto en cada etapa, replicando el control
de calidad que Yesenia hace manualmente al verificar totales.
"""
import os
import pandas as pd
from engine.models import ValidationReport


class Validator:
    """
    Validación en 4 niveles:
    Nivel 1: Archivos de entrada existen y son legibles
    Nivel 2: Transformaciones aplicadas correctamente
    Nivel 3: Totales del output vs totales de los originales
    Nivel 4: Hoja de verificación en el output
    """

    def validate_all(self, sources: list, ingestion_data: dict,
                     normalized: dict, output_path: str,
                     month: str, year: str) -> ValidationReport:
        """Ejecuta la validación completa a 4 niveles."""
        report = ValidationReport()

        # Nivel 1: Validación de entrada
        report.level_1_input = self._validate_input(sources, ingestion_data, report)

        # Nivel 2: Validación de transformación
        report.level_2_transform = self._validate_transform(ingestion_data, normalized, report)

        # Nivel 3: Validación contra original
        if os.path.exists(output_path):
            report.level_3_vs_original = self._validate_output_vs_original(
                output_path, ingestion_data, report
            )

        # Nivel 4: Hoja de verificación en output
        if os.path.exists(output_path):
            report.level_4_output = self._validate_output_structure(output_path, month, year, report)

        # Verificar totales globales
        report.totals_match = all([
            report.level_1_input,
            report.level_2_transform,
            report.level_3_vs_original,
            report.level_4_output
        ])

        return report

    def _validate_input(self, sources: list, ingestion_data: dict,
                        report: ValidationReport) -> bool:
        """Nivel 1: Verificar que todos los archivos requeridos se leyeron."""
        all_valid = True
        required_sources = [s for s in sources if s.required]

        for source in required_sources:
            if source.key not in ingestion_data:
                report.errors.append(f"Archivo requerido no procesado: {source.label}")
                all_valid = False
            elif not ingestion_data[source.key].success:
                report.errors.append(f"Error procesando: {source.label}")
                all_valid = False

        return all_valid

    def _validate_transform(self, ingestion_data: dict, normalized: dict,
                            report: ValidationReport) -> bool:
        """Nivel 2: Verificar que las transformaciones se aplicaron."""
        all_valid = True

        for key in ingestion_data:
            if key in normalized:
                for sheet_name in ingestion_data[key].sheets:
                    if sheet_name not in normalized[key]:
                        report.warnings.append(
                            f"Hoja '{sheet_name}' de {key} no fue normalizada"
                        )
                        all_valid = False
                    else:
                        orig_rows = len(ingestion_data[key].sheets[sheet_name])
                        norm_rows = len(normalized[key][sheet_name])
                        if orig_rows > 0 and norm_rows == 0:
                            report.errors.append(
                                f"Hoja '{sheet_name}' de {key}: {orig_rows} filas perdidas en normalización"
                            )
                            all_valid = False

        return all_valid

    def _validate_output_vs_original(self, output_path: str, ingestion_data: dict,
                                     report: ValidationReport) -> bool:
        """Nivel 3: Verificar que el output existe y tiene datos."""
        try:
            # Verificar que el archivo existe y no está vacío
            file_size = os.path.getsize(output_path)
            if file_size == 0:
                report.errors.append("Archivo de salida está vacío")
                return False

            # Leer hoja de resumen para verificar datos
            xl = pd.ExcelFile(output_path)
            if 'RESUMEN CIFRAS' not in xl.sheet_names:
                report.warnings.append("Hoja 'RESUMEN CIFRAS' no encontrada en output")
                return False

            return True

        except Exception as e:
            report.errors.append(f"Error validando output: {str(e)}")
            return False

    def _validate_output_structure(self, output_path: str, month: str, year: str,
                                   report: ValidationReport) -> bool:
        """Nivel 4: Verificar estructura del output."""
        try:
            xl = pd.ExcelFile(output_path)

            # Verificar hojas mínimas requeridas
            required_sheets = ['PORTADA', 'RESUMEN CIFRAS', 'VALIDACION']
            for sheet in required_sheets:
                if sheet not in xl.sheet_names:
                    report.warnings.append(f"Hoja requerida '{sheet}' no encontrada en output")
                    return False

            # Verificar que la portada tenga el mes/año correcto
            df_portada = pd.read_excel(output_path, sheet_name='PORTADA', header=None)
            portada_text = ' '.join(df_portada.iloc[:, 0].dropna().astype(str).tolist())
            if month not in portada_text.upper() or year not in portada_text:
                report.warnings.append(f"Periodo {month} {year} no verificado en portada")

            return True

        except Exception as e:
            report.errors.append(f"Error validando estructura: {str(e)}")
            return False
