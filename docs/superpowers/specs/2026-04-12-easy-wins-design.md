# Easy Win Improvements — vyos.vyos Ansible Collection

## Overview

Five sequential phases of improvements to the vyos.vyos collection, ordered by risk (lowest first). Each phase is an independent PR with its own changelog fragment.

Collection version: 6.0.0. Minimum supported VyOS: 1.3.8. Roadmap: v7.0.0 drops VyOS 1.3.x support.

---

## Phase 1 — Formatting Compliance

**Goal:** Bring the entire codebase into compliance with configured formatters.

**Scope:**
- Run `black .` — 193 files currently fail formatting (line-length=100)
- Run `isort .` — 4 files have import ordering violations:
  - `plugins/module_utils/network/vyos/utils/version.py`
  - `plugins/module_utils/network/vyos/rm_templates/ospf_interfaces_14.py`
  - `plugins/module_utils/network/vyos/facts/bgp_global/bgp_global.py`
  - `plugins/module_utils/network/vyos/facts/bgp_address_family/bgp_address_family.py`
- Remove unused import in `plugins/module_utils/network/vyos/utils/version.py:13` — `LooseVersion` imported but never used in that file

**Verification:** `black --check . && isort --check-only . && flake8 .` all pass with zero issues.

**Changelog fragment:** `minor_changes` — "Collection-wide formatting compliance with black, isort, and flake8."

---

## Phase 2 — Fix meta/runtime.yml Redirect

**Goal:** Fix broken module redirect for `snmp_server`.

**Bug:** `meta/runtime.yml:57-58` redirects `snmp_server` to `vyos.vyos.vyos_snmp_servers` (plural). The actual module is `vyos_snmp_server` (singular). No file `vyos_snmp_servers.py` exists. All other 27 redirects are correct.

**Fix:** Change line 58 from `redirect: vyos.vyos.vyos_snmp_servers` to `redirect: vyos.vyos.vyos_snmp_server`.

**Verification:** Confirm the module `plugins/modules/vyos_snmp_server.py` exists. Grep for any other references to `vyos_snmp_servers` (plural) that might need updating.

**Changelog fragment:** `bugfixes` — "Fix meta/runtime.yml redirect for snmp_server pointing to non-existent vyos_snmp_servers module."

---

## Phase 3 — Deprecated Feature Audit and Cleanup

**Goal:** Remove dead code for features deprecated before VyOS 1.3.8 and document remaining deprecations clearly. Do NOT remove features that are still valid for 1.3.8 — those are scheduled for v7.0.0.

### 3a — Remove pre-1.3 commented-out code (safe to remove now)

`plugins/modules/vyos_bgp_global.py` contains multiple commented-out parameter blocks with notes like "Removed before 1.3", "Removed prior to 1.3", "Moved to address-family before 1.3". These are at lines 121, 149, 191, 206, 210, 231, 246, 249, 261, 264, 270, 279, 283. Remove all commented-out pre-1.3 artifacts.

### 3b — Document deprecations targeting v7.0.0 (no code removal, documentation only)

These features are deprecated but still needed for VyOS 1.3.8 support. Verify deprecation markers are correct and consistent:

| Feature | Location | Target |
|---------|----------|--------|
| `vyos_firewall_interfaces` module | `vyos_firewall_interfaces.py:49` | Deprecated in VyOS 1.4+ |
| `no_ipv4_unicast` param (bgp_global) | `vyos_bgp_global.py:406` | Unavailable after 1.4 |
| `no_ipv4_unicast` param (vrf) | `vyos_vrf.py:288` | Unavailable after 1.4 |
| `address` param (lldp_global) | `vyos_lldp_global.py:63-64` | Removal in 7.0.0 |
| `archive` param (logging_global argspec) | `logging_global.py:178-179` | `removed_in_version: 7.0.0` |
| `protocol` param (logging_global argspec) | `logging_global.py:287-288` | `removed_in_version: 7.0.0` |

For each: verify the deprecation notice text is accurate and consistent. No code removal — these still serve 1.3.8 users.

### 3c — Verify tombstoned modules

`meta/runtime.yml:36-42` tombstones `logging` and `vyos_logging` with `removal_version: 6.0.0`. Verify no code for these modules still exists. If stale code remains, remove it.

**Verification:** `grep -r "Removed before 1.3\|Removed prior to 1.3\|Moved to address-family before 1.3" plugins/` returns no results after cleanup.

**Changelog fragment:** `minor_changes` — "Remove commented-out pre-1.3 deprecated parameter artifacts from vyos_bgp_global module documentation."

---

## Phase 4 — Missing Unit Tests

