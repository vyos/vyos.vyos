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
        {
            "name": "allow_clients_address",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sallow-clients\saddress   (\s(?P<address>\S+))?
                $""",
                re.VERBOSE),
            "setval": "ntp allow_clients address {{address}}",
            "compval": "address",
            "result": {         
                 "allow_clients": {
                "{{address}}": {
                    "address": "{{address}}"
                }
            }
            }
            
        },
        {
            "name": "listen_address_address",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\slisten-address (\s(?P<address>\S+))? 
                $""",
                re.VERBOSE),
            "setval": "ntp listen_address {{address}}",
            "compval": "address",
            "result": {            
                 "listen_address": {
                    "{{address}}": {
                        "address": "{{address}}"
                    }
                }
            }
        },
        {
            "name": "server_name",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sserver (\s(?P<name>\S+))? 
                $""",
                re.VERBOSE),
            "setval": "ntp server {{name}}",
            "compval": "name",
            "result": {
                "server": {
                    "{{name}}": {                    
                        "name": "{{name}}"
                    }
                }
            }
        },
        {
            "name": "server_options",
            "getval": re.compile(
                r"""
                ^set\ssystem\sntp\sserver (\s(?P<name>\S+))?  (\s(?P<options>noselect|pool|preempt|prefer))? 
                $""",
                re.VERBOSE),
            "setval": "ntp server {{name}} {{options}}",
            "compval": "options",
            "result": {
                "server": {
                    "{{name}}": {
                        "name": "{{name}}",
                        "options": "{{options}}"
                    }
                }
            }
        }
    ]
    # fmt: on
