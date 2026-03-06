# Public API Contract (MVP Baseline)

## Base Path

`/api/v1`

## Auth Endpoints

- `POST /auth/register`
- `POST /auth/login`
- `POST /auth/refresh`

## Catalog and Profile

- `GET /games`
- `GET /games/{game_id}`
- `POST /users/{id}/preferences`
- `GET /users/{id}/preferences`
- `POST /users/{id}/interactions`
- `GET /users/{id}/interactions`

## Recommendation

- `GET /users/{id}/recommendations?limit=10`
- `GET /users/{id}/recommendations/explain?game_id=123`

## API Client Operations

- `POST /api-keys`
- `GET /api-keys`
- `POST /api-keys/{id}/revoke`
- `GET /usage/current`
- `GET /usage/history?from=...&to=...`
- `GET /usage/limits`
- `GET /plans`

## Standard Error Codes

- `400` bad request
- `401` unauthorized
- `402` payment required (if enabled)
- `403` forbidden
- `404` not found
- `409` conflict
- `429` too many requests
- `500` internal error
