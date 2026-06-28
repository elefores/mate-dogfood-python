# mate-dogfood-python

A small, intentionally outdated **Python** app used as a dogfooding fixture for
[MATE (Keep Up)](https://github.com/elefores). It exists so keepup has a realistic
target to run against in CI.

## The app

A tiny Flask service (`src/app.py`) that validates user payloads with a Pydantic
model (`src/models.py`) and a pytest suite (`tests/`).

## Intentionally outdated dependencies

`requirements.txt` pins everything a few versions behind current. The headline
pin is the **breaking-change gap**:

| Dependency | Pinned | Why it matters |
|------------|--------|----------------|
| `pydantic` | `1.10.13` | **Breaking gap.** Upgrading to 2.x reworks `@validator` → `@field_validator`, `class Config` → `model_config`, and `.dict()` → `.model_dump()`. `src/models.py` uses the v1 APIs, so the upgrade must touch code. |
| `flask` | `2.2.5` | A few minor versions behind 3.x. |
| `requests` | `2.28.2` | Behind the current 2.3x line. |
| `pytest` | `7.2.2` | Behind 8.x (ignored in `kup.toml`). |

This makes keepup exercise the **AI code-upgrade path**, not just a version bump.

## keepup config

See [`kup.toml`](kup.toml): it includes Python sources under `src/`, ignores the
test pins, sets grouping thresholds, and selects the Claude Code agent.

## CI

[`.github/workflows/keepup.yml`](.github/workflows/keepup.yml) runs keepup on a
weekly schedule (and on demand). Set these repository secrets for it to run:

- `KUP_LICENSE_KEY` — signed keepup license key
- `CLAUDE_CODE_OAUTH_TOKEN` — Claude Code agent token
- `ACCESS_TOKEN` — GitHub token used to push branches and open PRs
