# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The vyos_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import Facts
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.interfaces import (
    InterfacesTemplate,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.utils.utils import (
    get_interface_type,
)


class Interfaces(ResourceModule):
    """
    The vyos_interfaces class
    """

    def __init__(self, module):
        super(Interfaces, self).__init__(
            empty_fact_val=[],
            facts_module=Facts(module),
            module=module,
            resource="interfaces",
            tmplt=InterfacesTemplate(),
        )
        self.parsers = ["description", "mtu", "duplex", "speed", "vrf"]
        self.vif_parsers = ["vifs.description", "vifs.mtu"]

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
        if self.state in ("merged", "replaced", "overridden", "rendered") and not self.want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(self.state),
            )

        wantd = self._list_to_dict(self.want)
        haved = self._list_to_dict(self.have)

        for name in wantd:
            if not get_interface_type(name):
                self._module.fail_json(
                    msg="interface {0} is not a valid interface type".format(name),
                )

        if self.state == "deleted":
            # reset the given interfaces, or all of them
            for name in wantd or haved:
                if name in haved:
                    self._compare(name, self._reset(name), haved[name])
            return

        if self.state == "overridden":
            for name, have in haved.items():
                if name not in wantd:
                    self._compare(name, self._reset(name), have)

        for name, want in wantd.items():
            # an interface not on the device yet keeps its wanted enabled state
            have = haved.get(name, {"name": name, "enabled": want.get("enabled", True)})
            if self.state in ("merged", "rendered"):
                want = dict_merge(have, want)
            self._compare(name, want, have)

    def _compare(self, name, want, have):
        """Compare one interface: its options, enabled, and its vifs."""
        base = {"name": name, "type": get_interface_type(name)}
        want = deepcopy(want)
        have = deepcopy(have)
        wvifs = want.pop("vifs", {}) or {}
        hvifs = have.pop("vifs", {}) or {}

        self.compare(parsers=self.parsers, want=dict(want, **base), have=dict(have, **base))
        self._compare_enabled(
            base,
            "disable",
            want.get("enabled", True),
            have.get("enabled", True),
        )

        for vlan_id, wvif in wvifs.items():
            hvif = hvifs.pop(vlan_id, {"vlan_id": vlan_id, "enabled": True})
            self.compare(
                parsers=self.vif_parsers,
                want=dict(base, vifs=wvif),
                have=dict(base, vifs=hvif),
            )
            self._compare_enabled(
                dict(base, vifs={"vlan_id": vlan_id}),
                "vifs.disable",
                wvif.get("enabled", True),
                hvif.get("enabled", True),
            )
        # vifs the configuration does not list are deleted as a whole
        for vlan_id in hvifs:
            self.addcmd(dict(base, vifs={"vlan_id": vlan_id}), "vifs", True)

    def _compare_enabled(self, data, parser, want, have):
        """enabled is the inverse of the disable flag: false sets it, true deletes it."""
        if want != have:
            self.addcmd(data, parser, want)

    def _reset(self, name):
        """The configuration of an interface without any options: enabled, no vifs."""
        return {"name": name, "enabled": True}

    def _list_to_dict(self, entries):
        """Interfaces by name, and their vifs by VLAN ID."""
        result = {}
        for entry in deepcopy(entries) or []:
            vifs = entry.get("vifs") or []
            entry["vifs"] = {vif["vlan_id"]: vif for vif in vifs}
            result[entry["name"]] = entry
        return result
