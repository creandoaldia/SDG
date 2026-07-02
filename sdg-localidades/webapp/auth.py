"""
SDG Localidades — Módulo de Autenticación
Flask session-based auth, compatible con SSE (cookies via EventSource).
Correcciones de Judgment Day aplicadas:
  - hmac.compare_digest para comparación constant-time
  - SESSION_COOKIE_PATH configurable para proxy subpath
  - CSRF token vía session
  - /api/events whitelisted con auth check interno
  - Rate limiting básico (5 intentos/min por IP)
"""
import os
import hmac
import time
import secrets
import threading
from functools import wraps

from flask import (
    Blueprint, session, request, jsonify, render_template,
    redirect, url_for, Response, current_app
)

# ── Config ──
LOGIN_ATTEMPTS = {}       # IP -> [timestamps]
LOGIN_ATTEMPTS_LOCK = threading.Lock()  # Thread safety + cleanup
MAX_LOGIN_ATTEMPTS = 5
LOGIN_WINDOW_SEC = 60     # 5 attempts per 60s
LOGIN_CLEANUP_INTERVAL = 300  # Cleanup stale IPs every 5 min
_last_cleanup = time.time()

# ── Blueprint ──
auth_bp = Blueprint('auth', __name__, url_prefix='')


def get_password() -> str:
    """Retorna el password desde env, con fallback warning."""
    pw = os.environ.get('APP_PASSWORD', '')
    if not pw:
        import logging
        logging.warning("⚠️ APP_PASSWORD no configurada. Usando default inseguro.")
        pw = 'sdg2024'  # Default solo para desarrollo local
    return pw


def check_password(attempt: str) -> bool:
    """Comparación constant-time para prevenir timing attack."""
    return hmac.compare_digest(attempt, get_password())


def generate_csrf_token() -> str:
    """Genera y almacena un token CSRF en la sesión."""
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(32)
    return session['csrf_token']


def validate_csrf_token(token: str) -> bool:
    """Valida el token CSRF de forma constant-time."""
    expected = session.get('csrf_token', '')
    return bool(token and hmac.compare_digest(token, expected))


def _cleanup_stale_ips():
    """Limpia IPs que ya no tienen intentos activos (memory leak fix)."""
    global _last_cleanup
    now = time.time()
    if now - _last_cleanup < LOGIN_CLEANUP_INTERVAL:
        return
    _last_cleanup = now
    with LOGIN_ATTEMPTS_LOCK:
        stale = [ip for ip, attempts in LOGIN_ATTEMPTS.items()
                 if not any(now - t < LOGIN_WINDOW_SEC for t in attempts)]
        for ip in stale:
            del LOGIN_ATTEMPTS[ip]


def _is_rate_limited(ip: str) -> bool:
    """Verifica rate limiting por IP."""
    _cleanup_stale_ips()
    now = time.time()
    with LOGIN_ATTEMPTS_LOCK:
        if ip not in LOGIN_ATTEMPTS:
            LOGIN_ATTEMPTS[ip] = []
        # Limpiar intentos viejos para esta IP
        LOGIN_ATTEMPTS[ip] = [t for t in LOGIN_ATTEMPTS[ip] if now - t < LOGIN_WINDOW_SEC]
        return len(LOGIN_ATTEMPTS[ip]) >= MAX_LOGIN_ATTEMPTS


def _record_attempt(ip: str):
    """Registra un intento de login."""
    now = time.time()
    with LOGIN_ATTEMPTS_LOCK:
        if ip not in LOGIN_ATTEMPTS:
            LOGIN_ATTEMPTS[ip] = []
        LOGIN_ATTEMPTS[ip].append(now)


# ── Decorator ──
def login_required(f):
    """Decorador para rutas que requieren autenticación.
    SSE endpoint (/api/events) NO debe usar este decorador —
    su auth check va dentro del generator con response SSE-format."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('authenticated'):
            return jsonify({'error': 'No autorizado'}), 401
        return f(*args, **kwargs)
    return decorated


# ── Routes ──

@auth_bp.route('/login', methods=['GET'])
def login_page():
    """Renderiza la página de login."""
    if session.get('authenticated'):
        return redirect(url_for('index'))
    csrf_token = generate_csrf_token()
    return render_template('login.html', csrf_token=csrf_token)


@auth_bp.route('/api/login', methods=['POST'])
def api_login():
    """API login: valida password + crea sesión."""
    ip = request.remote_addr or 'unknown'

    if _is_rate_limited(ip):
        return jsonify({'error': 'Demasiados intentos. Espera 1 minuto.'}), 429

    data = request.get_json() or {}
    password = data.get('password', '')
    csrf_token = data.get('csrf_token', '')

    # Validar CSRF solo si hay sesión previa (evita CSRF-Login vector)
    if session.get('csrf_token') and not validate_csrf_token(csrf_token):
        return jsonify({'error': 'Token CSRF inválido'}), 403

    if not check_password(password):
        _record_attempt(ip)
        return jsonify({'error': 'Contraseña incorrecta'}), 401

    # Login exitoso
    session.permanent = True
    session['authenticated'] = True
    session['csrf_token'] = secrets.token_hex(32)  # Refresh token
    session['login_time'] = time.time()

    next_url = data.get('next', '') or request.args.get('next', '')
    if next_url and not next_url.startswith('/'):
        next_url = ''  # Evitar open redirect

    return jsonify({
        'success': True,
        'redirect': next_url or url_for('index')
    })


@auth_bp.route('/api/logout', methods=['POST'])
def api_logout():
    """Cierra la sesión."""
    session.clear()
    return jsonify({'success': True})


@auth_bp.route('/api/auth/status', methods=['GET'])
def api_auth_status():
    """Retorna estado de autenticación."""
    return jsonify({
        'authenticated': session.get('authenticated', False),
        'csrf_token': generate_csrf_token() if session.get('authenticated') else None
    })
