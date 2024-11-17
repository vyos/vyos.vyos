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

from ansible_collections.vyos.vyos.plugins.modules import vyos_firewall_global
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosFirewallGlobalModule(TestVyosModule):
    module = vyos_firewall_global

    def setUp(self):
        super(TestVyosFirewallGlobalModule, self).setUp()
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
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.firewall_global.firewall_global.Firewall_globalFacts.get_device_data",
        )

        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.firewall_global.firewall_global.get_os_version",
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "1.2"

        self.execute_show_command = self.mock_execute_show_command.start()
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosFirewallGlobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("vyos_firewall_global_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_firewall_global_set_01_merged(self):
        set_module_args(
            dict(
                config=dict(
                    validation="strict",
                    config_trap=True,
                    log_martians=True,
                    syn_cookies=True,
                    twa_hazards_protection=True,
                    ping=dict(all=True, broadcast=True),
                    state_policy=[
                        dict(
                            connection_type="established",
                            action="accept",
                            log=True,
                            log_level="emerg",
                        ),
                        dict(connection_type="invalid", action="reject"),
                    ],
                    route_redirects=[
                        dict(ip_src_route=True, afi="ipv6"),
                        dict(
                            afi="ipv4",
                            ip_src_route=True,
                            icmp_redirects=dict(send=True, receive=False),
                        ),
                    ],
                    group=dict(
                        address_group=[
                            dict(
                                afi="ipv4",
                                name="MGMT-HOSTS",
                                description="This group has the Management hosts address lists",
                                members=[
                                    dict(address="192.0.1.1"),
                                    dict(address="192.0.1.3"),
                                    dict(address="192.0.1.5"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                name="GOOGLE-DNS-v6",
                                members=[
                                    dict(address="2001:4860:4860::8888"),
                                    dict(address="2001:4860:4860::8844"),
                                ],
                            ),
                        ],
                        network_group=[
                            dict(
                                afi="ipv4",
                                name="MGMT",
                                description="This group has the Management network addresses",
                                members=[dict(address="192.0.1.0/24")],
                            ),
                            dict(
                                afi="ipv6",
                                name="DOCUMENTATION-v6",
                                description="IPv6 Addresses reserved for documentation per RFC 3849",
                                members=[
                                    dict(address="2001:0DB8::/32"),
                                    dict(address="3FFF:FFFF::/32"),
                                ],
                            ),
                        ],
                        port_group=[
                            dict(
                                name="TELNET",
                                description="This group has the telnet ports",
                                members=[dict(port="23")],
                            ),
                        ],
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set firewall group address-group MGMT-HOSTS address 192.0.1.1",
            "set firewall group address-group MGMT-HOSTS address 192.0.1.3",
            "set firewall group address-group MGMT-HOSTS address 192.0.1.5",
            "set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address lists'",
            "set firewall group address-group MGMT-HOSTS",
            "set firewall group ipv6-address-group GOOGLE-DNS-v6 address 2001:4860:4860::8888",
            "set firewall group ipv6-address-group GOOGLE-DNS-v6 address 2001:4860:4860::8844",
            "set firewall group ipv6-address-group GOOGLE-DNS-v6",
            "set firewall group network-group MGMT network 192.0.1.0/24",
            "set firewall group network-group MGMT description 'This group has the Management network addresses'",
            "set firewall group network-group MGMT",
            "set firewall group ipv6-network-group DOCUMENTATION-v6 network 2001:0DB8::/32",
            "set firewall group ipv6-network-group DOCUMENTATION-v6 network 3FFF:FFFF::/32",
            "set firewall group ipv6-network-group DOCUMENTATION-v6 description 'IPv6 Addresses reserved for documentation per RFC 3849'",
            "set firewall group ipv6-network-group DOCUMENTATION-v6",
            "set firewall group port-group TELNET port 23",
            "set firewall group port-group TELNET description 'This group has the telnet ports'",
            "set firewall group port-group TELNET",
            "set firewall ip-src-route 'enable'",
            "set firewall ipv6-src-route 'enable'",
            "set firewall receive-redirects 'disable'",
            "set firewall send-redirects 'enable'",
            "set firewall config-trap 'enable'",
            "set firewall state-policy established action 'accept'",
            "set firewall state-policy established log 'enable'",
            "set firewall state-policy invalid action 'reject'",
            "set firewall broadcast-ping 'enable'",
            "set firewall all-ping 'enable'",
            "set firewall log-martians 'enable'",
            "set firewall twa-hazards-protection 'enable'",
            "set firewall syn-cookies 'enable'",
            "set firewall source-validation 'strict'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_global_set_01_merged_idem(self):
        set_module_args(
            dict(
                config=dict(
                    group=dict(
                        address_group=[
                            dict(
                                afi="ipv4",
                                name="RND-HOSTS",
                                description="This group has the Management hosts address lists",
                                members=[
                                    dict(address="192.0.2.1"),
                                    dict(address="192.0.2.3"),
                                    dict(address="192.0.2.5"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                name="LOCAL-v6",
                                description="This group has the hosts address lists of this machine",
                                members=[
                                    dict(address="::1"),
                                    dict(address="fdec:2503:89d6:59b3::1"),
                                ],
                            ),
                        ],
                        network_group=[
                            dict(
                                afi="ipv4",
                                name="RND",
                                description="This group has the Management network addresses",
                                members=[dict(address="192.0.2.0/24")],
                            ),
                            dict(
                                afi="ipv6",
                                name="UNIQUE-LOCAL-v6",
                                description="This group encompasses the ULA address space in IPv6",
                                members=[dict(address="fc00::/7")],
                            ),
                        ],
                        port_group=[
                            dict(
                                name="SSH",
                                description="This group has the ssh ports",
                                members=[dict(port="22")],
                            ),
                        ],
                    ),
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_firewall_global_set_01_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    group=dict(
                        address_group=[
                            dict(
                                afi="ipv4",
                                name="RND-HOSTS",
                                description="This group has the Management hosts address lists",
                                members=[
                                    dict(address="192.0.2.1"),
                                    dict(address="192.0.2.7"),
                                    dict(address="192.0.2.9"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                name="LOCAL-v6",
                                description="This group has the hosts address lists of this machine",
                                members=[
                                    dict(address="::1"),
                                    dict(address="fdec:2503:89d6:59b3::2"),
                                ],
                            ),
                        ],
                        network_group=[
                            dict(
                                afi="ipv4",
                                name="RND",
                                description="This group has the Management network addresses",
                                members=[dict(address="192.0.2.0/24")],
                            ),
                            dict(
                                afi="ipv6",
                                name="UNIQUE-LOCAL-v6",
                                description="This group encompasses the ULA address space in IPv6",
                                members=[dict(address="fc00::/7")],
                            ),
                        ],
                        port_group=[
                            dict(
                                name="SSH",
                                description="This group has the ssh ports",
                                members=[dict(port="2222")],
                            ),
                        ],
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "delete firewall group address-group RND-HOSTS address 192.0.2.3",
            "delete firewall group address-group RND-HOSTS address 192.0.2.5",
            "set firewall group address-group RND-HOSTS address 192.0.2.7",
            "set firewall group address-group RND-HOSTS address 192.0.2.9",
            "delete firewall group ipv6-address-group LOCAL-v6 address fdec:2503:89d6:59b3::1",
            "set firewall group ipv6-address-group LOCAL-v6 address fdec:2503:89d6:59b3::2",
            "delete firewall group port-group SSH port 22",
            "set firewall group port-group SSH port 2222",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_global_set_01_replaced_idem(self):
        set_module_args(
            dict(
                config=dict(
                    group=dict(
                        address_group=[
                            dict(
                                afi="ipv4",
                                name="RND-HOSTS",
                                description="This group has the Management hosts address lists",
                                members=[
                                    dict(address="192.0.2.1"),
                                    dict(address="192.0.2.3"),
                                    dict(address="192.0.2.5"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                name="LOCAL-v6",
                                description="This group has the hosts address lists of this machine",
                                members=[
                                    dict(address="::1"),
                                    dict(address="fdec:2503:89d6:59b3::1"),
                                ],
                            ),
                        ],
                        network_group=[
                            dict(
                                afi="ipv4",
                                name="RND",
                                description="This group has the Management network addresses",
                                members=[dict(address="192.0.2.0/24")],
                            ),
                            dict(
                                afi="ipv6",
                                name="UNIQUE-LOCAL-v6",
                                description="This group encompasses the ULA address space in IPv6",
                                members=[dict(address="fc00::/7")],
                            ),
                        ],
                        port_group=[
                            dict(
                                name="SSH",
                                description="This group has the ssh ports",
                                members=[dict(port="22")],
                            ),
                        ],
                    ),
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_firewall_global_set_01_deleted(self):
        set_module_args(dict(config=dict(), state="deleted"))
        commands = ["delete firewall"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_global_set_01_merged_version14(self):
        self.get_os_version.return_value = "1.4"
        set_module_args(
            dict(
                config=dict(
                    validation="strict",
                    config_trap=True,
                    log_martians=True,
                    syn_cookies=True,
                    twa_hazards_protection=True,
                    ping=dict(all=True, broadcast=True),
                    state_policy=[
                        dict(
                            connection_type="established",
                            action="accept",
                            log=True,
                        ),
                        dict(connection_type="invalid", action="reject"),
                    ],
                    route_redirects=[
                        dict(
                            afi="ipv4",
                            ip_src_route=True,
                            icmp_redirects=dict(send=True, receive=False),
                        ),
                        dict(
                            afi="ipv6",
                            ip_src_route=True,
                            icmp_redirects=dict(receive=False),
                        ),
                    ],
                    group=dict(
                        address_group=[
                            dict(
                                afi="ipv4",
                                name="MGMT-HOSTS",
                                description="This group has the Management hosts address lists",
                                members=[
                                    dict(address="192.0.1.1"),
                                    dict(address="192.0.1.3"),
                                    dict(address="192.0.1.5"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                name="GOOGLE-DNS-v6",
                                members=[
                                    dict(address="2001:4860:4860::8888"),
                                    dict(address="2001:4860:4860::8844"),
                                ],
                            ),
                        ],
                        network_group=[
                            dict(
                                afi="ipv4",
                                name="MGMT",
                                description="This group has the Management network addresses",
                                members=[dict(address="192.0.1.0/24")],
                            ),
                            dict(
                                afi="ipv6",
                                name="DOCUMENTATION-v6",
                                description="IPv6 Addresses reserved for documentation per RFC 3849",
                                members=[
                                    dict(address="2001:0DB8::/32"),
                                    dict(address="3FFF:FFFF::/32"),
                                ],
                            ),
                        ],
                        port_group=[
                            dict(
                                name="TELNET",
                                description="This group has the telnet ports",
                                members=[dict(port="23")],
                            ),
                        ],
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set firewall group address-group MGMT-HOSTS address 192.0.1.1",
            "set firewall group address-group MGMT-HOSTS address 192.0.1.3",
            "set firewall group address-group MGMT-HOSTS address 192.0.1.5",
            "set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address lists'",
            "set firewall group address-group MGMT-HOSTS",
            "set firewall group ipv6-address-group GOOGLE-DNS-v6 address 2001:4860:4860::8888",
            "set firewall group ipv6-address-group GOOGLE-DNS-v6 address 2001:4860:4860::8844",
            "set firewall group ipv6-address-group GOOGLE-DNS-v6",
            "set firewall group network-group MGMT network 192.0.1.0/24",
            "set firewall group network-group MGMT description 'This group has the Management network addresses'",
            "set firewall group network-group MGMT",
            "set firewall group ipv6-network-group DOCUMENTATION-v6 network 2001:0DB8::/32",
            "set firewall group ipv6-network-group DOCUMENTATION-v6 network 3FFF:FFFF::/32",
            "set firewall group ipv6-network-group DOCUMENTATION-v6 description 'IPv6 Addresses reserved for documentation per RFC 3849'",
            "set firewall group ipv6-network-group DOCUMENTATION-v6",
            "set firewall group port-group TELNET port 23",
            "set firewall group port-group TELNET description 'This group has the telnet ports'",
            "set firewall group port-group TELNET",
            "set firewall global-options ip-src-route 'enable'",
            "set firewall global-options receive-redirects 'disable'",
            "set firewall global-options send-redirects 'enable'",
            "set firewall global-options config-trap 'enable'",
            "set firewall global-options ipv6-src-route 'enable'",
            "set firewall global-options ipv6-receive-redirects 'disable'",
            "set firewall global-options state-policy established action 'accept'",
            "set firewall global-options state-policy established log 'enable'",
            "set firewall global-options state-policy invalid action 'reject'",
            "set firewall global-options broadcast-ping 'enable'",
            "set firewall global-options all-ping 'enable'",
            "set firewall global-options log-martians 'enable'",
            "set firewall global-options twa-hazards-protection 'enable'",
            "set firewall global-options syn-cookies 'enable'",
            "set firewall global-options source-validation 'strict'",
        ]
        self.execute_module(changed=True, commands=commands)
