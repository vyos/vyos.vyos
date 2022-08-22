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

from ansible_collections.vyos.vyos.tests.unit.compat.mock import patch
from ansible_collections.vyos.vyos.plugins.modules import vyos_snmp_server
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    set_module_args,
)
from .vyos_module import TestVyosModule, load_fixture


class TestVyosSnmpServerModule(TestVyosModule):

    module = vyos_snmp_server

    def setUp(self):
        super(TestVyosSnmpServerModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
        )
        self.get_resource_connection_facts = (
            self.mock_get_resource_connection_facts.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.snmp_server.snmp_server.Snmp_serverFacts.get_config"
        )

        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosSnmpServerModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_snmp_server_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_snmp_server_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="bridges",
                            networks=["12.1.1.0/24", "1.1.1.0/24"],
                        )
                    ],
                    listen_addresses=[
                        dict(address="100.1.2.1", port=33),
                    ],
                    location="RDU, NC",
                    snmp_v3=dict(
                        users=[
                            dict(
                                user="admin_user",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                            dict(
                                user="guest_user",
                                authentication=dict(
                                    type="sha", plaintext_key="opq1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="opq1234567"
                                ),
                            ),
                        ]
                    ),
                ),
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_snmp_server_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="bridges",
                            networks=["12.1.1.0/24", "1.1.1.0/24"],
                        )
                    ],
                    listen_addresses=[
                        dict(address="100.1.2.1", port=33),
                    ],
                    location="RDU, NC",
                    snmp_v3=dict(
                        users=[
                            dict(
                                user="admin_user",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                            dict(
                                user="guest_user",
                                authentication=dict(
                                    type="sha", plaintext_key="opq1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="opq1234567"
                                ),
                            ),
                        ]
                    ),
                ),
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_snmp_server_overridden_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="bridges",
                            networks=["12.1.1.0/24", "1.1.1.0/24"],
                        )
                    ],
                    listen_addresses=[
                        dict(address="100.1.2.1", port=33),
                    ],
                    location="RDU, NC",
                    snmp_v3=dict(
                        users=[
                            dict(
                                user="admin_user",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                            dict(
                                user="guest_user",
                                authentication=dict(
                                    type="sha", plaintext_key="opq1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="opq1234567"
                                ),
                            ),
                        ]
                    ),
                ),
                state="overridden",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_snmp_server_merged(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="routers",
                            clients=["12.1.1.0/24", "1.1.1.0/24"],
                            authorization_type="rw",
                        ),
                        dict(name="switches", authorization_type="ro"),
                    ],
                    contact="admin@example.com",
                    description="snmp_config",
                    smux_peer="peer1",
                    trap_source="1.1.1.1",
                    trap_target=dict(
                        address="10.10.1.1", community="switches", port="80"
                    ),
                    snmp_v3=dict(
                        engine_id="34",
                        groups=[
                            dict(
                                group="default",
                                mode="rw",
                                seclevel="priv",
                                view="view1",
                            )
                        ],
                        trap_targets=[
                            dict(
                                address="20.12.1.1",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                        ],
                    ),
                ),
                state="merged",
            )
        )
        commands = [
            "set service snmp community routers client 1.1.1.0/24",
            "set service snmp community routers client 12.1.1.0/24",
            "set service snmp community routers authorization rw",
            "set service snmp community switches authorization ro",
            "set service snmp v3 group default mode rw",
            "set service snmp v3 group default seclevel priv",
            "set service snmp v3 group default view view1",
            "set service snmp v3 engineid 34",
            "set service snmp contact admin@example.com",
            "set service snmp description snmp_config",
            "set service snmp smux-peer peer1",
            "set service snmp trap-source 1.1.1.1",
            "set service snmp trap-target 10.10.1.1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_snmp_server_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="routers",
                            clients=["12.1.1.0/24", "1.1.1.0/24"],
                            authorization_type="rw",
                        ),
                        dict(name="switches", authorization_type="ro"),
                    ],
                    contact="admin@example.com",
                    description="snmp_config",
                    smux_peer="peer1",
                    trap_source="1.1.1.1",
                    trap_target=dict(
                        address="10.10.1.1", community="switches", port="80"
                    ),
                    snmp_v3=dict(
                        engine_id="34",
                        groups=[
                            dict(
                                group="default",
                                mode="rw",
                                seclevel="priv",
                                view="view1",
                            )
                        ],
                        trap_targets=[
                            dict(
                                address="20.12.1.1",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                        ],
                    ),
                ),
                state="replaced",
            )
        )
        commands = [
            "set service snmp community routers client 1.1.1.0/24",
            "set service snmp community routers client 12.1.1.0/24",
            "set service snmp community routers authorization rw",
            "set service snmp community switches authorization ro",
            "delete service snmp community bridges network 1.1.1.0/24",
            "delete service snmp community bridges network 12.1.1.0/24",
            "delete service snmp listen-address 100.1.2.1 port 33",
            "set service snmp v3 group default mode rw",
            "set service snmp v3 group default seclevel priv",
            "set service snmp v3 group default view view1",
            "delete service snmp v3 user admin_user auth type sha",
            "delete service snmp v3 user admin_user auth plaintext-key abc1234567",
            "delete service snmp v3 user admin_user privacy type aes",
            "delete service snmp v3 user admin_user privacy plaintext-key abc1234567",
            "delete service snmp v3 user guest_user auth type sha",
            "delete service snmp v3 user guest_user auth plaintext-key opq1234567",
            "delete service snmp v3 user guest_user privacy type aes",
            "delete service snmp v3 user guest_user privacy plaintext-key opq1234567",
            "set service snmp v3 engineid 34",
            "set service snmp contact admin@example.com",
            "set service snmp description snmp_config",
            "set service snmp smux-peer peer1",
            "set service snmp trap-source 1.1.1.1",
            "set service snmp trap-target 10.10.1.1",
            "delete service snmp location 'RDU, NC'",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_snmp_server_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="routers",
                            clients=["12.1.1.0/24", "1.1.1.0/24"],
                            authorization_type="rw",
                        ),
                        dict(name="switches", authorization_type="ro"),
                    ],
                    contact="admin@example.com",
                    description="snmp_config",
                    smux_peer="peer1",
                    trap_source="1.1.1.1",
                    trap_target=dict(
                        address="10.10.1.1", community="switches", port="80"
                    ),
                    snmp_v3=dict(
                        engine_id="34",
                        groups=[
                            dict(
                                group="default",
                                mode="rw",
                                seclevel="priv",
                                view="view1",
                            )
                        ],
                        trap_targets=[
                            dict(
                                address="20.12.1.1",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                        ],
                    ),
                ),
                state="overridden",
            )
        )
        commands = [
            "set service snmp community routers client 1.1.1.0/24",
            "set service snmp community routers client 12.1.1.0/24",
            "set service snmp community routers authorization rw",
            "set service snmp community switches authorization ro",
            "delete service snmp community bridges network 1.1.1.0/24",
            "delete service snmp community bridges network 12.1.1.0/24",
            "delete service snmp listen-address 100.1.2.1 port 33",
            "set service snmp v3 group default mode rw",
            "set service snmp v3 group default seclevel priv",
            "set service snmp v3 group default view view1",
            "delete service snmp v3 user admin_user auth type sha",
            "delete service snmp v3 user admin_user auth plaintext-key abc1234567",
            "delete service snmp v3 user admin_user privacy type aes",
            "delete service snmp v3 user admin_user privacy plaintext-key abc1234567",
            "delete service snmp v3 user guest_user auth type sha",
            "delete service snmp v3 user guest_user auth plaintext-key opq1234567",
            "delete service snmp v3 user guest_user privacy type aes",
            "delete service snmp v3 user guest_user privacy plaintext-key opq1234567",
            "set service snmp v3 engineid 34",
            "set service snmp contact admin@example.com",
            "set service snmp description snmp_config",
            "set service snmp smux-peer peer1",
            "set service snmp trap-source 1.1.1.1",
            "set service snmp trap-target 10.10.1.1",
            "delete service snmp location 'RDU, NC'",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_snmp_server_deleted(self):
        set_module_args(
            dict(
                state="deleted",
            )
        )
        commands = ["delete service snmp"]
        self.execute_module(changed=True, commands=commands)

    def test_snmp_server_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    communities=[
                        dict(
                            name="routers",
                            clients=["12.1.1.0/24", "1.1.1.0/24"],
                            authorization_type="rw",
                        ),
                        dict(name="switches", authorization_type="ro"),
                    ],
                    contact="admin@example.com",
                    description="snmp_config",
                    smux_peer="peer1",
                    trap_source="1.1.1.1",
                    trap_target=dict(
                        address="10.10.1.1", community="switches", port="80"
                    ),
                    snmp_v3=dict(
                        engine_id="34",
                        groups=[
                            dict(
                                group="default",
                                mode="rw",
                                seclevel="priv",
                                view="view1",
                            )
                        ],
                        trap_targets=[
                            dict(
                                address="20.12.1.1",
                                authentication=dict(
                                    type="sha", plaintext_key="abc1234567"
                                ),
                                privacy=dict(
                                    type="aes", plaintext_key="abc1234567"
                                ),
                            ),
                        ],
                    ),
                ),
                state="rendered",
            )
        )
        commands = [
            "set service snmp community routers client 1.1.1.0/24",
            "set service snmp community routers client 12.1.1.0/24",
            "set service snmp community routers authorization rw",
            "set service snmp community switches authorization ro",
            "set service snmp v3 group default mode rw",
            "set service snmp v3 group default seclevel priv",
            "set service snmp v3 group default view view1",
            "set service snmp v3 engineid 34",
            "set service snmp contact admin@example.com",
            "set service snmp description snmp_config",
            "set service snmp smux-peer peer1",
            "set service snmp trap-source 1.1.1.1",
            "set service snmp trap-target 10.10.1.1",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"],
        )

    def test_snmp_server_parsed(self):
        commands = [
            "set service snmp community routers client 1.1.1.0/24",
            "set service snmp community routers client 12.1.1.0/24",
            "set service snmp community routers authorization rw",
            "set service snmp community switches authorization ro",
            "set service snmp v3 group default mode rw",
            "set service snmp v3 group default seclevel priv",
            "set service snmp v3 group default view view1",
            "set service snmp v3 engineid 34",
            "set service snmp contact admin@example.com",
            "set service snmp description snmp_config",
            "set service snmp smux-peer peer1",
            "set service snmp trap-source 1.1.1.1",
            "set service snmp trap-target 10.10.1.1",
        ]
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "communities": [
                {
                    "authorization_type": "rw",
                    "clients": ["1.1.1.0/24", "12.1.1.0/24"],
                    "name": "routers",
                },
                {"authorization_type": "ro", "name": "switches"},
            ],
            "contact": "admin@example.com",
            "description": "snmp_config",
            "smux_peer": "peer1",
            "snmp_v3": {
                "engine_id": "34",
                "groups": [
                    {
                        "group": "default",
                        "mode": "rw",
                        "seclevel": "priv",
                        "view": "view1",
                    }
                ],
            },
            "trap_source": "1.1.1.1",
            "trap_target": {"address": "10.10.1.1"},
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_snmp_server_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered_list = {
            "communities": [
                {"name": "bridges", "networks": ["1.1.1.0/24", "12.1.1.0/24"]},
            ],
            "listen_addresses": [{"address": "100.1.2.1", "port": 33}],
            "location": "RDU, NC",
            "snmp_v3": {
                "users": [
                    {
                        "authentication": {
                            "plaintext_key": "abc1234567",
                            "type": "sha",
                        },
                        "privacy": {
                            "plaintext_key": "abc1234567",
                            "type": "aes",
                        },
                        "user": "admin_user",
                    },
                    {
                        "authentication": {
                            "plaintext_key": "opq1234567",
                            "type": "sha",
                        },
                        "privacy": {
                            "plaintext_key": "opq1234567",
                            "type": "aes",
                        },
                        "user": "guest_user",
                    },
                ]
            },
        }
        self.assertEqual(gathered_list, result["gathered"])
