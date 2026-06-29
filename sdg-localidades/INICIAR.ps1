#!/usr/bin/env pwsh
# SDG Localidades — Lanzador (modo background)
# Inicia el servidor como proceso en segundo plano.
# Ya no bloquea la terminal — puedes cerrarla.
#
# Despues de ejecutar, abre: http://localhost:5000
# Para verificar estado: .\status.ps1
# Para detener: .\stop-server.ps1

$ErrorActionPreference = "Stop"
$Host.UI.RawUI.WindowTitle = "SDG Localidades - Iniciando..."

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  SDG LOCALIDADES - Sistema de Informes PQRS" -ForegroundColor White
Write-Host "  Secretaria Distrital de Gobierno" -ForegroundColor Gray
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Iniciando servidor en segundo plano..." -ForegroundColor Yellow
Write-Host "  Los datos NUNCA salen de este computador." -ForegroundColor Green
Write-Host ""

# Ir al directorio del proyecto
Set-Location -LiteralPath $PSScriptRoot

# Verificar Python
try {
    $pyVersion = python --version
    Write-Host "  [OK] Python: $pyVersion" -ForegroundColor Green
} catch {
    Write-Host "  [ERROR] Python no esta instalado." -ForegroundColor Red
    Write-Host "  Instala Python 3.9+ desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "`nPresiona Enter para salir"
    exit 1
}

# Ejecutar start-server.ps1 que maneja todo el proceso en background
& "$PSScriptRoot\start-server.ps1"

# Mostrar estado final
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  SERVIDOR EN SEGUNDO PLANO" -ForegroundColor White
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Puedes CERRAR esta ventana. El servidor seguira corriendo." -ForegroundColor Yellow
Write-Host ""
Write-Host "  Para verificar estado despues:" -ForegroundColor Gray
Write-Host "    .\status.ps1       - Muestra estado (auto-reinicia si esta caido)" -ForegroundColor Gray
Write-Host "  Para detener el servidor:" -ForegroundColor Gray
Write-Host "    .\stop-server.ps1  - Detiene el servidor limpiamente" -ForegroundColor Gray
Write-Host ""

# Preguntar si abrir navegador
$openBrowser = Read-Host "  Abrir navegador ahora? (S/n)"
if ($openBrowser -ne 'n' -and $openBrowser -ne 'N') {
    Start-Process "http://localhost:5000"
}

# No esperar - el servidor corre en background
Write-Host ""
Write-Host "  Presiona Enter para cerrar esta ventana (el servidor sigue corriendo)."
Read-Host
