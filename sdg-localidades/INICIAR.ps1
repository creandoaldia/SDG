#!/usr/bin/env pwsh
# SDG Localidades - PowerShell Launcher
# Proporciona una experiencia más rica que launch.bat

$ErrorActionPreference = "Stop"
$Host.UI.RawUI.WindowTitle = "SDG Localidades - Sistema de Informes PQRS"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  SDG LOCALIDADES - Sistema de Informes PQRS" -ForegroundColor White
Write-Host "  Secretaría Distrital de Gobierno" -ForegroundColor Gray
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Iniciando sistema..." -ForegroundColor Yellow
Write-Host "  Los datos NUNCA salen de este computador." -ForegroundColor Green
Write-Host ""

# Ir al directorio del proyecto
Set-Location -LiteralPath $PSScriptRoot

# Verificar Python
try {
    $pyVersion = python --version
    Write-Host "  [OK] Python detectado: $pyVersion" -ForegroundColor Green
} catch {
    Write-Host "  [ERROR] Python no está instalado." -ForegroundColor Red
    Write-Host ""
    Write-Host "  Por favor instala Python 3.9+ desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "  Durante la instalación, MARCA la opción 'Add Python to PATH'." -ForegroundColor Yellow
    Read-Host "`nPresiona Enter para salir"
    exit 1
}

# Crear entorno virtual si no existe
if (-not (Test-Path "venv")) {
    Write-Host "  [..] Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "  [OK] Entorno virtual creado" -ForegroundColor Green
}

# Activar entorno virtual
. .\venv\Scripts\Activate.ps1

# Instalar dependencias
Write-Host "  [..] Verificando dependencias..." -ForegroundColor Yellow
pip install -q --upgrade pip 2>$null
$installResult = pip install -q -r requirements.txt 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  [..] Instalando dependencias (puede tomar un minuto)..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  [ERROR] No se pudieron instalar las dependencias" -ForegroundColor Red
        Read-Host "`nPresiona Enter para salir"
        exit 1
    }
}
Write-Host "  [OK] Dependencias listas" -ForegroundColor Green

# Crear carpetas necesarias
New-Item -ItemType Directory -Path "input" -Force | Out-Null
New-Item -ItemType Directory -Path "output" -Force | Out-Null

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Abriendo interfaz web..." -ForegroundColor White
Write-Host "  http://localhost:5000" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  IMPORTANTE: No cierres esta ventana mientras usas el sistema." -ForegroundColor Yellow
Write-Host "  Para salir, presiona Ctrl+C o cierra esta ventana." -ForegroundColor Yellow
Write-Host ""

# Abrir navegador
Start-Process "http://localhost:5000"

# Iniciar la aplicación
python webapp\app.py

Write-Host ""
Write-Host "  Sistema detenido." -ForegroundColor Red
Read-Host "Presiona Enter para salir"
