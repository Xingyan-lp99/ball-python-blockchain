set shell := ["powershell.exe", "-NoLogo", "-NoProfile", "-Command"]

default:
    @just --list

up: db chain check backend frontend
    @Write-Host "Open http://127.0.0.1:8502 | Logs: storage/logs"

db:
    docker compose --env-file .env -f infrastructure/compose.yaml up -d --wait db

check:
    uv run --locked --env-file .env python -m backend.check_demo_readiness

backend: check
    if (Get-NetTCPConnection -LocalPort 8001 -State Listen -ErrorAction SilentlyContinue) { Write-Host "Port 8001 is occupied; backend startup skipped." } else { New-Item -ItemType Directory -Force -Path storage/logs | Out-Null; Start-Process -FilePath "uv" -ArgumentList "run --locked --env-file .env python -m uvicorn backend.main:app --host 127.0.0.1 --port 8001" -WorkingDirectory (Get-Location).Path -WindowStyle Hidden -RedirectStandardOutput "storage/logs/backend.out.log" -RedirectStandardError "storage/logs/backend.err.log"; Write-Host "Backend launch requested." }

frontend:
    if (Get-NetTCPConnection -LocalPort 8502 -State Listen -ErrorAction SilentlyContinue) { Write-Host "Port 8502 is occupied; frontend startup skipped." } else { New-Item -ItemType Directory -Force -Path storage/logs | Out-Null; Start-Process -FilePath "uv" -ArgumentList "run --locked python -m streamlit run frontend/app.py --server.address 127.0.0.1 --server.port 8502" -WorkingDirectory (Get-Location).Path -WindowStyle Hidden -RedirectStandardOutput "storage/logs/frontend.out.log" -RedirectStandardError "storage/logs/frontend.err.log"; Write-Host "Frontend launch requested." }

chain:
    uv run --locked python -m backend.demo_chain start

chain-save:
    uv run --locked python -m backend.demo_chain save

chain-stop:
    uv run --locked python -m backend.demo_chain stop

backup:
    uv run --locked --env-file .env python -m backend.demo_backup

ps:
    docker compose --env-file .env -f infrastructure/compose.yaml ps

logs:
    docker compose --env-file .env -f infrastructure/compose.yaml logs --tail 100 -f
