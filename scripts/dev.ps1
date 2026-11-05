> Windows 无 make 时的等价命令。用法：powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 test

param(
    [Parameter(Position = 0)]
    [ValidateSet("setup", "run", "test", "lint", "up", "down")]
    [string]$Target = "test"
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$backend = Join-Path $root "backend"
$py = Join-Path $backend ".venv\Scripts\python.exe"

switch ($Target) {
    "setup" {
        Set-Location $backend
        if (-not (Test-Path $py)) { python -m venv .venv }
        & $py -m pip install -q --upgrade pip
        & $py -m pip install -q -r requirements.txt pytest httpx ruff
    }
    "run" {
        Set-Location $backend
        & $py -m uvicorn app.main:app --reload --port 8000
    }
    "test" {
        Set-Location $backend
        & $py -m pytest -q
    }
    "lint" {
        Set-Location $backend
        & $py -m ruff check .
    }
    "up" {
        Set-Location (Join-Path $root "infra")
        docker compose up -d --build
    }
    "down" {
        Set-Location (Join-Path $root "infra")
        docker compose down
    }
}
