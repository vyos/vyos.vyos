# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos vpp_acl fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vpp_acl.vpp_acl import (
    Vpp_aclArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vpp_acl import (
    Vpp_aclTemplate,
)


def _number(item, key):
    return int(item[key])


class Vpp_aclFacts(object):
    """The vyos vpp_acl facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Vpp_aclArgs.argument_spec

    def get_device_data(self, connection):
        return connection.get("show configuration commands | grep 'vpp acl'")

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Vpp_acl network resource
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = self.get_device_data(connection)

        lines = [line.replace("'", "") for line in data.splitlines()]
        objs = Vpp_aclTemplate(lines=lines, module=self._module).parse()

        for family in ("ip", "mac"):
            section = objs.get(family)
            if not section:
                continue
            acls = []
            for acl in (section.get("acls") or {}).values():
                rules = []
                for rule in (acl.get("rules") or {}).values():
                    flags = rule.get("tcp_flags") or {}
                    for key in list(flags):
                        flags[key] = sorted(flags[key].values())
                    rules.append(rule)
                if rules:
                    acl["rules"] = sorted(rules, key=lambda r: _number(r, "number"))
                acls.append(acl)
            if acls:
                section["acls"] = sorted(acls, key=lambda a: a["name"])
            interfaces = []
            for iface in (section.get("interfaces") or {}).values():
                for direction in ("input", "output"):
                    if direction in iface:
                        iface[direction] = sorted(
                            iface[direction].values(),
                            key=lambda b: _number(b, "acl_tag"),
                        )
                interfaces.append(iface)
            if interfaces:
                section["interfaces"] = sorted(interfaces, key=lambda i: i["name"])

        facts = {"vpp_acl": {}}
        if objs:
            params = utils.validate_config(self.argument_spec, {"config": objs})
            facts["vpp_acl"] = utils.remove_empties(params["config"])

        ansible_facts["ansible_network_resources"].update(facts)
        return ansible_facts
