---
applyTo: "tests/unit/**"
---

# Unit test conventions

## Base class and structure

All test classes inherit from `TestVyosModule` in `tests/unit/modules/network/vyos/vyos_module.py`.

```python
class TestVyosFooModule(TestVyosModule):
    module = vyos_foo

    def setUp(self): ...
    def tearDown(self): ...
    def load_fixtures(self, commands=None, filename=None): ...
    def test_...(self): ...
```

## Mocking: resource modules

Resource modules (argspec/config/facts/rm_templates pattern) patch at the `get_resource_connection` level:

```python
self.mock_get_resource_connection_config = patch(
    "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection"
)
self.mock_get_resource_connection_facts = patch(
    "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
)
```

`load_fixtures` sets: `self.get_resource_connection_facts.return_value.get_config.return_value = fixture_data`

## Mocking: legacy modules

Legacy modules (`vyos_vlan`, `vyos_config`, `vyos_command`, etc.) patch directly in the module:

```python
self.mock_run_commands = patch("ansible_collections.vyos.vyos.plugins.modules.vyos_foo.run_commands")
self.mock_load_config = patch("ansible_collections.vyos.vyos.plugins.modules.vyos_foo.load_config")
```

`load_fixtures` sets: `self.run_commands.return_value = [fixture_data]`

## load_fixtures and filename

`execute_module()` always calls `load_fixtures()`. Never set mock return values inside a test method after calling `execute_module` — they will be overwritten. Use the `filename` parameter to select fixtures:

```python
def load_fixtures(self, commands=None, filename=None):
    if filename == "alternate":
        self.run_commands.return_value = [ALTERNATE_OUTPUT]
    else:
        self.run_commands.return_value = [DEFAULT_OUTPUT]
```

Then call: `self.execute_module(changed=True, commands=commands, filename="alternate")`

## Fixture files

Raw device CLI output lives in `tests/unit/modules/network/vyos/fixtures/` as `.cfg` files.
Load with `load_fixture("vyos_foo_config.cfg")`.

## Required test coverage for resource modules

A complete resource module test file should cover all applicable states:
- `merged` (including an idempotent case)
- `replaced`
- `overridden`
- `deleted`
- `rendered` — assert `result["rendered"]` matches expected CLI commands
- `gathered` — assert `result["gathered"]` contains expected structured data
- `parsed` — pass `running_config=raw_string` and assert `result["parsed"]`

Flag test files that are missing `rendered`, `gathered`, or `parsed` tests without explanation.

## Copyright

New test files created for this project must use:
```python
# (c) 2024 VyOS Networks <maintainers@vyos.net>
```
Do not copy Red Hat or other third-party copyright headers onto new files.
