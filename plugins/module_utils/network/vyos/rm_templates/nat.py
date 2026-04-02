# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Nat parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class NatTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        self._overrides = {  # 1.4+ by default
            "_path": "service",  # 1.4 or greater, "system" for 1.3 or less
            "_ac": "allow-client",  # 1.4 or greater, "allow-clients" for 1.3 or less
        }
        super(NatTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # def set_nat_path(self, path: str):
    #     """set_nat_path"""
    #     self._overrides["_path"] = path

    # def set_ntp_ac(self, ac: str):
    #     """set_ntp_ac"""
    #     self._overrides["_ac"] = ac

    # def render(self, data, parser_name, negate=False):
    #     """render"""
    #     # add path to the data before rendering
    #     data = data.copy()
    #     data.update(self._overrides)
    #     # call the original method
    #     return super(NtpTemplate, self).render(data, parser_name, negate)

    # fmt: off
    PARSERS = [



        # set nat cgnat log-allocation
        {
            "name": "log_allocation",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                log-allocation
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat log-allocation",
            "result": {
                "cgnat": {
                    "log_allocation": True,
                },
            },
        },

        # set nat cgnat pool external <name> external-port-range <range>
        {
            "name": "external_port_range",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                pool\s
                external\s
                (?P<name>\S+)\s
                external-port-range\s
                ['"]?(?P<range>\S+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{name}} external-port-range '{{external_port_range}}'",
            "result": {
                "cgnat": {
                    "pool": {
                        "external": [
                            {
                                "name": "{{name}}",
                                "external_port_range": "{{range}}",
                            },
                        ],
                    },
                },
            },
        },

        # set nat cgnat pool external <name> per-user-limit port <limit>
        {
            "name": "per_user_limit_port",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                pool\s
                external\s
                (?P<name>\S+)\s
                per-user-limit\s
                port\s
                ['"]?(?P<limit>\d+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{name}} per-user-limit port '{{per_user_limit_port}}'",
            "result": {
                "cgnat": {
                    "pool": {
                        "external": [
                            {
                                "name": "{{name}}",
                                "per_user_limit_port": "{{limit}}",
                            },
                        ],
                    },
                },
            },
        },

        # set nat cgnat pool external <name> range <range>
        {
            "name": "external_range",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                pool\s
                external\s
                (?P<name>\S+)\s
                range\s
                ['"]?(?P<range>\S+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{name}} range '{{range}}'",
            "result": {
                "cgnat": {
                    "pool": {
                        "external": [
                            {
                                "name": "{{name}}",
                                "ranges": ["{{range}}"],
                            },
                        ],
                    },
                },
            },
        },

        # set nat cgnat pool external <name> range <range> seq <seq>
        {
            "name": "external_range_seq",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                pool\s
                external\s
                (?P<name>\S+)\s
                range\s
                ['"]?(?P<range>\S+)['"]?\s
                seq\s
                ['"]?(?P<seq>\d+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{name}} range '{{range}}' seq '{{seq}}'",
            "result": {
                "cgnat": {
                    "pool": {
                        "external": [
                            {
                                "name": "{{name}}",
                                "ranges": ["{{range}}"],
                                "seq": "{{seq}}",
                            },
                        ],
                    },
                },
            },
        },

        # set nat cgnat pool internal <name> range <range>
        {
            "name": "internal_range",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                pool\s
                internal\s
                (?P<name>\S+)\s
                range\s
                ['"]?(?P<range>\S+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool internal {{name}} range '{{range}}'",
            "result": {
                "cgnat": {
                    "pool": {
                        "internal": [
                            {
                                "name": "{{name}}",
                                "ranges": ["{{range}}"],
                            },
                        ],
                    },
                },
            },
        },

        # set nat cgnat rule <id> source pool <pool>
        {
            "name": "rule_source_pool",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                rule\s
                (?P<id>\d+)\s
                source\s
                pool\s
                ['"]?(?P<pool>\S+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat rule {{id}} source pool '{{source_pool}}'",
            "result": {
                "cgnat": {
                    "rule": [
                        {
                            "id": "{{id}}",
                            "source": {
                                "pool": "{{pool}}",
                            },
                        },
                    ],
                },
            },
        },

        # set nat cgnat rule <id> translation pool <pool>
        {
            "name": "rule_translation_pool",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                cgnat\s
                rule\s
                (?P<id>\d+)\s
                translation\s
                pool\s
                ['"]?(?P<pool>\S+)['"]?
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat cgnat rule {{id}} translation pool '{{translation_pool}}'",
            "result": {
                "cgnat": {
                    "rule": [
                        {
                            "id": "{{id}}",
                            "translation": {
                                "pool": "{{pool}}",
                            },
                        },
                    ],
                },
            },
        },

        # set nat destination rule <id> description <description>
        {
            "name": "nat_destination_description",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                destination\s
                rule\s
                (?P<rule>\d+)\s
                description\s
                (?P<description>.+)
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat destination rule {{ rule }} description {{ description }}",
            "result": {
                "destination": {
                    "rule": {
                        "{{ rule }}": {
                            "description": "{{ description }}",
                        },
                    },
                },
            },
        },

        # set nat destination rule <id> destination address <dest_address>
        {
            "name": "nat_destination_dest_address",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                destination\s
                rule\s
                (?P<rule>\d+)\s
                destination\s
                address\s
                (?P<dest_address>\S+)
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat destination rule {{ rule }} destination address {{ dest_address }}",
            "result": {
                "destination": {
                    "rule": {
                        "{{ rule }}": {
                            "destination": {
                                "address": "{{ dest_address }}",
                            },
                        },
                    },
                },
            },
        },

        # set nat destination rule <id> destination port <dest_port>
        {
            "name": "nat_destination_dest_port",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                destination\s
                rule\s
                (?P<rule>\d+)\s
                destination\s
                port\s
                (?P<dest_port>\d+)
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat destination rule {{ rule }} destination port {{ dest_port }}",
            "result": {
                "destination": {
                    "rule": {
                        "{{ rule }}": {
                            "destination": {
                                "port": "{{ dest_port }}",
                            },
                        },
                    },
                },
            },
        },

        # set nat destination rule <id> translation address
        {
            "name": "nat_destination_translation_address",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                destination\s
                rule\s
                (?P<rule>\d+)\s
                translation\s
                address\s
                (?P<trans_address>\S+)
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat destination rule {{ rule }} translation address {{ trans_address }}",
            "result": {
                "destination": {
                    "rule": {
                        "{{ rule }}": {
                            "translation": {
                                "address": "{{ trans_address }}",
                            },
                        },
                    },
                },
            },
        },

        # set nat destination rule <id> translation port
        {
            "name": "nat_destination_translation_port",
            "getval": re.compile(
                r"""
                ^set\s
                nat\s
                destination\s
                rule\s
                (?P<rule>\d+)\s
                translation\s
                port\s
                (?P<trans_port>\d+)
                $
                """,
                re.VERBOSE,
            ),
            "setval": "nat destination rule {{ rule }} translation port {{ trans_port }}",
            "result": {
                "destination": {
                    "rule": {
                        "{{ rule }}": {
                            "translation": {
                                "port": "{{ trans_port }}",
                            },
                        },
                    },
                },
            },
        },

    ]
    # fmt: on
