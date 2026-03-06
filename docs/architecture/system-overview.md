# System Overview (Initial)

## Baseline Components

- FastAPI service for public HTTP endpoints
- PostgreSQL + pgvector for transactional and vector data
- Redis for rate limiting and cache
- Background jobs for ingestion, embeddings, and usage aggregation

## Request Flow (Public API)

1. Client sends `x-api-key`
2. API validates key + active subscription
3. Rate limit is enforced
4. Daily and monthly quotas are checked
5. Recommendation request is executed
6. Usage event is recorded
7. Response includes quota and rate-limit headers

## Repository Boundary

This repository stores product code and public documentation only.
`AGENTS.md` and `PLANS.md` remain outside this repository in the parent workspace.
