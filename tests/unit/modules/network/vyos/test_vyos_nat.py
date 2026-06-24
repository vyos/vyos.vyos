# (c) 2024 Red Hat Inc.
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

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_nat
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosNatModule(TestVyosModule):
    module = vyos_nat

    def setUp(self):
        super(TestVyosNatModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.nat.nat.NatFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosNatModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_nat_config.cfg"

        def load_from_file(*args, **kwargs):
            return load_fixture(filename)

        self.execute_show_command.side_effect = load_from_file

    # -------------------------------------------------------------------------
    # merged
    # -------------------------------------------------------------------------

    def test_vyos_nat_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        cgnat=dict(
                            log_allocation=True,
                            pool=dict(
                                external=[
                                    dict(
                                        name="ext-pool-1",
                                        external_port_range="10000-20000",
                                        per_user_limit=dict(port="200"),
                                        range=[
                                            dict(value="203.0.113.0/24"),
                                            dict(value="203.1.113.1-203.1.113.60", seq="10"),
                                        ],
                                    ),
                                ],
                                internal=[
                                    dict(
                                        name="int-pool-1",
                                        range=["10.0.0.0/24", "10.1.0.0/24"],
                                    ),
                                ],
                            ),
                            rule=[
                                dict(
                                    id=1,
                                    source=dict(pool="int-pool-1"),
                                    translation=dict(pool="ext-pool-1"),
                                ),
                            ],
                        ),
                        destination=dict(
                            rule=[
                                dict(
                                    id=100,
                                    description="Web server NAT",
                                    protocol="tcp",
                                    log=True,
                                    inbound_interface=dict(name="eth2"),
                                    destination=dict(address="198.51.100.10", port="80"),
                                    translation=dict(
                                        address="192.168.1.10",
                                        port="8080",
                                        address_mapping="persistent",
                                        port_mapping="random",
                                    ),
                                ),
                            ],
                        ),
                        source=dict(
                            rule=[
                                dict(
                                    id=200,
                                    description="Outbound NAT",
                                    protocol="tcp",
                                    log=True,
                                    exclude=True,
                                    disable=True,
                                    destination=dict(address="192.168.10.100", port="8083"),
                                    translation=dict(address="masquerade", port="443"),
                                ),
                            ],
                        ),
                        static=dict(
                            rule=[
                                dict(
                                    id=300,
                                    description="Static mapping",
                                    inbound_interface="eth2",
                                    destination=dict(address="192.168.100.20"),
                                    translation=dict(address="192.168.1.20"),
                                    log=True,
                                ),
                            ],
                        ),
                    ),
                    nat64=dict(
                        source=dict(
                            rule=[
                                dict(
                                    id=10,
                                    description="NAT64 example",
                                    disable=True,
                                    match=dict(mark=100),
                                    source=dict(prefix="2001:db8::/96"),
                                    translation=dict(
                                        pool=[
                                            dict(
                                                id=1,
                                                address="192.168.100.10",
                                                description="NAT64 translacton pool",
                                                disable=True,
                                                port="1-65535",
                                                protocol="udp",
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                    nat66=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=20,
                                    description="NAT66 DNAT",
                                    protocol="tcp",
                                    inbound_interface=dict(name="eth1"),
                                    destination=dict(address="2001:db8::1"),
                                    translation=dict(address="2001:db8:1::10", port="8443"),
                                ),
                            ],
                        ),
                        source=dict(
                            rule=[
                                dict(
                                    id=30,
                                    description="NAT66 SNAT",
                                    protocol="tcp",
                                    destination=dict(prefix="2001:db8::/96"),
                                    outbound_interface=dict(name="eth2"),
                                    source=dict(prefix="2001:db8:2::/64"),
                                    translation=dict(address="masquerade"),
                                ),
                            ],
                        ),
                    ),
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_nat_merged_new_rule(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=101,
                                    description="New DNAT rule",
                                    protocol="tcp",
                                    destination=dict(address="198.51.100.11", port="443"),
                                    translation=dict(address="192.168.1.11", port="8443"),
                                ),
                            ],
                        ),
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set nat destination rule 101 description 'New DNAT rule'",
            "set nat destination rule 101 protocol tcp",
            "set nat destination rule 101 destination address 198.51.100.11",
            "set nat destination rule 101 destination port 443",
            "set nat destination rule 101 translation address 192.168.1.11",
            "set nat destination rule 101 translation port 8443",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_merged_update_existing_rule(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=100,
                                    description="Updated DNAT rule",
                                    protocol="tcp",
                                    inbound_interface=dict(name="eth2"),
                                    destination=dict(address="198.51.100.10", port="80"),
                                    translation=dict(
                                        address="192.168.1.10",
                                        port="8080",
                                        address_mapping="persistent",
                                        port_mapping="random",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set nat destination rule 100 description 'Updated DNAT rule'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_merged_cgnat_new_pool(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        cgnat=dict(
                            pool=dict(
                                external=[
                                    dict(
                                        name="ext-pool-2",
                                        external_port_range="30000-40000",
                                        range=[dict(value="203.0.114.0/24")],
                                    ),
                                ],
                            ),
                        ),
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set nat cgnat pool external ext-pool-2 external-port-range 30000-40000",
            "set nat cgnat pool external ext-pool-2 range 203.0.114.0/24",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_merged_nat66_new_rule(self):
        set_module_args(
            dict(
                config=dict(
                    nat66=dict(
                        source=dict(
                            rule=[
                                dict(
                                    id=31,
                                    description="New NAT66 SNAT",
                                    protocol="udp",
                                    outbound_interface=dict(name="eth3"),
                                    source=dict(prefix="2001:db8:3::/64"),
                                    translation=dict(address="masquerade"),
                                ),
                            ],
                        ),
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set nat66 source rule 31 description 'New NAT66 SNAT'",
            "set nat66 source rule 31 protocol udp",
            "set nat66 source rule 31 outbound-interface name eth3",
            "set nat66 source rule 31 source prefix 2001:db8:3::/64",
            "set nat66 source rule 31 translation address masquerade",
        ]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # deleted
    # -------------------------------------------------------------------------

    def test_vyos_nat_deleted_all(self):
        set_module_args(dict(state="deleted"))
        commands = [
            "delete nat",
            "delete nat64",
            "delete nat66",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_deleted_specific_rules(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(rule=[dict(id=100)]),
                        source=dict(rule=[dict(id=200)]),
                    ),
                ),
                state="deleted",
            ),
        )
        commands = [
            "delete nat destination rule 100",
            "delete nat source rule 200",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_deleted_cgnat_pool(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        cgnat=dict(
                            pool=dict(
                                external=[dict(name="ext-pool-1")],
                                internal=[dict(name="int-pool-1")],
                            ),
                        ),
                    ),
                ),
                state="deleted",
            ),
        )
        commands = [
            "delete nat cgnat pool external ext-pool-1",
            "delete nat cgnat pool internal int-pool-1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_deleted_nat64_rule(self):
        set_module_args(
            dict(
                config=dict(
                    nat64=dict(
                        source=dict(rule=[dict(id=10)]),
                    ),
                ),
                state="deleted",
            ),
        )
        commands = ["delete nat64 source rule 10"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nat_deleted_nonexistent_rule(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(rule=[dict(id=999)]),
                    ),
                ),
                state="deleted",
            ),
        )
        self.execute_module(changed=False, commands=[])

    # -------------------------------------------------------------------------
    # replaced
    # -------------------------------------------------------------------------

    def test_vyos_nat_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=100,
                                    description="Web server NAT",
                                    protocol="tcp",
                                    log=True,
                                    inbound_interface=dict(name="eth2"),
                                    destination=dict(address="198.51.100.10", port="80"),
                                    translation=dict(
                                        address="192.168.1.10",
                                        port="8080",
                                        address_mapping="persistent",
                                        port_mapping="random",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_nat_replaced_rule(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=100,
                                    description="Replaced DNAT rule",
                                    protocol="udp",
                                    destination=dict(address="198.51.100.10", port="53"),
                                    translation=dict(address="192.168.1.53", port="53"),
                                ),
                            ],
                        ),
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "delete nat destination rule 100",
            "set nat destination rule 100 description 'Replaced DNAT rule'",
            "set nat destination rule 100 protocol udp",
            "set nat destination rule 100 destination address 198.51.100.10",
            "set nat destination rule 100 destination port 53",
            "set nat destination rule 100 translation address 192.168.1.53",
            "set nat destination rule 100 translation port 53",
        ]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # overridden
    # -------------------------------------------------------------------------

    def test_vyos_nat_overridden_remove_sections(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=100,
                                    description="Overridden web server NAT",  # changed
                                    protocol="tcp",
                                    inbound_interface=dict(name="eth3"),  # changed
                                    destination=dict(address="198.51.100.10", port="80"),
                                    translation=dict(
                                        address="192.168.1.10",
                                        port="8080",
                                    ),
                                ),
                            ],
                        ),
                    ),
                ),
                state="overridden",
            ),
        )
        commands = [
            "delete nat cgnat",
            "delete nat source",
            "delete nat static",
            "delete nat64",
            "delete nat66",
            "delete nat destination rule 100",
            "set nat destination rule 100 description 'Overridden web server NAT'",
            "set nat destination rule 100 protocol tcp",
            "set nat destination rule 100 inbound-interface name eth3",
            "set nat destination rule 100 destination address 198.51.100.10",
            "set nat destination rule 100 destination port 80",
            "set nat destination rule 100 translation address 192.168.1.10",
            "set nat destination rule 100 translation port 8080",
        ]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # rendered
    # -------------------------------------------------------------------------

    def test_vyos_nat_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    nat=dict(
                        destination=dict(
                            rule=[
                                dict(
                                    id=100,
                                    description="Rendered rule",
                                    protocol="tcp",
                                    destination=dict(address="198.51.100.10", port="80"),
                                    translation=dict(address="192.168.1.10", port="8080"),
                                ),
                            ],
                        ),
                    ),
                ),
                state="rendered",
            ),
        )
        rendered_cmds = [
            "set nat destination rule 100 description 'Rendered rule'",
            "set nat destination rule 100 protocol tcp",
            "set nat destination rule 100 destination address 198.51.100.10",
            "set nat destination rule 100 destination port 80",
            "set nat destination rule 100 translation address 192.168.1.10",
            "set nat destination rule 100 translation port 8080",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered_cmds), result["rendered"])

    # -------------------------------------------------------------------------
    # parsed
    # -------------------------------------------------------------------------

    def test_vyos_nat_parsed(self):
        parsed_str = (
            "set nat destination rule 100 description 'Web server NAT'\n"
            "set nat destination rule 100 destination address '198.51.100.10'\n"
            "set nat destination rule 100 destination port '80'\n"
            "set nat destination rule 100 inbound-interface name 'eth2'\n"
            "set nat destination rule 100 log\n"
            "set nat destination rule 100 protocol 'tcp'\n"
            "set nat destination rule 100 translation address '192.168.1.10'\n"
            "set nat destination rule 100 translation port '8080'"
        )
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "nat": {
                "destination": {
                    "rule": [
                        {
                            "id": 100,
                            "description": "Web server NAT",
                            "protocol": "tcp",
                            "log": True,
                            "inbound_interface": {"name": "eth2"},
                            "destination": {"address": "198.51.100.10", "port": "80"},
                            "translation": {"address": "192.168.1.10", "port": "8080"},
                        },
                    ],
                },
            },
        }
        self.assertEqual(parsed_list, result["parsed"])

    # -------------------------------------------------------------------------
    # gathered
    # -------------------------------------------------------------------------

    def test_vyos_nat_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered = result["gathered"]
        self.assertIn("nat", gathered)
        self.assertIn("nat64", gathered)
        self.assertIn("nat66", gathered)
        self.assertEqual(gathered["nat"]["destination"]["rule"][0]["id"], 100)
        self.assertEqual(gathered["nat64"]["source"]["rule"][0]["id"], 10)
        self.assertEqual(gathered["nat66"]["destination"]["rule"][0]["id"], 20)
