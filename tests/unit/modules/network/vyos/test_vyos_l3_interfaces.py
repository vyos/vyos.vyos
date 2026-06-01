# (c) 2024 VyOS Networks <maintainers@vyos.net>
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

    def tearDown(self):
        super(TestVyosL3InterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()

    def load_fixtures(self, commands=None, filename=None):
        fixture_data = load_fixture("vyos_l3_interfaces_config.cfg")
        self.get_resource_connection_facts.return_value.get_config.return_value = fixture_data

    def test_vyos_l3_interfaces_merged(self):
        """Merge a new IPv4 address onto eth1 (currently has 192.0.2.14/24)."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv4=[dict(address="192.0.2.1/24")],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set interfaces ethernet eth1 address '192.0.2.1/24'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_merged_idempotent(self):
        """No change when desired config already matches existing config."""
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
        """Merge a new IPv6 address onto eth1."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv6=[dict(address="2001:db8::1/32")],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set interfaces ethernet eth1 address '2001:db8::1/32'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_replaced(self):
        """Replace eth1 addresses: remove existing, add new."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ipv4=[dict(address="10.0.0.1/24")],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "delete interfaces ethernet eth1 address '192.0.2.14/24'",
            "set interfaces ethernet eth1 address '10.0.0.1/24'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_overridden(self):
        """Override: keep only eth2, delete all other interface addresses."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth2",
                        ipv4=[dict(address="192.0.2.10/24")],
                        ipv6=[dict(address="2001:db8::10/32")],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "delete interfaces ethernet eth0",
            "delete interfaces ethernet eth1",
            "delete interfaces ethernet eth3",
            "delete interfaces loopback lo",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_deleted(self):
        """Delete all L3 config from eth1."""
        set_module_args(
            dict(
                config=[
                    dict(name="eth1"),
                ],
                state="deleted",
            ),
        )
        commands = [
            "delete interfaces ethernet eth1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_rendered(self):
        """Render set commands without connecting to the device."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        ipv4=[dict(address="dhcp")],
                    ),
                    dict(
                        name="eth1",
                        ipv4=[dict(address="192.0.2.14/24")],
                    ),
                ],
                state="rendered",
            ),
        )
        rendered_cmds = [
            "set interfaces ethernet eth0 address 'dhcp'",
            "set interfaces ethernet eth1 address '192.0.2.14/24'",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )

    def test_vyos_l3_interfaces_gathered(self):
        """Gather L3 interface facts from the device."""
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered = result["gathered"]
        # Verify eth1 is present with its IPv4 address
        eth1 = next((i for i in gathered if i["name"] == "eth1"), None)
        self.assertIsNotNone(eth1)
        self.assertIn({"address": "192.0.2.14/24"}, eth1["ipv4"])

    def test_vyos_l3_interfaces_parsed(self):
        """Parse a raw config string into structured data."""
        raw_config = (
            "set interfaces ethernet eth0 address 'dhcp'\n"
            "set interfaces ethernet eth1 address '192.0.2.14/24'\n"
        )
        set_module_args(
            dict(
                running_config=raw_config,
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed = result["parsed"]
        eth0 = next((i for i in parsed if i["name"] == "eth0"), None)
        self.assertIsNotNone(eth0)
        self.assertIn({"address": "dhcp"}, eth0["ipv4"])
        eth1 = next((i for i in parsed if i["name"] == "eth1"), None)
        self.assertIsNotNone(eth1)
        self.assertIn({"address": "192.0.2.14/24"}, eth1["ipv4"])

    def test_vyos_l3_interfaces_vif_merged(self):
        """Merge a new address onto a VIF sub-interface."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        vifs=[
                            dict(
                                vlan_id=101,
                                ipv4=[dict(address="198.51.100.200/25")],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set interfaces ethernet eth3 vif 101 address '198.51.100.200/25'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_l3_interfaces_vif_deleted(self):
        """Delete addresses from VIF sub-interfaces on eth3."""
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
            "delete interfaces ethernet eth3 vif 102 address '2001:db8:4000::3/34'",
            "delete interfaces ethernet eth3 address '198.51.100.10/24'",
        ]
        self.execute_module(changed=True, commands=commands)
