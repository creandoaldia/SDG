"""
SDG Localidades — Aplicación Web
Interfaz gráfica local para que Yesenia cargue archivos y procese el informe.
Corre en localhost:5000, los datos NUNCA salen de su PC.

Arquitectura:
  - Flask sirve el frontend y la API REST
  - El pipeline ETL corre en un hilo separado
  - La UI recibe eventos SSE (Server-Sent Events) para mostrar progreso en vivo
  - Tailwind CSS para una interfaz moderna y responsiva
"""
import os
import sys
import json
import threading
import time
from pathlib import Path

# Asegurar que el directorio raíz del proyecto está en el path
sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from werkzeug.utils import secure_filename

from engine.pipeline import SDGPipeline
from engine.models import PipelinePhase

app = Flask(__name__)

# Configuración
BASE_DIR = Path(__file__).parent.parent
app.config['UPLOAD_FOLDER'] = str(BASE_DIR / 'input')
app.config['OUTPUT_FOLDER'] = str(BASE_DIR / 'output')
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB máximo
app.config['ALLOWED_EXTENSIONS'] = {'xlsx', 'xls'}

# Estado global del pipeline
pipeline_state = {
    'running': False,
    'progress': 0.0,
    'phase': 'idle',
    'message': '',
    'events': [],
    'output_file': None,
    'error': None
}

# Lock para acceso concurrente al estado
state_lock = threading.Lock()


