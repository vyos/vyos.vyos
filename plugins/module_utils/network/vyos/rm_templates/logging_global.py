# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Logging_global parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class Logging_globalTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Logging_globalTemplate, self).__init__(
            lines=lines, tmplt=self, prefix=prefix, module=module
        )

    # fmt: off
    def tmplt_params(config_data):
        tmplt = "system syslog"
        if config_data.get("global_params"):
            val = config_data.get("global_params")
            if val.get("facility"):
                tmplt += " global facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"])            
        elif config_data.get("console"):
            val = config_data.get("console")
            if val.get("facility"):
                tmplt += " console facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"]) 
        elif config_data.get("users"):
            val = config_data.get("users")
            if config_data.get("tag"):
                tmplt += " user {username}".format(username=config_data["tag"])
            if val.get("facility"):
                tmplt += " facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"])
        elif config_data.get("hosts"):
            val = config_data.get("hosts")
            if config_data.get("tag"):
                tmplt += " host {hostname}".format(hostname=config_data["tag"])
            if val.get("facility"):
                tmplt += " facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"]) 
            if val.get("protocol"):
                tmplt += " protocol {protocol}".format(protocol=val["protocol"])
        elif config_data.get("files"):
            val = config_data.get("files")
            if config_data.get("tag"):
                tmplt += " file {path}".format(path=config_data["tag"])
            if val.get("facility"):
                tmplt += " facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"])
        if tmplt == "system syslog":
            tmplt = None
        return tmplt

    PARSERS = [
        { #console parsers
            "name": "console",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sconsole\sfacility
                (\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "remval": "system syslog console",
            "result": {
                "config": {
                    "console": {
                        "facilities": [{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        }]
                    }
                }
            },
        },
        {
            "name": "console.state",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog
                (\s(?P<console>console))
                $""", re.VERBOSE),
            "setval": "system syslog console",
            "result": {
                "config": {
                    "console": {
                        "state": "{{ 'enabled' if console is defined else 'disabled' }}",
                    }
                }
            },
        },
        {
            "name": "files.archive_size",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sfile
                (\s(?P<path>\S+))?
                (\sarchive\ssize\s(?P<size>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog file {{ files.tag }} archive size {{ files.archive_size }}",
            "result": {
                "config": {
                    "files": {"{{ path }}": {
                        "path": "{{ path }}",
                        "archive": {
                            "size": "{{ size }}",
                        },
                    },}
                }
            },
        },
        {
            "name": "files.archive_file_num",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sfile
                (\s(?P<path>\S+))?
                (\sarchive\sfile\s(?P<file_num>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog file {{ files.tag }} archive file {{ files.archive_file_num }}",
            "result": {
                "config": {
                    "files": {"{{ path }}":{
                        "path": "{{ path }}",
                        "archive": {
                            "file_num": "{{ file_num }}",
                        },
                    },}
                }
            },
        },
        {
            "name": "files",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sfile
                (\s(?P<path>\S+))?
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "remval": "system syslog file",
            "result": {
                "config": {
                    "files": {"{{ path }}":{
                        "path": "{{ path }}",
                        "facilities":[{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },]
                    },}
                }
            },
        },
        { #global_param parsers
            "name": "global_params.state",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog
                (\s(?P<global>global))
                $""", re.VERBOSE),
            "setval": "system syslog global",
            "result": {
                "config": {
                    "global_params": {
                        "state": "{{ 'enabled' if global is defined else 'disabled' }}",
                    }
                }
            },
        },
        {
            "name": "global_params.archive_file_num",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal\sarchive\sfile
                (\s(?P<file_num>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog global archive file {{ global_params.archive_file_num }}",
            "result": {
                "config": {
                    "global_params": {
                        "archive": {
                            "file_num": "{{ file_num }}",
                        },
                    }
                }
            },
        },
        {
            "name": "global_params.archive_size",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal\sarchive\ssize
                (\s(?P<size>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog global archive size {{ global_params.archive_size }}",
            "result": {
                "config": {
                    "global_params": {
                        "archive": {
                            "size": "{{ size }}",
                        },
                    }
                }
            },
        },
        {
            "name": "global_params.marker_interval",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal\smarker\sinterval
                (\s(?P<marker_interval>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog global marker interval {{ global_params.marker_interval }}",
            "result": {
                "config": {
                    "global_params": {
                        "marker_interval": "{{ marker_interval }}",
                    }
                }
            },
        },
        {
            "name": "global_params.preserve_fqdn",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal
                (\s(?P<preserve_fqdn>preserve-fqdn))
                $""", re.VERBOSE),
            "setval": "system syslog global preserve-fqdn",
            "result": {
                "config": {
                    "global_params": {
                        "preserve_fqdn": "{{ True if preserve_fqdn is defined }}",
                    }
                }
            },
        },
        {
            "name": "global_params",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal\sfacility
                (\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "remval": "system syslog global",
            "result": {
                "config": {
                    "global_params": {
                        "facilities": [{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },],
                    }
                }
            },
        },
        {
            "name": "hosts",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\shost
                (\s(?P<hostname>\S+))
                (\sport\s(?P<port>'(\d+)'))
                $""", re.VERBOSE),
            "setval": "system syslog host {{ hosts.tag }} port {{ hosts.port }}",
            "remval": "system syslog host",
            "result": {
                "config": {
                    "hosts": {"{{ hostname }}":{
                        "hostname": "{{ hostname }}",
                        "port": "{{ port }}",
                    },}
                }
            },
        },
        {
            "name": "hosts.facility",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\shost
                (\s(?P<hostname>\S+))
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                (\sprotocol\s(?P<protocol>'(udp|tcp)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "result": {
                "config": {
                    "hosts": {"{{ hostname }}":{
                        "hostname": "{{ hostname }}",
                        "facilities":[{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                            "protocol": "{{ protocol }}",
                        },]
                    },}
                }
            },
        },
        { #user parsers
            "name": "users",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\suser
                (\s(?P<username>\S+))?
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "remval": "system syslog user",
            "result": {
                "config": {
                    "users": {
                        "{{ username }}":{
                        "username": "{{ username }}",
                        "facilities":[{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },]
                    }}
                }
            },
        },
    ]
    # fmt: on
