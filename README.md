# Game Scout Platform

Video game recommendation platform for third-party integrations, built with Django to serve both a public API and a website in a single project.

## Overview

Game Scout Platform provides:
- A public API (`/api/v1`) for catalog browsing, user profiles, and personalized recommendations.
- A commercial layer with API keys, usage plans, rate limiting, and quotas.
- A public website for integration docs, pricing, and onboarding.

## Project Status

This repository is currently in the initial commit stage (documentation-first).  
Core Django code, API endpoints, and deployment files are planned and will be added in the next implementation commits.

## Planned MVP Features

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

## Planned API Snapshot

Base path: `/api/v1`

- `POST /auth/register`
- `POST /auth/login`
- `GET /games`
- `GET /users/{id}/recommendations`
- `POST /api-keys`
- `GET /usage/current`
- `GET /usage/limits`

## Planned Website Routes

- `GET /` landing
- `GET /docs` integration guide
- `GET /pricing` plans
- `GET /contact` onboarding
- `GET /api/docs` Swagger UI
- `GET /api/redoc` ReDoc

## Next Implementation Steps

1. Bootstrap Django project and app structure.
2. Add database models and migrations.
3. Implement API key auth, rate limiting, and quota enforcement.
4. Build recommendation flow and usage tracking.
5. Add public website pages and API documentation UI.

## Repository Structure

```text
game-scout-api/
|-- .gitignore
|-- LICENSE
|-- README.md
`-- (code scaffold coming in next commits)
```

## License

Distributed under the GNU AGPL v3 license. See [`LICENSE`](LICENSE).
