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
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
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

    def test_vyos_interfaces_replaced_remove_vrf(self):
        # we have a vrf in eth2 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
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
                    dict(name="eth2", description="Configured by Ansible"),
                ],
                state="replaced",
            ),
        )

        commands = [
            "delete interfaces ethernet eth2 vrf",
            "set interfaces ethernet eth2 description 'Configured by Ansible'",
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

    def test_vyos_overridden_remove_vrf(self):
        # we have a vrf in eth2 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
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
                    dict(name="eth2", description="Configured by Ansible"),
                ],
                state="overridden",
            ),
        )

        commands = [
            "set interfaces ethernet eth2 description 'Configured by Ansible'",
            "set interfaces ethernet eth4 description 'Ethernet 4'",
            "set interfaces ethernet eth4 duplex 'auto'",
            "set interfaces ethernet eth4 speed 'auto'",
            "delete interfaces ethernet eth2 vrf",
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

    def test_vyos_interfaces_deleted_remove_vrf(self):
        # we have a vrf in eth2 at this point, so that should be removed
        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="eth2"),
                ],
                state="deleted",
            ),
        )

        commands = [
            "delete interfaces ethernet eth2 vrf",
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

    def test_vyos_interfaces_merged_idempotent_vrf(self):

        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="eth2", vrf="green"),
                ],
                state="merged",
            ),
        )

        commands = []
        self.execute_module(changed=False, commands=commands)

    def test_vyos_interfaces_replaced_idempotent_vrf(self):

        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="eth2", vrf="green"),
                ],
                state="replaced",
            ),
        )

        commands = []
        self.execute_module(changed=False, commands=commands)

    def test_vyos_interfaces_overridden_idempotent_vrf(self):

        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="eth2", vrf="green"),
                ],
                state="overridden",
            ),
        )

        commands = []
        self.execute_module(changed=False, commands=commands)

    def test_vyos_interfaces_merged_additional_vrf(self):

        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        vrf="pink",
                    ),
                ],
                state="merged",
            ),
        )

        commands = [
            "set interfaces ethernet eth1 vrf 'pink'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_interfaces_gathered_vrf(self):
        # gathered facts should surface the vrf set on eth2
        self.fixture_path = "vyos_interfaces_config_vrf.cfg"
        set_module_args(
            dict(
                config=[],
                state="gathered",
            ),
        )

        result = self.execute_module(changed=False)
        eth2_facts = [i for i in result["gathered"] if i["name"] == "eth2"][0]
        self.assertEqual(eth2_facts["vrf"], "green")

    def test_vyos_interfaces_parsed_vrf(self):
        # parsing a running_config string should surface vrf on eth2
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth2 vrf 'green'",
                state="parsed",
            ),
        )

        result = self.execute_module(changed=False)
        eth2_facts = [i for i in result["parsed"] if i["name"] == "eth2"][0]
        self.assertEqual(eth2_facts["vrf"], "green")

    def test_vyos_interfaces_rendered_vrf(self):
        # rendered output should include the vrf set command without touching a device
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        vrf="pink",
                    ),
                ],
                state="rendered",
            ),
        )

        result = self.execute_module(changed=False)
        commands = [
            "set interfaces ethernet eth1 vrf 'pink'",
        ]
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_vyos_interfaces_parsed_disable_prefixed_options(self):
        # disable-link-detect is not disable: the interface stays enabled
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth0 disable-link-detect\n"
                "set interfaces ethernet eth0 hw-id '00:50:56:00:00:01'",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [{"name": "eth0", "enabled": True}],
        )

    def test_vyos_interfaces_parsed_vif_ids_kept_apart(self):
        # vif 110's lines must not end up in vif 10
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth1 vif 10 description 'ten'\n"
                "set interfaces ethernet eth1 vif 110 description 'one-ten'\n"
                "set interfaces ethernet eth1 vif 110 mtu '1400'",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [
                {
                    "name": "eth1",
                    "enabled": True,
                    "vifs": [
                        {"vlan_id": 10, "description": "ten", "enabled": True},
                        {"vlan_id": 110, "description": "one-ten", "mtu": 1400, "enabled": True},
                    ],
                },
            ],
        )

    def test_vyos_interfaces_parsed_vif_in_description(self):
        # a description containing "vif" is an interface option, not a vif line
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth2 description 'vif uplink'\n"
                "set interfaces ethernet eth2 mtu '1450'",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [{"name": "eth2", "description": "vif uplink", "mtu": 1450, "enabled": True}],
        )

    def test_vyos_interfaces_replaced_enable_once(self):
        # re-enabling a disabled interface deletes disable once, not twice
        set_module_args(dict(config=[dict(name="eth3")], state="replaced"))
        self.execute_module(
            changed=True,
            commands=[
                "delete interfaces ethernet eth3 description",
                "delete interfaces ethernet eth3 disable",
            ],
        )

    def test_vyos_interfaces_deleted_not_on_device(self):
        # an interface without configuration on the device: nothing to delete
        set_module_args(dict(config=[dict(name="eth9")], state="deleted"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_interfaces_parsed_quoted_vif(self):
        # a vif without options ends the line, and VyOS quotes its VLAN ID
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth1 vif '10'\n"
                "set interfaces ethernet eth1 vif 20 description 'twenty'",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [
                {
                    "name": "eth1",
                    "enabled": True,
                    "vifs": [
                        {"vlan_id": 10, "enabled": True},
                        {"vlan_id": 20, "description": "twenty", "enabled": True},
                    ],
                },
            ],
        )

    def test_vyos_interfaces_merged_vif_vrf(self):
        set_module_args(
            dict(
                config=[dict(name="eth1", vifs=[dict(vlan_id=200, vrf="green")])],
                state="merged",
            ),
        )
        self.execute_module(
            changed=True,
            commands=["set interfaces ethernet eth1 vif 200 vrf 'green'"],
        )

    def test_vyos_interfaces_parsed_vif_vrf(self):
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth1 vif 200 vrf 'green'\n"
                "set interfaces ethernet eth1 vif 200 description 'in green'",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [
                {
                    "name": "eth1",
                    "enabled": True,
                    "vifs": [
                        {
                            "vlan_id": 200,
                            "vrf": "green",
                            "description": "in green",
                            "enabled": True,
                        },
                    ],
                },
            ],
        )

    def test_vyos_interfaces_replaced_vif_vrf_removed(self):
        self.fixture_path = "vyos_interfaces_config_vif_vrf.cfg"
        set_module_args(
            dict(
                config=[dict(name="eth1", vifs=[dict(vlan_id=200, description="in green")])],
                state="replaced",
            ),
        )
        self.execute_module(
            changed=True,
            commands=["delete interfaces ethernet eth1 vif 200 vrf"],
        )

    def test_vyos_interfaces_parsed_tunnel(self):
        set_module_args(
            dict(
                running_config="set interfaces tunnel tun0 encapsulation 'gre'\n"
                "set interfaces tunnel tun0 source-address '192.0.2.1'\n"
                "set interfaces tunnel tun0 enable-multicast\n"
                "set interfaces tunnel tun0 parameters ip key '1'\n"
                "set interfaces tunnel tun0 parameters ip no-pmtu-discovery",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [
                {
                    "name": "tun0",
                    "enabled": True,
                    "tunnel": {
                        "encapsulation": "gre",
                        "source_address": "192.0.2.1",
                        "enable_multicast": True,
                        "parameters": {"ip": {"key": 1, "no_pmtu_discovery": True}},
                    },
                },
            ],
        )

    def test_vyos_interfaces_rendered_tunnel(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="tun1",
                        tunnel=dict(
                            encapsulation="gre",
                            source_interface="eth0",
                            remote="198.51.100.1",
                            parameters=dict(ip=dict(ttl=0, tos="inherit")),
                        ),
                    ),
                ],
                state="rendered",
            ),
        )
        self.assertEqual(
            sorted(self.execute_module(changed=False)["rendered"]),
            [
                "set interfaces tunnel tun1 encapsulation 'gre'",
                "set interfaces tunnel tun1 parameters ip tos 'inherit'",
                "set interfaces tunnel tun1 parameters ip ttl '0'",
                "set interfaces tunnel tun1 remote '198.51.100.1'",
                "set interfaces tunnel tun1 source-interface 'eth0'",
            ],
        )

    def test_vyos_interfaces_merged_tunnel_idempotent(self):
        self.fixture_path = "vyos_interfaces_config_tunnel.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="tun0",
                        description="dmvpn hub",
                        tunnel=dict(
                            encapsulation="gre",
                            source_address="192.0.2.1",
                            enable_multicast=True,
                            parameters=dict(ip=dict(key=1)),
                        ),
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_interfaces_replaced_without_tunnel_keeps_tunnel(self):
        # no tunnel key: the tunnel definition is left as it is
        self.fixture_path = "vyos_interfaces_config_tunnel.cfg"
        set_module_args(dict(config=[dict(name="tun0", description="new")], state="replaced"))
        self.execute_module(
            changed=True,
            commands=["set interfaces tunnel tun0 description 'new'"],
        )

    def test_vyos_interfaces_replaced_tunnel_options(self):
        # a tunnel key: options it does not list are removed
        self.fixture_path = "vyos_interfaces_config_tunnel.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="tun0",
                        description="dmvpn hub",
                        tunnel=dict(encapsulation="gre", source_address="192.0.2.1"),
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(
            changed=True,
            commands=[
                "delete interfaces tunnel tun0 enable-multicast",
                "delete interfaces tunnel tun0 parameters ip key",
            ],
        )

    def test_vyos_interfaces_tunnel_on_non_tunnel(self):
        set_module_args(
            dict(config=[dict(name="eth1", tunnel=dict(encapsulation="gre"))], state="merged"),
        )
        result = self.execute_module(failed=True)
        self.assertEqual(
            result["msg"],
            "tunnel options are only valid for tunnel interfaces, not eth1",
        )

    def test_vyos_interfaces_merged_vxlan_unchanged(self):
        # an unchanged VXLAN interface: nothing to do, and no failure
        self.fixture_path = "vyos_interfaces_config_vxlan.cfg"
        set_module_args(
            dict(config=[dict(name="vxlan2", description="overlay", mtu=1450)], state="merged"),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_interfaces_merged_vxlan(self):
        self.fixture_path = "vyos_interfaces_config_vxlan.cfg"
        set_module_args(dict(config=[dict(name="vxlan2", description="new")], state="merged"))
        self.execute_module(
            changed=True,
            commands=["set interfaces vxlan vxlan2 description 'new'"],
        )

    def test_vyos_interfaces_parsed_adjust_mss(self):
        set_module_args(
            dict(
                running_config="set interfaces ethernet eth1 ip adjust-mss '1436'\n"
                "set interfaces ethernet eth1 ipv6 adjust-mss 'clamp-mss-to-pmtu'\n"
                "set interfaces ethernet eth1 vif 10 ip adjust-mss 'clamp-mss-to-pmtu'",
                state="parsed",
            ),
        )
        self.assertEqual(
            self.execute_module(changed=False)["parsed"],
            [
                {
                    "name": "eth1",
                    "enabled": True,
                    "ip": {"adjust_mss": "1436"},
                    "ipv6": {"adjust_mss": "clamp-mss-to-pmtu"},
                    "vifs": [
                        {"vlan_id": 10, "enabled": True, "ip": {"adjust_mss": "clamp-mss-to-pmtu"}},
                    ],
                },
            ],
        )

    def test_vyos_interfaces_merged_adjust_mss_idempotent(self):
        # a number given as an integer matches the device's quoted value
        self.fixture_path = "vyos_interfaces_config_adjust_mss.cfg"
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        ip=dict(adjust_mss=1436),
                        ipv6=dict(adjust_mss="clamp-mss-to-pmtu"),
                        vifs=[dict(vlan_id=10, ip=dict(adjust_mss="clamp-mss-to-pmtu"))],
                    ),
                    dict(name="tun0", ip=dict(adjust_mss=1360)),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_interfaces_merged_adjust_mss(self):
        self.fixture_path = "vyos_interfaces_config_adjust_mss.cfg"
        set_module_args(
            dict(
                config=[
                    dict(name="tun0", ip=dict(adjust_mss="clamp-mss-to-pmtu")),
                    dict(name="bond0", vifs=[dict(vlan_id=20, ipv6=dict(adjust_mss=1400))]),
                ],
                state="merged",
            ),
        )
        self.execute_module(
            changed=True,
            commands=[
                "set interfaces tunnel tun0 ip adjust-mss 'clamp-mss-to-pmtu'",
                "set interfaces bonding bond0 vif 20 ipv6 adjust-mss '1400'",
            ],
        )

    def test_vyos_interfaces_replaced_adjust_mss_removed(self):
        self.fixture_path = "vyos_interfaces_config_adjust_mss.cfg"
        set_module_args(
            dict(
                config=[dict(name="eth1", ip=dict(adjust_mss="1436"), vifs=[dict(vlan_id=10)])],
                state="replaced",
            ),
        )
        self.execute_module(
            changed=True,
            commands=[
                "delete interfaces ethernet eth1 ipv6 adjust-mss",
                "delete interfaces ethernet eth1 vif 10 ip adjust-mss",
            ],
        )

    def test_vyos_interfaces_adjust_mss_out_of_range(self):
        set_module_args(
            dict(config=[dict(name="eth1", ip=dict(adjust_mss="100"))], state="merged"),
        )
        result = self.execute_module(failed=True)
        self.assertEqual(
            result["msg"],
            "ip adjust_mss of eth1 must be clamp-mss-to-pmtu or 536-65535, got 100",
        )

    def test_vyos_interfaces_adjust_mss_on_loopback(self):
        set_module_args(
            dict(config=[dict(name="lo", ip=dict(adjust_mss="1400"))], state="merged"),
        )
        result = self.execute_module(failed=True)
        self.assertEqual(result["msg"], "ip adjust-mss is not supported on lo")
