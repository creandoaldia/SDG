"""
SDG Localidades — Aplicación Web
Interfaz gráfica local para que Yesenia cargue archivos y procese el informe.
Corre en localhost:5000, los datos NUNCA salen de su PC.

Arquitectura:
  - Flask sirve el frontend y la API REST
  - El pipeline ETL corre en un hilo separado
  - La UI recibe eventos SSE (Server-Sent Events) para mostrar progreso en vivo
  - Tailwind CSS para una interfaz moderna y responsiva
  - Autenticación via Flask session + cookies (SSE-compatible)
"""
import os
import sys
import json
import threading
import time
import hmac
import pandas as pd
import unidecode
from pathlib import Path

# Asegurar que el directorio raíz del proyecto está en el path
sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Flask, render_template, request, jsonify, Response, stream_with_context, redirect, url_for, session as flask_session
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix

from engine.pipeline import SDGPipeline
from engine.models import PipelinePhase
from engine.tab_processors import (
    process_tab, validate_tab_type, validate_file_content, ALLOWED_TAB_TYPES
)
from webapp.auth import auth_bp, login_required

app = Flask(__name__)

# ── Config del proxy (Traefik/Caddy detrás de /sdg/) ──
# Aplica ProxyFix para que url_for() genere rutas correctas con SCRIPT_NAME
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# ── Session config para subruta /sdg/ (Juicio: CRÍTICO #1) ──
app.config['APPLICATION_ROOT'] = os.environ.get('APPLICATION_ROOT', '/')
app.config['SESSION_COOKIE_PATH'] = os.environ.get('SESSION_COOKIE_PATH', '/')
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = int(os.environ.get('SESSION_LIFETIME_HOURS', '8')) * 3600
app.config['SESSION_COOKIE_SECURE'] = os.environ.get('HTTPS', 'false').lower() == 'true'
app.secret_key = os.environ.get('FLASK_SECRET_KEY', '')
if not app.secret_key:
    raise RuntimeError(
        "FLASK_SECRET_KEY no configurada. "
        "Establece la variable de entorno FLASK_SECRET_KEY en docker-compose.yml o .env"
    )

# Registrar blueprint de autenticación
app.register_blueprint(auth_bp)

# Directorios para uploads de tabs (separado del pipeline principal)
TAB_UPLOAD_BASE = str(Path(__file__).parent.parent / 'input' / 'tabs')

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
    'error': None,
    'dashboard_data': None       # Datos para el dashboard post-informe
}

# ── Rutas whitelisted (no requieren auth) ──
AUTH_WHITELIST = {'/api/login', '/api/auth/status', '/login', '/static'}
# SSE endpoint NO debe usar @login_required — el auth check va dentro del generator
# para evitar que EventSource reciba un 302/401 en lugar de SSE.

# Lock para acceso concurrente al estado
state_lock = threading.Lock()

# Estado individual por tab (separado del pipeline principal)
tab_states = {}
tab_state_lock = threading.Lock()


def allowed_file(filename: str) -> bool:
    """Verifica si la extensión del archivo es válida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    """Página principal. Redirige a /login si no autenticado."""
    if not flask_session.get('authenticated'):
        return redirect(url_for('auth.login_page', next=request.url))
    return render_template('index.html')


@app.route('/api/status')
@login_required
def api_status():
    """Retorna el estado actual del pipeline."""
    with state_lock:
        return jsonify(pipeline_state)


@app.route('/api/upload', methods=['POST'])
@login_required
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
@login_required
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
        pipeline_state['dashboard_data'] = None

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
    NO usa @login_required — el auth check va DENTRO del generator
    para que EventSource reciba un mensaje SSE en lugar de un 302/401.
    """
    def generate():
        # Auth check inside generator (Juicio: CRÍTICO #3)
        if not flask_session.get('authenticated'):
            yield f"data: {json.dumps({'type': 'error', 'message': 'No autorizado', 'auth_required': True})}\n\n"
            yield f"retry: 60000\n\n"  # Reducir frecuencia de reconexión
            return

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
            'X-Accel-Buffering': 'no'
        }
    )


