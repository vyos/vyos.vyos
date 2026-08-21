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


class TestVyosFirewallRulesModule15(TestVyosModule):
    module = vyos_firewall_global

    def setUp(self):
        super(TestVyosFirewallRulesModule15, self).setUp()
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
        self.get_os_version.return_value = "1.5"

        self.execute_show_command = self.mock_execute_show_command.start()
        self.maxDiff = None

    def tearDown(self):
        super(TestVyosFirewallRulesModule15, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()

    def load_fixtures(self, commands=None, filename=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("vyos_firewall_global_config_v15.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_firewall_global_set_01_merged_interface_uses_member_keyword(self):
        # On a 1.5.0 device (empty fixture, no existing zone), merging a
        # zone with an interface should render "member interface", not the
        # bare "interface" used on 1.4.x / 1.5-rolling. This is the sole
        # thing this class exists to prove right now -- the version-gate
        # added to _render_interfaces.
        set_module_args(
            dict(
                config=dict(
                    zone=[
                        dict(
                            name="ZONE-15",
                            interfaces=["eth1"],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = [
            "set firewall zone ZONE-15 default-action 'drop'",
            "set firewall zone ZONE-15 member interface eth1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_firewall_global_set_02_gathered_member_interface_parsed(self):
        # ZONE-15-EXISTING in the fixture uses 1.5.0's "member interface"
        # syntax. Before the parse_zone fix, this misparsed into a bogus
        # zone['member'] = "interface eth2" string field, and 'interfaces'
        # was missing entirely. After the fix, it should land in
        # 'interfaces' exactly like the pre-1.5.0 bare "interface" form.
        set_module_args(dict(config=dict(), state="gathered"))
        result = self.execute_module(changed=False)
        zones = result["gathered"]["zone"]
        zone = next(z for z in zones if z["name"] == "ZONE-15-EXISTING")
        self.assertEqual(zone["interfaces"], ["eth2"])
        self.assertEqual(zone["description"], "existing 1.5.0 zone for facts parsing test")
        self.assertNotIn("member", zone)

    def test_vyos_firewall_global_ruleset_lines_filtered_from_facts(self):
        # Same coverage as the 1.4 version, confirmed independently on the
        # 1.5.0 fixture/version path.
        set_module_args(dict(config=dict(), state="gathered"))
        result = self.execute_module(changed=False)
        facts = result["gathered"]
        self.assertNotIn("TESTRULESET-V4", str(facts))
        self.assertNotIn("TESTRULESET-V6-LEGACY", str(facts))
        self.assertNotIn("TESTRULESET-V6-1_4PLUS", str(facts))
