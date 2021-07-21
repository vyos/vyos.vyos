# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Ntp parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)

class NtpTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        prefix = {"set": "set", "remove": "delete"}
        super(NtpTemplate, self).__init__(
                lines=lines, tmplt=self, prefix=prefix
                )     

    # fmt: off  
    PARSERS = [

        #set system ntp allow_clients address <address>        
        {
            "name": "allow_clients",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sallow-clients\saddress (\s(?P<ipaddress>\S+))?
                $""",
                re.VERBOSE),
            "setval": "system ntp allow-clients address {{allow_clients}}",
            #"compval": "address",
            "result": {  
                       
                 "allow_clients": ["{{ipaddress}}"]
                     
                
            }
            
        },

        #set system ntp allow_clients          
        {
            "name": "allow_clients_delete",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sallow-clients
                $""",
                re.VERBOSE),
            "setval": "system ntp allow-clients",
            #"compval": "address",
            "result": {                       
                
            }
            
        },

        #set system ntp listen_address <address>
        {
            "name": "listen_addresses",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\slisten-address (\s(?P<ip_address>\S+))? 
                $""",
                re.VERBOSE),
            "setval": "system ntp listen-address {{listen_addresses}}",
            #"compval": "address",
            "result": {            
                 "listen_addresses": ["{{ip_address}}"]
            
            }
        },

         #set system ntp listen_address 
        {
            "name": "listen_addresses_delete",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\slisten-address
                $""",
                re.VERBOSE),
            "setval": "system ntp listen-address",
            #"compval": "address",
            "result": {                        
            }
        },

        #set system ntp server <name>
        {
            "name": "name",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sserver (\s(?P<name>\S+))? 
                $""",
                re.VERBOSE),
            "setval": "system ntp server {{name}}",
            #"compval": "name",
            "result": {
                "servers": {
                    "{{name}}": {                    
                        "name": "{{name}}"
                    }
                }
            
            }
        },

        #set system ntp server <name> <options>
        {
            "name": "options",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sserver (\s(?P<name>\S+))? (\s(?P<options>noselect|pool|preempt|prefer))?            
                $""",
                re.VERBOSE),
            "setval": "system ntp server {{name}} {{options}}",
            #"compval": "options",
            "result": {
                "servers": {
                    "{{name}}": {
                        "name": "{{name}}",
                        "options":["{{options}}"]                 
                    }  
                }
            }
        }
    ]
    # fmt: on
