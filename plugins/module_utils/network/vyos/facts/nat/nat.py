# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.nat.nat import (
    NatArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.nat import (
    NatTemplate,
)


class NatFacts(object):
    """The vyos nat facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = NatArgs.argument_spec

    def get_config(self, connection):
        return connection.get("show configuration commands | match 'nat'")

    def populate_facts(self, connection, ansible_facts, data=None):
        facts = {}
        config_lines = []

        if not data:
            data = self.get_config(connection)

        for resource in data.splitlines():
            config_lines.append(re.sub(r"'([^']*)'", r"\1", resource))

        nat_parser = NatTemplate(lines=config_lines, module=self._module)
        objs = nat_parser.parse()
        objs = self._normalise(objs)

        ansible_facts["ansible_network_resources"].pop("nat", None)

        params = utils.remove_empties(
            nat_parser.validate_config(self.argument_spec, {"config": objs}, redact=True),
        )

        if params.get("config"):
            facts["nat"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts

    def _deep_merge(self, base, override):
        for k, v in override.items():
            if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                self._deep_merge(base[k], v)
            elif k in base and isinstance(base[k], list) and isinstance(v, list):
                for entry in v:
                    if entry not in base[k]:
                        base[k].append(entry)
            else:
                base[k] = v
        return base

    def _merge_rule_list(self, rules):
        merged = {}
        for item in rules:
            rid = item["id"]
            if rid not in merged:
                merged[rid] = {"id": rid}
            for k, v in item.items():
                if k == "id":
                    continue
                if isinstance(v, list):
                    existing = merged[rid].setdefault(k, [])
                    for entry in v:
                        if entry not in existing:
                            existing.append(entry)
                elif isinstance(v, dict):
                    merged[rid].setdefault(k, {})
                    self._deep_merge(merged[rid][k], v)
                else:
                    merged[rid][k] = v
        return list(merged.values())

    def _merge_pool_list(self, pools):
        merged = {}
        for item in pools:
            name = item["name"]
            if name not in merged:
                merged[name] = {"name": name}
            for k, v in item.items():
                if k == "name":
                    continue
                if k == "range" and isinstance(v, list):
                    existing = merged[name].setdefault(k, [])
                    existing.extend(v)
                    if v and isinstance(v[0], dict):
                        merged[name][k] = self._merge_range_list(existing)
                    else:
                        merged[name][k] = list(dict.fromkeys(existing))
                elif isinstance(v, list):
                    merged[name].setdefault(k, [])
                    for val in v:
                        if val not in merged[name][k]:
                            merged[name][k].append(val)
                elif isinstance(v, dict):
                    merged[name].setdefault(k, {})
                    self._deep_merge(merged[name][k], v)
                else:
                    merged[name][k] = v
        return list(merged.values())

    def _merge_range_list(self, ranges):
        """Merge external pool range entries by value, preserving seq."""
        merged = {}
        for entry in ranges:
            if isinstance(entry, dict):
                key = entry.get("value") or entry.get("address", "")
                if not key:
                    continue
                if key not in merged:
                    merged[key] = {"value": key}
                if entry.get("seq"):
                    merged[key]["seq"] = entry["seq"]
            else:
                if entry not in merged:
                    merged[entry] = {"value": entry}
        return list(merged.values())

    def _normalise(self, objs):
        for nat_type in ["nat", "nat64", "nat66"]:
            nat = objs.get(nat_type)
            if not nat:
                continue

            for section in ["destination", "source", "static", "cgnat"]:
                if section not in nat:
                    continue
                rules = nat[section].get("rule")
                if isinstance(rules, list):
                    nat[section]["rule"] = self._merge_rule_list(rules)
                    nat[section]["rule"].sort(key=lambda x: x.get("id", 0))

            if "cgnat" in nat and "pool" in nat["cgnat"]:
                pool = nat["cgnat"]["pool"]
                for ptype in ["external", "internal"]:
                    if ptype in pool and isinstance(pool[ptype], list):
                        pool[ptype] = self._merge_pool_list(pool[ptype])

            if nat_type == "nat64":
                for rule in nat.get("source", {}).get("rule", []):
                    pools = rule.get("translation", {}).get("pool")
                    if pools and isinstance(pools, list):
                        rule["translation"]["pool"] = self._merge_rule_list(pools)
                        rule["translation"]["pool"].sort(key=lambda x: x.get("id", 0))

        self._cast_ports(objs)
        return objs

    def _cast_ports(self, obj):
        """Recursively cast known integer port/seq fields to str."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("port", "seq") and isinstance(v, int):
                    obj[k] = str(v)
                else:
                    self._cast_ports(v)
        elif isinstance(obj, list):
            for item in obj:
                self._cast_ports(item)
