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
        """Populate the facts for Ntp network resource

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
            config_lines.append(re.sub("'", "", resource))

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

        # self._module.fail_json(msg=ansible_facts)
        return ansible_facts

    def _merge_rule_list(self, rules):
        merged = {}

        for item in rules:
            rid = item["id"]

            if rid not in merged:
                merged[rid] = {"id": rid}

            for k, v in item.items():
                if k == "id":
                    continue

                if isinstance(v, dict):
                    merged[rid].setdefault(k, {})
                    merged[rid][k].update(v)
                else:
                    merged[rid][k] = v

        return list(merged.values())

    def _normalise(self, objs):
        for nat_type in ["nat", "nat64", "nat66"]:
            nat = objs.get(nat_type)

            if not nat:
                continue

            for section in ["destination", "source", "static", "cgnat"]:
                if section in nat and "rule" in nat[section]:
                    nat[section]["rule"] = self._merge_rule_list(
                        nat[section]["rule"],
                    )
        return objs
