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

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_vlan
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule


SHOW_INTERFACES_OUTPUT = """\
Codes: S - State, L - Link, u - Up, D - Down, A - Admin Down
Interface        IP Address                        S/L  Description
---------        ----------                        ---  -----------
eth0             10.0.2.15/24                      u/u
eth0.100         -                                 u/u  vlan-100
eth1             -                                 u/u
eth1.200         192.0.2.1/24                      u/u  vlan-200
eth2             -                                 u/u
lo               127.0.0.1/8                       u/u
                 ::1/128
"""


class TestVyosVlanModule(TestVyosModule):
    module = vyos_vlan

    def setUp(self):
        super(TestVyosVlanModule, self).setUp()

        self.mock_load_config = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_vlan.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_run_commands = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_vlan.run_commands",
        )
        self.run_commands = self.mock_run_commands.start()

    def tearDown(self):
        super(TestVyosVlanModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_run_commands.stop()

    def load_fixtures(self, commands=None, filename=None):
        self.load_config.return_value = dict(diff=None, session="session")
        self.run_commands.return_value = [SHOW_INTERFACES_OUTPUT]

    def test_vyos_vlan_purge_no_bare_interfaces(self):
        """Purge should only delete VLANs, not bare interfaces without vlan_id."""
        set_module_args(
            dict(
                vlan_id=100,
                interfaces=["eth0"],
                state="present",
                purge=True,
            ),
        )
        result = self.execute_module(changed=True)
        # Should only delete eth1.200, not bare eth0/eth1/eth2 with vif None
        for cmd in result.get("commands", []):
            self.assertNotIn(
                "vif None",
                cmd,
                "Purge generated 'vif None' command for bare interface: {0}".format(cmd),
            )
        # eth1.200 should be purged since it's not in the desired state
        self.assertIn(
            "delete interfaces ethernet eth1 vif 200",
            result.get("commands", []),
        )

    def test_vyos_vlan_present(self):
        set_module_args(
            dict(
                vlan_id=300,
                name="vlan-300",
                interfaces=["eth2"],
                state="present",
            ),
        )
        commands = [
            "set interfaces ethernet eth2 vif 300 description vlan-300",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_absent(self):
        set_module_args(
            dict(
                vlan_id=100,
                interfaces=["eth0"],
                state="absent",
            ),
        )
        commands = [
            "delete interfaces ethernet eth0 vif 100",
        ]
        self.execute_module(changed=True, commands=commands)
