# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Route_maps parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

class Route_mapsTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Route_mapsTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix)

    # fmt: off
    PARSERS = [
        {
            "name": "route_map",
            "getval": re.compile(
                r"""
                ^set
                \s+policy
                \s+route-map
                \s+(?P<route_map>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "policy route-map {{route_map_name}}",
            "compval": "route_map_name",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map_name": "{{route_map}}"
                    },
                },
            },
            "shared": True
        },
        {
            "name": "route_map_description",
            "getval": re.compile(
                r"""
                ^set
                \s+policy
                \s+route-map
                \s+(?P<route_map>\S+)
                \s+description
                \s(?P<description>\S+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "policy route-map {{route_map_name}} description {{description}}",
            "compval": "description",
            "result": {
                "route_maps": {
                    "{{ route_map}}": {
                        "description": "{{description}}"
                    },
                },
            },
        },
        {
            "name": "rule_number",
            "getval": re.compile(
                r"""
                ^set
                \s+policy
                \s+route-map
                \s+(?P<route_map>\S+)
                \s+rule
                \s+(?P<rule_number>\d+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "policy route-map {{route_map_name}} rule {{rule_number}}",
            "result": {
                "route_maps": {
                    "{{ route_map}}": {
                        "rules": {
                            "{{rule_number}}": {
                                "rule_number": "{{rule_number}}"
                            }

                        }
                    },
                },
            },
        },
        {
            "name": "rule_number",
            "getval": re.compile(
                r"""
                ^set
                \s+policy
                \s+route-map
                \s+(?P<route_map>\S+)
                \s+rule
                \s+(?P<rule_number>\d+)
                *$""",
                re.VERBOSE,
            ),
            "setval": "policy route-map {{route_map_name}} rule {{rule_number}}",
            "result": {
                "route_maps": {
                    "{{ route_map}}": {
                        "rules": {
                            "{{rule_number}}": {
                                "rule_number": "{{rule_number}}"
                            }

                        }
                    },
                },
            },
        },
    ]
    # fmt: on
