# Local Development Runbook

## Prerequisites

- Python 3.12
- Docker and Docker Compose
- PostgreSQL 16 (or container)
- Redis 7 (or container)

## Initial Bootstrap Checklist

1. Confirm baseline directories exist:
   - `app/`, `tests/`, `scripts/`, `docs/`
2. Read docs entry point:
   - `docs/README.md`
3. Confirm context boundary:
   - `AGENTS.md` and `PLANS.md` are outside repository
4. Run boundary check script:
   - `bash scripts/check-no-context-files.sh`

## Daily Workflow

1. Update OpenSpec artifact/task state
2. Implement scoped changes
3. Update docs or record no-impact note
4. Run checks
5. Commit with traceability token
