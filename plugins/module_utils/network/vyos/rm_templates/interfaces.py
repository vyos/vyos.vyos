# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Interfaces parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


# interface types the module manages
TYPES = r"ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard"

# set interfaces <type> <name>; the name is quoted when it ends the line ('lo')
INTF = (
    r"""
    ^set
    \s+interfaces
    \s+(?P<type>"""
    + TYPES
    + r""")
    \s+'?(?P<name>[^'\s]+)'?
"""
)

# ... vif <vlan-id>
VIF = (
    INTF
    + r"""
    \s+vif
    \s+'?(?P<vlan>\d+)'?
"""
)

# a value, quoted ('text with spaces') or not
VALUE = r"""
    \s+(?:'(?P<q>.*)'|(?P<u>\S+))
    \s*$
"""

VAL = "{{ q if q is defined else u }}"


def _intf_parser(name, keyword, key=None):
    """An interface option with a value, e.g. description 'text'."""
    key = key or name
    return {
        "name": name,
        "getval": re.compile(INTF + r"\s+" + keyword + VALUE, re.VERBOSE),
        "setval": "interfaces {{ type }} {{ name }} " + keyword + " '{{ " + key + " }}'",
        "remval": "interfaces {{ type }} {{ name }} " + keyword,
        "result": {"{{ name }}": {"name": "{{ name }}", key: VAL}},
    }


def _vif_parser(name, keyword, key):
    """A vif option with a value, e.g. vif 10 description 'text'."""
    return {
        "name": name,
        "getval": re.compile(VIF + r"\s+" + keyword + VALUE, re.VERBOSE),
        "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} "
        + keyword
        + " '{{ vifs."
        + key
        + " }}'",
        "remval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} " + keyword,
        "compval": "vifs." + key,
        "result": {
            "{{ name }}": {
                "name": "{{ name }}",
                "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", key: VAL}},
            },
        },
    }


class InterfacesTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(InterfacesTemplate, self).__init__(
            lines=lines,
            tmplt=self,
            prefix=prefix,
            module=module,
        )

    # The first matching parser wins for each line, so specific parsers come first,
    # then the vif catch-all, then the interface catch-all.
    # fmt: off
    PARSERS = [
        _intf_parser("description", "description"),
        _intf_parser("mtu", "mtu"),
        _intf_parser("duplex", "duplex"),
        _intf_parser("speed", "speed"),
        _intf_parser("vrf", "vrf"),
        {
            "name": "disable",
            "getval": re.compile(INTF + r"\s+disable\s*$", re.VERBOSE),
            "setval": "interfaces {{ type }} {{ name }} disable",
            "result": {"{{ name }}": {"name": "{{ name }}", "enabled": False}},
        },
        _vif_parser("vifs.description", "description", "description"),
        _vif_parser("vifs.mtu", "mtu", "mtu"),
        _vif_parser("vifs.vrf", "vrf", "vrf"),
        {
            "name": "vifs.disable",
            "getval": re.compile(VIF + r"\s+disable\s*$", re.VERBOSE),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} disable",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "enabled": False}},
                },
            },
        },
        {
            # any other vif line: the vif exists
            "name": "vifs",
            "getval": re.compile(VIF + r"(?:\s.*)?$", re.VERBOSE),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }}",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}"}},
                },
            },
        },
        # set interfaces tunnel <name> encapsulation|source-address|source-interface|remote <value>
        {
            "name": "tunnel.encapsulation",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+encapsulation
                \s+'?(?P<encapsulation>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} encapsulation '{{ tunnel.encapsulation }}'",
            "remval": "interfaces {{ type }} {{ name }} encapsulation",
            "compval": "tunnel.encapsulation",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"encapsulation": "{{ encapsulation }}"}}},
        },
        {
            "name": "tunnel.source_address",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+source-address
                \s+'?(?P<source_address>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} source-address '{{ tunnel.source_address }}'",
            "remval": "interfaces {{ type }} {{ name }} source-address",
            "compval": "tunnel.source_address",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"source_address": "{{ source_address }}"}}},
        },
        {
            "name": "tunnel.source_interface",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+source-interface
                \s+'?(?P<source_interface>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} source-interface '{{ tunnel.source_interface }}'",
            "remval": "interfaces {{ type }} {{ name }} source-interface",
            "compval": "tunnel.source_interface",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"source_interface": "{{ source_interface }}"}}},
        },
        {
            "name": "tunnel.remote",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+remote
                \s+'?(?P<remote>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} remote '{{ tunnel.remote }}'",
            "remval": "interfaces {{ type }} {{ name }} remote",
            "compval": "tunnel.remote",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"remote": "{{ remote }}"}}},
        },
        # set interfaces tunnel <name> enable-multicast
        {
            "name": "tunnel.enable_multicast",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+enable-multicast
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} enable-multicast",
            "remval": "interfaces {{ type }} {{ name }} enable-multicast",
            "compval": "tunnel.enable_multicast",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"enable_multicast": True}}},
        },
        # set interfaces tunnel <name> parameters ip key|ttl|tos <value>
        {
            "name": "tunnel.parameters.ip.key",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+parameters\s+ip\s+key
                \s+'?(?P<key>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} parameters ip key '{{ tunnel.parameters.ip.key }}'",
            "remval": "interfaces {{ type }} {{ name }} parameters ip key",
            "compval": "tunnel.parameters.ip.key",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"parameters": {"ip": {"key": "{{ key }}"}}}}},
        },
        {
            "name": "tunnel.parameters.ip.ttl",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+parameters\s+ip\s+ttl
                \s+'?(?P<ttl>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} parameters ip ttl '{{ tunnel.parameters.ip.ttl }}'",
            "remval": "interfaces {{ type }} {{ name }} parameters ip ttl",
            "compval": "tunnel.parameters.ip.ttl",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"parameters": {"ip": {"ttl": "{{ ttl }}"}}}}},
        },
        {
            "name": "tunnel.parameters.ip.tos",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+parameters\s+ip\s+tos
                \s+'?(?P<tos>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} parameters ip tos '{{ tunnel.parameters.ip.tos }}'",
            "remval": "interfaces {{ type }} {{ name }} parameters ip tos",
            "compval": "tunnel.parameters.ip.tos",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"parameters": {"ip": {"tos": "{{ tos }}"}}}}},
        },
        # set interfaces tunnel <name> parameters ip no-pmtu-discovery|ignore-df
        {
            "name": "tunnel.parameters.ip.no_pmtu_discovery",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+parameters\s+ip\s+no-pmtu-discovery
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} parameters ip no-pmtu-discovery",
            "remval": "interfaces {{ type }} {{ name }} parameters ip no-pmtu-discovery",
            "compval": "tunnel.parameters.ip.no_pmtu_discovery",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"parameters": {"ip": {"no_pmtu_discovery": True}}}}},
        },
        {
            "name": "tunnel.parameters.ip.ignore_df",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>tunnel)
                \s+'?(?P<name>[^'\s]+)'?
                \s+parameters\s+ip\s+ignore-df
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} parameters ip ignore-df",
            "remval": "interfaces {{ type }} {{ name }} parameters ip ignore-df",
            "compval": "tunnel.parameters.ip.ignore_df",
            "result": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"parameters": {"ip": {"ignore_df": True}}}}},
        },
        {
            # any other interface line: the interface exists
            "name": "name",
            "getval": re.compile(INTF + r"(?:\s.*)?$", re.VERBOSE),
            "setval": "interfaces {{ type }} {{ name }}",
            "result": {"{{ name }}": {"name": "{{ name }}"}},
        },
    ]
    # fmt: on