@app.route('/api/download')
@login_required
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


@app.route('/api/dashboard')
@login_required
def api_dashboard():
    """Retorna datos estructurados del ultimo informe generado para el dashboard.
    Solo usa datos REALES de resumen_df — NO aproximaciones (Juicio: DASH-002)."""
    with state_lock:
        data = pipeline_state.get('dashboard_data')

    if not data:
        return jsonify({
            'periodo': None,
            'resumen': None,
            'localidades': [],
            'tabs': None,
            'message': 'Genere un informe para ver el dashboard'
        })

    return jsonify(data)


# ═══════════════════════════════════════════════════════════════
# Helpers: Tab dashboard data
# ═══════════════════════════════════════════════════════════════

def _build_tab_dashboard(tab_type: str, filepath: str, result: dict, real_data: dict = None) -> dict:
    """Construye datos de dashboard para un tab individual.
    Usa real_data si está disponible (datos reales del procesamiento).
    Si no, retorna empty state — NO aproximaciones (Juicio: DASH-002)."""
    DASHBOARD_LABELS = {
        'pqrs': {'title': 'PQRS', 'metric': 'Registros PQRS', 'secondary_label': 'Duplicados',
                 'chart_type': 'bar', 'chart_labels': ['Gestionadas', 'Pendientes'],
                 'chart_colors': ['#10B981', '#F59E0B']},
        'atenciones': {'title': 'Atenciones SAC', 'metric': 'Atenciones', 'secondary_label': None,
                       'chart_type': None, 'chart_labels': [], 'chart_colors': []},
        'cert-residencia': {'title': 'Cert. Residencia', 'metric': 'Solicitudes', 'secondary_label': None,
                            'chart_type': None, 'chart_labels': [], 'chart_colors': []},
        'prop-horizontal': {'title': 'Prop. Horizontal', 'metric': 'Tramites', 'secondary_label': None,
                            'chart_type': None, 'chart_labels': [], 'chart_colors': []},
        'encuestas': {'title': 'Encuestas', 'metric': 'Encuestas', 'secondary_label': 'Tasa Completa',
                      'chart_type': 'doughnut', 'chart_labels': ['Completas', 'Incompletas'],
                      'chart_colors': ['#10B981', '#FCA5A5']},
        'doc-extraviados': {'title': 'Doc. Extraviados', 'metric': 'Registrados', 'secondary_label': None,
                            'chart_type': None, 'chart_labels': [], 'chart_colors': []},
    }

    info = DASHBOARD_LABELS.get(tab_type, {})

    # Si tenemos datos reales, usarlos
    if real_data:
        rows = real_data.get('total', 0)
        sheets = real_data.get('sheets', 0)
        extra = real_data.get('extra', {})
        summary = real_data.get('summary', {})
        filename = real_data.get('filename', '')
        output_path = real_data.get('output_path', '')
    else:
        # Empty state — NO aproximaciones
        return {
            'tab_type': tab_type,
            'title': info.get('title', tab_type),
            'metric_label': info.get('metric', 'Registros'),
            'metric_value': 0,
            'secondary_label': None,
            'secondary_value': None,
            'sheets': 0,
            'actual_sheets': [],
            'filename': '',
            'breakdown': {},
            'chart_data': [],
            'chart_type': info.get('chart_type'),
            'chart_labels': info.get('chart_labels', []),
            'chart_colors': info.get('chart_colors', []),
        }

    # Extraer metricas segun tipo con datos REALES
    breakdown = {}
    chart_data = []
    secondary_val = None

    # Escanear el archivo de salida para sheet names
    actual_sheets = []
    if output_path:
        try:
            xl = pd.ExcelFile(output_path)
            actual_sheets = xl.sheet_names
        except Exception:
            pass

    if tab_type == 'pqrs':
        secondary_val = summary.get('duplicados', 0)
        breakdown = {
            'gestionadas': summary.get('gestionadas', 0),
            'pendientes': summary.get('pendientes', 0),
            'duplicados': summary.get('duplicados', 0),
            'pivot_tables': summary.get('pivot_count', 0),
        }
        if breakdown['gestionadas'] > 0 or breakdown['pendientes'] > 0:
            chart_data = [
                {'label': 'Gestionadas', 'value': breakdown['gestionadas'], 'color': '#10B981'},
                {'label': 'Pendientes', 'value': breakdown['pendientes'], 'color': '#F59E0B'},
            ]

    elif tab_type == 'encuestas':
        total = summary.get('total', rows)
        completas = summary.get('completas', 0)
        incompletas = max(0, total - completas)
        tasa = round(completas / total * 100, 1) if total > 0 else 0
        secondary_val = f"{tasa}%"
        breakdown = {
            'total': total,
            'completas': completas,
            'incompletas': incompletas,
            'tasa_completitud': tasa,
        }
        if completas > 0 or incompletas > 0:
            chart_data = [
                {'label': 'Completas', 'value': completas, 'color': '#10B981'},
                {'label': 'Incompletas', 'value': incompletas, 'color': '#FCA5A5'},
            ]

    elif tab_type == 'doc-extraviados':
        breakdown = {
            'stock': summary.get('stock', 0),
            'registrados': summary.get('registrados', 0),
            'entregados': summary.get('entregados', 0),
            'secciones': summary.get('secciones', 0),
        }

    elif tab_type in ('atenciones', 'cert-residencia', 'prop-horizontal'):
        breakdown = {'total': rows}

    return {
        'tab_type': tab_type,
        'title': info.get('title', tab_type),
        'metric_label': info.get('metric', 'Registros'),
        'metric_value': rows,
        'secondary_label': info.get('secondary_label'),
        'secondary_value': secondary_val,
        'sheets': sheets,
        'actual_sheets': actual_sheets,
        'filename': filename,
        'breakdown': breakdown,
        'chart_data': chart_data,
        'chart_type': info.get('chart_type'),
        'chart_labels': info.get('chart_labels', []),
        'chart_colors': info.get('chart_colors', []),
    }


