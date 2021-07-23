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
from ansible_collections.vyos.vyos.plugins.modules import vyos_firewall_rules
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    set_module_args,
)
from .vyos_module import TestVyosModule, load_fixture


class TestVyosFirewallRulesModule(TestVyosModule):

    module = vyos_firewall_rules

    def setUp(self):
        super(TestVyosFirewallRulesModule, self).setUp()
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
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.static_routes.static_routes.Static_routesFacts.get_device_data"
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.firewall_rules.firewall_rules.Firewall_rulesFacts.get_device_data"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosFirewallRulesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("issue170_vyos_firewall_rules.cfg")

        self.execute_show_command.side_effect = load_from_file


    def vyos_firewall_rule_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[                           
                            dict(
                                icmp= dict(
                                    type_name= "echo-request"
                                )
                            ),
                        ],
                    ),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])


    def vyos_firewall_rule_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[ 
                            dict(
                                rules=[ 
                                    dict(
                                        icmp= dict(
                                            type_name= "echo-request"
                                            )
                                    )
                                ] 
                            )       
                            
                        ],
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20 icmpv6 type echo-request"
        ]
        self.execute_module(changed=True, commands=commands)





    """ def test_vyos_firewall_rule_set_01_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        rule_sets=[
                            dict(
                                default_action="drop",
                                description="local WAN rulesset",
                                name="V6-OUTSIDE-LOCAL",
                                rules=[
                                    dict(
                                        action="accept",
                                        description="rule 10 configured by ansible",
                                        number=10,
                                        state=dict(
                                            established="true",
                                            related="true"
                                        )
                                    ),
                                    dict(
                                        action="accept",
                                        description="rule 20 configured by ansible",
                                        icmp= dict(
                                            type_name="echo-request"
                                        ),
                                        number=20,
                                        protocol="icmp",
                                        state=dict(
                                            new="true"
                                        )
                                    )
                                ]
                            )
                        ],
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "set firewall ipv6-name V6-OUTSIDE-LOCAL description 'local WAN ruleset'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL default-action 'drop'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 10",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 10 action 'accept'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 10 description 'rule 10 configured by ansible'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 10 state established enable",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 10 state related enable",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20 action 'accept'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20 protocol 'icmp'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20 icmpv6 type echo-request",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20 description 'rule 20 configured by ansible'",
            "set firewall ipv6-name V6-OUTSIDE-LOCAL rule 20 state new enable"

        ]
        self.execute_module(changed=True, commands=commands) """

