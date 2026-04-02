#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_ha config file.
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
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.ha import (
    HaTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.utils import combine
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.version import (
    LooseVersion,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos import get_os_version


class Ha(ResourceModule):
    """
    The vyos_ha config class
    """

    def __init__(self, module):
        super(Ha, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="ha",
            tmplt=HaTemplate(),
        )
        self.parsers = [
            "disable",
        ]

    def _validate_template(self):
        version = get_os_version(self._module)
        if LooseVersion(version) >= LooseVersion("1.4"):
            self._tmplt = HaTemplate()
        else:
            self._module.fail_json(msg="High Availability is not supported in this version of VyOS")

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
            wantd = {"disable": False}
            haved = deepcopy(self.have)
            if wantd != haved:
                self.commands = ["delete high-availability"]
            self.run_commands()
        if "before" in self.result:
            self._normalize_lists(self.result["before"])
        if "after" in self.result:
            self._normalize_lists(self.result["after"])
        if "parsed" in self.result:
            self._normalize_lists(self.result["parsed"])
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
            self._vrrp_groups_list_to_dict(entry)
            self._virtual_servers_list_to_dict(entry)
            self._vrrp_sync_groups_list_to_dict(entry)
            self._normalize_lists(entry)

        if self.state in ["deleted"]:
            wantd, haved, p = self._prune_stubs(self._module.params.get("config", {}), haved)

        if self.state in ["overridden"]:
            wo = deepcopy(wantd)
            self._diff_w_h(wo, haved)

            haved_disable = haved.get("disable")

            for k1, v1 in wo.items():

                if not isinstance(v1, dict):
                    continue

                for name, obj in v1.items():
                    if isinstance(obj, dict) and not obj:
                        wi, hi, pi = self._prune_stubs({k1: {name: {}}}, haved)
                        haved = hi

                for k2, v2 in v1.items():
                    if not isinstance(v2, dict):
                        continue

                    for name, obj in v2.items():
                        if isinstance(obj, dict) and not obj:
                            wi, hi, pi = self._prune_stubs({k1: {k2: {name: {}}}}, haved)
                            haved = hi

            if haved_disable is not None:
                haved["disable"] = haved_disable

        keys = set(wantd) | set(haved)

        for k in keys:

            want = wantd.get(k, {})
            have = haved.get(k, {})

            if k == "vrrp":
                if self.state in ["merged"]:
                    want = combine(have, want, recursive=True, list_merge="append_rp")
                self._compare_vrrp(want, have)

            if k == "virtual_servers":
                if self.state in ["merged"]:
                    want = combine(have, want, recursive=True)
                self._compare_vsrvs(want, have)

            if self.state in ["deleted"] and k == "disable":
                want = have
            if self.state in ["overridden"] and k == "disable" and not want:
                want = False
            if self.state in ["rendered"]:
                have = None

            self.compare(
                parsers=self.parsers,
                want={k: want},
                have={k: have},
            )

        self.commands = sorted(list(dict.fromkeys(self.commands)))

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

        hlist = self._extract_named_leafs(have)
        wlist = self._extract_named_leafs(want)

        if self.state == "rendered":
            hlist = []

        if self.state in ["replaced", "deleted"]:
            for hdict in hlist:
                wdict = self._find_matching_vsrv(hdict, wlist)
                if self.state == "deleted" and wdict:
                    wdict = {}
                elif not wdict:
                    hdict = {}
                self.compare(
                    parsers=vs_parsers,
                    want={"virtual_servers": wdict},
                    have={"virtual_servers": hdict},
                )
        if self.state in ["merged", "replaced", "rendered", "overridden"]:
            for wdict in wlist:
                hdict = self._find_matching_vsrv(wdict, hlist)
                self.compare(
                    parsers=vs_parsers,
                    want={"virtual_servers": wdict},
                    have={"virtual_servers": hdict},
                )

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
            "vrrp.groups.address",
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

        if (
            have.get("snmp") == "enabled"
            and want.get("snmp") != "enabled"
            and self.state not in ["deleted", "overridden"]
        ):
            self.commands.append("delete high-availability vrrp snmp")

        hlist = self._extract_leaf_items(have)
        wlist = self._extract_leaf_items(want)

        if self.state == "rendered":
            hlist = []

        if self.state in ["replaced", "deleted"]:
            for hdict in hlist:
                wdict = self._find_matching_vrrp(hdict, wlist)

                if self.state == "deleted" and wdict:
                    wdict = {}
                if self.state == "replaced" and wdict and wdict != hdict:
                    wdict = {}
                elif not wdict:
                    hdict = {}

                self.compare(parsers=vrrp_parsers, want={"vrrp": wdict}, have={"vrrp": hdict})

        if self.state in ["merged", "replaced", "rendered", "overridden"]:

            for wdict in wlist:
                hdict = self._find_matching_vrrp(wdict, hlist)
                self.compare(parsers=vrrp_parsers, want={"vrrp": wdict}, have={"vrrp": hdict})

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

            if "real_server" in item:
                rs = item["real_server"]
                if not isinstance(rs, dict) or "address" not in rs:
                    return None

                addr = rs["address"]

                for k in rs:
                    if k != "address":
                        return ("real_server", name, addr, k)

                return ("real_server", name, addr, None)

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

            if isinstance(inner, dict) and "name" in inner:
                sig.append(("name", inner["name"]))

            if isinstance(inner, dict):
                for k, v in inner.items():
                    if k == "name":
                        continue

                    if not isinstance(v, dict):
                        sig.append(k)
                        break

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
                    if all(not isinstance(i, (dict, list)) for i in v):
                        node[k] = sorted(v)
                    else:
                        for item in v:
                            self._normalize_lists(item)
                elif isinstance(v, dict):
                    self._normalize_lists(v)
        elif isinstance(node, list):
            for item in node:
                self._normalize_lists(item)

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

        if isinstance(data, dict):
            current_name = data.get("name", parent_name)

            for k, v in data.items():
                if k == "name":
                    continue

                results.extend(
                    self._extract_named_leafs(v, current_name, k),
                )

            return results

        return [
            {
                "name": parent_name,
                prefix_key: data,
            },
        ]

    def _prune_stubs(self, w, h, path=""):
        wc = {}
        hc = self._remove_defaults(h)

        if not self._remove_defaults(w) and remove_empties(hc):
            self.commands = ["delete high-availability"]
            return {}, {}, path

        for k, wg in (self._remove_defaults(w) or {}).items():
            next_path = f"{path} {k}".strip()
            stub = self._cli_path(next_path)
            hg = remove_empties(hc).get(k)

            if hg is None:
                continue

            if not isinstance(wg, (dict, list)):
                self.commands.append(f"delete high-availability {stub}")
                hc.pop(k, None)
                wc.pop(k, None)
                continue

            if not wg:
                self.commands.append(f"delete high-availability {stub}")
                hc.pop(k, None)
                wc.pop(k, None)
                continue

            if isinstance(wg, list) and isinstance(hg, dict):
                for item in wg:
                    name = item.get("name")
                    if not name:
                        continue

                    if name in hg:
                        self.commands.append(
                            f"delete high-availability {stub} {name}",
                        )

                        hg.pop(name, None)

                if hg:
                    hc[k] = hg
                else:
                    hc.pop(k, None)

                if self._remove_defaults(wg):
                    wc[k] = wg
                else:
                    wc.pop(k, None)

                continue

            if isinstance(wg, dict) and isinstance(hg, dict):
                wi, hi, p = self._prune_stubs(wg, hg, next_path)

                if wi:
                    wc[k] = wi

                if hi:
                    hc[k] = hi
                else:
                    hc.pop(k, None)

        return wc, hc, path

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

    def _cli_path(self, path):
        token_map = {
            "groups": "group",
            "sync_groups": "sync-group",
            "virtual_servers": "virtual-server",
        }

        parts = []
        for p in path.split():
            p = token_map.get(p, p)
            parts.append(p.replace("_", "-"))

        return " ".join(parts)

    def _diff_w_h(self, w, h):

        NAMED_OBJECT_KEYS = {
            "groups",
            "sync_groups",
            "virtual_servers",
            "global_parameters",
        }

        if not isinstance(w, dict) or not isinstance(h, dict):
            return w

        for key in w.keys() & h.keys():
            wv = w[key]
            hv = h[key]

            if key in NAMED_OBJECT_KEYS and isinstance(wv, dict) and isinstance(hv, dict):
                for name in wv.keys() & hv.keys():
                    if wv[name] != hv[name] and isinstance(wv[name], (dict, list)):
                        wv[name] = {}
                    elif wv[name] != hv[name]:
                        wv[name] = None
                continue
            self._diff_w_h(wv, hv)
        return w
