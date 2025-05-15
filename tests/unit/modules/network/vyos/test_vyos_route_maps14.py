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

from ansible_collections.vyos.vyos.plugins.modules import vyos_route_maps
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosRouteMapsModule(TestVyosModule):
    module = vyos_route_maps

    def setUp(self):
        super(TestVyosRouteMapsModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.route_maps.route_maps.Route_mapsFacts.get_config",
        )

        self.execute_show_command = self.mock_execute_show_command.start()
        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.route_maps.route_maps.get_os_version",
        )
        self.test_version = "1.4"
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = self.test_version
        self.mock_facts_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.route_maps.route_maps.get_os_version",
        )
        self.get_facts_os_version = self.mock_facts_get_os_version.start()
        self.get_facts_os_version.return_value = self.test_version
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosRouteMapsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_route_maps_config_v14.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_route_maps_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test3",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                    metric=1,
                                    peer="1.1.1.2",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.20",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-1",
                                    origin="egp",
                                    originator_id="10.0.2.3",
                                    src="10.0.2.15",
                                    tag=5,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_route_maps_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test2",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                    metric=1,
                                    peer="1.1.1.3",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.22",
                                    large_community="10:20:21",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-2",
                                    origin="egp",
                                    originator_id="10.0.2.2",
                                    src="10.0.2.15",
                                    tag=4,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set policy route-map test2 rule 1 action permit",
            "set policy route-map test2 rule 1 set bgp-extcommunity-rt 22:11",
            "set policy route-map test2 rule 1 set ip-next-hop 10.20.10.22",
            "set policy route-map test2 rule 1 set ipv6-next-hop global fdda:5cc1:23:4::1f",
            "set policy route-map test2 rule 1 set large-community replace 10:20:21",
            "set policy route-map test2 rule 1 set local-preference 4",
            "set policy route-map test2 rule 1 set metric 5",
            "set policy route-map test2 rule 1 set metric-type type-2",
            "set policy route-map test2 rule 1 set origin egp",
            "set policy route-map test2 rule 1 set originator-id 10.0.2.2",
            "set policy route-map test2 rule 1 set src 10.0.2.15",
            "set policy route-map test2 rule 1 set tag 4",
            "set policy route-map test2 rule 1 set weight 4",
            "set policy route-map test2 rule 1 set community replace internet",
            "set policy route-map test2 rule 1 match interface eth2",
            "set policy route-map test2 rule 1 match metric 1",
            "set policy route-map test2 rule 1 match peer 1.1.1.3",
            "set policy route-map test2 rule 1 match ipv6 nexthop fdda:5cc1:23:4::1f",
            "set policy route-map test2 rule 1 match rpki invalid",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_route_maps_extras_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test2",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                call="2",
                                continue_sequence=2,
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                    metric=1,
                                    peer="1.1.1.3",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                    community=dict(community_list="235"),
                                    protocol="bgp",
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    extcommunity_rt="22:11",
                                    extcommunity_soo="220:110",
                                    extcommunity_bandwidth="100",
                                    extcommunity_bandwidth_non_transitive=True,
                                    atomic_aggregate=True,
                                    aggregator={"ip": "10.20.11.22", "as": "245"},
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.22",
                                    large_community="10:20:21",
                                    as_path_prepend="100 200 350",
                                    as_path_exclude="150",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-2",
                                    origin="egp",
                                    originator_id="10.0.2.2",
                                    src="10.0.2.15",
                                    tag=4,
                                    weight=4,
                                    table=7,
                                ),
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set policy route-map test2 rule 1 action permit",
            "set policy route-map test2 rule 1 call 2",
            "set policy route-map test2 rule 1 set bgp-extcommunity-rt 22:11",
            "set policy route-map test2 rule 1 set ip-next-hop 10.20.10.22",
            "set policy route-map test2 rule 1 set ipv6-next-hop global fdda:5cc1:23:4::1f",
            "set policy route-map test2 rule 1 set large-community replace 10:20:21",
            "set policy route-map test2 rule 1 set as-path prepend '100 200 350'",
            "set policy route-map test2 rule 1 set as-path exclude 150",
            "set policy route-map test2 rule 1 set local-preference 4",
            "set policy route-map test2 rule 1 set metric 5",
            "set policy route-map test2 rule 1 set metric-type type-2",
            "set policy route-map test2 rule 1 set origin egp",
            "set policy route-map test2 rule 1 set originator-id 10.0.2.2",
            "set policy route-map test2 rule 1 set src 10.0.2.15",
            "set policy route-map test2 rule 1 set tag 4",
            "set policy route-map test2 rule 1 set weight 4",
            "set policy route-map test2 rule 1 set table 7",
            "set policy route-map test2 rule 1 set community replace internet",
            "set policy route-map test2 rule 1 set extcommunity rt 22:11",
            "set policy route-map test2 rule 1 set extcommunity soo 220:110",
            "set policy route-map test2 rule 1 set extcommunity bandwidth 100",
            "set policy route-map test2 rule 1 set extcommunity bandwidth-non-transitive",
            "set policy route-map test2 rule 1 set atomic-aggregate",
            "set policy route-map test2 rule 1 set aggregator as 245",
            "set policy route-map test2 rule 1 set aggregator ip 10.20.11.22",
            "set policy route-map test2 rule 1 match interface eth2",
            "set policy route-map test2 rule 1 match metric 1",
            "set policy route-map test2 rule 1 match peer 1.1.1.3",
            "set policy route-map test2 rule 1 match ipv6 nexthop fdda:5cc1:23:4::1f",
            "set policy route-map test2 rule 1 match rpki invalid",
            "set policy route-map test2 rule 1 match protocol bgp",
            "set policy route-map test2 rule 1 match community community-list 235",
            "set policy route-map test2 rule 1 continue 2",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_route_maps_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test3",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    metric=1,
                                    peer="1.1.1.3",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="100:100"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.22",
                                    large_community="10:20:21",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-2",
                                    origin="egp",
                                    originator_id="10.0.2.2",
                                    src="fdda:5cc1:23:4::12",
                                    tag=4,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "delete policy route-map test3 rule 1 match interface eth2",
            "set policy route-map test3 rule 1 set ip-next-hop 10.20.10.22",
            "set policy route-map test3 rule 1 set community replace 100:100",
            "set policy route-map test3 rule 1 set large-community replace 10:20:21",
            "set policy route-map test3 rule 1 set metric-type type-2",
            "set policy route-map test3 rule 1 set originator-id 10.0.2.2",
            "set policy route-map test3 rule 1 set tag 4",
            "set policy route-map test3 rule 1 set src fdda:5cc1:23:4::12",
            "set policy route-map test3 rule 1 match peer 1.1.1.3",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_route_maps_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test3",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                    metric=1,
                                    peer="1.1.1.2",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.20",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-1",
                                    origin="egp",
                                    originator_id="10.0.2.3",
                                    src="10.0.2.15",
                                    tag=5,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_route_maps_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test2",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(rpki="invalid", peer="1.1.1.3"),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.22",
                                    large_community="10:20:21",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-2",
                                    origin="egp",
                                    originator_id="10.0.2.2",
                                    src="10.0.2.15",
                                    tag=4,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "delete policy route-map test3",
            "set policy route-map test2 rule 1 action permit",
            "set policy route-map test2 rule 1 set bgp-extcommunity-rt 22:11",
            "set policy route-map test2 rule 1 set ip-next-hop 10.20.10.22",
            "set policy route-map test2 rule 1 set ipv6-next-hop global fdda:5cc1:23:4::1f",
            "set policy route-map test2 rule 1 set large-community replace 10:20:21",
            "set policy route-map test2 rule 1 set local-preference 4",
            "set policy route-map test2 rule 1 set metric 5",
            "set policy route-map test2 rule 1 set metric-type type-2",
            "set policy route-map test2 rule 1 set origin egp",
            "set policy route-map test2 rule 1 set originator-id 10.0.2.2",
            "set policy route-map test2 rule 1 set src 10.0.2.15",
            "set policy route-map test2 rule 1 set tag 4",
            "set policy route-map test2 rule 1 set weight 4",
            "set policy route-map test2 rule 1 set community replace internet",
            "set policy route-map test2 rule 1 match peer 1.1.1.3",
            "set policy route-map test2 rule 1 match rpki invalid",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_route_maps__deny_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test2",
                        entries=[
                            dict(
                                sequence=1,
                                action="deny",
                                match=dict(rpki="invalid", peer="1.1.1.5"),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "delete policy route-map test3",
            "set policy route-map test2 rule 1 action deny",
            "set policy route-map test2 rule 1 match peer 1.1.1.5",
            "set policy route-map test2 rule 1 match rpki invalid",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_route_maps_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test3",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                    metric=1,
                                    peer="1.1.1.2",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.20",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-1",
                                    origin="egp",
                                    originator_id="10.0.2.3",
                                    src="10.0.2.15",
                                    tag=5,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_route_maps_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test3",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                    metric=1,
                                    peer="1.1.1.2",
                                    ipv6=dict(next_hop="fdda:5cc1:23:4::1f"),
                                ),
                                set=dict(
                                    ipv6_next_hop=dict(
                                        ip_type="global",
                                        value="fdda:5cc1:23:4::1f",
                                    ),
                                    community=dict(value="internet"),
                                    bgp_extcommunity_rt="22:11",
                                    ip_next_hop="10.20.10.20",
                                    local_preference=4,
                                    metric=5,
                                    metric_type="type-1",
                                    origin="egp",
                                    originator_id="10.0.2.3",
                                    src="10.0.2.15",
                                    tag=5,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                    dict(
                        route_map="test1",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                description="test",
                                on_match=dict(next=True),
                            ),
                            dict(
                                sequence=2,
                                action="permit",
                                on_match=dict(goto=4),
                            ),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )
        rendered_cmds = [
            "set policy route-map test3 rule 1 action permit",
            "set policy route-map test3 rule 1 set bgp-extcommunity-rt 22:11",
            "set policy route-map test3 rule 1 set ip-next-hop 10.20.10.20",
            "set policy route-map test3 rule 1 set ipv6-next-hop global fdda:5cc1:23:4::1f",
            "set policy route-map test3 rule 1 set local-preference 4",
            "set policy route-map test3 rule 1 set metric 5",
            "set policy route-map test3 rule 1 set metric-type type-1",
            "set policy route-map test3 rule 1 set origin egp",
            "set policy route-map test3 rule 1 set originator-id 10.0.2.3",
            "set policy route-map test3 rule 1 set src 10.0.2.15",
            "set policy route-map test3 rule 1 set tag 5",
            "set policy route-map test3 rule 1 set weight 4",
            "set policy route-map test3 rule 1 set community replace internet",
            "set policy route-map test3 rule 1 match interface eth2",
            "set policy route-map test3 rule 1 match metric 1",
            "set policy route-map test3 rule 1 match peer 1.1.1.2",
            "set policy route-map test3 rule 1 match ipv6 nexthop fdda:5cc1:23:4::1f",
            "set policy route-map test3 rule 1 match rpki invalid",
            "set policy route-map test1 rule 1 description test",
            "set policy route-map test1 rule 1 action permit",
            "set policy route-map test1 rule 1 on-match next",
            "set policy route-map test1 rule 2 action permit",
            "set policy route-map test1 rule 2 on-match goto 4",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )

    def test_yos_route_maps_parsed(self):
        parsed_str = (
            "set policy route-map test3 rule 1 action 'permit'"
            "\nset policy route-map test3 rule 1 match interface 'eth2'\nset policy route-map test3 rule 1 match ipv6 nexthop"
            " 'fdda:5cc1:23:4::1f'\nset policy route-map test3 rule 1 match metric '1'\nset policy route-map test3 rule 1 match peer "
            "'1.1.1.2'\nset policy route-map test3 rule 1 match rpki 'invalid'\nset policy route-map test3 rule 1 set bgp-extcommunity-rt "
            "'22:11'\nset policy route-map test3 rule 1 set community replace 'internet'\nset policy route-map test3 rule 1 set ipv6-next-hop global"
            " 'fdda:5cc1:23:4::1f'\nset policy route-map test3 rule 1 set ip-next-hop '10.20.10.20'\nset policy route-map "
            "test3 rule 1 set local-preference '4'\nset policy route-map test3 rule 1 set metric '5'\nset policy route-map test3 "
            "rule 1 set metric-type 'type-1'\nset policy route-map test3 rule 1 set origin 'egp'\nset policy route-map test3 rule 1 set originator-id "
            "'10.0.2.3'\nset policy route-map test3 rule 1 set src '10.0.2.15'"
            "\nset policy route-map test3 rule 1 set tag '5'\nset policy route-map test3 rule 1 set weight '4'"
        )
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "entries": [
                    {
                        "action": "permit",
                        "match": {
                            "interface": "eth2",
                            "ipv6": {"next_hop": "fdda:5cc1:23:4::1f"},
                            "metric": 1,
                            "peer": "1.1.1.2",
                            "rpki": "invalid",
                        },
                        "sequence": 1,
                        "set": {
                            "bgp_extcommunity_rt": "22:11",
                            "community": {"value": "internet"},
                            "ip_next_hop": "10.20.10.20",
                            "ipv6_next_hop": {
                                "ip_type": "global",
                                "value": "fdda:5cc1:23:4::1f",
                            },
                            "local_preference": "4",
                            "metric": "5",
                            "metric_type": "type-1",
                            "origin": "egp",
                            "originator_id": "10.0.2.3",
                            "src": "10.0.2.15",
                            "tag": "5",
                            "weight": "4",
                        },
                    },
                ],
                "route_map": "test3",
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_vyos_route_maps_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered_list = [
            {
                "entries": [
                    {
                        "action": "permit",
                        "match": {
                            "interface": "eth2",
                            "ipv6": {"next_hop": "fdda:5cc1:23:4::1f"},
                            "metric": 1,
                            "peer": "1.1.1.2",
                            "rpki": "invalid",
                        },
                        "sequence": 1,
                        "set": {
                            "bgp_extcommunity_rt": "22:11",
                            "community": {"value": "internet"},
                            "ip_next_hop": "10.20.10.20",
                            "ipv6_next_hop": {
                                "ip_type": "global",
                                "value": "fdda:5cc1:23:4::1f",
                            },
                            "local_preference": "4",
                            "metric": "5",
                            "metric_type": "type-1",
                            "origin": "egp",
                            "originator_id": "10.0.2.3",
                            "src": "10.0.2.15",
                            "tag": "5",
                            "weight": "4",
                        },
                    },
                ],
                "route_map": "test3",
            },
        ]
        self.assertEqual(gathered_list, result["gathered"])

    def test_vyos_route_maps_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        route_map="test3",
                        entries=[
                            dict(
                                sequence=1,
                                action="permit",
                                match=dict(
                                    rpki="invalid",
                                    interface="eth2",
                                ),
                                set=dict(
                                    origin="egp",
                                    originator_id="10.0.2.3",
                                    src="10.0.2.15",
                                    tag=5,
                                    weight=4,
                                ),
                            ),
                        ],
                    ),
                ],
                state="deleted",
            ),
        )
        commands = ["delete policy route-map test3"]
        self.execute_module(changed=True, commands=commands)
