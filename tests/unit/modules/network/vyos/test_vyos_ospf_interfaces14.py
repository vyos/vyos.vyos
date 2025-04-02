# Spawned from test_vyos_ospf_interfaces (c) 2016 Red Hat Inc.
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

from ansible_collections.vyos.vyos.plugins.modules import vyos_ospf_interfaces
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosOspfInterfacesModule14(TestVyosModule):
    module = vyos_ospf_interfaces

    def setUp(self):
        super(TestVyosOspfInterfacesModule14, self).setUp()
        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.ospf_interfaces.ospf_interfaces.Ospf_interfacesFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospf_interfaces.ospf_interfaces.get_os_version",
        )
        self.test_version = "1.4"
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = self.test_version
        self.mock_facts_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.ospf_interfaces.ospf_interfaces.get_os_version",
        )
        self.get_facts_os_version = self.mock_facts_get_os_version.start()
        self.get_facts_os_version.return_value = self.test_version
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosOspfInterfacesModule14, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_ospf_interfaces_config_14.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def sort_address_family(self, entry_list):
        for entry in entry_list:
            if entry.get("address_family"):
                entry["address_family"].sort(key=lambda i: i.get("afi"))

    def test_vyos_ospf_interfaces_merged_new_config(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                                authentication=dict(plaintext_password="abcdefg!"),
                                priority=55,
                            ),
                            dict(afi="ipv6", mtu_ignore=True, instance=20),
                        ],
                    ),
                    dict(
                        name="bond2",
                        address_family=[
                            dict(
                                afi="ipv4",
                                transmit_delay=9,
                            ),
                            dict(afi="ipv6", passive=True),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set protocols ospf interface bond2 transmit-delay 9",
            "set protocols ospfv3 interface bond2 passive",
            "set protocols ospf interface eth0 cost 100",
            "set protocols ospf interface eth0 priority 55",
            "set protocols ospf interface eth0 authentication plaintext-password abcdefg!",
            "set protocols ospfv3 interface eth0 instance-id 20",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_interfaces_merged_vif_config(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0.3",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                                authentication=dict(plaintext_password="abcdefg!"),
                                priority=55,
                            ),
                            dict(afi="ipv6", mtu_ignore=True),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set protocols ospf interface eth0.3 cost 100",
            "set protocols ospf interface eth0.3 priority 55",
            "set protocols ospf interface eth0.3 authentication plaintext-password abcdefg!",
            "set protocols ospfv3 interface eth0.3 mtu-ignore",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_interfaces_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(afi="ipv6", mtu_ignore=True, instance=33),
                        ],
                    ),
                    dict(
                        name="eth1",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                            ),
                            dict(afi="ipv6", ifmtu=33),
                        ],
                    ),
                ],
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_ospf_interfaces_existing_config_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(afi="ipv6", cost=500),
                        ],
                    ),
                    dict(
                        name="eth1",
                        address_family=[
                            dict(
                                afi="ipv4",
                                priority=100,
                            ),
                            dict(afi="ipv6", ifmtu=25),
                        ],
                    ),
                ],
            ),
        )
        commands = [
            "set protocols ospfv3 interface eth0 cost 500",
            "set protocols ospf interface eth1 priority 100",
            "set protocols ospfv3 interface eth1 ifmtu 25",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                                authentication=dict(plaintext_password="abcdefg!"),
                                priority=55,
                            ),
                        ],
                    ),
                    dict(
                        name="bond2",
                        address_family=[
                            dict(
                                afi="ipv4",
                                transmit_delay=9,
                            ),
                            dict(afi="ipv6", passive=True),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "set protocols ospf interface bond2 transmit-delay 9",
            "set protocols ospfv3 interface bond2 passive",
            "set protocols ospf interface eth0 cost 100",
            "set protocols ospf interface eth0 priority 55",
            "set protocols ospf interface eth0 authentication plaintext-password abcdefg!",
            "delete protocols ospfv3 interface eth0 instance-id 33",
            "delete protocols ospfv3 interface eth0 mtu-ignore",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_passive_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(
                                afi="ipv4",
                                passive=True,
                            ),
                        ],
                    ),
                    dict(
                        name="eth1",
                        address_family=[
                            dict(
                                afi="ipv4",
                                passive=True,
                            ),
                            dict(
                                afi="ipv6",
                                passive=True,
                            ),
                        ],
                    ),
                    dict(
                        name="bond2",
                        address_family=[
                            dict(
                                afi="ipv4",
                                passive=True,
                            ),
                            dict(afi="ipv6", passive=True),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "delete protocols ospf interface eth1 cost 100",
            "delete protocols ospfv3 interface eth0 instance-id 33",
            "delete protocols ospfv3 interface eth0 mtu-ignore",
            "delete protocols ospfv3 interface eth1 ifmtu 33",
            "set protocols ospf interface bond2 passive",
            "set protocols ospfv3 interface bond2 passive",
            "set protocols ospf interface eth0 passive",
            "set protocols ospf interface eth1 passive",
            "set protocols ospfv3 interface eth1 passive",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_interfaces_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(afi="ipv6", mtu_ignore=True, instance=33),
                        ],
                    ),
                    dict(
                        name="eth1",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                            ),
                            dict(afi="ipv6", ifmtu=33),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_ospf_interfaces_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                                authentication=dict(plaintext_password="abcdefg!"),
                                priority=55,
                            ),
                        ],
                    ),
                    dict(
                        name="bond2",
                        address_family=[
                            dict(
                                afi="ipv4",
                                transmit_delay=9,
                            ),
                            dict(afi="ipv6", passive=True),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "set protocols ospf interface bond2 transmit-delay 9",
            "set protocols ospfv3 interface bond2 passive",
            "set protocols ospf interface eth0 cost 100",
            "set protocols ospf interface eth0 priority 55",
            "set protocols ospf interface eth0 authentication plaintext-password abcdefg!",
            "delete protocols ospf interface eth1",
            "delete protocols ospfv3 interface eth1",
            "delete protocols ospfv3 interface eth0 mtu-ignore",
            "delete protocols ospfv3 interface eth0 instance-id 33",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_interfaces_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(afi="ipv6", mtu_ignore=True, instance=33),
                        ],
                    ),
                    dict(
                        name="eth1",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                            ),
                            dict(afi="ipv6", ifmtu=33),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_ospf_interfaces_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                    ),
                ],
                state="deleted",
            ),
        )
        commands = ["delete protocols ospfv3 interface eth0"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_ospf_interfaces_notpresent_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                    ),
                ],
                state="deleted",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_ospf_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth0",
                        address_family=[
                            dict(
                                afi="ipv4",
                                cost=100,
                                authentication=dict(plaintext_password="abcdefg!"),
                                priority=55,
                            ),
                            dict(afi="ipv6", mtu_ignore=True, instance=20),
                        ],
                    ),
                    dict(
                        name="bond2",
                        address_family=[
                            dict(
                                afi="ipv4",
                                transmit_delay=9,
                            ),
                            dict(afi="ipv6", passive=True),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            "set protocols ospf interface eth0 cost 100",
            "set protocols ospf interface eth0 authentication plaintext-password abcdefg!",
            "set protocols ospf interface eth0 priority 55",
            "set protocols ospfv3 interface eth0 mtu-ignore",
            "set protocols ospfv3 interface eth0 instance-id 20",
            "set protocols ospf interface bond2 transmit-delay 9",
            "set protocols ospfv3 interface bond2 passive",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands), result["rendered"])

    def test_vyos_ospf_interfaces_parsed(self):
        commands = [
            "set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'",
            "set protocols ospf interface bond2 bandwidth '70'",
            "set protocols ospf interface bond2 transmit-delay '45'",
            "set protocols ospfv3 interface bond2 'passive'",
            "set protocols ospf interface eth0 cost '50'",
            "set protocols ospf interface eth0 priority '26'",
            "set protocols ospfv3 interface eth0 instance-id '33'",
            "set protocols ospfv3 interface eth0 'mtu-ignore'",
            "set protocols ospf interface eth1 network 'point-to-point'",
            "set protocols ospf interface eth1 priority '26'",
            "set protocols ospf interface eth1 transmit-delay '50'",
            "set protocols ospfv3 interface eth1 dead-interval '39'",
        ]

        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "authentication": {
                            "md5_key": {
                                "key": "1111111111232345",
                                "key_id": 10,
                            },
                        },
                        "bandwidth": 70,
                        "transmit_delay": 45,
                    },
                    {"afi": "ipv6", "passive": True},
                ],
                "name": "bond2",
            },
            {
                "address_family": [
                    {"afi": "ipv4", "cost": 50, "priority": 26},
                    {"afi": "ipv6", "instance": "33", "mtu_ignore": True},
                ],
                "name": "eth0",
            },
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "network": "point-to-point",
                        "priority": 26,
                        "transmit_delay": 50,
                    },
                    {"afi": "ipv6", "dead_interval": 39},
                ],
                "name": "eth1",
            },
        ]
        result_list = self.sort_address_family(result["parsed"])
        given_list = self.sort_address_family(parsed_list)
        self.assertEqual(result_list, given_list)

    def test_vyos_ospf_interfaces_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False, filename="vyos_ospf_interfaces_config.cfg")
        gathered_list = [
            {
                "address_family": [{"afi": "ipv6", "instance": "33", "mtu_ignore": True}],
                "name": "eth0",
            },
            {
                "address_family": [
                    {"afi": "ipv4", "cost": 100},
                    {"afi": "ipv6", "ifmtu": 33},
                ],
                "name": "eth1",
            },
        ]

        result_list = self.sort_address_family(result["gathered"])
        given_list = self.sort_address_family(gathered_list)
        self.assertEqual(result_list, given_list)
