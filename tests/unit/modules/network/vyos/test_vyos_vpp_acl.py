# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_vpp_acl
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


WEB_IN = dict(
    name="WEB-IN",
    description="Inbound web traffic",
    rules=[
        dict(
            number=10,
            action="permit",
            description="Allow HTTPS from partners",
            protocol="tcp",
            source=dict(prefix="192.0.2.0/24", port="1024-65535"),
            destination=dict(prefix="198.51.100.10/32", port="443"),
            tcp_flags=dict(is_set=["syn"], is_not_set=["ack"]),
        ),
        dict(number=20, action="deny"),
    ],
)
ACLS = dict(
    ip=dict(
        acls=[
            dict(name="MGMT", rules=[dict(number=10, action="permit")]),
            WEB_IN,
            dict(name="WEB-OUT", rules=[dict(number=10, action="permit-reflect")]),
        ],
        interfaces=[
            dict(
                name="eth1",
                input=[dict(acl_tag=1, tag_name="WEB-IN"), dict(acl_tag=2, tag_name="MGMT")],
                output=[dict(acl_tag=1, tag_name="WEB-OUT")],
            ),
        ],
    ),
    mac=dict(
        acls=[
            dict(
                name="MAC-FILTER",
                rules=[
                    dict(
                        number=10,
                        action="permit",
                        prefix="192.0.2.0/24",
                        mac_address="00:11:22:33:44:55",
                        mac_mask="ff:ff:ff:00:00:00",
                    ),
                ],
            ),
        ],
        interfaces=[dict(name="eth1", tag_name="MAC-FILTER")],
    ),
)


