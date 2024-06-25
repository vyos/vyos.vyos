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

from ansible_collections.vyos.vyos.plugins.modules import vyos_ntp_global
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosNTPModule(TestVyosModule):
    module = vyos_ntp_global

    def setUp(self):
        super(TestVyosNTPModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.ntp_global.ntp_global.Ntp_globalFacts.get_config",
        )

        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosNTPModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_ntp_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_ntp_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.1.1.0/24", "10.1.2.0/24"],
                    listen_addresses=["10.2.3.1", "10.4.3.1"],
                    servers=[
                        dict(server="server1"),
                        dict(server="server3", options=["noselect", "dynamic"]),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_ntp_merged(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.2.2.0/24", "10.3.3.0/24"],
                    listen_addresses=["10.3.4.1", "10.4.5.1"],
                    servers=[
                        dict(server="server4", options=["dynamic", "preempt"]),
                        dict(
                            server="server5",
                            options=[
                                "noselect",
                                "pool",
                                "preempt",
                                "prefer",
                            ],
                        ),
                    ],
                ),
                state="merged",
            ),
        )

        commands = [
            "set system ntp allow-clients address 10.2.2.0/24",
            "set system ntp allow-clients address 10.3.3.0/24",
            "set system ntp listen-address 10.3.4.1",
            "set system ntp listen-address 10.4.5.1",
            "set system ntp server server4 dynamic",
            "set system ntp server server4 preempt",
            "set system ntp server server5 pool",
            "set system ntp server server5 noselect",
            "set system ntp server server5 preempt",
            "set system ntp server server5 prefer",
        ]

        self.execute_module(changed=True, commands=commands)

    def test_ntp_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.3.4.0/24", "10.4.5.0/24"],
                    listen_addresses=["10.3.3.1", "10.4.4.1"],
                    servers=[
                        dict(server="server4", options=["noselect", "prefer"]),
                        dict(
                            server="server6",
                            options=[
                                "noselect",
                                "dynamic",
                                "prefer",
                                "preempt",
                            ],
                        ),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="replaced",
            ),
        )
        commands = [
            "delete system ntp allow-clients address 10.1.1.0/24",
            "delete system ntp allow-clients address 10.1.2.0/24",
            "delete system ntp listen-address 10.2.3.1",
            "delete system ntp listen-address 10.4.3.1",
            "delete system ntp server server1",
            "delete system ntp server server3",
            "set system ntp allow-clients address 10.3.4.0/24",
            "set system ntp allow-clients address 10.4.5.0/24",
            "set system ntp listen-address 10.3.3.1",
            "set system ntp listen-address 10.4.4.1",
            "set system ntp server server4 noselect",
            "set system ntp server server4 prefer",
            "set system ntp server server6 noselect",
            "set system ntp server server6 dynamic",
            "set system ntp server server6 prefer",
            "set system ntp server server6 preempt",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_ntp_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.1.1.0/24", "10.1.2.0/24"],
                    listen_addresses=["10.2.3.1", "10.4.3.1"],
                    servers=[
                        dict(server="server1"),
                        dict(server="server3", options=["noselect", "dynamic"]),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_ntp_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.9.9.0/24"],
                    listen_addresses=["10.9.9.1"],
                    servers=[
                        dict(server="server9"),
                        dict(server="server6", options=["noselect", "dynamic"]),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="overridden",
            ),
        )
        commands = [
            "delete system ntp allow-clients address 10.1.1.0/24",
            "delete system ntp allow-clients address 10.1.2.0/24",
            "delete system ntp listen-address 10.2.3.1",
            "delete system ntp listen-address 10.4.3.1",
            "delete system ntp server server1",
            "delete system ntp server server3",
            "set system ntp allow-clients address 10.9.9.0/24",
            "set system ntp listen-address 10.9.9.1",
            "set system ntp server server9",
            "set system ntp server server6 noselect",
            "set system ntp server server6 dynamic",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_ntp_overridden_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.1.1.0/24", "10.1.2.0/24"],
                    listen_addresses=["10.2.3.1", "10.4.3.1"],
                    servers=[
                        dict(server="server1"),
                        dict(server="server3", options=["noselect", "dynamic"]),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_ntp_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.7.7.0/24", "10.8.8.0/24"],
                    listen_addresses=["10.7.9.1"],
                    servers=[
                        dict(server="server79"),
                        dict(server="server46", options=["noselect", "dynamic"]),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="rendered",
            ),
        )
        rendered_commands = [
            "set system ntp allow-clients address 10.7.7.0/24",
            "set system ntp allow-clients address 10.8.8.0/24",
            "set system ntp listen-address 10.7.9.1",
            "set system ntp server server79",
            "set system ntp server server46 noselect",
            "set system ntp server server46 dynamic",
            "set system ntp server time1.vyos.net",
            "set system ntp server time2.vyos.net",
            "set system ntp server time3.vyos.net",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_commands),
            result["rendered"],
        )

    def test_ntp_parsed(self):
        commands = (
            "set system ntp allow-clients address 10.7.7.0/24",
            "set system ntp allow-clients address 10.6.7.0/24",
            "set system ntp listen-address 10.7.9.1",
            "set system ntp listen-address 10.7.7.1",
            "set system ntp server check",
            "set system ntp server server46 noselect",
            "set system ntp server server46 prefer",
            "set system ntp server time1.vyos.net",
            "set system ntp server time2.vyos.net",
            "set system ntp server time3.vyos.net",
        )
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "allow_clients": ["10.6.7.0/24", "10.7.7.0/24"],
            "listen_addresses": ["10.7.7.1", "10.7.9.1"],
            "servers": [
                {"server": "check"},
                {"server": "server46", "options": ["noselect", "prefer"]},
                {"server": "time1.vyos.net"},
                {"server": "time2.vyos.net"},
                {"server": "time3.vyos.net"},
            ],
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_ntp_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered_list = {
            "allow_clients": ["10.1.1.0/24", "10.1.2.0/24"],
            "listen_addresses": ["10.2.3.1", "10.4.3.1"],
            "servers": [
                {"server": "server1"},
                {"server": "server3", "options": ["dynamic", "noselect"]},
                {"server": "time1.vyos.net"},
                {"server": "time2.vyos.net"},
                {"server": "time3.vyos.net"},
            ],
        }

        self.assertEqual(gathered_list, result["gathered"])

    def test_ntp_deleted(self):
        set_module_args(
            dict(
                config=dict(
                    allow_clients=["10.1.1.0/24"],
                    listen_addresses=["10.2.3.1"],
                    servers=[
                        dict(server="server1"),
                        dict(server="server3", options=["noselect"]),
                        dict(server="time1.vyos.net"),
                        dict(server="time2.vyos.net"),
                        dict(server="time3.vyos.net"),
                    ],
                ),
                state="deleted",
            ),
        )
        commands = [
            "delete system ntp allow-clients",
            "delete system ntp listen-address",
            "delete system ntp server server1",
            "delete system ntp server server3",
            "delete system ntp server time1.vyos.net",
            "delete system ntp server time2.vyos.net",
            "delete system ntp server time3.vyos.net",
        ]
        self.execute_module(changed=True, commands=commands)
