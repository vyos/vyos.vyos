#
# (c) 2026, Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_vpn_ipsec_s2s
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosVpnIpsecS2sModule(TestVyosModule):
    module = vyos_vpn_ipsec_s2s

    def setUp(self):
        super(TestVyosVpnIpsecS2sModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.vpn_ipsec_s2s.vpn_ipsec_s2s.Vpn_ipsec_s2sFacts.get_vpn_ipsec_s2s_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosVpnIpsecS2sModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    # Single fixture file, reused across every test. Carries PEER-TEST
    # (richly configured -- authentication, tunnel, vti, every scalar
    # type) and PEER-EXTRA (minimal, to prove "unlisted peer preserved
    # under replaced / removed under overridden").
    def load_fixtures(self, commands=None, filename=None):
        if filename is None:
            filename = "vyos_vpn_ipsec_s2s_config.cfg"

        def load_from_file(*args, **kwargs):
            return load_fixture(filename)

        self.execute_show_command.side_effect = load_from_file

    # -------------------------------------------------------------------
    # merged
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_s2s_merged_idempotent(self):
        playbook = dict(
            config=dict(
                peer=[
                    dict(
                        name="PEER-TEST",
                        authentication=dict(
                            local_id="local@example.com",
                            mode="pre-shared-secret",
                            remote_id="remote@example.com",
                        ),
                        childless="prefer",
                        connection_type="initiate",
                        default_esp_group="ESP-TEST",
                        description="test peer for site-to-site module",
                        force_udp_encapsulation=True,
                        ike_group="IKE-TEST",
                        ikev2_reauth="inherit",
                        local_address="any",
                        remote_address=["203.0.113.1"],
                        replay_window=32,
                        virtual_address=["0.0.0.0"],
                        tunnel=[
                            dict(
                                tunnel_id=1,
                                esp_group="ESP-TEST",
                                protocol="tcp",
                                priority=10,
                                local=dict(port=443, prefix=["10.0.0.0/24"]),
                                remote=dict(port=443, prefix=["10.1.0.0/24"]),
                            ),
                        ],
                        vti=dict(
                            bind="vti0",
                            esp_group="ESP-TEST",
                            traffic_selector=dict(
                                local=dict(prefix=["10.2.0.0/24"]),
                                remote=dict(prefix=["10.3.0.0/24"]),
                            ),
                        ),
                    ),
                ],
            ),
            state="merged",
        )
        set_module_args(playbook)
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), [])

    def test_vyos_vpn_ipsec_s2s_merged_new_peer_leaves_existing_untouched(self):
        playbook = dict(
            config=dict(peer=[dict(name="PEER-NEW", ike_group="IKE-TEST")]),
            state="merged",
        )
        compare_cmds = [
            "set vpn ipsec site-to-site peer PEER-NEW",
            "set vpn ipsec site-to-site peer PEER-NEW ike-group 'IKE-TEST'",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # replaced
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_s2s_replaced_only_named_peer_touched(self):
        # Name PEER-TEST fully (mirroring the fixture exactly) except a
        # changed tunnel priority -- PEER-EXTRA must be left alone.
        playbook = dict(
            config=dict(
                peer=[
                    dict(
                        name="PEER-TEST",
                        authentication=dict(
                            local_id="local@example.com",
                            mode="pre-shared-secret",
                            remote_id="remote@example.com",
                        ),
                        childless="prefer",
                        connection_type="initiate",
                        default_esp_group="ESP-TEST",
                        description="test peer for site-to-site module",
                        force_udp_encapsulation=True,
                        ike_group="IKE-TEST",
                        ikev2_reauth="inherit",
                        local_address="any",
                        remote_address=["203.0.113.1"],
                        replay_window=32,
                        virtual_address=["0.0.0.0"],
                        tunnel=[
                            dict(
                                tunnel_id=1,
                                esp_group="ESP-TEST",
                                protocol="tcp",
                                priority=99,
                                local=dict(port=443, prefix=["10.0.0.0/24"]),
                                remote=dict(port=443, prefix=["10.1.0.0/24"]),
                            ),
                        ],
                        vti=dict(
                            bind="vti0",
                            esp_group="ESP-TEST",
                            traffic_selector=dict(
                                local=dict(prefix=["10.2.0.0/24"]),
                                remote=dict(prefix=["10.3.0.0/24"]),
                            ),
                        ),
                    ),
                ],
            ),
            state="replaced",
        )
        compare_cmds = ["set vpn ipsec site-to-site peer PEER-TEST tunnel 1 priority '99'"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # overridden
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_s2s_overridden_removes_unlisted_peer(self):
        playbook = dict(
            config=dict(peer=[dict(name="PEER-TEST", ike_group="IKE-TEST")]),
            state="overridden",
        )
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertIn("delete vpn ipsec site-to-site peer PEER-EXTRA", result["commands"])
        # PEER-TEST had far more fields than just ike_group in the
        # fixture -- overridden must reconcile all of those away too,
        # since only ike_group was named.
        self.assertIn(
            "delete vpn ipsec site-to-site peer PEER-TEST default-esp-group 'ESP-TEST'",
            result["commands"],
        )

    # -------------------------------------------------------------------
    # deleted -- bare and scoped
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_s2s_deleted_bare(self):
        set_module_args(dict(state="deleted"))
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertIn("delete vpn ipsec site-to-site peer PEER-TEST", result["commands"])
        self.assertIn("delete vpn ipsec site-to-site peer PEER-EXTRA", result["commands"])

    def test_vyos_vpn_ipsec_s2s_deleted_scoped_named_peer_only(self):
        set_module_args(dict(config=dict(peer=[dict(name="PEER-EXTRA")]), state="deleted"))
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(result["commands"], ["delete vpn ipsec site-to-site peer PEER-EXTRA"])

    # -------------------------------------------------------------------
    # rendered / parsed / gathered
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_s2s_rendered(self):
        playbook = dict(
            config=dict(peer=[dict(name="PEER-RENDER-TEST", ike_group="IKE-TEST")]),
            state="rendered",
        )
        compare_cmds = [
            "set vpn ipsec site-to-site peer PEER-RENDER-TEST",
            "set vpn ipsec site-to-site peer PEER-RENDER-TEST ike-group 'IKE-TEST'",
        ]
        set_module_args(playbook)
        result = self.execute_module()
        self.maxDiff = None
        self.assertEqual(sorted(result["rendered"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_s2s_gathered(self):
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        self.maxDiff = None
        names = sorted(p["name"] for p in result["gathered"]["peer"])
        self.assertEqual(names, ["PEER-EXTRA", "PEER-TEST"])
