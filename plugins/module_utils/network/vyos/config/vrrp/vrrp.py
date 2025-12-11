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
            self._vrrp_sync_groups_list_to_dict(entry)
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
            "virtual_servers.real_server",
        ]

        for pair in self._extract_named_leafs(want):
            self.compare(
                parsers=vs_parsers,
                want={"virtual_servers": pair},
                have={"virtual_servers": {}},
            )

    def _compare_vrrp(self, want, have):
        """Compare the instances of VRRP"""
        vrrp_parsers = [
            "vrrp.snmp",
            "vrrp.global_parameters",
            "vrrp.global_parameters.garp",
            "vrrp.groups",
            "vrrp.groups.excluded_address",
            "vrrp.groups.garp",
            "vrrp.groups.authentication",
            "vrrp.groups.transition_script",
            "vrrp.groups.health_check",
            "vrrp.groups.track",
            "vrrp.sync_groups.member",
            "vrrp.sync_groups.transition_script",
            "vrrp.sync_groups.health_check",
        ]

        pairs = []
        # self._module.fail_json(msg="Want: " + str(want) + "&&&&&&&&&&&&&&&&&&&& have:  " + str(have))
        # for wdict in self._extract_leaf_items(want):
        #     self._module.fail_json(
        #         msg=self._lookup_element(wdict, self._extract_leaf_items(have)),
        #     )

        # for wdict in self._extract_leaf_items(want):
        #     self.compare(parsers=vrrp_parsers, want={"vrrp": wdict}, have={"vrrp": {}})

        hlist = self._extract_leaf_items(have)
        # wdict =         {
        #     "groups": {
        #         "name": "g2",
        #         "preempt": False
        #     }
        # }
        # self._module.fail_json(msg=self._extract_path_tuple(wdict))
        # self._module.fail_json(msg=self._lookup_element(wdict, hlist))
        # self._module.fail_json(msg=self._find_matching_by_path(wdict, hlist))

        # self._module.fail_json(msg=self._extract_leaf_items(want))

        # wdict = {
        #         "groups": {
        #             "name": "g1",
        #             "track": {
        #                 "interface": [
        #                     "eth0",
        #                 ]
        #             }
        #         }
        #     }
        # hdict = {
        #     "groups": {
        #         "name": "g1",
        #         "track": {
        #             "interface": [
        #                 "eth2",
        #             ]
        #         }
        #     }
        # }

        # self.compare(parsers=vrrp_parsers, want={"vrrp": wdict}, have={"vrrp": hdict})
        for wdict in self._extract_leaf_items(want):
            # hdict = {}
            hdict = self._find_matching_by_path(wdict, hlist)
            pairs.append((wdict, hdict))
            self.compare(parsers=vrrp_parsers, want={"vrrp": wdict}, have={"vrrp": hdict})
        # self._module.fail_json(msg=pairs)

    def _vrrp_groups_list_to_dict(self, data):

        vrrp = data.get("vrrp", {})
        groups = vrrp.get("groups")

        if not groups:
            return data
        if isinstance(groups, dict):
            return data
        if isinstance(groups, list):
            new_groups = {}
            for item in groups:
                name = item.get("name")
                if not name:
                    continue
                new_groups[name] = item

            data["vrrp"]["groups"] = new_groups
            return data
        return data

    def _vrrp_sync_groups_list_to_dict(self, data):

        vrrp = data.get("vrrp", {})
        groups = vrrp.get("sync_groups")

        if not groups:
            return data
        if isinstance(groups, dict):
            return data
        if isinstance(groups, list):
            new_groups = {}
            for item in groups:
                name = item.get("name")
                if not name:
                    continue
                new_groups[name] = item

            data["vrrp"]["sync_groups"] = new_groups
            return data
        return data

    def _virtual_servers_list_to_dict(self, data):

        vss = data.get("virtual_servers")
        if not vss:
            return data

        if isinstance(vss, dict):
            for vs in vss.items():
                rs = vs.get("real_server")
                if isinstance(rs, list):
                    vs["real_server"] = {
                        item["address"]: item
                        for item in rs
                        if isinstance(item, dict) and item.get("address")
                    }

            return data

        if isinstance(vss, list):
            new_vss = {}
            for vs in vss:
                if not isinstance(vs, dict):
                    continue
                name = vs.get("name")
                if not name:
                    continue
                rs = vs.get("real_server")
                if isinstance(rs, list):
                    vs["real_server"] = {
                        item["address"]: item
                        for item in rs
                        if isinstance(item, dict) and item.get("address")
                    }

                new_vss[name] = vs

            data["virtual_servers"] = new_vss
            return data

        return data

    def _extract_leaf_items(self, data, path=None, parent_name=None):
        path = path or []
        results = []

        if isinstance(data, dict):
            current_name = data.get("name", parent_name)

            for k, v in data.items():
                if k == "name":
                    continue
                results.extend(self._extract_leaf_items(v, path + [k], current_name))
            return results

        leaf_key = path[-1]
        top_key = path[0]

        if top_key in ["groups", "sync_groups"]:
            subkeys = path[2:]
        else:
            subkeys = path[1:]

        nested = {leaf_key: data}

        for p in reversed(subkeys[:-1]):
            nested = {p: nested}
        if parent_name:
            out = {top_key: {"name": parent_name}}
            out[top_key].update(nested)
        else:
            out = {top_key: nested}

        results.append(out)
        return results

    def _extract_named_leafs(self, data, parent_name=None, prefix_key=None):
        results = []

        if prefix_key == "real_server" and isinstance(data, dict):
            for server_name, server_data in data.items():
                if isinstance(server_data, dict):
                    results.append(
                        {
                            "name": parent_name,
                            "real_server": server_data,
                        },
                    )
            return results

        if isinstance(data, dict):
            current_name = data.get("name", parent_name)

            for k, v in data.items():
                if k == "name":
                    continue
                leaves = self._extract_named_leafs(v, current_name, k)
                results.extend(leaves)
            return results
        return [
            {
                "name": parent_name,
                prefix_key: data,
            },
        ]

    # def _extract_path_tuple(self, d):

    #     path = []
    #     cur = d
    #     while isinstance(cur, dict) and cur:
    #         k = next(iter(cur))
    #         path.append(k)
    #         cur = cur[k]
    #     return tuple(path)

    # def _lookup_element(self, element, target_list):

    #     key = self._extract_path_tuple(element)
    #     for obj in target_list:
    #         if self._extract_path_tuple(obj) == key:
    #             return obj
    #     return {}

    def _lookup_by_path(self, want_item, have_list):
        """
        Find matching object in have_list by structural path + name (if present).
        Ignore values. Return {} if not found.
        """

        def extract_signature(d):
            sig = []

            while isinstance(d, dict) and d:
                k = next(iter(d))
                sig.append(k)
                d = d[k]

                # capture identity if present
                if isinstance(d, dict) and "name" in d:
                    sig.append(("name", d["name"]))
            self._module.fail_json(msg="SIG: " + str(sig))
            return tuple(sig)

        want_sig = extract_signature(want_item)

        for obj in have_list:
            if extract_signature(obj) == want_sig:
                return obj

        return {}

    def _find_matching_by_path(self, want_item, have_list):
        """
        Return the object from have_list that matches the structural path of want_item.
        Matching ignores values; 'name' inside objects is treated as identity and included.
        Returns {} if no match.
        """

        def build_sig_node(node):
            """Return a tuple fragment describing node (no top-level key)."""
            if not isinstance(node, dict):
                return ()
            # single-key dict: descend
            if len(node) == 1:
                k = next(iter(node))
                return (k,) + build_sig_node(node[k])
            # multi-key dict: capture name (if present), then remaining keys deterministically
            parts = []
            if "name" in node:
                parts.append(("name", node["name"]))
            # process other keys in sorted order for determinism
            for k in sorted(k for k in node.keys() if k != "name"):
                v = node[k]
                if isinstance(v, dict):
                    # include the key and recurse into it
                    parts.append(k)
                    parts += list(build_sig_node(v))
                else:
                    parts.append(k)
            return tuple(parts)

        # build signature for want_item
        if not (isinstance(want_item, dict) and want_item):
            return {}
        top = next(iter(want_item))  # e.g. "groups" or "global_parameters"
        sig_want = (top,) + build_sig_node(want_item[top])

        # search
        for obj in have_list:
            if not (isinstance(obj, dict) and obj):
                continue
            top2 = next(iter(obj))
            sig_have = (top2,) + build_sig_node(obj[top2])
            if sig_have == sig_want:
                return obj

        return {}
