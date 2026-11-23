# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_nhrp config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.nhrp import (
    NhrpTemplate,
)


class Nhrp(ResourceModule):
    """
    The vyos_nhrp config class
    """

    def __init__(self, module):
        super(Nhrp, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="nhrp",
            tmplt=NhrpTemplate(),
        )
        self.parsers = [
            "authentication",
            "holdtime",
            "mtu",
            "network_id",
            "redirect",
            "shortcut",
            "registration_no_unique",
        ]

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
        wantd = self._tunnels(self.want)
        haved = self._tunnels(self.have)

        if self.state == "deleted":
            if not wantd:
                # no tunnels given: remove all of protocols nhrp
                if haved:
                    self.commands.append("delete protocols nhrp")
                return
            for name in wantd:
                if name in haved:
                    self.addcmd({"name": name}, "tunnel", True)
            return

        if self.state == "overridden":
            for name in haved:
                if name not in wantd:
                    self.addcmd({"name": name}, "tunnel", True)

        merge = self.state in ("merged", "rendered")
        for name, want in wantd.items():
            if name not in haved and want.keys() == {"name"}:
                # a new tunnel without options still needs its node
                self.addcmd({"name": name}, "tunnel", False)
                continue
            self._compare(name, want, haved.get(name, {"name": name}), merge)

    def _compare(self, name, want, have, merge):
        """Compare one tunnel: options and flags, then multicast, map and nhs."""
        scalars = dict_merge(have, want) if merge else want
        self.compare(parsers=self.parsers, want=scalars, have=have)
        self._compare_multicast(name, want, have, merge)
        self._compare_map(name, want, have, merge)
        self._compare_nhs(name, want, have, merge)

    def _compare_multicast(self, name, want, have, merge):
        wantm = set(want.get("multicast") or [])
        havem = set(have.get("multicast") or [])
        for value in sorted(wantm - havem):
            self.addcmd({"name": name, "multicast": value}, "multicast", False)
        if not merge:
            for value in sorted(havem - wantm):
                self.addcmd({"name": name, "multicast": value}, "multicast", True)

    def _compare_map(self, name, want, have, merge):
        wantm = {m["tunnel_ip"]: m for m in want.get("map") or []}
        havem = {m["tunnel_ip"]: m for m in have.get("map") or []}
        for ip, entry in sorted(wantm.items()):
            if havem.get(ip) != entry:
                self.addcmd({"name": name, "map": entry}, "map", False)
        if not merge:
            for ip, entry in sorted(havem.items()):
                if ip not in wantm:
                    self.addcmd({"name": name, "map": entry}, "map", True)

    def _compare_nhs(self, name, want, have, merge):
        wantn = {n["tunnel_ip"]: n for n in want.get("nhs") or []}
        haven = {n["tunnel_ip"]: n for n in have.get("nhs") or []}
        for ip, entry in sorted(wantn.items()):
            wnbma = set(entry.get("nbma") or [])
            hnbma = set((haven.get(ip) or {}).get("nbma") or [])
            for nbma in sorted(wnbma - hnbma):
                self.addcmd({"name": name, "nhs": {"tunnel_ip": ip, "nbma": nbma}}, "nhs", False)
            if not merge:
                for nbma in sorted(hnbma - wnbma):
                    self.commands.append(
                        "delete protocols nhrp tunnel {0} nhs tunnel-ip {1} nbma {2}".format(
                            name,
                            ip,
                            nbma,
                        ),
                    )
        if not merge:
            for ip in sorted(haven):
                if ip not in wantn:
                    self.addcmd({"name": name, "nhs": {"tunnel_ip": ip}}, "nhs", True)

    def _tunnels(self, data):
        """Tunnels by name."""
        return {t["name"]: t for t in (data or {}).get("tunnels") or []}
