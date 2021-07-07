#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The vyos_ntp config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""


from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import (
    Facts,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.ntp import (
    NtpTemplate,
)


class Ntp(ResourceModule):
    """
    The vyos_ntp config class
    """

    def __init__(self, module):
        super(Ntp, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="ntp",
            tmplt=NtpTemplate(),
        )
        self.parsers = [
            "allow_clients",
            "listen_addresses",
            "name",
            "options"
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """

        wantd = self._ntp_list_to_dict(self.want)
        haved = self._ntp_list_to_dict(self.have)
        

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    if k == "servers":
                        prsrname = "name"
                    else:
                        prsrname = k
                    # self._compare(want={}, have=have)
                    self.commands.append (
                        self._tmplt.render({prsrname:have},prsrname,True)
                   )

     
        for k, want in iteritems(wantd):
            if "name" in want:
                self.compare(parsers = self.parsers, want=want, have=haved.pop(k, {}))
                #self._compare(want=want, have=haved.pop(k, {}))
            else:
                want = {k:want}
                x= haved.pop(k,{})
                have = {k:x}
                self.compare(parsers = self.parsers, want = want, have = have)


    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Ntp network resource.
        """

        """ w_servers = want.get("servers", {})
        h_servers = have.get("servers", {}) """

        #q(want)
        #q(have)
        """q(want["servers"])
        q(have["servers"]) """
        """ if "name" in want:
            w_servers = want
            h_servers = have

            #q(w_servers)
            #q(h_servers)
            self._compare_servers(want=w_servers, have=h_servers) """

    
    """ def _compare_servers(self,want,have):
        for wk, wserver in iteritems(want):
            hserver = have.pop(wk, {})
            #q(wserver)
            #q(hserver)
            self.compare(parsers = self.parsers, want = wserver, have = hserver) """
    
    
    def _ntp_list_to_dict(self, entry):
        servers_dict = {}
        for k, data in iteritems(entry):
            if "servers" in k:
                for value in data:
                    servers_dict.update({value["name"]: value})
            else:
                servers_dict.update({k:data})
        return servers_dict
 
    
    
    
    """ def _ntp_list_to_dict(self, entry):
        q(entry)
        for k, data in iteritems(entry):
            # if "servers" in k:
                servers_dict = {}
                for value in data:
                    servers_dict.update({value["name"]: value})
                data = servers_dict                                    
                # entry["servers"] = servers_dict
                # self._ntp_list_to_dict()    
                
        q(entry) """