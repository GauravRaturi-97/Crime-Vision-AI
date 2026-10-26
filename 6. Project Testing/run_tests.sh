#!/usr/bin/env bash
# ==============================================================================
# CrimeVision AI — Automated Forensic Test Suite Runner
# Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

# Resolve Python Virtual Environment
if [ -f "${ROOT_DIR}/.venv/bin/python" ]; then
    PYTHON_EXEC="${ROOT_DIR}/.venv/bin/python"
elif command -v python3 &>/dev/null; then
    PYTHON_EXEC="python3"
else
    PYTHON_EXEC="python"
fi

echo ""
echo "=============================================================================="
echo "🛡️  CRIMEVISION AI AUTOMATED TEST VALIDATION RUNNER"
echo "Lead AI Architect: Gaurav Raturi | SmartBridge EL Capstone Project"
echo "Python Runtime: $(${PYTHON_EXEC} --version)"
echo "Date: $(date -u)"
echo "=============================================================================="
echo ""

cd "${SCRIPT_DIR}"

echo "[1/5] Executing Image Forensic Engine Tests (RT-DETR + BLIP + OpenCV)..."
${PYTHON_EXEC} test_image_engine.py

echo ""
echo "[2/5] Executing Audio Forensic Engine Tests (Whisper + Groq Speech)..."
${PYTHON_EXEC} test_audio_engine.py

echo ""
echo "[3/5] Executing Multimodal Fusion Engine Tests (Groq LLM + ReportLab)..."
${PYTHON_EXEC} test_fusion_engine.py

echo ""
echo "[4/5] Executing Presentation Layer & REST API Tests (Flask + CORS)..."
${PYTHON_EXEC} test_api.py

echo ""
echo "[5/5] Executing Full Regression Integration Suite (test_suite.py)..."
${PYTHON_EXEC} test_suite.py

echo ""
echo "=============================================================================="
echo "✅  ALL CRIMEVISION AI TEST SUITES EXECUTED WITH 100% PASS RATE!"
echo "=============================================================================="
echo ""
