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

        self.mock_copy_file = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_config.copy_file",
        )
        self.copy_file = self.mock_copy_file.start()

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
        self.mock_copy_file.stop()

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

    # -- replace=config (T6837, cisco.iosxr.iosxr_config replace=config analogue) --

    def test_vyos_config_replace_config_requires_src(self):
        """replace=config without src must fail argument validation, not run."""
        set_module_args(dict(replace="config"))
        result = self.execute_module(failed=True)
        self.assertIn("src", result["msg"])

    def test_vyos_config_replace_config_rejects_lines_only(self):
        """replace=config with only lines (no src) must fail --
        required_if demands src regardless of what else is set.
        """
        set_module_args(dict(replace="config", lines=["set system host-name foo"]))
        self.execute_module(failed=True)

    def test_vyos_config_replace_config_rejects_lines_and_src_together(self):
        """lines/src remain mutually exclusive regardless of replace --
        this is the pre-existing constraint, unaffected by replace=config."""
        set_module_args(
            dict(
                replace="config",
                src="system {\n    host-name router\n}\n",
                lines=["set system host-name foo"],
            ),
        )
        self.execute_module(failed=True)

    def test_vyos_config_replace_config_pushes_and_loads(self):
        """replace=config with a real change: copies the candidate to a fixed
        remote path, issues a single `load <path>` command, and reports the
        device's own diff verbatim -- not an itemized set/delete list.
        """
        src = "interfaces {\n    ethernet eth0 {\n        address dhcp\n    }\n}\n"
        set_module_args(dict(replace="config", src=src))
        self.load_config.side_effect = lambda *a, **kw: (
            "[edit interfaces]\n+ethernet eth0 {\n+    address dhcp\n+}"
        )

        result = self.execute_module(changed=True)

        self.assertEqual(result["commands"], ["load /tmp/ansible_vyos_replace.cfg"])
        self.copy_file.assert_called_once()
        # positional call: copy_file(module, local_path, remote_path, proto)
        self.assertEqual(self.copy_file.call_args[0][2], "/tmp/ansible_vyos_replace.cfg")
        self.assertEqual(self.copy_file.call_args[0][3], "scp")
        self.assertEqual(
            self.load_config.call_args[0][1],
            ["load /tmp/ansible_vyos_replace.cfg"],
        )

    def test_vyos_config_replace_config_noop(self):
        """replace=config with load_config() returning falsy (VyOS's own
        `compare` reported no changes) must report changed=False, not
        unconditionally True.
        """
        src = "system {\n    host-name router\n}\n"
        set_module_args(dict(replace="config", src=src))
        self.load_config.return_value = None

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], ["load /tmp/ansible_vyos_replace.cfg"])

    def test_vyos_config_replace_config_check_mode(self):
        """Under check_mode, commit=False must be passed through to
        load_config() -- the candidate is still copied/loaded for an accurate
        compare-based preview diff, but nothing is committed.
        """
        src = "system {\n    host-name router\n}\n"
        set_module_args(dict(replace="config", src=src, _ansible_check_mode=True))
        self.load_config.side_effect = lambda *a, **kw: (
            "[edit system]\n-host-name foo\n+host-name router"
        )

        self.execute_module(changed=True)

        self.assertEqual(self.load_config.call_args[1]["commit"], False)

    def test_vyos_config_replace_config_confirm_automatic(self):
        src = "system {\n    host-name router\n}\n"
        confirm_timeout = 9
        set_module_args(
            dict(
                replace="config",
                src=src,
                confirm="automatic",
                confirm_timeout=confirm_timeout,
            ),
        )
        self.load_config.side_effect = lambda *a, **kw: (
            "[edit system]\n-host-name foo\n+host-name router"
        )

        self.execute_module(changed=True)

        self.assertEqual(self.load_config.call_args[1]["confirm"], confirm_timeout)
        self.run_commands.assert_called_once()
        self.assertEqual(["configure", "confirm", "exit"], self.run_commands.call_args[0][1])

    def test_vyos_config_replace_config_diff(self):
        """With --diff, result['diff']['prepared'] must carry VyOS's own
        compare() output verbatim -- not an itemized command list, since none
        is computed in this mode.
        """
        src = "system {\n    host-name router\n}\n"
        set_module_args(dict(replace="config", src=src, _ansible_diff=True))
        raw_compare = "[edit system]\n-host-name foo\n+host-name router"
        self.load_config.side_effect = lambda *a, **kw: raw_compare

        result = self.execute_module(changed=True)

        self.assertEqual(result["diff"]["prepared"], raw_compare)

    def test_vyos_config_replace_config_does_not_use_line_diff_path(self):
        """replace=config must never call connection.get_diff() -- that path
        (and match/allow_password_change) is specific to replace=line and is
        documented as ignored under replace=config.
        """
        src = "system {\n    host-name router\n}\n"
        set_module_args(dict(replace="config", src=src, match="none"))
        self.load_config.side_effect = lambda *a, **kw: (
            "[edit system]\n-host-name foo\n+host-name router"
        )

        self.execute_module(changed=True)

        self.conn.get_diff.assert_not_called()

    def test_vyos_config_replace_config_confirm_automatic_check_mode_no_confirm_sent(self):
        """Regression guard: confirm=automatic must not send the
        configure/confirm/exit sequence under check_mode, even when a real
        diff is present -- nothing was actually committed to confirm.
        """
        src = "system {\n    host-name router\n}\n"
        set_module_args(
            dict(
                replace="config",
                src=src,
                confirm="automatic",
                _ansible_check_mode=True,
            ),
        )
        self.load_config.side_effect = lambda *a, **kw: (
            "[edit system]\n-host-name foo\n+host-name router"
        )

        self.execute_module(changed=True)

        self.run_commands.assert_not_called()

    def test_vyos_config_replace_config_confirm_automatic_noop_no_confirm_sent(self):
        """Regression guard: confirm=automatic must not send the
        configure/confirm/exit sequence when load_config() reports no diff
        (VyOS's own compare() found nothing to commit) -- there is nothing
        pending to confirm.
        """
        src = "system {\n    host-name router\n}\n"
        set_module_args(dict(replace="config", src=src, confirm="automatic"))
        self.load_config.return_value = None

        self.execute_module(changed=False)

        self.run_commands.assert_not_called()

    def test_vyos_config_replace_line_default_unaffected(self):
        """Regression guard: default replace='line' must behave identically
        to the pre-patch module -- copy_file() must never be invoked.
        """
        commands = ["set system host-name foo"]
        set_module_args(dict(lines=commands))
        candidate = "\n".join(commands)
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )
        self.execute_module(changed=True, commands=commands)
        self.copy_file.assert_not_called()
