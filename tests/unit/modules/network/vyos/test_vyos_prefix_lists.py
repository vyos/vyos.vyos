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

from textwrap import dedent
from ansible_collections.vyos.vyos.tests.unit.compat.mock import patch
from ansible_collections.vyos.vyos.plugins.modules import vyos_prefix_lists
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    set_module_args,
)
from .vyos_module import TestVyosModule


class TestVyosPrefixListsModule(TestVyosModule):

    # Testing strategy
    # ------------------
    # (a) The unit tests cover `merged` and `replaced` for every attribute.
    #     Since `overridden` is essentially `replaced` but at a larger
    #     scale, these indirectly cover `overridden` as well.
    # (b) For linear attributes replaced is not valid and hence, those tests
    #     delete the attributes from the config subsection.
    # (c) The argspec for VRFs is same as the top-level spec and the config logic
    #     is re-used. Hence, those attributes are not explictly covered. However, a
    #     combination of VRF + top-level spec + AF is tested.

    module = vyos_prefix_lists

    def setUp(self):
        super(TestVyosPrefixListsModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection = (
            self.mock_get_resource_connection.start()
        )

        self.mock_get_config = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.prefix_lists.prefix_lists.Prefix_listsFacts.get_config"
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestVyosPrefixListsModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    # test merged for linear attributes
    def test_vyos_prefix_lists_linear_merged(self):
        self.get_config.return_value = dedent(
            """\
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist1",
                                description="Test plist1",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="permit",
                                        description="Test rule 10",
                                        prefix="92.168.10.0/26",
                                    ),
                                    dict(
                                        sequence=20,
                                        action="deny",
                                        description="Test rule 20",
                                        prefix="72.168.2.0/24",
                                    ),
                                ],
                            ),
                            dict(
                                name="plist2",
                                entries=[
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        prefix="82.168.10.0/26",
                                        le=32,
                                    ),
                                    dict(
                                        sequence=30,
                                        action="deny",
                                        prefix="62.168.2.0/24",
                                        ge=25,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="plist3",
                                description="Test plist3",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        description="Test rule 10",
                                        prefix="2001:db8:1000::/36",
                                        le=36,
                                    ),
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        description="Test rule 20",
                                        prefix="2001:db8:2000::/36",
                                    ),
                                ],
                            ),
                            dict(
                                name="plist4",
                                entries=[
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        prefix="2001:db8:3000::/36",
                                    ),
                                    dict(
                                        sequence=50,
                                        action="deny",
                                        prefix="2001:db8:4000::/36",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "set policy prefix-list plist1",
            "set policy prefix-list plist1 description 'Test plist1'",
            "set policy prefix-list plist1 rule 10",
            "set policy prefix-list plist1 rule 10 action 'permit'",
            "set policy prefix-list plist1 rule 10 description 'Test rule 10'",
            "set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'",
            "set policy prefix-list plist1 rule 20",
            "set policy prefix-list plist1 rule 20 action 'deny'",
            "set policy prefix-list plist1 rule 20 description 'Test rule 20'",
            "set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'",
            "set policy prefix-list plist2",
            "set policy prefix-list plist2 rule 20",
            "set policy prefix-list plist2 rule 20 action 'permit'",
            "set policy prefix-list plist2 rule 20 le '32'",
            "set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'",
            "set policy prefix-list plist2 rule 30",
            "set policy prefix-list plist2 rule 30 action 'deny'",
            "set policy prefix-list plist2 rule 30 ge '25'",
            "set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'",
            "set policy prefix-list6 plist3",
            "set policy prefix-list6 plist3 description 'Test plist3'",
            "set policy prefix-list6 plist3 rule 10",
            "set policy prefix-list6 plist3 rule 10 action 'deny'",
            "set policy prefix-list6 plist3 rule 10 description 'Test rule 10'",
            "set policy prefix-list6 plist3 rule 10 le '36'",
            "set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'",
            "set policy prefix-list6 plist3 rule 20",
            "set policy prefix-list6 plist3 rule 20 action 'permit'",
            "set policy prefix-list6 plist3 rule 20 description 'Test rule 20'",
            "set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'",
            "set policy prefix-list6 plist4",
            "set policy prefix-list6 plist4 rule 20",
            "set policy prefix-list6 plist4 rule 20 action 'permit'",
            "set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'",
            "set policy prefix-list6 plist4 rule 50",
            "set policy prefix-list6 plist4 rule 50 action 'deny'",
            "set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test merged for linear attributes (idempotent)
    def test_vyos_prefix_lists_linear_merged_idempotent(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist1",
                                description="Test plist1",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="permit",
                                        description="Test rule 10",
                                        prefix="92.168.10.0/26",
                                    ),
                                    dict(
                                        sequence=20,
                                        action="deny",
                                        description="Test rule 20",
                                        prefix="72.168.2.0/24",
                                    ),
                                ],
                            ),
                            dict(
                                name="plist2",
                                entries=[
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        prefix="82.168.10.0/26",
                                        le=32,
                                    ),
                                    dict(
                                        sequence=30,
                                        action="deny",
                                        prefix="62.168.2.0/24",
                                        ge=25,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="plist3",
                                description="Test plist3",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        description="Test rule 10",
                                        prefix="2001:db8:1000::/36",
                                        le=36,
                                    ),
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        description="Test rule 20",
                                        prefix="2001:db8:2000::/36",
                                    ),
                                ],
                            ),
                            dict(
                                name="plist4",
                                entries=[
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        prefix="2001:db8:3000::/36",
                                    ),
                                    dict(
                                        sequence=50,
                                        action="deny",
                                        prefix="2001:db8:4000::/36",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            )
        )
        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    # test existing rule with replaced
    def test_vyos_prefix_lists_replaced_update(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist1",
                                description="Test plist1",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="permit",
                                        prefix="82.168.10.0/26",
                                    ),
                                    dict(
                                        sequence=20,
                                        action="deny",
                                        description="Test rule 20",
                                        prefix="72.168.2.0/24",
                                    ),
                                ],
                            )
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "delete policy prefix-list plist1 rule 10 description 'Test rule 10'",
            "set policy prefix-list plist1 rule 10 prefix '82.168.10.0/26'",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test replaced
    def test_vyos_prefix_lists_replaced(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist1",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="permit",
                                        prefix="82.168.10.0/26",
                                    )
                                ],
                            )
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "delete policy prefix-list plist1 description 'Test plist1'",
            "set policy prefix-list plist1 rule 10 prefix '82.168.10.0/26'",
            "delete policy prefix-list plist1 rule 20",
            "delete policy prefix-list plist1 rule 10 description 'Test rule 10'",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test update with overridden
    def test_vyos_prefix_lists_overridden_update(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist1",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        prefix="102.168.10.0/26",
                                    )
                                ],
                            )
                        ],
                    )
                ],
                state="overridden",
            )
        )
        commands = [
            "delete policy prefix-list plist1 description 'Test plist1'",
            "delete policy prefix-list6 plist4",
            "delete policy prefix-list plist1 rule 10 description 'Test rule 10'",
            "set policy prefix-list plist1 rule 10 prefix '102.168.10.0/26'",
            "delete policy prefix-list6 plist3",
            "delete policy prefix-list plist1 rule 20",
            "set policy prefix-list plist1 rule 10 action 'deny'",
            "delete policy prefix-list plist2",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test overridden
    def test_vyos_prefix_lists_overridden(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist5",
                                entries=[
                                    dict(
                                        sequence=50,
                                        action="permit",
                                        prefix="102.168.10.0/26",
                                    )
                                ],
                            )
                        ],
                    )
                ],
                state="overridden",
            )
        )
        commands = [
            "set policy prefix-list plist5",
            "set policy prefix-list plist5 rule 50",
            "set policy prefix-list plist5 rule 50 action 'permit'",
            "set policy prefix-list plist5 rule 50 prefix '102.168.10.0/26'",
            "delete policy prefix-list plist1",
            "delete policy prefix-list plist2",
            "delete policy prefix-list6 plist3",
            "delete policy prefix-list6 plist4",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test deleted (all)
    def test_vyos_prefix_lists_deleted_all(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(dict(state="deleted"))
        commands = [
            "delete policy prefix-list plist1",
            "delete policy prefix-list plist2",
            "delete policy prefix-list6 plist3",
            "delete policy prefix-list6 plist4",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test deleted (AFI)
    def test_vyos_prefix_lists_deleted_afi(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(dict(config=[dict(afi="ipv4")], state="deleted"))
        commands = [
            "delete policy prefix-list plist1",
            "delete policy prefix-list plist2",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test deleted (one prefix-list)
    def test_vyos_prefix_lists_deleted_one(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[dict(afi="ipv6", prefix_lists=[dict(name="plist3")])],
                state="deleted",
            )
        )
        commands = ["delete policy prefix-list6 plist3"]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test deleted (one prefix-list from each AFI)
    def test_vyos_prefix_lists_deleted_one_from_each_afi(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(
            dict(
                config=[
                    dict(afi="ipv4", prefix_lists=[dict(name="plist2")]),
                    dict(afi="ipv6", prefix_lists=[dict(name="plist3")]),
                ],
                state="deleted",
            )
        )
        commands = [
            "delete policy prefix-list plist2",
            "delete policy prefix-list6 plist3",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    # test parsed
    def test_vyos_prefix_lists_parsed(self):
        cfg = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(dict(running_config=cfg, state="parsed"))
        parsed = [
            {
                "afi": "ipv4",
                "prefix_lists": [
                    {
                        "description": "Test plist1",
                        "name": "plist1",
                        "entries": [
                            {
                                "action": "permit",
                                "description": "Test rule 10",
                                "sequence": 10,
                                "prefix": "92.168.10.0/26",
                            },
                            {
                                "action": "deny",
                                "description": "Test rule 20",
                                "sequence": 20,
                                "prefix": "72.168.2.0/24",
                            },
                        ],
                    },
                    {
                        "name": "plist2",
                        "entries": [
                            {
                                "action": "permit",
                                "sequence": 20,
                                "le": 32,
                                "prefix": "82.168.10.0/26",
                            },
                            {
                                "action": "deny",
                                "ge": 25,
                                "sequence": 30,
                                "prefix": "62.168.2.0/24",
                            },
                        ],
                    },
                ],
            },
            {
                "afi": "ipv6",
                "prefix_lists": [
                    {
                        "description": "Test plist3",
                        "name": "plist3",
                        "entries": [
                            {
                                "action": "deny",
                                "description": "Test rule 10",
                                "sequence": 10,
                                "le": 36,
                                "prefix": "2001:db8:1000::/36",
                            },
                            {
                                "action": "permit",
                                "description": "Test rule 20",
                                "sequence": 20,
                                "prefix": "2001:db8:2000::/36",
                            },
                        ],
                    },
                    {
                        "name": "plist4",
                        "entries": [
                            {
                                "action": "permit",
                                "sequence": 20,
                                "prefix": "2001:db8:3000::/36",
                            },
                            {
                                "action": "deny",
                                "sequence": 50,
                                "prefix": "2001:db8:4000::/36",
                            },
                        ],
                    },
                ],
            },
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(result["parsed"], parsed)

    # test rendered
    def test_vyos_prefix_lists_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="plist1",
                                description="Test plist1",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="permit",
                                        description="Test rule 10",
                                        prefix="92.168.10.0/26",
                                    ),
                                    dict(
                                        sequence=20,
                                        action="deny",
                                        description="Test rule 20",
                                        prefix="72.168.2.0/24",
                                    ),
                                ],
                            ),
                            dict(
                                name="plist2",
                                entries=[
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        prefix="82.168.10.0/26",
                                        le=32,
                                    ),
                                    dict(
                                        sequence=30,
                                        action="deny",
                                        prefix="62.168.2.0/24",
                                        ge=25,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="plist3",
                                description="Test plist3",
                                entries=[
                                    dict(
                                        sequence=10,
                                        action="deny",
                                        description="Test rule 10",
                                        prefix="2001:db8:1000::/36",
                                        le=36,
                                    ),
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        description="Test rule 20",
                                        prefix="2001:db8:2000::/36",
                                    ),
                                ],
                            ),
                            dict(
                                name="plist4",
                                entries=[
                                    dict(
                                        sequence=20,
                                        action="permit",
                                        prefix="2001:db8:3000::/36",
                                    ),
                                    dict(
                                        sequence=50,
                                        action="deny",
                                        prefix="2001:db8:4000::/36",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="rendered",
            )
        )
        rendered = [
            "set policy prefix-list plist1",
            "set policy prefix-list plist1 description 'Test plist1'",
            "set policy prefix-list plist1 rule 10",
            "set policy prefix-list plist1 rule 10 action 'permit'",
            "set policy prefix-list plist1 rule 10 description 'Test rule 10'",
            "set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'",
            "set policy prefix-list plist1 rule 20",
            "set policy prefix-list plist1 rule 20 action 'deny'",
            "set policy prefix-list plist1 rule 20 description 'Test rule 20'",
            "set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'",
            "set policy prefix-list plist2",
            "set policy prefix-list plist2 rule 20",
            "set policy prefix-list plist2 rule 20 action 'permit'",
            "set policy prefix-list plist2 rule 20 le '32'",
            "set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'",
            "set policy prefix-list plist2 rule 30",
            "set policy prefix-list plist2 rule 30 action 'deny'",
            "set policy prefix-list plist2 rule 30 ge '25'",
            "set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'",
            "set policy prefix-list6 plist3",
            "set policy prefix-list6 plist3 description 'Test plist3'",
            "set policy prefix-list6 plist3 rule 10",
            "set policy prefix-list6 plist3 rule 10 action 'deny'",
            "set policy prefix-list6 plist3 rule 10 description 'Test rule 10'",
            "set policy prefix-list6 plist3 rule 10 le '36'",
            "set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'",
            "set policy prefix-list6 plist3 rule 20",
            "set policy prefix-list6 plist3 rule 20 action 'permit'",
            "set policy prefix-list6 plist3 rule 20 description 'Test rule 20'",
            "set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'",
            "set policy prefix-list6 plist4",
            "set policy prefix-list6 plist4 rule 20",
            "set policy prefix-list6 plist4 rule 20 action 'permit'",
            "set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'",
            "set policy prefix-list6 plist4 rule 50",
            "set policy prefix-list6 plist4 rule 50 action 'deny'",
            "set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(set(result["rendered"]), set(rendered))

    # test gathered
    def test_vyos_prefix_lists_gathered(self):
        self.get_config.return_value = dedent(
            """\
                set policy prefix-list plist1
                set policy prefix-list plist1 description 'Test plist1'
                set policy prefix-list plist1 rule 10
                set policy prefix-list plist1 rule 10 action 'permit'
                set policy prefix-list plist1 rule 10 description 'Test rule 10'
                set policy prefix-list plist1 rule 10 prefix '92.168.10.0/26'
                set policy prefix-list plist1 rule 20
                set policy prefix-list plist1 rule 20 action 'deny'
                set policy prefix-list plist1 rule 20 description 'Test rule 20'
                set policy prefix-list plist1 rule 20 prefix '72.168.2.0/24'
                set policy prefix-list plist2
                set policy prefix-list plist2 rule 20
                set policy prefix-list plist2 rule 20 action 'permit'
                set policy prefix-list plist2 rule 20 le '32'
                set policy prefix-list plist2 rule 20 prefix '82.168.10.0/26'
                set policy prefix-list plist2 rule 30
                set policy prefix-list plist2 rule 30 action 'deny'
                set policy prefix-list plist2 rule 30 ge '25'
                set policy prefix-list plist2 rule 30 prefix '62.168.2.0/24'
                set policy prefix-list6 plist3
                set policy prefix-list6 plist3 description 'Test plist3'
                set policy prefix-list6 plist3 rule 10
                set policy prefix-list6 plist3 rule 10 action 'deny'
                set policy prefix-list6 plist3 rule 10 description 'Test rule 10'
                set policy prefix-list6 plist3 rule 10 le '36'
                set policy prefix-list6 plist3 rule 10 prefix '2001:db8:1000::/36'
                set policy prefix-list6 plist3 rule 20
                set policy prefix-list6 plist3 rule 20 action 'permit'
                set policy prefix-list6 plist3 rule 20 description 'Test rule 20'
                set policy prefix-list6 plist3 rule 20 prefix '2001:db8:2000::/36'
                set policy prefix-list6 plist4
                set policy prefix-list6 plist4 rule 20
                set policy prefix-list6 plist4 rule 20 action 'permit'
                set policy prefix-list6 plist4 rule 20 prefix '2001:db8:3000::/36'
                set policy prefix-list6 plist4 rule 50
                set policy prefix-list6 plist4 rule 50 action 'deny'
                set policy prefix-list6 plist4 rule 50 prefix '2001:db8:4000::/36'
            """
        )
        set_module_args(dict(state="gathered"))
        gathered = [
            {
                "afi": "ipv4",
                "prefix_lists": [
                    {
                        "description": "Test plist1",
                        "name": "plist1",
                        "entries": [
                            {
                                "action": "permit",
                                "description": "Test rule 10",
                                "sequence": 10,
                                "prefix": "92.168.10.0/26",
                            },
                            {
                                "action": "deny",
                                "description": "Test rule 20",
                                "sequence": 20,
                                "prefix": "72.168.2.0/24",
                            },
                        ],
                    },
                    {
                        "name": "plist2",
                        "entries": [
                            {
                                "action": "permit",
                                "sequence": 20,
                                "le": 32,
                                "prefix": "82.168.10.0/26",
                            },
                            {
                                "action": "deny",
                                "ge": 25,
                                "sequence": 30,
                                "prefix": "62.168.2.0/24",
                            },
                        ],
                    },
                ],
            },
            {
                "afi": "ipv6",
                "prefix_lists": [
                    {
                        "description": "Test plist3",
                        "name": "plist3",
                        "entries": [
                            {
                                "action": "deny",
                                "description": "Test rule 10",
                                "sequence": 10,
                                "le": 36,
                                "prefix": "2001:db8:1000::/36",
                            },
                            {
                                "action": "permit",
                                "description": "Test rule 20",
                                "sequence": 20,
                                "prefix": "2001:db8:2000::/36",
                            },
                        ],
                    },
                    {
                        "name": "plist4",
                        "entries": [
                            {
                                "action": "permit",
                                "sequence": 20,
                                "prefix": "2001:db8:3000::/36",
                            },
                            {
                                "action": "deny",
                                "sequence": 50,
                                "prefix": "2001:db8:4000::/36",
                            },
                        ],
                    },
                ],
            },
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(result["gathered"], gathered)
