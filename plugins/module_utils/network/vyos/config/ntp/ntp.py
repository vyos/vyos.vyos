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
            "options",
            "allow_clients_delete",
            "listen_addresses_delete"
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

            commandlist = self._commandlist(haved)
            servernames = self._servernames(haved)

             #removing the servername and commandlist from the list after deleting it from haved
            for k, have in iteritems(haved):
                if k not in wantd:
                    for hk, hval in iteritems(have):                    
                        if hk == "allow_clients" and hk in commandlist:
                            self.commands.append(
                                self._tmplt.render({"": hk}, "allow_clients_delete", True)
                            )
                            commandlist.remove(hk)
                        elif hk == "listen_addresses" and hk in commandlist:
                            self.commands.append(
                                self._tmplt.render({"": hk}, "listen_addresses_delete", True)
                            )
                            commandlist.remove(hk)
                        elif hk == "name" and have["name"] in servernames:
                            self._compareoverride(want={}, have=have)
                            servernames.remove(have["name"])    

        # remove existing config for overridden,replaced and deleted
        #Getting the list of the server names from haved 
        #   to avoid the duplication of overridding/replacing the servers
        if self.state in ["overridden","replaced"]:

            commandlist = self._commandlist(haved)
            servernames = self._servernames(haved)


            for k, have in iteritems(haved):
                if k not in wantd and "name" not in have:
                    self._compareoverride(want={}, have=have)
                    #removing the servername from the list after deleting it from haved
                elif k not in wantd and have["name"] in servernames:
                    self._compareoverride(want={}, have=have)
                    servernames.remove(have["name"])

            """ for k in commandlist:
                if k not in wantd and k == "allow_clients":
                    self.commands.append(
                        self._tmplt.render({"": k}, "allow_clients_delete", True)
                    )
                elif k not in wantd and k == "listen_addresses":
                     self.commands.append(
                        self._tmplt.render({"": k}, "listen_addresses_delete", True)
                    ) """
             #removing the servername and commandlist from the list after deleting it from haved
            """ for k, have in iteritems(haved):
                if k not in wantd:
                    for hk, hval in iteritems(have):                    
                        if hk == "allow_clients" and hk in commandlist:
                            self.commands.append(
                                self._tmplt.render({"": hk}, "allow_clients_delete", True)
                            )
                            commandlist.remove(hk)
                        elif hk == "listen_addresses" and hk in commandlist:
                            self.commands.append(
                                self._tmplt.render({"": hk}, "listen_addresses_delete", True)
                            )
                            commandlist.remove(hk)
                        elif hk == "name" and have["name"] in servernames:
                            self._compareoverride(want={}, have=have)
                            servernames.remove(have["name"]) """
                   

        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))
        
        """   for k, want in iteritems(wantd):
                if k in haved:
                    for wk,wval in iteritems(want):
                        if wk == "allow_clients":
                            self.commands.append(
                                self._tmplt.render({"allow_clients":wval}, "allow_clients", False)
                            )
                        elif wk == "listen_addresses":
                            self.commands.append(
                                self._tmplt.render({"listen_addresses":wval}, "listen_addresses", False)
                            ) """

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Ntp network resource.
        """
        if "options" in want:
            self.compare(parsers="options", want=want, have=have)
        else:
            self.compare(parsers=self.parsers, want=want, have=have)  


    def _compareoverride(self, want, have):
        # do not delete configuration with options level 
        for i, val in iteritems(have):
            if i =="options":
                pass
            else:
                self.compare(parsers=i, want={}, have=have)

    
    def _ntp_list_to_dict(self, entry):
        servers_dict = {}
        for k, data in iteritems(entry):
            if k == "servers":
                for value in data:
                    if "options" in value:
                        result = self._serveroptions_list_to_dict(value)
                        for res, resvalue in iteritems(result):
                            servers_dict.update({res:resvalue})
                    else:    
                        servers_dict.update({value["name"]: value})
            else:
                for value in data:
                    servers_dict.update({"ip_"+value: {k:value}})
        return servers_dict
 
   
    def _serveroptions_list_to_dict(self, entry):
        serveroptions_dict = {}
        for Opk, Op in iteritems(entry):
            if Opk == "options":
                for val in Op:
                    dict = {}
                    dict.update({"name":entry["name"]})
                    dict.update({Opk:val})
                    serveroptions_dict.update({entry["name"]+"_"+val: dict })                    
        return serveroptions_dict


    def _commandlist(self, haved):
        commandlist = []
        for k,have in iteritems(haved):
            for ck,cval in iteritems(have):
                if ck !="options" and ck not in commandlist:
                    commandlist.append(ck)
        return commandlist
    
    def _servernames(self,haved):
        servernames = []
        for k,have in iteritems(haved):
            for sk,sval in iteritems(have):
                if sk == "name" and sval not in ["time1.vyos.net","time2.vyos.net","time3.vyos.net"]:
                    if sval not in servernames:
                        servernames.append(sval)
        return servernames