class TestVyosVppAclModule(TestVyosModule):
    module = vyos_vpp_acl

    def setUp(self):
        super(TestVyosVppAclModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_get_device_data = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.vpp_acl.vpp_acl.Vpp_aclFacts.get_device_data",
        )
        self.get_device_data = self.mock_get_device_data.start()

    def tearDown(self):
        super(TestVyosVppAclModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_device_data.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_vpp_acl_config.cfg"

        def load_from_file(*args, **kwargs):
            return load_fixture(filename)

        self.get_device_data.side_effect = load_from_file

    def test_vyos_vpp_acl_merged_idempotent(self):
        set_module_args(dict(config=ACLS, state="merged"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_vpp_acl_merged_tcp_flag_order_does_not_matter(self):
        rule = dict(number=10, tcp_flags=dict(is_set=["syn"], is_not_set=["ack"]))
        set_module_args(
            dict(config=dict(ip=dict(acls=[dict(name="WEB-IN", rules=[rule])])), state="merged"),
        )
        self.execute_module(changed=False, commands=[])

    def test_vyos_vpp_acl_merged(self):
        set_module_args(
            dict(
                config=dict(
                    ip=dict(
                        acls=[
                            dict(
                                name="WEB-IN",
                                rules=[
                                    dict(number=10, tcp_flags=dict(is_set=["syn", "fin"])),
                                    dict(number=30, action="deny", protocol="udp"),
                                ],
                            ),
                            dict(name="NEW", description="New ACL with spaces"),
                        ],
                        interfaces=[
                            dict(name="eth1", input=[dict(acl_tag=3, tag_name="NEW")]),
                            dict(name="eth2", output=[dict(acl_tag=1, tag_name="NEW")]),
                        ],
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "set vpp acl ip tag-name NEW description 'New ACL with spaces'",
            "set vpp acl ip tag-name WEB-IN rule 10 tcp-flags is-set fin",
            "set vpp acl ip tag-name WEB-IN rule 30 action deny",
            "set vpp acl ip tag-name WEB-IN rule 30 protocol udp",
            "set vpp acl ip interface eth1 input acl-tag 3 tag-name NEW",
            "set vpp acl ip interface eth2 output acl-tag 1 tag-name NEW",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vpp_acl_replaced_acl(self):
        set_module_args(
            dict(
                config=dict(
                    ip=dict(
                        acls=[
                            dict(
                                name="WEB-IN",
                                rules=[
                                    dict(
                                        number=10,
                                        action="permit",
                                        protocol="tcp",
                                        tcp_flags=dict(is_set=["syn"]),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "delete vpp acl ip tag-name WEB-IN description",
            "delete vpp acl ip tag-name WEB-IN rule 10 description",
            "delete vpp acl ip tag-name WEB-IN rule 10 source prefix",
            "delete vpp acl ip tag-name WEB-IN rule 10 source port",
            "delete vpp acl ip tag-name WEB-IN rule 10 destination prefix",
            "delete vpp acl ip tag-name WEB-IN rule 10 destination port",
            "delete vpp acl ip tag-name WEB-IN rule 10 tcp-flags is-not-set ack",
            "delete vpp acl ip tag-name WEB-IN rule 20",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vpp_acl_replaced_bindings(self):
        set_module_args(
            dict(
                config=dict(
                    ip=dict(
                        interfaces=[dict(name="eth1", input=[dict(acl_tag=1, tag_name="MGMT")])],
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "set vpp acl ip interface eth1 input acl-tag 1 tag-name MGMT",
            "delete vpp acl ip interface eth1 input acl-tag 2",
            "delete vpp acl ip interface eth1 output acl-tag 1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vpp_acl_replaced_mac(self):
        set_module_args(
            dict(
                config=dict(
                    mac=dict(
                        acls=[
                            dict(
                                name="MAC-FILTER",
                                rules=[
                                    dict(number=10, action="deny", mac_address="00:11:22:33:44:55"),
                                ],
                            ),
                        ],
                        interfaces=[dict(name="eth1", tag_name="MAC-FILTER")],
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "set vpp acl mac tag-name MAC-FILTER rule 10 action deny",
            "delete vpp acl mac tag-name MAC-FILTER rule 10 prefix",
            "delete vpp acl mac tag-name MAC-FILTER rule 10 mac-mask",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vpp_acl_replaced_idempotent(self):
        set_module_args(dict(config=ACLS, state="replaced"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_vpp_acl_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    ip=dict(
                        acls=[dict(name="MGMT", rules=[dict(number=10, action="permit")])],
                        interfaces=[dict(name="eth1", input=[dict(acl_tag=1, tag_name="MGMT")])],
                    ),
                ),
                state="overridden",
            ),
        )
        commands = [
            "delete vpp acl ip tag-name WEB-IN",
            "delete vpp acl ip tag-name WEB-OUT",
            "set vpp acl ip interface eth1 input acl-tag 1 tag-name MGMT",
            "delete vpp acl ip interface eth1 input acl-tag 2",
            "delete vpp acl ip interface eth1 output acl-tag 1",
            "delete vpp acl mac interface eth1",
            "delete vpp acl mac tag-name MAC-FILTER",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vpp_acl_overridden_idempotent(self):
        set_module_args(dict(config=ACLS, state="overridden"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_vpp_acl_deleted_all(self):
        set_module_args(dict(state="deleted"))
        self.execute_module(changed=True, commands=["delete vpp acl"])

    def test_vyos_vpp_acl_deleted_parts(self):
        set_module_args(
            dict(
                config=dict(
                    ip=dict(acls=[dict(name="WEB-OUT")], interfaces=[dict(name="eth1")]),
                    mac=dict(interfaces=[dict(name="eth1")]),
                ),
                state="deleted",
            ),
        )
        commands = [
            "delete vpp acl ip interface eth1",
            "delete vpp acl ip tag-name WEB-OUT",
            "delete vpp acl mac interface eth1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_vpp_acl_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    mac=dict(
                        acls=[
                            dict(
                                name="MAC-FILTER",
                                description="Vendor filter",
                                rules=[
                                    dict(number=10, action="deny", mac_address="00:11:22:33:44:55"),
                                ],
                            ),
                        ],
                        interfaces=[dict(name="eth2", tag_name="MAC-FILTER")],
                    ),
                ),
                state="rendered",
            ),
        )
        commands = [
            "set vpp acl mac tag-name MAC-FILTER description 'Vendor filter'",
            "set vpp acl mac tag-name MAC-FILTER rule 10 action deny",
            "set vpp acl mac tag-name MAC-FILTER rule 10 mac-address 00:11:22:33:44:55",
            "set vpp acl mac interface eth2 tag-name MAC-FILTER",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_vyos_vpp_acl_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        self.assertEqual(result["gathered"], ACLS)

    def test_vyos_vpp_acl_parsed(self):
        set_module_args(
            dict(running_config=load_fixture("vyos_vpp_acl_config.cfg"), state="parsed"),
        )
        result = self.execute_module(changed=False)
        self.assertEqual(result["parsed"], ACLS)
