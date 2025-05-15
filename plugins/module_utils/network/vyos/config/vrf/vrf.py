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

        # if state is merged, merge want onto have and then compare
        if self.state in ["merged", "replaced"]:
            wantd = dict_merge(self.have, self.want)
        # self._module.fail_json(msg="Want: " + str(wantd) + "**** H:  " + str(haved))

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

            if "address_family" in entry:
                hdict = next((item for item in have if item["name"] == wname), None)
                # self._module.fail_json(msg="entry: " + str(entry) + "**** hdict:  " + str(hdict))

                self._compare_addr_family(entry, hdict)

    def _compare_addr_family(self, want, have):
        """Compare the address families of the VRF"""
        parsers = [
            "address_family",
            "disable_forwarding",
            "disable_nht",
        ]
        # self._module.fail_json(msg="wafi: " + str(want) + "**** Hafi:  " + str(have))

        wafi = self._vrf_inst_list_to_dict(want)
        hafi = self._vrf_inst_list_to_dict(have)
        # wafi = {
        #         "name": "vrf-test",
        #         "address_family": {
        #             "ipv4": {
        #                 "afi": "ipv4",
        #             },
        #         }
        #     }
        self.compare(parsers=parsers, want=wafi, have=hafi)

    def _vrf_inst_list_to_dict(self, entry):
        if entry and "address_family" in entry:
            address_family_dict = {f"{af['afi']}:": af for af in entry.get("address_family", [])}
            return {
                "name": entry["name"],
                "address_family": address_family_dict,
            }
