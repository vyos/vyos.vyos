# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.nat import (
    NatTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.utils import combine


class Nat(ResourceModule):
    """The vyos_nat config class"""

    def __init__(self, module):
        super(Nat, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="nat",
            tmplt=NatTemplate(),
        )
        self.parsers = []

    def execute_module(self):
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        wantd = deepcopy(self.want)
        haved = deepcopy(self.have)

        if self.state == "merged":
            wantd = combine(haved, wantd, recursive=True, list_merge="append_rp")

        if self.state == "deleted":
            if not wantd:
                for nat_type in haved:
                    self.commands.append(f"delete {nat_type}")
                return
            self._list_to_dict(wantd)
            self._list_to_dict(haved)
            self._delete_nat_objects(wantd, haved, only_missing=False)
            return

        self._list_to_dict(wantd)
        self._list_to_dict(haved)

        if self.state == "replaced":
            self._delete_nat_objects(wantd, haved, only_missing=False)
            self._set_commands(wantd, haved)
        elif self.state == "overridden":
            self._delete_nat_objects(wantd, haved, only_missing=True)
            self._delete_nat_objects(wantd, haved, only_missing=False)
            self._set_commands(wantd, haved)
        else:
            self._set_commands(wantd, haved)

        self.commands = list(dict.fromkeys(self.commands))

    # -------------------------------------------------------------------------
    # List → keyed dict conversion
    # -------------------------------------------------------------------------

    def _list_to_dict(self, config):
        nat = config.get("nat", {})
        cgnat = nat.get("cgnat", {})

        pool = cgnat.get("pool", {})
        for ptype in ("external", "internal"):
            entries = pool.get(ptype)
            if isinstance(entries, list):
                pool[ptype] = {item["name"]: item for item in entries}

        rules = cgnat.get("rule")
        if isinstance(rules, list):
            cgnat["rule"] = {r["id"]: r for r in rules}

        for section in ("destination", "source", "static"):
            rules = nat.get(section, {}).get("rule")
            if isinstance(rules, list):
                nat[section]["rule"] = {r["id"]: r for r in rules}

        nat64 = config.get("nat64", {})
        rules = nat64.get("source", {}).get("rule")
        if isinstance(rules, list):
            nat64["source"]["rule"] = {r["id"]: r for r in rules}
            for rule in nat64["source"]["rule"].values():
                pools = rule.get("translation", {}).get("pool")
                if isinstance(pools, list):
                    rule["translation"]["pool"] = {p["id"]: p for p in pools}

        nat66 = config.get("nat66", {})
        for section in ("destination", "source"):
            rules = nat66.get(section, {}).get("rule")
            if isinstance(rules, list):
                nat66[section]["rule"] = {r["id"]: r for r in rules}

    # -------------------------------------------------------------------------
    # Top-level dispatch
    # -------------------------------------------------------------------------

    def _set_commands(self, wantd, haved):
        self._compare_cgnat_global(wantd, haved)
        self._compare_cgnat_pools(wantd, haved)
        self._compare_cgnat_rules(wantd, haved)

        for section in ("destination", "source", "static"):
            self._compare_nat_rules("nat", section, wantd, haved)

        self._compare_nat_rules("nat64", "source", wantd, haved)

        for section in ("destination", "source"):
            self._compare_nat_rules("nat66", section, wantd, haved)

        self.commands = list(dict.fromkeys(self.commands))

    # -------------------------------------------------------------------------
    # Delete helpers
    # -------------------------------------------------------------------------

    def _delete_nat_objects(self, wantd, haved, only_missing=False):
        """
        Generate delete commands for NAT objects.
        only_missing=False: delete objects present in both want and have (when different)
        only_missing=True:  delete objects present in have but absent from want
        """
        for nat_type in haved:
            want_nat = wantd.get(nat_type, {})
            have_nat = haved[nat_type]

            if only_missing and nat_type not in wantd:
                self.commands.append(f"delete {nat_type}")
                continue

            for section in have_nat:
                want_section = want_nat.get(section, {})
                have_section = have_nat[section]

                if only_missing and section not in want_nat:
                    self.commands.append(
                        f"delete {nat_type} {section.replace('_', '-')}",
                    )
                    continue

                if section == "cgnat":
                    for pool_type in ("external", "internal"):
                        want_pools = want_section.get("pool", {}).get(pool_type, {})
                        have_pools = have_section.get("pool", {}).get(pool_type, {})
                        for name in have_pools:
                            if only_missing and name not in want_pools:
                                self.commands.append(
                                    f"delete {nat_type} cgnat pool {pool_type} {name}",
                                )
                            elif not only_missing and name in want_pools:
                                if want_pools[name] != have_pools[name]:
                                    self.commands.append(
                                        f"delete {nat_type} cgnat pool {pool_type} {name}",
                                    )
                    want_rules = want_section.get("rule", {})
                    have_rules = have_section.get("rule", {})
                    for rid in have_rules:
                        if only_missing and rid not in want_rules:
                            self.commands.append(f"delete {nat_type} cgnat rule {rid}")
                        elif not only_missing and rid in want_rules:
                            if want_rules[rid] != have_rules[rid]:
                                self.commands.append(f"delete {nat_type} cgnat rule {rid}")
                else:
                    want_rules = want_section.get("rule", {})
                    have_rules = have_section.get("rule", {})
                    cli_section = section.replace("_", "-")
                    for rid in have_rules:
                        if only_missing and rid not in want_rules:
                            self.commands.append(
                                f"delete {nat_type} {cli_section} rule {rid}",
                            )
                        elif not only_missing and rid in want_rules:
                            if want_rules[rid] != have_rules[rid]:
                                self.commands.append(
                                    f"delete {nat_type} {cli_section} rule {rid}",
                                )

    # -------------------------------------------------------------------------
    # CGNAT
    # -------------------------------------------------------------------------

    def _compare_cgnat_global(self, wantd, haved):
        if self.state in ("replaced", "overridden") and not wantd.get("nat", {}).get("cgnat"):
            return
        w = wantd.get("nat", {}).get("cgnat", {}).get("log_allocation")
        h = haved.get("nat", {}).get("cgnat", {}).get("log_allocation")
        if bool(w) != bool(h):
            self.addcmd(
                {"nat": {"cgnat": {"log_allocation": True}}},
                "cgnat_log_allocation",
                not bool(w),
            )

    def _compare_cgnat_pools(self, wantd, haved):
        want_ext = wantd.get("nat", {}).get("cgnat", {}).get("pool", {}).get("external", {})
        have_ext = haved.get("nat", {}).get("cgnat", {}).get("pool", {}).get("external", {})
        want_int = wantd.get("nat", {}).get("cgnat", {}).get("pool", {}).get("internal", {})
        have_int = haved.get("nat", {}).get("cgnat", {}).get("pool", {}).get("internal", {})

        scope = self.state in ("replaced", "overridden")
        ext_names = set(want_ext) if scope else set(want_ext) | set(have_ext)
        int_names = set(want_int) if scope else set(want_int) | set(have_int)

        for name in ext_names:
            self._compare_external_pool(name, want_ext.get(name, {}), have_ext.get(name, {}))

        for name in int_names:
            self._compare_internal_pool(name, want_int.get(name, {}), have_int.get(name, {}))

    def _compare_external_pool(self, name, want, have):
        w = want.get("external_port_range")
        h = have.get("external_port_range")
        if w != h:
            if w:
                self.addcmd({"name": name, "range": w}, "cgnat_pool_external_port_range", False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd({"name": name, "range": h}, "cgnat_pool_external_port_range", True)

        w = want.get("per_user_limit", {}).get("port")
        h = have.get("per_user_limit", {}).get("port")
        if w != h:
            if w:
                self.addcmd({"name": name, "limit": w}, "cgnat_pool_external_per_user", False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd({"name": name, "limit": h}, "cgnat_pool_external_per_user", True)

        want_ranges = {(r["value"] if isinstance(r, dict) else r): r for r in want.get("range", [])}
        have_ranges = {(r["value"] if isinstance(r, dict) else r): r for r in have.get("range", [])}
        for val, rng in want_ranges.items():
            if val not in have_ranges:
                seq = rng.get("seq") if isinstance(rng, dict) else None
                self.addcmd(
                    {"name": name, "range": val, "seq": seq},
                    "cgnat_pool_external_range",
                    False,
                )

        if self.state in ("replaced", "overridden"):
            for val in have_ranges:
                if val not in want_ranges:
                    self.addcmd({"name": name, "range": val}, "cgnat_pool_external_range", True)

    def _compare_internal_pool(self, name, want, have):
        want_ranges = set(want.get("range", []))
        have_ranges = set(have.get("range", []))

        for rng in want_ranges - have_ranges:
            self.addcmd({"name": name, "range": rng}, "cgnat_pool_internal_range", False)

        if self.state in ("replaced", "overridden"):
            for rng in have_ranges - want_ranges:
                self.addcmd({"name": name, "range": rng}, "cgnat_pool_internal_range", True)

    def _compare_cgnat_rules(self, wantd, haved):
        want_rules = wantd.get("nat", {}).get("cgnat", {}).get("rule", {})
        have_rules = haved.get("nat", {}).get("cgnat", {}).get("rule", {})

        rids = (
            set(want_rules)
            if self.state in ("replaced", "overridden")
            else set(want_rules) | set(have_rules)
        )

        for rid in rids:
            w = want_rules.get(rid, {})
            h = have_rules.get(rid, {})

            if self.state in ("replaced", "overridden") and w != h:
                h = {}

            w_src = w.get("source", {}).get("pool")
            h_src = h.get("source", {}).get("pool")
            if w_src != h_src:
                if w_src:
                    self.addcmd({"id": rid, "pool": w_src}, "cgnat_rule_source_pool", False)
                elif self.state in ("replaced", "overridden"):
                    self.addcmd({"id": rid, "pool": h_src}, "cgnat_rule_source_pool", True)

            w_tr = w.get("translation", {}).get("pool")
            h_tr = h.get("translation", {}).get("pool")
            if w_tr != h_tr:
                if w_tr:
                    self.addcmd({"id": rid, "pool": w_tr}, "cgnat_rule_translation_pool", False)
                elif self.state in ("replaced", "overridden"):
                    self.addcmd({"id": rid, "pool": h_tr}, "cgnat_rule_translation_pool", True)

    # -------------------------------------------------------------------------
    # NAT / NAT64 / NAT66 rules
    # -------------------------------------------------------------------------

    def _compare_nat_rules(self, nat_type, section, wantd, haved):
        want_rules = wantd.get(nat_type, {}).get(section, {}).get("rule", {})
        have_rules = haved.get(nat_type, {}).get(section, {}).get("rule", {})

        rids = (
            set(want_rules)
            if self.state in ("replaced", "overridden")
            else set(want_rules) | set(have_rules)
        )

        for rid in rids:
            w = want_rules.get(rid, {})
            h = have_rules.get(rid, {})
            if self.state in ("replaced", "overridden") and w != h:
                h = {}
            if w == h and self.state != "rendered":
                continue
            self._compare_rule(nat_type, section, rid, w, h)

    def _compare_rule(self, nat_type, section, rid, want, have):
        ctx = {"nat": nat_type, "type": section, "id": rid}

        for field in set(want) | set(have):
            val = want.get(field) if field in want else have.get(field)
            if isinstance(val, bool):
                self._cmp_bool(want, have, field, ctx, f"nat_type_{field}")
            elif isinstance(val, str):
                self._cmp_scalar(want, have, field, ctx, f"nat_type_{field}")

        self._cmp_interface(want, have, ctx, nat_type, section)
        self._cmp_outbound_interface(want, have, ctx)
        for atype in ("destination", "source"):
            self._cmp_addr_sub(want, have, atype, ctx)
        self._cmp_translation(want, have, ctx)
        self._cmp_match_mark(want, have, ctx)
        self._cmp_nat64_pools(want, have, ctx)

    # -------------------------------------------------------------------------
    # Field-level helpers
    # -------------------------------------------------------------------------

    def _cmp_scalar(self, want, have, field, ctx, parser):
        w = want.get(field)
        h = have.get(field)
        if w != h:
            if w is not None:
                self.addcmd(dict(ctx, **{field: w}), parser, False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx, **{field: h}), parser, True)

    def _cmp_bool(self, want, have, field, ctx, parser):
        w = bool(want.get(field))
        h = bool(have.get(field))
        if w != h:
            if w:
                self.addcmd(dict(ctx), parser, False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx), parser, True)

    def _cmp_interface(self, want, have, ctx, nat_type, section):
        iface_w = want.get("inbound_interface")
        iface_h = have.get("inbound_interface")
        if iface_w == iface_h:
            return

        if nat_type == "nat" and section == "static":
            if iface_w:
                self.addcmd(dict(ctx, value=iface_w), "nat_static_inbound_interface", False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx, value=iface_h), "nat_static_inbound_interface", True)
            return

        iface_w = iface_w or {}
        iface_h = iface_h or {}

        if nat_type == "nat":
            parser_name = "nat_inbound_interface_name"
            parser_group = "nat_inbound_interface_group"
        else:
            parser_name = "nat6x_inbound_interface"
            parser_group = "nat6x_inbound_interface"

        if iface_w.get("name") != iface_h.get("name"):
            if iface_w.get("name"):
                self.addcmd(dict(ctx, value=iface_w["name"]), parser_name, False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx, value=iface_h["name"]), parser_name, True)

        if nat_type == "nat" and iface_w.get("group") != iface_h.get("group"):
            if iface_w.get("group"):
                self.addcmd(dict(ctx, value=iface_w["group"]), parser_group, False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx, value=iface_h["group"]), parser_group, True)

    def _cmp_outbound_interface(self, want, have, ctx):
        iface_w = want.get("outbound_interface") or {}
        iface_h = have.get("outbound_interface") or {}

        if iface_w.get("name") != iface_h.get("name"):
            if iface_w.get("name"):
                self.addcmd(dict(ctx, value=iface_w["name"]), "nat_type_outbound_interface", False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx, value=iface_h["name"]), "nat_type_outbound_interface", True)

        if iface_w.get("group") != iface_h.get("group"):
            if iface_w.get("group"):
                self.addcmd(
                    dict(ctx, value=iface_w["group"]),
                    "nat_type_outbound_interface_group",
                    False,
                )
            elif self.state in ("replaced", "overridden"):
                self.addcmd(
                    dict(ctx, value=iface_h["group"]),
                    "nat_type_outbound_interface_group",
                    True,
                )

    def _cmp_addr_sub(self, want, have, atype, ctx):
        sub_w = want.get(atype) or {}
        sub_h = have.get(atype) or {}
        if sub_w == sub_h:
            return

        changed = {k: v for k, v in sub_w.items() if sub_h.get(k) != v}
        removed = {
            k: v
            for k, v in sub_h.items()
            if k not in sub_w and self.state in ("replaced", "overridden")
        }

        if changed:
            self.addcmd(dict(ctx, atype=atype, sub=changed), "nat_type_address", False)
        if removed:
            self.addcmd(dict(ctx, atype=atype, sub=removed), "nat_type_address", True)

    def _cmp_translation(self, want, have, ctx):
        trans_w = want.get("translation") or {}
        trans_h = have.get("translation") or {}
        if trans_w == trans_h:
            return

        changed = {k: v for k, v in trans_w.items() if k != "pool" and trans_h.get(k) != v}
        removed = {
            k: v
            for k, v in trans_h.items()
            if k != "pool" and k not in trans_w and self.state in ("replaced", "overridden")
        }

        if changed:
            self.addcmd(dict(ctx, translation=changed), "nat_type_translation_address", False)
        if removed:
            self.addcmd(dict(ctx, translation=removed), "nat_type_translation_address", True)

    def _cmp_match_mark(self, want, have, ctx):
        w = want.get("match", {}).get("mark")
        h = have.get("match", {}).get("mark")
        if w != h:
            if w is not None:
                self.addcmd(dict(ctx, mark=w), "nat64_match_mark", False)
            elif self.state in ("replaced", "overridden"):
                self.addcmd(dict(ctx, mark=h), "nat64_match_mark", True)

    def _cmp_nat64_pools(self, want, have, ctx):
        want_pools = want.get("translation", {}).get("pool", {})
        have_pools = have.get("translation", {}).get("pool", {})

        if isinstance(want_pools, list):
            want_pools = {p["id"]: p for p in want_pools}
        if isinstance(have_pools, list):
            have_pools = {p["id"]: p for p in have_pools}

        for pid in set(want_pools) | set(have_pools):
            wp = want_pools.get(pid, {})
            hp = have_pools.get(pid, {})

            if wp == hp:
                continue

            changed = {k: v for k, v in wp.items() if k != "id" and hp.get(k) != v}
            removed = {
                k: v
                for k, v in hp.items()
                if k != "id" and k not in wp and self.state in ("replaced", "overridden")
            }

            if changed:
                self.addcmd(
                    dict(ctx, pool_id=pid, pool=changed),
                    "nat64_translation_pool",
                    False,
                )
            if removed:
                self.addcmd(
                    dict(ctx, pool_id=pid, pool=removed),
                    "nat64_translation_pool",
                    True,
                )
