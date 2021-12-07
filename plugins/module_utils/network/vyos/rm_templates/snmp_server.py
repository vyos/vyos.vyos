# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Snmp_server parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)

class Snmp_serverTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Snmp_serverTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "communities",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\scommunity
                \s+(?<name>\S+)
                \s*(?P<auth>authorization\s\S+)*
                \s*(?P<client>client\s\S+)*
                \s*(?P<network>network\s\S+)*
                $""", re.VERBOSE),
            "setval": _tmplt_snmp_server_communities,
            "result": {
                "communities": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "authorization_type": "{{ auth.split(" ")[1] if auth is defined else None }}",
                        "client": "{{ client.split(" ")[1] if client is defined else None }}",
                        "network": "{{ network.split(" ")[1] if client is defined else None }}",
                    }
                }
            }
        },
        {
            "name": "contact",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\scontact
                \s+(?P<name>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'service snmp contact {{ contact }}',
            "compval": "contact",
            "result": {
                "contact": "{{ name }}",
            },
        },
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sdescription
                \s+(?P<name>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'service snmp description {{ description }}',
            "result": {
                "description": "{{ name }}",
            },
        },
        {
            "name": "listen_address",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\slisten-address
                \s+(?<ip>\S+)
                \s+port
                \s+(?P<port>\d+)*
                $""", re.VERBOSE),
            "setval": 'service snmp listen-address {{ listen_address.address }} port {{ listen_address.port }}',
            "result": {
                "listen_address": {
                    "address": "{{ ip }}",
                    "port": "{{ port }}"
                }
            }
        },
        {
            "name": "location",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\slocation
                \s+(?P<name>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'service snmp location {{ location }}',
            "result": {
                "location": "{{ name }}",
            },
        },
        {
            "name": "smux_peer",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\ssmux-peer
                \s+(?P<name>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'service snmp smux-peer {{ smux_peer }}',
            "result": {
                "smux_peer": "{{ name }}",
            },
        },
        {
            "name": "trap_source",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\strap-source
                \s+(?P<name>.+)
                *$""",
                re.VERBOSE,
            ),
            "setval": 'service snmp trap-source {{ trap_source }}',
            "result": {
                "trap_source": "{{ name }}",
            },
        },
        {
            "name": "trap_target",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\strap-target
                \s+(?P<address>\S+)
                \s*(?P<comm>community\s\S+)*
                \s*(?P<port>port\s\d+)*
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_snmp_server_trap_target,
            "result": {
                "trap_target": {
                    "address": "{{ address }}",
                    "port": "{{ port.split(" ")[1] if port is defined else None }}",
                    "community": "{{ comm.split(" ")[1] if comm is defined else None }}"
            },
        },

        {
            "name": "key_a",
            "getval": re.compile(
                r"""
                ^key_a\s(?P<key_a>\S+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
            },
            "shared": True
        },
        {
            "name": "key_b",
            "getval": re.compile(
                r"""
                \s+key_b\s(?P<key_b>\S+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
            },
        },
    ]
    # fmt: on
