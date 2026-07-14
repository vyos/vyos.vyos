# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The vyos vpn_ipsec fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.vyos.vyos_test.plugins.module_utils.network.vyos.argspec.vpn_ipsec.vpn_ipsec import (
    Vpn_ipsecArgs,
)
from ansible_collections.vyos.vyos_test.plugins.module_utils.network.vyos.rm_templates.vpn_ipsec import (
    Vpn_ipsecTemplate,
)


class Vpn_ipsecFacts(object):
    """The vyos vpn_ipsec facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Vpn_ipsecArgs.argument_spec

    def get_vpn_ipsec_data(self, connection):
        return connection.get('show configuration commands | match "vpn ipsec"')

    def process_facts(self, objFinal):
        """Convert the name-keyed dicts produced by the parser into the
        lists the argspec expects (config: type dict, with ike_group/
        esp_group/profile/authentication.psk each: type list, elements
        dict). Mirrors logging_global's hosts/files/users conversion.
        """
        if not objFinal:
            return objFinal

        for key in ("ike_group", "esp_group", "profile"):
            if key in objFinal:
                items = list(objFinal[key].values())
                for item in items:
                    if "proposal" in item:
                        item["proposal"] = sorted(
                            item["proposal"].values(),
                            key=lambda p: int(p["proposal_id"]),
                        )
                objFinal[key] = sorted(items, key=lambda item: item["name"])

        if "authentication" in objFinal:
            auth = objFinal["authentication"]
            for key in ("psk", "ppk"):
                if key in auth:
                    auth[key] = sorted(
                        auth[key].values(),
                        key=lambda item: item["name"],
                    )

        return objFinal

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Vpn_ipsec network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}

        if not data:
            data = self.get_vpn_ipsec_data(connection)

        vpn_ipsec_parser = Vpn_ipsecTemplate(lines=data.splitlines(), module=self._module)
        objs = vpn_ipsec_parser.parse()

        ansible_facts["ansible_network_resources"].pop("vpn_ipsec", None)
        objs = self.process_facts(objs)

        params = utils.remove_empties(
            vpn_ipsec_parser.validate_config(
                self.argument_spec,
                {"config": objs},
                redact=True,
            ),
        )

        facts["vpn_ipsec"] = params.get("config", {})
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts
