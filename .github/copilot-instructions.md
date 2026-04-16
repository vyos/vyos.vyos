# Copilot Review Instructions — vyos.vyos

This is the `vyos.vyos` Ansible network collection for managing VyOS devices.
Namespace `vyos`, name `vyos`, version `6.0.0`. All modules are prefixed `vyos_`.

## Copyright headers

- **New files** (not present on `origin/main`) must use `# (c) 2024 VyOS Networks <maintainers@vyos.net>`.
- **Existing files** must preserve the original copyright (Red Hat, etc.) unchanged.
- Flag any new file that uses a third-party copyright or any existing file where the copyright was modified.

## Commit and PR standards

- Every commit title must start with a Phorge task ID: `T<number>: description`.
- Every PR must have exactly one changelog fragment in `changelogs/fragments/`.
- PR descriptions that state a test count (e.g. "Add 8 unit tests") must match the actual number of test methods in the changed files. Flag mismatches.

## Changelog fragments

Fragments are YAML files under `changelogs/fragments/`. Valid top-level keys:

| Key | Use for |
|-----|---------|
| `trivial` | Developer tooling, CI, housekeeping, formatting-only changes |
| `bugfixes` | Bug fixes |
| `minor_changes` | New features or user-visible improvements |
| `major_changes` | Breaking changes |
| `security_fixes` | Security fixes |
| `doc_changes` | Documentation-only changes |

Flag any fragment that uses `minor_changes` for what is actually developer tooling (linting, formatting, gitignore, test scaffolding). Those should use `trivial`.

## Module architecture

Two module families:

**Resource modules** (`vyos_interfaces`, `vyos_firewall_rules`, `vyos_bgp_global`, etc.) follow a four-part structure under `plugins/module_utils/network/vyos/`:
- `argspec/{resource}/` — argument spec
- `config/{resource}/` — config builder
- `facts/{resource}/` — facts parser
- `rm_templates/{resource}.py` — regex/Jinja2 CLI templates

Resource modules support all states: `merged`, `replaced`, `overridden`, `deleted`, `rendered`, `gathered`, `parsed`.

**Legacy modules** (`vyos_vlan`, `vyos_config`, `vyos_command`, `vyos_user`, etc.) do not follow the resource module pattern.

## VyOS CLI conventions

- Set commands: `set interfaces ethernet eth0 address '192.0.2.1/24'`
- Delete commands: `delete interfaces ethernet eth0 address '192.0.2.1/24'`
- Values are always single-quoted in CLI output.
- Interface types: `ethernet`, `loopback`, `bonding`, `bridge`, `tunnel`, `wireguard`.
