#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The vyos interfaces fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.interfaces.interfaces import (
    InterfacesArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.interfaces import (
    InterfacesTemplate,
)


class InterfacesFacts(object):
    """The vyos interfaces fact class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = InterfacesArgs.argument_spec

    def get_device_data(self, connection):
        data = connection.get_config(flags=["| grep interfaces"])
        return data

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for interfaces
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = self.get_device_data(connection)

        parser = InterfacesTemplate(lines=data.splitlines(), module=self._module)
        objs = list(parser.parse().values())
        for obj in objs:
            # disable is the only state on the device; enabled is the default
            obj.setdefault("enabled", True)
            if "vifs" in obj:
                for vif in obj["vifs"].values():
                    vif.setdefault("enabled", True)
                obj["vifs"] = sorted(obj["vifs"].values(), key=lambda vif: int(vif["vlan_id"]))

        facts = {}
        if objs:
            facts["interfaces"] = []
            params = utils.validate_config(self.argument_spec, {"config": objs})
            for cfg in params["config"]:
                facts["interfaces"].append(utils.remove_empties(cfg))

        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts
