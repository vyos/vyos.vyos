#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The vyos_vrf config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.bgp_global.bgp_global import (
    Bgp_global,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospfv2.ospfv2 import (
    Ospfv2,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospfv3.ospfv3 import (
    Ospfv3,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.static_routes.static_routes import (
    Static_routes,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vrf import (
    VrfTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.utils import combine
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.version import (
    LooseVersion,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos import get_os_version


class Vrf(ResourceModule):
    """
    The vyos_vrf config class
    """

    def __init__(self, module):
        super(Vrf, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vrf",
            tmplt=VrfTemplate(),
        )
        self.parsers = [
            "bind_to_all",
        ]

    def _validate_template(self):
        version = get_os_version(self._module)
        if LooseVersion(version) >= LooseVersion("1.4"):
            self._tmplt = VrfTemplate()
        else:
            self._module.fail_json(msg="VRF is not supported in this version of VyOS")

    def parse(self):
        """override parse to check template"""
        self._validate_template()
        return super().parse()

    def get_parser(self, name):
        """get_parsers"""
        self._validate_template()
        return super().get_parser(name)

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
        wantd = {}
        haved = {}
        wantd = deepcopy(self.want)
        haved = deepcopy(self.have)

        # if state is merged, merge want onto have and then compare
        if self.state in ["merged", "replaced"]:

            wantd = combine(haved, wantd, recursive=True)

        # if state is deleted, delete and empty out wantd
        if self.state == "deleted":
            w = deepcopy(wantd)
            if w == {} and haved != {}:
                self.commands = ["delete vrf"]
                return
            for k, want in w.items():
                if not (k in haved and haved[k]):
                    del wantd[k]
                else:
                    if isinstance(want, list):
                        for entry in want:
                            wname = entry.get("name")
                            haved["instances"] = [
                                i for i in haved.get("instances", []) if i.get("name") != wname
                            ]
                            self.commands.append("delete vrf name {}".format(wname))
                    else:
                        self.commands.append("delete vrf {}".format(k.replace("_", "-")))
                        del wantd[k]

        if self.state == "overridden":
            w = deepcopy(wantd)
            h = deepcopy(haved)
            for k, want in w.items():
                if k in haved and haved[k] != want:
                    if isinstance(want, list):
                        for entry in want:
                            wname = entry.get("name")
                            hdict = next(
                                (inst for inst in haved["instances"] if inst["name"] == wname),
                                None,
                            )
                            wantc = self._canonicalise(entry)
                            havec = self._canonicalise(hdict or {})

                            if wantc != havec:
                                haved["instances"] = [
                                    i for i in haved.get("instances", []) if i.get("name") != wname
                                ]
                                self.commands.append("delete vrf name {}".format(wname))
                                self.commands.append("commit")

        for k, want in wantd.items():
            if isinstance(want, list):
                self._compare_instances(want=want, have=haved.pop(k, {}))
            self.compare(
                parsers=self.parsers,
                want={k: want},
                have={k: haved.pop(k, {})},
            )

    def _compare_instances(self, want, have):
        """Compare the instances of the VRF"""
        parsers = [
            "table_id",
            "vni",
            "description",
            "disable_vrf",
        ]

        for entry in want:
            h = {}
            wname = entry.get("name")
            h = {
                k: v
                for vrf in have
                if vrf.get("name") == wname
                for k, v in vrf.items()
                if k != "address_family"
            }
            self.compare(parsers=parsers, want=entry, have=h)

            if "address_family" in entry:
                wafi = {"name": wname, "address_family": entry.get("address_family", [])}
                hdict = next((d for d in have if d.get("name") == wname), None)

                hafi = {
                    "name": (hdict or {"name": wname})["name"],
                    "address_family": hdict.get("address_family", []) if hdict else [],
                }

                self._compare_addr_family(wafi, hafi)

            if "protocols" in entry:
                for protocol_name in entry["protocols"]:

                    w_p_dict = entry["protocols"][protocol_name]

                    h_p_dict = next(
                        (
                            v.get("protocols", {}).get(protocol_name, {})
                            for v in have
                            if v.get("name") == wname
                        ),
                        {},
                    )
                    if protocol_name == "bgp":
                        bgp_module = Bgp_global(self._module)
                        bgp_module._validate_template()
                        bgp_module.want = w_p_dict
                        bgp_module.have = h_p_dict
                        bgp_module.generate_commands()
                        protocol_commands = bgp_module.commands
                    elif protocol_name == "ospf":
                        ospfv2_module = Ospfv2(self._module)
                        ospfv2_module._module.params["config"] = w_p_dict
                        ospfv2_module.state = self.state
                        protocol_commands = ospfv2_module.set_config(h_p_dict)
                    elif protocol_name == "ospfv3":
                        ospfv3_module = Ospfv3(self._module)
                        ospfv3_module._module.params["config"] = w_p_dict
                        ospfv3_module.state = self.state
                        protocol_commands = ospfv3_module.set_config(h_p_dict)
                    elif protocol_name == "static":
                        static_routes_module = Static_routes(self._module)
                        static_routes_module._module.params["config"] = w_p_dict
                        static_routes_module.state = self.state
                        protocol_commands = static_routes_module.set_config(h_p_dict)
                    else:
                        self._module.fail_json(
                            msg="The protocol {} is not supported".format(protocol_name),
                        )
                    self.commands.extend(
                        [
                            cmd.replace("protocols", "vrf name " + wname + " protocols", 1)
                            for cmd in protocol_commands
                        ],
                    )

    def _compare_addr_family(self, want, have):
        """Compare the address families of the VRF"""
        afi_parsers = [
            "disable_forwarding",
            "disable_nht",
        ]

        wafi = self.afi_to_list(want)
        hafi = self.afi_to_list(have)

        lookup = {(d["name"], d["afi"]): d for d in hafi}
        pairs = [(d1, lookup.get((d1["name"], d1["afi"]), {})) for d1 in wafi]

        for wafd, hafd in pairs:
            if "route_maps" in wafd:
                self._compare_route_maps(wafd, hafd)
            self.compare(parsers=afi_parsers, want=wafd, have=hafd)

    def afi_to_list(self, data):
        """Convert address family dict to list"""

        return [
            {"name": data["name"], **{**af, "afi": "ip" if af["afi"] == "ipv4" else af["afi"]}}
            for af in data["address_family"]
        ]

    def _compare_route_maps(self, wafd, hafd):
        want_rms = wafd.get("route_maps", [])
        have_rms = hafd.get("route_maps", [])

        for want in want_rms:
            match = next(
                (
                    h
                    for h in have_rms
                    if h["rm_name"] == want["rm_name"] and h["protocol"] == want["protocol"]
                ),
                {},
            )
            base = {"name": wafd["name"], "afi": wafd["afi"]}

            self.compare(
                parsers="route_maps",
                want={**base, "route_maps": want},
                have={**base, "route_maps": match},
            )

    def _canonicalise(self, obj):
        if isinstance(obj, dict):
            return {k: self._canonicalise(v) for k, v in obj.items()}

        if isinstance(obj, list):
            if not obj:
                return obj

            if not isinstance(obj[0], dict):
                return sorted(obj)

            canon = [self._canonicalise(i) for i in obj]

            def sort_key(d):
                for k in ("name", "address", "afi", "area_id", "neighbor_id", "dest"):
                    if k in d:
                        return d[k]
                return tuple(sorted(d.items()))

            return sorted(canon, key=sort_key)

        return obj
