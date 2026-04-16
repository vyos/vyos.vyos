# (c) 2024 VyOS Networks <maintainers@vyos.net>
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

from ansible_collections.vyos.vyos.plugins.modules import vyos_vlan
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule


# show interfaces output with eth0.100 (vlan 100, description vlan-100)
# and eth1.200 (vlan 200, ip 192.0.2.1/24, description vlan-200).
# The parser skips the first 3 lines (Codes line, header, dashes).
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

# Empty show interfaces — no VLANs configured.
SHOW_INTERFACES_EMPTY = """\
Codes: S - State, L - Link, u - Up, D - Down, A - Admin Down
Interface        IP Address                        S/L  Description
---------        ----------                        ---  -----------
eth0             10.0.2.15/24                      u/u
eth1             -                                 u/u
eth2             -                                 u/u
lo               127.0.0.1/8                       u/u
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
        if filename == "empty":
            self.run_commands.return_value = [SHOW_INTERFACES_EMPTY]
        else:
            self.run_commands.return_value = [SHOW_INTERFACES_OUTPUT]

    def test_vyos_vlan_present(self):
        """Create a new VLAN with a description on eth2 (not in have)."""
        set_module_args(
            dict(
                vlan_id=300,
                name="vlan-300",
                interfaces=["eth2"],
                state="present",
            )
        )
        commands = ["set interfaces ethernet eth2 vif 300 description vlan-300"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_present_no_change(self):
        """Existing VLAN 100 on eth0 — no commands should be generated."""
        set_module_args(
            dict(
                vlan_id=100,
                name="vlan-100",
                interfaces=["eth0"],
                state="present",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_vlan_absent(self):
        """Delete an existing VLAN (200 on eth1)."""
        set_module_args(
            dict(
                vlan_id=200,
                interfaces=["eth1"],
                state="absent",
            )
        )
        commands = ["delete interfaces ethernet eth1 vif 200"]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_absent_no_change(self):
        """Delete a VLAN that does not exist — no commands."""
        set_module_args(
            dict(
                vlan_id=999,
                interfaces=["eth0"],
                state="absent",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_vlan_aggregate(self):
        """Create two new VLANs via aggregate; neither is in have."""
        set_module_args(
            dict(
                aggregate=[
                    dict(vlan_id=301, interfaces=["eth2"], name="vlan-301"),
                    dict(vlan_id=302, interfaces=["eth2"], name="vlan-302"),
                ],
            )
        )
        commands = [
            "set interfaces ethernet eth2 vif 301 description vlan-301",
            "set interfaces ethernet eth2 vif 302 description vlan-302",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_purge(self):
        """Purge VLANs not in want. Want only VLAN 100; VLAN 200 should be removed.

        The fixed parser only maps ethX.Y sub-interfaces, so bare ethX interfaces
        (vlan_id=None) are not in have. Only real VLANs (eth1.200) are purged.
        """
        set_module_args(
            dict(
                vlan_id=100,
                interfaces=["eth0"],
                state="present",
                purge=True,
            )
        )
        # VLAN 100 already exists — no create command.
        # Only eth1.200 (vlan_id=200) is purged; bare interfaces are excluded.
        commands = [
            "delete interfaces ethernet eth1 vif 200",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vlan_with_address(self):
        """Create a VLAN with an IP address and no description."""
        set_module_args(
            dict(
                vlan_id=400,
                address="10.10.40.1/24",
                interfaces=["eth1"],
                state="present",
            )
        )
        commands = ["set interfaces ethernet eth1 vif 400 address 10.10.40.1/24"]
        self.execute_module(changed=True, commands=commands, filename="empty")
