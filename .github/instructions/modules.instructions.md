---
applyTo: "plugins/**"
---

# Plugin conventions

## Module option descriptions

- Must be complete English sentences ending with a period.
- No grammar errors. Common mistake: "the number hops" should be "the number of hops".
- Deprecated options must include `removed_in_version` and `removed_from_collection` fields.
- Do not add new options with `deprecated: true` — remove deprecated options entirely.

## rm_templates files

Files in `plugins/module_utils/network/vyos/rm_templates/` define regex parsers and Jinja2 generators for a resource module. Each entry has:
- `name` — unique identifier
- `getval` — compiled regex with named groups
- `setval` — Jinja2 template or callable producing a VyOS CLI command
- `result` — dict mapping regex groups to facts structure
- `shared` (optional) — bool, whether the template applies to a shared config block

## meta/runtime.yml redirects

Short-name redirects must point to the actual module name with the `vyos_` prefix. For example:
```yaml
snmp_server:
  redirect: vyos.vyos.vyos_snmp_server   # correct
  # NOT: vyos.vyos.vyos_snmp_servers     # wrong (pluralized)
```

Verify any changed redirect target exists as a real module file under `plugins/modules/`.

## cliconf / terminal plugins

`plugins/cliconf/vyos.py` — do not modify without understanding edit-mode and commit semantics.
`plugins/terminal/vyos.py` — handles prompt detection; regex changes require testing against all supported VyOS versions (1.3.8, 1.4.1, 1.4.2, 1.5 rolling).
