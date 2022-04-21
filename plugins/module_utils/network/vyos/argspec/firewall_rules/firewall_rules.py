#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the vyos_firewall_rules module
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Firewall_rulesArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_firewall_rules module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "afi": {
                    "choices": ["ipv4", "ipv6"],
                    "required": True,
                    "type": "str",
                },
                "rule_sets": {
                    "elements": "dict",
                    "options": {
                        "default_action": {
                            "choices": ["drop", "reject", "accept"],
                            "type": "str",
                        },
                        "description": {"type": "str"},
                        "enable_default_log": {"type": "bool"},
                        "name": {"type": "str"},
                        "rules": {
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "choices": [
                                        "drop",
                                        "reject",
                                        "accept",
                                        "inspect",
                                    ],
                                    "type": "str",
                                },
                                "description": {"type": "str"},
                                "destination": {
                                    "options": {
                                        "address": {"type": "str"},
                                        "group": {
                                            "options": {
                                                "address_group": {
                                                    "type": "str"
                                                },
                                                "network_group": {
                                                    "type": "str"
                                                },
                                                "port_group": {"type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                        "port": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "disable": {
                                    "type": "bool",
                                    "aliases": ["disabled"],
                                },
                                "fragment": {
                                    "choices": [
                                        "match-frag",
                                        "match-non-frag",
                                    ],
                                    "type": "str",
                                },
                                "icmp": {
                                    "options": {
                                        "code": {"type": "int"},
                                        "type": {"type": "int"},
                                        "type_name": {
                                            "choices": [
                                                "any",
                                                "echo-reply",
                                                "destination-unreachable",
                                                "network-unreachable",
                                                "host-unreachable",
                                                "protocol-unreachable",
                                                "port-unreachable",
                                                "fragmentation-needed",
                                                "source-route-failed",
                                                "network-unknown",
                                                "host-unknown",
                                                "network-prohibited",
                                                "host-prohibited",
                                                "TOS-network-unreachable",
                                                "TOS-host-unreachable",
                                                "communication-prohibited",
                                                "host-precedence-violation",
                                                "precedence-cutoff",
                                                "source-quench",
                                                "redirect",
                                                "network-redirect",
                                                "host-redirect",
                                                "TOS-network-redirect",
                                                "TOS-host-redirect",
                                                "echo-request",
                                                "router-advertisement",
                                                "router-solicitation",
                                                "time-exceeded",
                                                "ttl-zero-during-transit",
                                                "ttl-zero-during-reassembly",
                                                "parameter-problem",
                                                "ip-header-bad",
                                                "required-option-missing",
                                                "timestamp-request",
                                                "timestamp-reply",
                                                "address-mask-request",
                                                "address-mask-reply",
                                                "ping",
                                                "pong",
                                                "ttl-exceeded",
                                            ],
                                            "type": "str",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "ipsec": {
                                    "choices": ["match-ipsec", "match-none"],
                                    "type": "str",
                                },
                                "limit": {
                                    "options": {
                                        "burst": {"type": "int"},
                                        "rate": {
                                            "options": {
                                                "number": {"type": "int"},
                                                "unit": {"type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "log": {
                                    "type": "str",
                                    "choices": ["enable", "disable"],
                                },
                                "number": {"required": True, "type": "int"},
                                "p2p": {
                                    "elements": "dict",
                                    "options": {
                                        "application": {
                                            "choices": [
                                                "all",
                                                "applejuice",
                                                "bittorrent",
                                                "directconnect",
                                                "edonkey",
                                                "gnutella",
                                                "kazaa",
                                            ],
                                            "type": "str",
                                        }
                                    },
                                    "type": "list",
                                },
                                "protocol": {"type": "str"},
                                "recent": {
                                    "options": {
                                        "count": {"type": "int"},
                                        "time": {"type": "int"},
                                    },
                                    "type": "dict",
                                },
                                "source": {
                                    "options": {
                                        "address": {"type": "str"},
                                        "group": {
                                            "options": {
                                                "address_group": {
                                                    "type": "str"
                                                },
                                                "network_group": {
                                                    "type": "str"
                                                },
                                                "port_group": {"type": "str"},
                                            },
                                            "type": "dict",
                                        },
                                        "mac_address": {"type": "str"},
                                        "port": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                                "state": {
                                    "options": {
                                        "established": {"type": "bool"},
                                        "invalid": {"type": "bool"},
                                        "new": {"type": "bool"},
                                        "related": {"type": "bool"},
                                    },
                                    "type": "dict",
                                },
                                "tcp": {
                                    "options": {"flags": {"type": "str"}},
                                    "type": "dict",
                                },
                                "time": {
                                    "options": {
                                        "monthdays": {"type": "str"},
                                        "startdate": {"type": "str"},
                                        "starttime": {"type": "str"},
                                        "stopdate": {"type": "str"},
                                        "stoptime": {"type": "str"},
                                        "utc": {"type": "bool"},
                                        "weekdays": {"type": "str"},
                                    },
                                    "type": "dict",
                                },
                            },
                            "type": "list",
                        },
                    },
                    "type": "list",
                },
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
