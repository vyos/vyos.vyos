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


class VrfTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(VrfTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # fmt: off
    PARSERS = [
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
            "compval": "bta",
            "result": {
                "bind_to_all": "{{ True if bta is defined }}",
            },
        },
        {
            "name": "table",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \stable
                \s(?P<tid>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} table {{tid}}",
            "compval": "table_id",
            "result": {
                "instances": {
                    "name": "{{ name }}",
                    "table_id": "{{ tid }}",
                },
            },
        },
        {
            "name": "vni",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \svni
                \s(?P<vni>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} vni {{vni}}",
            "compval": "vni",
            "result": {
                "instances": {
                    "name": "{{ name }}",
                    "vni": "{{ vni }}",
                },
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
            "setval": "vrf name {{name}} description {{desc}}",
            "compval": "desc",
            "result": {
                "instances": {
                    "name": "{{ name }}",
                    "description": "{{ desc }}",
                },
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
            "compval": "desc",
            "result": {
                "instances": {
                    "name": "{{ name }}",
                    "disable": "{{ True if disable is defined }}",
                },
            },
        },
        {
            "name": "disable_forwarding",
            "getval": re.compile(
                r"""
                ^set
                \svrf
                \sname
                \s(?P<name>\S+)
                \s(?P<af>\S+)
                \s(?P<df>disable-forwarding)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} {{ af }} disable-forwarding",
            "compval": "address_family.disable_forwarding",
            "result": {
                "name": "{{ name }}",
                "address_family": {
                    '{{ "ipv4" if af == "ip" else "ipv6" }}': {
                        "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
                        "disable_forwarding": "{{ True if df is defined }}",
                    },
                },
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
                \s(?P<af>\S+)
                \snht
                \s(?P<nht>no-resolve-via-default)
                $""",
                re.VERBOSE,
            ),
            "setval": "vrf name {{name}} {{ af }} nht no-resolve-via-default",
            "compval": "address_family.no_resolve_via_default",
            "result": {
                "name": "{{ name }}",
                "address_family": {
                    '{{ "ipv4" if af == "ip" else "ipv6" }}': {
                        "afi": '{{ "ipv4" if af == "ip" else "ipv6" }}',
                        "no_resolve_via_default": "{{ True if nht is defined }}",
                    },
                },
            },
        },
    ]
    # fmt: on
