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
import json

from unittest.mock import patch

from ansible.module_utils.connection import ConnectionError

from ansible_collections.vyos.vyos.plugins.modules import vyos_facts
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosFactsModule(TestVyosModule):
    module = vyos_facts

    def setUp(self):
        super(TestVyosFactsModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.legacy.base.run_commands",
        )
        self.run_commands = self.mock_run_commands.start()

        self.mock_get_connection = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.legacy.base.get_connection",
        )
        self.get_connection = self.mock_get_connection.start()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        # command outputs a test sets directly, instead of a fixture file
        self.outputs = {}

        self.mock_get_capabilities = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.legacy.base.get_capabilities",
        )
        self.get_capabilities = self.mock_get_capabilities.start()
        self.get_capabilities.return_value = {
            "device_info": {
                "network_os": "vyos",
                "network_os_hostname": "vyos01",
                "network_os_model": "VMware",
                "network_os_version": "VyOS 1.1.7",
                "network_os_major_version": "1.1",
            },
            "network_api": "cliconf",
        }

    def tearDown(self):
        super(TestVyosFactsModule, self).tearDown()
        self.mock_run_commands.stop()
        self.mock_get_connection.stop()
        self.mock_get_capabilities.stop()
        self.mock_get_resource_connection.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            module, commands = args
            output = list()
            for item in commands:
                try:
                    obj = json.loads(item)
                    command = obj["command"]
                except ValueError:
                    command = item
                if command in self.outputs:
                    if isinstance(self.outputs[command], Exception):
                        raise self.outputs[command]
                    output.append(self.outputs[command])
                    continue
                filename = str(command).replace(" ", "_")
                output.append(load_fixture(filename))
            return output

        self.run_commands.side_effect = load_from_file
        self.get_connection.return_value.run_commands.side_effect = (
            lambda commands, **kwargs: load_from_file(None, commands)
        )

    def test_vyos_facts_default(self):
        set_module_args(dict(gather_subset="default"))
        result = self.execute_module()
        facts = result.get("ansible_facts")
        self.assertEqual(len(facts), 11)
        self.assertEqual(facts["ansible_net_hostname"].strip(), "vyos01")
        self.assertEqual(facts["ansible_net_version"], "VyOS 1.1.7")

    def test_vyos_facts_not_all(self):
        set_module_args(dict(gather_subset="!all"))
        result = self.execute_module()
        facts = result.get("ansible_facts")
        self.assertEqual(len(facts), 11)
        self.assertEqual(facts["ansible_net_hostname"].strip(), "vyos01")
        self.assertEqual(facts["ansible_net_version"], "VyOS 1.1.7")

    def test_vyos_facts_exclude_most(self):
        set_module_args(dict(gather_subset=["!neighbors", "!config"]))
        result = self.execute_module()
        facts = result.get("ansible_facts")
        self.assertEqual(len(facts), 11)
        self.assertEqual(facts["ansible_net_hostname"].strip(), "vyos01")
        self.assertEqual(facts["ansible_net_version"], "VyOS 1.1.7")

    def test_vyos_facts_invalid_subset(self):
        set_module_args(dict(gather_subset="cereal"))
        self.execute_module(failed=True)

    def test_vyos_facts_secure_boot_legacy_bios(self):
        # real output of a rolling image booted with legacy BIOS (fixture show_secure-boot)
        set_module_args(dict(gather_subset="default"))
        facts = self.execute_module()["ansible_facts"]
        self.assertEqual(facts["ansible_net_secure_boot"], {"enabled": False, "uefi": False})

    def test_vyos_facts_secure_boot_uefi_disabled(self):
        # real output of a rolling image booted with UEFI, Secure Boot off
        self.outputs = {"show secure-boot": "SecureBoot disabled"}
        set_module_args(dict(gather_subset="default"))
        facts = self.execute_module()["ansible_facts"]
        self.assertEqual(facts["ansible_net_secure_boot"], {"enabled": False, "uefi": True})

    def test_vyos_facts_secure_boot_enabled(self):
        # format of the op-mode script (secure_boot.py); placeholder certificate names
        self.outputs = {
            "show secure-boot": "SecureBoot enabled",
            "show secure-boot detail": "Issuer:  /CN=VyOS Networks Secure Boot CA\n"
            "Subject: /CN=VyOS Networks Secure Boot Signer 2025 - linux",
        }
        set_module_args(dict(gather_subset="default"))
        facts = self.execute_module()["ansible_facts"]
        self.assertEqual(
            facts["ansible_net_secure_boot"],
            {
                "enabled": True,
                "uefi": True,
                "certificates": [
                    {
                        "issuer": "/CN=VyOS Networks Secure Boot CA",
                        "subject": "/CN=VyOS Networks Secure Boot Signer 2025 - linux",
                    },
                ],
            },
        )

    def test_vyos_facts_secure_boot_not_supported(self):
        # images without the command (1.5.1 and older): no fact, and no failure
        self.outputs = {"show secure-boot": ConnectionError("Invalid command: show [secure-boot]")}
        set_module_args(dict(gather_subset="default"))
        facts = self.execute_module()["ansible_facts"]
        self.assertNotIn("ansible_net_secure_boot", facts)
        self.assertEqual(len(facts), 10)

    def test_vyos_facts_secure_boot_connection_error(self):
        # a connection problem is not "command not supported": the module fails
        self.outputs = {"show secure-boot": ConnectionError("timeout value 30 seconds reached")}
        set_module_args(dict(gather_subset="default"))
        result = self.execute_module(failed=True)
        self.assertIn("timeout value 30 seconds reached", result["msg"])
