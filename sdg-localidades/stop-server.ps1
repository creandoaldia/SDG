#!/usr/bin/env pwsh
# SDG Localidades — Detiene el servidor en segundo plano
#
# Uso: .\stop-server.ps1

$PROJECT_DIR = Split-Path -Parent $PSCommandPath
$PID_FILE = Join-Path $PROJECT_DIR "server.pid"

if (Test-Path $PID_FILE) {
    $srvPid = (Get-Content $PID_FILE -Raw).Trim()
    if ($srvPid) {
        $proc = Get-Process -Id $srvPid -ErrorAction SilentlyContinue
        if ($proc) {
            Write-Host "  Deteniendo servidor SDG (PID: $srvPid)..." -ForegroundColor Yellow
            Stop-Process -Id $srvPid -Force -ErrorAction SilentlyContinue
            Write-Host "  [OK] Servidor detenido" -ForegroundColor Green
        } else {
            Write-Host "  Proceso $srvPid ya no existe" -ForegroundColor Gray
        }
    }
    Remove-Item $PID_FILE -Force -ErrorAction SilentlyContinue
} else {
    Write-Host "  No hay servidor SDG registrado" -ForegroundColor Gray
}

# Verificar limpieza del puerto
Start-Sleep -Seconds 1
$conn = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
if ($conn -and $conn.State -eq 'Listen') {
    Write-Host "  [WARN] Puerto 5000 sigue ocupado. Forzando cierre..." -ForegroundColor Yellow
    $conn | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    Write-Host "  [OK] Puerto liberado" -ForegroundColor Green
}
