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

from ansible_collections.vyos.vyos.plugins.modules import vyos_vrrp
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosVrrpModule(TestVyosModule):
    module = vyos_vrrp

    def setUp(self):
        super(TestVyosVrrpModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.vrrp.vrrp.VrrpFacts.get_config",
        )

        self.execute_show_command = self.mock_execute_show_command.start()

        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vrrp.vrrp.get_os_version",
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "1.5"
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosVrrpModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_vrrp_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_vrrp_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    disable=True,
                    virtual_servers=[
                        dict(
                            address="10.10.10.1",
                            algorithm="round-robin",
                            delay_loop=60,
                            forward_method="direct",
                            fwmark=10,
                            name="s1",
                            persistence_timeout="30",
                            protocol="tcp",
                            real_server=[
                                dict(
                                    address="10.10.50.1",
                                    port=443,
                                    health_check_script="/var/tmp/script.sh",
                                ),
                            ],
                        ),
                        dict(
                            address="10.10.10.2",
                            name="s2",
                            port=81,
                            real_server=[
                                dict(
                                    address="real1",
                                    port=8081,
                                    connection_timeout=5,
                                ),
                                dict(
                                    address="real2",
                                    port=8080,
                                ),
                            ],
                        ),
                    ],
                    vrrp=dict(
                        global_parameters=dict(
                            garp=dict(
                                master_refresh=100,
                            ),
                            version="3",
                        ),
                        groups=[
                            dict(
                                authentication=dict(
                                    password="testpass",
                                    type="plaintext-password",
                                ),
                                address="1.1.1.1",
                                advertise_interval=10,
                                description="Group_1",
                                disable=True,
                                excluded_address=[
                                    "192.168.1.8",
                                    "192.168.1.7 interface eth3",
                                ],
                                garp=dict(
                                    interval=20,
                                    master_delay=5,
                                    master_refresh_repeat=100,
                                    master_repeat=3,
                                ),
                                health_check=dict(
                                    failure_count=3,
                                    interval=10,
                                    ping="192.168.1.5",
                                    script="script.sh",
                                ),
                                hello_source_address="192.168.1.2",
                                interface="eth2",
                                name="g1",
                                no_preempt=True,
                                peer_address="192.168.1.3",
                                priority=100,
                                rfc3768_compatibility=True,
                                track=dict(
                                    exclude_vrrp_interface=True,
                                    interface=["eth1"],
                                ),
                                transition_script=dict(
                                    backup="/var/tmp/script.sh",
                                    master="/var/tmp/script.sh",
                                    stop="/var/tmp/script.sh",
                                ),
                                vrid=20,
                            ),
                        ],
                        snmp="enabled",
                        sync_groups=[
                            dict(
                                health_check=dict(
                                    failure_count=3,
                                    interval=10,
                                ),
                                member=["g1"],
                                name="sg1",
                                transition_script=dict(
                                    backup="/var/tmp/script.sh",
                                    master="/var/tmp/script.sh",
                                    stop="/var/tmp/script.sh",
                                ),
                            ),
                        ],
                    ),
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vrrp_merged(self):
        set_module_args(
            dict(
                config=dict(
                    disable=True,
                    virtual_servers=[
                        dict(
                            name="s1",
                            address="10.10.10.5",
                            algorithm="round-robin",
                            real_server=[
                                dict(
                                    address="10.10.50.2",
                                    port=8443,
                                ),
                            ],
                        ),
                        dict(
                            name="s2",
                            address="10.10.10.2",
                            persistence_timeout=30,
                            port=81,
                            protocol="tcp",
                        ),
                        dict(
                            name="s3",
                            address="10.10.10.3",
                            port=88,
                            protocol="udp",
                        ),
                    ],
                    vrrp=dict(
                        snmp="disabled",
                        global_parameters=dict(
                            startup_delay=35,
                            garp=dict(
                                master_repeat=6,
                            ),
                        ),
                        groups=[
                            dict(
                                name="g1",
                                peer_address="192.168.1.3",
                                priority=100,
                                disable=False,
                                no_preempt=False,
                            ),
                        ],
                        sync_groups=[
                            dict(
                                name="sg1",
                                health_check=dict(
                                    failure_count=5,
                                ),
                            ),
                        ],
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "delete high-availability vrrp group g1 no-preempt",
            "delete high-availability vrrp group g1 disable",
            "delete high-availability vrrp group g1 rfc3768-compatibility",
            "delete high-availability vrrp snmp",
            "set high-availability virtual-server s1 address 10.10.10.5",
            "set high-availability virtual-server s1 real-server 10.10.50.2 port 8443",
            "set high-availability virtual-server s2 persistence-timeout 30",
            "set high-availability virtual-server s2 protocol tcp",
            "set high-availability virtual-server s3 address 10.10.10.3",
            "set high-availability virtual-server s3 port 88",
            "set high-availability virtual-server s3 protocol udp",
            "set high-availability vrrp global-parameters garp master-repeat 6",
            "set high-availability vrrp global-parameters startup-delay 35",
            "set high-availability vrrp sync-group sg1 health-check failure-count 5",
        ]

        self.execute_module(changed=True, commands=commands)

    # def test_ntp_replaced(self):
    #     set_module_args(
    #         dict(
    #             config=dict(
    #                 allow_clients=["10.3.4.0/24", "10.4.5.0/24"],
    #                 listen_addresses=["10.3.3.1", "10.4.4.1"],
    #                 servers=[
    #                     dict(server="server4", options=["noselect", "prefer"]),
    #                     dict(
    #                         server="server6",
    #                         options=[
    #                             "noselect",
    #                             "dynamic",
    #                             "prefer",
    #                             "preempt",
    #                         ],
    #                     ),
    #                     dict(server="time1.vyos.net"),
    #                     dict(server="time2.vyos.net"),
    #                     dict(server="time3.vyos.net"),
    #                 ],
    #             ),
    #             state="replaced",
    #         ),
    #     )
    #     commands = [
    #         "delete system ntp allow-clients address 10.1.1.0/24",
    #         "delete system ntp allow-clients address 10.1.2.0/24",
    #         "delete system ntp listen-address 10.2.3.1",
    #         "delete system ntp listen-address 10.4.3.1",
    #         "delete system ntp server server1",
    #         "delete system ntp server server3",
    #         "set system ntp allow-clients address 10.3.4.0/24",
    #         "set system ntp allow-clients address 10.4.5.0/24",
    #         "set system ntp listen-address 10.3.3.1",
    #         "set system ntp listen-address 10.4.4.1",
    #         "set system ntp server server4 noselect",
    #         "set system ntp server server4 prefer",
    #         "set system ntp server server6 noselect",
    #         "set system ntp server server6 dynamic",
    #         "set system ntp server server6 prefer",
    #         "set system ntp server server6 preempt",
    #     ]
    #     self.execute_module(changed=True, commands=commands)

    # def test_ntp_replaced_idempotent(self):
    #     set_module_args(
    #         dict(
    #             config=dict(
    #                 allow_clients=["10.1.1.0/24", "10.1.2.0/24"],
    #                 listen_addresses=["10.2.3.1", "10.4.3.1"],
    #                 servers=[
    #                     dict(server="server1"),
    #                     dict(server="server3", options=["noselect", "dynamic"]),
    #                     dict(server="time1.vyos.net"),
    #                     dict(server="time2.vyos.net"),
    #                     dict(server="time3.vyos.net"),
    #                 ],
    #             ),
    #             state="replaced",
    #         ),
    #     )
    #     self.execute_module(changed=False, commands=[])

    # def test_ntp_overridden(self):
    #     set_module_args(
    #         dict(
    #             config=dict(
    #                 allow_clients=["10.9.9.0/24"],
    #                 listen_addresses=["10.9.9.1"],
    #                 servers=[
    #                     dict(server="server9"),
    #                     dict(server="server6", options=["noselect", "dynamic"]),
    #                     dict(server="time1.vyos.net"),
    #                     dict(server="time2.vyos.net"),
    #                     dict(server="time3.vyos.net"),
    #                 ],
    #             ),
    #             state="overridden",
    #         ),
    #     )
    #     commands = [
    #         "delete system ntp allow-clients address 10.1.1.0/24",
    #         "delete system ntp allow-clients address 10.1.2.0/24",
    #         "delete system ntp listen-address 10.2.3.1",
    #         "delete system ntp listen-address 10.4.3.1",
    #         "delete system ntp server server1",
    #         "delete system ntp server server3",
    #         "set system ntp allow-clients address 10.9.9.0/24",
    #         "set system ntp listen-address 10.9.9.1",
    #         "set system ntp server server9",
    #         "set system ntp server server6 noselect",
    #         "set system ntp server server6 dynamic",
    #     ]
    #     self.execute_module(changed=True, commands=commands)

    # def test_ntp_overridden_idempotent(self):
    #     set_module_args(
    #         dict(
    #             config=dict(
    #                 allow_clients=["10.1.1.0/24", "10.1.2.0/24"],
    #                 listen_addresses=["10.2.3.1", "10.4.3.1"],
    #                 servers=[
    #                     dict(server="server1"),
    #                     dict(server="server3", options=["noselect", "dynamic"]),
    #                     dict(server="time1.vyos.net"),
    #                     dict(server="time2.vyos.net"),
    #                     dict(server="time3.vyos.net"),
    #                 ],
    #             ),
    #             state="overridden",
    #         ),
    #     )
    #     self.execute_module(changed=False, commands=[])

    def test_vrrp_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    virtual_servers=[
                        dict(
                            name="s1",
                            address="10.10.10.1",
                            algorithm="round-robin",
                            delay_loop=60,
                            forward_method="direct",
                            fwmark=10,
                            persistence_timeout=30,
                            protocol="tcp",
                            real_server=[
                                dict(
                                    address="10.10.50.1",
                                    health_check_script="/var/tmp/script.sh",
                                    port=443,
                                ),
                            ],
                        ),
                        dict(
                            name="s2",
                            address="10.10.10.2",
                            port=81,
                            real_server=[
                                dict(
                                    address="real1",
                                    connection_timeout=5,
                                    port=8081,
                                ),
                                dict(
                                    address="real2",
                                    port=8080,
                                ),
                            ],
                        ),
                    ],
                    vrrp=dict(
                        snmp="enabled",
                        global_parameters=dict(
                            startup_delay=31,
                            version="3",
                            garp=dict(
                                interval=30,
                                master_delay=10,
                                master_refresh=100,
                                master_refresh_repeat=200,
                                master_repeat=5,
                            ),
                        ),
                        groups=[
                            dict(
                                name="g1",
                                description="Group_1",
                                interface="eth2",
                                address="1.1.1.1",
                                advertise_interval=10,
                                peer_address="192.168.1.3",
                                priority=100,
                                disable=True,
                                no_preempt=True,
                                rfc3768_compatibility=True,
                                vrid=20,
                                excluded_address=[
                                    "192.168.1.7 interface eth3",
                                ],
                                garp=dict(
                                    interval=20,
                                    master_delay=5,
                                    master_refresh=50,
                                    master_refresh_repeat=100,
                                    master_repeat=3,
                                ),
                                authentication=dict(
                                    type="plaintext-password",
                                    password="testpass",
                                ),
                                transition_script=dict(
                                    master="/var/tmp/script.sh",
                                    backup="/var/tmp/script.sh",
                                    fault="/var/tmp/script.sh",
                                    stop="/var/tmp/script.sh",
                                ),
                                track=dict(
                                    exclude_vrrp_interface=True,
                                    interface=[
                                        "eth0",
                                    ],
                                ),
                            ),
                            dict(
                                name="g2",
                                description="Group_2",
                                interface="eth1",
                                address="2.2.2.2",
                                disable=False,
                                no_preempt=False,
                                rfc3768_compatibility=False,
                                vrid=11,
                                health_check=dict(
                                    failure_count=5,
                                    interval=15,
                                    ping="192.168.1.100",
                                    script="/var/tmp/script.sh",
                                ),
                                hello_source_address="2.2.2.2",
                            ),
                        ],
                        sync_groups=[
                            dict(
                                name="sg1",
                                member=[
                                    "g1",
                                ],
                                transition_script=dict(
                                    master="/var/tmp/script.sh",
                                    backup="/var/tmp/script.sh",
                                    fault="/var/tmp/script.sh",
                                    stop="/var/tmp/script.sh",
                                ),
                                health_check=dict(
                                    failure_count=3,
                                    interval=10,
                                    ping="192.168.2.100",
                                    script="/var/tmp/script.sh",
                                ),
                            ),
                        ],
                    ),
                ),
                state="rendered",
            ),
        )
        rendered_commands = [
            "set high-availability virtual-server s1 address 10.10.10.1",
            "set high-availability virtual-server s1 algorithm round-robin",
            "set high-availability virtual-server s1 delay-loop 60",
            "set high-availability virtual-server s1 forward-method direct",
            "set high-availability virtual-server s1 fwmark 10",
            "set high-availability virtual-server s1 persistence-timeout 30",
            "set high-availability virtual-server s1 protocol tcp",
            "set high-availability virtual-server s1 real-server 10.10.50.1 health-check script /var/tmp/script.sh",
            "set high-availability virtual-server s1 real-server 10.10.50.1 port 443",
            "set high-availability virtual-server s2 address 10.10.10.2",
            "set high-availability virtual-server s2 port 81",
            "set high-availability virtual-server s2 real-server real1 connection-timeout 5",
            "set high-availability virtual-server s2 real-server real1 port 8081",
            "set high-availability virtual-server s2 real-server real2 port 8080",
            "set high-availability vrrp global-parameters garp interval 30",
            "set high-availability vrrp global-parameters garp master-delay 10",
            "set high-availability vrrp global-parameters garp master-refresh 100",
            "set high-availability vrrp global-parameters garp master-refresh-repeat 200",
            "set high-availability vrrp global-parameters garp master-repeat 5",
            "set high-availability vrrp global-parameters startup-delay 31",
            "set high-availability vrrp global-parameters version 3",
            "set high-availability vrrp group g1 address 1.1.1.1",
            "set high-availability vrrp group g1 advertise-interval 10",
            "set high-availability vrrp group g1 authentication password testpass",
            "set high-availability vrrp group g1 authentication type plaintext-password",
            "set high-availability vrrp group g1 description 'Group_1'",
            "set high-availability vrrp group g1 disable",
            "set high-availability vrrp group g1 excluded-address 192.168.1.7 interface eth3",
            "set high-availability vrrp group g1 garp interval 20",
            "set high-availability vrrp group g1 garp master-delay 5",
            "set high-availability vrrp group g1 garp master-refresh 50",
            "set high-availability vrrp group g1 garp master-refresh-repeat 100",
            "set high-availability vrrp group g1 garp master-repeat 3",
            "set high-availability vrrp group g1 interface eth2",
            "set high-availability vrrp group g1 no-preempt",
            "set high-availability vrrp group g1 peer-address 192.168.1.3",
            "set high-availability vrrp group g1 priority 100",
            "set high-availability vrrp group g1 rfc3768-compatibility",
            "set high-availability vrrp group g1 track exclude-vrrp-interface",
            "set high-availability vrrp group g1 track interface eth0",
            "set high-availability vrrp group g1 transition-script backup /var/tmp/script.sh",
            "set high-availability vrrp group g1 transition-script fault /var/tmp/script.sh",
            "set high-availability vrrp group g1 transition-script master /var/tmp/script.sh",
            "set high-availability vrrp group g1 transition-script stop /var/tmp/script.sh",
            "set high-availability vrrp group g1 vrid 20",
            "set high-availability vrrp group g2 address 2.2.2.2",
            "set high-availability vrrp group g2 description 'Group_2'",
            "set high-availability vrrp group g2 health-check failure-count 5",
            "set high-availability vrrp group g2 health-check interval 15",
            "set high-availability vrrp group g2 health-check ping 192.168.1.100",
            "set high-availability vrrp group g2 health-check script /var/tmp/script.sh",
            "set high-availability vrrp group g2 hello-source-address 2.2.2.2",
            "set high-availability vrrp group g2 interface eth1",
            "set high-availability vrrp group g2 vrid 11",
            "set high-availability vrrp snmp",
            "set high-availability vrrp sync-group sg1 health-check failure-count 3",
            "set high-availability vrrp sync-group sg1 health-check interval 10",
            "set high-availability vrrp sync-group sg1 health-check ping 192.168.2.100",
            "set high-availability vrrp sync-group sg1 health-check script /var/tmp/script.sh",
            "set high-availability vrrp sync-group sg1 member g1",
            "set high-availability vrrp sync-group sg1 transition-script backup /var/tmp/script.sh",
            "set high-availability vrrp sync-group sg1 transition-script fault /var/tmp/script.sh",
            "set high-availability vrrp sync-group sg1 transition-script master /var/tmp/script.sh",
            "set high-availability vrrp sync-group sg1 transition-script stop /var/tmp/script.sh",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_commands),
            result["rendered"],
        )

    def test_vrrp_parsed(self):
        commands = (
            "set high-availability disable",
            "set high-availability virtual-server s1 address 10.10.10.1",
            "set high-availability virtual-server s1 algorithm round-robin",
            "set high-availability virtual-server s1 delay-loop 60",
            "set high-availability virtual-server s1 forward-method direct",
            "set high-availability virtual-server s1 fwmark 10",
            "set high-availability virtual-server s1 persistence-timeout 30",
            "set high-availability virtual-server s1 protocol tcp",
            "set high-availability virtual-server s1 real-server 10.10.50.1 health-check script '/var/tmp/script.sh'",
            "set high-availability virtual-server s1 real-server 10.10.50.1 port 443",
            "set high-availability virtual-server s2 address 10.10.10.2",
            "set high-availability virtual-server s2 port 81",
            "set high-availability virtual-server s2 real-server real1 connection-timeout 5",
            "set high-availability virtual-server s2 real-server real1 port 8081",
            "set high-availability virtual-server s2 real-server real2 port 8080",
            "set high-availability vrrp global-parameters garp interval 30",
            "set high-availability vrrp global-parameters garp master-delay 10",
            "set high-availability vrrp global-parameters garp master-refresh 100",
            "set high-availability vrrp global-parameters garp master-refresh-repeat 200",
            "set high-availability vrrp global-parameters garp master-repeat 5",
            "set high-availability vrrp global-parameters startup-delay 30",
            "set high-availability vrrp global-parameters version 3",
            "set high-availability vrrp group g1 address '1.1.1.1'",
            "set high-availability vrrp group g1 advertise-interval 10",
            "set high-availability vrrp group g1 authentication password 'testpass'",
            "set high-availability vrrp group g1 authentication type 'plaintext-password'",
            "set high-availability vrrp group g1 description 'Group_1'",
            "set high-availability vrrp group g1 disable",
            "set high-availability vrrp group g1 excluded-address '192.168.1.7' interface 'eth3'",
            "set high-availability vrrp group g1 excluded-address '192.168.1.8'",
            "set high-availability vrrp group g1 garp interval 20",
            "set high-availability vrrp group g1 garp master-delay 5",
            "set high-availability vrrp group g1 garp master-refresh 50",
            "set high-availability vrrp group g1 garp master-refresh-repeat 100",
            "set high-availability vrrp group g1 garp master-repeat 3",
            "set high-availability vrrp group g1 health-check failure-count 3",
            "set high-availability vrrp group g1 health-check interval 10",
            "set high-availability vrrp group g1 health-check ping '192.168.1.5'",
            "set high-availability vrrp group g1 health-check script 'script.sh'",
            "set high-availability vrrp group g1 hello-source-address '192.168.1.2'",
            "set high-availability vrrp group g1 interface 'eth2'",
            "set high-availability vrrp group g1 no-preempt",
            "set high-availability vrrp group g1 peer-address '192.168.1.3'",
            "set high-availability vrrp group g1 priority 100",
            "set high-availability vrrp group g1 rfc3768-compatibility",
            "set high-availability vrrp group g1 track exclude-vrrp-interface",
            "set high-availability vrrp group g1 track interface 'eth1'",
            "set high-availability vrrp group g1 transition-script backup '/var/tmp/script.sh'",
            "set high-availability vrrp group g1 transition-script fault '/var/tmp/script.sh'",
            "set high-availability vrrp group g1 transition-script master '/var/tmp/script.sh'",
            "set high-availability vrrp group g1 transition-script stop '/var/tmp/script.sh'",
            "set high-availability vrrp group g1 vrid 20",
            "set high-availability vrrp snmp",
            "set high-availability vrrp sync-group sg1 health-check failure-count 3",
            "set high-availability vrrp sync-group sg1 health-check interval 10",
            "set high-availability vrrp sync-group sg1 health-check ping '192.168.1.1'",
            "set high-availability vrrp sync-group sg1 health-check script '/var/tmp/script.sh'",
            "set high-availability vrrp sync-group sg1 member 'g1'",
            "set high-availability vrrp sync-group sg1 transition-script backup '/var/tmp/script.sh'",
            "set high-availability vrrp sync-group sg1 transition-script fault '/var/tmp/script.sh'",
            "set high-availability vrrp sync-group sg1 transition-script master '/var/tmp/script.sh'",
            "set high-availability vrrp sync-group sg1 transition-script stop '/var/tmp/script.sh'",
        )
        parsed_str = "\n".join(commands)
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "disable": True,
            "virtual_servers": [
                {
                    "name": "s1",
                    "address": "10.10.10.1",
                    "algorithm": "round-robin",
                    "delay_loop": 60,
                    "forward_method": "direct",
                    "fwmark": 10,
                    "persistence_timeout": 30,
                    "protocol": "tcp",
                    "real_server": [
                        {
                            "address": "10.10.50.1",
                            "health_check_script": "/var/tmp/script.sh",
                            "port": 443,
                        },
                    ],
                },
                {
                    "name": "s2",
                    "address": "10.10.10.2",
                    "port": 81,
                    "real_server": [
                        {
                            "address": "real1",
                            "connection_timeout": 5,
                            "port": 8081,
                        },
                        {
                            "address": "real2",
                            "port": 8080,
                        },
                    ],
                },
            ],
            "vrrp": {
                "snmp": "enabled",
                "global_parameters": {
                    "startup_delay": 30,
                    "version": "3",
                    "garp": {
                        "interval": 30,
                        "master_delay": 10,
                        "master_refresh": 100,
                        "master_refresh_repeat": 200,
                        "master_repeat": 5,
                    },
                },
                "groups": [
                    {
                        "name": "g1",
                        "description": "Group_1",
                        "disable": True,
                        "no_preempt": True,
                        "rfc3768_compatibility": True,
                        "interface": "eth2",
                        "address": "1.1.1.1",
                        "advertise_interval": 10,
                        "peer_address": "192.168.1.3",
                        "priority": 100,
                        "vrid": 20,
                        "garp": {
                            "interval": 20,
                            "master_delay": 5,
                            "master_refresh": 50,
                            "master_refresh_repeat": 100,
                            "master_repeat": 3,
                        },
                        "authentication": {
                            "type": "plaintext-password",
                            "password": "testpass",
                        },
                        "transition_script": {
                            "master": "/var/tmp/script.sh",
                            "backup": "/var/tmp/script.sh",
                            "fault": "/var/tmp/script.sh",
                            "stop": "/var/tmp/script.sh",
                        },
                        "health_check": {
                            "failure_count": 3,
                            "interval": 10,
                            "ping": "192.168.1.5",
                            "script": "script.sh",
                        },
                        "track": {
                            "exclude_vrrp_interface": True,
                            "interface": ["eth1"],
                        },
                        "excluded_address": [
                            "192.168.1.7 interface eth3",
                            "192.168.1.8",
                        ],
                        "hello_source_address": "192.168.1.2",
                    },
                ],
                "sync_groups": [
                    {
                        "name": "sg1",
                        "member": ["g1"],
                        "transition_script": {
                            "master": "/var/tmp/script.sh",
                            "backup": "/var/tmp/script.sh",
                            "fault": "/var/tmp/script.sh",
                            "stop": "/var/tmp/script.sh",
                        },
                        "health_check": {
                            "failure_count": 3,
                            "interval": 10,
                            "ping": "192.168.1.1",
                            "script": "/var/tmp/script.sh",
                        },
                    },
                ],
            },
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_vrrp_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered_list = {
            "disable": True,
            "virtual_servers": [
                {
                    "name": "s1",
                    "address": "10.10.10.1",
                    "algorithm": "round-robin",
                    "delay_loop": 60,
                    "forward_method": "direct",
                    "fwmark": 10,
                    "persistence_timeout": 30,
                    "protocol": "tcp",
                    "real_server": [
                        {
                            "address": "10.10.50.1",
                            "health_check_script": "/var/tmp/script.sh",
                            "port": 443,
                        },
                    ],
                },
                {
                    "name": "s2",
                    "address": "10.10.10.2",
                    "port": 81,
                    "real_server": [
                        {
                            "address": "real1",
                            "connection_timeout": 5,
                            "port": 8081,
                        },
                        {
                            "address": "real2",
                            "port": 8080,
                        },
                    ],
                },
            ],
            "vrrp": {
                "snmp": "enabled",
                "global_parameters": {
                    "startup_delay": 30,
                    "version": "3",
                    "garp": {
                        "interval": 30,
                        "master_delay": 10,
                        "master_refresh": 100,
                        "master_refresh_repeat": 200,
                        "master_repeat": 5,
                    },
                },
                "groups": [
                    {
                        "name": "g1",
                        "description": "Group_1",
                        "disable": True,
                        "no_preempt": True,
                        "rfc3768_compatibility": True,
                        "interface": "eth2",
                        "address": "1.1.1.1",
                        "advertise_interval": 10,
                        "peer_address": "192.168.1.3",
                        "priority": 100,
                        "vrid": 20,
                        "garp": {
                            "interval": 20,
                            "master_delay": 5,
                            "master_refresh": 50,
                            "master_refresh_repeat": 100,
                            "master_repeat": 3,
                        },
                        "authentication": {
                            "type": "plaintext-password",
                            "password": "testpass",
                        },
                        "transition_script": {
                            "master": "/var/tmp/script.sh",
                            "backup": "/var/tmp/script.sh",
                            "fault": "/var/tmp/script.sh",
                            "stop": "/var/tmp/script.sh",
                        },
                        "health_check": {
                            "failure_count": 3,
                            "interval": 10,
                            "ping": "192.168.1.5",
                            "script": "script.sh",
                        },
                        "track": {
                            "exclude_vrrp_interface": True,
                            "interface": ["eth1"],
                        },
                        "excluded_address": [
                            "192.168.1.7 interface eth3",
                            "192.168.1.8",
                        ],
                        "hello_source_address": "192.168.1.2",
                    },
                ],
                "sync_groups": [
                    {
                        "name": "sg1",
                        "member": ["g1"],
                        "transition_script": {
                            "master": "/var/tmp/script.sh",
                            "backup": "/var/tmp/script.sh",
                            "fault": "/var/tmp/script.sh",
                            "stop": "/var/tmp/script.sh",
                        },
                        "health_check": {
                            "failure_count": 3,
                            "interval": 10,
                            "ping": "192.168.1.1",
                            "script": "/var/tmp/script.sh",
                        },
                    },
                ],
            },
        }

        self.assertEqual(gathered_list, result["gathered"])

    # def test_ntp_deleted(self):
    #     # Delete the subsections that we include (listen_addresses and servers)
    #     set_module_args(
    #         dict(
    #             config=dict(
    #                 allow_clients=["10.1.1.0/24"],
    #                 listen_addresses=["10.2.3.1"],
    #                 servers=[
    #                     dict(server="server1"),
    #                     dict(server="server3", options=["noselect"]),
    #                     dict(server="time1.vyos.net"),
    #                     dict(server="time2.vyos.net"),
    #                     dict(server="time3.vyos.net"),
    #                 ],
    #             ),
    #             state="deleted",
    #         ),
    #     )
    #     commands = [
    #         "delete system ntp allow-clients",  # 10.1.1.0/24",
    #         "delete system ntp listen-address",  # 10.2.3.1",
    #         "delete system ntp server server1",
    #         "delete system ntp server server3",
    #         "delete system ntp server time1.vyos.net",
    #         "delete system ntp server time2.vyos.net",
    #         "delete system ntp server time3.vyos.net",
    #         "delete system ntp",
    #     ]
    #     self.execute_module(changed=True, commands=commands)

    def test_vrrp_deleted_all(self):
        set_module_args(
            dict(
                config=dict(),
                state="deleted",
            ),
        )
        commands = [
            "delete high-availability",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vrrp_purged(self):
        set_module_args(
            dict(
                config=dict(),
                state="purged",
            ),
        )
        commands = [
            "delete high-availability",
        ]
        self.execute_module(changed=True, commands=commands)
