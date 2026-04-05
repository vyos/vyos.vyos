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
            "result": {"cgnat": {"log_allocation": True}},
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
                "cgnat": {
                    "pool": {
                        "external": [
                            {
                                "name": "{{ name }}",
                                "ranges": ["{{ range }}"],
                                "seq": "{{ seq }}",
                            },
                        ],
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
                "cgnat": {
                    "pool": {
                        "external": [
                            {
                                "name": "{{ name }}",
                                "per_user_limit_port": "{{ limit }}",
                            },
                        ],
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
                "cgnat": {
                    "pool": {
                        "internal": [
                            {
                                "name": "{{ name }}",
                                "ranges": ["{{ range }}"],
                            },
                        ],
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
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+description
                \s+(?P<description>.+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} description {{ description }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {"description": "{{ description }}"},
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
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+protocol
                \s+(?P<protocol>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} protocol {{ protocol }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {"protocol": "{{ protocol }}"},
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
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+disable
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} disable",
            "result": {"{{ type }}": {"rule": {"{{ rule }}": {"disable": True}}}},
        },
        {
            "name": "nat_type_exclude",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+exclude
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} exclude",
            "result": {"{{ type }}": {"rule": {"{{ rule }}": {"exclude": True}}}},
        },
        {
            "name": "nat_type_log",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+log
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} log",
            "result": {"{{ type }}": {"rule": {"{{ rule }}": {"log": True}}}},
        },

        # address (destination/source)
        {
            "name": "nat_type_address",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+(?P<atype>destination|source)
                \s+address
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} {{ atype }} address {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "{{ atype }}": {"address": "{{ value }}"},
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+(?P<atype>destination|source)
                \s+fqdn
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} {{ atype }} fqdn {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "{{ atype }}": {"fqdn": "{{ value }}"},
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+(?P<atype>destination|source)
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} {{ atype }} port {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "{{ atype }}": {"port": "{{ value }}"},
                        },
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
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+translation
                \s+address
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} translation address {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "translation": {"address": "{{ value }}"},
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+translation
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} translation port {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "translation": {"port": "{{ value }}"},
                        },
                    },
                },
            },
        },

        # inbound interface
        {
            "name": "nat_type_inbound_interface",
            "getval": re.compile(
                r"""
                ^set
                \s+nat
                \s+(?P<type>destination|source|static)
                \s+rule
                \s+(?P<rule>\S+)
                \s+inbound-interface
                \s+(?P<mode>group|name)
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} inbound-interface {{ mode }} {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "inbound_interface": {
                                "{{ mode }}": "{{ value }}",
                            },
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+packet-type
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} packet-type {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {"packet_type": "{{ value }}"},
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+load-balance
                \s+backend
                \s+(?P<ip>\S+)
                \s+weight
                \s+(?P<weight>\d+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} load-balance backend {{ ip }} weight {{ weight }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "load_balance": {
                                "backend": {
                                    "ip": "{{ ip }}",
                                    "weight": "{{ weight }}",
                                },
                            },
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+load-balance
                \s+hash
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} load-balance hash {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "load_balance": {"hash": "{{ value }}"},
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+translation
                \s+options
                \s+(?P<opt>address-mapping|port-mapping)
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} translation options {{ opt }} {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "translation": {
                                "options": {
                                    "{{ opt }}": "{{ value }}",
                                },
                            },
                        },
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
                \s+nat
                \s+(?P<type>destination|source)
                \s+rule
                \s+(?P<rule>\S+)
                \s+translation
                \s+redirect
                \s+port
                \s+(?P<value>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "nat {{ type }} rule {{ rule }} translation redirect port {{ value }}",
            "result": {
                "{{ type }}": {
                    "rule": {
                        "{{ rule }}": {
                            "translation": {
                                "redirect_port": "{{ value }}",
                            },
                        },
                    },
                },
            },
        },

    ]
    # fmt: on
