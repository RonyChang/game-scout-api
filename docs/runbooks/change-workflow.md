# Change Workflow

## Mandatory Rules

- Every technical change MUST update relevant docs OR include explicit "no documentation impact" note.
- Every commit for an OpenSpec change MUST include `[opsx:<change-name>]` in the commit message.
- `AGENTS.md` and `PLANS.md` MUST remain outside `game-scout-api/`.

## Commit Format

Recommended format:

`<type>(<scope>): <summary> [opsx:<change-name>]`

Examples:

- `chore(bootstrap): add docs baseline [opsx:bootstrap-project-structure-and-doc-governance]`
- `docs(workflow): define context boundary [opsx:bootstrap-project-structure-and-doc-governance]`

## Pre-Commit Checklist

1. OpenSpec tasks updated
2. Relevant docs updated (or no-impact note documented)
3. `bash scripts/check-no-context-files.sh` passes
4. Commit message includes `[opsx:<change-name>]`
