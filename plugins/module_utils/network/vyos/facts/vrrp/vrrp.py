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
            vrrp_snmp = re.search(r"set high-availability vrrp snmp", config_line)
            vrrp_gp = re.search(
                r"set high-availability vrrp global-parameters (\S+).*",
                config_line,
            )
            vrrp_sg = re.search(r"set high-availability vrrp sync-group (\S+).*", config_line)
            vrrp_vsrv = re.search(r"set high-availability virtual-server (\S+).*", config_line)
            vrrp_disable = re.search(r"set high-availability disable", config_line)
            if vrrp_disable:
                config_dict["disable"] = config_dict.get("disable", "") + config_line + "\n"
            if vrrp_gp:
                config_dict["global_parameters"] = (
                    config_dict.get(vrrp_gp.group(1), "") + config_line + "\n"
                )
            if vrrp_vsrv:
                config_dict[vrrp_vsrv.group(1)] = (
                    config_dict.get(vrrp_vsrv.group(1), "") + config_line + "\n"
                )
            if vrrp_sg:
                config_dict[vrrp_sg.group(1)] = (
                    config_dict.get(vrrp_sg.group(1), "") + config_line + "\n"
                )
            if vrrp_grp:
                config_dict[vrrp_grp.group(1)] = (
                    config_dict.get(vrrp_grp.group(1), "") + config_line + "\n"
                )
        return list(config_dict.values())

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
        vrrp_facts = {}
        groups = []
        sync_groups = []
        vsvrs = []
        resources = self.get_config_set(data, connection)
        # self._module.fail_json(msg=resources)
        for resource in data.splitlines():  # resources:
            vrrp_parser = VrrpTemplate(
                lines=resource.split("\n"),
                module=self._module,
            )
            objs = vrrp_parser.parse()
            if "virtual_servers" in objs:
                objs["virtual_servers"] = sorted(
                    list(objs["virtual_servers"].values()),
                    key=lambda k, sk="alias": k[sk],
                )
        self._module.fail_json(msg=str(objs))
        ansible_facts["ansible_network_resources"].pop("vrrp", None)

        params = utils.remove_empties(
            vrrp_parser.validate_config(self.argument_spec, {"config": objs}, redact=True),
        )

        facts["vrrp"] = params.get("config", [])
        ansible_facts["ansible_network_resources"].update(facts)
        self._module.fail_json(msg=ansible_facts)

        return ansible_facts
