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
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    remove_empties,
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

        if self.state not in ["parsed", "gathered", "purged"]:
            self.generate_commands()
            self.run_commands()

        if self.state == "purged":
            wantd = {"disable": False, "vrrp": {"snmp": "disabled"}}
            haved = deepcopy(self.have)

            if wantd != haved:
                self.commands = ["delete high-availability"]
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
        # self._module.fail_json(msg="Generate commands - want: " + str(self.want) + " (((()))) have:  " + str(haved))
        for entry in wantd, haved:
            # self._module.fail_json(msg="Before normalize_vrrp_groups - entry: " + str(entry))
            self._vrrp_groups_list_to_dict(entry)
            self._virtual_servers_list_to_dict(entry)
            self._vrrp_sync_groups_list_to_dict(entry)
            self._normalize_lists(entry)
        # self._module.fail_json(msg="Normalise - want: " + str(wantd) + " (((()))) have:  " + str(haved))

        if self.state in ["overridden", "deleted"]:
            # self._module.fail_json(msg=self._module.params.get('config', {}))
            (wantd, haved, path) = self._prune_stubs(self._module.params.get("config", {}), haved)
            # self._module.fail_json(msg=wantd)
            # wantg = [ ((), wantd) ]
            # while wantg:
            #     path, node = wantg.pop()

            # if path and isinstance(node, dict) and any(isinstance(v, dict) for v in node.values()):
            #     self._module.fail_json(msg="Path: " + str(path) + " Node: " + str(node))

            #     for k, v in reversed(node.items()):
            #         wantg.append((path + (k,), v))

        keys = set(wantd) | set(haved)

        for k in keys:
            want = wantd.get(k, {})
            have = haved.get(k, {})

            if k == "vrrp":
                if self.state in ["merged"]:
                    want = combine(have, want, recursive=True)
                self._compare_vrrp(want, have)
            if k == "virtual_servers":
                if self.state in ["merged"]:
                    want = combine(have, want, recursive=True)
                self._compare_vsrvs(want, have)
            if self.state in ["deleted"] and k == "disable":
                want = have
            if self.state in ["rendered"]:
                have = None
            self.compare(
                parsers=self.parsers,
                want={k: want},
                have={k: have},
            )

        # for k, want in wantd.items():
        #     if k == "vrrp":
        #         if self.state in ["merged"]:
        #             want = combine(haved.get(k, {}), want, recursive=True)
        #         self._compare_vrrp(want, haved.get(k, {}))
        #     if k == "virtual_servers":
        #         if self.state in ["merged"]:
        #             want = combine(haved.get(k, {}), want, recursive=True)
        #         self._compare_vsrvs(want, haved.get(k, {}))
        #     self.compare(
        #         parsers=self.parsers,
        #         want={k: want},
        #         have={k: haved.pop(k, {})},
        # )
        self.commands = sorted(list(dict.fromkeys(self.commands)))
        self._module.fail_json(msg=self.commands)

    def _compare_vsrvs(self, want, have):
        """Compare virtual servers of VRRP"""
        vs_parsers = [
            "virtual_servers.address",
            "virtual_servers.algorithm",
            "virtual_servers.delay_loop",
            "virtual_servers.forward_method",
            "virtual_servers.persistence_timeout",
            "virtual_servers.fwmark",
            "virtual_servers.port",
            "virtual_servers.protocol",
            "virtual_servers.real_server.port",
            "virtual_servers.real_server.health_check_script",
            "virtual_servers.real_server.connection_timeout",
        ]
        pairs = []
        # self._module.fail_json(msg="Want: " + str(want) + "&&&&&&&&&&&&&&&&&&&& have:  " + str(have))

        hlist = self._extract_named_leafs(have)
        wlist = self._extract_named_leafs(want)

        if self.state == "rendered":
            hlist = []
        # self._module.fail_json(msg="Want: " + str(wlist) + "&&&&&&&&&&&&&&&&&&&& have:  " + str(hlist))

        if self.state in ["replaced", "deleted", "overridden"]:
            for hdict in hlist:
                wdict = self._find_matching_vsrv(hdict, wlist)
                if self.state == "deleted" and wdict:
                    wdict = {}
                pairs.append((wdict, hdict))
                self.compare(
                    parsers=vs_parsers,
                    want={"virtual_servers": wdict},
                    have={"virtual_servers": hdict},
                )
            # self._module.fail_json(msg=pairs)
        if self.state in ["merged", "replaced", "rendered"]:
            for wdict in wlist:
                hdict = self._find_matching_vsrv(wdict, hlist)
                pairs.append((wdict, hdict))
                self.compare(
                    parsers=vs_parsers,
                    want={"virtual_servers": wdict},
                    have={"virtual_servers": hdict},
                )
        # self._module.fail_json(msg=pairs)

    def _compare_vrrp(self, want, have):
        """Compare the instances of VRRP"""
        vrrp_parsers = [
            "vrrp.snmp",
            "vrrp.global_parameters",
            "vrrp.global_parameters.garp",
            "vrrp.groups",
            "vrrp.groups.disable",
            "vrrp.groups.no_preempt",
            "vrrp.groups.rfc3768_compatibility",
            "vrrp.groups.excluded_address",
            "vrrp.groups.garp",
            "vrrp.groups.authentication",
            "vrrp.groups.transition_script",
            "vrrp.groups.health_check",
            "vrrp.groups.track.interface",
            "vrrp.groups.track.exclude_vrrp_interface",
            "vrrp.sync_groups.member",
            "vrrp.sync_groups.transition_script",
            "vrrp.sync_groups.health_check",
        ]

        pairs = []

        # self._module.fail_json(msg="Compare VRRP - want: " + str(want) + " (((()))) have:  " + str(have))

        if have.get("snmp") == "enabled" and want.get("snmp") != "enabled":
            self.commands.append("delete high-availability vrrp snmp")

        hlist = self._extract_leaf_items(have)
        wlist = self._extract_leaf_items(want)

        if self.state == "rendered":
            hlist = []
        # self._module.fail_json(msg="leaf VRRP - want: " + str(wlist) + " (((()))) have:  " + str(hlist))

        # self.compare(parsers=vrrp_parsers, want={}, have={"vrrp": have})

        if self.state in ["replaced", "deleted", "overridden"]:
            for hdict in hlist:
                wdict = self._find_matching_vrrp(hdict, wlist)
                # self._module.fail_json(msg=wdict)

                if self.state == "deleted" and wdict:
                    wdict = {}
                pairs.append((wdict, hdict))
                self.compare(parsers=vrrp_parsers, want={"vrrp": wdict}, have={"vrrp": hdict})
            # self._module.fail_json(msg=pairs)

        if self.state in ["merged", "replaced", "rendered"]:
            for wdict in wlist:
                hdict = self._find_matching_vrrp(wdict, hlist)
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
                if k == "name" or (k == "snmp" and v == "disabled"):
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

    def _find_matching_vsrv(self, want_item, have_list):

        def build_sig(item):
            if not isinstance(item, dict):
                return None

            name = item.get("name")
            if not name:
                return None

            # --- real_server case ---
            if "real_server" in item:
                rs = item["real_server"]
                if not isinstance(rs, dict) or "address" not in rs:
                    return None

                addr = rs["address"]

                # attribute path under real_server
                for k in rs:
                    if k != "address":
                        return ("real_server", name, addr, k)

                # address-only (rare but valid)
                return ("real_server", name, addr, None)

            # --- flat attribute ---
            for k in item:
                if k != "name":
                    return ("attr", name, k)

            return None

        sig_want = build_sig(want_item)

        for obj in have_list:
            if build_sig(obj) == sig_want:
                return obj

        return {}

    def _find_matching_vrrp(self, want_item, have_list):

        def build_sig(item):
            if not isinstance(item, dict) or not item:
                return ()

            container = next(iter(item))
            inner = item[container]

            sig = [container]

            # identity (group / sync_group name)
            if isinstance(inner, dict) and "name" in inner:
                sig.append(("name", inner["name"]))

            # find the real leaf
            if isinstance(inner, dict):
                for k, v in inner.items():
                    if k == "name":
                        continue

                    # flat leaf (e.g. vrid, address)
                    if not isinstance(v, dict):
                        sig.append(k)
                        break

                    # nested leaf (e.g. health_check.interval)
                    sig.append(k)
                    for leaf in v:
                        sig.append(leaf)
                        break
                    break

            return tuple(sig)

        sig_want = build_sig(want_item)

        for obj in have_list:
            if build_sig(obj) == sig_want:
                return obj

        return {}

    def _normalize_lists(self, node):
        """
        Recursively normalize all lists inside a dict or list.
        All lists are sorted to ensure consistent ordering for comparison.
        """
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, list):
                    # sort the list if it contains only scalars
                    if all(not isinstance(i, (dict, list)) for i in v):
                        node[k] = sorted(v)
                    else:
                        # recurse into each item if the list contains dicts
                        for item in v:
                            self._normalize_lists(item)
                elif isinstance(v, dict):
                    self._normalize_lists(v)
        elif isinstance(node, list):
            for item in node:
                self._normalize_lists(item)

    def project_structure(self, have, want):
        """
        Project the structure of `have` onto `want`.

        - Existing values in `want` are preserved
        - Missing paths are created with empty values
        """
        if not isinstance(have, dict):
            return want

        if want is None or not isinstance(want, dict):
            want = {}

        for key, have_val in have.items():
            if key not in want:
                want[key] = self.empty_like(have_val)
            else:
                want[key] = self.project_structure(have_val, want[key])

        return want

    def empty_like(self, value):
        if isinstance(value, dict):
            return {}
        if isinstance(value, list):
            return []
        return None

    def _extract_named_leafs(self, data, parent_name=None, prefix_key=None):
        results = []

        if prefix_key == "real_server" and isinstance(data, dict):
            for d, server_data in data.items():
                if not isinstance(server_data, dict):
                    continue

                address = server_data.get("address")
                if not address:
                    continue

                for k, v in server_data.items():
                    if k == "address":
                        continue

                    results.append(
                        {
                            "name": parent_name,
                            "real_server": {
                                "address": address,
                                k: v,
                            },
                        },
                    )
            return results

        # Generic dict handling
        if isinstance(data, dict):
            current_name = data.get("name", parent_name)

            for k, v in data.items():
                if k == "name":
                    continue

                results.extend(
                    self._extract_named_leafs(v, current_name, k),
                )

            return results

        # Primitive leaf
        return [
            {
                "name": parent_name,
                prefix_key: data,
            },
        ]

        # def _prune_stubs(self, w, h, path=None):
        #     wc = {}
        #     hc = self._remove_defaults(h)
        #     # if w:
        #     #     wc = self._remove_defaults(w)

        #     if not w and remove_empties(hc):
        #         self.commands = ["delete high-availability"]
        #         wc = {}
        #         hc = {}
        #     elif w:
        #         for k in w.keys():
        #             if path:
        #                 path = path + " " + k
        #             else:
        #                 path = k
        #             wg = w.get(k, {})
        #             hg = hc.get(k, {})
        #             wr = self._remove_defaults(wg)

        #             if (k in w and hg and (wg is not None and not isinstance(wg, (list, dict)))) or (
        #                 k in w and hg and isinstance(wg, (list, dict)) and not self._remove_defaults(wg)
        #             ):
        #                 # self._module.fail_json(msg="W " + str(self.want) + " H " + str(hg) + " K " + k)
        #                 self.commands.append("delete high-availability " + path)
        #                 wc.pop(k, {})
        #                 hc.pop(k, {})
        #             elif k in w and hg and isinstance(wg, dict) and self._remove_defaults(wg):
        #                 (wi, hi, path) = self._prune_stubs(wg, hg, path=k)
        #                 # self._module.fail_json(msg="W " + str(wi) + " H " + str(hi) + " K " + path)

        # return wc, hc, path

    def _prune_stubs(self, w, h, path=None):
        wc = {}
        hc = self._remove_defaults(h)  # This removes default values from 'h'

        if not w and remove_empties(hc):  # If 'w' is empty and hc has empty values
            self.commands = ["delete high-availability"]
            wc = {}
            hc = {}
        elif w:  # If there are keys to process in 'w'
            for k in w.keys():
                if path:
                    path = path + " " + k  # Create a path for nested keys
                else:
                    path = k

                wg = w.get(k, {})  # The wanted configuration for the key 'k'
                hg = hc.get(k, {})  # The current configuration for the key 'k'
                wr = self._remove_defaults(wg)  # Remove defaults from 'wg'

                # The pruning logic:
                if (k in w and hg and (wg is not None and not isinstance(wg, (list, dict)))) or (
                    k in w and hg and isinstance(wg, (list, dict)) and not self._remove_defaults(wg)
                ):
                    # If the condition is met, delete the high-availability setting
                    self.commands.append("delete high-availability " + path)
                    wc.pop(k, {})
                    hc.pop(k, {})
                elif k in w and hg and isinstance(wg, dict) and self._remove_defaults(wg):
                    # If 'wg' is a dict and not default, recurse into it
                    (wi, hi, path) = self._prune_stubs(wg, hg, path=k)
                    wc.update(wi)  # Add the result to the wc dictionary
                    hc.update(hi)  # Add the result to the hc dictionary
                elif k in w and hg and isinstance(wg, list) and self._remove_defaults(wg):
                    # Handle lists similarly, if applicable
                    if not wg:  # If the list is empty, remove the entry
                        self.commands.append("delete high-availability " + path)
                        wc.pop(k, {})
                        hc.pop(k, {})
                    else:
                        for idx, item in enumerate(wg):
                            item_path = f"{path} {idx}"
                            wi, hi, _ = self._prune_stubs(item, hg.get(k, []), path=item_path)
                            wc.update(wi)
                            hc.update(hi)

        return wc, hc, path

    def _remove_nulls(self, data):
        """Remove null values but keep empty containers."""
        if isinstance(data, dict):
            # Remove None values, keep empty dicts
            cleaned = {}
            for k, v in data.items():
                if v in [None, False, "disabled"]:
                    continue  # Skip null values
                cleaned[k] = self._remove_nulls(v)
            return cleaned
        return data

    def _remove_defaults(self, data):
        if isinstance(data, dict):
            cleaned = {}
            for k, v in data.items():
                if v in [None, False, "disabled"]:
                    continue
                v = self._remove_defaults(v)
                cleaned[k] = v
            return cleaned
        return data

    def _remove_nulls_keep_empty_parents(self, data):
        """Remove null/disabled/false/true but keep parent containers even if empty."""
        if isinstance(data, dict):
            cleaned = {}
            for k, v in data.items():
                if v in [None, False, "disabled"]:
                    continue
                v = self._remove_nulls_keep_empty_parents(v)
                cleaned[k] = v
            return cleaned
        return data
