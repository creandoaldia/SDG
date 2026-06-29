#!/usr/bin/env pwsh
# SDG Localidades — Arranque del servidor en segundo plano
# Inicia el servidor web como proceso background silencioso.
# No requiere ventana de terminal abierta.
#
# Uso: .\start-server.ps1
# Para ver logs: Get-Content .\server.log -Tail 20

$ErrorActionPreference = "Stop"
$Host.UI.RawUI.WindowTitle = "SDG Localidades - Iniciando servidor..."

$PROJECT_DIR = Split-Path -Parent $PSCommandPath
$LOG_FILE = Join-Path $PROJECT_DIR "server.log"
$PID_FILE = Join-Path $PROJECT_DIR "server.pid"
$RESTART_COUNT_FILE = Join-Path $PROJECT_DIR ".restart_count"
$VENV_PYTHON = Join-Path $PROJECT_DIR "venv\Scripts\python.exe"

# ==================================================
#  ANTILOOP - Circuit Breaker
#  Max 3 restart attempts in a 5-minute window.
#  If exceeded, blocks for 15 minutes.
# ==================================================
$MAX_RESTART_ATTEMPTS = 3
$RESTART_WINDOW_MINUTES = 5
$COOLDOWN_MINUTES = 15

$now = Get-Date
$restartData = @{ attempts = @() }

if (Test-Path $RESTART_COUNT_FILE) {
    try {
        $restartData = Get-Content $RESTART_COUNT_FILE -Raw -Encoding utf8 | ConvertFrom-Json
    } catch { $restartData = @{ attempts = @() } }
}

# Limpiar intentos fuera de ventana
$restartData.attempts = @($restartData.attempts | Where-Object {
    $attemptTime = [datetime]::ParseExact($_, "yyyy-MM-dd HH:mm:ss", $null)
    ($now - $attemptTime).TotalMinutes -le $RESTART_WINDOW_MINUTES
})

if ($restartData.attempts.Count -ge $MAX_RESTART_ATTEMPTS) {
    $oldest = [datetime]::ParseExact($restartData.attempts[0], "yyyy-MM-dd HH:mm:ss", $null)
    $cooldownEnd = $oldest.AddMinutes($COOLDOWN_MINUTES)
    if ($now -lt $cooldownEnd) {
        $remaining = [math]::Round(($cooldownEnd - $now).TotalMinutes, 1)
        Write-Host "  [BLOQUEO] Demasiados reinicios en $RESTART_WINDOW_MINUTES min." -ForegroundColor Red
        Write-Host "  Espera $remaining min antes de intentar de nuevo." -ForegroundColor Yellow
        Write-Host "  Para forzar: elimina el archivo .restart_count" -ForegroundColor Gray
        exit 1
    }
    # Reset si ya pasó el cooldown
    $restartData.attempts = @()
}

# Registrar este intento
$restartData.attempts += $now.ToString("yyyy-MM-dd HH:mm:ss")
$restartData | ConvertTo-Json | Out-File $RESTART_COUNT_FILE -Encoding utf8 -Force

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  SDG LOCALIDADES - Servidor de Informes PQRS" -ForegroundColor White
Write-Host "============================================================" -ForegroundColor Cyan

# ── Anti-loop: Forzar limpieza de puerto 5000 antes de empezar ──
$conn = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
if ($conn -and $conn.State -eq 'Listen') {
    Write-Host "  [..] Puerto 5000 ocupado, liberando..." -ForegroundColor Yellow
    $conn | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    Start-Sleep -Seconds 2
}

# ── Verificar si ya esta corriendo (despues de limpieza) ──
if (Test-Path $PID_FILE) {
    $oldPid = Get-Content $PID_FILE -Raw | ForEach-Object { $_.Trim() }
    if ($oldPid -and (Get-Process -Id $oldPid -ErrorAction SilentlyContinue)) {
        Write-Host "  [OK] Servidor YA esta corriendo (PID: $oldPid)" -ForegroundColor Green
        Write-Host "  Abre: http://localhost:5000" -ForegroundColor Cyan
        exit 0
    }
    Remove-Item $PID_FILE -Force -ErrorAction SilentlyContinue
}

