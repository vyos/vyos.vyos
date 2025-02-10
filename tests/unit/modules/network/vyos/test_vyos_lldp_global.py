# (c) 2021 Red Hat Inc.
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

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_lldp_global
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosLLDPModule(TestVyosModule):
    module = vyos_lldp_global

    def setUp(self):
        super(TestVyosLLDPModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_get_config = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.lldp_global.lldp_global.Lldp_globalFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestVyosLLDPModule, self).tearDown()

        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()

    def load_fixtures(self, commands=None, filename=None):
        self.get_config.return_value = load_fixture("vyos_lldp_global_config.cfg")

    def test_vyos_lldp_global_merge_enabled(self):
        set_module_args(dict(config=dict(enable=True)))
        self.execute_module(changed=False)

    def test_vyos_lldp_global_merge_disabled(self):
        set_module_args(dict(config=dict(enable=False)))
        self.execute_module(changed=True, commands=["delete service lldp"])

    def test_vyos_lldp_global_merge_addresses(self):
        set_module_args(
            dict(
                config=dict(
                    enable=True,
                    addresses=["192.0.0.1"],
                ),
            ),
        )
        self.execute_module(
            changed=True,
            commands=["set service lldp management-address '192.0.0.1'"],
        )

    def test_vyos_lldp_global_replace_addresses(self):
        set_module_args(
            dict(
                config=dict(
                    enable=True,
                    addresses=["192.0.0.1"],
                    legacy_protocols=["cdp", "fdp"],
                ),
                state="replaced",
            ),
        )
        commands = [
            "set service lldp management-address '192.0.0.1'",
            "delete service lldp management-address '192.0.2.14'",
            "delete service lldp management-address 'ff00::1'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_global_replace_protocols(self):
        set_module_args(
            dict(
                config=dict(
                    enable=True,
                    addresses=["192.0.2.14", "ff00::1"],
                    legacy_protocols=["cdp"],
                ),
                state="replaced",
            ),
        )
        commands = [
            "delete service lldp legacy-protocols 'fdp'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_global_replace_address(self):
        set_module_args(
            dict(
                config=dict(
                    enable=True,
                    address="192.0.0.1",
                    legacy_protocols=["cdp", "fdp"],
                ),
                state="replaced",
            ),
        )
        commands = [
            "set service lldp management-address '192.0.0.1'",
            "delete service lldp management-address '192.0.2.14'",
            "delete service lldp management-address 'ff00::1'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_global_delete_all(self):
        set_module_args(dict(config=dict(), state="deleted"))
        self.execute_module(changed=True, commands=["delete service lldp"])
