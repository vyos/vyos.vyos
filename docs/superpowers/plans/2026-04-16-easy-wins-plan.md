# Easy Wins Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Four sequential quality improvements to the vyos.vyos Ansible collection — formatting, bugfix, dead code removal, test coverage. (Template deduplication was evaluated and deferred to v7.0.0 — see spec for rationale.)

**Architecture:** Each phase is an independent branch and PR. Phases are ordered by risk: mechanical formatting first, then a one-line bugfix, then dead code cleanup, then new tests. **Each phase must be merged to `main` before the next phase branches** — later phases depend on earlier ones for clean diffs and test coverage.

**Tech Stack:** Python 3, Ansible (netcommon), pytest, black, isort, flake8

**Spec:** `docs/superpowers/specs/2026-04-12-easy-wins-design.md`

---

## Phase 1: Formatting Compliance

### Task 1: Run black formatter across entire codebase

**Files:**
- Modify: ~193 Python files across `plugins/` and `tests/`

- [ ] **Step 1: Create branch**

```bash
git checkout -b fix/formatting-compliance main
```

- [ ] **Step 2: Run black formatter**

```bash
black .
```

Expected: "reformatted N files" (approximately 193 files).

- [ ] **Step 3: Verify black passes**

```bash
black --check .
```

Expected: "All done!" with exit code 0.

- [ ] **Step 4: Commit black changes**

```bash
git add -A
git commit -m "style: apply black formatting across entire codebase"
```

### Task 2: Fix isort violations

**Files:**
- Modify: `plugins/module_utils/network/vyos/rm_templates/ospf_interfaces_14.py`
- Modify: `plugins/module_utils/network/vyos/facts/bgp_global/bgp_global.py`
- Modify: `plugins/module_utils/network/vyos/facts/bgp_address_family/bgp_address_family.py`

Note: `plugins/module_utils/network/vyos/utils/version.py` imports `LooseVersion` with `# pylint: disable=unused-import`. This is a deliberate re-export — 19 files import `LooseVersion` through this module. Do NOT remove this import or change isort's handling of it.

- [ ] **Step 1: Run isort**

```bash
isort .
```

- [ ] **Step 2: Verify isort passes**

```bash
isort --check-only .
```

Expected: exit code 0, no violations.

- [ ] **Step 3: Commit isort changes**

```bash
git add -A
git commit -m "style: fix isort import ordering violations"
```

### Task 3: Fix flake8 issues, add .git-blame-ignore-revs, verify, and add changelog

**Files:**
- Possibly modify: files with new flake8 issues after black/isort
- Create: `.git-blame-ignore-revs`
- Create: `changelogs/fragments/formatting-compliance.yml`

- [ ] **Step 1: Run flake8 and fix any issues**

```bash
flake8 .
```

Black/isort may have introduced new flake8 violations (e.g., line-length edge cases in comments, unused variables exposed by reformatting). Fix any that appear before proceeding.

- [ ] **Step 2: Run full lint suite**

```bash
black --check . && isort --check-only . && flake8 .
```

Expected: All three pass with zero issues.

- [ ] **Step 3: Run unit tests to confirm no regressions**

```bash
pytest tests/unit -vvv -n 2
```

Expected: All tests pass.

- [ ] **Step 4: Get the formatting commit hash and create .git-blame-ignore-revs**

A 193-file formatting commit pollutes `git blame`. Add the commit hash to `.git-blame-ignore-revs` so tools like `git blame --ignore-revs-file` skip it:

```bash
FORMATTING_HASH=$(git log --oneline --all | grep "style: apply black formatting" | awk '{print $1}')
```

Create `.git-blame-ignore-revs`:

```
# black formatting pass
<FORMATTING_HASH>
```

Replace `<FORMATTING_HASH>` with the actual commit hash from the command above.

- [ ] **Step 5: Commit .git-blame-ignore-revs**

```bash
git add .git-blame-ignore-revs
git commit -m "chore: add .git-blame-ignore-revs for formatting commit"
```

- [ ] **Step 6: Create changelog fragment**

Create `changelogs/fragments/formatting-compliance.yml`:

```yaml
---
minor_changes:
  - Collection-wide formatting compliance with black and isort.
```

- [ ] **Step 7: Commit changelog**

```bash
git add changelogs/fragments/formatting-compliance.yml
git commit -m "chore: add changelog fragment for formatting compliance"
```

---

## Phase 2: Fix meta/runtime.yml Redirect

### Task 4: Fix snmp_server redirect typo

