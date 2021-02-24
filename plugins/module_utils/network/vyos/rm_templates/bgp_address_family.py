# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The Bgp_address_family parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

def _tmplt_bgp_af_aggregate_address(config_data):
    afi = config_data['address_family']['afi'] + '-unicast'
    command = "protocols bgp {as_number} address-family ".format(
        **config_data
    )
    config_data = config_data["adress_family"]
    if config_data["aggregate_address"].get("as_set"):
        command += " {prefix} as-set".format(
            **config_data["aggregate_address"]
        )
    if config_data["aggregate_address"].get("summary_only"):
        command += " {prefix} summary-only".format(
            **config_data["aggregate_address"]
        )
    return command


class Bgp_address_familyTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Bgp_address_familyTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix)

    # fmt: off
    PARSERS = [
        {
            "name": "router",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+bgp
                \s+(?P<as_num>\d+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "protocols bgp {{ as_number }}",
            "compval": "as_number",
            "result": {
                "as_number": "{{ as_num }}",
            }
        },
        {
            "name": "aggregate_address",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+bgp
                \s+(?P<as_num>\d+)
                \s+address-family
                \s+(?P<afi>\S+)
                \s+aggregate-address
                \s+(?P<address>\S+)
                \s*(?P<as_set>as-set)*
                \s*(?P<summary_only>summary-only)*
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_bgp_af_aggregate_address,
            "remval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast aggregate-address {{ aggregate_address.prefix }}",
            "compval": "aggregate_address",
            "result": {
                "as_number": "{{ as_num }}",
                "address_family": {
                    "{{ afi }}": {
                        "afi": "{{ afi }}",
                        "aggregate_address": [
                            {
                                "prefix": "{{ address }}",
                                "as_set": "{{ True if as_set is defined }}",
                                "summary_only": "{{ True if summary_only is defined }}"
                            }
                        ]
                    }
                }
            }
        },
        {
            "name": "network.backdoor",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+bgp
                \s+(?P<as_num>\d+)
                \s+address-family
                \s+(?P<afi>\S+)
                \s+network
                \s+(?P<address>\S+)
                \s+backdoor
                *$""",
                re.VERBOSE,
            ),
            "setval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast network {{ network.address }} backdoor",
            "remval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast network {{ network.address }}",
            "compval": "network.backdoor",
            "result": {
                "as_number": "{{ as_num }}",
                "address_family": {
                    "{{ afi }}": {
                        "afi": "{{ afi }}",
                        "network": [
                            {
                                "address": "{{ address }}",
                                "backdoor": "{{ True }}"
                            }
                        ]
                    }
                }
            }
        },
        {
            "name": "network.path_limit",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+bgp
                \s+(?P<as_num>\d+)
                \s+address-family
                \s+(?P<afi>\S+)
                \s+network
                \s+(?P<address>\S+)
                \s+path-limit
                \s+(?P<limit>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast network {{ network.address }} path-limit {{ network.path_limit }}",
            "remval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast network {{ network.address }}",
            "compval": "network.route_map",
            "result": {
                "as_number": "{{ as_num }}",
                "address_family": {
                    "{{ afi }}": {
                        "afi": "{{ afi }}",
                        "network": [
                            {
                                "address": "{{ address }}",
                                "path_limit": "{{ limit|int }}"
                            }
                        ]
                    }
                }
            }
        }, 
        {
            "name": "network.route_map",
            "getval": re.compile(
                r"""
                ^set
                \s+protocols
                \s+bgp
                \s+(?P<as_num>\d+)
                \s+address-family
                \s+(?P<afi>\S+)
                \s+network
                \s+(?P<address>\S+)
                \s+route-map
                \s+(?P<map>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast network {{ network.address }} route-map {{ network.route_map }}",
            "remval": "protocols bgp {{ as_number }} address-family {{ afi }}-unicast network {{ network.address }}",
            "compval": "network.route_map",
            "result": {
                "as_number": "{{ as_num }}",
                "address_family": {
                    "{{ afi }}": {
                        "afi": "{{ afi }}",
                        "network": [
                            {
                                "address": "{{ address }}",
                                "route_map": "{{ map }}"
                            }
                        ]
                    }
                }
            }
        }, 
    ]
    # fmt: on
