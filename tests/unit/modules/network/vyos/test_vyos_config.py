#
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

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import MagicMock, patch

from ansible_collections.vyos.vyos.plugins.cliconf.vyos import Cliconf
from ansible_collections.vyos.vyos.plugins.modules import vyos_config
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosConfigModule(TestVyosModule):
    module = vyos_config

    def setUp(self):
        super(TestVyosConfigModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_run_commands = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_config.run_commands",
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_get_connection = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_config.get_connection",
        )
        self.get_connection = self.mock_get_connection.start()

        self.cliconf_obj = Cliconf(MagicMock())
        self.running_config = load_fixture("vyos_config_config.cfg")

        self.conn = self.get_connection()
        self.conn.edit_config = MagicMock()
        self.running_config = load_fixture("vyos_config_config.cfg")

    def tearDown(self):
        super(TestVyosConfigModule, self).tearDown()

        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_run_commands.stop()
        self.mock_get_connection.stop()

    def load_fixtures(self, commands=None, filename=None):
        config_file = "vyos_config_config.cfg"
        self.get_config.return_value = load_fixture(config_file)
        self.load_config.return_value = None

    def test_vyos_config_unchanged(self):
        src = load_fixture("vyos_config_config.cfg")
        self.conn.get_diff = MagicMock(return_value=self.cliconf_obj.get_diff(src, src))
        set_module_args(dict(src=src))
        self.execute_module()

    def test_vyos_config_src(self):
        src = load_fixture("vyos_config_src.cfg")
        set_module_args(dict(src=src))
        candidate = "\n".join(self.module.format_commands(src.splitlines()))
        commands = [
            "set system host-name foo",
            "delete interfaces ethernet eth0 address",
        ]
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )
        self.execute_module(changed=True, commands=commands)

    def test_vyos_config_src_brackets(self):
        src = load_fixture("vyos_config_src_brackets.cfg")
        set_module_args(dict(src=src))
        commands = [
            "set interfaces ethernet eth0 address 10.10.10.10/24",
            "set policy route testroute rule 1 set table 10",
            "set system host-name foo",
        ]
        self.conn.get_diff = MagicMock(side_effect=self.cliconf_obj.get_diff)
        self.execute_module(changed=True, commands=commands)

    def test_vyos_config_backup(self):
        set_module_args(dict(backup=True))
        result = self.execute_module()
        self.assertIn("__backup__", result)

    def test_vyos_config_lines(self):
        commands = ["set system host-name foo"]
        set_module_args(dict(lines=commands))
        candidate = "\n".join(commands)
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )
        self.execute_module(changed=True, commands=commands)

    def test_vyos_config_config(self):
        config = "set system host-name localhost"
        new_config = ["set system host-name router"]
        set_module_args(dict(lines=new_config, config=config))
        candidate = "\n".join(new_config)
        self.conn.get_diff = MagicMock(return_value=self.cliconf_obj.get_diff(candidate, config))
        self.execute_module(changed=True, commands=new_config)

    def test_vyos_config_match_none(self):
        lines = [
            "set system interfaces ethernet eth0 address 1.2.3.4/24",
            "set system interfaces ethernet eth0 description test string",
        ]
        set_module_args(dict(lines=lines, match="none"))
        candidate = "\n".join(lines)
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, None, diff_match="none"),
        )
        self.execute_module(changed=True, commands=lines, sort=False)

    def test_vyos_config_confirm_automatic(self):
        src = load_fixture("vyos_config_src.cfg")
        confirm_timeout = 7
        set_module_args(dict(src=src, confirm="automatic", confirm_timeout=confirm_timeout))
        candidate = "\n".join(self.module.format_commands(src.splitlines()))
        commands = [
            "set system host-name foo",
            "delete interfaces ethernet eth0 address",
        ]
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )

        self.execute_module(changed=True, commands=commands)

        self.assertEqual(self.load_config.call_args[1]["confirm"], confirm_timeout)
        self.run_commands.assert_called_once()
        self.assertEqual(
            ["configure", "confirm", "exit"],
            self.run_commands.call_args[0][1],
        )

    def test_vyos_config_confirm_manual(self):
        lines = [
            "set system host-name foo",
        ]
        confirm_timeout = 12
        set_module_args(dict(lines=lines, confirm="manual", confirm_timeout=confirm_timeout))
        candidate = "\n".join(lines)
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )

        self.execute_module(changed=True, commands=lines)

        self.assertEqual(self.load_config.call_args[1]["confirm"], confirm_timeout)
        self.run_commands.assert_not_called()

    def test_vyos_config_replace_leaf_change(self):
        """replace=True with a full candidate: a changed scalar value gets an
        explicit delete-then-set pair.

        Earlier design suppressed the delete here based on observed
        cardinality (1 running value, 1 candidate value -> assumed unique
        scalar). That heuristic was unsound: it can't distinguish a
        genuinely scalar attribute from a list-style attribute that merely
        has one value right now (see test_vyos_config_replace_list_value_change
        below for the failure case this caused). Deleting unconditionally,
        ordered before the corresponding set, is correct for both cases and
        carries no risk of the delete clobbering the just-applied set, since
        the delete always runs first, while its target value is still active.
        """
        running_hierarchical = "\n".join(
            [
                "system {",
                "    host-name router",
                "    domain-name example.com",
                "}",
            ],
        )
        candidate = "\n".join(
            [
                "set system host-name 'foo'",
                "set system domain-name 'example.com'",
            ],
        )
        diff = self.cliconf_obj.get_diff(candidate, running_hierarchical, diff_replace=True)
        assert diff["config_diff"] == [
            "delete system host-name router",
            "set system host-name 'foo'",
        ]

    def test_vyos_config_replace_list_value_change(self):
        """replace=True: a list-style attribute with one value changing to a
        different single value must not retain the old value alongside the
        new one. Regression guard for a real bug: a cardinality-based
        heuristic previously mistook this for a scalar attribute update and
        suppressed the delete, leaving both values configured.
        """
        running_hierarchical = "system {\n    name-server 8.8.8.8\n}\n"
        candidate = "set system name-server 8.8.4.4"
        diff = self.cliconf_obj.get_diff(candidate, running_hierarchical, diff_replace=True)
        assert diff["config_diff"] == [
            "delete system name-server 8.8.8.8",
            "set system name-server 8.8.4.4",
        ]

    def test_vyos_config_replace_removes_missing_leaf(self):
        """replace=True: a leaf present on router but absent from candidate gets deleted."""
        running_hierarchical = "\n".join(
            [
                "system {",
                "    host-name router",
                "}",
                "interfaces {",
                "    ethernet eth1 {",
                "        address 6.7.8.9/24",
                '        description "test string"',
                "    }",
                "}",
            ],
        )
        candidate = "\n".join(
            [
                "set system host-name router",
                "set interfaces ethernet eth1 address '6.7.8.9/24'",
            ],
        )
        diff = self.cliconf_obj.get_diff(candidate, running_hierarchical, diff_replace=True)
        assert "delete interfaces ethernet eth1 description" in " ".join(diff["config_diff"])

    def test_vyos_config_replace_does_not_affect_default_match(self):
        """Regression guard: replace=False must produce byte-identical diff to pre-PR behavior."""
        src = load_fixture("vyos_config_src.cfg")
        candidate = "\n".join(self.module.format_commands(src.splitlines()))
        diff_default = self.cliconf_obj.get_diff(candidate, self.running_config)
        diff_explicit_false = self.cliconf_obj.get_diff(
            candidate,
            self.running_config,
            diff_replace=False,
        )
        assert diff_default == diff_explicit_false

    def test_vyos_config_replace_quoted_value_not_falsely_flagged(self):
        """Double-quote-insensitive matching must stay scoped to replace mode.

        Single quotes are already stripped unconditionally on both sides before
        this comparison, so they can't distinguish the two code paths. Double
        quotes are the actual difference: match_cmd() (used only when
        diff_replace=True) strips them too, while the default exact-match path
        does not. This locks in that the default path still treats a
        double-quoted running value as distinct from an unquoted candidate value,
        while replace mode (which requires hierarchical running) correctly
        treats them as the same value.
        """
        candidate = "set system host-name foo"

        running_flat = 'set system host-name "foo"'
        diff_default = self.cliconf_obj.get_diff(candidate, running_flat)
        assert diff_default["config_diff"] == ["set system host-name foo"]

        running_hierarchical = 'system {\n    host-name "foo"\n}\n'
        diff_replace = self.cliconf_obj.get_diff(
            candidate,
            running_hierarchical,
            diff_replace=True,
        )
        assert diff_replace["config_diff"] == []

    def test_vyos_config_replace_removes_orphaned_node(self):
        """A rule entirely removed from candidate must not leave an empty stub node."""
        running_hierarchical = "\n".join(
            [
                "firewall {",
                "    ipv4 {",
                "        name example {",
                "            rule 100 {",
                "                action drop",
                "            }",
                "            rule 200 {",
                "                action accept",
                "            }",
                "        }",
                "    }",
                "}",
            ],
        )
        candidate = "set firewall ipv4 name example rule 100 action 'drop'"
        diff = self.cliconf_obj.get_diff(candidate, running_hierarchical, diff_replace=True)
        commands = diff["config_diff"]
        # must delete the whole rule node, not just its leaf
        assert "delete firewall ipv4 name example rule 200" in commands
        assert commands.count("delete firewall ipv4 name example rule 200") == 1
        assert not any(
            "action" in c and "rule 200" in c for c in commands if c.startswith("delete")
        )

    def test_vyos_config_replace_explicit_delete_line_not_treated_as_present(self):
        """replace=True: an explicit delete line for a node must not fool the
        tree-diff into thinking that node is still 'present' in the desired
        state.

        Regression guard for a real bug: candidate_bodies previously included
        stripped bodies from delete lines too, so a candidate containing
        `delete firewall ipv4 name example rule 200` (while otherwise valid,
        e.g. with other unrelated set lines making up the rest of a full
        candidate) made _candidate_has_prefix() think that path "existed",
        suppressing the clean whole-node delete and instead deleting rule
        200's children one at a time -- the same empty-stub orphan pattern
        this whole diff_replace rewrite exists to fix, just reached via an
        explicit delete line instead of omission.
        """
        running_hierarchical = "\n".join(
            [
                "firewall {",
                "    ipv4 {",
                "        name example {",
                "            rule 100 {",
                "                action drop",
                "            }",
                "            rule 200 {",
                "                action accept",
                "                description example",
                "            }",
                "        }",
                "    }",
                "}",
                "system {",
                "    host-name router",
                "}",
            ],
        )
        candidate = "\n".join(
            [
                "set firewall ipv4 name example rule 100 action drop",
                "delete firewall ipv4 name example rule 200",
                "set system host-name router",
            ],
        )
        diff = self.cliconf_obj.get_diff(candidate, running_hierarchical, diff_replace=True)
        commands = diff["config_diff"]

        # the whole node must be deleted as a single unit, not per-leaf
        assert "delete firewall ipv4 name example rule 200" in commands
        assert not any(
            "action" in c and "rule 200" in c for c in commands if c.startswith("delete")
        )
        assert not any(
            "description" in c and "rule 200" in c for c in commands if c.startswith("delete")
        )

        # unrelated paths present in the full candidate must be untouched
        assert not any("rule 100" in c and c.startswith("delete") for c in commands)
        assert not any("host-name" in c and c.startswith("delete") for c in commands)

        # must not have wrongly deleted the entire firewall subtree
        assert "delete firewall" not in commands

    def test_vyos_config_replace_requests_hierarchical_config(self):
        """replace=True must request get_config(module, format='text') so
        get_diff() receives hierarchical running config, not flat set-lines.

        Regression guard for the module-side wiring: all the other
        replace-mode tests call Cliconf.get_diff() directly and never
        exercise run()'s own get_config() call, so a future change to that
        call site (e.g. dropping the format="text" argument) would go
        completely undetected by the rest of the suite.
        """
        lines = ["set system host-name foo"]
        set_module_args(dict(lines=lines, replace=True))
        self.conn.get_diff = MagicMock(return_value={"config_diff": lines})

        self.execute_module(changed=True, commands=lines)

        assert self.get_config.call_args.kwargs.get("format") == "text"
