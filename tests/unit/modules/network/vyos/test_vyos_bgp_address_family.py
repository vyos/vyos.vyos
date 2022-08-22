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
from ansible_collections.vyos.vyos.plugins.modules import (
    vyos_bgp_address_family,
)
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    set_module_args,
)
from .vyos_module import TestVyosModule, load_fixture


class TestVyosBgpafModule(TestVyosModule):

    module = vyos_bgp_address_family

    def setUp(self):
        super(TestVyosBgpafModule, self).setUp()
        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts."
            + "bgp_address_family.bgp_address_family.Bgp_address_familyFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosBgpafModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_bgp_address_family_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_bgp_address_family_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            aggregate_address=[
                                dict(prefix="192.0.2.0/24", as_set=True)
                            ],
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                                dict(prefix="192.2.13.0/24", backdoor=True),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ripng", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.0.2.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="export", route_map="map01"
                                        )
                                    ],
                                    soft_reconfiguration=True,
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                            address_family=[
                                dict(
                                    afi="ipv6",
                                    attribute_unchanged=dict(next_hop=True),
                                )
                            ],
                        ),
                    ],
                )
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_bgp_address_family_merged(self):
        set_module_args(
            dict(
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            aggregate_address=[
                                dict(prefix="192.0.2.0/24", summary_only=True)
                            ],
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ospfv3", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.10.21.25",
                            address_family=[
                                dict(
                                    afi="ipv6",
                                    distribute_list=[
                                        dict(action="export", acl=10)
                                    ],
                                    route_server_client=True,
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    filter_list=[
                                        dict(
                                            action="export", path_list="list01"
                                        ),
                                    ],
                                    capability=dict(orf="send"),
                                )
                            ],
                        ),
                    ],
                )
            )
        )
        commands = [
            "set protocols bgp 65536 address-family ipv4-unicast aggregate-address 192.0.2.0/24 as-setipv4-unicast aggregate-address 192.0.2.0/24 summary-only",
            "set protocols bgp 65536 address-family ipv6-unicast redistribute ospfv3 metric 20",
            "set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv4-unicast filter-list export list01",
            "set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv4-unicast capability  prefix-list send",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv6-unicast distribute-list export 10",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv6-unicast route-server-client",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_bgp_address_family_replaced_idempotent(self):
        set_module_args(
            dict(
                state="replaced",
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            aggregate_address=[
                                dict(prefix="192.0.2.0/24", as_set=True)
                            ],
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                                dict(prefix="192.2.13.0/24", backdoor=True),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ripng", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.0.2.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="export", route_map="map01"
                                        )
                                    ],
                                    soft_reconfiguration=True,
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                            address_family=[
                                dict(
                                    afi="ipv6",
                                    attribute_unchanged=dict(next_hop=True),
                                )
                            ],
                        ),
                    ],
                ),
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_bgp_address_family_replaced(self):
        set_module_args(
            dict(
                state="replaced",
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            aggregate_address=[
                                dict(prefix="192.0.2.0/24", summary_only=True)
                            ],
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ospfv3", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.10.21.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="import", route_map="map01"
                                        )
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    distribute_list=[
                                        dict(action="export", acl=10)
                                    ],
                                    route_server_client=True,
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="192.0.2.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="export", route_map="map01"
                                        )
                                    ],
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    filter_list=[
                                        dict(
                                            action="export", path_list="list01"
                                        ),
                                    ],
                                    capability=dict(orf="send"),
                                )
                            ],
                        ),
                    ],
                ),
            )
        )
        commands = [
            "delete protocols bgp 65536 neighbor 203.0.113.5 address-family ipv6-unicast attribute-unchanged",
            "delete protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast soft-reconfiguration",
            "delete protocols bgp 65536 address-family ipv6-unicast redistribute ripng",
            "delete protocols bgp 65536 address-family ipv4-unicast network 192.2.13.0/24",
            "set protocols bgp 65536 address-family ipv4-unicast aggregate-address 192.0.2.0/24 summary-only",
            "set protocols bgp 65536 address-family ipv6-unicast redistribute ospfv3 metric 20",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv4-unicast route-map import map01",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv6-unicast distribute-list export 10",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv6-unicast route-server-client",
            "set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv4-unicast filter-list export list01",
            "set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv4-unicast capability  prefix-list send",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_bgp_address_family_overridden_idempotent(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            aggregate_address=[
                                dict(prefix="192.0.2.0/24", as_set=True)
                            ],
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                                dict(prefix="192.2.13.0/24", backdoor=True),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ripng", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.0.2.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="export", route_map="map01"
                                        )
                                    ],
                                    soft_reconfiguration=True,
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                            address_family=[
                                dict(
                                    afi="ipv6",
                                    attribute_unchanged=dict(next_hop=True),
                                )
                            ],
                        ),
                    ],
                ),
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_bgp_address_family_overridden(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ospfv3", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.10.21.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="import", route_map="map01"
                                        )
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    distribute_list=[
                                        dict(action="export", acl=10)
                                    ],
                                    route_server_client=True,
                                ),
                            ],
                        ),
                    ],
                ),
            )
        )
        commands = [
            "delete protocols bgp 65536 neighbor 203.0.113.5 address-family",
            "delete protocols bgp 65536 neighbor 192.0.2.25 address-family",
            "delete protocols bgp 65536 address-family ipv6-unicast redistribute ripng",
            "delete protocols bgp 65536 address-family ipv4 aggregate-address",
            "delete protocols bgp 65536 address-family ipv4-unicast network 192.2.13.0/24",
            "set protocols bgp 65536 address-family ipv6-unicast redistribute ospfv3 metric 20",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv4-unicast route-map import map01",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv6-unicast distribute-list export 10",
            "set protocols bgp 65536 neighbor 192.10.21.25 address-family ipv6-unicast route-server-client",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_bgp_address_family_deleted(self):
        set_module_args(
            dict(
                state="deleted",
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.0.2.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                        ),
                    ],
                ),
            )
        )
        commands = [
            "delete protocols bgp 65536 address-family ipv4-unicast",
            "delete protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast",
            "delete protocols bgp 65536 neighbor 203.0.113.5 address-family",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_vyos_bgp_address_family_incorrect_instance(self):
        set_module_args(
            dict(
                state="overridden",
                config=dict(
                    as_number=100,
                    address_family=[
                        dict(
                            afi="ipv4",
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ospfv3", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.10.21.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="import", route_map="map01"
                                        )
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    distribute_list=[
                                        dict(action="export", acl=10)
                                    ],
                                    route_server_client=True,
                                ),
                            ],
                        ),
                    ],
                ),
            )
        )
        result = self.execute_module(failed=True)
        self.assertIn(
            "Only one bgp instance is allowed per device", result["msg"]
        )

    def test_vyos_bgp_address_family_rendered(self):
        set_module_args(
            dict(
                state="rendered",
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(
                            afi="ipv4",
                            aggregate_address=[
                                dict(prefix="192.0.2.0/24", as_set=True)
                            ],
                            networks=[
                                dict(
                                    prefix="192.1.13.0/24", route_map="map01"
                                ),
                                dict(prefix="192.2.13.0/24", backdoor=True),
                            ],
                        ),
                        dict(
                            afi="ipv6",
                            redistribute=[dict(protocol="ripng", metric=20)],
                        ),
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="192.0.2.25",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    route_map=[
                                        dict(
                                            action="export", route_map="map01"
                                        )
                                    ],
                                    soft_reconfiguration=True,
                                ),
                            ],
                        ),
                        dict(
                            neighbor_address="203.0.113.5",
                            address_family=[
                                dict(
                                    afi="ipv6",
                                    attribute_unchanged=dict(next_hop=True),
                                )
                            ],
                        ),
                    ],
                ),
            )
        )

        rendered_cmds = [
            "set protocols bgp 65536 address-family ipv4-unicast network 192.1.13.0/24 route-map map01",
            "set protocols bgp 65536 address-family ipv4-unicast network 192.2.13.0/24 backdoor",
            "set protocols bgp 65536 address-family ipv4-unicast aggregate-address 192.0.2.0/24 as-set",
            "set protocols bgp 65536 address-family ipv6-unicast redistribute ripng metric 20",
            "set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast route-map export map01",
            "set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast soft-reconfiguration inbound",
            "set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv6-unicast attribute-unchanged next-hop",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
            result["rendered"],
        )

    def test_vyos_bgp_address_family_parsed(self):
        commands = [
            "set protocols bgp 65536 address-family ipv4-unicast network 192.1.13.0/24 route-map map01",
            "set protocols bgp 65536 address-family ipv4-unicast network 192.2.13.0/24 backdoor",
            "set protocols bgp 65536 address-family ipv4-unicast aggregate-address 192.0.2.0/24 as-set",
            "set protocols bgp 65536 address-family ipv6-unicast redistribute ripng metric 20",
            "set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast route-map export map01",
            "set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast soft-reconfiguration inbound",
            "set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv6-unicast attribute-unchanged next-hop",
        ]

        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": 65536,
            "address_family": [
                {
                    "afi": "ipv4",
                    "networks": [
                        {"prefix": "192.1.13.0/24", "route_map": "map01"},
                        {"prefix": "192.2.13.0/24", "backdoor": True},
                    ],
                    "aggregate_address": [
                        {"prefix": "192.0.2.0/24", "as_set": True}
                    ],
                },
                {
                    "afi": "ipv6",
                    "redistribute": [{"protocol": "ripng", "metric": 20}],
                },
            ],
            "neighbors": [
                {
                    "neighbor_address": "192.0.2.25",
                    "address_family": [
                        {"afi": "ipv4", "soft_reconfiguration": True},
                    ],
                },
                {
                    "neighbor_address": "203.0.113.5",
                    "address_family": [
                        {
                            "afi": "ipv6",
                            "attribute_unchanged": {"next_hop": True},
                        }
                    ],
                },
            ],
        }
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_vyos_bgp_address_family_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = {
            "as_number": 65536,
            "address_family": [
                {
                    "afi": "ipv4",
                    "networks": [
                        {"prefix": "192.1.13.0/24", "route_map": "map01"},
                        {"prefix": "192.2.13.0/24", "backdoor": True},
                    ],
                    "aggregate_address": [
                        {"prefix": "192.0.2.0/24", "as_set": True}
                    ],
                },
                {
                    "afi": "ipv6",
                    "redistribute": [{"protocol": "ripng", "metric": 20}],
                },
            ],
            "neighbors": [
                {
                    "neighbor_address": "192.0.2.25",
                    "address_family": [
                        {"afi": "ipv4", "soft_reconfiguration": True},
                    ],
                },
                {
                    "neighbor_address": "203.0.113.5",
                    "address_family": [
                        {
                            "afi": "ipv6",
                            "attribute_unchanged": {"next_hop": True},
                        }
                    ],
                },
            ],
        }
        self.assertEqual(sorted(gather_list), sorted(result["gathered"]))