**Goal:** Add unit tests for the three modules that lack them.

### 4a — vyos_l3_interfaces (resource module)

- Create `tests/unit/modules/network/vyos/test_vyos_l3_interfaces.py`
- Create fixture `tests/unit/modules/network/vyos/fixtures/vyos_l3_interfaces_config.cfg`
- Follow pattern from `test_vyos_interfaces.py` (TestVyosModule base, mock facts + connection)
- Test cases: merged, merged_idempotent, replaced, overridden, deleted, rendered, gathered, parsed
- Include VIF (virtual sub-interface) test cases

### 4b — vyos_lldp_interfaces (resource module)

- Create `tests/unit/modules/network/vyos/test_vyos_lldp_interfaces.py`
- Create fixture `tests/unit/modules/network/vyos/fixtures/vyos_lldp_interfaces_config.cfg`
- Follow same resource module test pattern
- Test cases: merged, merged_idempotent, replaced, overridden, deleted, rendered, gathered, parsed
- Include coordinate-based location and ELIN-specific tests

### 4c — vyos_vlan (legacy module — different pattern)

- Create `tests/unit/modules/network/vyos/test_vyos_vlan.py`
- Create fixture `tests/unit/modules/network/vyos/fixtures/vyos_vlan_config.cfg`
- Legacy module uses `present`/`absent` states (not merged/replaced/etc.)
- Uses `load_config()` directly, not ConfigBase
- Test cases: present, present_idempotent, absent, aggregate, with_address, with_interfaces

**Verification:** `pytest tests/unit -vvv -n 2` passes with new tests included. No regressions in existing tests.

**Changelog fragment:** `minor_changes` — "Add unit tests for vyos_l3_interfaces, vyos_lldp_interfaces, and vyos_vlan modules."

---

## Phase 5 — Template Deduplication

**Goal:** Reduce duplication between version-specific template pairs by extracting shared logic into a base, with version-specific overrides.

### Current State

Four template pairs exist in `plugins/module_utils/network/vyos/rm_templates/`:

| Base | VyOS 1.4+ variant | Lines (base/14) | Key difference |
|------|--------------------|------------------|----------------|
| `bgp_global.py` | `bgp_global_14.py` | 1859/1795 | `{as_number}` in command paths |
| `bgp_address_family.py` | `bgp_address_family_14.py` | 1450/1433 | `{as_number}` in command paths |
| `route_maps.py` | `route_maps_14.py` | 1405/1405 | Class naming only |
| `ospf_interfaces.py` | `ospf_interfaces_14.py` | 776/650 | Interface-centric vs protocol-centric paths |

### Dispatch mechanism

Config modules (e.g., `config/bgp_global/bgp_global.py`) import both template classes and switch via `_validate_template()` using `LooseVersion(get_os_version(module)) >= LooseVersion("1.4")`. Facts modules do the same in `populate_facts()`.

### Deduplication strategy

**For BGP templates (bgp_global, bgp_address_family):** The only difference is `{as_number}` in command path strings. Extract a base class with a `_cmd_prefix()` method that returns the protocol path prefix. Pre-1.4 subclass includes `{as_number}`, 1.4+ subclass omits it. All template functions and PARSERS list stay in the base.

**For route_maps:** These are identical except the class name. Merge into a single file. The `_14` variant becomes a subclass alias or is eliminated entirely.

**For ospf_interfaces:** The structural difference is larger (interface-centric vs protocol-centric command paths). These may not be good deduplication candidates. Assess shared template entries vs divergent ones. If >70% shared, extract a base; otherwise leave as-is.

### Files to modify

For each deduplicated template pair:
- Create or modify the base template file with shared logic
- Modify the `_14` file to inherit from the base, overriding only what differs
- Update imports in corresponding `config/` and `facts/` modules if class names change
- Update corresponding unit test imports if any

### Constraints

- The dispatch mechanism in config and facts modules must continue to work identically
- All existing unit tests must pass without modification (except import path changes)
- Template class interfaces (PARSERS list, method signatures) must remain identical

**Verification:** Full test suite passes. Manual review of generated commands for both VyOS versions matches current behavior.

**Changelog fragment:** `minor_changes` — "Refactor version-specific rm_templates to reduce duplication between pre-1.4 and 1.4+ variants."

---

## Ordering Rationale

1. **Formatting first** — creates a clean diff baseline for all subsequent work
2. **Runtime fix** — trivial, fixes a real bug
3. **Deprecation cleanup** — removes dead code before we add tests or refactor around it
4. **Tests** — adds coverage before the highest-risk refactor
5. **Deduplication** — highest risk, most lines changed, benefits from all prior cleanup
