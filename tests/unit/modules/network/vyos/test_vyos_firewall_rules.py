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

from ansible_collections.vyos.vyos.plugins.modules import vyos_firewall_rules
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosFirewallRulesModule(TestVyosModule):
    module = vyos_firewall_rules

    def setUp(self):
        super(TestVyosFirewallRulesModule, self).setUp()
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

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.firewall_rules.firewall_rules.Firewall_rulesFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.firewall_rules.firewall_rules.get_os_version",
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "1.2"

    def tearDown(self):
        super(TestVyosFirewallRulesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("vyos_firewall_rules_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_firewall_rule_set_01_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INBOUND",
                                description="This is IPv6 INBOUND rule set",
                                default_action="reject",
                                enable_default_log=True,
                                rules=[],
                            ),
                            dict(
                                name="V6-OUTBOUND",
                                description="This is IPv6 OUTBOUND rule set",
                                default_action="accept",
                                enable_default_log=False,
                                rules=[],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INBOUND",
                                description="This is IPv4 INBOUND rule set",
                                default_action="reject",
                                enable_default_log=True,
                                rules=[],
                            ),
                            dict(
                                name="V4-OUTBOUND",
                                description="This is IPv4 OUTBOUND rule set",
                                default_action="accept",
                                enable_default_log=False,
                                rules=[],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set firewall ipv6-name V6-INBOUND default-action 'reject'",
            "set firewall ipv6-name V6-INBOUND description 'This is IPv6 INBOUND rule set'",
            "set firewall ipv6-name V6-INBOUND enable-default-log",
            "set firewall ipv6-name V6-OUTBOUND default-action 'accept'",
            "set firewall ipv6-name V6-OUTBOUND description 'This is IPv6 OUTBOUND rule set'",
            "set firewall name V4-INBOUND default-action 'reject'",
            "set firewall name V4-INBOUND description 'This is IPv4 INBOUND rule set'",
            "set firewall name V4-INBOUND enable-default-log",
            "set firewall name V4-OUTBOUND default-action 'accept'",
            "set firewall name V4-OUTBOUND description 'This is IPv4 OUTBOUND rule set'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_rule_set_02_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INBOUND",
                                description="This is IPv6 INBOUND rule set",
                                default_action="reject",
                                enable_default_log=True,
                                rules=[],
                            ),
                            dict(
                                name="V6-OUTBOUND",
                                description="This is IPv6 OUTBOUND rule set",
                                default_action="accept",
                                enable_default_log=False,
                                rules=[],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INBOUND",
                                description="This is IPv4 INBOUND rule set",
                                default_action="reject",
                                enable_default_log=True,
                                rules=[],
                            ),
                            dict(
                                name="V4-OUTBOUND",
                                description="This is IPv4 OUTBOUND rule set",
                                default_action="accept",
                                enable_default_log=False,
                                rules=[],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set firewall ipv6-name V6-INBOUND default-action 'reject'",
            "set firewall ipv6-name V6-INBOUND description 'This is IPv6 INBOUND rule set'",
            "set firewall ipv6-name V6-INBOUND enable-default-log",
            "set firewall ipv6-name V6-OUTBOUND default-action 'accept'",
            "set firewall ipv6-name V6-OUTBOUND description 'This is IPv6 OUTBOUND rule set'",
            "set firewall name V4-INBOUND default-action 'reject'",
            "set firewall name V4-INBOUND description 'This is IPv4 INBOUND rule set'",
            "set firewall name V4-INBOUND enable-default-log",
            "set firewall name V4-OUTBOUND default-action 'accept'",
            "set firewall name V4-OUTBOUND description 'This is IPv4 OUTBOUND rule set'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                description="This is IPv4 INBOUND rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        log="disable",
                                        protocol="icmp",
                                        fragment="match-frag",
                                        disable=True,
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
            "set firewall name INBOUND default-action 'accept'",
            "set firewall name INBOUND description 'This is IPv4 INBOUND rule set'",
            "set firewall name INBOUND enable-default-log",
            "set firewall name INBOUND rule 101 protocol 'icmp'",
            "set firewall name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall name INBOUND rule 101 fragment 'match-frag'",
            "set firewall name INBOUND rule 101",
            "set firewall name INBOUND rule 101 disable",
            "set firewall name INBOUND rule 101 action 'accept'",
            "set firewall name INBOUND rule 101 ipsec 'match-ipsec'",
            "set firewall name INBOUND rule 101 log 'disable'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        protocol="tcp",
                                        source=dict(
                                            address="192.0.2.0",
                                            mac_address="38:00:25:19:76:0c",
                                            port=2127,
                                        ),
                                        destination=dict(address="192.0.1.0", port=2124),
                                        limit=dict(
                                            burst=10,
                                            rate=dict(number=20, unit="second"),
                                        ),
                                        recent=dict(count=10, time=20),
                                        state=dict(
                                            established=True,
                                            related=True,
                                            invalid=True,
                                            new=True,
                                        ),
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
            "set firewall name INBOUND rule 101 protocol 'tcp'",
            "set firewall name INBOUND rule 101 destination address 192.0.1.0",
            "set firewall name INBOUND rule 101 destination port 2124",
            "set firewall name INBOUND rule 101",
            "set firewall name INBOUND rule 101 source address 192.0.2.0",
            "set firewall name INBOUND rule 101 source mac-address 38:00:25:19:76:0c",
            "set firewall name INBOUND rule 101 source port 2127",
            "set firewall name INBOUND rule 101 state new enable",
            "set firewall name INBOUND rule 101 state invalid enable",
            "set firewall name INBOUND rule 101 state related enable",
            "set firewall name INBOUND rule 101 state established enable",
            "set firewall name INBOUND rule 101 limit burst 10",
            "set firewall name INBOUND rule 101 limit rate 20/second",
            "set firewall name INBOUND rule 101 recent count 10",
            "set firewall name INBOUND rule 101 recent time 20",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_03(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        destination=dict(
                                            group=dict(
                                                address_group="OUT-ADDR-GROUP",
                                                network_group="OUT-NET-GROUP",
                                                port_group="OUT-PORT-GROUP",
                                            ),
                                        ),
                                        source=dict(
                                            group=dict(
                                                address_group="IN-ADDR-GROUP",
                                                network_group="IN-NET-GROUP",
                                                port_group="IN-PORT-GROUP",
                                            ),
                                        ),
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
            "set firewall name INBOUND rule 101 source group address-group IN-ADDR-GROUP",
            "set firewall name INBOUND rule 101 source group network-group IN-NET-GROUP",
            "set firewall name INBOUND rule 101 source group port-group IN-PORT-GROUP",
            "set firewall name INBOUND rule 101 destination group address-group OUT-ADDR-GROUP",
            "set firewall name INBOUND rule 101 destination group network-group OUT-NET-GROUP",
            "set firewall name INBOUND rule 101 destination group port-group OUT-PORT-GROUP",
            "set firewall name INBOUND rule 101",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_04(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        time=dict(
                                            monthdays="2",
                                            startdate="2020-01-24",
                                            starttime="13:20:00",
                                            stopdate="2020-01-28",
                                            stoptime="13:30:00",
                                            weekdays="!Sat,Sun",
                                            utc=True,
                                        ),
                                        tcp=dict(
                                            flags=[
                                                dict(flag="all"),
                                            ]
                                        ),

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
            "set firewall name INBOUND rule 101",
            "set firewall name INBOUND rule 101 tcp flags ALL",
            "set firewall name INBOUND rule 101 time utc",
            "set firewall name INBOUND rule 101 time monthdays 2",
            "set firewall name INBOUND rule 101 time startdate 2020-01-24",
            "set firewall name INBOUND rule 101 time stopdate 2020-01-28",
            "set firewall name INBOUND rule 101 time weekdays !Sat,Sun",
            "set firewall name INBOUND rule 101 time stoptime 13:30:00",
            "set firewall name INBOUND rule 101 time starttime 13:20:00",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v6_rule_sets_rule_merged_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                description="This is IPv6 INBOUND rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        disable=True,
                                        icmp=dict(type_name="echo-request"),
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
            "set firewall ipv6-name INBOUND default-action 'accept'",
            "set firewall ipv6-name INBOUND description 'This is IPv6 INBOUND rule set'",
            "set firewall ipv6-name INBOUND enable-default-log",
            "set firewall ipv6-name INBOUND rule 101 protocol 'icmp'",
            "set firewall ipv6-name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6-name INBOUND rule 101",
            "set firewall ipv6-name INBOUND rule 101 disable",
            "set firewall ipv6-name INBOUND rule 101 action 'accept'",
            "set firewall ipv6-name INBOUND rule 101 ipsec 'match-ipsec'",
            "set firewall ipv6-name INBOUND rule 101 icmpv6 type echo-request",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v6_rule_sets_rule_merged_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        protocol="tcp",
                                        source=dict(
                                            address="2001:db8::12",
                                            mac_address="38:00:25:19:76:0c",
                                            port=2127,
                                        ),
                                        destination=dict(address="2001:db8::11", port=2124),
                                        limit=dict(
                                            burst=10,
                                            rate=dict(number=20, unit="second"),
                                        ),
                                        recent=dict(count=10, time=20),
                                        state=dict(
                                            established=True,
                                            related=True,
                                            invalid=True,
                                            new=True,
                                        ),
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
            "set firewall ipv6-name INBOUND rule 101 protocol 'tcp'",
            "set firewall ipv6-name INBOUND rule 101 destination address 2001:db8::11",
            "set firewall ipv6-name INBOUND rule 101 destination port 2124",
            "set firewall ipv6-name INBOUND rule 101",
            "set firewall ipv6-name INBOUND rule 101 source address 2001:db8::12",
            "set firewall ipv6-name INBOUND rule 101 source mac-address 38:00:25:19:76:0c",
            "set firewall ipv6-name INBOUND rule 101 source port 2127",
            "set firewall ipv6-name INBOUND rule 101 state new enable",
            "set firewall ipv6-name INBOUND rule 101 state invalid enable",
            "set firewall ipv6-name INBOUND rule 101 state related enable",
            "set firewall ipv6-name INBOUND rule 101 state established enable",
            "set firewall ipv6-name INBOUND rule 101 limit burst 10",
            "set firewall ipv6-name INBOUND rule 101 recent count 10",
            "set firewall ipv6-name INBOUND rule 101 recent time 20",
            "set firewall ipv6-name INBOUND rule 101 limit rate 20/second",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v6_rule_sets_rule_merged_03(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        destination=dict(
                                            group=dict(
                                                address_group="OUT-ADDR-GROUP",
                                                network_group="OUT-NET-GROUP",
                                                port_group="OUT-PORT-GROUP",
                                            ),
                                        ),
                                        source=dict(
                                            group=dict(
                                                address_group="IN-ADDR-GROUP",
                                                network_group="IN-NET-GROUP",
                                                port_group="IN-PORT-GROUP",
                                            ),
                                        ),
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
            "set firewall ipv6-name INBOUND rule 101 source group address-group IN-ADDR-GROUP",
            "set firewall ipv6-name INBOUND rule 101 source group network-group IN-NET-GROUP",
            "set firewall ipv6-name INBOUND rule 101 source group port-group IN-PORT-GROUP",
            "set firewall ipv6-name INBOUND rule 101 destination group address-group OUT-ADDR-GROUP",
            "set firewall ipv6-name INBOUND rule 101 destination group network-group OUT-NET-GROUP",
            "set firewall ipv6-name INBOUND rule 101 destination group port-group OUT-PORT-GROUP",
            "set firewall ipv6-name INBOUND rule 101",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v6_rule_sets_rule_merged_04(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        time=dict(
                                            monthdays="2",
                                            startdate="2020-01-24",
                                            starttime="13:20:00",
                                            stopdate="2020-01-28",
                                            stoptime="13:30:00",
                                            weekdays="!Sat,Sun",
                                            utc=True,
                                        ),
                                        tcp=dict(
                                            flags=[
                                                dict(flag="all"),
                                            ]
                                        ),
                                    ),
                                    dict(
                                        number="102",
                                        tcp=dict(
                                            flags=[
                                                dict(flag="ack"),
                                                dict(flag="syn"),
                                                dict(flag="fin", invert=True),
                                            ],
                                        )
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set firewall ipv6-name INBOUND rule 101",
            "set firewall ipv6-name INBOUND rule 101 tcp flags ALL",
            "set firewall ipv6-name INBOUND rule 101 time utc",
            "set firewall ipv6-name INBOUND rule 101 time monthdays 2",
            "set firewall ipv6-name INBOUND rule 101 time startdate 2020-01-24",
            "set firewall ipv6-name INBOUND rule 101 time stopdate 2020-01-28",
            "set firewall ipv6-name INBOUND rule 101 time weekdays !Sat,Sun",
            "set firewall ipv6-name INBOUND rule 101 time stoptime 13:30:00",
            "set firewall ipv6-name INBOUND rule 101 time starttime 13:20:00",
            "set firewall ipv6-name INBOUND rule 102",
            "set firewall ipv6-name INBOUND rule 102 tcp flags ACK,SYN,!FIN",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v6_rule_sets_rule_merged_icmp_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        protocol="icmp",
                                        icmp=dict(type_name="port-unreachable"),
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
            "set firewall ipv6-name INBOUND rule 101 icmpv6 type port-unreachable",
            "set firewall ipv6-name INBOUND rule 101 protocol 'icmp'",
            "set firewall ipv6-name INBOUND rule 101",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_icmp_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        protocol="icmp",
                                        icmp=dict(type=1, code=1),
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
            "set firewall name INBOUND rule 101 icmp type 1",
            "set firewall name INBOUND rule 101 icmp code 1",
            "set firewall name INBOUND rule 101 protocol 'icmp'",
            "set firewall name INBOUND rule 101",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_icmp_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        protocol="icmp",
                                        icmp=dict(type_name="echo-request"),
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
            "set firewall name INBOUND rule 101 icmp type-name echo-request",
            "set firewall name INBOUND rule 101 protocol 'icmp'",
            "set firewall name INBOUND rule 101",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_del_01(self):
        set_module_args(
            dict(
                config=[dict(afi="ipv4", rule_sets=[dict(name="V4-INGRESS")])],
                state="deleted",
            ),
        )
        commands = ["delete firewall name V4-INGRESS"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_del_02(self):
        set_module_args(
            dict(
                config=[
                    dict(afi="ipv4", rule_sets=[dict(name="V4-INGRESS")]),
                    dict(afi="ipv6", rule_sets=[dict(name="V6-INGRESS")]),
                ],
                state="deleted",
            ),
        )
        commands = [
            "delete firewall name V4-INGRESS",
            "delete firewall ipv6-name V6-INGRESS",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_del_03(self):
        set_module_args(dict(config=[], state="deleted"))
        commands = ["delete firewall name", "delete firewall ipv6-name"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_del_04(self):
        set_module_args(
            dict(
                config=[
                    dict(afi="ipv4", rule_sets=[dict(name="V4-ING")]),
                    dict(afi="ipv6", rule_sets=[dict(name="V6-ING")]),
                ],
                state="deleted",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_firewall_v4v6_rule_sets_rule_rep_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="reject",
                                        description="Rule 101 is configured by Ansible RM",
                                        ipsec="match-ipsec",
                                        protocol="tcp",
                                        fragment="match-frag",
                                        disable=False,
                                    ),
                                    dict(
                                        number="102",
                                        action="accept",
                                        description="Rule 102 is configured by Ansible RM",
                                        protocol="icmp",
                                        disable=True,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INGRESS",
                                default_action="accept",
                                description="This rule-set is configured by Ansible RM",
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                                description="This rule-set is configured by Ansible RM",
                                rules=[
                                    dict(
                                        icmp=dict(type_name="echo-request"),
                                        number=20,
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
            "delete firewall name V4-INGRESS rule 101 disable",
            "set firewall name V4-INGRESS description 'This is IPv4 INGRESS rule set'",
            "set firewall name V4-INGRESS rule 101 protocol 'tcp'",
            "set firewall name V4-INGRESS rule 101 description 'Rule 101 is configured by Ansible RM'",
            "set firewall name V4-INGRESS rule 101 action 'reject'",
            "delete firewall name V4-INGRESS rule 101 log",
            "set firewall name V4-INGRESS rule 102 disable",
            "set firewall name V4-INGRESS rule 102 action 'accept'",
            "set firewall name V4-INGRESS rule 102 protocol 'icmp'",
            "set firewall name V4-INGRESS rule 102 description 'Rule 102 is configured by Ansible RM'",
            "set firewall name V4-INGRESS rule 102",
            "set firewall ipv6-name V6-INGRESS description 'This rule-set is configured by Ansible RM'",
            "set firewall ipv6-name EGRESS description 'This rule-set is configured by Ansible RM'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_rule_rep_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 V4-INGRESS rule set",
                                default_action="accept",
                                enable_default_log=False,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        fragment="match-frag",
                                        disable=True,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INGRESS",
                                default_action="accept",
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                                rules=[
                                    dict(
                                        icmp=dict(type_name="echo-request"),
                                        number=20,
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
            "delete firewall name V4-INGRESS enable-default-log",
            "delete firewall name V4-INGRESS rule 101 log",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_rule_rep_idem_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 V4-INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        fragment="match-frag",
                                        disable=True,
                                        log="enable",
                                    )
                                ],
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INGRESS",
                                default_action="accept",
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                                rules=[
                                    dict(
                                        icmp=dict(type_name="echo-request"),
                                        number=20,
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

    def test_vyos_firewall_v4v6_rule_sets_rule_rep_idem_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 V4-INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        fragment="match-frag",
                                        disable=True,
                                        log="enable"
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

    def test_vyos_firewall_v4v6_rule_sets_rule_mer_idem_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 V4-INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        fragment="match-frag",
                                        disable=True,
                                    )
                                ],
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INGRESS",
                                default_action="accept",
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                                rules=[
                                    dict(
                                        icmp=dict(type_name="echo-request"),
                                        number=20,
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

    def test_vyos_firewall_v4v6_rule_sets_rule_ovr_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-IN",
                                description="This is IPv4 INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="1",
                                        action="reject",
                                        description="Rule 1 is configured by Ansible RM",
                                        ipsec="match-ipsec",
                                        log="enable",
                                        protocol="tcp",
                                        fragment="match-frag",
                                        disable=False,
                                        source=dict(
                                            group=dict(
                                                address_group="IN-ADDR-GROUP",
                                                network_group="IN-NET-GROUP",
                                                port_group="IN-PORT-GROUP",
                                            ),
                                        ),
                                    ),
                                    dict(
                                        number="2",
                                        action="accept",
                                        description="Rule 102 is configured by Ansible RM",
                                        protocol="icmp",
                                        disable=True,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-IN",
                                default_action="accept",
                                description="This rule-set is configured by Ansible RM",
                            ),
                            dict(
                                name="V6-EG",
                                default_action="reject",
                                description="This rule-set is configured by Ansible RM",
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "delete firewall ipv6-name V6-INGRESS",
            "delete firewall ipv6-name EGRESS",
            "delete firewall name V4-INGRESS",
            "delete firewall name EGRESS",
            "set firewall name V4-IN default-action 'accept'",
            "set firewall name V4-IN description 'This is IPv4 INGRESS rule set'",
            "set firewall name V4-IN enable-default-log",
            "set firewall name V4-IN rule 1 protocol 'tcp'",
            "set firewall name V4-IN rule 1 log 'enable'",
            "set firewall name V4-IN rule 1 description 'Rule 1 is configured by Ansible RM'",
            "set firewall name V4-IN rule 1 fragment 'match-frag'",
            "set firewall name V4-IN rule 1 source group address-group IN-ADDR-GROUP",
            "set firewall name V4-IN rule 1 source group network-group IN-NET-GROUP",
            "set firewall name V4-IN rule 1 source group port-group IN-PORT-GROUP",
            "set firewall name V4-IN rule 1",
            "set firewall name V4-IN rule 1 action 'reject'",
            "set firewall name V4-IN rule 1 ipsec 'match-ipsec'",
            "set firewall name V4-IN rule 2 disable",
            "set firewall name V4-IN rule 2 action 'accept'",
            "set firewall name V4-IN rule 2 protocol 'icmp'",
            "set firewall name V4-IN rule 2 description 'Rule 102 is configured by Ansible RM'",
            "set firewall name V4-IN rule 2",
            "set firewall ipv6-name V6-IN default-action 'accept'",
            "set firewall ipv6-name V6-IN description 'This rule-set is configured by Ansible RM'",
            "set firewall ipv6-name V6-EG default-action 'reject'",
            "set firewall ipv6-name V6-EG description 'This rule-set is configured by Ansible RM'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_rule_ovr_idem_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 V4-INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        fragment="match-frag",
                                        disable=True,
                                        log="enable",
                                    )
                                ],
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INGRESS",
                                default_action="accept",
                            ),
                            dict(
                                name="EGRESS",
                                default_action="reject",
                                rules=[
                                    dict(
                                        icmp=dict(type_name="echo-request"),
                                        number=20,
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

    def test_vyos_firewall_v6_rule_sets_rule_merged_01_version(self):
        self.get_os_version.return_value = "1.4"
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                description="This is IPv6 INBOUND rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        disable=True,
                                        icmp=dict(type_name="echo-request"),
                                        log="enable",
                                    ),
                                    dict(
                                        number="102",
                                        action="reject",
                                        description="Rule 102 is configured by Ansible",
                                        protocol="ipv6-icmp",
                                        icmp=dict(type=7),
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
            "set firewall ipv6 name INBOUND default-action 'accept'",
            "set firewall ipv6 name INBOUND description 'This is IPv6 INBOUND rule set'",
            "set firewall ipv6 name INBOUND default-log",
            "set firewall ipv6 name INBOUND rule 101 protocol 'icmp'",
            "set firewall ipv6 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6 name INBOUND rule 101",
            "set firewall ipv6 name INBOUND rule 101 disable",
            "set firewall ipv6 name INBOUND rule 101 action 'accept'",
            "set firewall ipv6 name INBOUND rule 101 ipsec 'match-ipsec'",
            "set firewall ipv6 name INBOUND rule 101 icmpv6 type-name echo-request",
            "set firewall ipv6 name INBOUND rule 101 log 'enable'",
            "set firewall ipv6 name INBOUND rule 102",
            "set firewall ipv6 name INBOUND rule 102 action 'reject'",
            "set firewall ipv6 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
            "set firewall ipv6 name INBOUND rule 102 protocol 'ipv6-icmp'",
            'set firewall ipv6 name INBOUND rule 102 icmpv6 type 7',
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_jump_rules_merged_01(self):
        self.get_os_version.return_value = "1.4"
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                description="This is IPv6 INBOUND rule set with a jump action",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="jump",
                                        description="Rule 101 is configured by Ansible",
                                        ipsec="match-ipsec",
                                        protocol="icmp",
                                        icmp=dict(type_name="echo-request"),
                                        jump_target="PROTECT-RE",
                                        packet_length_exclude=[dict(length=100), dict(length=200)]
                                    ),
                                    dict(
                                        number="102",
                                        action="reject",
                                        description="Rule 102 is configured by Ansible",
                                        protocol="ipv6-icmp",
                                        icmp=dict(type=7),
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
                state="merged",
            )
        )
        commands = [
            "set firewall ipv6 name INBOUND default-action 'accept'",
            "set firewall ipv6 name INBOUND description 'This is IPv6 INBOUND rule set with a jump action'",
            "set firewall ipv6 name INBOUND default-log",
            "set firewall ipv6 name INBOUND rule 101 protocol 'icmp'",
            "set firewall ipv6 name INBOUND rule 101 packet-length-exclude 100",
            "set firewall ipv6 name INBOUND rule 101 packet-length-exclude 200",
            "set firewall ipv6 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6 name INBOUND rule 101",
            "set firewall ipv6 name INBOUND rule 101 ipsec 'match-ipsec'",
            "set firewall ipv6 name INBOUND rule 101 icmpv6 type-name echo-request",
            "set firewall ipv6 name INBOUND rule 101 action 'jump'",
            "set firewall ipv6 name INBOUND rule 101 jump-target 'PROTECT-RE'",
            "set firewall ipv6 name INBOUND rule 102",
            "set firewall ipv6 name INBOUND rule 102 action 'reject'",
            "set firewall ipv6 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
            "set firewall ipv6 name INBOUND rule 102 protocol 'ipv6-icmp'",
            'set firewall ipv6 name INBOUND rule 102 icmpv6 type 7',
        ]
        self.execute_module(changed=True, commands=commands)


class TestVyosFirewallRulesModule14(TestVyosModule):
    module = vyos_firewall_rules

    def setUp(self):
        super(TestVyosFirewallRulesModule14, self).setUp()
        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection"
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()
        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.static_routes.static_routes.Static_routesFacts.get_device_data"
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.firewall_rules.firewall_rules.Firewall_rulesFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.firewall_rules.firewall_rules.get_os_version"
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "1.4"
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosFirewallRulesModule14, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("vyos_firewall_rules_config_v14.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_firewall_packet_length_merged_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                description="This is IPv6 INBOUND rule set with a jump action",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="jump",
                                        description="Rule 101 is configured by Ansible",
                                        jump_target="PROTECT-RE",
                                        packet_length_exclude=[dict(length=100), dict(length=200)],
                                        packet_length=[dict(length=22)]
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
                state="merged",
            )
        )
        commands = [
            "set firewall ipv6 name INBOUND default-action 'accept'",
            "set firewall ipv6 name INBOUND description 'This is IPv6 INBOUND rule set with a jump action'",
            "set firewall ipv6 name INBOUND default-log",
            "set firewall ipv6 name INBOUND rule 101 packet-length-exclude 100",
            "set firewall ipv6 name INBOUND rule 101 packet-length-exclude 200",
            "set firewall ipv6 name INBOUND rule 101 packet-length 22",
            "set firewall ipv6 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6 name INBOUND rule 101",
            "set firewall ipv6 name INBOUND rule 101 action 'jump'",
            "set firewall ipv6 name INBOUND rule 101 jump-target 'PROTECT-RE'",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_packet_length_replace_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="V4-INGRESS",
                                description="This is IPv4 V4-INGRESS rule set",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        packet_length_exclude=[dict(length=100), dict(length=200)],
                                        packet_length=[dict(length=22)]
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "delete firewall ipv4 name V4-INGRESS rule 101 protocol",
            "delete firewall ipv4 name V4-INGRESS rule 101 disable",
            "delete firewall ipv4 name V4-INGRESS rule 101 packet-length-exclude 300",
            "set firewall ipv4 name V4-INGRESS rule 101 packet-length-exclude 200",
            "set firewall ipv4 name V4-INGRESS rule 101 packet-length 22",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_filter_merged_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                filter="input",
                                description="This is IPv6 INBOUND rule set with a jump action",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="jump",
                                        description="Rule 101 is configured by Ansible",
                                        jump_target="PROTECT-RE",
                                        packet_length_exclude=[dict(length=100), dict(length=200)],
                                        packet_length=[dict(length=22)]
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
                state="merged",
            )
        )
        commands = [
            "set firewall ipv6 input filter default-action 'accept'",
            "set firewall ipv6 input filter description 'This is IPv6 INBOUND rule set with a jump action'",
            "set firewall ipv6 input filter default-log",
            "set firewall ipv6 input filter rule 101 packet-length-exclude 100",
            "set firewall ipv6 input filter rule 101 packet-length-exclude 200",
            "set firewall ipv6 input filter rule 101 packet-length 22",
            "set firewall ipv6 input filter rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6 input filter rule 101",
            "set firewall ipv6 input filter rule 101 action 'jump'",
            "set firewall ipv6 input filter rule 101 jump-target 'PROTECT-RE'",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_interface_merged_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="V6-INGRESS",
                                description="This is IPv6 INBOUND rule set with a jump action",
                                default_action="accept",
                                rules=[
                                    dict(
                                        number="101",
                                        action="jump",
                                        description="Rule 101 is configured by Ansible",
                                        jump_target="PROTECT-RE",
                                        inbound_interface=dict(name="eth0"),
                                        outbound_interface=dict(group="eth1"),
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
                state="merged",
            )
        )
        commands = [
            "set firewall ipv6 name V6-INGRESS description 'This is IPv6 INBOUND rule set with a jump action'",
            "set firewall ipv6 name V6-INGRESS rule 101 inbound-interface name eth0",
            "set firewall ipv6 name V6-INGRESS rule 101 outbound-interface group eth1",
            "set firewall ipv6 name V6-INGRESS rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6 name V6-INGRESS rule 101",
            "set firewall ipv6 name V6-INGRESS rule 101 action 'jump'",
            "set firewall ipv6 name V6-INGRESS rule 101 jump-target 'PROTECT-RE'",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_interface_replace_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="IF-TEST",
                                description="Changed",
                                rules=[
                                    dict(
                                        number="10",
                                        action="accept",
                                        description="Rule 10 is configured by Ansible",
                                        inbound_interface=dict(name="eth1"),
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "set firewall ipv4 name IF-TEST description 'Changed'",
            "set firewall ipv4 name IF-TEST rule 10 description 'Rule 10 is configured by Ansible'",
            'set firewall ipv4 name IF-TEST rule 10 inbound-interface name eth1',
            "delete firewall ipv4 name IF-TEST rule 10 outbound-interface group",
            "delete firewall ipv4 name IF-TEST rule 10 disable",
            "delete firewall ipv4 name IF-TEST rule 10 state related",
            "delete firewall ipv4 name IF-TEST rule 10 icmp type-name echo-request",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_rule_merged_02(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        protocol="tcp",
                                        source=dict(
                                            address="192.0.2.0",
                                            mac_address="38:00:25:19:76:0c",
                                            port=2127,
                                        ),
                                        destination=dict(address="192.0.1.0", port=2124),
                                        limit=dict(
                                            burst=10,
                                            rate=dict(number=20, unit="second"),
                                        ),
                                        recent=dict(count=10, time=20),
                                        state=dict(
                                            established=True,
                                            related=True,
                                            invalid=True,
                                            new=True,
                                        ),
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
            "set firewall ipv4 name INBOUND rule 101 protocol 'tcp'",
            "set firewall ipv4 name INBOUND rule 101 destination port 2124",
            "set firewall ipv4 name INBOUND rule 101",
            "set firewall ipv4 name INBOUND rule 101 destination address 192.0.1.0",
            "set firewall ipv4 name INBOUND rule 101 source address 192.0.2.0",
            "set firewall ipv4 name INBOUND rule 101 source mac-address 38:00:25:19:76:0c",
            "set firewall ipv4 name INBOUND rule 101 source port 2127",
            "set firewall ipv4 name INBOUND rule 101 state new",
            "set firewall ipv4 name INBOUND rule 101 state invalid",
            "set firewall ipv4 name INBOUND rule 101 state related",
            "set firewall ipv4 name INBOUND rule 101 state established",
            "set firewall ipv4 name INBOUND rule 101 limit burst 10",
            "set firewall ipv4 name INBOUND rule 101 limit rate 20/second",
            "set firewall ipv4 name INBOUND rule 101 recent count 10",
            "set firewall ipv4 name INBOUND rule 101 recent time 20",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4_rule_sets_change_state_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        rule_sets=[
                            dict(
                                name="IF-TEST",
                                rules=[
                                    dict(
                                        number="10",
                                        disable=False,
                                        action="accept",
                                        state=dict(
                                            established=True,
                                            new=True,
                                        ),
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
            "delete firewall ipv4 name IF-TEST rule 10 disable",
            "delete firewall ipv4 name IF-TEST rule 10 inbound-interface name",
            "delete firewall ipv4 name IF-TEST rule 10 icmp type-name echo-request",
            "delete firewall ipv4 name IF-TEST rule 10 outbound-interface group",
            "delete firewall ipv4 name IF-TEST rule 10 state related",
            "set firewall ipv4 name IF-TEST rule 10 state established",
            "set firewall ipv4 name IF-TEST rule 10 state new",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_del_03(self):
        set_module_args(dict(config=[], state="deleted"))
        commands = ["delete firewall ipv4", "delete firewall ipv6"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v6_rule_sets_rule_merged_04(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                rules=[
                                    dict(
                                        number="101",
                                        time=dict(
                                            monthdays="2",
                                            startdate="2020-01-24",
                                            starttime="13:20:00",
                                            stopdate="2020-01-28",
                                            stoptime="13:30:00",
                                            weekdays="!Sat,Sun",
                                            utc=True,
                                        ),
                                        tcp=dict(
                                            flags=[
                                                dict(flag="all"),
                                            ]
                                        ),
                                    ),
                                    dict(
                                        number="102",
                                        tcp=dict(
                                            flags=[
                                                dict(flag="ack"),
                                                dict(flag="syn"),
                                                dict(flag="fin", invert=True),
                                            ],
                                        )
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set firewall ipv6 name INBOUND rule 101",
            "set firewall ipv6 name INBOUND rule 101 tcp flags all",
            "set firewall ipv6 name INBOUND rule 101 time utc",
            "set firewall ipv6 name INBOUND rule 101 time monthdays 2",
            "set firewall ipv6 name INBOUND rule 101 time startdate 2020-01-24",
            "set firewall ipv6 name INBOUND rule 101 time stopdate 2020-01-28",
            "set firewall ipv6 name INBOUND rule 101 time weekdays !Sat,Sun",
            "set firewall ipv6 name INBOUND rule 101 time stoptime 13:30:00",
            "set firewall ipv6 name INBOUND rule 101 time starttime 13:20:00",
            "set firewall ipv6 name INBOUND rule 102",
            "set firewall ipv6 name INBOUND rule 102 tcp flags ack",
            "set firewall ipv6 name INBOUND rule 102 tcp flags not fin",
            "set firewall ipv6 name INBOUND rule 102 tcp flags syn",
        ]
        self.execute_module(changed=True, commands=commands)
