#
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos_vpn_ipsec config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.

Command generation is delegated entirely to the generic, argspec-driven
generic_compare() engine in module_utils/utils/generic_nested_resource_v2.py
-- no field name (ike_group, esp_group, profile, proposal_id, encryption,
...) appears in this file. If the VyOS CLI structure changes in a future
release, only the docstring/argspec and the rm_template PARSERS need
updating; this file should not need to change for that alone.

KNOWN GAPS (see generic_nested_resource_v2.py docstring / conversation
history for detail):
  - "replaced" and "overridden" are currently treated identically. For
    this singleton-style resource (one config object per device) that's
    likely correct, but hasn't been deliberately confirmed against real
    device behaviour the way merged/deleted/idempotency have been.
  - No signature-based multi-field identity (every list[dict] node in
    this module has a single clean identity field, so this hasn't been
    needed yet -- would require extending generic_nested_resource_v2 if
    a future nested list here doesn't).
  - Bool-field handling (disable_uniqreqids, compression, disable_rekey,
    etc.) is implemented but not yet exercised against real fixture data.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)

# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
#     dict_merge,
# )
from ansible_collections.vyos.vyos_test.plugins.module_utils.network.vyos.argspec.vpn_ipsec.vpn_ipsec import (
    Vpn_ipsecArgs,
)
from ansible_collections.vyos.vyos_test.plugins.module_utils.network.vyos.facts.facts import (
    Facts,
)
from ansible_collections.vyos.vyos_test.plugins.module_utils.network.vyos.rm_templates.vpn_ipsec import (
    Vpn_ipsecTemplate,
)
from ansible_collections.vyos.vyos_test.plugins.module_utils.network.vyos.utils.generic_nested_resource_v2 import (
    generic_compare,
)


class Vpn_ipsec(ResourceModule):
    """
    The vyos_vpn_ipsec config class
    """

    def __init__(self, module):
        super(Vpn_ipsec, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vpn_ipsec",
            tmplt=Vpn_ipsecTemplate(),
        )
        self._spec = Vpn_ipsecArgs.argument_spec["config"]["options"]

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

        This is a singleton resource (one `config` dict per device, with
        named collections nested inside it), not a list of top-level
        named resources -- so `self.want`/`self.have` are single dicts,
        not lists to key by `name`. `generic_compare()` handles the
        merged/replaced/overridden/deleted/rendered branching internally
        via `self.state`; this method only needs to shape `wantd` for the
        "deleted" case (force empty) before handing off.
        """
        wantd = self.want or {}
        haved = self.have or {}

        if self.state == "deleted":
            wantd = {}

        # NOTE: unlike merged's dict_merge in the old design, we do NOT
        # merge want onto have here -- generic_compare()'s own per-item
        # equality short-circuit and per-state branching (see
        # generic_nested_resource_v2.generic_compare, state == "merged"
        # branch: `all_ids = set(w_items)`, i.e. only touch what's named
        # in want) already produces correct merged-state behaviour
        # without needing a pre-merged wantd. Merging here first would
        # actually break the multi-value list diffing (want would already
        # contain have's values, masking real removals-within-merge).
        generic_compare(self, self._spec, wantd, haved)
