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
        resources = self.get_config_set(data, connection)
        # self._module.fail_json(msg=resources)
        for resource in resources:
            vrf_parser = VrfTemplate(
                lines=resource.split("\n"),
                module=self._module,
            )
            objs = vrf_parser.parse()
            if "name" in objs and objs["name"]:
                instances.append(objs)
            # for key, sortv in [("address_family", "afi")]:
            #     if key in objs and objs[key]:
            #         objs[key] = list(objs[key].values())
        vrf_facts["instances"] = instances
        # for resource in data.splitlines():
        #     config_lines.append(re.sub("'", "", resource))
        # # parse native config using the Vrf template
        # vrf_parser = VrfTemplate(lines=config_lines, module=self._module)

        # objs = vrf_parser.parse()
        # self._module.fail_json(msg=objs)

        # if objs:
        #     if "allow_clients" in objs:
        #         objs["allow_clients"] = sorted(list(objs["allow_clients"]))

        #     if "listen_addresses" in objs:
        #         objs["listen_addresses"] = sorted(list(objs["listen_addresses"]))

        #     """ if "options" in objs["servers"].values():
        #         val = objs["servers"].values()
        #         val["options"] = sorted(val["options"]) """

        #     if "servers" in objs:
        #         objs["servers"] = list(objs["servers"].values())
        #         objs["servers"] = sorted(objs["servers"], key=lambda k: k["server"])
        #         for i in objs["servers"]:
        #             if "options" in i:
        #                 i["options"] = sorted(list(i["options"]))

        # self._module.fail_json(msg=vrf_facts)
        ansible_facts["ansible_network_resources"].pop("vrf", None)

        params = utils.remove_empties(
            vrf_parser.validate_config(self.argument_spec, {"config": vrf_facts}, redact=True),
        )

        # self._module.fail_json(msg=params)

        if params.get("config"):
            facts["vrf"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        # self._module.fail_json(msg=ansible_facts)

        return ansible_facts
