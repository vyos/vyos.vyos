# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Vrrp parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def _tmplt_vsrvs(config_data):
    config_data = config_data["virtual_servers"]
    command = []

    cmd = "high-availability virtual-server {name}".format(**config_data)
    for key, value in config_data.items():
        if key == "name" or isinstance(value, dict) or value is None:
            continue
        else:
            command.append(f"{cmd} {key.replace('_', '-')} {value}")

    return command


def _tmplt_vsrvs_rsrv(config_data):
    config_data = config_data["virtual_servers"]
    command = []
    cmd = "high-availability virtual-server {name}".format(**config_data)
    config_data = config_data["real_server"]
    address = config_data["address"]
    for key, value in config_data.items():
        if key == "address" or value is None:
            continue
        if value is not None and key == "health_check_script":
            command.append(cmd + " real-server " + address + " health-check script " + value)
        else:
            command.append(cmd + " real-server " + f"{address} {key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_sgroup_hc(config_data):
    config_data = config_data["vrrp"]["sync_groups"]
    command = []
    cmd = "high-availability vrrp sync-group {name}".format(**config_data)
    config_data = config_data["health_check"]
    for key, value in config_data.items():
        if value is not None:
            command.append(cmd + " health-check " + f"{key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_sgroup_ts(config_data):
    config_data = config_data["vrrp"]["sync_groups"]
    command = []
    cmd = "high-availability vrrp sync-group {name}".format(**config_data)
    config_data = config_data["transition_script"]
    for key, value in config_data.items():
        if value is not None:
            command.append(cmd + " transition-script " + f"{key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_gp(config_data):
    config_data = config_data["vrrp"]["global_parameters"]
    command = []

    cmd = "high-availability vrrp global-parameters".format(**config_data)
    for key, value in config_data.items():
        if isinstance(value, dict) or value is None:
            continue
        else:
            command.append(f"{cmd} {key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_gp_garp(config_data):
    config_data = config_data["vrrp"]["global_parameters"]["garp"]
    command = []
    cmd = "high-availability vrrp global-parameters garp"

    for key, value in config_data.items():
        if value is None:
            continue
        command.append(f"{cmd} {key.replace('_', '-')} {value}")

    return command


def _tmplt_vrrp_group(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)

    for key, value in config_data.items():
        if (
            key == "name"
            or isinstance(value, dict)
            or isinstance(value, list)
            or isinstance(value, bool)
            or value is None
        ):
            continue
        else:
            command.append(f"{cmd} {key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_group_bool(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)

    for key, value in config_data.items():
        if key != "name" and value is not None:
            command.append(f"{cmd} {key.replace('_', '-')}")
    return command


def _tmplt_vrrp_group_garp(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)
    config_data = config_data["garp"]
    for key, value in config_data.items():
        if value is not None:
            command.append(cmd + " garp " + f"{key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_group_auth(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)
    config_data = config_data["authentication"]
    for key, value in config_data.items():
        if value is not None:
            command.append(cmd + " authentication " + f"{key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_group_ts(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)
    config_data = config_data["transition_script"]
    for key, value in config_data.items():
        if value is not None:
            command.append(cmd + " transition-script " + f"{key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_sgroup_member(config_data):
    sgroup = config_data["vrrp"]["sync_groups"]
    command = []
    cmd = "high-availability vrrp sync-group {name}".format(**sgroup)
    members = sgroup.get("member", [])
    for member in members:
        if member is None:
            continue
        command.append(f"{cmd} member {member}")
    return command


def _tmplt_vrrp_group_exaddress(config_data):
    group = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**group)
    exaddresses = group.get("excluded_address", [])
    for exaddress in exaddresses:
        if exaddress is None:
            continue
        command.append(f"{cmd} excluded-address {exaddress}")
    return command


def _tmplt_vrrp_group_hc(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)
    config_data = config_data["health_check"]
    for key, value in config_data.items():
        if value is not None:
            command.append(cmd + " health-check " + f"{key.replace('_', '-')} {value}")
    return command


def _tmplt_vrrp_group_track_list(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)
    config_data = config_data["track"]
    for key, value in config_data.items():
        if isinstance(value, list) and value is not None and key != "name":
            for item in value:
                command.append(cmd + " track " + f"{key.replace('_', '-')} {item}")
    return command


def _tmplt_vrrp_group_track_bool(config_data):
    config_data = config_data["vrrp"]["groups"]
    command = []
    cmd = "high-availability vrrp group {name}".format(**config_data)
    config_data = config_data["track"]
    for key, value in config_data.items():
        if key != "name" and value is not None:
            command.append(cmd + " track " + f"{key.replace('_', '-')}")
    return command


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
                "disable": "{{ True if disable is defined else False }}",
            },
        },
        # {
        #     "name": "virtual_servers",
        #     "getval": re.compile(
        #         r"""
        #         ^set\shigh-availability\svirtual-server
        #         \s+(?P<name>\S+)
        #         # (?:\s+address\s+(?P<address>\S+))?
        #         (?:\s+algorithm\s+(?P<algorithm>\S+))?
        #         (?:\s+delay-loop\s+(?P<delay_loop>\S+))?
        #         (?:\s+forward-method\s+(?P<forward_method>\S+))?
        #         (?:\s+fwmark\s+(?P<fwmark>\S+))?
        #         (?:\s+persistence-timeout\s+(?P<persistence_timeout>\S+))?
        #         (?:\s+port\s+(?P<port>\S+))?
        #         (?:\s+protocol\s+(?P<protocol>\S+))?
        #         $
        #         """,
        #         re.VERBOSE,
        #     ),
        #     "setval": _tmplt_vsrvs,
        #     "result": {
        #         "virtual_servers": {
        #             "{{ name }}": {
        #                 "name": "{{ name }}",
        #                 # "address": "{{ address if address is defined else None }}",
        #                 "algorithm": "{{ algorithm if algorithm is defined else None }}",
        #                 "delay_loop": "{{ delay_loop if delay_loop is defined else None }}",
        #                 "forward_method": "{{ forward_method if forward_method is defined else None }}",
        #                 "fwmark": "{{ fwmark if fwmark is defined else None }}",
        #                 "persistence_timeout": "{{ persistence_timeout if persistence_timeout is defined else None }}",
        #                 "port": "{{ port if port is defined else None }}",
        #                 "protocol": "{{ protocol if protocol is defined else None }}",
        #             },
        #         },
        #     },
        # },
        {
            "name": "virtual_servers.address",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+address\s+(?P<address>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "address": "{{ address if address is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.algorithm",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+algorithm\s+(?P<algorithm>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "algorithm": "{{ algorithm if algorithm is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.delay_loop",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+delay-loop\s+(?P<delay_loop>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "delay_loop": "{{ delay_loop if delay_loop is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.forward_method",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+forward-method\s+(?P<forward_method>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "forward_method": "{{ forward_method if forward_method is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.fwmark",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+fwmark\s+(?P<fwmark>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "fwmark": "{{ fwmark if fwmark is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.persistence_timeout",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+persistence-timeout\s+(?P<persistence_timeout>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "persistence_timeout": "{{ persistence_timeout if persistence_timeout is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.port",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+port\s+(?P<port>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "port": "{{ port if port is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "virtual_servers.protocol",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                (?:\s+protocol\s+(?P<protocol>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "protocol": "{{ protocol if protocol is defined else None }}",
                    },
                },
            },
        },
        # {
        #     "name": "virtual_servers.real_server",
        #     "getval": re.compile(
        #         r"""
        #         ^set\shigh-availability\svirtual-server
        #         \s+(?P<name>\S+)
        #         \sreal-server
        #         \s+(?P<address>\S+)
        #         (?:\s+port\s+(?P<port>\S+))?
        #         (?:\s+health-check\sscript\s+(?P<hcscript>\S+))?
        #         (?:\s+connection-timeout\s+(?P<cont>\S+))?
        #         $
        #         """,
        #         re.VERBOSE,
        #     ),
        #     "setval": _tmplt_vsrvs_rsrv,
        #     "result": {
        #         "virtual_servers": {
        #             "{{ name }}": {
        #                 "name": "{{ name }}",
        #                 "real_server": {
        #                     "{{ address }}": {
        #                         "address": "{{ address }}",
        #                         "port": "{{ port if port is defined else None }}",
        #                         "health_check_script": "{{ hcscript if hcscript is defined else None }}",
        #                         "connection_timeout": "{{ cont if cont is defined else None }}",
        #                     },
        #                 },
        #             },
        #         },
        #     },
        # },
        {
            "name": "virtual_servers.real_server.port",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                \sreal-server
                \s+(?P<address>\S+)
                (?:\s+port\s+(?P<port>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs_rsrv,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "real_server": {
                            "{{ address }}": {
                                "address": "{{ address }}",
                                "port": "{{ port if port is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "virtual_servers.real_server.health_check_script",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                \sreal-server
                \s+(?P<address>\S+)
                (?:\s+health-check\sscript\s+(?P<hcscript>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs_rsrv,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "real_server": {
                            "{{ address }}": {
                                "address": "{{ address }}",
                                "health_check_script": "{{ hcscript if hcscript is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "virtual_servers.real_server.connection_timeout",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svirtual-server
                \s+(?P<name>\S+)
                \sreal-server
                \s+(?P<address>\S+)
                (?:\s+connection-timeout\s+(?P<cont>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vsrvs_rsrv,
            "result": {
                "virtual_servers": {
                    "{{ name }}": {
                        "name": "{{ name }}",
                        "real_server": {
                            "{{ address }}": {
                                "address": "{{ address }}",
                                "connection_timeout": "{{ cont if cont is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.sync_groups.member",
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
            "setval": _tmplt_vrrp_sgroup_member,
            "result": {
                "vrrp": {
                    "sync_groups": {
                        "{{ sgname }}": {
                            "name": "{{ sgname }}",
                            "member": [
                                "{{ member }}",
                            ],
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.sync_groups.health_check",
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
            "setval": _tmplt_vrrp_sgroup_hc,
            "result": {
                "vrrp": {
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
        },
        {
            "name": "vrrp.sync_groups.transition_script",
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
            "setval": _tmplt_vrrp_sgroup_ts,
            "result": {
                "vrrp": {
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
                            "master_delay": "{{ master_delay if master_delay is defined else None }}",
                            "master_refresh": "{{ master_refresh if master_refresh is defined else None }}",
                            "master_refresh_repeat": "{{ master_refresh_repeat if master_refresh_repeat is defined else None }}",
                            "master_repeat": "{{ master_repeat if master_repeat is defined else None }}",
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
                        "startup_delay": "{{ startup_delay if startup_delay is defined else None }}",
                        "version": "{{ version if version is defined else None }}",
                    },
                },
            },
        },
        {
            "name": "vrrp.groups",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
                (?:\s+address\s+(?P<address>\S+))?
                (?:\s+description\s+(?P<description>'.+?'|\S+))?
                (?:\s+advertise-interval\s+(?P<advertise_interval>\S+))?
                (?:\s+hello-source-address\s+(?P<hello_source>\S+))?
                (?:\s+interface\s+(?P<interface>\S+))?
                (?:\s+peer-address\s+(?P<peer_address>\S+))?
                (?:\s+priority\s+(?P<priority>\S+))?
                (?:\s+vrid\s+(?P<vrid>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
                            "address": "{{ address if address is defined else None }}",
                            "description": "{{ description if description is defined else None }}",
                            "advertise_interval": "{{ advertise_interval if advertise_interval is defined else None }}",
                            "hello_source_address": "{{ hello_source if hello_source is defined else None }}",
                            "interface": "{{ interface if interface is defined else None }}",
                            "peer_address": "{{ peer_address if peer_address is defined else None }}",
                            "priority": "{{ priority if priority is defined else None }}",
                            "vrid": "{{ vrid if vrid is defined else None }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.groups.excluded_address",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
                \sexcluded-address
                \s+(?P<excluded_address>.*)
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_exaddress,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
                            "excluded_address": [
                                "{{ excluded_address | replace(\"'\", \"\") }}",
                            ],
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.groups.garp",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
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
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
                            "garp": {
                                "interval": "{{ interval if interval is defined else None }}",
                                "master_delay": "{{ master_delay if master_delay is defined else None }}",
                                "master_refresh": "{{ master_refresh if master_refresh is defined else None }}",
                                "master_refresh_repeat": "{{ master_refresh_repeat if master_refresh_repeat is defined else None }}",
                                "master_repeat": "{{ master_repeat if master_repeat is defined else None }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.groups.authentication",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
                \s+authentication
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
                        "{{ gname }}": {
                            "name": "{{ gname }}",
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
            "name": "vrrp.groups.transition_script",
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
            "name": "vrrp.groups.health_check",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
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
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
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
            "name": "vrrp.groups.track.interface",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
                \strack
                (?:\s+interface\s+(?P<interface>\S+))?
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_track_list,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
                            "track": {
                                "interface": "{{ [interface.strip(\"'\")] if interface is defined else [] }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.snmp",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability
                \svrrp
                \s(?P<snmp>snmp)
                $""",
                re.VERBOSE,
            ),
            "setval": "high-availability vrrp snmp",
            "result": {
                "vrrp": {
                    "snmp": "{{ 'enabled' if snmp is defined else 'disabled' }}",
                },
            },
        },
        {
            "name": "vrrp.groups.disable",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability\svrrp\sgroup
                \s(?P<gname>\S+)
                \s(?P<disable>disable)
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_bool,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "disable": "{{ True if disable is defined else False }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.groups.no_preempt",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability\svrrp\sgroup
                \s(?P<gname>\S+)
                \s(?P<no_preempt>no-preempt)
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_bool,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "no_preempt": "{{ True if no_preempt is defined else False }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.groups.rfc3768_compatibility",
            "getval": re.compile(
                r"""
                ^set
                \shigh-availability\svrrp\sgroup
                \s(?P<gname>\S+)
                \s(?P<rfc3768_compatibility>rfc3768-compatibility)
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_bool,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "rfc3768_compatibility": "{{ True if rfc3768_compatibility is defined else False }}",
                        },
                    },
                },
            },
        },
        {
            "name": "vrrp.groups.track.exclude_vrrp_interface",
            "getval": re.compile(
                r"""
                ^set\shigh-availability\svrrp\sgroup
                \s+(?P<gname>\S+)
                \strack
                \s(?P<exclude_vrrp_inter>exclude-vrrp-interface)
                $
                """,
                re.VERBOSE,
            ),
            "setval": _tmplt_vrrp_group_track_bool,
            "result": {
                "vrrp": {
                    "groups": {
                        "{{ gname }}": {
                            "name": "{{ gname }}",
                            "track": {
                                "exclude_vrrp_interface": "{{ True if exclude_vrrp_inter is defined else False }}",
                            },
                        },
                    },
                },
            },
        },
    ]
    # fmt: on
