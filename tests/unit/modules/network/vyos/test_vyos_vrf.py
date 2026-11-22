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


from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import MagicMock, patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_vrf
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosVrfModule(TestVyosModule):
    module = vyos_vrf

    def setUp(self):
        super(TestVyosVrfModule, self).setUp()

        self.fake_connection = MagicMock()
        self.fake_connection.get.return_value = "{}"

        self.fake_connection.get_device_info.return_value = {
            "version": "1.5",
        }

        self.fake_connection.get_device_info.return_value = {
            "network_os_major_version": "1.5",
        }
        patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos.get_connection",
            return_value=self.fake_connection,
        ).start()

        def _get_resource_connection_side_effect(module, *args, **kwargs):
            module._connection = self.fake_connection
            return self.fake_connection

        patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
            side_effect=_get_resource_connection_side_effect,
        ).start()

        patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
            side_effect=_get_resource_connection_side_effect,
        ).start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.vrf.vrf.VrfFacts.get_config",
        ).start()

        patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vrf.vrf.get_os_version",
            return_value="1.5",
        ).start()

        patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.bgp_global.bgp_global.get_os_version",
            return_value="1.5",
        ).start()

        self.maxDiff = None

    def tearDown(self):
        super(TestVyosVrfModule, self).tearDown()
        patch.stopall()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_vrf_config.cfg"

        def load_from_file(*args, **kwargs):
            return load_fixture(filename)

        self.mock_execute_show_command.side_effect = load_from_file

    def test_vrf_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-blue",
                            description="blue-vrf",
                            disable=False,
                            table_id=100,
                            vni=1000,
                        ),
                        dict(
                            name="vrf-red",
                            description="red-vrf",
                            disable=True,
                            table_id=101,
                            vni=1001,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    disable_forwarding=True,
                                    route_maps=[
                                        dict(rm_name="rm1", protocol="rip"),
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    nht_no_resolve_via_default=True,
                                ),
                            ],
                            protocols=dict(
                                bgp=dict(
                                    as_number=65000,
                                    neighbor=[
                                        dict(
                                            address="192.0.2.1",
                                            remote_as=65002,
                                        ),
                                        dict(
                                            address="1.1.1.3",
                                            remote_as=400,
                                            passive=True,
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )

        self.execute_module(changed=False, commands=[])

    def test_vrf_merged(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=False,
                    instances=[
                        dict(
                            name="vrf-green",
                            description="green-vrf",
                            table_id=110,
                            vni=1010,
                            protocols=dict(
                                ospf=dict(
                                    log_adjacency_changes="detail",
                                    max_metric=dict(
                                        router_lsa=dict(
                                            administrative=True,
                                            on_shutdown=10,
                                            on_startup=10,
                                        ),
                                    ),
                                    default_information=dict(
                                        originate=dict(
                                            always=True,
                                            metric=10,
                                            metric_type=2,
                                        ),
                                    ),
                                    auto_cost=dict(
                                        reference_bandwidth=2,
                                    ),
                                    neighbor=[
                                        dict(
                                            neighbor_id="192.0.11.12",
                                            poll_interval=10,
                                            priority=2,
                                        ),
                                    ],
                                    redistribute=[
                                        dict(
                                            route_type="bgp",
                                            metric=10,
                                            metric_type=2,
                                        ),
                                    ],
                                    parameters=dict(
                                        router_id="192.0.1.1",
                                        rfc1583_compatibility=True,
                                        abr_type="cisco",
                                    ),
                                    areas=[
                                        dict(
                                            area_id="2",
                                            area_type=dict(
                                                normal=True,
                                            ),
                                            authentication="plaintext-password",
                                            shortcut="enable",
                                        ),
                                        dict(
                                            area_id="3",
                                            area_type=dict(
                                                nssa=dict(
                                                    set=True,
                                                ),
                                            ),
                                        ),
                                        dict(
                                            area_id="4",
                                            area_type=dict(
                                                stub=dict(
                                                    default_cost=20,
                                                ),
                                            ),
                                            network=[
                                                dict(
                                                    address="192.0.2.0/24",
                                                ),
                                            ],
                                            range=[
                                                dict(
                                                    address="192.0.3.0/24",
                                                    cost=10,
                                                ),
                                                dict(
                                                    address="192.0.4.0/24",
                                                    cost=12,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )

        commands = [
            "delete vrf bind-to-all",
            "set vrf name vrf-green table 110",
            "set vrf name vrf-green vni 1010",
            "set vrf name vrf-green description green-vrf",
            "set vrf name vrf-green protocols ospf log-adjacency-changes 'detail'",
            "set vrf name vrf-green protocols ospf max-metric router-lsa administrative",
            "set vrf name vrf-green protocols ospf max-metric router-lsa on-shutdown 10",
            "set vrf name vrf-green protocols ospf max-metric router-lsa on-startup 10",
            "set vrf name vrf-green protocols ospf default-information originate always",
            "set vrf name vrf-green protocols ospf default-information originate metric 10",
            "set vrf name vrf-green protocols ospf default-information originate metric-type 2",
            "set vrf name vrf-green protocols ospf auto-cost reference-bandwidth '2'",
            "set vrf name vrf-green protocols ospf neighbor 192.0.11.12",
            "set vrf name vrf-green protocols ospf neighbor 192.0.11.12 poll-interval 10",
            "set vrf name vrf-green protocols ospf neighbor 192.0.11.12 priority 2",
            "set vrf name vrf-green protocols ospf redistribute bgp",
            "set vrf name vrf-green protocols ospf redistribute bgp metric 10",
            "set vrf name vrf-green protocols ospf redistribute bgp metric-type 2",
            "set vrf name vrf-green protocols ospf parameters router-id '192.0.1.1'",
            "set vrf name vrf-green protocols ospf parameters rfc1583-compatibility",
            "set vrf name vrf-green protocols ospf parameters abr-type 'cisco'",
            "set vrf name vrf-green protocols ospf area '2'",
            "set vrf name vrf-green protocols ospf area 2 area-type normal",
            "set vrf name vrf-green protocols ospf area 2 authentication plaintext-password",
            "set vrf name vrf-green protocols ospf area 2 shortcut enable",
            "set vrf name vrf-green protocols ospf area '3'",
            "set vrf name vrf-green protocols ospf area 3 area-type nssa",
            "set vrf name vrf-green protocols ospf area '4'",
            "set vrf name vrf-green protocols ospf area 4 area-type stub default-cost 20",
            "set vrf name vrf-green protocols ospf area 4 network 192.0.2.0/24",
            "set vrf name vrf-green protocols ospf area 4 range 192.0.3.0/24",
            "set vrf name vrf-green protocols ospf area 4 range 192.0.3.0/24 cost 10",
            "set vrf name vrf-green protocols ospf area 4 range 192.0.4.0/24",
            "set vrf name vrf-green protocols ospf area 4 range 192.0.4.0/24 cost 12",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_vrf_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-blue",
                            description="blue-vrf-replaced",
                            disable=True,
                            table_id=100,
                            vni=1000,
                        ),
                        dict(
                            name="vrf-red",
                            description="red-vrf",
                            disable=True,
                            table_id=101,
                            vni=1001,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    disable_forwarding=False,
                                    route_maps=[
                                        dict(rm_name="rm1", protocol="rip"),
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    nht_no_resolve_via_default=False,
                                ),
                            ],
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        commands = [
            "set vrf name vrf-blue description blue-vrf-replaced",
            "set vrf name vrf-blue disable",
            "delete vrf name vrf-red ip disable-forwarding",
            "delete vrf name vrf-red ipv6 nht no-resolve-via-default",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vrf_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-blue",
                            description="blue-vrf",
                            disable=False,
                            table_id=100,
                            vni=1000,
                        ),
                        dict(
                            name="vrf-red",
                            description="red-vrf",
                            disable=True,
                            table_id=101,
                            vni=1001,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    disable_forwarding=True,
                                    route_maps=[
                                        dict(rm_name="rm1", protocol="rip"),
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    nht_no_resolve_via_default=True,
                                ),
                            ],
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vrf_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    instances=[
                        dict(
                            name="vrf-blue",
                            description="blue-vrf",
                            disable=True,
                            table_id=103,
                            vni=1002,
                        ),
                        dict(
                            name="vrf-red",
                            description="red-vrf",
                            disable=True,
                            table_id=101,
                            vni=1001,
                            protocols=dict(
                                bgp=dict(
                                    as_number=65000,
                                    neighbor=[
                                        dict(
                                            address="192.0.2.1",
                                            remote_as=65003,
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        commands = [
            "delete vrf name vrf-blue",
            "commit",
            "delete vrf name vrf-red",
            "commit",
            "set vrf name vrf-blue table 103",
            "set vrf name vrf-blue vni 1002",
            "set vrf name vrf-blue description blue-vrf",
            "set vrf name vrf-blue disable",
            "set vrf name vrf-red table 101",
            "set vrf name vrf-red vni 1001",
            "set vrf name vrf-red description red-vrf",
            "set vrf name vrf-red disable",
            "set vrf name vrf-red protocols bgp system-as 65000",
            "set vrf name vrf-red protocols bgp neighbor 192.0.2.1 remote-as 65003",
            "delete vrf bind-to-all",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vrf_overridden_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-blue",
                            description="blue-vrf",
                            disable=False,
                            table_id=100,
                            vni=1000,
                        ),
                        dict(
                            name="vrf-red",
                            description="red-vrf",
                            disable=True,
                            table_id=101,
                            vni=1001,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    disable_forwarding=True,
                                    nht_no_resolve_via_default=False,
                                    route_maps=[
                                        dict(rm_name="rm1", protocol="rip"),
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    disable_forwarding=False,
                                    nht_no_resolve_via_default=True,
                                ),
                            ],
                            protocols=dict(
                                bgp=dict(
                                    as_number=65000,
                                    neighbor=[
                                        dict(
                                            address="192.0.2.1",
                                            remote_as=65002,
                                        ),
                                        dict(
                                            address="1.1.1.3",
                                            remote_as=400,
                                            passive=True,
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vrf_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-green",
                            description="green-vrf",
                            disabled=True,
                            table_id=105,
                            vni=1000,
                        ),
                        dict(
                            name="vrf-amber",
                            description="amber-vrf",
                            disable=False,
                            table_id=111,
                            vni=1001,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    disable_forwarding=True,
                                    route_maps=[
                                        dict(rm_name="rm1", protocol="ospf"),
                                    ],
                                ),
                                dict(
                                    afi="ipv6",
                                    nht_no_resolve_via_default=False,
                                ),
                            ],
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        rendered_commands = [
            "set vrf bind-to-all",
            "set vrf name vrf-green table 105",
            "set vrf name vrf-green vni 1000",
            "set vrf name vrf-green description green-vrf",
            "set vrf name vrf-green disable",
            "set vrf name vrf-amber table 111",
            "set vrf name vrf-amber vni 1001",
            "set vrf name vrf-amber description amber-vrf",
            "set vrf name vrf-amber ip protocol ospf route-map rm1",
            "set vrf name vrf-amber ip disable-forwarding",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_commands),
            result["rendered"],
        )

    def test_vrf_parsed(self):
        commands = (
            "set vrf bind-to-all",
            "set vrf name vrf1 description 'red'",
            "set vrf name vrf1 disable",
            "set vrf name vrf1 table 101",
            "set vrf name vrf1 vni 501",
            "set vrf name vrf2 description 'green'",
            "set vrf name vrf2 disable",
            "set vrf name vrf2 table 102",
            "set vrf name vrf2 vni 102",
            "set vrf name vrf1 ip disable-forwarding",
            "set vrf name vrf1 ip nht no-resolve-via-default",
            "set vrf name vrf-red ip protocol ospf route-map 'rm1'",
            "set vrf name vrf-red ipv6 nht no-resolve-via-default",
        )
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "bind_to_all": True,
            "instances": [
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": True,
                            "nht_no_resolve_via_default": True,
                        },
                    ],
                    "description": "red",
                    "disable": True,
                    "name": "vrf1",
                },
                {
                    "description": "green",
                    "disable": True,
                    "name": "vrf2",
                },
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": False,
                            "nht_no_resolve_via_default": False,
                            "route_maps": [
                                {
                                    "protocol": "ospf",
                                    "rm_name": "rm1",
                                },
                            ],
                        },
                        {
                            "afi": "ipv6",
                            "disable_forwarding": False,
                            "nht_no_resolve_via_default": True,
                        },
                    ],
                    "disable": False,
                    "name": "vrf-red",
                },
            ],
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_vrf_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered_list = {
            "bind_to_all": True,
            "instances": [
                {
                    "description": "blue-vrf",
                    "disable": False,
                    "name": "vrf-blue",
                    "table_id": 100,
                    "vni": 1000,
                },
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": True,
                            "nht_no_resolve_via_default": False,
                            "route_maps": [
                                {"protocol": "rip", "rm_name": "rm1"},
                            ],
                        },
                        {
                            "afi": "ipv6",
                            "disable_forwarding": False,
                            "nht_no_resolve_via_default": True,
                        },
                    ],
                    "description": "red-vrf",
                    "disable": True,
                    "name": "vrf-red",
                    "protocols": {
                        "bgp": {
                            "as_number": 65000,
                            "neighbor": [
                                {"address": "1.1.1.3", "passive": True, "remote_as": 400},
                                {"address": "192.0.2.1", "remote_as": 65002},
                            ],
                        },
                    },
                    "table_id": 101,
                    "vni": 1001,
                },
            ],
        }
        self.assertEqual(gathered_list, result["gathered"])

    def test_vrf_deleted(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-blue",
                        ),
                    ],
                ),
                state="deleted",
            ),
        )
        commands = [
            "delete vrf bind-to-all",
            "delete vrf name vrf-blue",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vrf_all_deleted(self):
        set_module_args(
            dict(
                state="deleted",
            ),
        )
        commands = [
            "delete vrf",
        ]
        self.execute_module(changed=True, commands=commands)
