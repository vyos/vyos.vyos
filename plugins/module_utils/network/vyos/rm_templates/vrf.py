# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The VRF parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class VrfTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(VrfTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "table_id",
            "getval": re.compile(
                r"""
                ^set
                \s+vrf
                \s+name
                \s+(?P<name>\S+)
                \s+table
                \s+'(?P<tid>\S+)'
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{ name }} table {{ table_id }}",
            "result": {
                "name": "{{ name }}",
                "table_id": "{{ tid }}",
            },
        },
        {
            "name": "bind_to_all",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \s(?P<bta>bind-to-all)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf bind-to-all",
            "result": {
                "bind_to_all": "{{ True if bta is defined }}",
            },
        },
        {
            "name": "vni",
            "getval": re.compile(
                r"""
                ^set
                \s+vrf
                \s+name
                \s+(?P<name>\S+)
                \s+vni
                \s'(?P<vni>\S+)'
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} vni {{vni}}",
            "result": {
                "name": "{{ name }}",
                "vni": "{{ vni }}",
            },
        },
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \sdescription
                \s(?P<desc>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} description {{description}}",
            "result": {
                "name": "{{ name }}",
                "description": "{{ desc }}",
            },
        },
        {
            "name": "disable_vrf",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \s(?P<disable>disable)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} disable",
            "compval": "disable",
            "result": {
                "name": "{{ name }}",
                "disable": "{{ True if disable is defined }}",
            },
        },
        # {
        #     "name": "address_family",
        #     "getval": re.compile(
        #         r"""
        #         ^set
        #         \svrf
        #         \sname
        #         \s(?P<name>\S+)
        #         \s(?P<af>ip|ipv6)
        #         $""",
        #         re.VERBOSE,
        #     ),
        #     "setval": "vrf name {{name}} {{ af }}",
        #     'compval': "address_family",
        #     "result": {
        #         "name": "{{ name }}",
        #         "address_family": {
        #             '{{ "ipv4" if af == "ip" else "ipv6" }}': {
        #                 "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
        #             },
        #         },
        #     },
        # },
        # {
        #     "name": "address_family.disable_forwarding",
        #     "getval": re.compile(
        #         r"""
        #         ^set
        #         \svrf
        #         \sname
        #         \s(?P<name>\S+)
        #         \s(?P<af>ip|ipv6)
        #         \s(?P<df>disable-forwarding)
        #         $""",
        #         re.VERBOSE,
        #     ),
        #     "setval": "vrf name {{name}} {{ afi }} disable-forwarding",
        #     # "compval": "address_family.ipv6.disable_forwarding",
        #     "result": {
        #         "name": "{{ name }}",
        #         "address_family": {
        #             '{{ "ipv4" if af == "ip" else "ipv6" }}': {
        #                 "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
        #                 "disable_forwarding": "{{ True if df is defined }}",
        #             },
        #         },
        #     },
        # },
        {
            "name": "disable_forwarding",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \s(?P<af>ip|ipv6)
                \s(?P<df>disable-forwarding)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} {{ afi }} disable-forwarding",
            "compval": "disable_forwarding",
            "result": {
                "name": "{{ name }}",
                'address_family': [{
                    "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
                    "disable_forwarding": "{{ True if df is defined }}",
                }],
            },
        },
        {
            "name": "disable_nht",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \s(?P<af>ip|ipv6)
                \snht
                \s(?P<nht>no-resolve-via-default)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} {{ afi }} nht no-resolve-via-default",
            "compval": "nht_no_resolve_via_default",
            "result": {
                "name": "{{ name }}",
                "address_family": [{
                    "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
                    "nht_no_resolve_via_default": "{{ True if nht is defined }}",
                }],
            },
        },
        {
            "name": "route_maps",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \s(?P<af>ip|ipv6)
                \sprotocol
                \s(?P<proto>\S+)
                \sroute-map
                \s'(?P<rm>\S+)'
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} {{ afi }} protocol {{ route_maps.protocol }} route-map {{ route_maps.rm_name }}",
            "compval": "route_maps",
            "remval": "vrf name {{name}} {{ afi }} protocol {{ route_maps.protocol }}",
            "result": {
                "name": "{{ name }}",
                "address_family": [{
                    "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
                    "route_maps": [{
                        "rm_name": "{{ rm }}",
                        "protocol": "{{ proto }}",
                    }],
                }],
            },
        },
    ]
    # fmt: on
