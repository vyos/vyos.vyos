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

Resource module tests require two framework-level patches in `setUp`:

```python
self.mock_get_resource_connection_config = patch(
    "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection"
)
self.mock_get_resource_connection_facts = patch(
    "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
)
```

Most resource module tests also patch the facts class's `get_device_data` method directly and use it in `load_fixtures`:

```python
# in setUp:
self.mock_execute_show_command = patch(
    "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos."
    "facts.{resource}.{resource}.{Resource}Facts.get_device_data"
)
self.execute_show_command = self.mock_execute_show_command.start()

# in load_fixtures:
def load_from_file(*args, **kwargs):
    return load_fixture("vyos_{resource}_config.cfg")
self.execute_show_command.side_effect = load_from_file
```

An alternative pattern sets `self.get_resource_connection_facts.return_value.get_config.return_value = fixture_data` in `load_fixtures` instead — both approaches work, but the `get_device_data` pattern is used by most existing tests.

## Mocking: legacy modules

Legacy modules (`vyos_vlan`, `vyos_config`, `vyos_command`, etc.) patch the specific helper the module calls, directly in the module under test. Which helper depends on the module:

```python
# vyos_command, vyos_facts, vyos_ping — patch run_commands
self.mock_run_commands = patch("ansible_collections.vyos.vyos.plugins.modules.vyos_foo.run_commands")
# vyos_config — patch get_config / load_config
self.mock_load_config = patch("ansible_collections.vyos.vyos.plugins.modules.vyos_foo.load_config")
```

In `load_fixtures`, configure the mock using `side_effect` (for dynamic fixture loading) or `return_value` (for a fixed response):

```python
# side_effect — used by most existing legacy tests
def load_from_file(*args, **kwargs):
    return load_fixture("vyos_foo_config.cfg")
self.run_commands.side_effect = load_from_file

# return_value — acceptable for simple fixed responses
self.run_commands.return_value = [SHOW_OUTPUT]
```

## load_fixtures and filename

`execute_module()` always calls `load_fixtures()`. Never set mock return values inside a test method — they will be overwritten by the next `execute_module` call. Use the `filename` parameter to vary the fixture:

```python
def load_fixtures(self, commands=None, filename=None):
    if filename == "empty":
        self.run_commands.return_value = [EMPTY_OUTPUT]
    else:
        self.run_commands.return_value = [DEFAULT_OUTPUT]
```

Then call: `self.execute_module(changed=True, commands=commands, filename="empty")`

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

