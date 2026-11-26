# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The arg spec for the vyos_vpp_acl module
"""

TCP_FLAGS = ["ack", "cwr", "ecn", "fin", "psh", "rst", "syn", "urg"]

IP_MATCH = {
    "type": "dict",
    "options": {
        "prefix": {"type": "str"},
        "port": {"type": "str"},
    },
}

BINDINGS = {
    "type": "list",
    "elements": "dict",
    "options": {
        "acl_tag": {"type": "int", "required": True},
        "tag_name": {"type": "str", "required": True},
    },
}


class Vpp_aclArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_vpp_acl module"""

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "ip": {
                    "type": "dict",
                    "options": {
                        "acls": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "description": {"type": "str"},
                                "rules": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "number": {"type": "int", "required": True},
                                        "action": {
                                            "type": "str",
                                            "choices": ["permit", "deny", "permit-reflect"],
                                        },
                                        "description": {"type": "str"},
                                        "protocol": {"type": "str"},
                                        "source": IP_MATCH,
                                        "destination": IP_MATCH,
                                        "tcp_flags": {
                                            "type": "dict",
                                            "options": {
                                                "is_set": {
                                                    "type": "list",
                                                    "elements": "str",
                                                    "choices": TCP_FLAGS,
                                                },
                                                "is_not_set": {
                                                    "type": "list",
                                                    "elements": "str",
                                                    "choices": TCP_FLAGS,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        "interfaces": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "input": BINDINGS,
                                "output": BINDINGS,
                            },
                        },
                    },
                },
                "mac": {
                    "type": "dict",
                    "options": {
                        "acls": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "description": {"type": "str"},
                                "rules": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "number": {"type": "int", "required": True},
                                        "action": {"type": "str", "choices": ["permit", "deny"]},
                                        "description": {"type": "str"},
                                        "prefix": {"type": "str"},
                                        "mac_address": {"type": "str"},
                                        "mac_mask": {"type": "str"},
                                    },
                                },
                            },
                        },
                        "interfaces": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "tag_name": {"type": "str"},
                            },
                        },
                    },
                },
            },
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
