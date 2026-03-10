@echo off
echo ====================================
echo CM TRAINING HUB
echo ====================================
echo.
echo Checking if setup is complete...
echo.

REM Check if streamlit is installed
python -m pip show streamlit >nul 2>&1
if %errorlevel% neq 0 (
    echo First time setup required!
    echo Installing dependencies...
    echo.
    python -m pip install -r requirements.txt
    echo.
    echo Setup complete!
    echo.
)

echo Starting CM Training Hub...
echo.
echo The hub will open in your browser at: http://localhost:8501
echo.
echo To stop the hub, close this window.
echo ====================================
echo.

python -m streamlit run cm_training_hub.py
