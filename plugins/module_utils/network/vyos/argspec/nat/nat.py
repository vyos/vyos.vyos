# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The arg spec for the vyos_nat module
"""


class NatArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_nat module"""

    argument_spec = {
        "config": {
            "type": "dict",
            "nat": {
                "type": "dict",
                "options": {
                    "cgnat": {
                        "type": "dict",
                        "options": {
                            "log_allocation": {
                                "type": "bool",
                            },
                            "pool": {
                                "type": "dict",
                                "options": {
                                    "external": {
                                        "type": "list",
                                        "elements": "dict",
                                        "options": {
                                            "name": {
                                                "type": "str",
                                                "required": True,
                                            },
                                            "external_port_range": {
                                                "type": "str",
                                            },
                                            "per_user_limit": {
                                                "type": "dict",
                                                "options": {
                                                    "port": {
                                                        "type": "str",
                                                    },
                                                },
                                            },
                                            "range": {
                                                "type": "list",
                                                "elements": "str",
                                            },
                                        },
                                    },
                                    "internal": {
                                        "type": "list",
                                        "elements": "dict",
                                        "options": {
                                            "name": {
                                                "type": "str",
                                                "required": True,
                                            },
                                            "range": {
                                                "type": "list",
                                                "elements": "str",
                                            },
                                        },
                                    },
                                },
                            },
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "source": {
                                        "type": "dict",
                                        "options": {
                                            "pool": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "pool": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "destination": {
                        "type": "dict",
                        "options": {
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "description": {
                                        "type": "str",
                                    },
                                    "protocol": {
                                        "type": "str",
                                    },
                                    "packet_type": {
                                        "type": "str",
                                    },
                                    "exclude": {
                                        "type": "bool",
                                    },
                                    "log": {
                                        "type": "bool",
                                    },
                                    "disable": {
                                        "type": "bool",
                                    },
                                    "inbound_interface": {
                                        "type": "dict",
                                        "options": {
                                            "name": {
                                                "type": "str",
                                            },
                                            "group": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "destination": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "fqdn": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                            "address_group": {
                                                "type": "str",
                                            },
                                            "domain_group": {
                                                "type": "str",
                                            },
                                            "mac_group": {
                                                "type": "str",
                                            },
                                            "network_group": {
                                                "type": "str",
                                            },
                                            "port_group": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                            "redirect_port": {
                                                "type": "str",
                                            },
                                            "address_mapping": {
                                                "type": "str",
                                                "choices": [
                                                    "random",
                                                    "persistent",
                                                ],
                                            },
                                            "port_mapping": {
                                                "type": "str",
                                                "choices": [
                                                    "random",
                                                    "none",
                                                ],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "source": {
                        "type": "dict",
                        "options": {
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "description": {
                                        "type": "str",
                                    },
                                    "protocol": {
                                        "type": "str",
                                    },
                                    "packet_type": {
                                        "type": "str",
                                    },
                                    "exclude": {
                                        "type": "bool",
                                    },
                                    "log": {
                                        "type": "bool",
                                    },
                                    "disable": {
                                        "type": "bool",
                                    },
                                    "outbound_interface": {
                                        "type": "dict",
                                        "options": {
                                            "name": {
                                                "type": "str",
                                            },
                                            "group": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "destination": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "fqdn": {
                                                "type": "str",
                                            },
                                            "address_group": {
                                                "type": "str",
                                            },
                                            "domain_group": {
                                                "type": "str",
                                            },
                                            "mac_group": {
                                                "type": "str",
                                            },
                                            "network_group": {
                                                "type": "str",
                                            },
                                            "port_group": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "source": {
                                        "type": "dict",
                                        "options": {
                                            "address": {"type": "str"},
                                            "fqdn": {"type": "str"},
                                            "port": {"type": "str"},
                                            "address_group": {"type": "str"},
                                            "domain_group": {"type": "str"},
                                            "mac_group": {"type": "str"},
                                            "network_group": {"type": "str"},
                                            "port_group": {"type": "str"},
                                        },
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                            "address_mapping": {
                                                "type": "str",
                                                "choices": [
                                                    "random",
                                                    "persistent",
                                                ],
                                            },
                                            "port_mapping": {
                                                "type": "str",
                                                "choices": [
                                                    "random",
                                                    "none",
                                                ],
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "static": {
                        "type": "dict",
                        "options": {
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "description": {
                                        "type": "str",
                                    },
                                    "destination": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "inbound_interface": {
                                        "type": "str",
                                    },
                                    "log": {
                                        "type": "bool",
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "nat64": {
                "type": "dict",
                "options": {
                    "source": {
                        "type": "dict",
                        "options": {
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "description": {
                                        "type": "str",
                                    },
                                    "disable": {
                                        "type": "bool",
                                    },
                                    "match": {
                                        "type": "dict",
                                        "options": {
                                            "mark": {
                                                "type": "int",
                                            },
                                        },
                                    },
                                    "source": {
                                        "type": "dict",
                                        "options": {
                                            "prefix": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "pool": {
                                                "type": "list",
                                                "elements": "dict",
                                                "options": {
                                                    "id": {
                                                        "type": "int",
                                                        "required": True,
                                                    },
                                                    "address": {
                                                        "type": "str",
                                                    },
                                                    "description": {
                                                        "type": "str",
                                                    },
                                                    "disable": {
                                                        "type": "bool",
                                                    },
                                                    "port": {
                                                        "type": "str",
                                                    },
                                                    "protocol": {
                                                        "type": "str",
                                                        "choices": [
                                                            "icmp",
                                                            "tcp",
                                                            "udp",
                                                        ],
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "nat66": {
                "type": "dict",
                "options": {
                    "destination": {
                        "type": "dict",
                        "options": {
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "description": {
                                        "type": "str",
                                    },
                                    "destination": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "disable": {
                                        "type": "bool",
                                    },
                                    "exclude": {
                                        "type": "bool",
                                    },
                                    "inbound_interface": {
                                        "type": "dict",
                                        "options": {
                                            "name": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "log": {
                                        "type": "bool",
                                    },
                                    "protocol": {
                                        "type": "str",
                                    },
                                    "source": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "source": {
                        "type": "dict",
                        "options": {
                            "rule": {
                                "type": "list",
                                "elements": "dict",
                                "options": {
                                    "id": {
                                        "type": "int",
                                        "required": True,
                                    },
                                    "description": {
                                        "type": "str",
                                    },
                                    "destination": {
                                        "type": "dict",
                                        "options": {
                                            "port": {
                                                "type": "str",
                                            },
                                            "prefix": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "disable": {
                                        "type": "bool",
                                    },
                                    "exclude": {
                                        "type": "bool",
                                    },
                                    "log": {
                                        "type": "bool",
                                    },
                                    "outbound_interface": {
                                        "type": "dict",
                                        "options": {
                                            "name": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "protocol": {
                                        "type": "str",
                                    },
                                    "source": {
                                        "type": "dict",
                                        "options": {
                                            "port": {
                                                "type": "str",
                                            },
                                            "prefix": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                    "translation": {
                                        "type": "dict",
                                        "options": {
                                            "address": {
                                                "type": "str",
                                            },
                                            "port": {
                                                "type": "str",
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "type": "str",
            "choices": [
                "deleted",
                "merged",
                "overridden",
                "replaced",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
