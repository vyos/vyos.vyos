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
    \s+(?P<vlan>\d+)
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
        {
            # any other interface line: the interface exists
            "name": "name",
            "getval": re.compile(INTF + r"(?:\s.*)?$", re.VERBOSE),
            "setval": "interfaces {{ type }} {{ name }}",
            "result": {"{{ name }}": {"name": "{{ name }}"}},
        },
    ]
    # fmt: on
