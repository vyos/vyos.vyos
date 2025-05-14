#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_ntp config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vrf import (
    VrfTemplate,
)
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

        for entry in wantd, haved:
            self._vrf_inst_list_to_dict(entry)

        self._module.fail_json(msg=str(wantd))
        # if state is merged, merge want onto have and then compare
        if self.state in ["merged", "replaced"]:
            wantd = dict_merge(self.have, self.want)

        # if state is deleted, delete and empty out wantd
        if self.state == "deleted":
            w = deepcopy(wantd)
            for k, want in iteritems(w):
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
            for k, want in iteritems(w):
                if k in haved and haved[k] != want:
                    if isinstance(want, list):
                        for entry in want:
                            wname = entry.get("name")
                            hdict = next(
                                (inst for inst in haved["instances"] if inst["name"] == wname),
                                None,
                            )
                            if entry != hdict:
                                haved["instances"] = [
                                    i for i in haved.get("instances", []) if i.get("name") != wname
                                ]
                                self.commands.append("delete vrf name {}".format(wname))
                                self.commands.append("commit")

        for k, want in iteritems(wantd):
            if isinstance(want, list):
                self._compare_instances(want=want, have=haved.pop(k, {}))
            self.compare(
                parsers=self.parsers,
                want={k: want},
                have={k: haved.pop(k, {})},
            )
        self._module.fail_json(msg=self.commands)

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
            # h = next((vrf for vrf in have if vrf["name"] == wname), {})
            h = {
                k: v
                for vrf in have
                if vrf.get("name") == wname
                for k, v in vrf.items()
                if k != "address_family"
            }
            self.compare(parsers=parsers, want=entry, have=h)
            # if "address_family" in entry:
            #     for afi in want, have:
            #         # self._vrf_inst_list_to_dict(afi)
            #     self._module.fail_json(msg=want)
            #     self._compare_addr_family(want, have)

    def _compare_addr_family(self, want, have):
        """Compare the address families of the VRF"""
        parsers = [
            "disable_forwarding",
            "disable_nht",
        ]
        wdict = want.get("address_family", {})
        hdict = have.get("address_family", {})
        wname = want.get("name")
        hname = have.get("name")
        for name, entry in iteritems(wdict):
            for key, param in iteritems(entry):
                w_addr = {"afi": name, key: param}
                h_addr = {}
                if hdict.get(name):
                    h_addr = {"afi": name, key: hdict[name].pop(key, {})}
                w = {"name": wname, "address_family": w_addr}
                h = {"name": hname, "address_family": h_addr}
                self.compare(parsers=parsers, want=w, have=h)
        for name, entry in iteritems(hdict):
            for key, param in iteritems(entry):
                h_addr = {"afi": name, key: param}
                w_addr = {}
                w = {"name": wname, "address_family": w_addr}
                h = {"name": hname, "address_family": h_addr}
                self.compare(parsers=parsers, want=w, have=h)

    def _vrf_inst_list_to_dict(self, entry):
        # for data in entry:
        #     data["address_family"] = {
        #         af["afi"]: af for af in data["address_family"]
        #         }
        #     #

        for name, family in iteritems(entry):
            if "address_family" in family:
                addr_dict = {}
                for entry in family.get("address_family", []):
                    addr_dict.update({entry["afi"]: entry})
                family["address_family"] = addr_dict
                self._ospf_int_list_to_dict(family["address_family"])
