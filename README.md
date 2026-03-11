# Game Scout Platform

Video game recommendation platform for third-party integrations, built with Django to serve both a public API and a website in a single project.

## Overview

Game Scout Platform provides:
- A public API (`/api/v1`) for catalog browsing, user profiles, and personalized recommendations.
- A commercial layer with API keys, usage plans, rate limiting, and quotas.
- A public website for integration docs, pricing, and onboarding.

## Current Status

Initial Django scaffold is in place:
- Environment-aware settings (`base`, `dev`, `test`, `prod`).
- PostgreSQL-ready database configuration via `DATABASE_URL`.
- DRF + OpenAPI docs setup (`drf-spectacular`).
- Health endpoints (`/health/live/`, `/health/ready/`).
- Public web routes (`/`, `/docs/`, `/pricing/`, `/contact/`).
- CI baseline (lint + tests).

## MVP Scope

- Game catalog with filters and game detail endpoints.
- User profiles with preferences and interactions.
- Personalized recommendations with explainability.
- API key authentication for API clients.
- Usage control with rate limiting and daily/monthly quotas.
- Public web portal with landing page, API guide, pricing page, and contact/onboarding page.

## Planned Tech Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- drf-spectacular (OpenAPI/Swagger/ReDoc)
- PostgreSQL + pgvector
- Redis
- Celery
- Docker / Docker Compose

## API Snapshot

Base path: `/api/v1`

- `GET /api/v1/` (scaffold root endpoint)
- `GET /api/schema/`
- `GET /api/docs/`
- `GET /api/redoc/`

## Website Routes

- `GET /` landing
- `GET /docs` integration guide
- `GET /pricing` plans
- `GET /contact` onboarding

## Quickstart (Local)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
copy .env.example .env
python manage.py check
python manage.py migrate
python manage.py runserver
```

## Quickstart (Docker)

```bash
docker compose up -d --build
docker compose exec web python manage.py migrate
```

## Repository Structure

```text
game-scout-api/
|-- .github/workflows/
|-- apps/
|-- data/
|-- docker/
|-- game_scout/
|-- scripts/
|-- static/
|-- templates/
|-- tests/
|-- .env.example
|-- .gitignore
|-- docker-compose.yml
|-- LICENSE
|-- manage.py
|-- README.md
|-- requirements-dev.txt
|-- requirements.txt
`-- pyproject.toml
```

## License

Distributed under the GNU AGPL v3 license. See [`LICENSE`](LICENSE).
