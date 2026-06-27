# Fork Operations

This fork keeps a small owner-specific health layer on top of the upstream tutorials project.

## Scope

- Preserve upstream source layout and workflows.
- Keep owner-specific checks isolated in `rrg1225_fork_health.py` and `.github/workflows/rrg1225-fork-health.yml`.
- Avoid broad rewrites that make upstream synchronization difficult.

## Maintenance

Run this before pushing fork-only changes:

```bash
python rrg1225_fork_health.py
```

The lightweight GitHub Action validates this fork layer without running the full upstream documentation build.
