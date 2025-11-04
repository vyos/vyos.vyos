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


# from ansible.plugins.filter.core import combine


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

        # self._module.fail_json(msg="WanT: " + str(self.want) + "**** H:  " + str(self.have))

        # if state is merged, merge want onto have and then compare
        if self.state in ["merged", "replaced"]:
            # wantd = dict_merge(wantd, haved)
            # wantd = haved | combine(wantd, recursive=True)
            wantd = combine(haved, wantd, recursive=True)
            # self._module.fail_json(msg="Want: " + str(wantd) + "**** H:  " + str(haved))

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
                            if entry != hdict:
                                # self._module.fail_json(msg="Want: " + str(entry) + "**** H:  " + str(hdict))
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
        # self._module.fail_json(msg=self.commands)

    def _compare_instances(self, want, have):
        """Compare the instances of the VRF"""
        parsers = [
            "table_id",
            "vni",
            "description",
            "disable_vrf",
        ]
        # self._module.fail_json(msg="want: " + str(want) + "**** have:  " + str(have))

        for entry in want:
            h = {}
            wname = entry.get("name")
            # h = next((vrf for vrf in have if vrf["name"] == wname), {})
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
                # hdict = next((item for item in have if item["name"] == wname), None)
                hdict = next((d for d in have if d.get("name") == wname), None)

                hafi = {
                    "name": (hdict or {"name": wname})["name"],
                    "address_family": hdict.get("address_family", []) if hdict else [],
                }

                # self._module.fail_json(msg="wafi: " + str(wafi) + "**** hafi:  " + str(hafi))

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
                        # self._module.fail_json(msg=str(h_p_dict))
                        # self._module.fail_json(msg="wafi: " + str(w_p_dict) + "**** hafi:  " + str(h_p_dict))
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
            # "address_family",
            "disable_forwarding",
            "disable_nht",
        ]
        # self._module.fail_json(msg="wAfi: " + str(want) + "**** hAfi:  " + str(have))

        wafi = self.afi_to_list(want)
        hafi = self.afi_to_list(have)

        lookup = {(d["name"], d["afi"]): d for d in hafi}
        pairs = [(d1, lookup.get((d1["name"], d1["afi"]), {})) for d1 in wafi]

        for wafd, hafd in pairs:
            # self._module.fail_json(msg="wAfd: " + str(wafd) + "**** hAfd:  " + str(hafd))
            if "route_maps" in wafd:
                self._compare_route_maps(wafd, hafd)
            self.compare(parsers=afi_parsers, want=wafd, have=hafd)
        # self.compare(parsers=afi_parsers, want=wafi, have=hafi)

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

    # def _load_protocol_module(self, protocol_name):
    #     if protocol_name == "bgp":
    #         from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.bgp_global.bgp_global import (
    #             Bgp_global,
    #         )

    #         return Bgp_global(self._module)
    #     elif protocol_name == "ospf":
    #         from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospfv2.ospfv2 import (
    #             Ospfv2,
    #         )

    #         return Ospfv2(self._module)
    #     elif protocol_name == "ospfv3":
    #         from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospfv3.ospfv3 import (
    #             Ospfv3,
    #         )

    #         return Ospfv3(self._module)
    #     elif protocol_name == "static":
    #         self._module.fail_json(msg="here!")
    #         from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.static_routes.static_routes import (
    #             Static_routes,
    #         )

    #         return Static_routes(self._module)
    #     else:
    #         self._module.fail_json(msg="The protocol is not supported")