# ── Verificar entorno virtual ──
if (-not (Test-Path $VENV_PYTHON)) {
    Write-Host "  [..] Creando entorno virtual..." -ForegroundColor Yellow
    & "python" -m venv (Join-Path $PROJECT_DIR "venv")
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [ERROR] No se pudo crear el entorno virtual" -ForegroundColor Red
        exit 1
    }
    Write-Host "  [OK] Entorno virtual creado" -ForegroundColor Green
}

# ── Verificar/instalar dependencias ──
$REQUIREMENTS = Join-Path $PROJECT_DIR "requirements.txt"
Write-Host "  [..] Verificando dependencias..." -ForegroundColor Yellow
& $VENV_PYTHON -m pip install -q --upgrade pip 2>&1 | Out-Null
$installLog = & $VENV_PYTHON -m pip install -q -r $REQUIREMENTS 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  [..] Instalando dependencias..." -ForegroundColor Yellow
    & $VENV_PYTHON -m pip install -r $REQUIREMENTS 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [ERROR] No se pudieron instalar las dependencias" -ForegroundColor Red
        exit 1
    }
}
Write-Host "  [OK] Dependencias listas" -ForegroundColor Green

# ── Crear carpetas necesarias ──
New-Item -ItemType Directory -Path (Join-Path $PROJECT_DIR "input") -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $PROJECT_DIR "output") -Force | Out-Null

# ── Iniciar servidor en segundo plano ──
$APP_SCRIPT = Join-Path $PROJECT_DIR "webapp\app.py"
$STDOUT_FILE = Join-Path $PROJECT_DIR "server_stdout.log"
$STDERR_FILE = Join-Path $PROJECT_DIR "server_stderr.log"

"=== SDG Localidades iniciado: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ===" | Out-File $STDOUT_FILE -Encoding utf8
"=== SDG Localidades iniciado: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ===" | Out-File $STDERR_FILE -Encoding utf8

Write-Host "  [..] Iniciando servidor en segundo plano..." -ForegroundColor Yellow

$process = Start-Process -FilePath $VENV_PYTHON -WindowStyle Hidden -PassThru `
    -ArgumentList @($APP_SCRIPT) `
    -RedirectStandardOutput $STDOUT_FILE `
    -RedirectStandardError $STDERR_FILE `
    -WorkingDirectory $PROJECT_DIR

# Esperar a que el servidor este realmente escuchando (hasta 15 segundos)
$timeout = 15
$serverUp = $false
for ($i = 0; $i -lt $timeout; $i++) {
    Start-Sleep -Seconds 1
    try {
        $conn = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
        if ($conn -and $conn.State -eq 'Listen') {
            $serverUp = $true
            break
        }
    } catch { }
}

if ($serverUp) {
    $process.Id | Out-File $PID_FILE -Encoding utf8 -Force
    Write-Host "  [OK] Servidor iniciado (PID: $($process.Id))" -ForegroundColor Green
    Write-Host "" -ForegroundColor Cyan
    Write-Host "  Abre tu navegador en: http://localhost:5000" -ForegroundColor Cyan
    Write-Host "  Logs: Get-Content server_stdout.log -Tail 20" -ForegroundColor Gray
    Write-Host "  Detener: .\stop-server.ps1" -ForegroundColor Gray
    Write-Host "  Estado: .\status.ps1" -ForegroundColor Gray
} else {
    Write-Host "  [WARN] El servidor no respondio en $timeout segundos" -ForegroundColor Yellow
    Write-Host "  Revisa los logs:" -ForegroundColor Yellow
    Write-Host "    Get-Content server_stdout.log -Tail 30" -ForegroundColor Yellow
    Write-Host "    Get-Content server_stderr.log -Tail 30" -ForegroundColor Yellow
    Write-Host "  O ejecuta manualmente: .\venv\Scripts\python.exe webapp\app.py" -ForegroundColor Yellow
}