# ═══════════════════════════════════════════════════════════════
# API: Procesamiento individual por Tab
# ═══════════════════════════════════════════════════════════════

TAB_DIR_NAMES = {
    'pqrs': 'pqrs', 'atenciones': 'sac',
    'cert-residencia': 'cr', 'prop-horizontal': 'ph',
    'encuestas': 'encuestas', 'doc-extraviados': 'side'
}


def _get_tab_state(tab_type: str) -> dict:
    """Obtiene o crea el estado para un tab."""
    with tab_state_lock:
        if tab_type not in tab_states:
            tab_states[tab_type] = {
                'phase': 'idle',
                'progress': 0.0,
                'message': '',
                'file': None,
                'output_file': None,
                'error': None
            }
        return tab_states[tab_type]


@app.route('/api/tabs/<tab_type>/upload', methods=['POST'])
@login_required
def api_tab_upload(tab_type):
    """Sube un archivo para un tab especifico."""
    if not validate_tab_type(tab_type):
        return jsonify({'error': f'Tipo de tab invalido: {tab_type}'}), 400

    if 'file' not in request.files:
        return jsonify({'error': 'No se envio archivo'}), 400

    file = request.files['file']
    if not file or not file.filename:
        return jsonify({'error': 'Archivo vacio'}), 400

    ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
    if ext not in app.config['ALLOWED_EXTENSIONS']:
        return jsonify({'error': f'Extension no valida: .{ext}. Solo .xlsx y .xls'}), 400

    # Validar tipo de tab y guardar en directorio separado
    tab_dir = os.path.join(TAB_UPLOAD_BASE, tab_type)
    os.makedirs(tab_dir, exist_ok=True)

    filename = secure_filename(file.filename)
    filepath = os.path.join(tab_dir, filename)
    file.save(filepath)

    # Validar contenido contra el tipo de tab
    validation_msg = validate_file_content(filepath, tab_type)
    if validation_msg:
        os.remove(filepath)
        return jsonify({'error': validation_msg}), 400

    state = _get_tab_state(tab_type)
    with tab_state_lock:
        state['phase'] = 'uploaded'
        state['message'] = f'Archivo cargado: {filename}'
        state['file'] = filepath
        state['error'] = None

    return jsonify({
        'success': True,
        'filename': filename,
        'size': os.path.getsize(filepath),
        'message': f'{filename} cargado correctamente'
    })


@app.route('/api/tabs/<tab_type>/process', methods=['POST'])
@login_required
def api_tab_process(tab_type):
    """Procesa el archivo subido para un tab en un hilo separado.
    El progreso se consulta vía GET /api/tabs/<tab_type>/status (polling cada 2s).
    Incluye: guard contra doble procesamiento, thread lifecycle cleanup con timeout."""
    if not validate_tab_type(tab_type):
        return jsonify({'error': f'Tipo de tab invalido: {tab_type}'}), 400

    state = _get_tab_state(tab_type)

    # ── Guard contra doble procesamiento (Judgment Day fix) ──
    with tab_state_lock:
        if state.get('phase') == 'processing':
            return jsonify({'error': 'Ya hay un procesamiento en curso para este tab'}), 409

    if not state.get('file') or not os.path.exists(state['file']):
        return jsonify({'error': 'No hay archivo cargado para procesar'}), 400

    # Obtener mes y año dinámicos
    data = request.get_json() or {}
    month = data.get('month', time.strftime('%B').upper()[:5])
    year = data.get('year', str(time.localtime().tm_year))
    start_time = time.time()
    PROCESS_TIMEOUT = 1800  # 30 minutos máximo

    with tab_state_lock:
        state['phase'] = 'processing'
        state['progress'] = 0.0
        state['message'] = 'Procesando...'
        state['error'] = None
        state['month'] = month
        state['year'] = year
        state['started_at'] = start_time

    def _progress_callback(progress: float, message: str = ''):
        """Callback para actualizar progreso desde el thread (thread-safe)."""
        with tab_state_lock:
            if tab_type in tab_states:
                tab_states[tab_type]['progress'] = progress
                if message:
                    tab_states[tab_type]['message'] = message

    def _process_thread():
        """Ejecuta process_tab en un hilo separado y actualiza estado.
        Con timeout y cleanup automático."""
        try:
            # Verificar timeout
            if time.time() - start_time > PROCESS_TIMEOUT:
                raise TimeoutError("Tiempo de procesamiento excedido (30 min)")

            output_dir = os.path.join(str(BASE_DIR / 'output'), 'tabs', tab_type)
            os.makedirs(output_dir, exist_ok=True)

            _progress_callback(0.1, 'Iniciando procesamiento...')
            result = process_tab(
                tab_type, state.get('file'), output_dir,
                month, year, progress_callback=_progress_callback
            )

            with tab_state_lock:
                if tab_type not in tab_states:
                    return  # State was cleaned up
                if result.get('success'):
                    tab_states[tab_type]['phase'] = 'completed'
                    tab_states[tab_type]['progress'] = 1.0
                    tab_states[tab_type]['message'] = f'Completado: {result.get("filename", "")}'
                    tab_states[tab_type]['output_file'] = result.get('output_path')

                    # Extraer summary real para dashboard
                    safe_result = {k: v for k, v in result.items() if not k.startswith('_')}
                    summary = result.get('summary', {})
                    rows = result.get('rows', 0)

                    # Construir real_data con métricas reales del procesamiento
                    real_data = {
                        'total': rows,
                        'sheets': result.get('sheets', 0),
                        'extra': result.get('extra', {}),
                        'summary': summary,
                        'filename': result.get('filename', ''),
                        'output_path': result.get('output_path', ''),
                    }
                    tab_states[tab_type]['dashboard_data'] = _build_tab_dashboard(
                        tab_type, state.get('file'), result, real_data=real_data
                    )
                    tab_states[tab_type]['last_result'] = safe_result
                else:
                    tab_states[tab_type]['phase'] = 'error'
                    tab_states[tab_type]['message'] = f'Error: {result.get("error", "Desconocido")}'
                    tab_states[tab_type]['error'] = result.get('error')

        except Exception as e:
            with tab_state_lock:
                if tab_type in tab_states:
                    tab_states[tab_type]['phase'] = 'error'
                    tab_states[tab_type]['message'] = f'Error: {str(e)}'
                    tab_states[tab_type]['error'] = str(e)

    # Iniciar hilo de procesamiento
    thread = threading.Thread(target=_process_thread, daemon=True)
    thread.start()

    return jsonify({'status': 'processing', 'message': 'Procesamiento iniciado en segundo plano'})


