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

from ansible_collections.vyos.vyos.plugins.modules import vyos_vrf
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosVrfModule(TestVyosModule):
    module = vyos_vrf

    def setUp(self):
        super(TestVyosVrfModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.vrf.vrf.VrfFacts.get_config",
        )

        self.execute_show_command = self.mock_execute_show_command.start()

        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vrf.vrf.get_os_version",
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "1.5"
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosVrfModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_vrf_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

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
                                        dict(rm_name="rm1", protocol="kernel"),
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
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vrf_merged(self):
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=True,
                    instances=[
                        dict(
                            name="vrf-green",
                            description="green-vrf",
                            table_id=110,
                            vni=1010,
                        ),
                    ],
                ),
                state="merged",
            ),
        )

        commands = [
            "set vrf name vrf-green table 110",
            "set vrf name vrf-green vni 1010",
            "set vrf name vrf-green description green-vrf",
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
                                        dict(rm_name="rm1", protocol="kernel"),
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
        commands = [
            "set vrf name vrf-blue description blue-vrf-replaced",
            "set vrf name vrf-blue disable",
            "delete vrf name vrf-red ip disable-forwarding",
            "set vrf name vrf-red ipv6 nht no-resolve-via-default",
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
                                        dict(rm_name="rm1", protocol="kernel"),
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
                    ],
                ),
                state="overridden",
            ),
        )
        commands = [
            "delete vrf name vrf-blue",
            "commit",
            "set vrf name vrf-blue table 103",
            "set vrf name vrf-blue vni 1002",
            "set vrf name vrf-blue description blue-vrf",
            "set vrf name vrf-blue disable",
            "delete vrf bind-to-all",
        ]
        self.execute_module(changed=True, commands=commands)

    # def test_vrf_overridden_idempotent(self):
    #     set_module_args(
    #         dict(
    #             config=dict(
    #                 bind_to_all=True,
    #                 instances=[
    #                     dict(
    #                         name="vrf-blue",
    #                         description="blue-vrf",
    #                         disable=False,
    #                         table_id=100,
    #                         vni=1000,
    #                     ),
    #                     dict(
    #                         name="vrf-red",
    #                         description="red-vrf",
    #                         disable=True,
    #                         table_id=101,
    #                         vni=1001,
    #                         address_family=[
    #                             dict(
    #                                 afi="ipv4",
    #                                 disable_forwarding=True,
    #                                 route_maps=[
    #                                     dict(rm_name="rm1", protocol="kernel"),
    #                                     dict(rm_name="rm1", protocol="rip"),
    #                                 ],
    #                             ),
    #                             dict(
    #                                 afi="ipv6",
    #                                 nht_no_resolve_via_default=False,
    #                             ),
    #                         ],
    #                     ),
    #                 ],
    #             ),
    #             state="overridden",
    #         ),
    #     )
    #     self.execute_module(changed=False, commands=[])

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
                                        dict(rm_name="rm1", protocol="kernel"),
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
            "set vrf name vrf-amber ip protocol kernel route-map rm1",
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
            "set vrf name vrf-red ip protocol kernel route-map 'rm1'",
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
                                    "protocol": "kernel",
                                    "rm_name": "rm1",
                                },
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
                                {
                                    "protocol": "kernel",
                                    "rm_name": "rm1",
                                },
                                {
                                    "protocol": "rip",
                                    "rm_name": "rm1",
                                },
                            ],
                        },
                    ],
                    "description": "red-vrf",
                    "disable": True,
                    "name": "vrf-red",
                    "table_id": 101,
                    "vni": 1001,
                },
            ],
        }
        self.assertEqual(gathered_list, result["gathered"])

    def test_vrf_deleted(self):
        # Delete the instances and global setting bind_to_all
        set_module_args(
            dict(
                config=dict(
                    bind_to_all=False,
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

    # def test_vrf__all_deleted(self):
    #     set_module_args(
    #         dict(
    #             config=dict({}),
    #             state="deleted",
    #         ),
    #     )
    #     commands = [
    #         "delete vrf",
    #     ]
    #     self.execute_module(changed=True, commands=commands)
