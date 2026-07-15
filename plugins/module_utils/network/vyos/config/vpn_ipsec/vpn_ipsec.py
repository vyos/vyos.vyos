#
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_vpn_ipsec config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.

Follows the established per-module convention used by vyos_ha/vyos_nat
(list-to-dict conversion + explicit per-state branching in
generate_commands), rather than a shared generic engine.

State semantics (standard Ansible RM convention, confirmed against a
real device run that caught a bug in an earlier version of this file):
  - merged:     only items/fields named in `want` are touched. Nothing
                absent from `want` is ever deleted.
  - replaced:   only items NAMED in `want` are touched (same item scope
                as merged) -- but for each named item, its full state is
                reconciled to exactly match `want` (fields present in
                `have` but omitted from `want` ARE deleted). Items not
                named in `want` at all are left completely alone.
  - overridden: every item is in scope, including ones absent from
                `want` entirely -- those get deleted wholesale. Named
                items are reconciled the same way as `replaced`.

This is implemented via two independent flags:
  - select_all: whether item iteration considers have-only items too
                (True only for overridden; False for merged/replaced).
  - reconcile:  whether omitted fields within an already-selected item
                get deleted (True for replaced/overridden; False for
                merged/rendered).
"""

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import (
    Facts,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vpn_ipsec import (
    Vpn_ipsecTemplate,
)


class Vpn_ipsec(ResourceModule):
    """
    The vyos_vpn_ipsec config class
    """

    def __init__(self, module):
        super(Vpn_ipsec, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vpn_ipsec",
            tmplt=Vpn_ipsecTemplate(),
        )
        self.parsers = [
            "esp_group",
            "esp_group.proposal",
            "esp_group.proposal.encryption",
            "esp_group.proposal.hash",
            "esp_group.compression",
            "esp_group.disable_rekey",
            "esp_group.life_bytes",
            "esp_group.life_packets",
            "esp_group.lifetime",
            "esp_group.mode",
            "esp_group.pfs",
            "ike_group",
            "ike_group.key_exchange",
            "ike_group.proposal",
            "ike_group.proposal.dh_group",
            "ike_group.proposal.encryption",
            "ike_group.proposal.hash",
            "ike_group.close_action",
            "ike_group.dead_peer_detection.action",
            "ike_group.dead_peer_detection.interval",
            "ike_group.dead_peer_detection.timeout",
            "ike_group.disable_mobike",
            "ike_group.ikev2_reauth",
            "ike_group.lifetime",
            "ike_group.mode",
            "profile",
            "profile.authentication.mode",
            "profile.authentication.pre_shared_secret",
            "profile.esp_group",
            "profile.ike_group",
            "profile.disable",
            "authentication.psk.secret_type",
            "authentication.psk.dhcp_interface",
            "authentication.ppk",
            "authentication.ppk.id",
            "authentication.ppk.secret",
            "authentication.ppk.secret_type",
            "interface",
            "log.level",
            "log.subsystem",
            "options.disable_route_autoinstall",
            "options.flexvpn",
            "options.interface",
            "options.retransmission.attempts",
            "options.retransmission.base",
            "options.retransmission.timeout",
            "options.virtual_ip",
            "disable_uniqreqids",
        ]

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """Generate configuration commands to send based on
        want, have and desired state.
        """
        wantd = deepcopy(self.want) or {}
        haved = deepcopy(self.have) or {}

        for entry in (wantd, haved):
            self._list_to_dict(entry)

        scoped_delete = None
        if self.state == "deleted":
            if wantd:
                # user named specific items -- surgical removal of just
                # those, everything else preserved (vyos_vrf precedent:
                # deleted + instances:[{name: vrf-blue}] removes only
                # vrf-blue). Capture what was named before wiping wantd.
                scoped_delete = wantd
            wantd = {}

        if self.state == "merged":
            # NOTE: list_to_dict() above must run BEFORE this. dict_merge
            # concatenates lists rather than merging matching entries by
            # key, so merging while ike_group/esp_group/etc are still
            # lists would duplicate entries instead of filling in omitted
            # fields from `have`. Once they're name-keyed dicts, dict_merge
            # recurses per-key correctly, which is what lets a partial
            # update (e.g. specifying only key_exchange) leave other
            # existing fields on that same group untouched.
            wantd = dict_merge(haved, wantd)

        select_all = self.state in ("overridden", "deleted")
        reconcile = self.state in ("replaced", "overridden", "deleted")

        self._compare_esp_groups(wantd, haved, select_all, reconcile, scoped_delete)
        self._compare_ike_groups(wantd, haved, select_all, reconcile, scoped_delete)
        self._compare_profiles(wantd, haved, select_all, reconcile, scoped_delete)
        self._compare_psks(wantd, haved, select_all, reconcile, scoped_delete)
        self._compare_ppks(wantd, haved, select_all, reconcile, scoped_delete)
        self._compare_top_level(wantd, haved, select_all, reconcile, scoped_delete)

        self.commands = list(dict.fromkeys(self.commands))

    # -------------------------------------------------------------------
    # List -> name-keyed dict conversion (matches vyos_ha/vyos_nat style)
    # -------------------------------------------------------------------

    def _list_to_dict(self, config):
        for key in ("ike_group", "esp_group", "profile"):
            items = config.get(key)
            if isinstance(items, list):
                config[key] = {item["name"]: item for item in items}
                for item in config[key].values():
                    if isinstance(item.get("proposal"), list):
                        item["proposal"] = {p["proposal_id"]: p for p in item["proposal"]}

        auth = config.get("authentication", {})
        for key in ("psk", "ppk"):
            items = auth.get(key)
            if isinstance(items, list):
                auth[key] = {item["name"]: item for item in items}

    # -------------------------------------------------------------------
    # ESP groups
    # -------------------------------------------------------------------

    def _compare_esp_groups(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        have_groups = haved.get("esp_group", {})

        if scoped_delete is not None:
            for name in set(scoped_delete.get("esp_group", {})):
                if name in have_groups:
                    self.commands.append("delete vpn ipsec esp-group {0}".format(name))
            return

        want_groups = wantd.get("esp_group", {})
        names = set(want_groups) | set(have_groups) if select_all else set(want_groups)

        for name in names:
            w = want_groups.get(name, {})
            h = have_groups.get(name, {})
            if w == h:
                continue

            if name in have_groups and name not in want_groups:
                # only reached when select_all (overridden): item entirely
                # absent from want -> delete wholesale
                self.commands.append("delete vpn ipsec esp-group {0}".format(name))
                continue

            if name not in have_groups:
                self.addcmd({"name": name}, "esp_group", False)

            for field in ("mode", "pfs", "lifetime", "life_bytes", "life_packets"):
                self._cmp_scalar(
                    w,
                    h,
                    field,
                    {"name": name},
                    "esp_group.{0}".format(field),
                    reconcile,
                )
            for field in ("compression", "disable_rekey"):
                self._cmp_bool(
                    w,
                    h,
                    field,
                    {"name": name},
                    "esp_group.{0}".format(field),
                    reconcile,
                )

            self._compare_proposals(
                w.get("proposal", {}),
                h.get("proposal", {}),
                {"name": name},
                "esp_group.proposal",
                "esp_group.proposal.encryption",
                "esp_group.proposal.hash",
                None,
                reconcile,
            )

    # -------------------------------------------------------------------
    # IKE groups
    # -------------------------------------------------------------------

    def _compare_ike_groups(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        have_groups = haved.get("ike_group", {})

        if scoped_delete is not None:
            for name in set(scoped_delete.get("ike_group", {})):
                if name in have_groups:
                    self.commands.append("delete vpn ipsec ike-group {0}".format(name))
            return

        want_groups = wantd.get("ike_group", {})
        names = set(want_groups) | set(have_groups) if select_all else set(want_groups)

        for name in names:
            w = want_groups.get(name, {})
            h = have_groups.get(name, {})
            if w == h:
                continue

            if name in have_groups and name not in want_groups:
                self.commands.append("delete vpn ipsec ike-group {0}".format(name))
                continue

            if name not in have_groups:
                self.addcmd({"name": name}, "ike_group", False)

            self._cmp_scalar(
                w,
                h,
                "key_exchange",
                {"name": name},
                "ike_group.key_exchange",
                reconcile,
            )
            for field in ("close_action", "lifetime", "mode"):
                self._cmp_scalar(
                    w,
                    h,
                    field,
                    {"name": name},
                    "ike_group.{0}".format(field),
                    reconcile,
                )
            for field in ("disable_mobike", "ikev2_reauth"):
                self._cmp_bool(
                    w,
                    h,
                    field,
                    {"name": name},
                    "ike_group.{0}".format(field),
                    reconcile,
                )

            w_dpd = w.get("dead_peer_detection", {})
            h_dpd = h.get("dead_peer_detection", {})
            for field in ("action", "interval", "timeout"):
                self._cmp_scalar(
                    w_dpd,
                    h_dpd,
                    field,
                    {"name": name},
                    "ike_group.dead_peer_detection.{0}".format(field),
                    reconcile,
                )

            self._compare_proposals(
                w.get("proposal", {}),
                h.get("proposal", {}),
                {"name": name},
                "ike_group.proposal",
                "ike_group.proposal.encryption",
                "ike_group.proposal.hash",
                "ike_group.proposal.dh_group",
                reconcile,
            )

    # -------------------------------------------------------------------
    # Proposals (shared by esp_group / ike_group)
    # -------------------------------------------------------------------

    def _compare_proposals(
        self,
        want_props,
        have_props,
        group_ctx,
        bare_parser,
        encryption_parser,
        hash_parser,
        dh_group_parser,
        reconcile,
    ):
        # a proposal collection lives entirely inside an already-selected
        # group -- once that group is in scope, its own proposals always
        # get full reconciliation under replaced/overridden (never a
        # separate select_all concern of their own).
        ids = set(want_props) | set(have_props) if reconcile else set(want_props)
        for pid in ids:
            w = want_props.get(pid, {})
            h = have_props.get(pid, {})
            if w == h:
                continue

            if pid in have_props and pid not in want_props:
                self.addcmd(dict(group_ctx, proposal_id=pid), bare_parser, True)
                continue

            if pid not in have_props:
                self.addcmd(dict(group_ctx, proposal_id=pid), bare_parser, False)

            ctx = dict(group_ctx, proposal_id=pid)
            self._cmp_scalar(w, h, "encryption", ctx, encryption_parser, reconcile)
            self._cmp_scalar(w, h, "hash", ctx, hash_parser, reconcile)
            if dh_group_parser:
                self._cmp_scalar(w, h, "dh_group", ctx, dh_group_parser, reconcile)

    # -------------------------------------------------------------------
    # Profiles
    # -------------------------------------------------------------------

    def _compare_profiles(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        have_profiles = haved.get("profile", {})

        if scoped_delete is not None:
            for name in set(scoped_delete.get("profile", {})):
                if name in have_profiles:
                    self.commands.append("delete vpn ipsec profile {0}".format(name))
            return

        want_profiles = wantd.get("profile", {})
        names = set(want_profiles) | set(have_profiles) if select_all else set(want_profiles)

        for name in names:
            w = want_profiles.get(name, {})
            h = have_profiles.get(name, {})
            if w == h:
                continue

            if name in have_profiles and name not in want_profiles:
                self.commands.append("delete vpn ipsec profile {0}".format(name))
                continue

            if name not in have_profiles:
                self.addcmd({"name": name}, "profile", False)

            ctx = {"name": name}
            w_auth = w.get("authentication", {})
            h_auth = h.get("authentication", {})
            self._cmp_scalar(
                w_auth,
                h_auth,
                "mode",
                ctx,
                "profile.authentication.mode",
                reconcile,
            )
            self._cmp_scalar(
                w_auth,
                h_auth,
                "pre_shared_secret",
                ctx,
                "profile.authentication.pre_shared_secret",
                reconcile,
            )
            self._cmp_scalar(w, h, "esp_group", ctx, "profile.esp_group", reconcile)
            self._cmp_scalar(w, h, "ike_group", ctx, "profile.ike_group", reconcile)
            self._cmp_bool(w, h, "disable", ctx, "profile.disable", reconcile)

            w_tunnels = set(w.get("bind_tunnel") or [])
            h_tunnels = set(h.get("bind_tunnel") or [])
            for tun in w_tunnels - h_tunnels:
                self.addcmd(dict(ctx, bind_tunnel=tun), "profile.bind_tunnel", False)
            if reconcile:
                for tun in h_tunnels - w_tunnels:
                    self.addcmd(dict(ctx, bind_tunnel=tun), "profile.bind_tunnel", True)

    # -------------------------------------------------------------------
    # PSKs
    # -------------------------------------------------------------------

    def _compare_psks(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        have_psks = haved.get("authentication", {}).get("psk", {})

        if scoped_delete is not None:
            for name in set(scoped_delete.get("authentication", {}).get("psk", {})):
                if name in have_psks:
                    self.commands.append(
                        "delete vpn ipsec authentication psk {0}".format(name),
                    )
            return

        want_psks = wantd.get("authentication", {}).get("psk", {})
        names = set(want_psks) | set(have_psks) if select_all else set(want_psks)

        for name in names:
            w = want_psks.get(name, {})
            h = have_psks.get(name, {})
            if w == h:
                continue

            if name in have_psks and name not in want_psks:
                self.commands.append("delete vpn ipsec authentication psk {0}".format(name))
                continue

            if name not in have_psks:
                self.addcmd({"name": name}, "authentication.psk", False)

            ctx = {"name": name}
            self._cmp_scalar(w, h, "secret", ctx, "authentication.psk.secret", reconcile)
            self._cmp_scalar(
                w,
                h,
                "secret_type",
                ctx,
                "authentication.psk.secret_type",
                reconcile,
            )

            w_ids = set(w.get("id") or [])
            h_ids = set(h.get("id") or [])
            for i in w_ids - h_ids:
                self.addcmd(dict(ctx, id=i), "authentication.psk.id", False)
            if reconcile:
                for i in h_ids - w_ids:
                    self.addcmd(dict(ctx, id=i), "authentication.psk.id", True)

            w_dhcp = set(w.get("dhcp_interface") or [])
            h_dhcp = set(h.get("dhcp_interface") or [])
            for i in w_dhcp - h_dhcp:
                self.addcmd(dict(ctx, dhcp_interface=i), "authentication.psk.dhcp_interface", False)
            if reconcile:
                for i in h_dhcp - w_dhcp:
                    self.addcmd(
                        dict(ctx, dhcp_interface=i),
                        "authentication.psk.dhcp_interface",
                        True,
                    )

    def _compare_ppks(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        have_ppks = haved.get("authentication", {}).get("ppk", {})

        if scoped_delete is not None:
            for name in set(scoped_delete.get("authentication", {}).get("ppk", {})):
                if name in have_ppks:
                    self.commands.append(
                        "delete vpn ipsec authentication ppk {0}".format(name),
                    )
            return

        want_ppks = wantd.get("authentication", {}).get("ppk", {})
        names = set(want_ppks) | set(have_ppks) if select_all else set(want_ppks)

        for name in names:
            w = want_ppks.get(name, {})
            h = have_ppks.get(name, {})
            if w == h:
                continue

            if name in have_ppks and name not in want_ppks:
                self.commands.append("delete vpn ipsec authentication ppk {0}".format(name))
                continue

            if name not in have_ppks:
                self.addcmd({"name": name}, "authentication.ppk", False)

            ctx = {"name": name}
            self._cmp_scalar(w, h, "secret", ctx, "authentication.ppk.secret", reconcile)
            self._cmp_scalar(
                w,
                h,
                "secret_type",
                ctx,
                "authentication.ppk.secret_type",
                reconcile,
            )

            w_ids = set(w.get("id") or [])
            h_ids = set(h.get("id") or [])
            for i in w_ids - h_ids:
                self.addcmd(dict(ctx, id=i), "authentication.ppk.id", False)
            if reconcile:
                for i in h_ids - w_ids:
                    self.addcmd(dict(ctx, id=i), "authentication.ppk.id", True)

    # -------------------------------------------------------------------
    # Top-level scalar / list / bool fields
    #
    # NOTE: these are all direct fields of the single top-level config
    # object, not named collections -- there is no "item entirely absent
    # from want" concept here, only "field omitted from want". So only
    # `reconcile` applies; `select_all` is irrelevant at this level (it's
    # accepted for a consistent call signature but unused).
    # -------------------------------------------------------------------

    def _compare_top_level(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        if scoped_delete is not None:
            # Principle: naming a parameter under scoped `deleted` means
            # "delete this specific value" -- a scalar/bool key present
            # (regardless of value) signals whole-field removal; a list
            # value present means "delete exactly these elements", not
            # the whole list, mirroring vyos_vrf's bind_to_all precedent
            # extended consistently to list- and nested-dict-shaped
            # fields.
            if "disable_uniqreqids" in scoped_delete and haved.get("disable_uniqreqids"):
                self.commands.append("delete vpn ipsec disable-uniqreqids")

            h_ifaces = set(haved.get("interface") or [])
            for i in set(scoped_delete.get("interface") or []) & h_ifaces:
                self.addcmd({"interface": i}, "interface", True)

            s_log = scoped_delete.get("log", {})
            h_log = haved.get("log", {})
            if "level" in s_log and "level" in h_log:
                self.addcmd({"level": h_log["level"]}, "log.level", True)
            h_sub = set(h_log.get("subsystem") or [])
            for s in set(s_log.get("subsystem") or []) & h_sub:
                self.addcmd({"subsystem": s}, "log.subsystem", True)

            s_opt = scoped_delete.get("options", {})
            h_opt = haved.get("options", {})
            for field in ("disable_route_autoinstall", "flexvpn", "virtual_ip"):
                if field in s_opt and h_opt.get(field):
                    self.addcmd({}, "options.{0}".format(field), True)
            if "interface" in s_opt and "interface" in h_opt:
                self.addcmd({"interface": h_opt["interface"]}, "options.interface", True)

            s_retrans = s_opt.get("retransmission", {})
            h_retrans = h_opt.get("retransmission", {})
            for field in ("attempts", "base", "timeout"):
                if field in s_retrans and field in h_retrans:
                    self.addcmd(
                        {field: h_retrans[field]},
                        "options.retransmission.{0}".format(field),
                        True,
                    )
            return

        self._cmp_bool(wantd, haved, "disable_uniqreqids", {}, "disable_uniqreqids", reconcile)

        w_ifaces = set(wantd.get("interface") or [])
        h_ifaces = set(haved.get("interface") or [])
        for i in w_ifaces - h_ifaces:
            self.addcmd({"interface": i}, "interface", False)
        if reconcile:
            for i in h_ifaces - w_ifaces:
                self.addcmd({"interface": i}, "interface", True)

        w_log = wantd.get("log", {})
        h_log = haved.get("log", {})
        self._cmp_scalar(w_log, h_log, "level", {}, "log.level", reconcile)
        w_sub = set(w_log.get("subsystem") or [])
        h_sub = set(h_log.get("subsystem") or [])
        for s in w_sub - h_sub:
            self.addcmd({"subsystem": s}, "log.subsystem", False)
        if reconcile:
            for s in h_sub - w_sub:
                self.addcmd({"subsystem": s}, "log.subsystem", True)

        w_opt = wantd.get("options", {})
        h_opt = haved.get("options", {})
        for field in ("disable_route_autoinstall", "flexvpn", "virtual_ip"):
            self._cmp_bool(w_opt, h_opt, field, {}, "options.{0}".format(field), reconcile)
        self._cmp_scalar(w_opt, h_opt, "interface", {}, "options.interface", reconcile)

        w_retrans = w_opt.get("retransmission", {})
        h_retrans = h_opt.get("retransmission", {})
        for field in ("attempts", "base", "timeout"):
            self._cmp_scalar(
                w_retrans,
                h_retrans,
                field,
                {},
                "options.retransmission.{0}".format(field),
                reconcile,
            )

    # -------------------------------------------------------------------
    # Field-level helpers (mirrors vyos_nat's _cmp_scalar / _cmp_bool)
    # -------------------------------------------------------------------

    def _cmp_scalar(self, want, have, field, ctx, parser, reconcile=False):
        w = want.get(field)
        h = have.get(field)
        if w != h:
            if w is not None:
                self.addcmd(dict(ctx, **{field: w}), parser, False)
            elif reconcile and h is not None:
                self.addcmd(dict(ctx, **{field: h}), parser, True)

    def _cmp_bool(self, want, have, field, ctx, parser, reconcile=False):
        # An explicitly-specified value (even False) is always enforced,
        # regardless of state -- that's the user directly saying what
        # they want. An OMITTED field is only enforced (i.e. deleted if
        # currently True) under full reconciliation (replaced/overridden).
        # Under merged, an omitted field is left alone -- protected
        # further upstream by dict_merge backfilling `want` from `have`
        # before this is ever reached, but this still needs to be correct
        # in isolation (e.g. for a field nested inside a dict that wasn't
        # part of the dict_merge'd top-level structure).
        explicit = field in want
        w = bool(want.get(field))
        h = bool(have.get(field))
        if w != h and (w or explicit or reconcile):
            self.addcmd(dict(ctx), parser, not w)
