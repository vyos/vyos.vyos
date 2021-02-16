# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The vyos bgp_global fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.bgp_global import (
    Bgp_globalTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.bgp_global.bgp_global import (
    Bgp_globalArgs,
)
import q

class Bgp_globalFacts(object):
    """ The vyos bgp_global facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Bgp_globalArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_device_data(self, connection):
        return connection.get(
            'show configuration commands |  match "set protocols bgp"'
        )

    def get_config_set(self, data):
        """ To classify the configurations beased on interface """
        interface_list = []
        config_set = []
        int_string = ""
        for config_line in data.splitlines():
            ospf_int = re.search(r"set interfaces \S+ (\S+) .*", config_line)
            if ospf_int:
                if ospf_int.group(1) not in interface_list:
                    if int_string:
                        config_set.append(int_string)
                    interface_list.append(ospf_int.group(1))
                    int_string = ""
                int_string = int_string + config_line + "\n"
        if int_string:
            config_set.append(int_string)
        return config_set

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Bgp_global network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = self.get_device_data(connection)
    
        q(data)

        # parse native config using the Ospf_interfaces template
        bgp_global_facts = []
        for resource in data.splitlines():
            q(resource)
            bgp_global_parser = Bgp_globalTemplate(
                lines=resource.split("\n")
            )
            objs = bgp_global_parser.parse()
            q(objs)
            for key, sortv in [("neighbor", "address")]:
                if key in objs and objs[key]:
                    objs[key] = list(objs[key].values())
            #bgp_global_facts.append(objs)

        ansible_facts["ansible_network_resources"].pop("bgp_global", None)

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )

        facts["bgp_global"] = params.get("config", [])
        ansible_facts["ansible_network_resources"].update(facts)


        return ansible_facts
