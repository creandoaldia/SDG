#!/usr/bin/env pwsh
# SDG Localidades — Verificador de estado del servidor
# Verifica si el servidor esta corriendo. Si no, lo arranca automaticamente.
#
# Uso: .\status.ps1          (verifica y reporta)
#       .\status.ps1 -quiet  (solo codigo de salida: 0=OK, 1=caido pero arrancado, 2=error)

param([switch]$quiet)

$PROJECT_DIR = Split-Path -Parent $PSCommandPath
$PID_FILE = Join-Path $PROJECT_DIR "server.pid"
$RESTART_COUNT_FILE = Join-Path $PROJECT_DIR ".restart_count"

# ==================================================
#  ANTILOOP - Circuit Breaker check
#  status.ps1 only restarts once.
#  If restart_count exceeds max, does NOT retry.
# ==================================================
$MAX_RESTART_ATTEMPTS = 3
$RESTART_WINDOW_MINUTES = 5

$now = Get-Date
if (Test-Path $RESTART_COUNT_FILE) {
    try {
        $restartData = Get-Content $RESTART_COUNT_FILE -Raw -Encoding utf8 | ConvertFrom-Json
        $restartData.attempts = @($restartData.attempts | Where-Object {
            $t = [datetime]::ParseExact($_, "yyyy-MM-dd HH:mm:ss", $null)
            ($now - $t).TotalMinutes -le $RESTART_WINDOW_MINUTES
        })
        if ($restartData.attempts.Count -ge $MAX_RESTART_ATTEMPTS) {
            if (-not $quiet) {
                Write-Host "  [BLOQUEO ANTILOOP] Servidor ha fallado $MAX_RESTART_ATTEMPTS veces." -ForegroundColor Red
                Write-Host "  Espera o elimina .restart_count para forzar." -ForegroundColor Yellow
            }
            exit 2
        }
    } catch { }
}

$LOGO = @"
    ____  ____   ___   ____    _     ___   _   _    __  ___
   / ___||  _ \ / _ \ |  _ \  | |   / _ \ | \ | |  / _|/ _ \
   \___ \| | | | | | || | | | | |  | | | ||  \| | | |_| | | |
    ___) | |_| | |_| || |_| | | |__| |_| || |\  | |  _| |_| |
   |____/|____/ \___/ |____/  |_____\___/ |_| \_| |_|  \___/

"@

function Test-Port5000 {
    try {
        $conn = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
        return ($conn -and $conn.State -eq 'Listen')
    } catch { return $false }
}

# ── Verificar proceso ──
$pidRunning = $false
if (Test-Path $PID_FILE) {
    $oldPid = (Get-Content $PID_FILE -Raw).Trim()
    if ($oldPid -and (Get-Process -Id $oldPid -ErrorAction SilentlyContinue)) {
        $pidRunning = $true
    }
}

$portOpen = Test-Port5000

if ($pidRunning -and $portOpen) {
    if (-not $quiet) {
        Clear-Host
        Write-Host $LOGO -ForegroundColor Cyan
        Write-Host "  ESTADO:  [OK] Servidor SDG Localidades CORRIENDO" -ForegroundColor Green
        Write-Host "  PID:     $oldPid" -ForegroundColor Gray
        Write-Host "  PUERTO:  5000 (escuchando)" -ForegroundColor Green
        Write-Host "  URL:     http://localhost:5000" -ForegroundColor Cyan
        Write-Host "" -ForegroundColor Cyan
        Write-Host "  Logs:    Get-Content server.log -Tail 20" -ForegroundColor Gray
        Write-Host "  Detener: .\stop-server.ps1" -ForegroundColor Gray
    }
    exit 0
}

# ── Servidor caido — reiniciar ──
if (-not $quiet) {
    Clear-Host
    Write-Host $LOGO -ForegroundColor DarkYellow
    Write-Host "  ESTADO:  [!!] Servidor SDG Localidades CAIDO" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Re-arrancando automaticamente..." -ForegroundColor Yellow
}

# Limpiar PID file viejo
Remove-Item $PID_FILE -Force -ErrorAction SilentlyContinue

# Arrancar
$VENV_PYTHON = Join-Path $PROJECT_DIR "venv\Scripts\python.exe"
$APP_SCRIPT = Join-Path $PROJECT_DIR "webapp\app.py"
$LOG_FILE = Join-Path $PROJECT_DIR "server.log"

if (-not (Test-Path $VENV_PYTHON)) {
    if (-not $quiet) { Write-Host "  [ERROR] No hay entorno virtual. Ejecuta .\start-server.ps1 primero" -ForegroundColor Red }
    exit 2
}

"=== SDG Localidades reiniciado: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ===" | Out-File $LOG_FILE -Encoding utf8

$STDOUT_FILE = Join-Path $PROJECT_DIR "server_stdout.log"
$STDERR_FILE = Join-Path $PROJECT_DIR "server_stderr.log"

$process = Start-Process -FilePath $VENV_PYTHON -WindowStyle Hidden -PassThru `
    -ArgumentList @($APP_SCRIPT) `
    -RedirectStandardOutput $STDOUT_FILE `
    -RedirectStandardError $STDERR_FILE `
    -WorkingDirectory $PROJECT_DIR

# Esperar hasta 10 segundos
$serverUp = $false
for ($i = 0; $i -lt 10; $i++) {
    Start-Sleep -Seconds 1
    try {
        $conn = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
        if ($conn -and $conn.State -eq 'Listen') { $serverUp = $true; break }
    } catch { }
}

if ($serverUp) {
    $process.Id | Out-File $PID_FILE -Encoding utf8 -Force
    if (-not $quiet) {
        Write-Host "  [OK] Servidor reiniciado (PID: $($process.Id))" -ForegroundColor Green
        Write-Host "  http://localhost:5000" -ForegroundColor Cyan
    }
    exit 0
} else {
    if (-not $quiet) {
        Write-Host "  [ERROR] No se pudo iniciar el servidor" -ForegroundColor Red
        Write-Host "  Revisa: Get-Content server.log -Tail 30" -ForegroundColor Yellow
    }
    exit 2
}