**Files:**
- Modify: `meta/runtime.yml:58`
- Create: `changelogs/fragments/fix-snmp-server-redirect.yml`

- [ ] **Step 1: Create branch**

```bash
git checkout -b fix/snmp-server-redirect main
```

- [ ] **Step 2: Verify the bug exists**

```bash
grep "vyos_snmp_servers" meta/runtime.yml
```

Expected output: `      redirect: vyos.vyos.vyos_snmp_servers`

Verify the correct module exists:

```bash
ls plugins/modules/vyos_snmp_server.py
```

Expected: file exists.

```bash
ls plugins/modules/vyos_snmp_servers.py 2>/dev/null; echo "exit: $?"
```

Expected: file does not exist, exit code non-zero.

- [ ] **Step 3: Fix the redirect**

In `meta/runtime.yml`, change line 58 from:

```yaml
      redirect: vyos.vyos.vyos_snmp_servers
```

to:

```yaml
      redirect: vyos.vyos.vyos_snmp_server
```

- [ ] **Step 4: Check for other references to the plural form**

```bash
grep -r "vyos_snmp_servers" . --include="*.py" --include="*.yml" --include="*.yaml" | grep -v "docs/superpowers"
```

Expected: Only `meta/runtime.yml` should match (now fixed). If other files reference the plural form, fix those too.

- [ ] **Step 5: Create changelog fragment**

Create `changelogs/fragments/fix-snmp-server-redirect.yml`:

```yaml
---
bugfixes:
  - Fix meta/runtime.yml redirect for snmp_server pointing to non-existent vyos_snmp_servers module.
```

- [ ] **Step 6: Commit**

```bash
git add meta/runtime.yml changelogs/fragments/fix-snmp-server-redirect.yml
git commit -m "fix: correct snmp_server redirect in meta/runtime.yml"
```

---

## Phase 3: Deprecated Feature Cleanup

### Task 5: Remove pre-1.3 commented-out code from vyos_bgp_global

**Files:**
- Modify: `plugins/modules/vyos_bgp_global.py`

- [ ] **Step 1: Create branch**

```bash
git checkout -b chore/deprecated-cleanup main
```

- [ ] **Step 2: Identify all commented-out pre-1.3 blocks**

The following commented-out blocks in `plugins/modules/vyos_bgp_global.py` are pre-1.3 artifacts and must be removed. Each block starts with a `#` comment containing one of these markers:
- "Moved to address-family before 1.3"
- "Removed before 1.3"
- "Removed prior to 1.3"

