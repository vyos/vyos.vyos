# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos vrf fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vrf.vrf import VrfArgs
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vrf import (
    VrfTemplate,
)


class VrfFacts(object):
    """The vyos vrf facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = VrfArgs.argument_spec

    def get_config(self, connection):
        return connection.get("show configuration commands |  match 'set vrf'")

    def get_config_set(self, data, connection):
        """To classify the configurations beased on vrf"""
        config_dict = {}
        for config_line in data.splitlines():
            vrf_inst = re.search(r"set vrf name (\S+).*", config_line)
            vrf_bta = re.search(r"set vrf bind-to-all", config_line)
            if vrf_bta:
                config_dict["bind_to_all"] = config_dict.get("bind_to_all", "") + config_line + "\n"
            if vrf_inst:
                config_dict[vrf_inst.group(1)] = (
                    config_dict.get(vrf_inst.group(1), "") + config_line + "\n"
                )
        return list(config_dict.values())

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Vrf network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = self.get_config(connection)

        vrf_facts = {}
        instances = []
        vrf_parser = VrfTemplate(lines=[], module=self._module)
        resources = self.get_config_set(data, connection)

        for resource in resources:
            vrf_parser = VrfTemplate(
                lines=resource.split("\n"),
                module=self._module,
            )
            objs = vrf_parser.parse()
            if objs:
                if "bind_to_all" in objs:
                    vrf_facts.update(objs)
                if "name" in objs:
                    # for key, afiv in [("address_family", "afi")]:
                    #     if key in objs and objs[key]:
                    #         # self._module.fail_json(msg=str(objs[key]))
                    #         objs[key] = list(objs[key].values())
                    instances.append(self._normalise_instance(objs))

        if instances:
            vrf_facts.update({"instances": instances})

        ansible_facts["ansible_network_resources"].pop("vrf_facts", None)
        facts = {"vrf": []}

        params = utils.remove_empties(
            vrf_parser.validate_config(
                self.argument_spec,
                {"config": vrf_facts},
                redact=True,
            ),
        )

        if not resources:
            params["config"].pop("bind_to_all", None)

        if params.get("config"):
            facts["vrf"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)
        # self._module.fail_json(msg=ansible_facts)
        return ansible_facts

    def _normalise_instance(self, instance):
        n_inst = instance.copy()
        af_map = {}

        for af in instance.get("address_family", []):
            afi = af.get("afi")
            if not afi:
                continue

            if afi not in af_map:
                af_map[afi] = {"afi": afi}

            for k, v in af.items():
                if k == "afi":
                    continue
                elif k == "route_maps":
                    if "route_maps" not in af_map[afi]:
                        af_map[afi]["route_maps"] = []
                    af_map[afi]["route_maps"].extend(v)
                else:
                    af_map[afi][k] = v

        for afi_data in af_map.values():
            if "route_maps" in afi_data:
                seen = []
                deduped = []
                for item in afi_data["route_maps"]:
                    if item not in seen:
                        seen.append(item)
                        deduped.append(item)
                afi_data["route_maps"] = deduped

        n_inst["address_family"] = list(af_map.values())
        return n_inst