@app.route('/api/tabs/<tab_type>/status')
@login_required
def api_tab_status(tab_type):
    """Retorna el estado del procesamiento de un tab."""
    if not validate_tab_type(tab_type):
        return jsonify({'error': f'Tipo de tab invalido: {tab_type}'}), 400

    state = _get_tab_state(tab_type)
    with tab_state_lock:
        return jsonify({
            'phase': state.get('phase', 'idle'),
            'progress': state.get('progress', 0.0),
            'message': state.get('message', ''),
            'file': os.path.basename(state['file']) if state.get('file') else None,
            'output_file': os.path.basename(state['output_file']) if state.get('output_file') else None,
            'error': state.get('error')
        })


@app.route('/api/tabs/<tab_type>/dashboard')
@login_required
def api_tab_dashboard(tab_type):
    """Retorna datos de dashboard para un tab especifico."""
    if not validate_tab_type(tab_type):
        return jsonify({'error': f'Tipo de tab invalido: {tab_type}'}), 400

    state = _get_tab_state(tab_type)
    dash_data = state.get('dashboard_data')

    if not dash_data:
        return jsonify({
            'tab_type': tab_type,
            'message': 'Procese un archivo para ver el dashboard',
            'metric_value': 0,
            'metric_label': 'Sin datos'
        })

    return jsonify(dash_data)


