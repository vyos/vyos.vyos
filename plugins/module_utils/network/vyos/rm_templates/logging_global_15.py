# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def tmplt_params(config_data):
    def templt_common(val, tmplt):
        if val.get("facility"):
            tmplt += " facility {facility}".format(facility=val["facility"])
        if val.get("severity"):
            tmplt += " level {level}".format(level=val["severity"])
        return tmplt

    tmplt = ""
    if config_data.get("global_params"):
        val = config_data.get("global_params")
        tmplt += "system syslog local"
        tmplt = templt_common(val.get("facilities", {}), tmplt)
    elif config_data.get("console"):
        val = config_data.get("console")
        tmplt += "system syslog console"
        tmplt = templt_common(val.get("facilities", {}), tmplt)
    elif config_data.get("hosts"):
        val = config_data.get("hosts")
        if val.get("hostname") and not val.get("port") and not val.get("protocol"):
            tmplt += "system syslog remote {hostname}".format(hostname=val["hostname"])
        if val.get("facilities"):
            tmplt = templt_common(val.get("facilities"), tmplt)
    return tmplt


class Logging_globalTemplate15(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Logging_globalTemplate15, self).__init__(
            lines=lines,
            tmplt=self,
            prefix=prefix,
            module=module,
        )

    # fmt: off
    PARSERS = [
        {
            "name": "syslog.state",
            "getval": re.compile(
                r"""
                ^set\ssystem
                (\s(?P<syslog>syslog))
                $""", re.VERBOSE,
            ),
            "setval": "system syslog",
            "result": {
                "syslog": {
                    "state": "{{ 'enabled' if syslog is defined else 'disabled' }}",
                },
            },
        },
        {
            "name": "console.state",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog
                (\s(?P<console>console))
                $""", re.VERBOSE,
            ),
            "setval": "system syslog console",
            "result": {
                "console": {
                    "state": "{{ 'enabled' if console is defined else 'disabled' }}",
                },
            },
        },
        {
            "name": "console.facilities",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sconsole\sfacility
                (\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE,
            ),
            "setval": tmplt_params,
            "remval": "system syslog console facility {{ console.facilities.facility }}",
            "result": {
                "console": {
                    "facilities": [
                        {
                            "facility": "{{ facility }}",
                            "severity": "{{ level }}",
                        },
                    ],
                },
            },
        },
        {
            "name": "global_params.state",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog
                (\s(?P<local>local))
                $""", re.VERBOSE,
            ),
            "setval": "system syslog local",
            "result": {
                "global_params": {
                    "state": "{{ 'enabled' if local is defined else 'disabled' }}",
                },
            },
        },
        {
            "name": "global_params.marker_interval",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\smarker\sinterval
                (\s(?P<marker_interval>'(\d+)'))?
                $""", re.VERBOSE,
            ),
            "setval": "system syslog marker interval {{ global_params.marker_interval }}",
            "remval": "system syslog marker",
            "result": {
                "global_params": {
                    "marker_interval": "{{ marker_interval }}",
                },
            },
        },
        {
            "name": "global_params.preserve_fqdn",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog
                (\s(?P<preserve_fqdn>preserve-fqdn))
                $""", re.VERBOSE,
            ),
            "setval": "system syslog preserve-fqdn",
            "result": {
                "global_params": {
                    "preserve_fqdn": "{{ True if preserve_fqdn is defined }}",
                },
            },
        },
        {
            "name": "global_params.facilities",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\slocal\sfacility
                (\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE,
            ),
            "setval": tmplt_params,
            "remval": "system syslog local facility {{ global_params.facilities.facility }}",
            "result": {
                "global_params": {
                    "facilities": [
                        {
                            "facility": "{{ facility }}",
                            "severity": "{{ level }}",
                        },
                    ],
                },
            },
        },
        {
            "name": "hosts.port",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sremote
                (\s(?P<hostname>\S+))
                (\sport\s(?P<port>'(\d+)'))
                $""", re.VERBOSE,
            ),
            "setval": "system syslog remote {{ hosts.hostname }} port {{ hosts.port }}",
            "result": {
                "hosts": {
                    "{{ hostname }}": {
                        "hostname": "{{ hostname }}",
                        "port": "{{ port }}",
                    },
                },
            },
        },
        {
            "name": "hosts.protocol",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sremote
                (\s(?P<hostname>\S+))
                (\sprotocol\s(?P<protocol>'(udp|tcp)'))
                $""", re.VERBOSE,
            ),
            "setval": "system syslog remote {{ hosts.hostname }} protocol {{ hosts.protocol }}",
            "result": {
                "hosts": {
                    "{{ hostname }}": {
                        "hostname": "{{ hostname }}",
                        "protocol": "{{ protocol }}",
                    },
                },
            },
        },
        {
            "name": "hosts",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sremote
                (\s(?P<hostname>\S+))
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE,
            ),
            "setval": tmplt_params,
            "remval": "system syslog remote {{ hosts.hostname }}",
            "result": {
                "hosts": {
                    "{{ hostname }}": {
                        "hostname": "{{ hostname }}",
                        "facilities": [
                            {
                                "facility": "{{ facility }}",
                                "severity": "{{ level }}",
                            },
                        ],
                    },
                },
            },
        },
    ]
    # fmt: on
