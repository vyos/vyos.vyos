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

    # vyos@vyos:~$ show configuration commands | grep syslog
    # set system syslog console facility all
    # set system syslog console facility local7 level 'err'
    # set system syslog console facility news level 'debug'

    # set system syslog file abc archive size '125'
    # set system syslog file def archive file '2'
    # set system syslog file def facility local7 level 'emerg'

    # set system syslog host 10.0.2.15 facility all level 'all'
    # set system syslog host 10.0.2.15 facility all protocol 'udp'

    # set system syslog user paul facility local7 level 'err'
    # set system syslog user vyos facility local6 level 'emerg'
    # set system syslog user vyos facility local7 level 'err'

    # set system syslog global archive file '2'
    # set system syslog global facility cron level 'err'
    # set system syslog global marker interval '111'
    # set system syslog global preserve-fqdn
    # fmt: off

    def tmplt_params(config_data):
        tmplt = "system syslog"
        if config_data.get("global_params"):
            val = config_data.get("global_params")
            if val.get("facility"):
                tmplt += " global facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"])            
        elif config_data.get("console_params"):
            val = config_data.get("console_params")
            if val.get("facility"):
                tmplt += " console facility {facility}".format(facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"]) 
        elif config_data.get("users"):
            val = config_data.get("users")
            if val.get("facility") and val.get("username"):
                tmplt += " user {username} facility {facility}".format(username=val["username"],facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"])
        elif config_data.get("hosts_params"):
            val = config_data.get("hosts_params")
            if val.get("facility") and val.get("hostname"):
                tmplt += " host {hostname} facility {facility}".format(hostname=val["hostname"],facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"]) 
        elif config_data.get("hosts_protocol"):
            val = config_data.get("hosts_protocol")
            if val.get("facility") and val.get("hostname"):
                tmplt += " host {hostname} facility {facility}".format(hostname=val["hostname"],facility=val["facility"])
            if val.get("protocol"):
                tmplt += " protocol {protocol}".format(protocol=val["protocol"])
        elif config_data.get("files_param"):
            val = config_data.get("files_param")
            if val.get("facility") and val.get("path"):
                tmplt += " file {path} facility {facility}".format(path=val["path"],facility=val["facility"])
            if val.get("level"):
                tmplt += " level {level}".format(level=val["level"]) 
        return tmplt

    PARSERS = [
        { #console parsers
            "name": "console_params",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sconsole
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "result": {
                "config": {
                    "console_params": [{
                        "facility": "{{ facility }}",
                        "level": "{{ level }}",
                    }]
                }
            },
        },
        { #file parsers
            "name": "file_archive_size",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sfile
                (\s(?P<path>\S+))?
                (\sarchive\ssize\s(?P<size>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog file {{ file_archive_size.path }} archive size {{ file_archive_size.size }}",
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
            "name": "files_archive_num",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sfile
                (\s(?P<path>\S+))?
                (\sarchive\sfile\s(?P<file_num>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog file {{ files_archive_num.path }} archive size {{ files_archive_num.file_num }}",
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
            "name": "files_param",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sfile
                (\s(?P<path>\S+))?
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "result": {
                "config": {
                    "files": {"{{ path }}":{
                        "path": "{{ path }}",
                        "params":[{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },]
                    },}
                }
            },
        },
        { #global_param parsers
            "name": "global_archive_num",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal
                (\sarchive\sfile\s(?P<file_num>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog global archive file {{ global_archive_num.file_num }}",
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
            "name": "global_archive_size",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal
                (\sarchive\ssize\s(?P<size>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog global archive size {{ global_archive_size.size }}",
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
            "name": "global_marker_interval",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal
                (\smarker\sinterval\s(?P<marker_interval>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog global marker interval {{ global_marker_interval }}",
            "result": {
                "config": {
                    "global_params": {
                        "marker_interval": "{{ marker_interval }}",
                    }
                }
            },
        },
        {
            "name": "global_preserve_fqdn",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\sglobal
                (\s(?P<preserve_fqdn>preserve-fqdn))?
                $""", re.VERBOSE),
            "setval": "system syslog global preserve-fqdn {{ global_preserve_fqdn }}",
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
                ^set\ssystem\ssyslog\sglobal
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "result": {
                "config": {
                    "global_params": {
                        "params": [{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },],
                    }
                }
            },
        },
        { #host parsers
            "name": "hosts_port",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\shost
                (\s(?P<hostname>\S+))?
                (\sport\s(?P<port>'(\d+)'))?
                $""", re.VERBOSE),
            "setval": "system syslog host {{ hosts_port.hostname }} port {{ hosts_port.port }}",
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
            "name": "hosts_params",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\shost
                (\s(?P<hostname>\S+))?
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\slevel\s(?P<level>'(emerg|alert|crit|err|warning|notice|info|debug|all)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "result": {
                "config": {
                    "hosts": {"{{ hostname }}":{
                        "hostname": "{{ hostname }}",
                        "params":[{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },]
                    },}
                }
            },
        },
        {
            "name": "hosts_protocol",
            "getval": re.compile(
                r"""
                ^set\ssystem\ssyslog\shost
                (\s(?P<hostname>\S+))?
                (\sfacility\s(?P<facility>all|auth|authpriv|cron|daemon|kern|lpr|mail|mark|news|protocols|security|syslog|user|uucp|local[0-7]))?
                (\sprotocol\s(?P<protocol>'(udp|tcp)'))?
                $""", re.VERBOSE),
            "setval": tmplt_params,
            "result": {
                "config": {
                    "hosts": {"{{ hostname }}":{
                        "hostname": "{{ hostname }}",
                        "params":[{
                            "protocol": "{{ protocol }}",
                            "facility": "{{ facility }}",
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
            "result": {
                "config": {
                    "users": {
                        "{{ username }}":{
                        "username": "{{ username }}",
                        "params":[{
                            "facility": "{{ facility }}",
                            "level": "{{ level }}",
                        },]
                    }}
                }
            },
            # "shared": True
        },                
    ]
    # fmt: on
