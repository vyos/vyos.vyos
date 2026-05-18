# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def _tmplt_cgnat_pool_ext(config_data):
    config_data = config_data["nat"]["cgnat"]["pool"]["external"]

    command = []

    for m, pool in config_data.items():
        name = pool["name"]
        base_cmd = f"nat cgnat pool external {name}"

        if pool.get("external_port_range") is not None:
            command.append(
                f"{base_cmd} external-port-range " f"{pool['external_port_range']}",
            )

        per_user = pool.get("per_user_limit")
        if per_user and per_user.get("port") is not None:
            command.append(
                f"{base_cmd} per-user-limit port " f"{per_user['port']}",
            )

        for rng in pool.get("range", []):
            if isinstance(rng, dict):
                cmd = f"{base_cmd} range {rng['address']}"

                if rng.get("seq") is not None:
                    cmd += f" seq {rng['seq']}"

                command.append(cmd)

            else:
                command.append(f"{base_cmd} range {rng}")

    return command


def _tmplt_cgnat_pool_int(config_data):
    config_data = config_data["nat"]["cgnat"]["pool"]["internal"]

    command = []

    for _, pool in config_data.items():
        name = pool["name"]
        base_cmd = f"nat cgnat pool internal {name}"

        for rng in pool.get("range", []):
            command.append(f"{base_cmd} range {rng['address']}")

    return command


def _render_cgnat_rule_pool(config_data, section):
    rules = config_data["nat"]["cgnat"]["rule"]

    command = []

    for rule in rules:
        rid = rule["id"]

        data = rule.get(section)
        if data and data.get("pool") is not None:
            command.append(
                f"nat cgnat rule {rid} {section} pool {data['pool']}",
            )

    return command


def _tmplt_cgnat_rule_source_pool(config_data):
    return _render_cgnat_rule_pool(config_data, "source")


def _tmplt_cgnat_rule_translation_pool(config_data):
    return _render_cgnat_rule_pool(config_data, "translation")


class NatTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(NatTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "nat.cgnat.log_allocation",
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
            "name": "nat.cgnat.pool.external",
            "getval": re.compile(
                r"""
                ^set\s+nat\s+cgnat\s+pool\s+external\s+(?P<name>\S+)
                (?:
                \s+external-port-range\s+(?P<port_range>\S+)
                | \s+range\s+(?P<range>\S+)(?:\s+seq\s+(?P<seq>\d+))?
                | \s+per-user-limit\s+port\s+(?P<limit>\d+)
                )?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_cgnat_pool_ext,
            "result": {
                "nat": {
                    "cgnat": {
                        "pool": {
                            "external": {
                                "{{ name }}": {
                                    "name": "{{ name }}",
                                    "external_port_range": "{{ port_range }}",
                                    "per_user_limit": {
                                        "port": "{{ limit }}",
                                    },
                                    "range": [
                                        {
                                            "address": "{{ range }}",
                                            "seq": "{{ seq }}",
                                        },
                                    ],
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "nat.cgnat.pool.internal",
            "getval": re.compile(
                r"""
                ^set\s+nat\s+cgnat\s+pool\s+internal\s+(?P<name>\S+)
                (?:
                \s+range\s+(?P<range>\S+)
                )?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_cgnat_pool_int,
            "result": {
                "nat": {
                    "cgnat": {
                        "pool": {
                            "internal": {
                                "{{ name }}": {
                                    "name": "{{ name }}",
                                    "range": [
                                        {
                                            "address": "{{ range }}",
                                        },
                                    ],
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "nat.cgnat.rule.source.pool",
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
            "setval": _tmplt_cgnat_rule_source_pool,
            "result": {
                "nat": {
                    "cgnat": {
                        "rule": {
                            "{{ id }}": {
                                "id": "{{ id }}",
                                "source": {"pool": "{{ pool }}"},
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "nat.cgnat.rule.translation.pool",
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
            "setval": _tmplt_cgnat_rule_translation_pool,
            "result": {
                "nat": {
                    "cgnat": {
                        "rule": {
                            "{{ id }}": {
                                "id": "{{ id }}",
                                "translation": {"pool": "{{ pool }}"},
                            },
                        },
                    },
                },
            },
        },

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
                                "inbound_interface": {"name": "{{ value }}"},
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
