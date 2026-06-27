@echo off
title SDG Localidades - Sistema de Informes PQRS
color 0F

echo ============================================================
echo   SDG LOCALIDADES - Sistema de Informes PQRS
echo   Secretaria Distrital de Gobierno
echo ============================================================
echo.
echo   Iniciando sistema...
echo   Los datos NUNCA salen de este computador.
echo.

:: Ir al directorio del proyecto
cd /d "%~dp0"

:: Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado.
    echo.
    echo   Por favor instala Python 3.9+ desde: https://www.python.org/downloads/
    echo   Durante la instalacion, MARCA la opcion "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

echo [OK] Python detectado

:: Crear entorno virtual si no existe
if not exist "venv\" (
    echo [..] Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado
)

:: Activar entorno virtual
call venv\Scripts\activate.bat

:: Instalar dependencias
echo [..] Verificando dependencias...
pip install -q --upgrade pip 2>nul
pip install -q -r requirements.txt 2>nul
if errorlevel 1 (
    echo [..] Instalando dependencias (puede tomar un minuto)...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] No se pudieron instalar las dependencias
        pause
        exit /b 1
    )
)
echo [OK] Dependencias listas

:: Crear carpetas necesarias
if not exist "input\" mkdir input
if not exist "output\" mkdir output

echo.
echo ============================================================
echo   Abriendo interfaz web...
echo   http://localhost:5000
echo ============================================================
echo.
echo   IMPORTANTE: No cierres esta ventana mientras usas el sistema.
echo   Para salir, presiona Ctrl+C o cierra esta ventana.
echo.

:: Iniciar la aplicacion
python webapp\app.py

:: Si llegamos aqui, la app se cerro
echo.
echo   Sistema detenido.
pause