Remove these complete commented-out blocks (the marker line AND all indented commented lines that follow as part of that parameter's YAML documentation block):

1. Lines ~86-89: `allowas_in` — "Moved to address-family before 1.3"
2. Lines ~90-93: `as_override` — "Moved to address-family before 1.3"
3. Lines ~94-107: `attribute_unchanged` — "Moved to address-family before 1.3" (includes suboptions)
4. Lines ~121-127: `orf` — "Removed before 1.3" (includes choices)
5. Lines ~149-161: `distribute_list` — "Moved to address-family before 1.3" (includes suboptions)
6. Lines ~166-190: `interface` comment block — "added in 1.3" (this is a commented-out description of a feature, not active code)
7. Lines ~191-202: `filter_list` — "Moved to address-family before 1.3" (includes suboptions)
8. Lines ~206-212: `maximum_prefix` and `nexthop_self` — "Moved to address-family before 1.3"
9. Lines ~231-242: `prefix_list` — "Moved to address-family before 1.3" (includes suboptions)
10. Lines ~246-248: `remove_private_as` — "Moved to address-family before 1.3"
11. Lines ~249-260: `route_map` — "Moved to address-family before 1.3" (includes suboptions)
12. Lines ~261-263: `route_reflector_client` — "Moved to address-family before 1.3"
13. Lines ~264-266: `route_server_client` — "Removed prior to 1.3"
14. Lines ~270-272: `soft_reconfiguration` — "Moved to address-family before 1.3"
15. Lines ~279-281: `unsuppress_map` — "Moved to address-family before 1.3"
16. Lines ~283-285: `weight` — "Moved to address-family before 1.3"

**Important:** Do NOT remove the `# <-- added in 1.3` inline comment on `solo` (line ~273) — that's an active parameter notation, not dead code.

- [ ] **Step 3: Remove all identified blocks**

Open `plugins/modules/vyos_bgp_global.py` and remove all 16 blocks listed above. After removal, the YAML docstring should flow cleanly from `capability:` → `extended_nexthop:` directly to `default_originate:`, and from `port:` directly to `remote_as:`, etc.

- [ ] **Step 4: Verify removal is complete**

```bash
grep -n "Removed before 1.3\|Removed prior to 1.3\|Moved to address-family before 1.3" plugins/modules/vyos_bgp_global.py
```

Expected: No output (all markers removed).

- [ ] **Step 5: Run unit tests**

```bash
pytest tests/unit/modules/network/vyos/test_vyos_bgp_global.py -vvv
```

Expected: All tests pass. These tests exercise config/facts, not DOCUMENTATION strings, so removing commented-out YAML should have no effect.

- [ ] **Step 6: Commit**

```bash
git add plugins/modules/vyos_bgp_global.py
git commit -m "chore: remove commented-out pre-1.3 parameter artifacts from vyos_bgp_global docs"
```

### Task 6: Verify tombstoned modules have no stale code

**Files:**
- Possibly modify: any stale `vyos_logging.py` files (if found)

- [ ] **Step 1: Check for stale logging module code**

`meta/runtime.yml` tombstones `logging` and `vyos_logging` (removal_version 6.0.0). Verify no module files exist:

```bash
ls plugins/modules/vyos_logging.py 2>/dev/null; echo "exit: $?"
find plugins/ -name "*vyos_logging*" -not -name "*logging_global*" | head -20
```

Expected: No files found (the tombstoned modules are already removed and replaced by `vyos_logging_global`).

- [ ] **Step 2: Check for stale vrf.old file**

A file `plugins/module_utils/network/vyos/config/vrf/vrf.old` is tracked in git. This appears to be a leftover from development:

```bash
head -5 plugins/module_utils/network/vyos/config/vrf/vrf.old
```

If it's a backup/old version of `vrf.py`, remove it:

```bash
git rm plugins/module_utils/network/vyos/config/vrf/vrf.old
```

- [ ] **Step 3: Verify deprecation markers on v7.0.0-targeted features**

These features are deprecated but still needed for VyOS 1.3.8 support. Verify each has correct deprecation documentation (read-only, no changes unless text is wrong):

```bash
grep -n -A2 "Deprecated" plugins/modules/vyos_firewall_interfaces.py | head -10
grep -n -A2 "Deprecated\|Unavailable after 1.4" plugins/modules/vyos_bgp_global.py | head -10
grep -n -A2 "Deprecated\|Unavailable after 1.4" plugins/modules/vyos_vrf.py | head -10
grep -n "removed_in_version" plugins/module_utils/network/vyos/argspec/logging_global/logging_global.py
```

Expected: Each prints existing deprecation markers. No changes needed if text is accurate.

- [ ] **Step 4: Create changelog fragment**

Create `changelogs/fragments/deprecated-cleanup.yml`:

```yaml
---
minor_changes:
  - vyos_bgp_global - remove commented-out pre-1.3 deprecated parameter documentation artifacts.
```

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "chore: remove stale pre-1.3 artifacts and verify deprecation markers"
```

---

## Phase 4: Missing Unit Tests

### Task 7: Add unit tests for vyos_l3_interfaces

**Files:**
- Create: `tests/unit/modules/network/vyos/fixtures/vyos_l3_interfaces_config.cfg`
- Create: `tests/unit/modules/network/vyos/test_vyos_l3_interfaces.py`

- [ ] **Step 1: Create branch**

```bash
git checkout -b test/missing-unit-tests main
```

- [ ] **Step 2: Create fixture file**

Create `tests/unit/modules/network/vyos/fixtures/vyos_l3_interfaces_config.cfg`:

```
set interfaces ethernet eth0 address 'dhcp'
set interfaces ethernet eth1 address '192.0.2.14/24'
set interfaces ethernet eth2 address '192.0.2.10/24'
set interfaces ethernet eth2 address '2001:db8::10/32'
set interfaces ethernet eth3 address '198.51.100.10/24'
set interfaces ethernet eth3 vif 101 address '198.51.100.130/25'
set interfaces ethernet eth3 vif 102 address '2001:db8:4000::3/34'
set interfaces loopback lo
```

- [ ] **Step 3: Create test file**

Create `tests/unit/modules/network/vyos/test_vyos_l3_interfaces.py`:

```python
# (c) 2016 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_l3_interfaces
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosL3InterfacesModule(TestVyosModule):
    module = vyos_l3_interfaces

    def setUp(self):
        super(TestVyosL3InterfacesModule, self).setUp()
        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos."
            "facts.l3_interfaces.l3_interfaces.L3_interfacesFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        self.fixture_path = "vyos_l3_interfaces_config.cfg"

    def tearDown(self):
        super(TestVyosL3InterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture(self.fixture_path)

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_l3_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv4=[dict(address="192.0.2.15/24")],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set interfaces ethernet eth1 address '192.0.2.15/24'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv4=[dict(address="192.0.2.14/24")],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_l3_interfaces_merged_ipv6(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv6=[dict(address="2001:db8::1/64")],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set interfaces ethernet eth1 address '2001:db8::1/64'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth2",
                        ipv4=[dict(address="203.0.113.1/24")],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "delete interfaces ethernet eth2 address '192.0.2.10/24'",
            "delete interfaces ethernet eth2 address '2001:db8::10/32'",
            "set interfaces ethernet eth2 address '203.0.113.1/24'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(name="eth1"),
                ],
                state="deleted",
            ),
        )
        commands = [
            "delete interfaces ethernet eth1 address '192.0.2.14/24'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False, commands=[])
        self.assertIn("gathered", result)

    def test_vyos_l3_interfaces_parsed(self):
        parsed_cfg = (
            "set interfaces ethernet eth1 address '192.0.2.14/24'\n"
            "set interfaces ethernet eth2 address '192.0.2.10/24'"
        )
        set_module_args(dict(state="parsed", running_config=parsed_cfg))
        result = self.execute_module(changed=False, commands=[])
        self.assertIn("parsed", result)

    def test_vyos_l3_interfaces_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv4=[dict(address="192.0.2.14/24")],
                    ),
                ],
                state="overridden",
            ),
        )
        # Overridden removes config from all interfaces not in the desired state
        result = self.execute_module(changed=True)
        # Verify commands contain delete operations for interfaces not specified
        self.assertTrue(
            any("delete" in cmd for cmd in result.get("commands", [])),
        )

    def test_vyos_l3_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        ipv4=[dict(address="10.0.0.1/24")],
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            "set interfaces ethernet eth4 address '10.0.0.1/24'",
        ]
        self.execute_module(changed=False, commands=commands)

    def test_vyos_l3_interfaces_vif_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        vifs=[
                            dict(
                                vlan_id=101,
                                ipv4=[dict(address="198.51.100.131/25")],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set interfaces ethernet eth3 vif 101 address '198.51.100.131/25'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_vif_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        vifs=[
                            dict(vlan_id=101),
                        ],
                    ),
                ],
                state="deleted",
            ),
        )
        commands = [
            "delete interfaces ethernet eth3 vif 101 address '198.51.100.130/25'",
        ]
        self.execute_module(changed=True, commands=commands)
