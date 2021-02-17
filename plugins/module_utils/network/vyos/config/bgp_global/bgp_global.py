#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function
__metaclass__ = type

"""
The vyos_bgp_global config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""
import q
from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import (
    Facts,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.bgp_global import (
    Bgp_globalTemplate,
)


class Bgp_global(ResourceModule):
    """
    The vyos_bgp_global config class
    """

    def __init__(self, module):
        super(Bgp_global, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="bgp_global",
            tmplt=Bgp_globalTemplate(),
        )
        self.parsers = [
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """
        wantd = {}
        haved = {}

        if (
            self.want.get("as_number") == self.have.get("as_number")
            or not self.have
        ):
            if self.want:
                wantd = {self.want["as_number"]: self.want}
            if self.have:
                haved = {self.have["as_number"]: self.have}
        else:
            self._module.fail_json(
                msg="Only one bgp instance is allowed per device"
            )

        # turn all lists of dicts into dicts prior to merge
        for entry in wantd, haved:
            self._bgp_global_list_to_dict(entry)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self._compare(want={}, have=have)

        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Bgp_global network resource.
        """
        parsers = [
            "maximum_paths",
            "timers"
        ]
        self._compare_neighbor(want, have)
        self._compare_lists(want, have)
        self._compare_bgp_params(want, have)
        for name, entry in iteritems(want):
            if name != "as_number":
                self.compare(
                    parsers=parsers,
                    want={"as_number": want["as_number"], name: entry},
                    have={"as_number": want["as_number"], name: have.pop(name, {})},
                )
        for name, entry in iteritems(have):
            if name != "as_number":
                self.compare(
                    parsers=self.parsers, want={}, have={"as_number": have["as_number"], name: have.get(name)}
                )
                
    def _compare_neighbor(self, want, have):

        parsers = [
            "neighbor.advertisement_interval",
            "neighbor.allowas_in",
            "neighbor.as_override",
            "neighbor.attribute_unchanged.as_path",
            "neighbor.attribute_unchanged.med",
            "neighbor.attribute_unchanged.next_hop",
            "neighbor.capability_dynamic",
            "neighbor.capability_orf",
            "neighbor.default_originate",
            "neighbor.description",
            "neighbor.disable_capability_negotiation",
            "neighbor.disable_connected_check",
            "neighbor.disable_send_community",
            "neighbor.distribute_list",
            "neighbor.ebgp_multihop",
            "neighbor.filter_list",
            "neighbor.local_as",
            "neighbor.maximum_prefix",
            "neighbor.nexthop_self",
            "neighbor.override_capability",
            "neighbor.passive",
            "neighbor.password",
            "neighbor.peer_group_name",
            "neighbor.port",
            "neighbor.prefix_list",
            "neighbor.remote_as",
            "neighbor.remove_private_as",
            "neighbor.route_map",
            "neighbor.route_reflector_client",
            "neighbor.route_server_client",
            "neighbor.shutdown",
            "neighbor.soft_reconfiguration",
            "neighbor.strict_capability_match",
            "neighbor.unsuppress_map",
            "neighbor.update_source",
            "neighbor.weight",
            "neighbor.ttl_security",
            "neighbor.timers",
            "network.backdoor",
            "network.route_map"
        ]
        wneigh = want.pop("neighbor", {})
        hneigh = have.pop("neighbor", {})
        self._compare_neigh_lists(want, have)
        for name, entry in iteritems(wneigh):
            for k, v in entry.items():
                peer = entry["address"]
                if hneigh.get(name):
                    h = {"address": peer, k: hneigh[name].pop(k, {})}
                else:
                    h = {}
                self.compare(
                    parsers=parsers,
                    want={"as_number": want["as_number"], "neighbor": {"address": peer, k: v}},
                    have={"as_number": want["as_number"], "neighbor": h},
                )
        for name, entry in iteritems(hneigh):
            if name not in wneigh.keys():
                self.commands.append("no neighbor " + name)
                continue
            for k, v in entry.items():
                peer = entry["address"]
                self.compare(
                    parsers=parsers,
                    want={},
                    have={"as_number": have["as_number"], "neighbor": {"address": peer, k: v}},
                )

    def _compare_bgp_params(self, want, have):
        parsers = [
            "bgp_params.always_compare_med",
            "bgp_params.bestpath.as_path",
            "bgp_params.bestpath.compare_routerid",
            "bgp_params.bestpath.med",
            "bgp_params.cluster_id",
            "bgp_params.confederation",
            "bgp_params.dampening_half_life",
            "bgp_params.dampening_max_suppress_time",
            "bgp_params.dampening_re_use",
            "bgp_params.dampening_start_suppress_time",
            "bgp_params.default",
            "bgp_params.deterministic_med",
            "bgp_params.disbale_network_import_check",
            "bgp_params.distance.prefix",
            "bgp_params.distance.global",
            "bgp_params.enforce_first_as",
            "bgp_params.graceful_restart",
            "bgp_params.log_neighbor_changes",
            "bgp_params.no_client_to_client_reflection",
            "bgp_params.no_fast_external_failover",
            "bgp_params.routerid",
            "bgp_params.scan_time"
        ]
        wbgp = want.pop("bgp_params", {})
        hbgp = have.pop("bgp_params", {})
        for name, entry in iteritems(wbgp):
            if name == "confederation":
                if entry != hbgp.pop(name, {}):
                    self.addcmd({"as_number": want["as_number"], "bgp_params": {name: entry}}, "bgp_params.confederation", False) 
            else:
                self.compare(
                    parsers=parsers,
                    want={"as_number": want["as_number"], "bgp_params": {name: entry}},
                    have={"as_number": want["as_number"], "bgp_params": {name: hbgp.pop(name, {})}},
                )
        for name, entry in iteritems(hbgp):
            if name == "confederation":
                self.addcmd({"as_number": have["as_number"], "bgp_params": {name: entry}}, "bgp_params.confederation", True)
                hbgp.pop(name)
            self.compare(parsers=parsers, want={}, have={"as_number": have["as_number"], "bgp_params": {name: entry}})

    def _compare_lists(self, want, have):
        parsers = [
            "network.backdoor",
            "network.route_map",
            "redistribute.metric",
            "redistribute.route_map",
            "aggregate_address"
        ]
        for attrib in ["redistribute", "network", "aggregate_address"]:
            wdict = want.pop(attrib, {})
            hdict = have.pop(attrib, {})
            for key, entry in iteritems(wdict):
                q(key, entry, hdict.get(key, {}))
                if entry != hdict.get(key, {}):
                    self.compare(parsers=parsers, want={"as_number": want["as_number"], attrib: entry}, have=hdict.pop(key, {}))
                hdict.pop(key, {})
            # remove remaining items in have for replaced
            for key, entry in iteritems(hdict):
                self.compare(parsers=parsers, want={}, have={"as_number": have["as_number"], attrib: entry})

    def _compare_neigh_lists(self, want, have):
        parsers = [
            "neighbor.distribute_list",
            "neighbor.filter_list",
            "neighbor.prefix_list",
            "neighbor.route_map",
        ]
        for attrib in ["distribute_list", "filter_list", "prefix_list", "route_map"]:
            wdict = want.pop(attrib, {})
            hdict = have.pop(attrib, {})
            for key, entry in iteritems(wdict):
                if entry != hdict.pop(key, {}):
                    self.addcmd(entry, "neighbor.{0}".format(attrib), False)
            # remove remaining items in have for replaced
            for entry in hdict.values():
                self.addcmd(entry, "neighbor.{0}".format(attrib), True)

    def _bgp_global_list_to_dict(self, entry):
        for name, proc in iteritems(entry):
            if "neighbor" in proc:
                neigh_dict = {}
                for entry in proc.get("neighbor", []):
                    neigh_dict.update({entry["address"]: entry})
                proc["neighbor"] = neigh_dict

            if "network" in proc:
                network_dict = {}
                for entry in proc.get("network", []):
                    network_dict.update({entry["address"]: entry})
                proc["network"] = network_dict


            if "aggregate_address" in proc:
                agg_dict = {}
                for entry in proc.get("aggregate_address", []):
                    agg_dict.update({entry["address"]: entry})
                proc["aggregate_address"] = agg_dict

            if "redistribute" in proc:
                redis_dict = {}
                for entry in proc.get("redistribute", []):
                    redis_dict.update({entry["protocol"]: entry})
                proc["redistribute"] = redis_dict

