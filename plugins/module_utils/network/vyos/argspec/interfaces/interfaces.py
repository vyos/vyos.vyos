#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The arg spec for the vyos_interfaces module
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


class InterfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_interfaces module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "description": {"type": "str"},
                "duplex": {
                    "choices": ["full", "half", "auto"],
                    "type": "str",
                },
                "enabled": {
                    "aliases": ["enable"],
                    "default": True,
                    "type": "bool",
                },
                "mtu": {"type": "int"},
                "name": {"required": True, "type": "str"},
                "speed": {
                    "choices": [
                        "auto",
                        "10",
                        "100",
                        "1000",
                        "2500",
                        "10000",
                    ],
                    "type": "str",
                },
                "vifs": {
                    "elements": "dict",
                    "options": {
                        "description": {"type": "str"},
                        "enabled": {
                            "aliases": ["enable"],
                            "default": True,
                            "type": "bool",
                        },
                        "mtu": {"type": "int"},
                        "vlan_id": {"type": "int"},
                        "vrf": {"type": "str"},
                    },
                    "type": "list",
                },
                "vrf": {"type": "str"},
                "tunnel": {
                    "type": "dict",
                    "options": {
                        "encapsulation": {
                            "type": "str",
                            "choices": [
                                "erspan",
                                "gre",
                                "gretap",
                                "ip6erspan",
                                "ip6gre",
                                "ip6gretap",
                                "ip6ip6",
                                "ipip",
                                "ipip6",
                                "sit",
                            ],
                        },
                        "source_address": {"type": "str"},
                        "source_interface": {"type": "str"},
                        "remote": {"type": "str"},
                        "enable_multicast": {"type": "bool"},
                        "parameters": {
                            "type": "dict",
                            "options": {
                                "ip": {
                                    "type": "dict",
                                    "options": {
                                        "key": {"type": "int", "no_log": False},
                                        "ttl": {"type": "int"},
                                        "tos": {"type": "str"},
                                        "no_pmtu_discovery": {"type": "bool"},
                                        "ignore_df": {"type": "bool"},
                                    },
                                },
                            },
                        },
                    },
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
                "rendered",
                "gathered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
