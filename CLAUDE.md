# CLAUDE.md

## Project purpose
The official Ansible Collection for managing VyOS network appliances (`vyos.vyos` namespace). Provides modules, plugins, action handlers, terminal plugins, and resource modules for BGP, OSPF, firewall, interfaces, NTP, etc.

## Tech stack
- Ansible Collection (Galaxy). Python control-plane code under `plugins/`.
- `galaxy.yml` declares `namespace: vyos`, `name: vyos`, `version: 6.0.0`, dep `ansible.netcommon >= 2.5.1`, license_file `LICENSE` (GPL-3.0).
- Test stack: `pytest` + `tox-ansible.ini`; lint via flake8, isort, black (line-length 100), pre-commit, ansible-lint.
- Runtime deps: `paramiko`, `scp` (`requirements.txt`); `bindep.txt` for system deps.

## Build / test / run
- Build: `ansible-galaxy collection build` produces a `vyos-vyos-<version>.tar.gz`.
- Install local dev: `ansible-galaxy collection install . --force`.
- Test: `tox -e <env>` (see `tox-ansible.ini`); run sanity / unit / integration tests against VyOS 1.3.8 / 1.4.1 / 1.5-rolling.

## Repository layout
- `plugins/{action,cliconf,doc_fragments,filter,inventory,module_utils,modules,terminal}/` — collection content.
- `tests/` — sanity, unit, integration; CI under `.github/workflows/tests.yml`.
- `docs/` — generated module docs.
- `meta/`, `changelogs/`, `CHANGELOG.rst` — Galaxy + release metadata.
- `pyproject.toml` (black/pytest config), `.flake8`, `.isort.cfg`, `.ansible-lint`, `.pre-commit-config.yaml`.
- `.github/workflows/` — `tests.yml`, `release.yml`, `codecoverage.yml`, `cla-check.yml`, `ah_token_refresh.yml`, `check_label.yaml`.

## Cross-repo context
- Consumed by Ansible users running playbooks against VyOS routers built by `vyos/vyos-build`.
- Sibling of `VyOS-Networks/vyos-ansible-collection` (older, mostly stale) and `VyOS-Networks/vyos-ansible-smoketests` (Jinja2 playbook smoketests driving this collection).
- The `vyos.vyos` collection talks to VyOS via `network_cli` connections; supports the same train branches (`current`, `circinus`, `sagitta`, `equuleus`).

## Conventions
- Commit / PR title: `component: T12345: description` (Phorge ID at https://vyos.dev mandatory).
- Default branch `main` (not `current` — this repo predates the rename convention).
- Issues tracked at https://vyos.dev (see `galaxy.yml`).
- Codecov + CodeRabbit configured (`codecov.yml`, `.coderabbit.yaml`).

## Mirror relationship
Twin at `VyOS-Networks/vyos.vyos`. Canonical side here.

## Notes for future contributors
- Galaxy versioning is independent of VyOS train versioning — bump in `galaxy.yml` per release.
- Tested matrix is in README; expand only after smoketesting against real images.
- `PR408_README.md` plus `pr408-diagram.png` document a non-trivial historical refactor; read before touching resource-module structure.
