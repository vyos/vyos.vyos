#
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos vpn_ipsec_s2s fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.

Follows the established per-key conversion convention used by
vyos_logging_global/vyos_ha/vyos_vpn_ipsec (explicit process_facts()
naming each name-keyed dict that needs converting to a list), matching
the config.py convention for this module, rather than a generic
argspec-driven walker.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vpn_ipsec_s2s.vpn_ipsec_s2s import (
    Vpn_ipsec_s2sArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.vpn_ipsec_s2s import (
    Vpn_ipsec_s2sTemplate,
)


class Vpn_ipsec_s2sFacts(object):
    """The vyos vpn_ipsec_s2s facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Vpn_ipsec_s2sArgs.argument_spec

    def get_vpn_ipsec_s2s_data(self, connection):
        return connection.get(
            'show configuration commands | match "vpn ipsec site-to-site"',
        )

    def process_facts(self, objFinal):
        """Convert the name-keyed dicts produced by the parser into the
        lists the argspec expects.

        NOTE: every PARSERS result template in rm_templates.py nests its
        output under "site_to_site" -> "peer" (mirroring the CLI's own
        tree: `vpn ipsec site-to-site peer <name> ...`), but the
        argspec's `config` has `peer` directly at the top level -- there
        is no `site_to_site` wrapper in the argspec, since that's the
        one node wrap_docstring.py unwrapped when building the
        docstring (its own children became config's children directly).
        So this needs to strip that outer key, not just convert the
        name-keyed dicts to lists.
        """
        if not objFinal:
            return objFinal

        site_to_site = objFinal.get("site_to_site", {})
        peers = site_to_site.get("peer", {})

        items = list(peers.values())
        for item in items:
            if "tunnel" in item:
                item["tunnel"] = sorted(
                    item["tunnel"].values(),
                    key=lambda t: int(t["tunnel_id"]),
                )

        return {"peer": sorted(items, key=lambda item: item["name"])}

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Vpn_ipsec_s2s network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}

        if not data:
            data = self.get_vpn_ipsec_s2s_data(connection)

        vpn_ipsec_s2s_parser = Vpn_ipsec_s2sTemplate(
            lines=data.splitlines(),
            module=self._module,
        )
        objs = vpn_ipsec_s2s_parser.parse()

        ansible_facts["ansible_network_resources"].pop("vpn_ipsec_s2s", None)
        objs = self.process_facts(objs)

        params = utils.remove_empties(
            vpn_ipsec_s2s_parser.validate_config(
                self.argument_spec,
                {"config": objs},
                redact=True,
            ),
        )

        facts["vpn_ipsec_s2s"] = params.get("config", {})
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts
