# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class NatTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(NatTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # def parse(self):
    #     data = super(NatTemplate, self).parse()
    #     return self._normalize(data)

    # def _normalize(self, data):
    #     def convert_rules(section):
    #         if not section or "rule" not in section:
    #             return section

    #         rules = section["rule"]

    #         if isinstance(rules, dict):
    #             new_rules = []
    #             for rule_id, rule_data in rules.items():
    #                 rule = rule_data.copy()

    #                 # normalize id
    #                 try:
    #                     rule["id"] = int(rule_id)
    #                 except (ValueError, TypeError):
    #                     rule["id"] = rule_id

    #                 new_rules.append(rule)

    #             section["rule"] = sorted(new_rules, key=lambda x: x.get("id", 0))

    #         return section

    #     if not data:
    #         return data

    #     for nat_type in ["nat", "nat64", "nat66"]:
    #         if nat_type not in data:
    #             continue

    #         nat = data[nat_type]

    #         for block in ["destination", "source", "static"]:
    #             if block in nat:
    #                 nat[block] = convert_rules(nat[block])

    #         # CGNAT rules
    #         if "cgnat" in nat and "rule" in nat["cgnat"]:
    #             rules = nat["cgnat"]["rule"]
    #             if isinstance(rules, list):
    #                 for r in rules:
    #                     if "id" in r:
    #                         r["id"] = int(r["id"])

    #     return data

    # def _normalize(self, data):
    #     if not data:
    #         return data

    #     def normalize_rules(rules):
    #         """Convert rules dict → sorted list with int IDs, or cast IDs in existing list."""
    #         if isinstance(rules, dict):
    #             result = []
    #             for rule_id, rule_data in rules.items():
    #                 rule = rule_data.copy()
    #                 try:
    #                     rule["id"] = int(rule_id)
    #                 except (ValueError, TypeError):
    #                     rule["id"] = rule_id
    #                 result.append(rule)
    #             return sorted(result, key=lambda x: x.get("id", 0))

    #         if isinstance(rules, list):
    #             for rule in rules:
    #                 if "id" in rule:
    #                     try:
    #                         rule["id"] = int(rule["id"])
    #                     except (ValueError, TypeError):
    #                         pass
    #             return rules

    #         return rules

    #     for nat_type in ["nat", "nat64", "nat66"]:
    #         nat = data.get(nat_type)
    #         if not nat:
    #             continue

    #         for block in ["destination", "source", "static", "cgnat"]:
    #             section = nat.get(block)
    #             if section and "rule" in section:
    #                 section["rule"] = normalize_rules(section["rule"])

    #     return data

    # fmt: off
    PARSERS = [

        #
        # -------------------------
        # CGNAT (keep explicit)
        # -------------------------
        #
        {
            "name": "cgnat_log_allocation",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+log-allocation
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat log-allocation",
            "result": {
                "nat": {
                    "cgnat": {
                        "log_allocation": True,
                    },
                },
            },
        },
        {
            "name": "cgnat_pool_external_range",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+pool
                \s+external
                \s+(?P<name>\S+)
                \s+range
                \s+(?P<range>\S+)(?:\s+seq\s+(?P<seq>\d+))?
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{ name }} range {{ range }}{% if seq is defined %} seq {{ seq }}{% endif %}",
            "result": {
                "nat": {
                    "cgnat": {
                        "pool": {
                            "external": [
                                {
                                    "name": "{{ name }}",
                                    "range": ["{{ range }}"],
                                    "seq": "{{ seq }}",
                                },
                            ],
                        },
                    },
                },
            },
        },
        {
            "name": "cgnat_pool_external_port_range",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+pool
                \s+external
                \s+(?P<name>\S+)
                \s+external-port-range
                \s+(?P<range>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{ name }} external-port-range {{ range }}",
            "result": {
                "nat": {
                    "cgnat": {
                        "pool": {
                            "external": [
                                {
                                    "name": "{{ name }}",
                                    "external_port_range": "{{ range }}",
                                },
                            ],
                        },
                    },
                },
            },
        },
        {
            "name": "cgnat_pool_external_per_user",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+pool
                \s+external
                \s+(?P<name>\S+)
                \s+per-user-limit
                \s+port
                \s+(?P<limit>\d+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool external {{ name }} per-user-limit port {{ limit }}",
            "result": {
                "nat": {
                    "cgnat": {
                        "pool": {
                            "external": [
                                {
                                    "name": "{{ name }}",
                                    "per_user_limit": {"port": "{{ limit }}"},
                                },
                            ],
                        },
                    },
                },
            },
        },
        {
            "name": "cgnat_pool_internal_range",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+pool
                \s+internal
                \s+(?P<name>\S+)
                \s+range
                \s+(?P<range>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat pool internal {{ name }} range {{ range }}",
            "result": {
                "nat": {
                    "cgnat": {
                        "pool": {
                            "internal": [
                                {
                                    "name": "{{ name }}",
                                    "range": ["{{ range }}"],
                                },
                            ],
                        },
                    },
                },
            },
        },
        {
            "name": "cgnat_rule_source_pool",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+rule
                \s+(?P<id>\d+)
                \s+source
                \s+pool
                \s+(?P<pool>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat rule {{ id }} source pool {{ pool }}",
            "result": {
                "nat": {
                    "cgnat": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "source": {"pool": "{{ pool }}"},
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "cgnat_rule_translation_pool",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+cgnat
                \s+rule
                \s+(?P<id>\d+)
                \s+translation
                \s+pool
                \s+(?P<pool>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat cgnat rule {{ id }} translation pool {{ pool }}",
            "result": {
                "nat": {
                    "cgnat": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {"pool": "{{ pool }}"},
                            },
                        ],
                    },
                },
            },
        },

        #
        # -------------------------
        # GENERIC NAT (destination/source/static)
        # -------------------------
        #

        # description
        {
            "name": "nat_type_description",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+description
                \s+(?P<description>.+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} description {{ description }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "description": "{{ description }}",
                            },
                        ],
                    },
                },
            },
        },

        # protocol
        {
            "name": "nat_type_protocol",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+protocol
                \s+(?P<protocol>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} protocol {{ protocol }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "protocol": "{{ protocol }}",
                            },
                        ],
                    },
                },
            },
        },

        # flags
        {
            "name": "nat_type_disable",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+disable
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} disable",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "disable": True,
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat_type_exclude",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+exclude
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} exclude",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "exclude": True,
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat_type_log",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+log
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} log",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "log": True,
                            },
                        ],
                    },
                },
            },
        },

        # address (destination/source)
        {
            "name": "nat_type_address",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+(?P<atype>destination|source)
                \s+address
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} {{ atype }} address {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "{{ atype }}": {"address": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        # prefix (destination/source)
        {
            "name": "nat_type_prefix",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+(?P<atype>destination|source)
                \s+prefix
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} {{ atype }} prefix {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "{{ atype }}": {"prefix": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        # fqdn
        {
            "name": "nat_type_fqdn",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+(?P<atype>destination|source)
                \s+fqdn
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} {{ atype }} fqdn {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "{{ atype }}": {"fqdn": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        # port
        {
            "name": "nat_type_port",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+(?P<atype>destination|source)
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} {{ atype }} port {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "{{ atype }}": {"port": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        # translation address
        {
            "name": "nat_type_translation_address",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+address
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} translation address {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {"address": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        # translation port
        {
            "name": "nat_type_translation_port",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} translation port {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {"port": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat_inbound_interface_name",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+inbound-interface
                \s+name
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ id }} inbound-interface name {{ value }}",
            "result": {
                "nat": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "inbound_interface": {"name": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat_inbound_interface_group",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+inbound-interface
                \s+group
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ id }} inbound-interface group {{ value }}",
            "result": {
                "nat": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "inbound_interface": {"group": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        {
            "name": "nat_static_inbound_interface",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+static
                \s+rule
                \s+(?P<id>\S+)
                \s+inbound-interface
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat static rule {{ id }} inbound-interface {{ value }}",
            "result": {
                "nat": {
                    "static": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "inbound_interface": "{{ value }}",
                            },
                        ],
                    },
                },
            },
        },

        # NAT6X inbound interface
        {
            "name": "nat6x_inbound_interface",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+inbound-interface
                \s+name
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} inbound-interface name {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "inbound_interface": "{{ value }}",
                            },
                        ],
                    },
                },
            },
        },


        # outbound interface
        {
            "name": "nat_type_outbound_interface",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+outbound-interface
                \s+name
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} outbound-interface name {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "outbound_interface": {"name": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat_type_outbound_interface_group",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<id>\S+)
                \s+outbound-interface
                \s+group
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} outbound-interface group {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "outbound_interface": {"group": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat_type_address_group",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+(?P<atype>destination|source)
                \s+group
                \s+(?P<gtype>address-group|domain-group|mac-group|network-group|port-group)
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} {{ atype }} group {{ gtype }} {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "{{ atype }}": {
                                    "{{ gtype | replace('-', '_') }}": "{{ value }}",
                                },
                            },
                        ],
                    },
                },
            },
        },
        # packet type
        {
            "name": "nat_type_packet_type",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+packet-type
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} packet-type {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "packet_type": "{{ value }}",
                            },
                        ],
                    },
                },
            },
        },

        # load balance backend
        {
            "name": "nat_type_lb_backend",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+load-balance
                \s+backend
                \s+(?P<ip>\S+)
                \s+weight
                \s+(?P<weight>\d+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} load-balance backend {{ ip }} weight {{ weight }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "load_balance": {
                                    "backend": {
                                        "ip": "{{ ip }}",
                                        "weight": "{{ weight }}",
                                    },
                                },
                            },
                        ],
                    },
                },
            },
        },

        # load balance hash
        {
            "name": "nat_type_lb_hash",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+load-balance
                \s+hash
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} load-balance hash {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "load_balance": {"hash": "{{ value }}"},
                            },
                        ],
                    },
                },
            },
        },

        # translation options
        {
            "name": "nat_type_translation_options",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+options
                \s+(?P<opt>address-mapping|port-mapping)
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} translation options {{ opt }} {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "{{ opt | replace(\"-\", \"_\") }}": "{{ value }}",
                                },
                            },
                        ],
                    },
                },
            },
        },

        # redirect port
        {
            "name": "nat_type_translation_redirect",
            "getval": re.compile(
                r"""
                ^set
                \s+(?P<nat>nat|nat64|nat66)
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+redirect
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "{{ nat }} {{ type }} rule {{ id }} translation redirect port {{ value }}",
            "result": {
                "{{ nat }}": {
                    "{{ type }}": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "redirect_port": "{{ value }}",
                                },
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat64_match_mark",
            "getval": re.compile(
                r"""
                ^set
                \s+nat64
                \s+source
                \s+rule
                \s+(?P<id>\S+)
                \s+match
                \s+mark
                \s+(?P<mark>\d+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat64 source rule {{ id }} match mark {{ mark }}",
            "result": {
                "nat64": {
                    "source": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "match": {"mark": "{{ mark }}"},
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat64_translation_pool_address",
            "getval": re.compile(
                r"""
                ^set
                \s+nat64
                \s+source
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+pool
                \s+(?P<pool_id>\d+)
                \s+address
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat64 source rule {{ id }} translation pool {{ pool_id }} address {{ value }}",
            "result": {
                "nat64": {
                    "source": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "pool": [{"id": "{{ pool_id }}", "address": "{{ value }}"}],
                                },
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat64_translation_pool_description",
            "getval": re.compile(
                r"""
                ^set
                \s+nat64
                \s+source
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+pool
                \s+(?P<pool_id>\d+)
                \s+description
                \s+(?P<value>.+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat64 source rule {{ id }} translation pool {{ pool_id }} description {{ value }}",
            "result": {
                "nat64": {
                    "source": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "pool": [{"id": "{{ pool_id }}", "description": "{{ value }}"}],
                                },
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat64_translation_pool_disable",
            "getval": re.compile(
                r"""
                ^set
                \s+nat64
                \s+source
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+pool
                \s+(?P<pool_id>\d+)
                \s+disable
                $""",
                re.VERBOSE,
            ),
            "setval": "nat64 source rule {{ id }} translation pool {{ pool_id }} disable",
            "result": {
                "nat64": {
                    "source": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "pool": [{"id": "{{ pool_id }}", "disable": True}],
                                },
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat64_translation_pool_port",
            "getval": re.compile(
                r"""
                ^set
                \s+nat64
                \s+source
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+pool
                \s+(?P<pool_id>\d+)
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat64 source rule {{ id }} translation pool {{ pool_id }} port {{ value }}",
            "result": {
                "nat64": {
                    "source": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "pool": [{"id": "{{ pool_id }}", "port": "{{ value }}"}],
                                },
                            },
                        ],
                    },
                },
            },
        },
        {
            "name": "nat64_translation_pool_protocol",
            "getval": re.compile(
                r"""
                ^set
                \s+nat64
                \s+source
                \s+rule
                \s+(?P<id>\S+)
                \s+translation
                \s+pool
                \s+(?P<pool_id>\d+)
                \s+protocol
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat64 source rule {{ id }} translation pool {{ pool_id }} protocol {{ value }}",
            "result": {
                "nat64": {
                    "source": {
                        "rule": [
                            {
                                "id": "{{ id }}",
                                "translation": {
                                    "pool": [{"id": "{{ pool_id }}", "protocol": "{{ value }}"}],
                                },
                            },
                        ],
                    },
                },
            },
        },
    ]

    # fmt: on
