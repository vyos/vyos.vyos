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

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
    get_from_dict,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vpp_acl import (
    Vpp_aclTemplate,
)


FAMILIES = ("ip", "mac")


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
        # parser groups come from the template: <family>.description for an ACL,
        # <family>.rule.* for a rule, <family>.interface.* for an interface binding
        names = [p["name"] for p in Vpp_aclTemplate.PARSERS]
        self.acl_parsers = {f: [n for n in names if n == f + ".description"] for f in FAMILIES}
        self.rule_parsers = {f: [n for n in names if n.startswith(f + ".rule.")] for f in FAMILIES}
        self.interface_parsers = {
            f: [n for n in names if n.startswith(f + ".interface.")] for f in FAMILIES
        }

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
            self._deleted(want, have)
            return

        merge = self.state in ("merged", "rendered")
        emptied = []
        for family in FAMILIES:
            wsec, hsec = want.get(family) or {}, have.get(family) or {}
            wacls, hacls = _by(wsec.get("acls"), "name"), _by(hsec.get("acls"), "name")
            wifs, hifs = _by(wsec.get("interfaces"), "name"), _by(hsec.get("interfaces"), "name")

            if self.state == "overridden":
                if not (wacls or wifs):
                    if hacls or hifs:
                        emptied.append(family)
                    continue
                for name in sorted(set(hifs) - set(wifs)):
                    self.addcmd({"name": name}, family + ".interface", True)
                for name in sorted(set(hacls) - set(wacls)):
                    self.addcmd({"name": name}, family + ".acl", True)

            for name, acl in sorted(wacls.items()):
                self._compare_acl(family, acl, hacls.get(name), merge)
            for name, iface in sorted(wifs.items()):
                self._compare_entity(
                    family + ".interface",
                    self.interface_parsers[family],
                    iface,
                    hifs.get(name),
                    merge,
                )
        self._delete_emptied(emptied, have)

    def _deleted(self, want, have):
        """Delete the given ACLs and bindings, or all of vpp acl."""
        if not want:
            if have:
                self.commands.append("delete vpp acl")
            return
        emptied = []
        for family in FAMILIES:
            wsec, hsec = want.get(family) or {}, have.get(family) or {}
            hacls, hifs = _by(hsec.get("acls"), "name"), _by(hsec.get("interfaces"), "name")
            dels_if = [i["name"] for i in wsec.get("interfaces") or [] if i["name"] in hifs]
            dels_acl = [a["name"] for a in wsec.get("acls") or [] if a["name"] in hacls]
            if (hacls or hifs) and set(dels_if) == set(hifs) and set(dels_acl) == set(hacls):
                emptied.append(family)
                continue
            for name in dels_if:
                self.addcmd({"name": name}, family + ".interface", True)
            for name in dels_acl:
                self.addcmd({"name": name}, family + ".acl", True)
        self._delete_emptied(emptied, have)

    def _delete_emptied(self, families, have):
        """Delete families that end up empty as a whole: VyOS rejects an empty family node."""
        if not families:
            return
        remaining = [f for f in FAMILIES if f not in families and have.get(f)]
        if not remaining and self.state == "deleted":
            self.commands.append("delete vpp acl")
            return
        for family in families:
            self.commands.append("delete vpp acl " + family)

    def _compare_acl(self, family, want, have, merge):
        """Compare one ACL, then its rules (each rule carries its ACL name as acl)."""
        name = want["name"]
        self._compare_entity(family + ".acl", self.acl_parsers[family], want, have, merge)
        wrules = _by(want.get("rules"), "number")
        hrules = _by((have or {}).get("rules"), "number")
        for number, rule in sorted(wrules.items()):
            hrule = hrules.get(number)
            self._compare_entity(
                family + ".rule",
                self.rule_parsers[family],
                dict(rule, acl=name),
                dict(hrule, acl=name) if hrule else None,
                merge,
            )
        if not merge:
            for number in sorted(set(hrules) - set(wrules)):
                self.addcmd({"acl": name, "number": number}, family + ".rule", True)

    def _compare_entity(self, node, parsers, want, have, merge):
        """Compare one ACL, rule or interface; create its bare node if it is new and empty."""
        content = [k for k in want if k not in ("name", "acl", "number")]
        if have is None and not content:
            self.addcmd(want, node, False)
            return
        have = have or {k: v for k, v in want.items() if k in ("name", "acl", "number")}
        if merge:
            want = dict_merge(have, want)
        for parser in parsers:
            path = self._tmplt.get_parser(parser).get("compval") or parser
            if isinstance(get_from_dict(want, path), list) or isinstance(
                get_from_dict(have, path),
                list,
            ):
                self._compare_items(parser, path, want, have, merge)
            else:
                self.compare(parsers=[parser], want=want, have=have)

    def _compare_items(self, parser, path, want, have, merge):
        """Compare a list-valued field one item at a time; an item's identity is
        what the parser's remval deletes by (the whole value when there is none)."""
        remval = self._tmplt.get_parser(parser).get("remval") or ""
        keys = re.findall(r"{{\s*%s\.(\w+)\s*}}" % re.escape(path), remval)

        def ident(item):
            return tuple(item[k] for k in keys) if keys else item

        witems = {ident(i): i for i in get_from_dict(want, path) or []}
        hitems = {ident(i): i for i in get_from_dict(have, path) or []}
        if merge:
            witems = dict(list(hitems.items()) + list(witems.items()))
        base = {k: v for k, v in want.items() if not isinstance(v, (list, dict))}
        for key in sorted(set(witems) | set(hitems), key=str):
            self.compare(
                parsers=[parser],
                want=self._with(base, path, witems.get(key)),
                have=self._with(base, path, hitems.get(key)),
            )

    @staticmethod
    def _with(base, path, value):
        """base with value placed at the dotted path (nothing placed for None)."""
        data = dict(base)
        if value is None:
            return data
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = value
        return data
