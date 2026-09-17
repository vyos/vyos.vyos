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

    def test_vyos_config_match_enforce(self):
        lines = [
            "set interfaces ethernet eth0 address '1.2.3.4/24'",
            "set interfaces ethernet eth0 description 'test string'",
        ]
        set_module_args(dict(lines=lines, match="enforce"))
        candidate = "\n".join(lines)

        response = self.cliconf_obj.get_diff(
            candidate,
            self.running_config,
            diff_match="enforce",
        )

        self.conn.get_diff = MagicMock(return_value=response)
        result = self.execute_module(changed=True, sort=False)

        self.conn.get_diff.assert_called_once_with(
            candidate=candidate,
            running=self.running_config,
            diff_match="enforce",
        )

        expected_config_diff = [
            "delete interfaces ethernet eth1",
        ]
        self.assertEqual(response["config_diff"], expected_config_diff)

        expected_commands = expected_config_diff
        self.assertEqual(result["commands"], expected_commands)

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

    def test_vyos_config_match_enforce_blank_lines(self):
        """enforce diff must not raise IndexError on blank lines in running config."""
        running_with_blanks = self.running_config + "\n\n"
        candidate = "set interfaces ethernet eth0 address 1.2.3.4/24"
        response = self.cliconf_obj.get_diff(candidate, running_with_blanks, diff_match="enforce")
        self.assertIn("config_diff", response)

    def test_vyos_config_match_enforce_additions(self):
        lines = [
            "set interfaces ethernet eth0 address '1.2.3.4/24'",
            "set interfaces ethernet eth0 description 'test string'",
            "set interfaces ethernet eth2 address '192.0.2.1/24'",
        ]
        set_module_args(dict(lines=lines, match="enforce"))
        candidate = "\n".join(lines)
        response = self.cliconf_obj.get_diff(
            candidate,
            self.running_config,
            diff_match="enforce",
        )
        self.conn.get_diff = MagicMock(return_value=response)
        result = self.execute_module(changed=True, sort=False)
        self.conn.get_diff.assert_called_once_with(
            candidate=candidate,
            running=self.running_config,
            diff_match="enforce",
        )
        self.assertIn(
            "set interfaces ethernet eth2 address 192.0.2.1/24",
            response["config_diff"],
        )
        self.assertEqual(result["commands"], response["config_diff"])

    def test_vyos_config_match_enforce_rejects_delete_lines(self):
        """
        match=enforce treats the candidate as the complete desired end-state.
        A candidate containing 'delete' lines must be rejected rather than
        silently producing a diff that removes most/all of the running
        config (regression test for a candidate that is a no-op/delete-only
        input generating deletes for everything the candidate omits).
        """
        lines = ["delete interfaces ethernet eth0 address"]
        candidate = "\n".join(lines)

        with self.assertRaises(ValueError):
            self.cliconf_obj.get_diff(
                candidate,
                self.running_config,
                diff_match="enforce",
            )

    def test_vyos_config_match_enforce_rejects_empty_candidate(self):
        """
        A candidate that is empty, whitespace-only, or comment-only must be
        rejected rather than silently treated as an empty desired end-state
        (which would generate deletes for the entire running config).
        Comment-only candidates are also stripped away entirely by upstream
        NetworkConfig parsing before reaching VyosConf, so this is a second,
        distinct route to the same mass-deletion failure mode as the
        'delete' lines case above.
        """
        for candidate in ("", "   ", "# just a comment"):
            with self.assertRaises(ValueError):
                self.cliconf_obj.get_diff(
                    candidate,
                    self.running_config,
                    diff_match="enforce",
                )

    def test_vyos_config_match_enforce_requires_running(self):
        """
        diff_match=enforce with running=None must raise a clear ValueError
        instead of falling through to an AttributeError on
        running.splitlines().
        """
        with self.assertRaises(ValueError):
            self.cliconf_obj.get_diff(
                "set system host-name foo",
                None,
                diff_match="enforce",
            )

    def test_vyos_config_match_enforce_ignores_comment_lines(self):
        """
        Comment lines mixed in with 'set' lines must be stripped out rather
        than causing the whole candidate to be rejected as not starting
        with 'set'.
        """
        candidate = "\n".join(
            [
                "set interfaces ethernet eth0 address '1.2.3.4/24'",
                "# a note about this interface",
                "set interfaces ethernet eth0 description 'test string'",
            ],
        )
        running = "set interfaces ethernet eth0 address '1.2.3.4/24'"
        response = self.cliconf_obj.get_diff(
            candidate,
            running,
            diff_match="enforce",
        )
        self.assertIn(
            "set interfaces ethernet eth0 description 'test string'",
            response["config_diff"],
        )

    def test_sanitize_config_filters_password_delete_lines(self):
        """
        sanitize_config()/PASSWORD_NEEDLE must filter 'delete ... password'
        lines the same way it filters 'set ... password' lines, since
        match=enforce can generate deletes for password config the candidate
        omits. Without this, allow_password_change=none/plaintext/encrypted
        would fail to catch a password-affecting delete.
        """
        result = {}
        commands = [
            "set system host-name foo",
            "delete system login user admin authentication encrypted-password",
            "set system login user admin authentication plaintext-password 'secret'",
        ]
        vyos_config.sanitize_config(commands, result, allow="none")
        self.assertIn(
            "delete system login user admin authentication encrypted-password",
            result["filtered"],
        )
        self.assertIn(
            "set system login user admin authentication plaintext-password 'secret'",
            result["filtered"],
        )
        self.assertNotIn("set system host-name foo", result["filtered"])

    def test_vyos_config_match_enforce_refuses_ssh_deletion(self):
        """
        match=enforce must refuse to generate 'delete service ssh ...'
        commands, since this could sever the management connection.
        Regression test for the incident where an enforce candidate that
        didn't restate 'service ssh' generated a delete for it.
        """
        running = "\n".join(
            [
                "set service ssh port '22'",
                "set service lldp",
            ],
        )
        candidate = "set service lldp"

        with self.assertRaises(ValueError):
            self.cliconf_obj.get_diff(
                candidate,
                running,
                diff_match="enforce",
            )

    def test_vyos_config_confirm_defaults_to_automatic_for_match_enforce(self):
        """
        confirm defaults to 'automatic' when match=enforce and confirm is
        not explicitly set, since enforce can generate broad deletes and a
        bad commit should self-revert rather than leave the device
        unreachable.
        """
        lines = [
            "set interfaces ethernet eth0 address '1.2.3.4/24'",
            "set interfaces ethernet eth0 description 'test string'",
        ]
        set_module_args(dict(lines=lines, match="enforce"))
        candidate = "\n".join(lines)
        response = self.cliconf_obj.get_diff(
            candidate,
            self.running_config,
            diff_match="enforce",
        )
        self.conn.get_diff = MagicMock(return_value=response)

        self.execute_module(changed=True, sort=False)

        self.assertEqual(self.load_config.call_args[1]["confirm"], 10)
        self.run_commands.assert_called_once()
        self.assertEqual(
            ["configure", "confirm", "exit"],
            self.run_commands.call_args[0][1],
        )

    def test_vyos_config_confirm_stays_none_for_other_match_values(self):
        """
        confirm stays 'none' (no confirm kwarg passed, no auto-confirm
        run_commands call) when match is not 'enforce' and confirm is not
        explicitly set -- the new conditional default must not change
        existing behaviour for match=line/none.
        """
        lines = ["set system host-name foo"]
        set_module_args(dict(lines=lines))
        candidate = "\n".join(lines)
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )

        self.execute_module(changed=True, commands=lines)

        self.assertIsNone(self.load_config.call_args[1]["confirm"])
        self.run_commands.assert_not_called()

    def test_vyos_config_match_enforce_rejects_comment_disguised_as_command(self):
        """
        A line like 'set # comment' has 3 raw tokens (passing a naive
        token-count check) but parse_line() strips the trailing comment,
        leaving no actual path/leaf. This must still be rejected rather
        than silently contributing an empty/degenerate entry to the diff.
        """
        for bad_line in ("set # comment", "set foo # comment"):
            candidate = "\n".join(["set system host-name foo", bad_line])
            with self.assertRaises(ValueError):
                self.cliconf_obj.get_diff(
                    candidate,
                    self.running_config,
                    diff_match="enforce",
                )

    def test_sanitize_config_filters_collapsed_login_subtree_deletes(self):
        """
        match=enforce's scoping can collapse an untouched subtree into a
        single parent delete (e.g. 'delete system login' when a candidate
        touches system without restating login, rather than an itemized
        per-field delete). PASSWORD_NEEDLE alone can't see into a collapsed
        delete to know it removes a password -- it must be treated as
        password-bearing by default under any restrictive
        allow_password_change value.
        """
        result = {}
        commands = [
            "set system host-name foo",
            "delete system login",
        ]
        vyos_config.sanitize_config(commands, result, allow="none")
        self.assertIn("delete system login", result["filtered"])
        self.assertNotIn("set system host-name foo", result["filtered"])

    def test_sanitize_config_filters_collapsed_login_user_subtree_delete(self):
        """
        Same collapse risk at the per-user level: 'delete system login
        user admin' (no specific authentication line) must also be
        treated as password-bearing.
        """
        result = {}
        commands = [
            "set system host-name foo",
            "delete system login user admin",
        ]
        vyos_config.sanitize_config(commands, result, allow="none")
        self.assertIn("delete system login user admin", result["filtered"])

    def test_sanitize_config_allows_collapsed_login_subtree_delete_when_all(self):
        """
        allow_password_change=all must still let a collapsed login-subtree
        delete through, same as it already does for explicit password
        lines.
        """
        result = {}
        commands = [
            "set system host-name foo",
            "delete system login",
        ]
        vyos_config.sanitize_config(commands, result, allow="all")
        self.assertEqual(result["filtered"], [])

    def test_vyos_config_match_enforce_accepts_bracket_format_src(self):
        """
        match=enforce must accept bracket-format candidates the same way
        match=line/none already do -- enforce_candidate_lines is now built
        from the same shared, correctly-normalized candidate_commands
        rather than parsing raw candidate text independently (which had no
        concept of bracket format at all).
        """
        candidate = "system {\n    host-name foo\n}\n"
        response = self.cliconf_obj.get_diff(
            candidate,
            self.running_config,
            diff_match="enforce",
        )
        self.assertIn("set system host-name foo", response["config_diff"])

    def test_vyos_config_match_line_ignores_comment_and_blank_lines(self):
        """
        A src/lines candidate containing comment or blank lines must not
        raise under match=line -- these are stripped during candidate
        normalization the same way match=enforce already does, rather than
        hitting the 'line must start with set or delete' check.
        """
        lines = [
            "# a note",
            "",
            "set system host-name foo",
        ]
        set_module_args(dict(lines=lines))
        candidate = "\n".join(lines)
        self.conn.get_diff = MagicMock(
            return_value=self.cliconf_obj.get_diff(candidate, self.running_config),
        )
        self.execute_module(changed=True, commands=["set system host-name foo"])

    def test_sanitize_config_filters_collapsed_login_user_authentication_subtree_delete(self):
        """
        A candidate that keeps other settings for a user but omits that
        user's entire authentication subtree collapses to 'delete system
        login user <name> authentication' -- one level deeper than the
        per-user collapse already covered. This must also be treated as
        password-bearing under the default allow_password_change=plaintext,
        not just under allow_password_change=none.
        """
        result = {}
        commands = [
            "set system host-name foo",
            "delete system login user admin authentication",
        ]
        vyos_config.sanitize_config(commands, result, allow="plaintext")
        self.assertIn(
            "delete system login user admin authentication",
            result["filtered"],
        )
        self.assertNotIn("set system host-name foo", result["filtered"])

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
