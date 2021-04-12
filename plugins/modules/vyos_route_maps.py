#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_route_maps
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: vyos_route_maps
version_added: 2.0.2
short_description: Route Map Resource Module.
description:
- This module manages route map configurations on devices running VYOS.
author: Ashwini Mhatre (@amhatre)
notes:
- Tested against vyos 1.2.
- This module works with connection C(network_cli).
options:
    config:
      description: A list of route-map configuration.
      type: list
      elements: dict
      suboptions:
        route_map:
          description: Route map name.
          type: str
        entries:
          description: Route Map rules.
          aliases: rules
          type: list
          elements: dict
          suboptions:
            rule_number:
              type: int
              description: Route-map rule number
            call:
              description: Route map name
              type: str
            description:
              description: Description for the rule.
              type: str
            action:
              description: Action for matching routes
              type: str
              choices: ["deny", "permit"]
            continue:
              description: Route map rule number <1-65535>.
              type: int
            set:
              description: Route parameters.
              type: dict
              suboptions:
                aggregator:
                  type: dict
                  description: Border Gateway Protocol (BGP) aggregator attribute.
                  suboptions:
                    ip:
                      type: str
                      description: IP address.
                    as:
                      type: str
                      description: AS number of an aggregation.
                as_path_exclude:
                  type: str
                  description: BGP AS path exclude string ex "456 64500 45001"
                as_path_prepend:
                  type: str
                  description: Prepend string for a Border Gateway Protocol (BGP) AS-path attribute.
                atomic_aggregate:
                  type: bool
                  description:  Border Gateway Protocol (BGP) atomic aggregate attribute.
                bgp_extcommunity_rt:
                  type: str
                  description: ExtCommunity in format AS:value
                comm_list:
                  type: dict
                  description: Border Gateway Protocol (BGP) communities matching a community-list.
                  suboptions:
                    comm_list:
                      type: str
                      description: BGP communities with a community-list.
                    delete:
                      type: bool
                      description: Delete BGP communities matching the community-list.
                community:
                  type: dict
                  description: Border Gateway Protocl (BGP) community attribute.
                  suboptions:
                    value:
                      type: str
                      description: Community in 4 octet AS:value format.
                    local_AS:
                      type: bool
                      description: Advertise communities in local AS only (NO_EXPORT_SUBCONFED).
                    no_advertise:
                      type: bool
                      description: Don't advertise this route to any peer (NO_ADVERTISE)
                    no_expert:
                      type: bool
                      description: Don't advertise outside of this AS of confederation boundry (NO_EXPORT)
                    internet:
                      type: bool
                      description: Symbolic Internet community 0.
                    additive:
                      type: bool
                      description: Add the community instead of replacing existing communities.
                    none:
                      type: bool
                      description: none
                extcommunity_rt:
                  type: str
                  description: Set route target value.
                extcommunity_soo:
                  type: str
                  description: Set Site of Origin value.
                ip_next_hop:
                  type: str
                  description: IP address.
                ipv6_next_hop:
                  type: str
                  description: Nexthop IPv6 address.
                large_community:
                  type: str
                  description: Set BGP large community value.
                local_preference:
                  type: str
                  description: Border Gateway Protocol (BGP) local preference attribute.
                metric:
                  type: str
                  description: Destination routing protocol metric.
                metric_type:
                  type: str
                  choices: ['type-1', 'type-2']
                  description: Open Shortest Path First (OSPF) external metric-type.
                origin:
                  description: Set bgp origin.
                  type: str
                  choices: [ "ebgp", "ibgp", "incomplete" ]
                originator_id:
                  type: str
                  description: Border Gateway Protocol (BGP) originator ID attribute.
                src:
                  type: str
                  description: Source address for route.
                tag:
                  type: str
                  description: Tag value for routing protocol
                weight:
                  type: str
                  description: Border Gateway Protocol (BGP) weight attribute.
            match:
              description: Route parameters to match.
              type: dict
              suboptions:
                as_path:
                  description: Set as-path.
                  type: str
                community:
                  description: BGP community attribute.
                  type: dict
                  suboptions:
                    community_list:
                      description: BGP community-list to match
                      type: str
                    exact_match:
                      description:  BGP community-list to match
                      type: bool
                extcommunity:
                  description: Extended community name.
                  type: str
                interface:
                  description: First hop interface of a route to match.
                  type: str
                ip:
                  description: IP prefix parameters to match.
                  type: dict
                  suboptions:
                    address:
                      description: IP address of route to match.
                      type: dict
                      suboptions:
                        access_list: &access_list
                          description: IP access-list to match.
                          type: int
                        prefix_list: &prefix_list
                          description: IP prefix-list to match
                          type: str
                    next_hop:
                      description: next hop prefix list.
                      type: dict
                      suboptions:
                        access_list: *access_list
                        prefix_list: *prefix_list
                    route_source:
                      description: IP route-source to match
                      type: dict
                      suboptions:
                        access_list: *access_list
                        prefix_list: *prefix_list
                ipv6:
                  description: IPv6 prefix parameters to match.
                  type: dict
                  suboptions:
                    address:
                      description: IPv6 address of route to match.
                      type: dict
                      suboptions:
                        access_list:
                          description: IPv6 access-list to match.
                          type: str
                        prefix_list:
                          description: IPv6 prefix-list to match
                          type: str
                    next_hop:
                      description: next-hop ipv6 address IPv6 <h:h:h:h:h:h:h:h>.
                      type: str
                large_community_large_community_list:
                  type: str
                  description: BGP large-community-list to match.
                metric:
                  description: Route metric <1-65535>.
                  type: int
                origin:
                  description: bgp origin.
                  type: str
                  choices: [ "ebgp", "ibgp", "incomplete" ]
                peer:
                  type: str
                  description: Peer IP address <x.x.x.x>.
                rpki:
                  type: dict
                  description: Match RPKI validation result.
                  suboptions:
                    rpki_validation:
                      type: str
                      description: Match RPKI validation result.
                    valid:
                      type: bool
                      description: valid rpki.
                    invalid:
                      type: bool
                      description: invalid rpki.
                    notfound:
                      type: bool
                      description: notfound rpki.
                    tag:
                      type: int
                      description: Route tag <1-65535>
            on_match:
              type: dict
              description: Exit policy on matches.
              suboptions:
                next:
                  type: bool
                  description: Next sequence number to goto on match.
                goto:
                  type: int
                  description: Rule number to goto on match <1-65535>.
    running_config:
      description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VYOS device by
        executing the command B(show configuration commands | grep route-map).
      - The state I(parsed) reads the configuration from C(show configuration commands | grep route-map) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
      type: str
    state:
      description:
      - The state the configuration should be left in.
      type: str
      choices:
      - deleted
      - merged
      - overridden
      - replaced
      - gathered
      - rendered
      - parsed
      default: merged
"""
EXAMPLES = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.route_maps.route_maps import (
    Route_mapsArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.route_maps.route_maps import (
    Route_maps,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Route_mapsArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Route_maps(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
