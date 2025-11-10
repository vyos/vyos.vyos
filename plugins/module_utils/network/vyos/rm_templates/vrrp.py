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

    def _tmplt_vrrp_group(config_data):
        config_data = config_data["vrrp"]["group"]
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

    def _tmplt_vrrp_group_track(config_data):
        config_data = config_data["vrrp"]["group"]["track"]
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

    def _tmplt_vrrp_group_hc(config_data):
        config_data = config_data["vrrp"]["group"]["health-check"]
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

    def _tmplt_vrrp_group_ts(config_data):
        config_data = config_data["vrrp"]["group"]["transcription-script"]
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

    def _tmplt_vrrp_group_garp(config_data):
        config_data = config_data["vrrp"]["group"]["garp"]
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

    def _tmplt_vrrp_group_auth(config_data):
        config_data = config_data["vrrp"]["group"]["authentication"]
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
            "name": "virtual_servers",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<alias>\S+)
                (?:\s+address\s+(?P<address>\S+))?
                (?:\s+algorithm\s+(?P<algorithm>\S+))?
                (?:\s+delay-loop\s+(?P<delay_loop>\S+))?
                (?:\s+forward-method\s+(?P<forward_method>\S+))?
                (?:\s+fwmark\s+(?P<fwmark>\S+))?
                (?:\s+persistence-timeout\s+(?P<persistence_timeout>\S+))?
                (?:\s+port\s+(?P<port>\S+))?
                (?:\s+protocol\s+(?P<protocol>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ alias }}": {
                        "alias": "{{ alias }}",
                        "address": "{{ address if address is defined else None }}",
                        "algorithm": "{{ algorithm if algorithm is defined else None }}",
                        "delay_loop": "{{ delay_loop if delay_loop is defined else None }}",
                        "forward_method": "{{ forward_method if forward_method is defined else None }}",
                        "fwmark": "{{ fwmark if fwmark is defined else None }}",
                        "persistence_timeout": "{{ persistence_timeout if persistence_timeout is defined else None }}",
                        "port": "{{ port if port is defined else None }}",
                        "protocol": "{{ protocol if protocol is defined else None }}",
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
                                "port": "{{ port if port is defined else None }}",
                                "health_check_script": "{{ hcscript if hcscript is defined else None }}",
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

        {
            "name": "vrrp.group",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<group_name>\S+)
                (?:\s+address\s+(?P<address>\S+))?
                (?:\s+description\s+(?P<description>'.+?'|\S+))?
                (?:\s+hello-source-address\s+(?P<hello_source>\S+))?
                (?:\s+interface\s+(?P<interface>\S+))?
                (?:\s+(?P<no_preempt>no-preempt))?
                (?:\s+peer-address\s+(?P<peer_address>\S+))?
                (?:\s+priority\s+(?P<priority>\S+))?
                (?:\s+vrid\s+(?P<vrid>\S+))?
                (?:\s+rfc3768-compatibility\s+(?P<rfc3768_compatibility>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ group_name }}": {
                            "name": "{{ group_name }}",
                            "address": "{{ address if address is defined else None }}",
                            "description": "{{ description.strip(\"'\") if description is defined else None }}",
                            "hello-source-address": "{{ hello_source if hello_source is defined else None }}",
                            "interface": "{{ interface if interface is defined else None }}",
                            "no-preempt": "{{ True if no_preempt is defined else False }}",
                            "peer-address": "{{ peer_address if peer_address is defined else None }}",
                            "priority": "{{ priority if priority is defined else None }}",
                            "vrid": "{{ vrid if vrid is defined else None }}",
                            "rfc3768-compatibility": "{{ rfc3768_compatibility if rfc3768_compatibility is defined else None }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.group.authentication",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<group_name>\S+)
                \s+(?P<authentication>\S+)
                (?:\s+password\s+(?P<password>\S+))?
                (?:\s+type\s+(?P<type>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_auth,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ group_name }}": {
                            "name": "{{ group_name }}",
                            "authentication": {
                                "password": "{{ password if password is defined else None }}",
                                "type": "{{ type if type is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.group.garp",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
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
            "setval": _tmplt_vrrp_group_garp,
            "result": {
                "vrrp": {
                    "group": {
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
            "name": "vrrp.group.transition_script",
            "getval": re.compile(
               r"""
               ^set\shigh-availability\svrrp\sgroup
               \s+(?P<gname>\S+)
               \stransition-script
               (?:\s+backup\s+(?P<backup>\S+))?
               (?:\s+fault\s+(?P<fault>\S+))?
               (?:\s+master\s+(?P<master>\S+))?
               (?:\s+stop\s+(?P<stop>\S+))?
               $
               """,
               re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_ts,
            # "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
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
        },
        {
            "name": "vrrp.group.health_check",
            "getval": re.compile(
               r"""
               ^set\shigh-availability\svrrp\sgroup
               \s+(?P<group_name>\S+)
               \shealth-check
               (?:\s+failure-count\s+(?P<failure_count>\S+))
               ?(?:\s+interval\s+(?P<int>\S+))
               ?(?:\s+ping\s+(?P<ping>\S+))
               ?(?:\s+script\s+(?P<script>\S+))?
               $
               """,
               re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_hc,
            # "compval": "global_parameters.garp.master_refersh_repeat",
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ group_name }}": {
                            "name": "{{ group_name }}",
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
        },
        {
            "name": "vrrp.group.track",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<group_name>\S+)
                \strack
                (?:\s+exculde-vrrp-interface\s+(?P<exclude_vrrp_inter>\S+))?
                (?:\s+interface\s+(?P<interface>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_track,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ group_name }}": {
                            "name": "{{ group_name }}",
                            "track": {
                                "exclude-vrrp-interface": "{{ exclude-vrrp-inter if exclude-vrrp-inter is defined else None }}",
                                "interface": "{{ interface if interface is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.group.excluded_address",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<group_name>\S+)
                \sexcluded-address\s+(?P<address>\S+)
                (?:\s+interface\s+(?P<interface>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_auth,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ group_name }}": {
                            "name": "{{ group_name }}",
                            "excluded_address": {
                                "{{ address }}": {
                                    "name": "{{ address }}",
                                    "interface": "{{ interface if interface is defined else None }}",
                                },
                            },
                        },
                    },
                },
            },
        },
    ]
    # fmt: on
