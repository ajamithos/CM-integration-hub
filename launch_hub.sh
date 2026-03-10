#!/bin/bash

echo ""
echo "  ============================================"
echo "   CM Integration Hub - Setup and Launch"
echo "  ============================================"
echo ""

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "  [!] Python 3 is not installed."
    echo ""
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "  Opening the Python download page..."
        open "https://www.python.org/downloads/"
    else
        echo "  Install Python 3: https://www.python.org/downloads/"
    fi
    echo ""
    echo "  After installing, run this script again."
    exit 1
fi

echo "  [OK] Python found: $(python3 --version)"
echo ""

# Check for Streamlit
if ! python3 -m streamlit --version &> /dev/null; then
    echo "  [..] Installing Streamlit (one-time setup)..."
    echo ""
    python3 -m pip install streamlit --quiet
    if [ $? -ne 0 ]; then
        echo "  [!] Streamlit install failed. Try: python3 -m pip install streamlit"
        exit 1
    fi
    echo "  [OK] Streamlit installed!"
    echo ""
fi

echo "  [OK] Streamlit found: $(python3 -m streamlit --version)"
echo ""

# Launch
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "  Launching CM Integration Hub..."
echo "  Your browser will open automatically."
echo "  To stop: press Ctrl+C"
echo ""
echo "  ============================================"
echo ""

python3 -m streamlit run "$SCRIPT_DIR/cm_training_hub.py"
