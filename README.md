# game-scout-api

REST API for video game discovery, recommendations, and search.

## Project Bootstrap

This repository contains only product code and public project docs.
Operational context files (`AGENTS.md`, `PLANS.md`) are intentionally kept outside this Git repository.

## Repository Layout

```text
game-scout-api/
|-- app/
|-- tests/
|-- scripts/
|-- docs/
|   |-- product/
|   |-- architecture/
|   |-- api/
|   |-- decisions/
|   |-- runbooks/
|   `-- changelog/
|-- LICENSE
`-- README.md
```

## Documentation

- Main docs index: `docs/README.md`
- Product vision: `docs/product/vision.md`
- Architecture baseline: `docs/architecture/system-overview.md`
- API baseline contract: `docs/api/public-contract.md`
- Local runbook: `docs/runbooks/local-dev.md`
- Change workflow and commit policy: `docs/runbooks/change-workflow.md`

## Context Boundary (Important)

- `AGENTS.md` and `PLANS.md` MUST stay in the parent workspace directory.
- They MUST NOT be added to this repository.
- Run `scripts/check-no-context-files.sh` before commit.

## Commit Traceability

Commit messages MUST reference the active OpenSpec change using this token:

`[opsx:<change-name>]`

Example:

`chore(bootstrap): create docs baseline [opsx:bootstrap-project-structure-and-doc-governance]`
