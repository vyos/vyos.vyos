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

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_lldp_interfaces
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosLldpInterfacesModule(TestVyosModule):
    module = vyos_lldp_interfaces

    def setUp(self):
        super(TestVyosLldpInterfacesModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

    def tearDown(self):
        super(TestVyosLldpInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()

    def load_fixtures(self, commands=None, filename=None):
        self.get_resource_connection_facts.return_value.get_config.return_value = load_fixture(
            "vyos_lldp_interfaces_config.cfg"
        )

    # -------------------------------------------------------------------------
    # merged
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_merged_elin(self):
        """Add ELIN location to a new interface (eth3)."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        location=dict(elin="0000000912"),
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set service lldp interface eth3",
            "set service lldp interface eth3 location elin '0000000912'",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_lldp_interfaces_merged_idempotent(self):
        """Existing ELIN config — no change expected."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="0000000911"),
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_lldp_interfaces_merged_coordinate(self):
        """Add coordinate-based location to a new interface (eth3)."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth3",
                        location=dict(
                            coordinate_based=dict(
                                altitude=1500,
                                datum="WGS84",
                                latitude="33.000000N",
                                longitude="222.000000W",
                            ),
                        ),
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "set service lldp interface eth3",
            "set service lldp interface eth3 location coordinate-based altitude '1500'",
            "set service lldp interface eth3 location coordinate-based datum 'WGS84'",
            "set service lldp interface eth3 location coordinate-based latitude '33.000000N'",
            "set service lldp interface eth3 location coordinate-based longitude '222.000000W'",
        ]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # replaced
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_replaced(self):
        """Replace eth1 ELIN with a new value."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="9999999999"),
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "delete service lldp interface eth1 location",
            "set service lldp interface eth1 location elin '9999999999'",
        ]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # overridden
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_overridden(self):
        """Override: keep eth1 with same ELIN, remove eth2."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="0000000911"),
                    ),
                ],
                state="overridden",
            ),
        )
        commands = ["delete service lldp interface eth2"]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # deleted
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_deleted(self):
        """Delete LLDP config for eth1."""
        set_module_args(
            dict(
                config=[dict(name="eth1")],
                state="deleted",
            ),
        )
        commands = ["delete service lldp interface eth1"]
        self.execute_module(changed=True, commands=commands)

    # -------------------------------------------------------------------------
    # gathered
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_gathered(self):
        """Gather current LLDP interface config from device."""
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered = result["gathered"]
        names = sorted(entry["name"] for entry in gathered)
        self.assertEqual(names, ["eth1", "eth2"])

        eth1 = next(e for e in gathered if e["name"] == "eth1")
        self.assertEqual(eth1["location"]["elin"], "0000000911")

        eth2 = next(e for e in gathered if e["name"] == "eth2")
        coord = eth2["location"]["coordinate_based"]
        self.assertEqual(coord["altitude"], 2200)
        self.assertEqual(coord["datum"], "WGS84")
        self.assertEqual(coord["latitude"], "33.524449N")
        self.assertEqual(coord["longitude"], "222.267255W")

    # -------------------------------------------------------------------------
    # parsed
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_parsed(self):
        """Parse a raw config string into structured facts."""
        raw_config = (
            "set service lldp interface eth1 location elin '0000000911'\n"
            "set service lldp interface eth2 location coordinate-based altitude '2200'\n"
            "set service lldp interface eth2 location coordinate-based datum 'WGS84'\n"
            "set service lldp interface eth2 location coordinate-based latitude '33.524449N'\n"
            "set service lldp interface eth2 location coordinate-based longitude '222.267255W'\n"
        )
        set_module_args(dict(running_config=raw_config, state="parsed"))
        result = self.execute_module(changed=False)
        parsed = result["parsed"]
        names = sorted(entry["name"] for entry in parsed)
        self.assertEqual(names, ["eth1", "eth2"])

        eth1 = next(e for e in parsed if e["name"] == "eth1")
        self.assertEqual(eth1["location"]["elin"], "0000000911")

        eth2 = next(e for e in parsed if e["name"] == "eth2")
        coord = eth2["location"]["coordinate_based"]
        self.assertEqual(coord["altitude"], 2200)
        self.assertEqual(coord["datum"], "WGS84")

    # -------------------------------------------------------------------------
    # rendered
    # -------------------------------------------------------------------------

    def test_vyos_lldp_interfaces_rendered(self):
        """Render set commands without connecting to the device."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="eth1",
                        location=dict(elin="0000000911"),
                    ),
                ],
                state="rendered",
            ),
        )
        rendered_cmds = [
            "set service lldp interface eth1",
            "set service lldp interface eth1 location elin '0000000911'",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(rendered_cmds),
        )
