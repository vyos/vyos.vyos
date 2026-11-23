# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_nhrp
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


HUB = dict(
    name="tun0",
    authentication="secret",
    holdtime=300,
    multicast=["dynamic"],
    network_id=1,
    redirect=True,
    registration_no_unique=True,
)
SPOKE = dict(
    name="tun1",
    map=[dict(tunnel_ip="10.0.0.2", nbma="192.0.2.2")],
    mtu=1400,
    nhs=[dict(tunnel_ip="dynamic", nbma=["192.0.2.1", "198.51.100.1"])],
    shortcut=True,
)


class TestVyosNhrpModule(TestVyosModule):
    module = vyos_nhrp

    def setUp(self):
        super(TestVyosNhrpModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_get_device_data = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.nhrp.nhrp.NhrpFacts.get_device_data",
        )
        self.get_device_data = self.mock_get_device_data.start()

    def tearDown(self):
        super(TestVyosNhrpModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_device_data.stop()

    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_nhrp_config.cfg"

        def load_from_file(*args, **kwargs):
            return load_fixture(filename)

        self.get_device_data.side_effect = load_from_file

    def test_vyos_nhrp_merged_idempotent(self):
        set_module_args(dict(config=dict(tunnels=[HUB, SPOKE]), state="merged"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_nhrp_merged_list_order_does_not_matter(self):
        spoke = dict(SPOKE, nhs=[dict(tunnel_ip="dynamic", nbma=["198.51.100.1", "192.0.2.1"])])
        set_module_args(dict(config=dict(tunnels=[spoke]), state="merged"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_nhrp_merged(self):
        set_module_args(
            dict(
                config=dict(
                    tunnels=[
                        dict(name="tun0", holdtime=600, multicast=["10.0.0.255"]),
                        dict(
                            name="tun1",
                            nhs=[dict(tunnel_ip="dynamic", nbma=["203.0.113.1"])],
                        ),
                        dict(
                            name="tun2",
                            map=[dict(tunnel_ip="10.1.0.1", nbma="local")],
                            network_id=2,
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = [
            "set protocols nhrp tunnel tun0 holdtime 600",
            "set protocols nhrp tunnel tun0 multicast 10.0.0.255",
            "set protocols nhrp tunnel tun1 nhs tunnel-ip dynamic nbma 203.0.113.1",
            "set protocols nhrp tunnel tun2 network-id 2",
            "set protocols nhrp tunnel tun2 map tunnel-ip 10.1.0.1 nbma local",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nhrp_merged_new_tunnel_without_options(self):
        set_module_args(dict(config=dict(tunnels=[dict(name="tun3")]), state="merged"))
        self.execute_module(changed=True, commands=["set protocols nhrp tunnel tun3"])

    def test_vyos_nhrp_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    tunnels=[
                        dict(name="tun0", authentication="newpass", multicast=["dynamic"]),
                        dict(
                            name="tun1",
                            nhs=[dict(tunnel_ip="dynamic", nbma=["192.0.2.1"])],
                            shortcut=True,
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        commands = [
            "set protocols nhrp tunnel tun0 authentication 'newpass'",
            "delete protocols nhrp tunnel tun0 holdtime",
            "delete protocols nhrp tunnel tun0 network-id",
            "delete protocols nhrp tunnel tun0 redirect",
            "delete protocols nhrp tunnel tun0 registration-no-unique",
            "delete protocols nhrp tunnel tun1 map tunnel-ip 10.0.0.2",
            "delete protocols nhrp tunnel tun1 mtu",
            "delete protocols nhrp tunnel tun1 nhs tunnel-ip dynamic nbma 198.51.100.1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_vyos_nhrp_replaced_idempotent(self):
        set_module_args(dict(config=dict(tunnels=[HUB, SPOKE]), state="replaced"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_nhrp_overridden(self):
        set_module_args(dict(config=dict(tunnels=[HUB]), state="overridden"))
        self.execute_module(changed=True, commands=["delete protocols nhrp tunnel tun1"])

    def test_vyos_nhrp_overridden_idempotent(self):
        set_module_args(dict(config=dict(tunnels=[HUB, SPOKE]), state="overridden"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_nhrp_deleted_tunnel(self):
        set_module_args(dict(config=dict(tunnels=[dict(name="tun1")]), state="deleted"))
        self.execute_module(changed=True, commands=["delete protocols nhrp tunnel tun1"])

    def test_vyos_nhrp_deleted_all(self):
        set_module_args(dict(state="deleted"))
        self.execute_module(changed=True, commands=["delete protocols nhrp"])

    def test_vyos_nhrp_deleted_not_configured(self):
        set_module_args(dict(config=dict(tunnels=[dict(name="tun9")]), state="deleted"))
        self.execute_module(changed=False, commands=[])

    def test_vyos_nhrp_rendered(self):
        set_module_args(dict(config=dict(tunnels=[SPOKE]), state="rendered"))
        commands = [
            "set protocols nhrp tunnel tun1 map tunnel-ip 10.0.0.2 nbma 192.0.2.2",
            "set protocols nhrp tunnel tun1 mtu 1400",
            "set protocols nhrp tunnel tun1 nhs tunnel-ip dynamic nbma 192.0.2.1",
            "set protocols nhrp tunnel tun1 nhs tunnel-ip dynamic nbma 198.51.100.1",
            "set protocols nhrp tunnel tun1 shortcut",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_vyos_nhrp_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        self.assertEqual(result["gathered"], dict(tunnels=[HUB, SPOKE]))

    def test_vyos_nhrp_parsed(self):
        set_module_args(
            dict(running_config=load_fixture("vyos_nhrp_config.cfg"), state="parsed"),
        )
        result = self.execute_module(changed=False)
        self.assertEqual(result["parsed"], dict(tunnels=[HUB, SPOKE]))

    def test_vyos_nhrp_overridden_round_trip_revert(self):
        # the gathered base configuration, fed back with overridden, undoes the changes
        set_module_args(dict(config=dict(tunnels=[HUB, SPOKE]), state="overridden"))
        commands = [
            "set protocols nhrp tunnel tun0 holdtime 300",
            "delete protocols nhrp tunnel tun0 multicast 10.0.0.255",
            "delete protocols nhrp tunnel tun1 nhs tunnel-ip dynamic nbma 203.0.113.1",
        ]
        self.execute_module(
            changed=True,
            commands=commands,
            filename="vyos_nhrp_config_changed.cfg",
        )
