#Requires -Version 7.0
<#
.SYNOPSIS
    Meta-Orchestrator Entry Point (PowerShell)

.DESCRIPTION
    Launches the Meta-Orchestrator parallel agent execution engine.
    Dispatches 40 specialized agents across 7 execution tiers.

.PARAMETER DryRun
    Print execution plan without running agents.

.PARAMETER Resume
    Resume from last checkpoint.

.PARAMETER MaxParallel
    Maximum concurrent agents (default: 8, env: ORCH_MAX_PARALLEL).

.PARAMETER MaxRetries
    Maximum retries per failed agent (default: 2).

.PARAMETER Timeout
    Timeout per agent in minutes (default: 30, env: ORCH_TIMEOUT).

.PARAMETER Tier
    Run only a specific tier (for debugging).

.PARAMETER Agent
    Run only a specific agent ID (for debugging).

.PARAMETER Verbose
    Enable verbose/debug logging.

.PARAMETER OutputDir
    Output directory (default: output/).

.PARAMETER LogDir
    Log directory (default: logs/).

.EXAMPLE
    .\scripts\run_orchestrator.ps1 -DryRun

.EXAMPLE
    .\scripts\run_orchestrator.ps1 -MaxParallel 4 -Timeout 45

.EXAMPLE
    .\scripts\run_orchestrator.ps1 -Resume

.EXAMPLE
    .\scripts\run_orchestrator.ps1 -Tier 0

.EXAMPLE
    .\scripts\run_orchestrator.ps1 -Agent AGT-001
#>

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$Resume,
    [int]$MaxParallel = 0,
    [int]$MaxRetries = 2,
    [int]$Timeout = 0,
    [int]$Tier = -1,
    [string]$Agent = "",
    [string]$OutputDir = "output",
    [string]$LogDir = "logs",
    [switch]$VerboseLog
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
$Orchestrator = Join-Path $ScriptDir "orchestrator.py"
$Config = Join-Path $ScriptDir "agent_config.json"

# ---------------------------------------------------------------------------
# Locate Python
# ---------------------------------------------------------------------------

function Find-Python {
    # Try common Python commands in order of preference
    $candidates = @("python3", "python", "py")
    foreach ($cmd in $candidates) {
        $found = Get-Command $cmd -ErrorAction SilentlyContinue
        if ($found) {
            # Verify it's Python 3.10+
            try {
                $version = & $cmd -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
                $parts = $version -split '\.'
                $major = [int]$parts[0]
                $minor = [int]$parts[1]
                if ($major -ge 3 -and $minor -ge 10) {
                    return @{ Command = $cmd; Version = $version }
                }
            }
            catch {
                continue
            }
        }
    }
    return $null
}

$pythonInfo = Find-Python
if (-not $pythonInfo) {
    Write-Error "Python 3.10+ not found. Install Python or ensure it is on PATH."
    exit 1
}

$PythonCmd = $pythonInfo.Command
$PythonVersion = $pythonInfo.Version

# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------

if (-not (Test-Path $Orchestrator)) {
    Write-Error "orchestrator.py not found at: $Orchestrator"
    exit 1
}

if (-not (Test-Path $Config)) {
    Write-Error "agent_config.json not found at: $Config"
    exit 1
}

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║          Meta-Orchestrator Parallel Execution Engine        ║" -ForegroundColor Cyan
Write-Host "║                   40 Agents · 7 Tiers                      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Python:     $PythonCmd ($PythonVersion)"
Write-Host "  Config:     $Config"
Write-Host "  Project:    $ProjectRoot"
Write-Host ""

# ---------------------------------------------------------------------------
# Build arguments
# ---------------------------------------------------------------------------

$pyArgs = @($Orchestrator, "--config", $Config)

if ($DryRun) {
    $pyArgs += "--dry-run"
}

if ($Resume) {
    $pyArgs += "--resume"
}

# MaxParallel: use param, then env, then default
if ($MaxParallel -gt 0) {
    $pyArgs += @("--max-parallel", $MaxParallel.ToString())
}
elseif ($env:ORCH_MAX_PARALLEL) {
    $pyArgs += @("--max-parallel", $env:ORCH_MAX_PARALLEL)
}

# Timeout: use param, then env, then default
if ($Timeout -gt 0) {
    $pyArgs += @("--timeout", $Timeout.ToString())
}
elseif ($env:ORCH_TIMEOUT) {
    $pyArgs += @("--timeout", $env:ORCH_TIMEOUT)
}

$pyArgs += @("--max-retries", $MaxRetries.ToString())
$pyArgs += @("--output-dir", $OutputDir)
$pyArgs += @("--log-dir", $LogDir)

if ($Tier -ge 0) {
    $pyArgs += @("--tier", $Tier.ToString())
}

if ($Agent -ne "") {
    $pyArgs += @("--agent", $Agent)
}

if ($VerboseLog) {
    $pyArgs += "--verbose"
}

# ---------------------------------------------------------------------------
# Launch
# ---------------------------------------------------------------------------

Push-Location $ProjectRoot
try {
    & $PythonCmd @pyArgs
    $exitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

exit $exitCode
