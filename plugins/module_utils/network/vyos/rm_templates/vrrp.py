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

    def _tmplt_vsrvs(config_data):
        config_data = config_data["virtual-server"]
        command = []
        # cmd = "service snmp v3 group {group}".format(**config_data)
        # if "mode" in config_data:
        #     mode_cmd = cmd + " mode {mode}".format(**config_data)
        #     command.append(mode_cmd)
        # if "seclevel" in config_data:
        #     sec_cmd = cmd + " seclevel {seclevel}".format(**config_data)
        #     command.append(sec_cmd)
        # if "view" in config_data:
        #     view_cmd = cmd + " view {view}".format(**config_data)
        #     command.append(view_cmd)
        return command

    def _tmplt_vsrvs_rsrv(config_data):
        config_data = config_data["virtual-server"]["real_servers"]
        command = []
        # cmd = "service snmp v3 group {group}".format(**config_data)
        # if "mode" in config_data:
        #     mode_cmd = cmd + " mode {mode}".format(**config_data)
        #     command.append(mode_cmd)
        # if "seclevel" in config_data:
        #     sec_cmd = cmd + " seclevel {seclevel}".format(**config_data)
        #     command.append(sec_cmd)
        # if "view" in config_data:
        #     view_cmd = cmd + " view {view}".format(**config_data)
        #     command.append(view_cmd)
        return command

    def _tmplt_sgroup_hc(config_data):
        config_data = config_data["sync-group"]["health-check"]
        command = []
        # cmd = "service snmp v3 group {group}".format(**config_data)
        # if "mode" in config_data:
        #     mode_cmd = cmd + " mode {mode}".format(**config_data)
        #     command.append(mode_cmd)
        # if "seclevel" in config_data:
        #     sec_cmd = cmd + " seclevel {seclevel}".format(**config_data)
        #     command.append(sec_cmd)
        # if "view" in config_data:
        #     view_cmd = cmd + " view {view}".format(**config_data)
        #     command.append(view_cmd)
        return command

    def _tmplt_sgroup_ts(config_data):
        config_data = config_data["sync-group"]["transition-script"]
        command = []
        # cmd = "service snmp v3 group {group}".format(**config_data)
        # if "mode" in config_data:
        #     mode_cmd = cmd + " mode {mode}".format(**config_data)
        #     command.append(mode_cmd)
        # if "seclevel" in config_data:
        #     sec_cmd = cmd + " seclevel {seclevel}".format(**config_data)
        #     command.append(sec_cmd)
        # if "view" in config_data:
        #     view_cmd = cmd + " view {view}".format(**config_data)
        #     command.append(view_cmd)
        return command

    def _tmplt_vrrp_gp(config_data):
        config_data = config_data["vrrp"]["global-parameters"]
        command = []
        # cmd = "service snmp v3 group {group}".format(**config_data)
        # if "mode" in config_data:
        #     mode_cmd = cmd + " mode {mode}".format(**config_data)
        #     command.append(mode_cmd)
        # if "seclevel" in config_data:
        #     sec_cmd = cmd + " seclevel {seclevel}".format(**config_data)
        #     command.append(sec_cmd)
        # if "view" in config_data:
        #     view_cmd = cmd + " view {view}".format(**config_data)
        #     command.append(view_cmd)
        return command

    def _tmplt_vrrp_gp_garp(config_data):
        config_data = config_data["vrrp"]["global-parameters"]["garp"]
        command = []
        # cmd = "service snmp v3 group {group}".format(**config_data)
        # if "mode" in config_data:
        #     mode_cmd = cmd + " mode {mode}".format(**config_data)
        #     command.append(mode_cmd)
        # if "seclevel" in config_data:
        #     sec_cmd = cmd + " seclevel {seclevel}".format(**config_data)
        #     command.append(sec_cmd)
        # if "view" in config_data:
        #     view_cmd = cmd + " view {view}".format(**config_data)
        #     command.append(view_cmd)
        return command

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
            "name": "virtual_servers",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability\svirtual-server
                \s+(?P<alias>\S+)
                \s*(?P<address>address\s\S+)*
                \s*(?P<alg>algorithm\s\S+)*
                \s*(?P<delay_loop>delay-loop\s\S+)*
                \s*(?P<fwmet>forward-method\s\S+)*
                \s*(?P<fwmark>fwmark\s\S+)*
                \s*(?P<ptime>persistence-timeout\s\S+)*
                \s*(?P<port>port\s\S+)*
                \s*(?P<proto>protocol\s\S+)*
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            # "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "virtual_servers": {
                    "{{ alias }}": {
                        "alias": "{{ alias }}",
                        "address": "{{ address.split(" ")[1] if address is defined else None }}",
                        "algorithm": "{{ alg.split(" ")[1] if alo is defined else None }}",
                        "delay_loop": "{{ delay_loop.split(" ")[1] if delay_loop is defined else None }}",
                        "forward_method": "{{ fwmet.split(" ")[1] if fwmet is defined else None }}",
                        "fwmark": "{{ fwmark.split(" ")[1] if fwmark is defined else None }}",
                        "persistence_timeout": "{{ ptime.split(" ")[1] if ptime is defined else None }}",
                        "port": "{{ port.split(" ")[1] if port is defined else None }}",
                        "protocol": "{{ proto.split(" ")[1] if proto is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.real_servers",
            "getval": re.compile(
               r"""
               ^set\shigh-availability\svirtual-server
               \s+(?P<alias>\S+)
               \sreal-server
               \s+(?P<name>\S+)
               (?:\s+port\s+(?P<port>\S+))?
               (?:\s+health-check\sscript\s+(?P<hcscript>\S+))?
               (?:\s+connection-timeout\s+(?P<cont>\S+))?
               $
               """,
               re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs_rsrv,
            # "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "virtual_servers": {
                    "{{ alias }}": {
                        "alias": "{{ alias }}",
                        "real_servers": {
                            "{{ name }}": {
                                "name": "{{ name }}",
                                "port": "{{ portif port is defined else None }}",
                                "health_check_script": "{{ hcscript f hcscript is defined else None }}",
                                "connection_timeout": "{{ cont if cont is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "sync_group.member",
            "getval": re.compile(
               r"""
               ^set\shigh-availability\svrrp\ssync-group
               \s+(?P<sgname>\S+)
               \smember
               \s+(?P<member>\S+)
               $
               """,
               re.VERBOSE,
            ),
            "setval": "set high-availability vrrp sync-group {{sgname}} member {{member}}",
            "compval": "sync_groups.member",
            "result": {
                "sync_groups": {
                    "{{ sgname }}": {
                        "name": "{{ sgname }}",
                        "member": "{{ member }}",
                    },
                },
            },
        },
        {
            "name": "sync_group.health_check",
            "getval": re.compile(
               r"""
               ^set\shigh-availability\svrrp\ssync-group
               \s+(?P<sgname>\S+)
               \shealth-check
               (?:\s+failure-count\s+(?P<failure_count>\S+))
               ?(?:\s+interval\s+(?P<int>\S+))
               ?(?:\s+ping\s+(?P<ping>\S+))
               ?(?:\s+script\s+(?P<script>\S+))?
               $
               """,
               re.VERBOSE,
            ),
            "setval": _tmplt_sgroup_hc,
            # "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "sync_groups": {
                    "{{ sgname }}": {
                        "name": "{{ sgname }}",
                        "health_check": {
                            "failure_count": "{{ failure_count if failure_count is defined else None }}",
                            "interval": "{{ int if int is defined else None }}",
                            "ping": "{{ ping if ping is defined else None }}",
                            "script": "{{ script if script is defined else None }}",
                        },
                    },
                },
            },
        },
        {
            "name": "sync_group.transition_script",
            "getval": re.compile(
               r"""
               ^set\shigh-availability\svrrp\ssync-group
               \s+(?P<sgname>\S+)
               \stransition-script
               (?:\s+backup\s+(?P<backup>\S+))?
               (?:\s+fault\s+(?P<fault>\S+))?
               (?:\s+master\s+(?P<master>\S+))?
               (?:\s+stop\s+(?P<stop>\S+))?
               $
               """,
               re.VERBOSE,
            ),
            "setval": _tmplt_sgroup_ts,
            # "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "sync_groups": {
                    "{{ sgname }}": {
                        "name": "{{ sgname }}",
                        "transition_script": {
                            "backup": "{{ backup if backup is defined else None }}",
                            "fault": "{{ fault if fault is defined else None }}",
                            "master": "{{ master if master is defined else None }}",
                            "stop": "{{ stop if stop is defined else None }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.global_parameters.garp",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sglobal-parameters
                \s+garp
                (?:\s+interval\s+(?P<interval>\S+))?
                (?:\s+master-delay\s+(?P<master_delay>\S+))?
                (?:\s+master-refresh\s+(?P<master_refresh>\S+))?
                (?:\s+master-refresh-repeat\s+(?P<master_refresh_repeat>\S+))?
                (?:\s+master-repeat\s+(?P<master_repeat>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_gp_garp,
            "result": {
                "vrrp": {
                    "global_parameters": {
                        "garp": {
                            "interval": "{{ interval if interval is defined else None }}",
                            "master-delay": "{{ master_delay if master_delay is defined else None }}",
                            "master-refresh": "{{ master_refresh if master_refresh is defined else None }}",
                            "master-refresh-repeat": "{{ master_refresh_repeat if master_refresh_repeat is defined else None }}",
                            "master-repeat": "{{ master_repeat if master_repeat is defined else None }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.global_parameters",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sglobal-parameters
                (?:\s+startup-delay\s+(?P<startup_delay>\S+))?
                (?:\s+version\s+(?P<version>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_gp,
            "result": {
                "vrrp": {
                    "global_parameters": {
                        "startup-delay": "{{ startup_delay if startup_delay is defined else None }}",
                        "version": "{{ version if version is defined else None }}",
                    },
                },
            },
        },
    ]
    # fmt: on