```

- [ ] **Step 4: Run the tests**

```bash
pytest tests/unit/modules/network/vyos/test_vyos_l3_interfaces.py -vvv
```

Expected: All tests pass. If any fail, examine the fixture data and expected commands — the module's facts parser and config builder determine what commands get generated. Adjust fixture data or expected commands to match.

- [ ] **Step 5: Commit**

```bash
git add tests/unit/modules/network/vyos/test_vyos_l3_interfaces.py tests/unit/modules/network/vyos/fixtures/vyos_l3_interfaces_config.cfg
git commit -m "test: add unit tests for vyos_l3_interfaces module"
```

### Task 8: Add unit tests for vyos_lldp_interfaces

**Files:**
- Create: `tests/unit/modules/network/vyos/fixtures/vyos_lldp_interfaces_config.cfg`
- Create: `tests/unit/modules/network/vyos/test_vyos_lldp_interfaces.py`

- [ ] **Step 1: Create fixture file**

Create `tests/unit/modules/network/vyos/fixtures/vyos_lldp_interfaces_config.cfg`:

```
set service lldp interface eth1 location elin '0000000911'
set service lldp interface eth2 location coordinate-based altitude '2200'
set service lldp interface eth2 location coordinate-based datum 'WGS84'
set service lldp interface eth2 location coordinate-based latitude '33.524449N'
set service lldp interface eth2 location coordinate-based longitude '222.267255W'
```

- [ ] **Step 2: Create test file**

Create `tests/unit/modules/network/vyos/test_vyos_lldp_interfaces.py`:

```python
# (c) 2016 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_lldp_interfaces
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosLldpInterfacesModule(TestVyosModule):
    module = vyos_lldp_interfaces

    def setUp(self):
        super(TestVyosLldpInterfacesModule, self).setUp()
        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos."
            "facts.lldp_interfaces.lldp_interfaces.Lldp_interfacesFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        self.fixture_path = "vyos_lldp_interfaces_config.cfg"

    def tearDown(self):
        super(TestVyosLldpInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture(self.fixture_path)

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_lldp_interfaces_merged_elin(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        location=dict(elin="9911"),
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set service lldp interface eth3 location elin '9911'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_interfaces_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="0000000911"),
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_lldp_interfaces_merged_coordinate(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        location=dict(
                            coordinate_based=dict(
                                altitude=1000,
                                datum="WGS84",
                                latitude="40.0N",
                                longitude="74.0W",
                            ),
                        ),
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set service lldp interface eth3 location coordinate-based altitude '1000'",
            "set service lldp interface eth3 location coordinate-based datum 'WGS84'",
            "set service lldp interface eth3 location coordinate-based latitude '40.0N'",
            "set service lldp interface eth3 location coordinate-based longitude '74.0W'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="1234567890"),
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "delete service lldp interface eth1 location elin '0000000911'",
            "set service lldp interface eth1 location elin '1234567890'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_interfaces_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="0000000911"),
                    ),
                ],
                state="overridden",
            ),
        )
        # Overridden removes config from all interfaces not specified (eth2 should be deleted)
        result = self.execute_module(changed=True)
        self.assertTrue(
            any("delete" in cmd and "eth2" in cmd for cmd in result.get("commands", [])),
        )

    def test_vyos_lldp_interfaces_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(name="eth1"),
                ],
                state="deleted",
            ),
        )
        commands = [
            "delete service lldp interface eth1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_interfaces_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False, commands=[])
        self.assertIn("gathered", result)

    def test_vyos_lldp_interfaces_parsed(self):
        parsed_cfg = "set service lldp interface eth1 location elin '0000000911'"
        set_module_args(dict(state="parsed", running_config=parsed_cfg))
        result = self.execute_module(changed=False, commands=[])
        self.assertIn("parsed", result)
```

- [ ] **Step 3: Run the tests**

```bash
pytest tests/unit/modules/network/vyos/test_vyos_lldp_interfaces.py -vvv
```

Expected: All tests pass. Adjust fixture data or expected commands if the facts parser returns different structures than expected.

- [ ] **Step 4: Commit**

```bash
git add tests/unit/modules/network/vyos/test_vyos_lldp_interfaces.py tests/unit/modules/network/vyos/fixtures/vyos_lldp_interfaces_config.cfg
git commit -m "test: add unit tests for vyos_lldp_interfaces module"
```

### Task 9: Add unit tests for vyos_vlan (legacy module)

**Files:**
- Create: `tests/unit/modules/network/vyos/test_vyos_vlan.py`

Note: `vyos_vlan` is a legacy module — it uses `get_config`/`load_config`/`run_commands` directly, not the resource module pattern. It uses `present`/`absent` states. The test pattern follows `test_vyos_banner.py`, not the resource module tests. This module also calls `run_commands` to do `show interfaces` for `map_config_to_obj`, so we need to mock that too.

- [ ] **Step 1: Create test file**

Create `tests/unit/modules/network/vyos/test_vyos_vlan.py`:

```python
# (c) 2016 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_vlan
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule


SHOW_INTERFACES_OUTPUT = """\
Codes: S - State, L - Link, u - Up, D - Down, A - Admin Down
Interface        IP Address                        S/L  Description
---------        ----------                        ---  -----------
eth0             10.0.2.15/24                      u/u
eth0.100         -                                 u/u  vlan-100
eth1             -                                 u/u
eth1.200         192.0.2.1/24                      u/u  vlan-200
eth2             -                                 u/u
lo               127.0.0.1/8                       u/u
                 ::1/128
"""


class TestVyosVlanModule(TestVyosModule):
    module = vyos_vlan

    def setUp(self):
        super(TestVyosVlanModule, self).setUp()

        self.mock_load_config = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_vlan.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_run_commands = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_vlan.run_commands",
        )
        self.run_commands = self.mock_run_commands.start()

    def tearDown(self):
        super(TestVyosVlanModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_run_commands.stop()

    def load_fixtures(self, commands=None, filename=None):
        self.load_config.return_value = dict(diff=None, session="session")
        self.run_commands.return_value = [SHOW_INTERFACES_OUTPUT]

    def test_vyos_vlan_present(self):
        set_module_args(
            dict(
                vlan_id=300,
                name="vlan-300",
                interfaces=["eth2"],
                state="present",
            ),
        )
        commands = [
            "set interfaces ethernet eth2 vif 300 description vlan-300",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_present_no_change(self):
        set_module_args(
            dict(
                vlan_id=100,
                interfaces=["eth0"],
                state="present",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_vlan_absent(self):
        set_module_args(
            dict(
                vlan_id=100,
                interfaces=["eth0"],
                state="absent",
            ),
        )
        commands = [
            "delete interfaces ethernet eth0 vif 100",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_absent_no_change(self):
        set_module_args(
            dict(
                vlan_id=999,
                interfaces=["eth0"],
                state="absent",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_vlan_aggregate(self):
        set_module_args(
            dict(
                aggregate=[
                    dict(vlan_id=300, interfaces=["eth2"]),
                    dict(vlan_id=400, interfaces=["eth2"], name="vlan-400"),
                ],
            ),
        )
        commands = [
            "set interfaces ethernet eth2 vif 300",
            "set interfaces ethernet eth2 vif 400 description vlan-400",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_purge(self):
        set_module_args(
            dict(
                vlan_id=100,
                interfaces=["eth0"],
                state="present",
                purge=True,
            ),
        )
        # Purge should delete VLANs not in the desired state (eth1.200 should be deleted)
        result = self.execute_module(changed=True)
        self.assertTrue(
            any("delete" in cmd and "200" in cmd for cmd in result.get("commands", [])),
        )

    def test_vyos_vlan_with_address(self):
        set_module_args(
            dict(
                vlan_id=300,
                interfaces=["eth2"],
                address="10.0.30.1/24",
                state="present",
            ),
        )
        commands = [
            "set interfaces ethernet eth2 vif 300 address 10.0.30.1/24",
        ]
        self.execute_module(changed=True, commands=commands)
```

- [ ] **Step 2: Run the tests**

```bash
pytest tests/unit/modules/network/vyos/test_vyos_vlan.py -vvv
```

Expected: All tests pass. The `show interfaces` mock output must match what `map_config_to_obj` parses — if tests fail, examine the parsing logic in `vyos_vlan.py:271-300` and adjust `SHOW_INTERFACES_OUTPUT` to produce the expected parsed objects.

- [ ] **Step 3: Commit**

```bash
git add tests/unit/modules/network/vyos/test_vyos_vlan.py
git commit -m "test: add unit tests for vyos_vlan module"
```

### Task 10: Verify full test suite and add changelog

**Files:**
- Create: `changelogs/fragments/missing-unit-tests.yml`

- [ ] **Step 1: Run full test suite**

```bash
pytest tests/unit -vvv -n 2
```

Expected: All tests pass, including the 3 new test files. No regressions.

- [ ] **Step 2: Create changelog fragment**

Create `changelogs/fragments/missing-unit-tests.yml`:

```yaml
---
minor_changes:
  - Add unit tests for vyos_l3_interfaces, vyos_lldp_interfaces, and vyos_vlan modules.
```

- [ ] **Step 3: Commit**

```bash
git add changelogs/fragments/missing-unit-tests.yml
git commit -m "chore: add changelog fragment for new unit tests"
```

---

## Phase 5: Template Deduplication — DEFERRED

**Status:** Deferred to v7.0.0. See spec for full rationale.

**Summary of findings from architect review:**

1. **route_maps are NOT identical** — ~12 semantic differences in VyOS CLI syntax (`as-path exclude` vs `as-path-exclude`, `extcommunity rt` vs `extcommunity-rt`, different `community`/`large-community` handling). A thin subclass alias would break VyOS 1.4 functionality.

2. **BGP templates blocked by Python scoping** — template functions are module-level (not class methods). Python resolves module-level constants at the module where the function is *defined*, not where it is *called*. Importing functions from a base file and having them use the importing file's `_BGP_PREFIX` constant does not work. Real dedup would require converting ~14-28 functions to class methods or a factory pattern — high risk, marginal gain.

3. **ospf_interfaces have fundamentally different command paradigms** — interface-centric (pre-1.4) vs protocol-centric (1.4+). Not parameterizable.

4. **v7.0.0 eliminates the problem at its source** — dropping VyOS 1.3.x support means deleting the pre-1.4 templates entirely, with zero refactoring risk.

No tasks in this phase. Template deduplication should be revisited as part of the v7.0.0 release work.
