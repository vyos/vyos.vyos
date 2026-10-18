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

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_lag_interfaces
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosLagInterfacesModule(TestVyosModule):
    module = vyos_lag_interfaces

    def setUp(self):
        super(TestVyosLagInterfacesModule, self).setUp()
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
            "facts.lag_interfaces.lag_interfaces.Lag_interfacesFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        # define the default fixture for the vyos_interfaces module
        self.fixture_path = "vyos_lag_interfaces_config.cfg"

    def tearDown(self):
        super(TestVyosLagInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture(self.fixture_path)

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="bond1",
                        members=[{"member": "eth2"}, {"member": "eth3"}],
                        mode="802.3ad",
                        hash_policy="layer2+3",
                        primary="eth2",
                    ),
                ],
                state="merged",
            ),
        )

        commands = [
            "set interfaces bonding bond1 member interface 'eth2'",
            "set interfaces bonding bond1 member interface 'eth3'",
            "set interfaces bonding bond1 primary 'eth2'",
            "set interfaces bonding bond1 mode '802.3ad'",
            "set interfaces bonding bond1 hash-policy 'layer2+3'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="bond1",
                        members=[{"member": "eth2"}, {"member": "eth3"}],
                        mode="802.3ad",
                        hash_policy="layer2+3",
                        primary="eth2",
                    ),
                ],
                state="replaced",
            ),
        )

        commands = [
            "set interfaces bonding bond1 member interface 'eth2'",
            "set interfaces bonding bond1 member interface 'eth3'",
            "set interfaces bonding bond1 primary 'eth2'",
            "set interfaces bonding bond1 mode '802.3ad'",
            "set interfaces bonding bond1 hash-policy 'layer2+3'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="bond1",
                        members=[{"member": "eth2"}, {"member": "eth3"}],
                        mode="802.3ad",
                        hash_policy="layer2+3",
                        primary="eth2",
                    ),
                ],
                state="overridden",
            ),
        )

        commands = [
            "delete interfaces bonding bond0 member interface 'eth0'",
            "delete interfaces bonding bond0 member interface 'eth1'",
            "delete interfaces bonding bond0 primary",
            "delete interfaces bonding bond0 mode",
            "delete interfaces bonding bond0 hash-policy",
            "set interfaces bonding bond1 member interface 'eth2'",
            "set interfaces bonding bond1 member interface 'eth3'",
            "set interfaces bonding bond1 primary 'eth2'",
            "set interfaces bonding bond1 mode '802.3ad'",
            "set interfaces bonding bond1 hash-policy 'layer2+3'",
        ]
        self.execute_module(changed=True, commands=commands)