@app.route('/api/tabs/<tab_type>/download')
@login_required
def api_tab_download(tab_type):
    """Descarga el archivo generado por un tab."""
    from flask import send_file

    if not validate_tab_type(tab_type):
        return jsonify({'error': f'Tipo de tab invalido: {tab_type}'}), 400

    state = _get_tab_state(tab_type)
    output_file = state.get('output_file')

    if not output_file or not os.path.exists(output_file):
        return jsonify({'error': 'No hay archivo generado para descargar'}), 404

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

        # Extraer datos REALES para dashboard desde resumen_df
        month_display = {'01':'ENERO','02':'FEBRERO','03':'MARZO','04':'ABRIL',
                         '05':'MAYO','06':'JUNIO','07':'JULIO','08':'AGOSTO',
                         '09':'SEPTIEMBRE','10':'OCTUBRE','11':'NOVIEMBRE','12':'DICIEMBRE'}
        month_name = month_display.get(month, month)

        # Construir dashboard desde resumen_df REAL (con guard contra None)
        if hasattr(pipeline, 'resumen_df') and pipeline.resumen_df is not None and not pipeline.resumen_df.empty:
            rdf = pipeline.resumen_df
            # Helper: encontrar columna por nombre flexible (tolower + unidecode)
            def _find_col(df, *candidates):
                for col in df.columns:
                    col_norm = unidecode.unidecode(str(col)).lower().strip()
                    for cand in candidates:
                        if unidecode.unidecode(cand).lower().strip() in col_norm:
                            return col
                return None

            gestionadas_col = _find_col(rdf, 'PQRS GESTIONADAS')
            pendientes_col = _find_col(rdf, 'PQRS PENDIENTES')
            doc_ext_col    = _find_col(rdf, 'DOC.EXT', 'DOC EXT')
            orientaciones_col = _find_col(rdf, 'ORIENTACIONES')
            cr_col         = _find_col(rdf, 'CERT. RESIDENCIA', 'CERT RESIDENCIA')
            ph_col         = _find_col(rdf, 'CERT. PROPIEDAD HORIZONTAL', 'CERT PROPIEDAD HORIZONTAL', 'PROPIEDAD HORIZONTAL')
            enc_total_col  = _find_col(rdf, 'ENCUESTAS DEL PERIODO', 'ENCUESTAS')
            enc_completa_col = _find_col(rdf, 'ENCUESTAS CON RESPUESTA COMPLETA', 'RESPUESTA COMPLETA')
            calif_col      = _find_col(rdf, 'CALIFICACION', 'SATISFACCION')

            def _safe_sum(col_name):
                if col_name and col_name in rdf.columns:
                    return int(pd.to_numeric(rdf[col_name], errors='coerce').fillna(0).sum())
                return 0

            def _safe_mean(col_name):
                if col_name and col_name in rdf.columns:
                    vals = pd.to_numeric(rdf[col_name], errors='coerce').dropna()
                    return round(float(vals.mean()), 1) if not vals.empty else 0.0
                return 0.0

            real_gestionadas = _safe_sum(gestionadas_col)
            real_pendientes  = _safe_sum(pendientes_col)
            real_doc_ext     = _safe_sum(doc_ext_col)
            real_orientaciones = _safe_sum(orientaciones_col)
            real_cr          = _safe_sum(cr_col)
            real_ph          = _safe_sum(ph_col)
            real_enc_total   = _safe_sum(enc_total_col)
            real_enc_completas = _safe_sum(enc_completa_col)
            real_calif       = _safe_mean(calif_col)

            dashboard_data = {
                'periodo': {'month': month_name, 'year': year},
                'resumen': {
                    'total_pqrs': real_gestionadas + real_pendientes,
                    'gestionadas': real_gestionadas,
                    'pendientes': real_pendientes,
                    'doc_extraviados': real_doc_ext,
                    'orientaciones': real_orientaciones,
                    'cert_residencia': real_cr,
                    'prop_horizontal': real_ph,
                    'encuestas_total': real_enc_total,
                    'encuestas_completas': real_enc_completas,
                    'calificacion': real_calif,
                    'satisfaccion': round(real_calif * 20, 1) if real_calif else 0.0
                },
                'localidades': rdf.to_dict(orient='records') if not rdf.empty else [],
                'tabs': {
                    'pqrs': {'total': real_gestionadas + real_pendientes,
                             'gestionadas': real_gestionadas,
                             'pendientes': real_pendientes},
                    'atenciones': {'total_sac': real_orientaciones,
                                   'orientaciones': real_orientaciones},
                    'cert_residencia': {'total': real_cr},
                    'prop_horizontal': {'total': real_ph},
                    'encuestas': {'total_periodo': real_enc_total,
                                  'completas': real_enc_completas,
                                  'calificacion': real_calif},
                    'doc_extraviados': {'registrados': real_doc_ext}
                }
            }
        else:
            # Path B ELIMINADO (Juicio: DASH-002). NO más aproximaciones.
            # Si no hay resumen_df, se retorna empty state.
            dashboard_data = {
                'periodo': {'month': month_name, 'year': year},
                'resumen': None,
                'localidades': [],
                'tabs': {
                    'pqrs': {'total': 0, 'gestionadas': 0, 'pendientes': 0},
                    'atenciones': {'total_sac': 0},
                    'cert_residencia': {'total': 0},
                    'prop_horizontal': {'total': 0},
                    'encuestas': {'total_periodo': 0, 'completas': 0},
                    'doc_extraviados': {'registrados': 0}
                }
            }

        with state_lock:
            pipeline_state['output_file'] = pipeline.output_path
            pipeline_state['phase'] = 'completed'
            pipeline_state['message'] = '✅ Procesamiento completado exitosamente'
            pipeline_state['progress'] = 1.0
            pipeline_state['dashboard_data'] = dashboard_data
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
