# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Vpp_acl parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class Vpp_aclTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Vpp_aclTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix, module=module)

    # Device lines reach the parser with their quotes removed (see the facts class).
    # The first matching parser wins for each line, so the catch-alls of a level come
    # after the parsers for its options. Each parser's compval is relative to the entity
    # its setval renders: an ACL, a rule (with the ACL name as acl) or an interface.
    # fmt: off
    PARSERS = [
        # set vpp acl ip tag-name <name> description <text>
        {
            "name": "ip.description",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+description
                \s+(?P<value>.+?)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "description",
            "setval": "vpp acl ip tag-name {{ name }} description '{{ description }}'",
            "remval": "vpp acl ip tag-name {{ name }} description",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ value }}",
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> action <value>
        {
            "name": "ip.rule.action",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+action
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "action",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} action {{ action }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} action",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "action": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> description <value>
        {
            "name": "ip.rule.description",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+description
                \s+(?P<value>.+?)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "description",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} description '{{ description }}'",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} description",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "description": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> protocol <value>
        {
            "name": "ip.rule.protocol",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+protocol
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "protocol",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} protocol {{ protocol }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} protocol",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "protocol": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> source prefix <value>
        {
            "name": "ip.rule.source.prefix",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+source
                \s+prefix
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "source.prefix",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} source prefix {{ source.prefix }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} source prefix",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "source": {
                                        "prefix": "{{ value }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> source port <value>
        {
            "name": "ip.rule.source.port",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+source
                \s+port
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "source.port",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} source port {{ source.port }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} source port",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "source": {
                                        "port": "{{ value }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> destination prefix <value>
        {
            "name": "ip.rule.destination.prefix",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+destination
                \s+prefix
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "destination.prefix",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} destination prefix {{ destination.prefix }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} destination prefix",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "destination": {
                                        "prefix": "{{ value }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> destination port <value>
        {
            "name": "ip.rule.destination.port",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+destination
                \s+port
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "destination.port",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} destination port {{ destination.port }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }} destination port",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "destination": {
                                        "port": "{{ value }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> tcp-flags is-set <flag>  (one line per flag)
        {
            "name": "ip.rule.tcp_flags.is_set",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+tcp-flags
                \s+is-set
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "tcp_flags.is_set",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} tcp-flags is-set {{ tcp_flags.is_set }}",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "tcp_flags": {
                                        "is_set": {
                                            "{{ value }}": "{{ value }}",
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n> tcp-flags is-not-set <flag>  (one line per flag)
        {
            "name": "ip.rule.tcp_flags.is_not_set",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+tcp-flags
                \s+is-not-set
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "tcp_flags.is_not_set",
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }} tcp-flags is-not-set {{ tcp_flags.is_not_set }}",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "tcp_flags": {
                                        "is_not_set": {
                                            "{{ value }}": "{{ value }}",
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip tag-name <name> rule <n>  (any other rule line)
        {
            "name": "ip.rule",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "vpp acl ip tag-name {{ acl }} rule {{ number }}",
            "remval": "vpp acl ip tag-name {{ acl }} rule {{ number }}",
            "result": {
                "ip": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip interface <if> input acl-tag <n> tag-name <acl>  (compared one acl-tag at a time)
        {
            "name": "ip.interface.input",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+interface
                \s+(?P<name>\S+)
                \s+input
                \s+acl-tag
                \s+(?P<acl_tag>\d+)
                \s+tag-name
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "input",
            "setval": "vpp acl ip interface {{ name }} input acl-tag {{ input.acl_tag }} tag-name {{ input.tag_name }}",
            "remval": "vpp acl ip interface {{ name }} input acl-tag {{ input.acl_tag }}",
            "result": {
                "ip": {
                    "interfaces": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "input": {
                                "{{ acl_tag }}": {
                                    "acl_tag": "{{ acl_tag }}",
                                    "tag_name": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip interface <if> output acl-tag <n> tag-name <acl>  (compared one acl-tag at a time)
        {
            "name": "ip.interface.output",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+interface
                \s+(?P<name>\S+)
                \s+output
                \s+acl-tag
                \s+(?P<acl_tag>\d+)
                \s+tag-name
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "output",
            "setval": "vpp acl ip interface {{ name }} output acl-tag {{ output.acl_tag }} tag-name {{ output.tag_name }}",
            "remval": "vpp acl ip interface {{ name }} output acl-tag {{ output.acl_tag }}",
            "result": {
                "ip": {
                    "interfaces": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "output": {
                                "{{ acl_tag }}": {
                                    "acl_tag": "{{ acl_tag }}",
                                    "tag_name": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl ip interface <if>  (any other interface line)
        {
            "name": "ip.interface",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+interface
                \s+(?P<name>\S+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "vpp acl ip interface {{ name }}",
            "remval": "vpp acl ip interface {{ name }}",
            "result": {"ip": {"interfaces": {"{{ name }}": {"name": "{{ name }}"}}}},
        },
        # set vpp acl ip tag-name <name>  (any other ACL line)
        {
            "name": "ip.acl",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+ip
                \s+tag-name
                \s+(?P<name>\S+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "vpp acl ip tag-name {{ name }}",
            "remval": "vpp acl ip tag-name {{ name }}",
            "result": {"ip": {"acls": {"{{ name }}": {"name": "{{ name }}"}}}},
        },
        # set vpp acl mac tag-name <name> description <text>
        {
            "name": "mac.description",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+description
                \s+(?P<value>.+?)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "description",
            "setval": "vpp acl mac tag-name {{ name }} description '{{ description }}'",
            "remval": "vpp acl mac tag-name {{ name }} description",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ value }}",
                        },
                    },
                },
            },
        },
        # set vpp acl mac tag-name <name> rule <n> action <value>
        {
            "name": "mac.rule.action",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+action
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "action",
            "setval": "vpp acl mac tag-name {{ acl }} rule {{ number }} action {{ action }}",
            "remval": "vpp acl mac tag-name {{ acl }} rule {{ number }} action",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "action": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl mac tag-name <name> rule <n> description <value>
        {
            "name": "mac.rule.description",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+description
                \s+(?P<value>.+?)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "description",
            "setval": "vpp acl mac tag-name {{ acl }} rule {{ number }} description '{{ description }}'",
            "remval": "vpp acl mac tag-name {{ acl }} rule {{ number }} description",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "description": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl mac tag-name <name> rule <n> prefix <value>
        {
            "name": "mac.rule.prefix",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+prefix
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "prefix",
            "setval": "vpp acl mac tag-name {{ acl }} rule {{ number }} prefix {{ prefix }}",
            "remval": "vpp acl mac tag-name {{ acl }} rule {{ number }} prefix",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "prefix": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl mac tag-name <name> rule <n> mac-address <value>
        {
            "name": "mac.rule.mac_address",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+mac-address
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "mac_address",
            "setval": "vpp acl mac tag-name {{ acl }} rule {{ number }} mac-address {{ mac_address }}",
            "remval": "vpp acl mac tag-name {{ acl }} rule {{ number }} mac-address",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "mac_address": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl mac tag-name <name> rule <n> mac-mask <value>
        {
            "name": "mac.rule.mac_mask",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                \s+mac-mask
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "mac_mask",
            "setval": "vpp acl mac tag-name {{ acl }} rule {{ number }} mac-mask {{ mac_mask }}",
            "remval": "vpp acl mac tag-name {{ acl }} rule {{ number }} mac-mask",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                    "mac_mask": "{{ value }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl mac tag-name <name> rule <n>  (any other rule line)
        {
            "name": "mac.rule",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                \s+rule
                \s+(?P<number>\d+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "vpp acl mac tag-name {{ acl }} rule {{ number }}",
            "remval": "vpp acl mac tag-name {{ acl }} rule {{ number }}",
            "result": {
                "mac": {
                    "acls": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "rules": {
                                "{{ number }}": {
                                    "number": "{{ number }}",
                                },
                            },
                        },
                    },
                },
            },
        },
        # set vpp acl mac interface <if> tag-name <acl>
        {
            "name": "mac.interface.tag_name",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+interface
                \s+(?P<name>\S+)
                \s+tag-name
                \s+(?P<value>\S+)
                \s*$""",
                re.VERBOSE,
            ),
            "compval": "tag_name",
            "setval": "vpp acl mac interface {{ name }} tag-name {{ tag_name }}",
            "remval": "vpp acl mac interface {{ name }} tag-name",
            "result": {
                "mac": {
                    "interfaces": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "tag_name": "{{ value }}",
                        },
                    },
                },
            },
        },
        # set vpp acl mac interface <if>  (any other interface line)
        {
            "name": "mac.interface",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+interface
                \s+(?P<name>\S+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "vpp acl mac interface {{ name }}",
            "remval": "vpp acl mac interface {{ name }}",
            "result": {"mac": {"interfaces": {"{{ name }}": {"name": "{{ name }}"}}}},
        },
        # set vpp acl mac tag-name <name>  (any other ACL line)
        {
            "name": "mac.acl",
            "getval": re.compile(
                r"""
                ^set
                \s+vpp
                \s+acl
                \s+mac
                \s+tag-name
                \s+(?P<name>\S+)
                (?:\s.*)?$""",
                re.VERBOSE,
            ),
            "setval": "vpp acl mac tag-name {{ name }}",
            "remval": "vpp acl mac tag-name {{ name }}",
            "result": {"mac": {"acls": {"{{ name }}": {"name": "{{ name }}"}}}},
        },
    ]
    # fmt: on
