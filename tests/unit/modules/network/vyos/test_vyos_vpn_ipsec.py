#
# (c) 2026, Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_vpn_ipsec
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule, load_fixture


class TestVyosVpnIpsecModule(TestVyosModule):
    module = vyos_vpn_ipsec

    def setUp(self):
        super(TestVyosVpnIpsecModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.vpn_ipsec.vpn_ipsec.Vpn_ipsecFacts.get_vpn_ipsec_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosVpnIpsecModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    # Single fixture file, reused across every test. Carries: two
    # ike_group entries (IKE-TEST richly configured incl.
    # dead_peer_detection/disable_mobike, IKE-EXTRA minimal, to prove
    # "unlisted items preserved"); esp_group with compression+proposal;
    # psk/ppk with multi-value id lists; a profile; and every top-level
    # singleton field (disable_uniqreqids, interface, log, options).
    def load_fixtures(self, commands=None, filename=None):
        if filename == "EMPTY":
            self.execute_show_command.side_effect = None
            self.execute_show_command.return_value = ""
            return

        if filename is None:
            filename = "vyos_vpn_ipsec_config.cfg"

        def load_from_file(*args, **kwargs):
            return load_fixture(filename)

        self.execute_show_command.side_effect = load_from_file

    # -------------------------------------------------------------------
    # merged
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_merged_idempotent(self):
        playbook = dict(
            config=dict(
                esp_group=[
                    dict(
                        name="ESP-TEST",
                        compression=True,
                        proposal=[dict(proposal_id=1, encryption="aes256", hash="sha256")],
                    ),
                ],
                ike_group=[
                    dict(
                        name="IKE-TEST",
                        key_exchange="ikev2",
                        disable_mobike=True,
                        dead_peer_detection=dict(action="restart", interval=15, timeout=60),
                        proposal=[
                            dict(proposal_id=1, encryption="aes256", hash="sha256", dh_group=14),
                        ],
                    ),
                ],
            ),
            state="merged",
        )
        set_module_args(playbook)
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), [])

    def test_vyos_vpn_ipsec_merged_new_group_leaves_existing_untouched(self):
        playbook = dict(
            config=dict(
                esp_group=[
                    dict(
                        name="ESP-NEW",
                        proposal=[dict(proposal_id=1, encryption="aes256", hash="sha256")],
                    ),
                ],
            ),
            state="merged",
        )
        compare_cmds = [
            "set vpn ipsec esp-group ESP-NEW",
            "set vpn ipsec esp-group ESP-NEW proposal 1",
            "set vpn ipsec esp-group ESP-NEW proposal 1 encryption aes256",
            "set vpn ipsec esp-group ESP-NEW proposal 1 hash sha256",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_merged_bool_field_toggle(self):
        # disable_mobike explicitly set to True in want when have already
        # has it True -> no-op; here we flip a different bool
        # (compression on ESP-TEST is already True in have) by instead
        # adding a brand new bool-bearing field: options.virtual_ip,
        # entirely absent from have.
        playbook = dict(config=dict(options=dict(virtual_ip=True)), state="merged")
        compare_cmds = ["set vpn ipsec options virtual-ip"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_merged_add_psk_id(self):
        # multi-value list field: add one id, existing ids must survive
        playbook = dict(
            config=dict(
                authentication=dict(
                    psk=[dict(name="PSK-TEST", id=["third@example.com"])],
                ),
            ),
            state="merged",
        )
        compare_cmds = ["set vpn ipsec authentication psk PSK-TEST id third@example.com"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_merged_create_ppk(self):
        playbook = dict(
            config=dict(
                authentication=dict(
                    ppk=[dict(name="PPK-NEW", id=["new-ppk-id"], secret="new-secret")],
                ),
            ),
            state="merged",
        )
        compare_cmds = [
            "set vpn ipsec authentication ppk PPK-NEW",
            "set vpn ipsec authentication ppk PPK-NEW id new-ppk-id",
            "set vpn ipsec authentication ppk PPK-NEW secret 'new-secret'",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_merged_profile_add_bind_tunnel(self):
        # multi-value list field on an EXISTING profile: add one tunnel,
        # existing tun0 must survive
        playbook = dict(
            config=dict(
                profile=[dict(name="testprofile", bind_tunnel=["tun1"])],
            ),
            state="merged",
        )
        compare_cmds = ["set vpn ipsec profile testprofile bind tunnel tun1"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_merged_create_profile_from_scratch(self):
        # Regression test: creating a brand new profile must correctly
        # emit its authentication.mode/pre_shared_secret commands. This
        # specific path was silently broken (a leftover dotted-Jinja
        # setval caused render() to return nothing, so addcmd() quietly
        # dropped both commands with no error) -- caught only by a real
        # device integration test, since no existing unit test actually
        # created a profile from scratch or touched its authentication
        # sub-dict through generate_commands().
        playbook = dict(
            config=dict(
                profile=[
                    dict(
                        name="NEWPROFILE",
                        authentication=dict(
                            mode="pre-shared-secret",
                            pre_shared_secret="brand-new-secret",
                        ),
                        esp_group="ESP-TEST",
                        ike_group="IKE-TEST",
                    ),
                ],
            ),
            state="merged",
        )
        compare_cmds = [
            "set vpn ipsec profile NEWPROFILE",
            "set vpn ipsec profile NEWPROFILE authentication mode pre-shared-secret",
            "set vpn ipsec profile NEWPROFILE authentication pre-shared-secret 'brand-new-secret'",
            "set vpn ipsec profile NEWPROFILE esp-group ESP-TEST",
            "set vpn ipsec profile NEWPROFILE ike-group IKE-TEST",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # replaced
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_replaced_only_named_item_touched(self):
        playbook = dict(
            config=dict(
                esp_group=[
                    dict(
                        name="ESP-TEST",
                        proposal=[dict(proposal_id=1, encryption="aes128", hash="sha256")],
                    ),
                ],
            ),
            state="replaced",
        )
        compare_cmds = [
            # compression omitted from want -> reconciled away (attribute
            # inside the selected instance is always reset under replaced)
            "delete vpn ipsec esp-group ESP-TEST compression",
            "set vpn ipsec esp-group ESP-TEST proposal 1 encryption aes128",
            # ike_group/profile/psk/ppk not named at all -> left alone.
            # Top-level singleton fields (no instance scope) are always
            # reconciled under replaced/overridden regardless of what's
            # named elsewhere.
            "delete vpn ipsec disable-uniqreqids",
            "delete vpn ipsec interface eth0",
            "delete vpn ipsec interface eth1",
            "delete vpn ipsec log level 1",
            "delete vpn ipsec log subsystem chd",
            "delete vpn ipsec log subsystem ike",
            "delete vpn ipsec options flexvpn",
            "delete vpn ipsec options retransmission attempts 3",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_replaced_idempotent(self):
        # want fully mirrors the ENTIRE fixture state for every top-level
        # singleton field plus the one named esp_group -- proves
        # replaced's per-item/per-field reconciliation doesn't spuriously
        # touch a fully-matching configuration.
        playbook = dict(
            config=dict(
                esp_group=[
                    dict(
                        name="ESP-TEST",
                        compression=True,
                        proposal=[dict(proposal_id=1, encryption="aes256", hash="sha256")],
                    ),
                ],
                disable_uniqreqids=True,
                interface=["eth0", "eth1"],
                log=dict(level=1, subsystem=["chd", "ike"]),
                options=dict(flexvpn=True, retransmission=dict(attempts=3)),
            ),
            state="replaced",
        )
        set_module_args(playbook)
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), [])

    def test_vyos_vpn_ipsec_replaced_scoped_dead_peer_detection(self):
        # naming ike_group under replaced without dead_peer_detection ->
        # every DPD field reconciled away (nested-dict attribute reset)
        playbook = dict(
            config=dict(
                ike_group=[dict(name="IKE-TEST", key_exchange="ikev2")],
            ),
            state="replaced",
        )
        compare_cmds = [
            "delete vpn ipsec ike-group IKE-TEST dead-peer-detection action restart",
            "delete vpn ipsec ike-group IKE-TEST dead-peer-detection interval 15",
            "delete vpn ipsec ike-group IKE-TEST dead-peer-detection timeout 60",
            "delete vpn ipsec ike-group IKE-TEST disable-mobike",
            "delete vpn ipsec ike-group IKE-TEST proposal 1",
            "delete vpn ipsec disable-uniqreqids",
            "delete vpn ipsec interface eth0",
            "delete vpn ipsec interface eth1",
            "delete vpn ipsec log level 1",
            "delete vpn ipsec log subsystem chd",
            "delete vpn ipsec log subsystem ike",
            "delete vpn ipsec options flexvpn",
            "delete vpn ipsec options retransmission attempts 3",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # overridden
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_overridden_removes_unlisted_instances(self):
        playbook = dict(
            config=dict(
                esp_group=[
                    dict(
                        name="ESP-TEST",
                        proposal=[dict(proposal_id=1, encryption="aes128", hash="sha256")],
                    ),
                ],
            ),
            state="overridden",
        )
        compare_cmds = [
            "delete vpn ipsec esp-group ESP-TEST compression",
            "set vpn ipsec esp-group ESP-TEST proposal 1 encryption aes128",
            "delete vpn ipsec ike-group IKE-TEST",
            "delete vpn ipsec ike-group IKE-EXTRA",
            "delete vpn ipsec profile testprofile",
            "delete vpn ipsec authentication psk PSK-TEST",
            "delete vpn ipsec authentication ppk PPK-TEST",
            "delete vpn ipsec disable-uniqreqids",
            "delete vpn ipsec interface eth0",
            "delete vpn ipsec interface eth1",
            "delete vpn ipsec log level 1",
            "delete vpn ipsec log subsystem chd",
            "delete vpn ipsec log subsystem ike",
            "delete vpn ipsec options flexvpn",
            "delete vpn ipsec options retransmission attempts 3",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # deleted -- bare (delete everything)
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_deleted_bare(self):
        playbook = dict(state="deleted")
        compare_cmds = [
            "delete vpn ipsec esp-group ESP-TEST",
            "delete vpn ipsec ike-group IKE-TEST",
            "delete vpn ipsec ike-group IKE-EXTRA",
            "delete vpn ipsec profile testprofile",
            "delete vpn ipsec authentication psk PSK-TEST",
            "delete vpn ipsec authentication ppk PPK-TEST",
            "delete vpn ipsec disable-uniqreqids",
            "delete vpn ipsec interface eth0",
            "delete vpn ipsec interface eth1",
            "delete vpn ipsec log level 1",
            "delete vpn ipsec log subsystem chd",
            "delete vpn ipsec log subsystem ike",
            "delete vpn ipsec options flexvpn",
            "delete vpn ipsec options retransmission attempts 3",
        ]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_deleted_bare_idempotent(self):
        playbook = dict(state="deleted")
        set_module_args(playbook)
        result = self.execute_module(changed=False, filename="EMPTY")
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), [])

    # -------------------------------------------------------------------
    # deleted -- scoped (delete only what's named)
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_deleted_scoped_named_item_only(self):
        playbook = dict(config=dict(ike_group=[dict(name="IKE-EXTRA")]), state="deleted")
        compare_cmds = ["delete vpn ipsec ike-group IKE-EXTRA"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_deleted_scoped_nonexistent_name_idempotent(self):
        playbook = dict(config=dict(ike_group=[dict(name="IKE-NONEXISTENT")]), state="deleted")
        set_module_args(playbook)
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), [])

    def test_vyos_vpn_ipsec_deleted_scoped_interface_element(self):
        # element-level list deletion: name only eth0, eth1 must survive
        playbook = dict(config=dict(interface=["eth0"]), state="deleted")
        compare_cmds = ["delete vpn ipsec interface eth0"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_deleted_scoped_log_subsystem_element(self):
        playbook = dict(config=dict(log=dict(subsystem=["chd"])), state="deleted")
        compare_cmds = ["delete vpn ipsec log subsystem chd"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_vpn_ipsec_deleted_scoped_options_field(self):
        playbook = dict(config=dict(options=dict(flexvpn=True)), state="deleted")
        compare_cmds = ["delete vpn ipsec options flexvpn"]
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # rendered (no device contact -- have is empty regardless of fixture)
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_rendered(self):
        playbook = dict(
            config=dict(
                esp_group=[
                    dict(
                        name="ESP-RENDER-TEST",
                        proposal=[dict(proposal_id=1, encryption="aes256", hash="sha256")],
                    ),
                ],
            ),
            state="rendered",
        )
        compare_cmds = [
            "set vpn ipsec esp-group ESP-RENDER-TEST",
            "set vpn ipsec esp-group ESP-RENDER-TEST proposal 1",
            "set vpn ipsec esp-group ESP-RENDER-TEST proposal 1 encryption aes256",
            "set vpn ipsec esp-group ESP-RENDER-TEST proposal 1 hash sha256",
        ]
        set_module_args(playbook)
        result = self.execute_module()
        self.maxDiff = None
        self.assertEqual(sorted(result["rendered"]), sorted(compare_cmds))

    # -------------------------------------------------------------------
    # parsed (reads running_config directly, not the mocked show command)
    # -------------------------------------------------------------------

    def test_vyos_vpn_ipsec_parsed(self):
        set_module_args(
            dict(
                running_config=dedent(
                    """\
                    set vpn ipsec esp-group ESP-PARSE-TEST proposal 1 encryption aes256
                    set vpn ipsec esp-group ESP-PARSE-TEST proposal 1 hash sha256
                    set vpn ipsec ike-group IKE-PARSE-TEST key-exchange ikev2
                    """,
                ),
                state="parsed",
            ),
        )
        parsed = dict(
            esp_group=[
                dict(
                    name="ESP-PARSE-TEST",
                    proposal=[dict(proposal_id=1, encryption="aes256", hash="sha256")],
                ),
            ],
            ike_group=[dict(name="IKE-PARSE-TEST", key_exchange="ikev2")],
        )
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(result["parsed"], parsed)

    # -------------------------------------------------------------------
    # gathered
    # -------------------------------------------------------------------

    def _normalize_scalar_lists(self, node):
        """Multi-value scalar-list fields (id, subsystem, interface, ...)
        have no meaningful order -- dict_merge's internal list handling
        doesn't guarantee a stable sequence between runs. Sort them
        in-place (recursively) before comparing so tests aren't
        sensitive to that non-determinism, while list-of-dict
        collections (already sorted by name in process_facts) are left
        untouched.
        """
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, list) and v and all(not isinstance(i, dict) for i in v):
                    node[k] = sorted(v)
                else:
                    self._normalize_scalar_lists(v)
        elif isinstance(node, list):
            for item in node:
                self._normalize_scalar_lists(item)
        return node

    def test_vyos_vpn_ipsec_gathered(self):
        set_module_args(dict(state="gathered"))
        gathered = dict(
            authentication=dict(
                ppk=[dict(name="PPK-TEST", id=["ppk-id-1"], secret="test-ppk-secret")],
                psk=[
                    dict(
                        name="PSK-TEST",
                        id=["local@example.com", "remote@example.com"],
                        secret="test-not-real-secret",
                    ),
                ],
            ),
            disable_uniqreqids=True,
            esp_group=[
                dict(
                    name="ESP-TEST",
                    compression=True,
                    proposal=[dict(proposal_id=1, encryption="aes256", hash="sha256")],
                ),
            ],
            ike_group=[
                dict(name="IKE-EXTRA", key_exchange="ikev1"),
                dict(
                    name="IKE-TEST",
                    key_exchange="ikev2",
                    disable_mobike=True,
                    dead_peer_detection=dict(action="restart", interval=15, timeout=60),
                    proposal=[
                        dict(proposal_id=1, encryption="aes256", hash="sha256", dh_group=14),
                    ],
                ),
            ],
            interface=["eth0", "eth1"],
            log=dict(level=1, subsystem=["chd", "ike"]),
            options=dict(flexvpn=True, retransmission=dict(attempts=3)),
            profile=[
                dict(
                    name="testprofile",
                    authentication=dict(
                        mode="pre-shared-secret",
                        pre_shared_secret="test-not-real-secret",
                    ),
                    bind_tunnel=["tun0"],
                    esp_group="ESP-TEST",
                    ike_group="IKE-TEST",
                ),
            ],
        )
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(
            self._normalize_scalar_lists(result["gathered"]),
            self._normalize_scalar_lists(gathered),
        )
