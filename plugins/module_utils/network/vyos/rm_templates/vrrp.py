# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Bgp_global parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

# from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class VrrpTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(VrrpTemplate, self).__init__(
            lines=lines,
            tmplt=self,
            prefix=prefix,
            module=module,
        )

    # fmt: off
    PARSERS = [
        {
            "name": "disable",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \s(?P<disable>disable)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability disable",
            "result": {
                "disable": "{{ True if disable is defined }}",
            },
        },
        {
            "name": "vg_addr",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \saddress
                \s(?P<address>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} address {{address}}",
            "compval": "address",
            "result": {
                "group": "{{ group }}",
                "address": "{{ address }}",
            },
        },
        {
            "name": "vg_addr_addr_int",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \saddress
                \s(?P<address>\S+)
                \sinterface
                \s(?P<interface>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} address {{address}} interface {{interface}}",
            "compval": "interface",
            "result": {
                "group": "{{ group }}",
                "address": "{{ address }}",
                "interface": "{{ interface }}",
            },
        },
        {
            "name": "vg_excluded_addr",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sexcluded-address
                \s(?P<excluded_addr>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} excluded-address {{excluded_addr}}",
            "compval": "excluded_address",
            "result": {
                "group": "{{ group }}",
                "excluded_address": "{{ excluded_addr }}",
            },
        },
        {
            "name": "vg_excluded_addr_int",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sexcluded-address
                \s(?P<excluded_addr>\S+)
                \sinterface
                \s(?P<excluded_addr_int>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} excluded-address {{excluded_addr}} interface {{excluded_addr_interface}}",
            "compval": "excluded_address_interface",
            "result": {
                "group": "{{ group }}",
                "excluded_address_interface": "{{ excluded_address_int }}",
            },
        },
        {
            "name": "vg_priority",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \spriority
                \s(?P<priority>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} priority {{priority}}",
            "compval": "priority",
            "result": {
                "group": "{{ group }}",
                "priority": "{{ priority }}",
            },
        },
        {
            "name": "vg_advertise_interval",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sadvertise-interval
                \s(?P<adv_int>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} advertise-interval {{adv_int}}",
            "compval": "advertise_interval",
            "result": {
                "group": "{{ group }}",
                "advertise_interval": "{{ adv_int }}",
            },
        },
        {
            "name": "vg_description",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sdescription
                \s(?P<description>.*)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} description {{description}}",
            "compval": "description",
            "result": {
                "group": "{{ group }}",
                "description": "{{ description }}",
            },
        },
        {
            "name": "vg_vrid",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \svrid
                \s(?P<vrid>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} vrid {{vrid}}",
            "compval": "vrid",
            "result": {
                "group": "{{ group }}",
                "vrid": "{{ vrid }}",
            },
        },
        {
            "name": "vg_no_preempt",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \s(?P<np>no-preempt)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} no-preempt",
            "compval": "no_preempt",
            "result": {
                "group": "{{ group }}",
                "no_preempt": "{{ True if np is defined }}",
            },
        },
        {
            "name": "vg_preempt_delay",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \spreempt-delay
                \s(?P<prd>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} preempt-delay {{prd}}",
            "compval": "preempt_delay",
            "result": {
                "group": "{{ group }}",
                "preempt-delay": "{{ prd }}",
            },
        },
        {
            "name": "vg_authentication_password",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sauthentication
                \spassword
                \s(?P<pass>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} authentication password {{pass}}",
            "compval": "pass",
            "result": {
                "group": "{{ group }}",
                "authentication": {
                    "password": "{{ pass }}",
                },
            },
        },
        {
            "name": "vg_authentication_type",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sauthentication
                \stype
                \s(?P<type>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} authentication type {{type}}",
            "compval": "type",
            "result": {
                "group": "{{ group }}",
                "authentication": {
                    "password": "{{ type }}",
                },
            },
        },
        {
            "name": "vg_rfc3768",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \srfc3768-compatibility
                \s(?P<rfc3768>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} rfc3768-compatibility {{rfc3768}}",
            "compval": "rfc3768_compatibility",
            "result": {
                "group": "{{ group }}",
                "rfc3768_compatibility": "{{ True if rfc3768 is defined }}",
            },
        },
        {
            "name": "vg_garp_interval",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sgarp
                \sinterval
                \s(?P<garp_int>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} garp interval {{garp_int}}",
            "compval": "interval",
            "result": {
                "group": "{{ group }}",
                "garp": {
                        "interval": "{{ garp_int}}",
                },
            },
        },
        {
            "name": "vg_garp_master_delay",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sgarp
                \smaster-delay
                \s(?P<garp_mdelay>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} garp master-delay {{garp_mdelay}}",
            "compval": "master_delay",
            "result": {
                "group": "{{ group }}",
                "garp": {
                        "master_delay": "{{ garp_mdelay }}",
                },
            },
        },
        {
            "name": "vg_garp_master_refresh",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sgarp
                \smaster-refresh
                \s(?P<garp_mrefresh>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} garp master-refresh {{garp_mrefresh}}",
            "compval": "master_refresh",
            "result": {
                "group": "{{ group }}",
                "garp": {
                        "master_refresh": "{{ garp_mrefresh }}",
                },
            },
        },
        {
            "name": "vg_garp_master_refresh_repeat",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sgarp
                \smaster-refresh-repeat
                \s(?P<garp_mrefresh_repeat>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} garp master-refresh-repeat {{garp_mrefresh_repeat}}",
            "compval": "master_refresh_repeat",
            "result": {
                "group": "{{ group }}",
                "garp": {
                        "master_refresh_repeat": "{{ garp_mrefresh_repeat }}",
                },
            },
        },
        {
            "name": "vg_garp_master_repeat",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sgroup
                \s(?P<group>\S+)
                \sgarp
                \smaster-repeat
                \s(?P<garp_mrepeat>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp group {{group}} garp master-repeat {{garp_mrepeat}}",
            "compval": "master_repeat",
            "result": {
                "group": "{{ group }}",
                "garp": {
                        "master_repeat": "{{ garp_mrepeat }}",
                },
            },
        },
        {
            "name": "vg_gp_version",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sversion
                \s(?P<version>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters version {{version}}",
            "compval": "global_parameters.version",
            "result": {
                "global_parameters": {
                    "version": "{{ version }}",
                },
            },
        },
        {
            "name": "gp_startup_delay",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sstartup-delay
                \s(?P<startup_delay>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters startup-delay {{startup_delay}}",
            "compval": "global_parameters.startup_delay",
            "result": {
                "global_parameters": {
                    "startup_delay": "{{ startup_delay }}",
                },
            },
        },
        {
            "name": "gp_garp_interval",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sgarp
                \sinterval
                \s(?P<interval>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters garp interval {{interval}}",
            "compval": "global_parameters.garp.interval",
            "result": {
                "global_parameters": {
                    "garp": {
                        "interval": "{{ interval }}",
                    },
                },
            },
        },
        {
            "name": "gp_garp_master_delay",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sgarp
                \smaster-delay
                \s(?P<master_delay>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters garp master-delay {{master_delay}}",
            "compval": "global_parameters.garp.master_delay",
            "result": {
                "global_parameters": {
                    "garp": {
                        "master_delay": "{{ master_delay }}",
                    },
                },
            },
        },
        {
            "name": "gp_garp_master_refresh",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sgarp
                \smaster-refresh
                \s(?P<master_refresh>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters garp master-refresh {{master_refresh}}",
            "compval": "global_parameters.garp.master_refresh",
            "result": {
                "global_parameters": {
                    "garp": {
                        "master_refresh": "{{ master_refresh }}",
                    },
                },
            },
        },
        {
            "name": "gp_garp_master_refresh_repeat",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sgarp
                \smaster-refresh-repeat
                \s(?P<master_refresh_repeat>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters garp master-refresh_repeat {{master_refresh_repeat}}",
            "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "global_parameters": {
                    "garp": {
                        "master_refresh_repeat": "{{ master_refresh_repeat }}",
                    },
                },
            },
        },
        {
            "name": "gp_garp_master_repeat",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \sglobal-parameters
                \sgarp
                \smaster-refresh-repeat
                \s(?P<master_refresh_repeat>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp global-parameters garp master-refresh-repeat {{master_refresh_repeat}}",
            "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "global_parameters": {
                    "garp": {
                        "master_refresh_repeat": "{{ master_refresh_repeat }}",
                    },
                },
            },
        },
    ]
    # fmt: on
