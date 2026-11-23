# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Nhrp parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class NhrpTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(NhrpTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # Device lines reach the parser with their quotes removed (see the facts class).
    # The first matching parser wins for each line, so the tunnel catch-all comes last.
    # fmt: off
    PARSERS = [
        # set protocols nhrp tunnel <name> authentication <secret>
        {
            "name": "authentication",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+authentication
                \s+(?P<authentication>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} authentication '{{ authentication }}'",
            "remval": "protocols nhrp tunnel {{ name }} authentication",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "authentication": "{{ authentication }}"}}},
        },
        # set protocols nhrp tunnel <name> holdtime <seconds>
        {
            "name": "holdtime",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+holdtime
                \s+(?P<holdtime>\d+)
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} holdtime {{ holdtime }}",
            "remval": "protocols nhrp tunnel {{ name }} holdtime",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "holdtime": "{{ holdtime }}"}}},
        },
        # set protocols nhrp tunnel <name> mtu <bytes>
        {
            "name": "mtu",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+mtu
                \s+(?P<mtu>\d+)
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} mtu {{ mtu }}",
            "remval": "protocols nhrp tunnel {{ name }} mtu",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "mtu": "{{ mtu }}"}}},
        },
        # set protocols nhrp tunnel <name> network-id <id>
        {
            "name": "network_id",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+network-id
                \s+(?P<network_id>\d+)
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} network-id {{ network_id }}",
            "remval": "protocols nhrp tunnel {{ name }} network-id",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "network_id": "{{ network_id }}"}}},
        },
        # set protocols nhrp tunnel <name> redirect
        {
            "name": "redirect",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+redirect
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} redirect",
            "remval": "protocols nhrp tunnel {{ name }} redirect",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "redirect": True}}},
        },
        # set protocols nhrp tunnel <name> shortcut
        {
            "name": "shortcut",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+shortcut
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} shortcut",
            "remval": "protocols nhrp tunnel {{ name }} shortcut",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "shortcut": True}}},
        },
        # set protocols nhrp tunnel <name> registration-no-unique
        {
            "name": "registration_no_unique",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+registration-no-unique
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} registration-no-unique",
            "remval": "protocols nhrp tunnel {{ name }} registration-no-unique",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "registration_no_unique": True}}},
        },
        # set protocols nhrp tunnel <name> multicast <address|dynamic>  (one line per value)
        {
            "name": "multicast",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+multicast
                \s+(?P<multicast>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} multicast {{ multicast }}",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}", "multicast": {"{{ multicast }}": "{{ multicast }}"}}}},
        },
        # set protocols nhrp tunnel <name> map tunnel-ip <address> [nbma <address|local>]
        {
            "name": "map",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+map
                \s+tunnel-ip
                \s+(?P<tunnel_ip>\S+)
                (?:\s+nbma\s+(?P<nbma>\S+))?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} map tunnel-ip {{ map.tunnel_ip }}"
                      "{{ ' nbma ' + map.nbma if map.nbma is defined and map.nbma else '' }}",
            "remval": "protocols nhrp tunnel {{ name }} map tunnel-ip {{ map.tunnel_ip }}",
            "result": {
                "tunnels": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "map": {"{{ tunnel_ip }}": {"tunnel_ip": "{{ tunnel_ip }}", "nbma": "{{ nbma }}"}},
                    },
                },
            },
        },
        # set protocols nhrp tunnel <name> nhs tunnel-ip <address|dynamic> [nbma <address>]
        # (one line per NBMA address)
        {
            "name": "nhs",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                \s+nhs
                \s+tunnel-ip
                \s+(?P<tunnel_ip>\S+)
                (?:\s+nbma\s+(?P<nbma>\S+))?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }} nhs tunnel-ip {{ nhs.tunnel_ip }}"
                      "{{ ' nbma ' + nhs.nbma if nhs.nbma is defined and nhs.nbma else '' }}",
            "remval": "protocols nhrp tunnel {{ name }} nhs tunnel-ip {{ nhs.tunnel_ip }}",
            "result": {
                "tunnels": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "nhs": {"{{ tunnel_ip }}": {"tunnel_ip": "{{ tunnel_ip }}", "nbma": {"{{ nbma }}": "{{ nbma }}"}}},
                    },
                },
            },
        },
        # any other tunnel line: the tunnel exists
        {
            "name": "tunnel",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+nhrp
                \s+tunnel
                \s+(?P<name>\S+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "protocols nhrp tunnel {{ name }}",
            "result": {"tunnels": {"{{ name }}": {"name": "{{ name }}"}}},
        },
    ]
    # fmt: on
