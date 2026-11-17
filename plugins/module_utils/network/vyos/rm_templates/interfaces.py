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
        # set interfaces <type> <name> description <value>
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+description
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} description '{{ description }}'",
            "remval": "interfaces {{ type }} {{ name }} description",
            "result": {"{{ name }}": {"name": "{{ name }}", "description": "{{ q if q is defined else u }}"}},
        },
        # set interfaces <type> <name> mtu <value>
        {
            "name": "mtu",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+mtu
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} mtu '{{ mtu }}'",
            "remval": "interfaces {{ type }} {{ name }} mtu",
            "result": {"{{ name }}": {"name": "{{ name }}", "mtu": "{{ q if q is defined else u }}"}},
        },
        # set interfaces <type> <name> duplex <value>
        {
            "name": "duplex",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+duplex
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} duplex '{{ duplex }}'",
            "remval": "interfaces {{ type }} {{ name }} duplex",
            "result": {"{{ name }}": {"name": "{{ name }}", "duplex": "{{ q if q is defined else u }}"}},
        },
        # set interfaces <type> <name> speed <value>
        {
            "name": "speed",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+speed
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} speed '{{ speed }}'",
            "remval": "interfaces {{ type }} {{ name }} speed",
            "result": {"{{ name }}": {"name": "{{ name }}", "speed": "{{ q if q is defined else u }}"}},
        },
        # set interfaces <type> <name> vrf <value>
        {
            "name": "vrf",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vrf
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vrf '{{ vrf }}'",
            "remval": "interfaces {{ type }} {{ name }} vrf",
            "result": {"{{ name }}": {"name": "{{ name }}", "vrf": "{{ q if q is defined else u }}"}},
        },
        {
            "name": "disable",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+disable
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} disable",
            "result": {"{{ name }}": {"name": "{{ name }}", "enabled": False}},
        },
        # set interfaces <type> <name> vif <vlan-id> description <value>
        {
            "name": "vifs.description",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                \s+description
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} description '{{ vifs.description }}'",
            "remval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} description",
            "compval": "vifs.description",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "description": "{{ q if q is defined else u }}"}},
                },
            },
        },
        # set interfaces <type> <name> vif <vlan-id> mtu <value>
        {
            "name": "vifs.mtu",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                \s+mtu
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} mtu '{{ vifs.mtu }}'",
            "remval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} mtu",
            "compval": "vifs.mtu",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "mtu": "{{ q if q is defined else u }}"}},
                },
            },
        },
        # set interfaces <type> <name> vif <vlan-id> vrf <value>
        {
            "name": "vifs.vrf",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                \s+vrf
                \s+(?:'(?P<q>.*)'|(?P<u>\S+))
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} vrf '{{ vifs.vrf }}'",
            "remval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} vrf",
            "compval": "vifs.vrf",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "vrf": "{{ q if q is defined else u }}"}},
                },
            },
        },
        {
            "name": "vifs.disable",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                \s+disable
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} disable",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "enabled": False}},
                },
            },
        },
        # set interfaces <type> <name> vif <vlan-id> ip adjust-mss <value>
        {
            "name": "vifs.ip.adjust_mss",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                \s+ip\s+adjust-mss
                \s+'?(?P<mss>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} ip adjust-mss '{{ vifs.ip.adjust_mss }}'",
            "remval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} ip adjust-mss",
            "compval": "vifs.ip.adjust_mss",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "ip": {"adjust_mss": "{{ mss }}"}}},
                },
            },
        },
        # set interfaces <type> <name> vif <vlan-id> ipv6 adjust-mss <value>
        {
            "name": "vifs.ipv6.adjust_mss",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                \s+ipv6\s+adjust-mss
                \s+'?(?P<mss>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} ipv6 adjust-mss '{{ vifs.ipv6.adjust_mss }}'",
            "remval": "interfaces {{ type }} {{ name }} vif {{ vifs.vlan_id }} ipv6 adjust-mss",
            "compval": "vifs.ipv6.adjust_mss",
            "result": {
                "{{ name }}": {
                    "name": "{{ name }}",
                    "vifs": {"{{ vlan }}": {"vlan_id": "{{ vlan }}", "ipv6": {"adjust_mss": "{{ mss }}"}}},
                },
            },
        },
        {
            # any other vif line: the vif exists
            "name": "vifs",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+vif
                \s+'?(?P<vlan>\d+)'?
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
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
        # set interfaces <type> <name> ip adjust-mss <value>
        {
            "name": "ip.adjust_mss",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|tunnel|vti|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+ip\s+adjust-mss
                \s+'?(?P<mss>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} ip adjust-mss '{{ ip.adjust_mss }}'",
            "remval": "interfaces {{ type }} {{ name }} ip adjust-mss",
            "compval": "ip.adjust_mss",
            "result": {"{{ name }}": {"name": "{{ name }}", "ip": {"adjust_mss": "{{ mss }}"}}},
        },
        # set interfaces <type> <name> ipv6 adjust-mss <value>
        {
            "name": "ipv6.adjust_mss",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|tunnel|vti|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                \s+ipv6\s+adjust-mss
                \s+'?(?P<mss>[^'\s]+)'?
                \s*$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }} ipv6 adjust-mss '{{ ipv6.adjust_mss }}'",
            "remval": "interfaces {{ type }} {{ name }} ipv6 adjust-mss",
            "compval": "ipv6.adjust_mss",
            "result": {"{{ name }}": {"name": "{{ name }}", "ipv6": {"adjust_mss": "{{ mss }}"}}},
        },
        {
            # any other interface line: the interface exists
            "name": "name",
            "getval": re.compile(
                r"""
                ^set
                \s+interfaces
                \s+(?P<type>ethernet|bonding|bridge|dummy|tunnel|vti|loopback|vxlan|openvpn|wireguard)
                \s+'?(?P<name>[^'\s]+)'?
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "interfaces {{ type }} {{ name }}",
            "result": {"{{ name }}": {"name": "{{ name }}"}},
        },
    ]
    # fmt: on
