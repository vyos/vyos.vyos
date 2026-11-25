# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_vpp_acl config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vpp_acl import (
    Vpp_aclTemplate,
)


# rule leaves per family: (path in the rule, parser)
RULE_LEAVES = {
    "ip": [
        (("action",), "ip.rule.action"),
        (("description",), "ip.rule.description"),
        (("protocol",), "ip.rule.protocol"),
        (("source", "prefix"), "ip.rule.source.prefix"),
        (("source", "port"), "ip.rule.source.port"),
        (("destination", "prefix"), "ip.rule.destination.prefix"),
        (("destination", "port"), "ip.rule.destination.port"),
    ],
    "mac": [
        (("action",), "mac.rule.action"),
        (("description",), "mac.rule.description"),
        (("prefix",), "mac.rule.prefix"),
        (("mac_address",), "mac.rule.mac_address"),
        (("mac_mask",), "mac.rule.mac_mask"),
    ],
}
TCP_FLAG_LISTS = ["is_set", "is_not_set"]


def _get(data, path):
    for key in path:
        data = (data or {}).get(key)
    return data


def _by(items, key):
    return {item[key]: item for item in items or []}


class Vpp_acl(ResourceModule):
    """
    The vyos_vpp_acl config class
    """

    def __init__(self, module):
        super(Vpp_acl, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vpp_acl",
            tmplt=Vpp_aclTemplate(),
        )

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """Generate configuration commands to send based on
        want, have and desired state.
        """
        want = self.want or {}
        have = self.have or {}

        if self.state == "deleted":
            if not want:
                # no config given: remove all of vpp acl
                if have:
                    self.commands.append("delete vpp acl")
                return
            for family in ("ip", "mac"):
                wsec, hsec = want.get(family) or {}, have.get(family) or {}
                hacls, hifs = _by(hsec.get("acls"), "name"), _by(hsec.get("interfaces"), "name")
                for iface in wsec.get("interfaces") or []:
                    if iface["name"] in hifs:
                        self.addcmd({"name": iface["name"]}, family + ".interface", True)
                for acl in wsec.get("acls") or []:
                    if acl["name"] in hacls:
                        self.addcmd({"name": acl["name"]}, family + ".acl", True)
            return

        merge = self.state in ("merged", "rendered")
        for family in ("ip", "mac"):
            wsec, hsec = want.get(family) or {}, have.get(family) or {}
            wacls, hacls = _by(wsec.get("acls"), "name"), _by(hsec.get("acls"), "name")
            wifs, hifs = _by(wsec.get("interfaces"), "name"), _by(hsec.get("interfaces"), "name")

            if self.state == "overridden":
                # bindings first, so no ACL is deleted while still bound
                for name in sorted(set(hifs) - set(wifs)):
                    self.addcmd({"name": name}, family + ".interface", True)
                for name in sorted(set(hacls) - set(wacls)):
                    self.addcmd({"name": name}, family + ".acl", True)

            for name, acl in sorted(wacls.items()):
                self._compare_acl(family, acl, hacls.get(name), merge)
            for name, iface in sorted(wifs.items()):
                if family == "ip":
                    self._compare_ip_interface(iface, hifs.get(name), merge)
                else:
                    self._compare_mac_interface(iface, hifs.get(name), merge)

    def _compare_acl(self, family, want, have, merge):
        """Compare one ACL: its description, then its rules."""
        name = want["name"]
        if have is None and want.keys() == {"name"}:
            self.addcmd({"name": name}, family + ".acl", False)
            return
        have = have or {"name": name}
        self._leaf(
            {"name": name},
            want.get("description"),
            have.get("description"),
            family + ".description",
            merge,
        )
        wrules, hrules = _by(want.get("rules"), "number"), _by(have.get("rules"), "number")
        for number, rule in sorted(wrules.items()):
            self._compare_rule(family, name, rule, hrules.get(number), merge)
        if not merge:
            for number in sorted(set(hrules) - set(wrules)):
                self.addcmd({"name": name, "number": number}, family + ".rule", True)

    def _compare_rule(self, family, name, want, have, merge):
        """Compare one rule: its leaves, and for IP rules the TCP flag lists."""
        number = want["number"]
        if have is None and want.keys() == {"number"}:
            self.addcmd({"name": name, "number": number}, family + ".rule", False)
            return
        have = have or {"number": number}
        base = {"name": name, "number": number}
        for path, parser in RULE_LEAVES[family]:
            self._leaf(base, _get(want, path), _get(have, path), parser, merge)
        if family == "ip":
            for key in TCP_FLAG_LISTS:
                wflags = set(_get(want, ("tcp_flags", key)) or [])
                hflags = set(_get(have, ("tcp_flags", key)) or [])
                parser = "ip.rule.tcp_flags." + key
                for flag in sorted(wflags - hflags):
                    self.addcmd(dict(base, value=flag), parser, False)
                if not merge:
                    for flag in sorted(hflags - wflags):
                        self.addcmd(dict(base, value=flag), parser, True)

    def _compare_ip_interface(self, want, have, merge):
        """Compare the input and output bindings of one interface, by acl_tag."""
        name = want["name"]
        if have is None and want.keys() == {"name"}:
            self.addcmd({"name": name}, "ip.interface", False)
            return
        have = have or {"name": name}
        for direction in ("input", "output"):
            wtags = {b["acl_tag"]: b["tag_name"] for b in want.get(direction) or []}
            htags = {b["acl_tag"]: b["tag_name"] for b in have.get(direction) or []}
            parser = "ip.interface." + direction
            for tag, acl in sorted(wtags.items()):
                if htags.get(tag) != acl:
                    self.addcmd({"name": name, "acl_tag": tag, "value": acl}, parser, False)
            if not merge:
                for tag in sorted(set(htags) - set(wtags)):
                    self.addcmd({"name": name, "acl_tag": tag}, parser, True)

    def _compare_mac_interface(self, want, have, merge):
        """Compare the MAC ACL bound to one interface."""
        name = want["name"]
        if have is None and want.keys() == {"name"}:
            self.addcmd({"name": name}, "mac.interface", False)
            return
        have = have or {"name": name}
        self._leaf(
            {"name": name},
            want.get("tag_name"),
            have.get("tag_name"),
            "mac.interface.tag_name",
            merge,
        )

    def _leaf(self, base, wval, hval, parser, merge):
        """Set a changed leaf; in replaced and overridden, delete one that is not wanted."""
        if wval is not None and wval != hval:
            self.addcmd(dict(base, value=wval), parser, False)
        elif wval is None and hval is not None and not merge:
            self.addcmd(dict(base, value=hval), parser, True)
