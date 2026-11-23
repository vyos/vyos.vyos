# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos nhrp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.nhrp.nhrp import (
    NhrpArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.nhrp import (
    NhrpTemplate,
)


class NhrpFacts(object):
    """The vyos nhrp facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = NhrpArgs.argument_spec

    def get_device_data(self, connection):
        return connection.get("show configuration commands | grep 'protocols nhrp'")

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Nhrp network resource
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = self.get_device_data(connection)

        lines = [line.replace("'", "") for line in data.splitlines()]
        objs = NhrpTemplate(lines=lines, module=self._module).parse()

        tunnels = []
        for tunnel in (objs.get("tunnels") or {}).values():
            if "multicast" in tunnel:
                tunnel["multicast"] = sorted(tunnel["multicast"].values())
            if "map" in tunnel:
                tunnel["map"] = sorted(tunnel["map"].values(), key=lambda m: m["tunnel_ip"])
            if "nhs" in tunnel:
                for nhs in tunnel["nhs"].values():
                    nbma = sorted(v for v in (nhs.get("nbma") or {}).values() if v)
                    if nbma:
                        nhs["nbma"] = nbma
                    else:
                        nhs.pop("nbma", None)
                tunnel["nhs"] = sorted(tunnel["nhs"].values(), key=lambda n: n["tunnel_ip"])
            tunnels.append(tunnel)

        facts = {"nhrp": {}}
        if tunnels:
            params = utils.validate_config(
                self.argument_spec,
                {"config": {"tunnels": sorted(tunnels, key=lambda t: t["name"])}},
            )
            facts["nhrp"] = utils.remove_empties(params["config"])

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts
