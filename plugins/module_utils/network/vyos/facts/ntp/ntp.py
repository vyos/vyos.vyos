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


from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.ntp import (
    NtpTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.ntp.ntp import (
    NtpArgs,
)

class NtpFacts(object):
    """ The vyos ntp facts class"""

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = NtpArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)


    def get_config(self, connection):
        return connection.get("show configuration commands | grep ntp")


    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Ntp network resource

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
           

        # parse native config using the Ntp template
        ntp_parser = NtpTemplate(lines=data.splitlines())       

        objs = ntp_parser.parse()

        if objs:
            if "allow_clients" in objs:
                objs["allow_clients"] = sorted(list(objs["allow_clients"]))
            
            if "listen_addresses" in objs:
                objs["listen_addresses"] = sorted(list(objs["listen_addresses"]))
            
            """ if "options" in objs["servers"].values():
                val = objs["servers"].values() 
                val["options"] = sorted(val["options"]) """

            if "servers" in objs:
                objs["servers"] = list(objs["servers"].values())
                objs["servers"] = sorted(
                    objs["servers"], key=lambda k: k["name"]
                )
                for i in objs["servers"]:
                    if "options" in i:
                        i["options"] = sorted(list(i["options"]))
                       
                            
        ansible_facts['ansible_network_resources'].pop('ntp', None)

        params = utils.remove_empties(
            ntp_parser.validate_config(self.argument_spec, {"config": objs})
        )

        if params.get("config"):
            facts["ntp"] = params["config"]
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
