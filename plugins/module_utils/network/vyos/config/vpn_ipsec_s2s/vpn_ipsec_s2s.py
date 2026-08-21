#
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_vpn_ipsec_s2s config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.

Mirrors vyos_vpn_ipsec's config.py exactly -- same list-to-dict
conversion + explicit per-state branching, same select_all/reconcile
two-flag design for the replaced/overridden distinction, same scoped
deleted handling. See that file's own docstring for the full state
semantics; the summary:

  - merged:     only items/fields named in `want` are touched.
  - replaced:   only items NAMED in `want` are touched, but each named
                item is fully reconciled (omitted fields removed).
  - overridden: every item is in scope, including ones absent from
                `want` -- those get deleted wholesale. Named items
                reconciled the same way as replaced.
  - deleted:    bare (no config) deletes everything; a scoped config
                deletes only what's named, down to individual list
                elements.
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
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vpn_ipsec_s2s import (
    Vpn_ipsec_s2sTemplate,
)


class Vpn_ipsec_s2s(ResourceModule):
    """
    The vyos_vpn_ipsec_s2s config class
    """

    def __init__(self, module):
        super(Vpn_ipsec_s2s, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vpn_ipsec_s2s",
            tmplt=Vpn_ipsec_s2sTemplate(),
        )

    def execute_module(self):
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        wantd = deepcopy(self.want) or {}
        haved = deepcopy(self.have) or {}

        for entry in (wantd, haved):
            self._list_to_dict(entry)

        scoped_delete = None
        if self.state == "deleted":
            if wantd:
                scoped_delete = wantd
            wantd = {}

        if self.state == "merged":
            # list_to_dict() above must run BEFORE this -- dict_merge
            # concatenates raw lists rather than merging matching items
            # by key, so it only does the right thing once both sides
            # are already name-keyed dicts.
            wantd = dict_merge(haved, wantd)

        select_all = self.state in ("overridden", "deleted")
        reconcile = self.state in ("replaced", "overridden", "deleted")

        self._compare_peers(wantd, haved, select_all, reconcile, scoped_delete)

        self.commands = list(dict.fromkeys(self.commands))

    # -------------------------------------------------------------------
    # List -> name-keyed dict conversion
    # -------------------------------------------------------------------

    def _list_to_dict(self, config):
        peers = config.get("peer")
        if isinstance(peers, list):
            config["peer"] = {p["name"]: p for p in peers}
            for peer in config["peer"].values():
                if isinstance(peer.get("tunnel"), list):
                    peer["tunnel"] = {t["tunnel_id"]: t for t in peer["tunnel"]}

    # -------------------------------------------------------------------
    # Peers
    # -------------------------------------------------------------------

    def _compare_peers(self, wantd, haved, select_all, reconcile, scoped_delete=None):
        have_peers = haved.get("peer", {})

        if scoped_delete is not None:
            for name in set(scoped_delete.get("peer", {})):
                if name in have_peers:
                    self.commands.append(
                        "delete vpn ipsec site-to-site peer {0}".format(name),
                    )
            return

        want_peers = wantd.get("peer", {})
        names = set(want_peers) | set(have_peers) if select_all else set(want_peers)

        for name in names:
            w = want_peers.get(name, {})
            h = have_peers.get(name, {})
            if w == h:
                continue

            if name in have_peers and name not in want_peers:
                self.commands.append(
                    "delete vpn ipsec site-to-site peer {0}".format(name),
                )
                continue

            if name not in have_peers:
                self.addcmd({"name": name}, "peer", False)

            ctx = {"name": name}
            self._cmp_bool(w, h, "disable", ctx, "peer.disable", reconcile)

            w_auth = w.get("authentication", {})
            h_auth = h.get("authentication", {})
            for field in ("local_id", "remote_id", "mode"):
                self._cmp_scalar(
                    w_auth,
                    h_auth,
                    field,
                    ctx,
                    "peer.authentication.{0}".format(field),
                    reconcile,
                )
            self._cmp_bool(
                w_auth,
                h_auth,
                "use_x509_id",
                ctx,
                "peer.authentication.use_x509_id",
                reconcile,
            )

            w_ppk = w_auth.get("ppk", {})
            h_ppk = h_auth.get("ppk", {})
            self._cmp_scalar(w_ppk, h_ppk, "id", ctx, "peer.authentication.ppk.id", reconcile)
            self._cmp_bool(
                w_ppk,
                h_ppk,
                "required",
                ctx,
                "peer.authentication.ppk.required",
                reconcile,
            )

            w_rsa = w_auth.get("rsa", {})
            h_rsa = h_auth.get("rsa", {})
            for field in ("local_key", "remote_key", "passphrase"):
                self._cmp_scalar(
                    w_rsa,
                    h_rsa,
                    field,
                    ctx,
                    "peer.authentication.rsa.{0}".format(field),
                    reconcile,
                )

            w_x509 = w_auth.get("x509", {})
            h_x509 = h_auth.get("x509", {})
            for field in ("certificate", "passphrase"):
                self._cmp_scalar(
                    w_x509,
                    h_x509,
                    field,
                    ctx,
                    "peer.authentication.x509.{0}".format(field),
                    reconcile,
                )
            w_ca = set(w_x509.get("ca_certificate") or [])
            h_ca = set(h_x509.get("ca_certificate") or [])
            for cert in w_ca - h_ca:
                self.addcmd(
                    dict(ctx, ca_certificate=cert),
                    "peer.authentication.x509.ca_certificate",
                    False,
                )
            if reconcile:
                for cert in h_ca - w_ca:
                    self.addcmd(
                        dict(ctx, ca_certificate=cert),
                        "peer.authentication.x509.ca_certificate",
                        True,
                    )

            for field in (
                "childless",
                "connection_type",
                "default_esp_group",
                "description",
                "dhcp_interface",
                "ike_group",
                "ikev2_reauth",
                "local_address",
            ):
                self._cmp_scalar(w, h, field, ctx, "peer.{0}".format(field), reconcile)
            self._cmp_bool(
                w,
                h,
                "force_udp_encapsulation",
                ctx,
                "peer.force_udp_encapsulation",
                reconcile,
            )
            self._cmp_scalar(w, h, "replay_window", ctx, "peer.replay_window", reconcile)

            w_remote_addr = set(w.get("remote_address") or [])
            h_remote_addr = set(h.get("remote_address") or [])
            for addr in w_remote_addr - h_remote_addr:
                self.addcmd(dict(ctx, remote_address=addr), "peer.remote_address", False)
            if reconcile:
                for addr in h_remote_addr - w_remote_addr:
                    self.addcmd(dict(ctx, remote_address=addr), "peer.remote_address", True)

            w_virt_addr = set(w.get("virtual_address") or [])
            h_virt_addr = set(h.get("virtual_address") or [])
            for addr in w_virt_addr - h_virt_addr:
                self.addcmd(dict(ctx, virtual_address=addr), "peer.virtual_address", False)
            if reconcile:
                for addr in h_virt_addr - w_virt_addr:
                    self.addcmd(dict(ctx, virtual_address=addr), "peer.virtual_address", True)

            self._compare_tunnels(w.get("tunnel", {}), h.get("tunnel", {}), ctx, reconcile)
            self._compare_vti(w.get("vti", {}), h.get("vti", {}), ctx, reconcile)

    # -------------------------------------------------------------------
    # Tunnels (nested collection within a peer)
    # -------------------------------------------------------------------

    def _compare_tunnels(self, want_tunnels, have_tunnels, peer_ctx, reconcile):
        # A tunnel collection lives entirely inside an already-selected
        # peer -- once that peer is in scope, its own tunnels always get
        # full reconciliation under replaced/overridden, matching how
        # esp_group/ike_group's own nested proposals behave in the
        # profile module.
        ids = set(want_tunnels) | set(have_tunnels) if reconcile else set(want_tunnels)
        for tid in ids:
            w = want_tunnels.get(tid, {})
            h = have_tunnels.get(tid, {})
            if w == h:
                continue

            if tid in have_tunnels and tid not in want_tunnels:
                self.addcmd(dict(peer_ctx, tunnel_id=tid), "peer.tunnel", True)
                continue

            if tid not in have_tunnels:
                self.addcmd(dict(peer_ctx, tunnel_id=tid), "peer.tunnel", False)

            ctx = dict(peer_ctx, tunnel_id=tid)
            self._cmp_bool(w, h, "disable", ctx, "peer.tunnel.disable", reconcile)
            for field in ("esp_group", "protocol"):
                self._cmp_scalar(w, h, field, ctx, "peer.tunnel.{0}".format(field), reconcile)
            self._cmp_scalar(w, h, "priority", ctx, "peer.tunnel.priority", reconcile)

            for side in ("local", "remote"):
                w_side = w.get(side, {})
                h_side = h.get(side, {})
                self._cmp_scalar(
                    w_side,
                    h_side,
                    "port",
                    ctx,
                    "peer.tunnel.{0}.port".format(side),
                    reconcile,
                )
                w_prefix = set(w_side.get("prefix") or [])
                h_prefix = set(h_side.get("prefix") or [])
                for p in w_prefix - h_prefix:
                    self.addcmd(
                        dict(ctx, prefix=p),
                        "peer.tunnel.{0}.prefix".format(side),
                        False,
                    )
                if reconcile:
                    for p in h_prefix - w_prefix:
                        self.addcmd(
                            dict(ctx, prefix=p),
                            "peer.tunnel.{0}.prefix".format(side),
                            True,
                        )

    # -------------------------------------------------------------------
    # VTI (nested dict within a peer, not a collection)
    # -------------------------------------------------------------------

    def _compare_vti(self, w_vti, h_vti, peer_ctx, reconcile):
        for field in ("bind", "esp_group"):
            self._cmp_scalar(w_vti, h_vti, field, peer_ctx, "peer.vti.{0}".format(field), reconcile)

        w_ts = w_vti.get("traffic_selector", {})
        h_ts = h_vti.get("traffic_selector", {})
        for side in ("local", "remote"):
            w_prefix = set(w_ts.get(side, {}).get("prefix") or [])
            h_prefix = set(h_ts.get(side, {}).get("prefix") or [])
            parser = "peer.vti.traffic_selector.{0}.prefix".format(side)
            for p in w_prefix - h_prefix:
                self.addcmd(dict(peer_ctx, prefix=p), parser, False)
            if reconcile:
                for p in h_prefix - w_prefix:
                    self.addcmd(dict(peer_ctx, prefix=p), parser, True)

    # -------------------------------------------------------------------
    # Field-level helpers (mirrors vyos_vpn_ipsec's own)
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
        explicit = field in want
        w = bool(want.get(field))
        h = bool(have.get(field))
        if w != h and (w or explicit or reconcile):
            self.addcmd(dict(ctx), parser, not w)
