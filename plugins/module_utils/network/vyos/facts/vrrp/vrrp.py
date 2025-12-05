# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos vrrp fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vrrp.vrrp import (
    VrrpArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vrrp import (
    VrrpTemplate,
)


class VrrpFacts(object):
    """The vyos vrrp facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = VrrpArgs.argument_spec

    def get_device_data(self, connection):
        return connection.get('show configuration commands |  match "set high-availability"')

    def get_config_set(self, data, connection):
        """To classify the configurations beased on vrrp"""
        config_dict = {}
        for config_line in data.splitlines():
            vrrp_grp = re.search(r"set high-availability vrrp group (\S+).*", config_line)
            vrrp_gp = re.search(
                r"set high-availability vrrp global-parameters (\S+).*",
                config_line,
            )
            vrrp_sg = re.search(r"set high-availability vrrp sync-group (\S+).*", config_line)
            vrrp_vsrv = re.search(r"set high-availability virtual-server (\S+).*", config_line)
            vrrp_disable = re.search(r"set high-availability disable", config_line)
            vrrp_snmp = re.search(r"set high-availability vrrp snmp", config_line)

            if vrrp_disable:
                config_dict["disable"] = config_dict.get("disable", "") + config_line + "\n"
            if vrrp_snmp:
                config_dict.setdefault("vrrp", []).append(config_line)
            if vrrp_gp:
                config_dict.setdefault("global_parameters", []).append(config_line)
            if vrrp_vsrv:
                config_dict.setdefault(vrrp_vsrv.group(1), []).append(config_line)
            if vrrp_sg:
                config_dict.setdefault(vrrp_sg.group(1), []).append(config_line)
            if vrrp_grp:
                config_dict.setdefault(vrrp_grp.group(1), []).append(config_line)
        return list(config_dict.values())

    def deep_merge(self, dest, src):
        for key, value in src.items():
            if key in dest and isinstance(dest[key], dict) and isinstance(value, dict):
                self.deep_merge(dest[key], value)
            else:
                dest[key] = value
        return dest

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for vrrp network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = {}
        config_lines = []

        if not data:
            data = self.get_device_data(connection)
        # self._module.fail_json(msg="Data: " + str(data))
        resources = self.get_config_set(data, connection)
        # self._module.fail_json(msg="Resources: " + str(resources))
        vrrp_facts = {"disable": False, "virtual_servers": {}, "vrrp": {}}
        for resource in resources:
            vrrp_parser = VrrpTemplate(
                lines=resource,
                module=self._module,
            )
            objs = vrrp_parser.parse()
            # self._module.fail_json(msg="VRRP Objs: " + str(objs))
            if "disable" in objs:
                vrrp_facts["disable"] = objs["disable"]

            for section in ("virtual_servers", "vrrp"):
                if section in objs:
                    # self._module.fail_json(msg="Section: " + str(section) + " Objs[section]: " + str(objs[section]))
                    for name, data in objs[section].items():
                        if not isinstance(data, dict):
                            vrrp_facts[section][name] = data
                            continue
                        existing = vrrp_facts[section].get(name, {})
                        vrrp_facts[section][name] = self.deep_merge(existing, data)

        ansible_facts["ansible_network_resources"].pop("vrrp", None)
        #
        vrrp_facts = self.normalize_config(vrrp_facts)
        #
        # self._module.fail_json(msg="VRRP_Facts: " + str(vrrp_facts))
        validate_parser = VrrpTemplate(lines=[], module=self._module)
        params = utils.remove_empties(
            validate_parser.validate_config(
                self.argument_spec,
                {"config": vrrp_facts},
                redact=True,
            ),
        )
        # self._module.fail_json(msg="Params: " + str(params))
        facts["vrrp"] = params.get("config", [])
        ansible_facts["ansible_network_resources"].update(facts)
        # self._module.fail_json(msg='Facts - ' + str(ansible_facts))
        return ansible_facts

    def normalize_config(self, config):
        if not config:
            return config

        # Normalize virtual_servers
        if isinstance(config.get("virtual_servers"), dict):
            config["virtual_servers"] = list(config["virtual_servers"].values())

        # Normalize vrrp
        vrrp = config.get("vrrp", {})
        # self._module.fail_json(msg=config.get("vrrp", {}))

        if isinstance(vrrp.get("groups"), dict):
            vrrp["groups"] = list(vrrp["groups"].values())
            # self._module.fail_json(msg="Groups: " + str(vrrp["groups"]))

        if isinstance(vrrp.get("sync_groups"), dict):
            vrrp["sync_groups"] = list(vrrp["sync_groups"].values())
            self._module.fail_json(msg="SGroups: " + str(vrrp["sync_groups"]))

        # Normalize real_server inside each virtual_server
        for vs in config.get("virtual_servers", []):
            if isinstance(vs.get("real_server"), dict):
                vs["real_server"] = list(vs["real_server"].values())

        return config
