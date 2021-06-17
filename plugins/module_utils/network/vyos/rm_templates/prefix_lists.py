# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Prefix_lists parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)

class Prefix_listsTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Prefix_listsTemplate, self).__init__(lines=lines, tmplt=self, module=module)

        # set policy prefix-list pl1 rule 3 action 'permit'
        # set policy prefix-list pl1 rule 3 description 'Test policy'
        # set policy prefix-list pl1 rule 3 prefix '10.0.0.0/24'
        # set policy prefix-list6 pl61 rule 3 action 'permit'
        # set policy prefix-list6 pl61 rule 3 prefix '2:A::4:78/62'


    # fmt: off
    PARSERS = [
        {
            "name": "name",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                """, re.VERBOSE),
            "setval": "policy prefix-list {{ name }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                        }
                    }
                }
            },
            "shared": True
        },
        # {
        #     "name": "key_b",
        #     "getval": re.compile(
        #         r"""
        #         \s+key_b\s(?P<key_b>\S+)
        #         $""", re.VERBOSE),
        #     "setval": "",
        #     "result": {
        #     },
        # },
    ]
    # fmt: on
