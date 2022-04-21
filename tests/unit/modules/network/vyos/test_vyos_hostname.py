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
from ansible_collections.vyos.vyos.plugins.modules import vyos_hostname
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    set_module_args,
)
from .vyos_module import TestVyosModule, load_fixture


class TestVyosHostnameModule(TestVyosModule):

    module = vyos_hostname

    def setUp(self):
        super(TestVyosHostnameModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
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
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.hostname.hostname.HostnameFacts.get_config"
        )

        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosHostnameModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None, transport="cli", filename=None):
        if filename is None:
            filename = "vyos_hostname_config.cfg"

        def load_from_file(*args, **kwargs):
            output = load_fixture(filename)
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_vyos_hostname_merged_idempotent(self):
        set_module_args(dict(config=dict(hostname="vyos_test")))
        self.execute_module(changed=False, commands=[])

    def test_vyos_hostname_replaced_idempotent(self):
        set_module_args(
            dict(config=dict(hostname="vyos_test"), state="replaced")
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_hostname_overridden_idempotent(self):
        set_module_args(
            dict(config=dict(hostname="vyos_test"), state="overridden")
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_hostname_merged(self):
        set_module_args(dict(config=dict(hostname="vyos")))
        self.execute_module(
            changed=True, commands=["set system host-name vyos"]
        )

    def test_vyos_hostname_replaced(self):
        set_module_args(dict(config=dict(hostname="vyos"), state="replaced"))
        self.execute_module(
            changed=True, commands=["set system host-name vyos"]
        )

    def test_vyos_hostname_overridden(self):
        set_module_args(dict(config=dict(hostname="vyos"), state="overridden"))

    def test_vyos_hostname_deleted(self):
        set_module_args(dict(state="deleted"))
        self.execute_module(
            changed=True, commands=["delete system host-name vyos_test"]
        )

    def test_vyos_hostname_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(
            changed=False, filename="vyos_hostname_config.cfg"
        )
        gathered_list = {"hostname": "vyos_test"}
        self.assertEqual(sorted(gathered_list), sorted(result["gathered"]))

    def test_vyos_hostname_parsed(self):
        parsed_str = "set system host-name vyos_test"
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {"hostname": "vyos_test"}
        self.assertEqual(sorted(parsed_list), sorted(result["parsed"]))

    def test_vyos_hostname_rendered(self):
        set_module_args(
            dict(state="rendered", config=dict(hostname="vyos_test"))
        )
        commands = ["set system host-name vyos_test"]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]), sorted(commands), result["rendered"]
        )
