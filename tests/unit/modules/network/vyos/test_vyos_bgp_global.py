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

from ansible_collections.vyos.vyos.tests.unit.compat.mock import patch
from ansible_collections.vyos.vyos.plugins.modules import vyos_bgp_global
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    set_module_args,
)
from .vyos_module import TestVyosModule, load_fixture


class TestVyosBgpglobalModule(TestVyosModule):

    module = vyos_bgp_global

    def setUp(self):
        super(TestVyosBgpglobalModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_execute_show_command_config = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.bgp_global.bgp_global.Bgp_global._get_config"
        )
        self.execute_show_command_config = (
            self.mock_execute_show_command_config.start()
        )

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
        )
        self.get_resource_connection_facts = (
            self.mock_get_resource_connection_facts.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.bgp_global.bgp_global.Bgp_globalFacts.get_device_data"
        )

        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosBgpglobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()
        self.mock_execute_show_command_config.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_bgp_global_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file
        self.execute_show_command_config.side_effect = load_from_file

    def test_vyos_bgp_global_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    neighbor=[
                        dict(
                            address="10.0.0.4",
                            disable_connected_check=True,
                            timers=dict(holdtime=30, keepalive=10),
                            capability=dict(orf="receive"),
                        ),
                        dict(
                            address="192.168.0.2",
                            attribute_unchanged=dict(as_path=True, med=True),
                            ebgp_multihop=2,
                            remote_as="65535",
                            soft_reconfiguration=True,
                            update_source="192.168.0.1",
                        ),
                        dict(
                            address="2001:db8::2",
                            ebgp_multihop=2,
                            remote_as="65535",
                            maximum_prefix=34,
                            update_source="2001:db8::1",
                        ),
                    ],
                    network=[
                        dict(address="172.16.42.32/27", backdoor=True),
                        dict(address="172.16.42.251/32", route_map="map01"),
                    ],
                    bgp_params=dict(
                        bestpath=dict(as_path="confed", compare_routerid=True),
                        default=dict(no_ipv4_unicast=True),
                        router_id="10.1.1.1",
                    ),
                    redistribute=[
                        dict(protocol="kernel", route_map="map01"),
                        dict(protocol="static", metric=20),
                        dict(protocol="static", route_map="map01"),
                    ],
                ),
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_bgp_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    maximum_paths=[
                        dict(path="ebgp", count=20),
                        dict(path="ibgp", count=45),
                    ],
                    neighbor=[
                        dict(
                            address="2001:db8::2",
                            ebgp_multihop=2,
                            remote_as="65535",
                            maximum_prefix=34,
                            update_source="2001:db8::1",
                            distribute_list=[
                                dict(action="export", acl=31),
                                dict(action="import", acl=9),
                            ],
                        )
                    ],
                    bgp_params=dict(
                        confederation=[dict(peers=20), dict(identifier=66)],
                        router_id="10.1.1.1",
                    ),
                ),
                state="merged",
            )
        )
        commands = [
            "set protocols bgp 65536 neighbor 2001:db8::2 distribute-list export 31",
            "set protocols bgp 65536 neighbor 2001:db8::2 distribute-list import 9",
            "set protocols bgp 65536 parameters confederation peers 20",
            "set protocols bgp 65536 parameters confederation identifier 66",
            "set protocols bgp 65536 maximum-paths ebgp 20",
            "set protocols bgp 65536 maximum-paths ibgp 45",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_bgp_global_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    neighbor=[
                        dict(
                            address="10.0.0.4",
                            disable_connected_check=True,
                            timers=dict(holdtime=30, keepalive=10),
                            capability=dict(orf="receive"),
                        ),
                        dict(
                            address="192.168.0.2",
                            attribute_unchanged=dict(as_path=True, med=True),
                            ebgp_multihop=2,
                            remote_as="65535",
                            soft_reconfiguration=True,
                            update_source="192.168.0.1",
                        ),
                        dict(
                            address="2001:db8::2",
                            ebgp_multihop=2,
                            remote_as="65535",
                            maximum_prefix=34,
                            update_source="2001:db8::1",
                        ),
                    ],
                    network=[
                        dict(address="172.16.42.32/27", backdoor=True),
                        dict(address="172.16.42.251/32", route_map="map01"),
                    ],
                    bgp_params=dict(
                        bestpath=dict(as_path="confed", compare_routerid=True),
                        default=dict(no_ipv4_unicast=True),
                        router_id="10.1.1.1",
                    ),
                    redistribute=[
                        dict(protocol="kernel", route_map="map01"),
                        dict(protocol="static", metric=20),
                        dict(protocol="static", route_map="map01"),
                    ],
                ),
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    #
    def test_vyos_bgp_global_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    timers=dict(holdtime=30, keepalive=10),
                    neighbor=[
                        dict(
                            address="200.11.155.3",
                            prefix_list=[
                                dict(action="export", prefix_list=10),
                            ],
                            allowas_in=10,
                        ),
                        dict(
                            address="2001:db8::2",
                            remote_as="65535",
                            as_override=True,
                            default_originate="map01",
                            route_map=[
                                dict(action="export", route_map="map01"),
                            ],
                        ),
                    ],
                    bgp_params=dict(
                        log_neighbor_changes=True,
                        no_client_to_client_reflection=True,
                        confederation=[dict(peers=20), dict(identifier=66)],
                        router_id="10.1.1.1",
                    ),
                ),
                state="replaced",
            )
        )
        commands = [
            "delete protocols bgp 65536 parameters default",
            "delete protocols bgp 65536 parameters bestpath compare-routerid",
            "delete protocols bgp 65536 parameters bestpath as-path confed",
            "delete protocols bgp 65536 network",
            "delete protocols bgp 65536 redistribute",
            "delete protocols bgp 65536 neighbor 2001:db8::2 update-source 2001:db8::1",
            "delete protocols bgp 65536 neighbor 2001:db8::2 maximum-prefix 34",
            "delete protocols bgp 65536 neighbor 2001:db8::2 ebgp-multihop 2",
            "delete protocols bgp 65536 neighbor 192.168.0.2",
            "delete protocols bgp 65536 neighbor 10.0.0.4",
            "set protocols bgp 65536 neighbor 200.11.155.3 prefix-list export 10",
            "set protocols bgp 65536 neighbor 200.11.155.3 allowas-in number 10",
            "set protocols bgp 65536 neighbor 2001:db8::2 as-override",
            "set protocols bgp 65536 neighbor 2001:db8::2 route-map export map01",
            "set protocols bgp 65536 parameters log-neighbor-changes",
            "set protocols bgp 65536 parameters no-client-to-client-reflection",
            "set protocols bgp 65536 parameters confederation peers 20",
            "set protocols bgp 65536 parameters confederation identifier 66",
            "set protocols bgp 65536 timers holdtime 30",
            "set protocols bgp 65536 timers keepalive 10",
        ]
        self.execute_module(changed=True, commands=commands)

    #
    def test_vyos_bgp_global_purged(self):
        set_module_args(dict(config=dict(as_number="65536"), state="purged"))
        #
        commands = ["delete protocols bgp 65536"]
        self.execute_module(changed=True, commands=commands)

    #
    def test_vyos_bgp_global_incorrect_instance(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="100",
                    timers=dict(holdtime=30, keepalive=10),
                    neighbor=[
                        dict(
                            address="200.11.155.3",
                            prefix_list=[
                                dict(action="export", prefix_list=10),
                            ],
                            allowas_in=10,
                        ),
                        dict(
                            address="2001:db8::2",
                            remote_as="65535",
                            as_override=True,
                            default_originate="map01",
                            route_map=[
                                dict(action="export", route_map="map01"),
                            ],
                        ),
                    ],
                    bgp_params=dict(
                        log_neighbor_changes=True,
                        no_client_to_client_reflection=True,
                        confederation=[dict(peers=20), dict(identifier=66)],
                        router_id="10.1.1.1",
                    ),
                ),
                state="replaced",
            )
        )
        result = self.execute_module(failed=True)
        self.assertIn(
            "Only one bgp instance is allowed per device", result["msg"]
        )

    def test_vyos_bgp_global_replaced_af(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    timers=dict(holdtime=30, keepalive=10),
                    neighbor=[
                        dict(
                            address="200.11.155.3",
                            prefix_list=[
                                dict(action="export", prefix_list=10),
                            ],
                            allowas_in=10,
                        ),
                        dict(
                            address="2001:db8::2",
                            remote_as="65535",
                            as_override=True,
                            default_originate="map01",
                            route_map=[
                                dict(action="export", route_map="map01"),
                            ],
                        ),
                    ],
                    bgp_params=dict(
                        log_neighbor_changes=True,
                        no_client_to_client_reflection=True,
                        confederation=[dict(peers=20), dict(identifier=66)],
                        router_id="10.1.1.1",
                    ),
                ),
                state="replaced",
            )
        )
        result = self.execute_module(
            failed=True, filename="vyos_bgp_global_af_config.cfg"
        )
        self.assertIn(
            "Use the _bgp_address_family module to delete the address_family under neighbor 5001::64, before replacing/deleting the neighbor.",
            result["msg"],
        )

    def test_vyos_bgp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    neighbor=[
                        dict(
                            address="10.0.0.4",
                            disable_connected_check=True,
                            timers=dict(holdtime=30, keepalive=10),
                            capability=dict(orf="receive"),
                        ),
                        dict(
                            address="192.168.0.2",
                            attribute_unchanged=dict(as_path=True, med=True),
                            ebgp_multihop=2,
                            remote_as="65535",
                            soft_reconfiguration=True,
                            update_source="192.168.0.1",
                        ),
                        dict(
                            address="2001:db8::2",
                            ebgp_multihop=2,
                            remote_as="65535",
                            maximum_prefix=34,
                            update_source="2001:db8::1",
                        ),
                    ],
                    network=[
                        dict(address="172.16.42.32/27", backdoor=True),
                        dict(address="172.16.42.251/32", route_map="map01"),
                    ],
                    bgp_params=dict(
                        bestpath=dict(as_path="confed", compare_routerid=True),
                        default=dict(no_ipv4_unicast=True),
                        router_id="10.1.1.1",
                    ),
                    redistribute=[
                        dict(protocol="kernel", route_map="map01"),
                        dict(protocol="static", metric=20),
                        dict(protocol="static", route_map="map01"),
                    ],
                ),
                state="rendered",
            )
        )
        rendered_cmds = [
            "set protocols bgp 65536 neighbor 10.0.0.4 disable-connected-check",
            "set protocols bgp 65536 neighbor 10.0.0.4 timers holdtime 30",
            "set protocols bgp 65536 neighbor 10.0.0.4 timers keepalive 10",
            "set protocols bgp 65536 neighbor 10.0.0.4 capability orf prefix-list receive",
            "set protocols bgp 65536 neighbor 192.168.0.2 attribute-unchanged as-path",
            "set protocols bgp 65536 neighbor 192.168.0.2 attribute-unchanged med",
            "set protocols bgp 65536 neighbor 192.168.0.2 attribute-unchanged next-hop",
            "set protocols bgp 65536 neighbor 192.168.0.2 ebgp-multihop 2",
            "set protocols bgp 65536 neighbor 192.168.0.2 remote-as 65535",
            "set protocols bgp 65536 neighbor 192.168.0.2 soft-reconfiguration",
            "set protocols bgp 65536 neighbor 192.168.0.2 update-source 192.168.0.1",
            "set protocols bgp 65536 neighbor 2001:db8::2 ebgp-multihop 2",
            "set protocols bgp 65536 neighbor 2001:db8::2 remote-as 65535",
            "set protocols bgp 65536 neighbor 2001:db8::2 maximum-prefix 34",
            "set protocols bgp 65536 neighbor 2001:db8::2 update-source 2001:db8::1",
            "set protocols bgp 65536 redistribute kernel route-map map01",
            "set protocols bgp 65536 redistribute static route-map map01",
            "set protocols bgp 65536 network 172.16.42.32/27 backdoor",
            "set protocols bgp 65536 network 172.16.42.251/32 route-map map01",
            "set protocols bgp 65536 parameters bestpath as-path confed",
            "set protocols bgp 65536 parameters bestpath compare-routerid",
            "set protocols bgp 65536 parameters default no-ipv4-unicast",
            "set protocols bgp 65536 parameters router-id 10.1.1.1",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )

    def test_vyos_bgp_global_parsed(self):

        commands = [
            "set protocols bgp 65536 neighbor 10.0.0.4 disable-connected-check",
            "set protocols bgp 65536 neighbor 10.0.0.4 timers holdtime 30",
            "set protocols bgp 65536 neighbor 10.0.0.4 timers keepalive 10",
            "set protocols bgp 65536 neighbor 10.0.0.4 capability orf prefix-list receive",
            "set protocols bgp 65536 neighbor 192.168.0.2 attribute-unchanged as-path",
            "set protocols bgp 65536 neighbor 192.168.0.2 attribute-unchanged med",
            "set protocols bgp 65536 neighbor 192.168.0.2 attribute-unchanged next-hop",
            "set protocols bgp 65536 neighbor 192.168.0.2 ebgp-multihop 2",
            "set protocols bgp 65536 neighbor 192.168.0.2 remote-as 65535",
            "set protocols bgp 65536 neighbor 192.168.0.2 soft-reconfiguration",
            "set protocols bgp 65536 neighbor 192.168.0.2 update-source 192.168.0.1",
            "set protocols bgp 65536 neighbor 2001:db8::2 ebgp-multihop 2",
            "set protocols bgp 65536 neighbor 2001:db8::2 remote-as 65535",
            "set protocols bgp 65536 neighbor 2001:db8::2 maximum-prefix 34",
            "set protocols bgp 65536 neighbor 2001:db8::2 update-source 2001:db8::1",
            "set protocols bgp 65536 redistribute kernel route-map map01",
            "set protocols bgp 65536 redistribute static route-map map01",
            "set protocols bgp 65536 network 172.16.42.32/27 backdoor",
            "set protocols bgp 65536 network 172.16.42.251/32 route-map map01",
            "set protocols bgp 65536 parameters bestpath as-path confed",
            "set protocols bgp 65536 parameters bestpath compare-routerid",
            "set protocols bgp 65536 parameters default no-ipv4-unicast",
            "set protocols bgp 65536 parameters router-id 10.1.1.1",
        ]
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": 65536,
            "bgp_params": {
                "bestpath": {"as_path": "confed", "compare_routerid": True},
                "default": {"no_ipv4_unicast": True},
                "router_id": "10.1.1.1",
            },
            "neighbor": [
                {
                    "address": "10.0.0.4",
                    "capability": {"orf": "receive"},
                    "disable_connected_check": True,
                    "timers": {"holdtime": 30, "keepalive": 10},
                },
                {
                    "address": "192.168.0.2",
                    "attribute_unchanged": {
                        "as_path": True,
                        "med": True,
                        "next_hop": True,
                    },
                    "ebgp_multihop": 2,
                    "remote_as": 65535,
                    "update_source": "192.168.0.1",
                },
                {
                    "address": "2001:db8::2",
                    "ebgp_multihop": 2,
                    "maximum_prefix": 34,
                    "remote_as": 65535,
                    "update_source": "2001:db8::1",
                },
            ],
            "network": [
                {"address": "172.16.42.32/27", "backdoor": True},
                {"address": "172.16.42.251/32", "route_map": "map01"},
            ],
            "redistribute": [
                {"protocol": "kernel", "route_map": "map01"},
                {"protocol": "static", "route_map": "map01"},
            ],
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_vyos_bgp_global_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = {
            "as_number": 65536,
            "bgp_params": {
                "bestpath": {"as_path": "confed", "compare_routerid": True},
                "default": {"no_ipv4_unicast": True},
                "router_id": "10.1.1.1",
            },
            "neighbor": [
                {
                    "address": "10.0.0.4",
                    "capability": {"orf": "receive"},
                    "disable_connected_check": True,
                    "timers": {"holdtime": 30, "keepalive": 10},
                },
                {
                    "address": "192.168.0.2",
                    "attribute_unchanged": {"as_path": True, "med": True},
                    "ebgp_multihop": 2,
                    "remote_as": 65535,
                    "soft_reconfiguration": True,
                    "update_source": "192.168.0.1",
                },
                {
                    "address": "2001:db8::2",
                    "ebgp_multihop": 2,
                    "maximum_prefix": 34,
                    "remote_as": 65535,
                    "update_source": "2001:db8::1",
                },
            ],
            "network": [
                {"address": "172.16.42.32/27", "backdoor": True},
                {"address": "172.16.42.251/32", "route_map": "map01"},
            ],
            "redistribute": [
                {"protocol": "kernel", "route_map": "map01"},
                {"metric": 20, "protocol": "static"},
                {"protocol": "static", "route_map": "map01"},
            ],
        }
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))
