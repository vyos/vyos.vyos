#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_vrrp config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vrrp import (
    VrrpTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.utils import combine
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.version import (
    LooseVersion,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos import get_os_version


# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
#     dict_merge,
# )


class Vrrp(ResourceModule):
    """
    The vyos_vrrp config class
    """

    def __init__(self, module):
        super(Vrrp, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vrrp",
            tmplt=VrrpTemplate(),
        )
        self.parsers = [
            "disable",
        ]

    def _validate_template(self):
        version = get_os_version(self._module)
        if LooseVersion(version) >= LooseVersion("1.4"):
            self._tmplt = VrrpTemplate()
        else:
            self._module.fail_json(msg="VRRP is not supported in this version of VyOS")

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
            # self._module.fail_json(msg="Before normalize_vrrp_groups - entry: " + str(entry))
            self._vrrp_groups_list_to_dict(entry)
            self._virtual_servers_list_to_dict(entry)

        # self._module.fail_json(msg="Normalise - want: " + str(wantd) + " (((()))) have:  " + str(haved))

        # if state is merged, merge want onto have and then compare
        if self.state in ["merged"]:
            wantd = combine(haved, wantd, recursive=True)
            # self._module.fail_json(msg="Want: " + str(wantd) + "**** H:  " + str(haved))

        # if state is deleted, delete and empty out wantd
        # if self.state == "deleted":
        #     w = deepcopy(wantd)
        #     if w == {} and haved != {}:
        #         self.commands = ["delete vrrp"]
        #         return
        #     for k, want in w.items():
        #         if not (k in haved and haved[k]):
        #             del wantd[k]
        #         else:
        #             if isinstance(want, list):
        #                 for entry in want:
        #                     wname = entry.get("name")
        #                     haved["instances"] = [
        #                         i for i in haved.get("instances", []) if i.get("name") != wname
        #                     ]
        #                     self.commands.append("delete vrrp name {}".format(wname))
        #             else:
        #                 self.commands.append("delete vrrp {}".format(k.replace("_", "-")))
        #                 del wantd[k]
        #
        # if self.state == "overridden":
        #     w = deepcopy(wantd)
        #     h = deepcopy(haved)
        #     for k, want in w.items():
        #         if k in haved anzd haved[k] != want:
        #             if isinstance(want, list):
        #                 for entry in want:
        #                     wname = entry.get("name")
        #                     hdict = next(
        #                         (inst for inst in haved["instances"] if inst["name"] == wname),
        #                         None,
        #                     )
        #                     if entry != hdict:
        #                         # self._module.fail_json(msg="Want: " + str(entry) + "**** H:  " + str(hdict))
        #                         haved["instances"] = [
        #                             i for i in haved.get("instances", []) if i.get("name") != wname
        #                         ]
        #                         self.commands.append("delete vrrp name {}".format(wname))
        #                         self.commands.append("commit")
        #
        for k, want in wantd.items():
            if k == "vrrp":
                self._compare_vrrp(want, haved.get(k, {}))
            if k == "virtual_servers":
                # self._module.fail_json(msg="VSERVERS: " + str(want) + " ---- " + str(haved.get(k, {})))
                self._compare_vsrvs(want, haved.get(k, {}))
            # if isinstance(want, list):
            # self._module.fail_json(msg=str(want) + " +++ " + str(haved.pop(k, {})))
            self.compare(
                parsers=self.parsers,
                want={k: want},
                have={k: haved.pop(k, {})},
            )
        self._module.fail_json(msg=self.commands)

    def _compare_vsrvs(self, want, have):
        """Compare virtual servers of VRRP.py"""
        vs_parsers = [
            "virtual_servers",
            # "virtual_servers.real_servers",
        ]
        # self._module.fail_json(msg="want: " + str(want) + "**** have:  " + str(have))

        self.compare(
            parsers=vs_parsers,
            want={"virtual_servers": want},
            have={"virtual_servers": have},
        )

    def _compare_vrrp(self, want, have):
        """Compare the instances of VRRP"""
        vrrp_parsers = [
            "vrrp.snmp",
            # "vrrp.sync_groups.member",
            # "vrrp.sync_groups.health_check",
            # "vrrp.sync_groups.transition_script",
            "vrrp.global_parameters.garp",
            "vrrp.global_parameters",
            "vrrp.groups.garp",
            "vrrp.groups",
            # "vrrp.group.aunthentication",
            # "vrrp.group.transition_script",
            # "vrrp.groups.health_check",
            # "vrrp.group.track",
            # "vrrp.group.transition_script",
        ]

        # self._module.fail_json(msg="Conf: " + str(want) + " <*****************> " + str(have))

        want = {
            "vrrp": {
                "groups": {
                    "name": "g2",
                    "interface": "eth1",
                    "address": "2.2.2.2",
                    "disable": False,
                    "no_preempt": False,
                    "vrid": 11,
                    "garp": {
                        "interval": 21,
                        "master_delay": 6,
                        "master_refresh": 51,
                        "master_refresh_repeat": 101,
                        "master_repeat": 4,
                    },
                },
            },
        }
        have = {"vrrp": {"groups": {}}}
        self.compare(parsers=vrrp_parsers, want=want, have=have)

        # self.compare(parsers=vrrp_parsers, want={"vrrp": want}, have={"vrrp": have})

    def _vrrp_groups_list_to_dict(self, data):

        vrrp = data.get("vrrp", {})
        groups = vrrp.get("groups")

        # Nothing to do
        if not groups:
            return data

        # Already dict-based
        if isinstance(groups, dict):
            return data

        # Must be list → convert it
        if isinstance(groups, list):
            new_groups = {}
            for item in groups:
                name = item.get("name")
                if not name:
                    continue
                new_groups[name] = item

            data["vrrp"]["groups"] = new_groups
            return data

        # Unexpected shape → leave as-is
        return data

    def _virtual_servers_list_to_dict(self, data):

        vss = data.get("virtual_servers")
        if not vss:
            return data

        # Already normalized dict → return untouched
        if isinstance(vss, dict):
            return data

        # List → convert
        if isinstance(vss, list):
            new_vss = {}

            for item in vss:
                # Skip non-dict items
                if not isinstance(item, dict):
                    continue

                alias = item.get("alias")
                if not alias:
                    continue

                new_vss[alias] = item

            data["virtual_servers"] = new_vss
            return data

        # Anything else → leave unchanged
        return data
