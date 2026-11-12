set shell := ["powershell.exe", "-NoLogo", "-Command"]

# Ball Python Blockchain Registry
# Local development commands

default:
    @just --list

up:
    docker compose up -d

down:
    docker compose down

ps:
    docker compose ps

logs:
    docker compose logs --tail=100 -f

restart:
    docker compose restart

build:
    docker compose build

check:
    docker compose config --quiet

test-contracts:
    cd contracts; npx.cmd hardhat test

chain:
    cd backend; uv run python dev_chain.py

deploy-registry:
    cd contracts; npx.cmd hardhat run scripts/deploy-snake-registry.ts --network localhost

migrate:
    cd backend; uv run python migrate.py

test-backend:
    cd backend; uv run pytest -q -ra

test-frontend:
    cd frontend; uv run python -m unittest discover -s tests -v

backend:
    cd backend; uv run uvicorn main:app --reload

frontend:
    cd frontend; uv run streamlit run main.py
