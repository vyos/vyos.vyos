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
        # policy prefix-list <list-name>
        {
            "name": "name",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }}",
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
            # "shared": True
        },

        # policy prefix-list <list-name> description <desc>
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \sdescription\s(?P<description>.+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}"
                        }
                    }
                }
            },
        },

        # policy prefix-list <list-name> rule <rule-num>
        {
            "name": "rules",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \srule\s(?P<rule>\d+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }} rule {{ rule }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}",
                            "rules": {
                                "{{ rule }}": {
                                    "id": "{{ rule }}"
                                }
                            }
                        }
                    }
                }
            },
        },

        # policy prefix-list <list-name> rule <rule-num> action
        {
            "name": "action",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \srule\s(?P<rule>\d+)
                \saction\s(?P<action>'?permit'?|'?deny'?)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }} rule {{ rule }} action {{ action }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}",
                            "rules": {
                                "{{ rule }}": {
                                    "id": "{{ rule }}",
                                    "action": "{{ action }}"
                                }
                            }
                        }
                    }
                }
            },
        },

        # policy prefix-list <list-name> rule <rule-num> description <desc>
        {
            "name": "rule_description",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \srule\s(?P<rule>\d+)
                \sdescription\s(?P<rule_description>.+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }} rule {{ rule }} description {{ rule_description }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}",
                            "rules": {
                                "{{ rule }}": {
                                    "id": "{{ rule }}",
                                    "action": "{{ action }}",
                                    "description": "{{ rule_description }}"
                                }
                            }
                        }
                    }
                }
            },
        },

        # policy prefix-list <list-name> rule <rule-num> ge <value>
        {
            "name": "ge",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \srule\s(?P<rule>\d+)
                \sge\s(?P<ge>\d+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }} rule {{ rule }} ge {{ ge }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}",
                            "rules": {
                                "{{ rule }}": {
                                    "id": "{{ rule }}",
                                    "action": "{{ action }}",
                                    "description": "{{ rule_description }}",
                                    "ge": "{{ ge }}"
                                }
                            }
                        }
                    }
                }
            },
        },

        # policy prefix-list <list-name> rule <rule-num> le <value>
        {
            "name": "le",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \srule\s(?P<rule>\d+)
                \sle\s(?P<le>\d+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }} rule {{ rule }} le {{ le }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}",
                            "rules": {
                                "{{ rule }}": {
                                    "id": "{{ rule }}",
                                    "action": "{{ action }}",
                                    "description": "{{ rule_description }}",
                                    "ge": "{{ ge }}",
                                    "le": "{{ le }}"
                                }
                            }
                        }
                    }
                }
            },
        },

        # policy prefix-list <list-name> rule <rule-num> prefix <ip>
        {
            "name": "prefix",
            "getval": re.compile(
                r"""
                ^set
                \spolicy
                \sprefix-(?P<afi>\S+)
                \s(?P<name>\S+)
                \srule\s(?P<rule>\d+)
                \sprefix\s(?P<prefix>\S+)
                $""", re.VERBOSE),
            "setval": "policy prefix-{{ 'list' if afi == 'ipv4' else 'list6' }} {{ name }} description {{ description }} rule {{ rule }} prefix {{ prefix }}",
            "result": {
                "{{ 'ipv4' if afi == 'list' else 'ipv6' }}": {
                    "afi": "{{ 'ipv4' if afi == 'list' else 'ipv6' }}",
                    "prefix_lists": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "description": "{{ description }}",
                            "rules": {
                                "{{ rule }}": {
                                    "id": "{{ rule }}",
                                    "action": "{{ action }}",
                                    "description": "{{ rule_description }}",
                                    "ge": "{{ ge }}",
                                    "le": "{{ le }}",
                                    "prefix": "{{ prefix }}"
                                }
                            }
                        }
                    }
                }
            },
        },
    ]
    # fmt: on
