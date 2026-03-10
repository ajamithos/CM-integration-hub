@echo off
title CM Integration Hub Launcher
color 0A

echo.
echo  ============================================
echo   CM Integration Hub - Setup and Launch
echo  ============================================
echo.

:: Check for Python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo  [!] Python is not installed or not in PATH.
    echo.
    echo  Opening the Python download page...
    echo  IMPORTANT: Check "Add Python to PATH" during install!
    echo.
    start https://www.python.org/downloads/
    echo  After installing Python, close this window and double-click launch_hub.bat again.
    echo.
    pause
    exit /b
)

echo  [OK] Python found:
python --version
echo.

:: Check for Streamlit
python -m streamlit --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo  [..] Installing Streamlit (one-time setup)...
    echo.
    python -m pip install streamlit --quiet
    if %ERRORLEVEL% NEQ 0 (
        echo  [!] Streamlit install failed. Try running manually:
        echo      python -m pip install streamlit
        echo.
        pause
        exit /b
    )
    echo  [OK] Streamlit installed!
    echo.
)

echo  [OK] Streamlit found:
python -m streamlit --version
echo.

:: Launch the app
echo  Launching CM Integration Hub...
echo  Your browser will open automatically.
echo  To stop the app, close this window or press Ctrl+C.
echo.
echo  ============================================
echo.

python -m streamlit run "%~dp0cm_training_hub.py"

pause