def allowed_file(filename: str) -> bool:
    """Verifica si la extensión del archivo es válida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')


@app.route('/api/status')
def api_status():
    """Retorna el estado actual del pipeline."""
    with state_lock:
        return jsonify(pipeline_state)


@app.route('/api/upload', methods=['POST'])
def api_upload():
    """
    Recibe los archivos fuente y los guarda en la carpeta input/.
    Acepta múltiples archivos en una sola petición.
    """
    if 'files[]' not in request.files:
        return jsonify({'error': 'No se enviaron archivos'}), 400

    files = request.files.getlist('files[]')
    uploaded = []
    errors = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            uploaded.append({
                'name': filename,
                'size': os.path.getsize(filepath),
                'path': filepath
            })
        else:
            errors.append(f"Archivo no válido: {file.filename}")

    return jsonify({
        'uploaded': uploaded,
        'errors': errors,
        'count': len(uploaded)
    })


@app.route('/api/process', methods=['POST'])
def api_process():
    """
    Inicia el procesamiento del pipeline ETL.
    Retorna inmediatamente; el progreso se consulta vía /api/events (SSE).
    """
    with state_lock:
        if pipeline_state['running']:
            return jsonify({'error': 'Ya hay un proceso en ejecución'}), 409

        # Resetear estado
        pipeline_state['running'] = True
        pipeline_state['progress'] = 0.0
        pipeline_state['phase'] = 'starting'
        pipeline_state['message'] = 'Iniciando procesamiento...'
        pipeline_state['events'] = []
        pipeline_state['output_file'] = None
        pipeline_state['error'] = None

    # Obtener mes y año del request
    data = request.get_json() or {}
    month = data.get('month', 'MAYO')
    year = data.get('year', '2026')

    # Iniciar pipeline en hilo separado
    thread = threading.Thread(
        target=_run_pipeline,
        args=(month, year),
        daemon=True
    )
    thread.start()

    return jsonify({'status': 'started', 'message': 'Procesamiento iniciado'})


@app.route('/api/events')
def api_events():
    """
    SSE (Server-Sent Events) endpoint.
    La UI se suscribe a este stream para recibir actualizaciones en vivo.
    """
    def generate():
        last_index = 0
        last_heartbeat = time.time()
        while True:
            with state_lock:
                if pipeline_state['phase'] == 'completed' or pipeline_state['phase'] == 'error':
                    # Enviar eventos pendientes y terminar
                    if last_index < len(pipeline_state['events']):
                        for event in pipeline_state['events'][last_index:]:
                            yield f"data: {json.dumps(event)}\n\n"
                            last_index += 1
                    yield f"data: {json.dumps({'type': 'done', 'phase': pipeline_state['phase']})}\n\n"
                    break

                if last_index < len(pipeline_state['events']):
                    for event in pipeline_state['events'][last_index:]:
                        yield f"data: {json.dumps(event)}\n\n"
                        last_index += 1

            # Heartbeat cada 5s para mantener conexión viva (evita timeouts de proxy/Waitress)
            now = time.time()
            if now - last_heartbeat >= 5.0:
                yield f": heartbeat\n\n"
                last_heartbeat = now

            time.sleep(0.5)

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            # NOTA: 'Connection' es hop-by-hop (PEP 3333), Waitress lo rechaza.
            # Waitress maneja keep-alive automáticamente para HTTP/1.1.
            'X-Accel-Buffering': 'no'
        }
    )


@app.route('/api/download')
def api_download():
    """Descarga el archivo de salida generado."""
    from flask import send_file

    with state_lock:
        output_file = pipeline_state.get('output_file')

    if not output_file or not os.path.exists(output_file):
        return jsonify({'error': 'No hay archivo de salida disponible'}), 404

    return send_file(
        output_file,
        as_attachment=True,
        download_name=os.path.basename(output_file)
    )


def _validate_input_files(input_dir: str) -> list:
    """Valida estructura mínima de archivos antes de procesar."""
    import glob
    warnings = []

    # Verificar que hay archivos Excel
    xlsx_files = glob.glob(os.path.join(input_dir, '*.xlsx'))
    if not xlsx_files:
        warnings.append("No se encontraron archivos .xlsx en la carpeta input/")

    # Verificar archivos mínimos por patrón
    patterns = {
        'PQRS': '*BOGOTA*ESCUCHA*',
        'SAC': '*SAC_atencion*',
        'SIDE': '*Resumen SIDE*',
        'CR': '*PRODUCTIVIDAD_CR*',
        'PH': '*PRODUCTIVIDAD_PH*',
    }
    for name, pattern in patterns.items():
        matches = glob.glob(os.path.join(input_dir, pattern))
        if not matches:
            warnings.append(f"Archivo {name} no encontrado (patrón: {pattern})")

    return warnings


def _run_pipeline(month: str, year: str):
    """Ejecuta el pipeline ETL en un hilo separado con backup y pre-validación."""
    # Pre-validación
    pre_warnings = _validate_input_files(app.config['UPLOAD_FOLDER'])
    for w in pre_warnings:
        with state_lock:
            pipeline_state['events'].append({
                'type': 'progress', 'phase': 'validation',
                'message': f'⚠️ {w}', 'progress': 0.0,
                'detail': '', 'status': 'warning'
            })

    # Backup del Excel anterior
    backup_path = None
    for f in os.listdir(app.config['OUTPUT_FOLDER']):
        if f.endswith('.xlsx') and not f.startswith('~$'):
            backup_path = os.path.join(app.config['OUTPUT_FOLDER'], f)
            break

    try:
        pipeline = SDGPipeline(
            input_dir=app.config['UPLOAD_FOLDER'],
            output_dir=app.config['OUTPUT_FOLDER'],
            month=month,
            year=year
        )

        for event in pipeline.run():
            with state_lock:
                pipeline_state['phase'] = event.phase.value
                pipeline_state['progress'] = event.progress
                pipeline_state['message'] = event.message
                pipeline_state['events'].append({
                    'type': 'progress',
                    'phase': event.phase.value,
                    'message': event.message,
                    'progress': event.progress,
                    'detail': event.detail,
                    'status': event.status
                })

        with state_lock:
            pipeline_state['output_file'] = pipeline.output_path
            pipeline_state['phase'] = 'completed'
            pipeline_state['message'] = '✅ Procesamiento completado exitosamente'
            pipeline_state['progress'] = 1.0
            pipeline_state['events'].append({
                'type': 'done',
                'phase': 'completed',
                'message': '✅ Procesamiento completado exitosamente',
                'progress': 1.0
            })

    except Exception as e:
        # Rollback: restaurar backup si existe
        if backup_path and os.path.exists(backup_path):
            import shutil
            try:
                shutil.copy2(backup_path, backup_path)
            except:
                pass  # Si falla el rollback, al menos reportamos el error

        with state_lock:
            pipeline_state['phase'] = 'error'
            pipeline_state['message'] = f'❌ Error: {str(e)}'
            pipeline_state['error'] = str(e)
            pipeline_state['events'].append({
                'type': 'error',
                'phase': 'error',
                'message': f'❌ Error: {str(e)}',
                'progress': pipeline_state.get('progress', 0)
            })
    finally:
        with state_lock:
            pipeline_state['running'] = False


def create_app():
    """Factory para crear la app Flask."""
    # Asegurar que las carpetas existen
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    return app


if __name__ == '__main__':
    create_app()
    from waitress import serve
    print("=" * 60)
    print("  SDG LOCALIDADES - Sistema de Informes PQRS")
    print("  ===========================================")
    print(f"  Abre tu navegador en: http://localhost:5000")
    print("  Los datos NUNCA salen de este computador.")
    print("=" * 60)
    serve(app, host='127.0.0.1', port=5000)
