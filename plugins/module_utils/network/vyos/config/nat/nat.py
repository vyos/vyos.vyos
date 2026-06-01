#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_nat config file.
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
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.nat import (
    NatTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.utils import combine


# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
#     dict_merge,
# )


class Nat(ResourceModule):
    """
    The vyos_nat config class
    """

    def __init__(self, module):
        super(Nat, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="nat",
            tmplt=NatTemplate(),
        )
        self.parsers = [
            "nat.cgnat.log_allocation",
            "nat.cgnat.pool.external",
            # "nat.cgnat.pool.external.range",
            # "nat.cgnat.pool.external.external_port_range",
            # "nat.cgnat.pool.external.external_per_user",
            "nat.cgnat.pool.internal",
            "nat.cgnat.rule.source.pool",
            # "nat.cgnat.rule.translation",
            "nat_type_description",
            "nat_type_protocol",
            "nat_type_disable",
            "nat_type_exclude",
            "nat_type_log",
            "nat_type_address",
            "nat_type_prefix",
            "nat_type_fqdn",
            "nat_type_port",
            "nat_type_translation_address",
            "nat_type_translation_port",
            "nat_inbound_interface_name",
            "nat_inbound_interface_group",
            "nat_static_inbound_interface",
            "nat6x_inbound_interface",
            "nat_type_outbound_interface",
            "nat_type_outbound_interface_group",
            "nat_type_address_group",
            "nat_type_packet_type",
            "nat_type_lb_backend",
            "nat_type_lb_hash",
            "nat_type_translation_options",
            "nat_type_translation_redirect",
            "nat64_match_mark",
            "nat64_translation_pool_address",
            "nat64_translation_pool_description",
            "nat64_translation_pool_disable",
            "nat64_translation_pool_port",
            "nat64_translation_pool_protocol",
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
        wantd = {}
        haved = {}
        wantd = deepcopy(self.want)
        haved = deepcopy(self.have)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            # wantd = dict_merge(haved, wantd)
            wantd = combine(haved, wantd, recursive=True, list_merge="append_rp")
        self._normalize_pool_list_to_dict(wantd)
        # self._module.fail_json(msg={"want": wantd, " ******** have": haved},)
        # self._module.fail_json(msg={"merged": wantd, " ******** have": haved, "******** original want": self.want},)

        self.compare(parsers=self.parsers, want=wantd, have=haved)
        self._module.fail_json(msg={"commands": self.commands})

    def _normalize_pool_list_to_dict(self, config):
        """Convert pool.external and pool.internal from list to name-keyed dict."""
        cgnat = config.get("nat", {}).get("cgnat", {})
        pool = cgnat.get("pool", {})

        for pool_type in ("external", "internal"):
            entries = pool.get(pool_type)
            if isinstance(entries, list):
                pool[pool_type] = {item["name"]: item for item in entries}
