# ADR-0001: Bootstrap Structure and Workflow Foundation

## Status

Accepted

## Date

2026-03-06

## Decision

- Keep product code and public docs inside `game-scout-api/`.
- Keep `AGENTS.md` and `PLANS.md` outside this repository.
- Require documentation updates (or explicit no-impact note) for technical changes.
- Require commit traceability with `[opsx:<change-name>]` token.

## Consequences

- Better separation between publishable content and operational AI context.
- Lower risk of missing docs when project evolves.
- Clear mapping between OpenSpec changes and Git history.

## Evidence Mapping

- Proposal: `openspec/changes/bootstrap-project-structure-and-doc-governance/proposal.md`
- Design: `openspec/changes/bootstrap-project-structure-and-doc-governance/design.md`
- Specs:
  - `project-structure-bootstrap`
  - `documentation-governance`
  - `external-context-files`
  - `change-commit-discipline`
