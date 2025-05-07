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


class TestVyosFirewallRulesModule13(TestVyosModule):
    module = vyos_firewall_rules

    def setUp(self):
        super(TestVyosFirewallRulesModule13, self).setUp()
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
        super(TestVyosFirewallRulesModule13, self).tearDown()
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

    def test_vyos_firewall_v4_rule_sets_rule_merged_01(self):
        """Test if plugin correctly adds new rules set and a rule with variant attributes"""
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing rule set
        """
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
        """Test if plugin correctly adds new ipv6 rules set and a rule with variant attributes"""
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing ipv6 rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing ipv6 rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing ipv6 rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing ipv6 rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing rule set
        """
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
        """Test if plugin correctly adds new rules with variant attributes
            within existing rule set
        """
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
        """Test if plugin correctly removes existing rule set
        """
        set_module_args(
            dict(
                config=[dict(afi="ipv4", rule_sets=[dict(name="V4-INGRESS")])],
                state="deleted",
            ),
        )
        commands = ["delete firewall name V4-INGRESS"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_del_02(self):
        """Test if plugin correctly removes existing rule sets, both ipv4 and ipv6
        """
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
        """Test if plugin correctly removes existing AFIs, both ipv4 and ipv6
        """
        set_module_args(dict(config=[], state="deleted"))
        commands = ["delete firewall name", "delete firewall ipv6-name"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_del_04(self):
        """Test if plugin has no effect on non-existent rule sets
        """
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
        """Test if plugin correctly replaces a particular rule set(s)
            without affecting the others
        """
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
            "delete firewall name V4-INGRESS rule 101",
            "set firewall name V4-INGRESS rule 101",
            "set firewall name V4-INGRESS description 'This is IPv4 INGRESS rule set'",
            "set firewall name V4-INGRESS rule 101 fragment 'match-frag'",
            "set firewall name V4-INGRESS rule 101 ipsec 'match-ipsec'",
            "set firewall name V4-INGRESS rule 101 protocol 'tcp'",
            "set firewall name V4-INGRESS rule 101 description 'Rule 101 is configured by Ansible RM'",
            "set firewall name V4-INGRESS rule 101 action 'reject'",
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
        """Test if plugin correctly replaces a particular rule(s) and rule set attribute(s)
            without affecting the others
        """
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
            "delete firewall name V4-INGRESS rule 101",
            "delete firewall name V4-INGRESS enable-default-log",
            "set firewall name V4-INGRESS rule 101",
            "set firewall name V4-INGRESS rule 101 action 'accept'",
            "set firewall name V4-INGRESS rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall name V4-INGRESS rule 101 disable",
            "set firewall name V4-INGRESS rule 101 fragment 'match-frag'",
            "set firewall name V4-INGRESS rule 101 ipsec 'match-ipsec'",
            "set firewall name V4-INGRESS rule 101 protocol 'icmp'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_rule_rep_idem_01(self):
        """Test if plugin correctly has no effect if there is no change in the configuration
        """
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
        """Test if plugin correctly has no effect if there is no change in the configuration
        """
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
        """Test if plugin correctly has no effect if there is no change in the configuration
        """
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
        """Test if plugin correctly resets the entire rule set if there is a change in the configuration
        """
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
                            dict(
                                name="MULTIPLE-RULE",
                                default_action="drop",
                                rules=[
                                    dict(
                                        number="1",
                                        action="accept",
                                        protocol="all",
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
            "delete firewall name MULTIPLE-RULE",
            "set firewall name MULTIPLE-RULE default-action 'drop'",
            "set firewall name MULTIPLE-RULE rule 1",
            "set firewall name MULTIPLE-RULE rule 1 action 'accept'",
            "set firewall name MULTIPLE-RULE rule 1 protocol 'all'",
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

    def test_vyos_firewall_v4v6_rule_sets_rule_ovr_02(self):
        """Test if plugin correctly resets the entire rule set
            while removing the absent ones if there is a change in the configuration
        """
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
                                        action="accept",
                                        protocol="udp",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="EGRESS",
                                default_action="reject",
                                description="This rule-set is configured by Ansible RM",
                                rules=[
                                    dict(
                                        number="20",
                                        action="accept",
                                        protocol="udp",
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
            "delete firewall ipv6-name V6-INGRESS",
            "delete firewall ipv6-name EGRESS",
            "delete firewall name V4-INGRESS",
            "delete firewall name EGRESS",
            "delete firewall name MULTIPLE-RULE",
            "set firewall name V4-INGRESS rule 101",
            "set firewall name V4-INGRESS description 'This is IPv4 INGRESS rule set'",
            "set firewall name V4-INGRESS default-action 'accept'",
            "set firewall name V4-INGRESS enable-default-log",
            "set firewall name V4-INGRESS rule 101 protocol 'udp'",
            "set firewall name V4-INGRESS rule 101 action 'accept'",
            "set firewall ipv6-name EGRESS description 'This rule-set is configured by Ansible RM'",
            "set firewall ipv6-name EGRESS default-action 'reject'",
            "set firewall ipv6-name EGRESS rule 20",
            "set firewall ipv6-name EGRESS rule 20 protocol 'udp'",
            "set firewall ipv6-name EGRESS rule 20 action 'accept'"
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_v4v6_rule_sets_rule_ovr_idem_01(self):
        """Test if plugin correctly has no effect if there is no change in the configuration
        """
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
                            dict(
                                name="MULTIPLE-RULE",
                                default_action="drop",
                                rules=[
                                    dict(
                                        number="1",
                                        action="accept",
                                        protocol="all",
                                    ),
                                    dict(
                                        number="2",
                                        action="drop",
                                        protocol="all",
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
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_firewall_v6_rule_sets_rule_merged_01_version(self):
        """Test if plugin correctly adds ipv6 rule set with rules
        """
        self.get_os_version.return_value = "1.3"
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
            "set firewall ipv6-name INBOUND rule 101 log 'enable'",
            "set firewall ipv6-name INBOUND rule 102",
            "set firewall ipv6-name INBOUND rule 102 action 'reject'",
            "set firewall ipv6-name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
            "set firewall ipv6-name INBOUND rule 102 protocol 'ipv6-icmp'",
            'set firewall ipv6-name INBOUND rule 102 icmpv6 type 7',
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_jump_rules_merged_01(self):
        """Test if plugin correctly adds rule set with a jump action
        """
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
            "set firewall ipv6-name INBOUND default-action 'accept'",
            "set firewall ipv6-name INBOUND description 'This is IPv6 INBOUND rule set with a jump action'",
            "set firewall ipv6-name INBOUND enable-default-log",
            "set firewall ipv6-name INBOUND rule 101 protocol 'icmp'",
            "set firewall ipv6-name INBOUND rule 101 packet-length-exclude 100",
            "set firewall ipv6-name INBOUND rule 101 packet-length-exclude 200",
            "set firewall ipv6-name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6-name INBOUND rule 101",
            "set firewall ipv6-name INBOUND rule 101 ipsec 'match-ipsec'",
            "set firewall ipv6-name INBOUND rule 101 icmpv6 type echo-request",
            "set firewall ipv6-name INBOUND rule 101 action 'jump'",
            "set firewall ipv6-name INBOUND rule 101 jump-target 'PROTECT-RE'",
            "set firewall ipv6-name INBOUND rule 102",
            "set firewall ipv6-name INBOUND rule 102 action 'reject'",
            "set firewall ipv6-name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
            "set firewall ipv6-name INBOUND rule 102 protocol 'ipv6-icmp'",
            'set firewall ipv6-name INBOUND rule 102 icmpv6 type 7',
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_log_merged_01(self):
        """Test if new stanza log is correctly applied"""
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                name="INBOUND",
                                description="This is IPv6 INBOUND rule set with a log",
                                default_action="accept",
                                enable_default_log=True,
                                rules=[
                                    dict(
                                        number="101",
                                        action="accept",
                                        description="Rule 101 is configured by Ansible",
                                        log="enable",
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
            "set firewall ipv6-name INBOUND default-action 'accept'",
            "set firewall ipv6-name INBOUND description 'This is IPv6 INBOUND rule set with a log'",
            "set firewall ipv6-name INBOUND enable-default-log",
            "set firewall ipv6-name INBOUND rule 101 log 'enable'",
            "set firewall ipv6-name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall ipv6-name INBOUND rule 101",
            "set firewall ipv6-name INBOUND rule 101 action 'accept'",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_log_replace_01(self):
        """Test that stanza is correctly replaced
            without touching the other stanzas
        """
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
                                        packet_length=[dict(length=22)],
                                        log="enable",
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
            "delete firewall name V4-INGRESS rule 101",
            "set firewall name V4-INGRESS rule 101",
            "set firewall name V4-INGRESS rule 101 action 'accept'",
            "set firewall name V4-INGRESS rule 101 description 'Rule 101 is configured by Ansible'",
            "set firewall name V4-INGRESS rule 101 packet-length-exclude 100",
            "set firewall name V4-INGRESS rule 101 packet-length-exclude 200",
            "set firewall name V4-INGRESS rule 101 packet-length 22",
            "set firewall name V4-INGRESS rule 101 log 'enable'",
        ]
        self.maxDiff = None
        self.execute_module(changed=True, commands=commands)
