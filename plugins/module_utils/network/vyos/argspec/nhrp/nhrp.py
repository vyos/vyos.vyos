# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The arg spec for the vyos_nhrp module
"""


class NhrpArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_nhrp module"""

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "tunnels": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str", "required": True},
                        "authentication": {"type": "str", "no_log": True},
                        "holdtime": {"type": "int"},
                        "mtu": {"type": "int"},
                        "network_id": {"type": "int"},
                        "multicast": {"type": "list", "elements": "str"},
                        "redirect": {"type": "bool"},
                        "shortcut": {"type": "bool"},
                        "registration_no_unique": {"type": "bool"},
                        "map": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "tunnel_ip": {"type": "str", "required": True},
                                "nbma": {"type": "str", "required": True},
                            },
                        },
                        "nhs": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "tunnel_ip": {"type": "str", "required": True},
                                "nbma": {"type": "list", "elements": "str", "required": True},
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
