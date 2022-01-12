# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
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
        prefix = {"set": "set", "remove": "delete"}
        super(Snmp_serverTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        # set service snmp community <>
        {
            "name": "communities",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\scommunity
                \s+(?P<name>\S+)
                \s*(?P<auth>authorization\srw|authorization\sro)*
                \s*(?P<client>client\s\S+)*
                \s*(?P<network>network\s\S+)*
                $""",
                re.VERBOSE),
            "setval": _tmplt_snmp_server_communities,
            "result": {
                "communities": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "client": '{{ client.split(" ")[1] if client is defined else None }}',
                        "network": '{{ network.split(" ")[1] if network is defined else None }}',
                        "authorization_type": '{{ auth.split(" ")[1] if auth is defined else None }}'
                    }
                }
            }
        },
        # set service snmp contact <>
        {
            "name": "contact",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\scontact
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp contact {{ contact }}",
            "result": {
                "contact": "{{ name }}"
            }
        },
        # set service snmp description <>
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sdescription
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp description {{ description }}",
            "result": {
                "description": "{{ name }}"
            }
        },
        # set service snmp listen-address <> port <>
        {
            "name": "listen_address",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\slisten-address
                \s+(?P<addr>\S+)
                \s+port
                \s+(?P<port>\d+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp listen-address {{ listen_address.address }} port {{ listen_address.port }}",
            "result": {
                "listen_address": {
                    "address": "{{ addr }}",
                    "port": "{{ port }}"
                }
            }
        },
        # set service snmp location <>
        {
            "name": "location",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\slocation
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp location {{ location }}",
            "result": {
                "location": "{{ name }}"
            }
        },
        # set service snmp smux-peer <>
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\ssmux-peer
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp smux-peer {{ smux_peer }}",
            "result": {
                "smux_peer": "{{ name }}"
            }
        },
        # set service snmp trap-source <>
        {
            "name": "trap_source",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\strap-source
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp trap-source {{ trap_source }}",
            "result": {
                "trap_source": "{{ name }}"
            }
        },
        # set service snmp trap-target <>
        {
            "name": "trap_target",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\strap-target
                \s+(?P<name>\S+)
                \s*(?P<comm>community\s\S+)*
                \s*(?<port>port\s\d+)*
                $""",
                re.VERBOSE),
            "setval": _tmplt_snmp_server_trap_target,
            "result": {
                "trap_target": {
                    "address": "{{ name }}",
                    "community": "{{ comm.split(" ")[1] if comm is defined else None }}",
                    "port": "{{ port.split(" ")[1] if port is defined else None }}",
                }
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp v3 group <>
        {
            "name": "snmp_v3.groups",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sgroup
                \s+(?P<name>\S+)
                \s*(?P<mode>mode\s\S+)*
                \s*(?P<sec>seclevel\s\S+)*
                \s*(?P<view>view\s\S+)*
                $""",
                re.VERBOSE),
            "setval": _tmpltsnmp_server_v3_groups,
            "result": {
                "snmp_v3": {
                    "groups": {
                        "{{ name }}": {
                            "{{ group }}": "{{ name }}",
                            "{{ mode }}": '{{ mode.split(" ")[1] is mode is defined else None }}',
                            "{{ seclevel }}": '{{ seclevel.split(" ")[1] is seclevel is defined else None }}',
                            "{{ view }}": '{{ view.split(" ")[1] is view is defined else None }}',
                } 
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp v3 engineid <>
        {
            "name": "snmp_v3.engine_id",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sv3\sengineid
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp v3 engineid {{ snmp_v3.engine_id }}",
            "result": {
                "snmp_v3": {
                    "engine_id": "{{ name }}",
                } 
            }
        },
        # set service snmp description <>
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sdescription
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp description {{ description }}",
            "result": {
                "description": "{{ name }}"
            }
        },
        # set service snmp description <>
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set\sservice\ssnmp\sdescription
                \s+(?P<name>\S+)
                *$""",
                re.VERBOSE),
            "setval": "set service snmp description {{ description }}",
            "result": {
                "description": "{{ name }}"
            }
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
