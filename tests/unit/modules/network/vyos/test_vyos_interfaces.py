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

from ansible_collections.vyos.vyos.plugins.modules import vyos_interfaces
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosInterfacesModule(TestVyosModule):
    module = vyos_interfaces

    def setUp(self):
        super(TestVyosInterfacesModule, self).setUp()
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
            "facts.interfaces.interfaces.InterfacesFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        # define the default fixture for the vyos_interfaces module
        self.fixture_path = "vyos_interfaces_config.cfg"

    def tearDown(self):
        super(TestVyosInterfacesModule, self).tearDown()
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
                    dict(name="bond1", description="Bond - 1", enabled=True),
                    dict(name="vtun1", description="vtun - 1", enabled=True),
                    dict(name="wg01", description="wg - 1", enabled=True),
                ],
                state="merged",
            ),
        )

        commands = [
            "set interfaces bonding bond1 description 'Bond - 1'",
            "set interfaces openvpn vtun1 description 'vtun - 1'",
            "set interfaces wireguard wg01 description 'wg - 1'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_merged_retain_vif(self):
        # we have a vif in eth1 at this point, so that should be retained
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="bond1", description="Bond - 1", enabled=True),
                    dict(name="vtun1", description="vtun - 1", enabled=True),
                    dict(name="wg01", description="wg - 1", enabled=True),
                ],
                state="merged",
            ),
        )

        commands = [
            "set interfaces bonding bond1 description 'Bond - 1'",
            "set interfaces openvpn vtun1 description 'vtun - 1'",
            "set interfaces wireguard wg01 description 'wg - 1'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_merged_additional_vif(self):
        # we have a vif in eth1 at this point, so that should be retained
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        vifs=[
                            dict(
                                vlan_id=105,
                                description="vlan 105",
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )

        commands = [
            "set interfaces ethernet eth1 vif 105 description 'vlan 105'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="wg02",
                        description="wire guard int 2",
                        enabled=True,
                    ),
                ],
                state="merged",
            ),
        )

        self.execute_module(changed=False, commands=[])

    def test_vyos_interfaces_merged_newinterface(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                    dict(name="eth1", description="Configured by Ansible"),
                ],
                state="merged",
            ),
        )

        commands = [
            "set interfaces ethernet eth1 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_replaced_newinterface(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                    dict(name="eth1", description="Configured by Ansible"),
                ],
                state="replaced",
            ),
        )

        commands = [
            "set interfaces ethernet eth1 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_replaced_remove_vif(self):
        # we have a vif in eth1 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                    dict(name="eth1", description="Configured by Ansible"),
                ],
                state="replaced",
            ),
        )

        commands = [
            "delete interfaces ethernet eth1 vif 200",
            "delete interfaces ethernet eth1 vif 201",
            "set interfaces ethernet eth1 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_merged_enable_vif(self):
        # merge in enabling vif
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        vifs=[
                            dict(
                                vlan_id=201,
                                enabled=True,
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )

        commands = [
            "delete interfaces ethernet eth1 vif 201 disable",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_replaced_retain_vif(self):
        # we have a vif in eth1 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                    dict(
                        name="eth1",
                        description="Configured by Ansible",
                        vifs=[
                            dict(
                                vlan_id=200,
                            ),
                            dict(
                                vlan_id=201,
                                description="VIF eth1.201",
                                enabled=True,
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )

        commands = [
            "delete interfaces ethernet eth1 vif 200 description",
            "delete interfaces ethernet eth1 vif 201 disable",
            "set interfaces ethernet eth1 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_overridden_newinterface(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                    dict(name="eth1", description="Configured by Ansible"),
                ],
                state="overridden",
            ),
        )

        commands = [
            "set interfaces ethernet eth1 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
            "delete interfaces wireguard wg02 description",
            "delete interfaces ethernet eth3 description",
            "delete interfaces ethernet eth3 disable",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_overridden_remove_vif(self):
        # we have a vif in eth1 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                    dict(name="eth1", description="Configured by Ansible"),
                ],
                state="overridden",
            ),
        )

        commands = [
            "set interfaces ethernet eth1 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
            "delete interfaces wireguard wg02 description",
            "delete interfaces ethernet eth3 description",
            "delete interfaces ethernet eth3 disable",
            "delete interfaces ethernet eth1 vif 200",
            "delete interfaces ethernet eth1 vif 201",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_idempotent_disable(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        description="Ethernet 3",
                        enabled=False,
                    ),
                ],
                state="merged",
            ),
        )

        commands = []
        self.execute_module(changed=False, commands=commands)

    def test_vyos_interfaces_idempotent_disable_replace(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        description="Ethernet 3",
                        enabled=False,
                    ),
                ],
                state="replaced",
            ),
        )

        commands = []
        self.execute_module(changed=False, commands=commands)

    def test_vyos_interfaces_deleted_remove_vif(self):
        # we have a vif in eth1 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vif.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="eth1"),
                ],
                state="deleted",
            ),
        )

        commands = [
            "delete interfaces ethernet eth1 vif 200",
            "delete interfaces ethernet eth1 vif 201",
            "delete interfaces ethernet eth1 description",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_deleted_remove_all(self):
        # we have a vif in eth1 at this point, so that should be removed
        set_module_args(
            dict(
                config=[],
                state="deleted",
            ),
        )

        commands = [
            "delete interfaces ethernet eth1 description",
            "delete interfaces ethernet eth3 description",
            "delete interfaces ethernet eth3 disable",
            "delete interfaces wireguard wg02 description",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_replaced_bad_name(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="int4",
                        description="Ethernet 4",
                        enabled=True,
                        speed="auto",
                        duplex="auto",
                    ),
                ],
                state="replaced",
            ),
        )

        self.execute_module(failed=True)
