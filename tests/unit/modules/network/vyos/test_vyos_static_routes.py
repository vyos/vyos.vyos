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

from ansible_collections.vyos.vyos.plugins.modules import vyos_static_routes
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosStaticRoutesModule(TestVyosModule):
    module = vyos_static_routes

    def setUp(self):
        super(TestVyosStaticRoutesModule, self).setUp()
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
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.static_routes.static_routes.Static_routesFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.static_routes.static_routes.get_os_version",
        )
        self.test_version = "1.3"
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = self.test_version

    def tearDown(self):
        super(TestVyosStaticRoutesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("vyos_static_routes_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_static_routes_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        address_families=[
                            dict(
                                afi="ipv4",
                                routes=[
                                    dict(
                                        dest="192.0.2.48/28",
                                        next_hops=[
                                            dict(
                                                forward_router_address="192.0.2.9",
                                                admin_distance=10,
                                            ),
                                            dict(
                                                forward_router_address="192.0.2.10",
                                                interface="eth0",
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set protocols static route 192.0.2.48/28",
            "set protocols static route 192.0.2.48/28 next-hop '192.0.2.9'",
            "set protocols static route 192.0.2.48/28 next-hop 192.0.2.9 distance '10'",
            "set protocols static route 192.0.2.48/28 next-hop '192.0.2.10'",
            "set protocols static interface-route 192.0.2.48/28 next-hop-interface 'eth0'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_static_routes_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        address_families=[
                            dict(
                                afi="ipv4",
                                routes=[
                                    dict(
                                        dest="192.0.2.32/28",
                                        next_hops=[
                                            dict(forward_router_address="192.0.2.9"),
                                            dict(forward_router_address="192.0.2.10"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_static_routes_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        address_families=[
                            dict(
                                afi="ipv4",
                                routes=[
                                    dict(
                                        dest="192.0.2.48/28",
                                        next_hops=[
                                            dict(
                                                forward_router_address="192.0.2.9",
                                                interface="eth0",
                                            ),
                                            dict(
                                                forward_router_address="192.0.2.10",
                                                admin_distance=10,
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "set protocols static route 192.0.2.48/28",
            "set protocols static route 192.0.2.48/28 next-hop '192.0.2.9'",
            "set protocols static interface-route 192.0.2.48/28 next-hop-interface 'eth0'",
            "set protocols static route 192.0.2.48/28 next-hop '192.0.2.10'",
            "set protocols static route 192.0.2.48/28 next-hop 192.0.2.10 distance '10'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_static_routes_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        address_families=[
                            dict(
                                afi="ipv4",
                                routes=[
                                    dict(
                                        dest="192.0.2.32/28",
                                        next_hops=[
                                            dict(forward_router_address="192.0.2.9"),
                                            dict(forward_router_address="192.0.2.10"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )

        self.execute_module(changed=False, commands=[])

    def test_vyos_static_routes_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        address_families=[
                            dict(
                                afi="ipv4",
                                routes=[
                                    dict(
                                        dest="192.0.2.48/28",
                                        next_hops=[
                                            dict(forward_router_address="192.0.2.9"),
                                            dict(forward_router_address="192.0.2.10"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "delete protocols static route 192.0.2.32/28",
            "set protocols static route 192.0.2.48/28",
            "set protocols static route 192.0.2.48/28 next-hop '192.0.2.9'",
            "set protocols static route 192.0.2.48/28 next-hop '192.0.2.10'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_static_routes_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        address_families=[
                            dict(
                                afi="ipv4",
                                routes=[
                                    dict(
                                        dest="192.0.2.32/28",
                                        next_hops=[
                                            dict(forward_router_address="192.0.2.9"),
                                            dict(forward_router_address="192.0.2.10"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_static_routes_deleted(self):
        set_module_args(
            dict(
                config=[dict(address_families=[dict(afi="ipv4")])],
                state="deleted",
            ),
        )
        commands = ["delete protocols static route"]
        self.execute_module(changed=True, commands=commands)
