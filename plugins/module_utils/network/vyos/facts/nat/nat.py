# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos ntp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

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
        """Populate the facts for NAT network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []
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
                    merged[name][k] = self._merge_range_list(existing)
                elif isinstance(v, list):  # ← elif not if
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

    def _normalise(self, objs):
        for nat_type in ["nat", "nat64", "nat66"]:
            nat = objs.get(nat_type)
            if not nat:
                continue

            for section in ["destination", "source", "static", "cgnat"]:
                if section in nat and "rule" in nat[section]:
                    nat[section]["rule"] = self._merge_rule_list(nat[section]["rule"])
                    nat[section]["rule"].sort(key=lambda x: x.get("id", 0))

            if "cgnat" in nat and "pool" in nat["cgnat"]:
                pool = nat["cgnat"]["pool"]
                for ptype in ["external", "internal"]:
                    if ptype in pool:
                        pool[ptype] = self._merge_pool_list(pool[ptype])

            if nat_type == "nat64":
                for rule in nat.get("source", {}).get("rule", []):
                    pools = rule.get("translation", {}).get("pool")
                    if pools:
                        rule["translation"]["pool"] = self._merge_rule_list(pools)
                        rule["translation"]["pool"].sort(key=lambda x: x.get("id", 0))

        return objs

    def _merge_range_list(self, ranges):
        """Merge range entries by value, preserving seq."""
        merged = {}
        for entry in ranges:
            if isinstance(entry, dict):
                key = entry["value"]
                if key not in merged:
                    merged[key] = {"value": key}
                if entry.get("seq"):
                    merged[key]["seq"] = entry["seq"]
            else:
                # fallback for plain strings during transition
                merged[entry] = entry
        return list(merged.values())
