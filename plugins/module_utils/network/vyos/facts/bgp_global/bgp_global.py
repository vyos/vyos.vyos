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
import re
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

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Bgp_global network resource

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
    
        for resource in data.splitlines():
            if "address-family" not in resource:
                config_lines.append(re.sub('\'', '', resource))

        bgp_global_parser = Bgp_globalTemplate(lines=config_lines)
        objs = bgp_global_parser.parse()
        for key, sortv in [("neighbor", "address")]:
            if key in objs and objs[key]:
                objs[key] = list(objs[key].values())

        ansible_facts["ansible_network_resources"].pop("bgp_global", None)

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )

        facts["bgp_global"] = params.get("config", [])
        ansible_facts["ansible_network_resources"].update(facts)


        return ansible_facts
