#!/usr/bin/env bash
# =============================================================================
# Meta-Orchestrator Entry Point (Bash)
# =============================================================================
#
# Usage:
#   ./scripts/run_orchestrator.sh [--dry-run] [--resume] [--max-parallel N]
#   ./scripts/run_orchestrator.sh --help
#
# Environment Variables:
#   ORCH_MAX_PARALLEL  - Maximum concurrent agents (default: 8)
#   ORCH_TIMEOUT       - Timeout per agent in minutes (default: 30)
#   PYTHON             - Python interpreter to use (default: python3)
#
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
ORCHESTRATOR="${SCRIPT_DIR}/orchestrator.py"
CONFIG="${SCRIPT_DIR}/agent_config.json"

PYTHON="${PYTHON:-python3}"

# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------

if ! command -v "${PYTHON}" &>/dev/null; then
    echo "ERROR: Python interpreter '${PYTHON}' not found on PATH."
    echo "       Install Python 3.10+ or set the PYTHON environment variable."
    exit 1
fi

PYTHON_VERSION=$("${PYTHON}" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PYTHON_MAJOR=$("${PYTHON}" -c "import sys; print(sys.version_info.major)")
PYTHON_MINOR=$("${PYTHON}" -c "import sys; print(sys.version_info.minor)")

if [[ "${PYTHON_MAJOR}" -lt 3 ]] || { [[ "${PYTHON_MAJOR}" -eq 3 ]] && [[ "${PYTHON_MINOR}" -lt 10 ]]; }; then
    echo "ERROR: Python 3.10+ required, found ${PYTHON_VERSION}"
    exit 1
fi

if [[ ! -f "${ORCHESTRATOR}" ]]; then
    echo "ERROR: orchestrator.py not found at ${ORCHESTRATOR}"
    exit 1
fi

if [[ ! -f "${CONFIG}" ]]; then
    echo "ERROR: agent_config.json not found at ${CONFIG}"
    exit 1
fi

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║          Meta-Orchestrator Parallel Execution Engine        ║"
echo "║                   40 Agents · 7 Tiers                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "  Python:     ${PYTHON} (${PYTHON_VERSION})"
echo "  Config:     ${CONFIG}"
echo "  Project:    ${PROJECT_ROOT}"
echo ""

# ---------------------------------------------------------------------------
# Launch
# ---------------------------------------------------------------------------

cd "${PROJECT_ROOT}"
exec "${PYTHON}" "${ORCHESTRATOR}" --config "${CONFIG}" "$@"
