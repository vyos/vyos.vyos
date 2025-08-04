#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_vrf
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_vrf
version_added: 1.0.0
short_description: VRF resource module
description:
- This module manages vrf configuration on devices running Vyos
author:
- Evgeny Molotkov (@omnom62)
notes:
- Tested against vyos 1.4.2 and 1.5-stream-2025-Q1
- This module works with connection C(network_cli).
options:
  config:
    description: List of vrf configuration.
    type: dict
    suboptions:
      bind_to_all:
        default: false
        description: Enable binding services to all VRFs
        type: bool
      instances:
        description: Virtual Routing and Forwarding instance
        type: list
        elements: dict
        suboptions:
          name:
            description: VRF instance name
            required: true
            type: str
          description:
            description: Description
            type: str
          disable:
            default: false
            description: Administratively disable interface
            type: bool
            aliases: ['disabled']
          table_id:
            description: Routing table associated with this instance
            type: int
          vni:
            description: Virtual Network Identifier
            type: int
          address_family:
            type: list
            elements: dict
            description: Address family configuration
            suboptions:
              afi:
                description: Address family identifier
                type: str
                choices: ['ipv4', 'ipv6']
              disable_forwarding:
                default: False
                description: Disable forwarding for this address family
                type: bool
              nht_no_resolve_via_default:
                default: False
                description: Disable next-hop resolution via default route
                type: bool
              route_maps:
                description: List of route maps for this address family
                type: list
                elements: dict
                suboptions:
                  rm_name:
                    description: Route map name
                    type: str
                    required: true
                  protocol:
                    description: Protocol to which the route map applies
                    type: str
                    choices:
                    - any
                    - babel
                    - bgp
                    - connected
                    - eigrp
                    - isis
                    - kernel
                    - ospf
                    - rip
                    - static
                    - table
          protocols:
            # type: list # sanity
            # elements: dict
            type: dict
            description: Protocol configuration
            suboptions:
              bgp:
                type: dict
                description: BGP configuration
                suboptions:
                  as_number:
                    description:
                    - AS number.
                    type: int
                  #maximum_paths: --> moved to address-family before 1.3
                  neighbor:
                    description: BGP neighbor
                    type: list
                    elements: dict
                    suboptions:
                      address:
                        description:
                        - BGP neighbor address (v4/v6).
                        type: str
                      advertisement_interval:
                        description:
                        - Minimum interval for sending routing updates.
                        type: int
                      capability:
                        description:
                        - Advertise capabilities to this neighbor.
                        type: dict
                        suboptions:
                          dynamic:
                            description:
                            - Advertise dynamic capability to this neighbor.
                            type: bool
                          extended_nexthop:
                            description:
                            - Advertise extended nexthop capability to this neighbor.
                            type: bool
                      default_originate:
                        description:
                        - Send default route to this neighbor
                        type: str
                      description:
                        description:
                        - Description of the neighbor
                        type: str
                      disable_capability_negotiation:
                        description:
                        - Disbale capability negotiation with the neighbor
                        type: bool
                      disable_connected_check:
                        description:
                        - Disable check to see if EBGP peer's address is a connected route.
                        type: bool
                      disable_send_community:
                        description:
                        - Disable sending community attributes to this neighbor.
                        type: str
                        choices: ['extended', 'standard']
                      ebgp_multihop:
                        description:
                          - Allow this EBGP neighbor to not be on a directly connected network. Specify
                            the number hops.
                        type: int
                      local_as:
                        description: local as number not to be prepended to updates from EBGP peers
                        type: int
                      override_capability:
                        description: Ignore capability negotiation with specified neighbor.
                        type: bool
                      passive:
                        description: Do not initiate a session with this neighbor
                        type: bool
                      password:
                        description: BGP MD5 password
                        type: str
                      peer_group_name:
                        description: IPv4 peer group for this peer
                        type: str
                      peer_group:
                        description: True if all the configs under this neighbor key is for peer group template.
                        type: bool
                      port:
                        description: Neighbor's BGP port
                        type: int
                      remote_as:
                        description: Neighbor BGP AS number
                        type: int
                      shutdown:
                        description: Administratively shut down neighbor
                        type: bool
                      solo: # <-- added in 1.3
                        description: Do not send back prefixes learned from the neighbor
                        type: bool
                      strict_capability_match:
                        description: Enable strict capability negotiation
                        type: bool
                      timers:
                        description: Neighbor timers
                        type: dict
                        suboptions:
                          connect:
                            description: BGP connect timer for this neighbor.
                            type: int
                          holdtime:
                            description: BGP hold timer for this neighbor
                            type: int
                          keepalive:
                            description: BGP keepalive interval for this neighbor
                            type: int
                      ttl_security:
                        description: Number of the maximum number of hops to the BGP peer
                        type: int
                      update_source:
                        description: Source IP of routing updates
                        type: str
                  timers:
                    description: BGP protocol timers
                    type: dict
                    suboptions:
                      keepalive:
                        description: Keepalive interval
                        type: int
                      holdtime:
                        description: Hold time interval
                        type: int
                  bgp_params:
                    description: BGP parameters
                    type: dict
                    suboptions:
                      always_compare_med:
                        description: Always compare MEDs from different neighbors
                        type: bool
                      bestpath:
                        description: Default bestpath selection mechanism
                        type: dict
                        suboptions:
                          as_path:
                            description: AS-path attribute comparison parameters
                            type: str
                            choices: ['confed', 'ignore']
                          compare_routerid:
                            description: Compare the router-id for identical EBGP paths
                            type: bool
                          med:
                            description: MED attribute comparison parameters
                            type: str
                            choices: ['confed', 'missing-as-worst']
                      cluster_id:
                        description: Route-reflector cluster-id
                        type: str
                      confederation:
                        description: AS confederation parameters
                        type: list
                        elements: dict
                        suboptions:
                          identifier:
                            description: Confederation AS identifier
                            type: int
                          peers:
                            description: Peer ASs in the BGP confederation
                            type: int
                      dampening:
                        description: Enable route-flap dampening
                        type: dict
                        suboptions:
                          half_life:
                            description: Half-life penalty in seconds
                            type: int
                          max_suppress_time:
                            description: Maximum duration to suppress a stable route
                            type: int
                          re_use:
                            description: Time to start reusing a route
                            type: int
                          start_suppress_time:
                            description: When to start suppressing a route
                            type: int
                      default:
                        description: BGP defaults
                        type: dict
                        suboptions:
                          local_pref:
                            description: Default local preference
                            type: int
                          no_ipv4_unicast:
                            description: |
                              Deactivate IPv4 unicast for a peer by default
                              Deprecated: Unavailable after 1.4
                            type: bool
                      deterministic_med:
                        description: Compare MEDs between different peers in the same AS
                        type: bool
                      disable_network_import_check:
                        description: Disable IGP route check for network statements
                        type: bool
                      distance:
                        description: Administrative distances for BGP routes
                        type: list
                        elements: dict
                        suboptions:
                          type:
                            description: Type of route
                            type: str
                            choices: ['external', 'internal', 'local']
                          value:
                            description: distance
                            type: int
                          prefix:
                            description: Administrative distance for a specific BGP prefix
                            type: int
                      enforce_first_as:
                        description: Require first AS in the path to match peer's AS
                        type: bool
                      graceful_restart:
                        description: Maximum time to hold onto restarting peer's stale paths
                        type: int
                      log_neighbor_changes:
                        description: Log neighbor up/down changes and reset reason
                        type: bool
                      no_client_to_client_reflection:
                        description: Disable client to client route reflection
                        type: bool
                      no_fast_external_failover:
                        description: Disable immediate session reset if peer's connected link goes down
                        type: bool
                      router_id:
                        description: BGP router-id
                        type: str
                      scan_time:
                        description: BGP route scanner interval
                        type: int
              ospf:
                type: dict
                description: OSPFv2 configuration
                suboptions:
                  areas:
                    description: OSPFv2 area.
                    type: list
                    elements: dict
                    suboptions:
                      area_id:
                        description: OSPFv2 area identity.
                        type: str
                      area_type:
                        description: Area type.
                        type: dict
                        suboptions:
                          normal:
                            description: Normal OSPFv2 area.
                            type: bool
                          nssa:
                            description: NSSA OSPFv2 area.
                            type: dict
                            suboptions:
                              set:
                                description: Enabling NSSA.
                                type: bool
                              default_cost:
                                description: Summary-default cost of NSSA area.
                                type: int
                              no_summary:
                                description: Do not inject inter-area routes into stub.
                                type: bool
                              translate:
                                description: NSSA-ABR.
                                type: str
                                choices: [always, candidate, never]
                          stub:
                            description: Stub OSPFv2 area.
                            type: dict
                            suboptions:
                              set:
                                description: Enabling stub.
                                type: bool
                              default_cost:
                                description: Summary-default cost of stub area.
                                type: int
                              no_summary:
                                description: Do not inject inter-area routes into stub.
                                type: bool
                      authentication:
                        description: OSPFv2 area authentication type.
                        type: str
                        choices: [plaintext-password, md5]
                      network:
                        description: OSPFv2 network.
                        type: list
                        elements: dict
                        suboptions:
                          address:
                            required: true
                            description: OSPFv2 IPv4 network address.
                            type: str
                      range:
                        description: Summarize routes matching prefix (border routers only).
                        type: list
                        elements: dict
                        suboptions:
                          address:
                            description: border router IPv4 address.
                            type: str
                          cost:
                            description: Metric for this range.
                            type: int
                          not_advertise:
                            description: Don't advertise this range.
                            type: bool
                          substitute:
                            description: Announce area range (IPv4 address) as another prefix.
                            type: str
                      shortcut:
                        description: Area's shortcut mode.
                        type: str
                        choices: [default, disable, enable]
                      virtual_link:
                        description: Virtual link address.
                        type: list
                        elements: dict
                        suboptions:
                          address:
                            description: virtual link address.
                            type: str
                          authentication:
                            description: OSPFv2 area authentication type.
                            type: dict
                            suboptions:
                              md5:
                                description: MD5 key id based authentication.
                                type: list
                                elements: dict
                                suboptions:
                                  key_id:
                                    description: MD5 key id.
                                    type: int
                                  md5_key:
                                    description: MD5 key.
                                    type: str
                              plaintext_password:
                                description: Plain text password.
                                type: str
                          dead_interval:
                            description: Interval after which a neighbor is declared dead.
                            type: int
                          hello_interval:
                            description: Interval between hello packets.
                            type: int
                          retransmit_interval:
                            description: Interval between retransmitting lost link state advertisements.
                            type: int
                          transmit_delay:
                            description: Link state transmit delay.
                            type: int
                  log_adjacency_changes:
                    description: Log changes in adjacency state.
                    type: str
                    choices: [detail]
                  max_metric:
                    description: OSPFv2 maximum/infinite-distance metric.
                    type: dict
                    suboptions:
                      router_lsa:
                        description: Advertise own Router-LSA with infinite distance (stub router).
                        type: dict
                        suboptions:
                          administrative:
                            description: Administratively apply, for an indefinite period.
                            type: bool
                          on_shutdown:
                            description: Time to advertise self as stub-router.
                            type: int
                          on_startup:
                            description: Time to advertise self as stub-router
                            type: int
                  auto_cost:
                    description: Calculate OSPFv2 interface cost according to bandwidth.
                    type: dict
                    suboptions:
                      reference_bandwidth:
                        description: Reference bandwidth cost in Mbits/sec.
                        type: int
                  default_information:
                    description: Control distribution of default information.
                    type: dict
                    suboptions:
                      originate:
                        description: Distribute a default route.
                        type: dict
                        suboptions:
                          always:
                            description: Always advertise default route.
                            type: bool
                          metric:
                            description: OSPFv2 default metric.
                            type: int
                          metric_type:
                            description: OSPFv2 Metric types for default routes.
                            type: int
                          route_map:
                            description: Route map references.
                            type: str
                  default_metric:
                    description: Metric of redistributed routes
                    type: int
                  distance:
                    description: Administrative distance.
                    type: dict
                    suboptions:
                      global:
                        description: Global OSPFv2 administrative distance.
                        type: int
                      ospf:
                        description: OSPFv2 administrative distance.
                        type: dict
                        suboptions:
                          external:
                            description: Distance for external routes.
                            type: int
                          inter_area:
                            description: Distance for inter-area routes.
                            type: int
                          intra_area:
                            description: Distance for intra-area routes.
                            type: int
                  mpls_te:
                    description: MultiProtocol Label Switching-Traffic Engineering (MPLS-TE) parameters.
                    type: dict
                    suboptions:
                      enabled:
                        description: Enable MPLS-TE functionality.
                        type: bool
                      router_address:
                        description: Stable IP address of the advertising router.
                        type: str
                  neighbor:
                    description: Neighbor IP address.
                    type: list
                    elements: dict
                    suboptions:
                      neighbor_id:
                        description: Identity (number/IP address) of neighbor.
                        type: str
                      poll_interval:
                        description: Seconds between dead neighbor polling interval.
                        type: int
                      priority:
                        description: Neighbor priority.
                        type: int
                  parameters:
                    description: OSPFv2 specific parameters.
                    type: dict
                    suboptions:
                      abr_type:
                        description: OSPFv2 ABR Type.
                        type: str
                        choices: [cisco, ibm, shortcut, standard]
                      opaque_lsa:
                        description: Enable the Opaque-LSA capability (rfc2370).
                        type: bool
                      rfc1583_compatibility:
                        description: Enable rfc1583 criteria for handling AS external routes.
                        type: bool
                      router_id:
                        description: Override the default router identifier.
                        type: str
                  passive_interface:
                    description: Suppress routing updates on an interface.
                    type: list
                    elements: str
                  passive_interface_exclude:
                    description: Interface to exclude when using passive-interface default.
                    type: list
                    elements: str
                  redistribute:
                    description: Redistribute information from another routing protocol.
                    type: list
                    elements: dict
                    suboptions:
                      route_type:
                        description: Route type to redistribute.
                        type: str
                        choices: [bgp, connected, kernel, rip, static]
                      metric:
                        description: Metric for redistribution routes.
                        type: int
                      metric_type:
                        description: OSPFv2 Metric types.
                        type: int
                      route_map:
                        description: Route map references.
                        type: str
                  route_map:
                    description: Filter routes installed in local route map.
                    type: list
                    elements: str
                  timers:
                    description: Adjust routing timers.
                    type: dict
                    suboptions:
                      refresh:
                        description: Adjust refresh parameters.
                        type: dict
                        suboptions:
                          timers:
                            description: refresh timer.
                            type: int
                      throttle:
                        description: Throttling adaptive timers.
                        type: dict
                        suboptions:
                          spf:
                            description: OSPFv2 SPF timers.
                            type: dict
                            suboptions:
                              delay:
                                description: Delay (msec) from first change received till SPF
                                  calculation.
                                type: int
                              initial_holdtime:
                                description: Initial hold time(msec) between consecutive SPF calculations.
                                type: int
                              max_holdtime:
                                description: maximum hold time (sec).
                                type: int
              ospfv3:
                type: dict
                description: OSPFv3 configuration
                suboptions:
                  areas:
                    description: OSPFv3 area.
                    type: list
                    elements: dict
                    suboptions:
                      area_id:
                        description: OSPFv3 Area name/identity.
                        type: str
                      export_list:
                        description: Name of export-list.
                        type: str
                      import_list:
                        description: Name of import-list.
                        type: str
                      interface:
                        description: Enable OSPVv3 on an interface for this area.
                        aliases: ['interfaces']
                        type: list
                        elements: dict
                        suboptions:
                          name:
                            description: Interface name.
                            type: str
                      range:
                        description: Summarize routes matching prefix (border routers only).
                        type: list
                        elements: dict
                        suboptions:
                          address:
                            description: border router IPv4 address.
                            type: str
                          advertise:
                            description: Advertise this range.
                            type: bool
                          not_advertise:
                            description: Don't advertise this range.
                            type: bool
                  parameters:
                    description: OSPFv3 specific parameters.
                    type: dict
                    suboptions:
                      router_id:
                        description: Override the default router identifier.
                        type: str
                  redistribute:
                    description: Redistribute information from another routing protocol.
                    type: list
                    elements: dict
                    suboptions:
                      route_type:
                        description: Route type to redistribute.
                        type: str
                        choices:
                        - bgp
                        - connected
                        - kernel
                        - ripng
                        - static
                      route_map:
                        description: Route map references.
                        type: str
              static:
                type: list
                description: Static routes configuration
                elements: dict
                suboptions:
                  address_families:
                    description: A dictionary specifying the address family to which the static
                      route(s) belong.
                    type: list
                    elements: dict
                    suboptions:
                      afi:
                        description:
                        - Specifies the type of route.
                        type: str
                        choices:
                        - ipv4
                        - ipv6
                        required: true
                      routes:
                        description: A dictionary that specify the static route configurations.
                        type: list
                        elements: dict
                        suboptions:
                          dest:
                            description:
                            - An IPv4/v6 address in CIDR notation that specifies the destination
                              network for the static route.
                            type: str
                            required: true
                          blackhole_config:
                            description:
                            - Configured to silently discard packets.
                            type: dict
                            suboptions:
                              type:
                                description:
                                - This is to configure only blackhole.
                                type: str
                              distance:
                                description:
                                - Distance for the route.
                                type: int
                          next_hops:
                            description:
                            - Next hops to the specified destination.
                            type: list
                            elements: dict
                            suboptions:
                              forward_router_address:
                                description:
                                - The IP address of the next hop that can be used to reach the
                                  destination network.
                                type: str
                              enabled:
                                description:
                                - Disable IPv4/v6 next-hop static route.
                                type: bool
                              admin_distance:
                                description:
                                - Distance value for the route.
                                type: int
                              interface:
                                description:
                                - Name of the outgoing interface.
                                type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the VYOS device by
      executing the command B(show configuration commands |  match "set vrf").
    - The states I(replaced) and I(overridden) have identical
      behaviour for this module.
    - The state I(parsed) reads the configuration from C(show configuration commands |  match "set vrf") option and
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
# # -------------------
# # 1. Using merged
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands |  match 'set vrf'
#      set vrf name vrf-blue description 'blue-vrf'
#      set vrf name vrf-blue disable
#      set vrf name vrf-blue table '100'
#      set vrf name vrf-blue vni '1000'
#   vyos@vyos:~$

# # Task
# # -------------
  # - name: Merge provided configuration with device configuration
  #   vyos.vyos.vyos_vrf:
  #     config:
  #       instances:
  #         - name: "vrf-green"
  #           description: "green-vrf"
  #           table_id: 110
  #           vni: 1010

# Task output:
# -------------
    # "after": {
    #     "bind_to_all": false,
    #     "instances": [
    #         {
    #             "description": "blue-vrf",
    #             "disable": true,
    #             "name": "vrf-blue",
    #             "table_id": 100,
    #             "vni": 1000
    #         },
    #         {
    #             "description": "green-vrf",
    #             "disable": false,
    #             "name": "vrf-green",
    #             "table_id": 110,
    #             "vni": 1010
    #         }
    #     ]
    # },
    # "before": {
    #     "bind_to_all": false,
    #     "instances": [
    #         {
    #             "description": "blue-vrf",
    #             "disable": true,
    #             "name": "vrf-blue",
    #             "table_id": 100,
    #             "vni": 1000
    #         }
    #     ]
    # },
    # "changed": true,
    # "commands": [
    #     "set vrf name vrf-green table 110",
    #     "set vrf name vrf-green vni 1010",
    #     "set vrf name vrf-green description green-vrf"
    # ]

# After state:
# # -------------
#   vyos@vyos:~$ show configuration commands |  match 'set vrf'
#     set vrf name vrf-blue description 'blue-vrf'
#     set vrf name vrf-blue disable
#     set vrf name vrf-blue table '100'
#     set vrf name vrf-blue vni '1000'
#     set vrf name vrf-green description 'green-vrf'
#     set vrf name vrf-green table '110'
#     set vrf name vrf-green vni '1010'
#   vyos@vyos:~$

# # -------------------
# # 2. Using replaced
# # -------------------

# # Before state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
      # set vrf bind-to-all
      # set vrf name vrf-blue description 'blue-vrf'
      # set vrf name vrf-blue table '100'
      # set vrf name vrf-blue vni '1000'
      # set vrf name vrf-red description 'red-vrf'
      # set vrf name vrf-red disable
      # set vrf name vrf-red ip disable-forwarding
      # set vrf name vrf-red ip protocol kernel route-map 'rm1'
      # set vrf name vrf-red ip protocol rip route-map 'rm1'
      # set vrf name vrf-red table '101'
      # set vrf name vrf-red vni '1001'
      # vyos@vyos:~$


# # Task
# # -------------
  # - name: Merge provided configuration with device configuration
  #   vyos.vyos.vyos_vrf:
  #     config:
  #       bind_to_all: true
  #       instances:
  #         - name: "vrf-blue"
  #           description: "blue-vrf"
  #           disable: false
  #           table_id: 100
  #           vni: 1002
  #         - name: "vrf-red"
  #           description: "red-vrf"
  #           disable: false
  #           table_id: 101
  #           vni: 1001
  #           address_family:
  #             - afi: "ipv4"
  #               disable_forwarding: false
  #               route_maps:
  #                 - rm_name: "rm1"
  #                   protocol: "kernel"
  #                 - rm_name: "rm1"
  #                   protocol: "ospf"
  #             - afi: "ipv6"
  #               nht_no_resolve_via_default: true
  #     state: replaced

# # Task output:
# # -------------
  # "after": {
  #     "bind_to_all": true,
  #     "instances": [
  #         {
  #             "description": "blue-vrf",
  #             "disable": false,
  #             "name": "vrf-blue",
  #             "table_id": 100,
  #             "vni": 1002
  #         },
  #         {
  #             "address_family": [
  #                 {
  #                     "afi": "ipv4",
  #                     "disable_forwarding": false,
  #                     "nht_no_resolve_via_default": false,
  #                     "route_maps": [
  #                         {
  #                             "protocol": "kernel",
  #                             "rm_name": "rm1"
  #                         },
  #                         {
  #                             "protocol": "ospf",
  #                             "rm_name": "rm1"
  #                         },
  #                         {
  #                             "protocol": "rip",
  #                             "rm_name": "rm1"
  #                         }
  #                     ]
  #                 },
  #                 {
  #                     "afi": "ipv6",
  #                     "disable_forwarding": false,
  #                     "nht_no_resolve_via_default": true
  #                 }
  #             ],
  #             "description": "red-vrf",
  #             "disable": false,
  #             "name": "vrf-red",
  #             "table_id": 101,
  #             "vni": 1001
  #         }
  #     ]
  # },
  # "before": {
  #     "bind_to_all": true,
  #     "instances": [
  #         {
  #             "description": "blue-vrf",
  #             "disable": false,
  #             "name": "vrf-blue",
  #             "table_id": 100,
  #             "vni": 1000
  #         },
  #         {
  #             "address_family": [
  #                 {
  #                     "afi": "ipv4",
  #                     "disable_forwarding": true,
  #                     "nht_no_resolve_via_default": false,
  #                     "route_maps": [
  #                         {
  #                             "protocol": "kernel",
  #                             "rm_name": "rm1"
  #                         },
  #                         {
  #                             "protocol": "rip",
  #                             "rm_name": "rm1"
  #                         }
  #                     ]
  #                 }
  #             ],
  #             "description": "red-vrf",
  #             "disable": true,
  #             "name": "vrf-red",
  #             "table_id": 101,
  #             "vni": 1001
  #         }
  #     ]
  # },
  # "changed": true,
  # "commands": [
  #     "set vrf name vrf-blue vni 1002",
  #     "delete vrf name vrf-red disable",
  #     "set vrf name vrf-red ip protocol ospf route-map rm1",
  #     "delete vrf name vrf-red ip disable-forwarding",
  #     "set vrf name vrf-red ipv6 nht no-resolve-via-default"
  # ]

# After state:
# # -------------
    # vyos@vyos:~$
      # set vrf bind-to-all
      # set vrf name vrf-blue description 'blue-vrf'
      # set vrf name vrf-blue table '100'
      # set vrf name vrf-blue vni '1002'
      # set vrf name vrf-red description 'red-vrf'
      # set vrf name vrf-red ip protocol kernel route-map 'rm1'
      # set vrf name vrf-red ip protocol ospf route-map 'rm1'
      # set vrf name vrf-red ip protocol rip route-map 'rm1'
      # set vrf name vrf-red ipv6 nht no-resolve-via-default
      # set vrf name vrf-red table '101'
      # set vrf name vrf-red vni '1001'
    # vyos@vyos:~$


# # -------------------
# # 3. Using overridden
# # -------------------

# # Before state:
# # -------------
  # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    # set vrf bind-to-all
    # set vrf name vrf-blue description 'blue-vrf'
    # set vrf name vrf-blue table '100'
    # set vrf name vrf-blue vni '1000'
    # set vrf name vrf-red description 'red-vrf'
    # set vrf name vrf-red disable
    # set vrf name vrf-red ip disable-forwarding
    # set vrf name vrf-red ip protocol kernel route-map 'rm1'
    # set vrf name vrf-red ip protocol rip route-map 'rm1'
    # set vrf name vrf-red table '101'
    # set vrf name vrf-red vni '1001'
  # vyos@vyos:~$

# Task
# -------------
  # - name: Overridden provided configuration with device configuration
  #   vyos.vyos.vyos_vrf:
  #     config:
  #       bind_to_all: true
  #       instances:
  #         - name: "vrf-blue"
  #           description: "blue-vrf"
  #           disable: true
  #           table_id: 100
  #           vni: 1000
  #         - name: "vrf-red"
  #           description: "red-vrf"
  #           disable: true
  #           table_id: 101
  #           vni: 1001
  #           address_family:
  #             - afi: "ipv4"
  #               disable_forwarding: false
  #               route_maps:
  #                 - rm_name: "rm1"
  #                   protocol: "kernel"
  #                 - rm_name: "rm1"
  #                   protocol: "rip"
  #             - afi: "ipv6"
  #               nht_no_resolve_via_default: false
  #     state: overridden

# # Task output:
# # -------------
    # "after": {
    #     "bind_to_all": true,
    #     "instances": [
    #         {
    #             "description": "blue-vrf",
    #             "disable": true,
    #             "name": "vrf-blue",
    #             "table_id": 100,
    #             "vni": 1000
    #         },
    #         {
    #             "address_family": [
    #                 {
    #                     "afi": "ipv4",
    #                     "disable_forwarding": false,
    #                     "nht_no_resolve_via_default": false,
    #                     "route_maps": [
    #                         {
    #                             "protocol": "kernel",
    #                             "rm_name": "rm1"
    #                         },
    #                         {
    #                             "protocol": "rip",
    #                             "rm_name": "rm1"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "description": "red-vrf",
    #             "disable": true,
    #             "name": "vrf-red",
    #             "table_id": 101,
    #             "vni": 1001
    #         }
    #     ]
    # },
    # "before": {
    #     "bind_to_all": true,
    #     "instances": [
    #         {
    #             "description": "blue-vrf",
    #             "disable": false,
    #             "name": "vrf-blue",
    #             "table_id": 100,
    #             "vni": 1000
    #         },
    #         {
    #             "address_family": [
    #                 {
    #                     "afi": "ipv4",
    #                     "disable_forwarding": true,
    #                     "nht_no_resolve_via_default": false,
    #                     "route_maps": [
    #                         {
    #                             "protocol": "kernel",
    #                             "rm_name": "rm1"
    #                         },
    #                         {
    #                             "protocol": "rip",
    #                             "rm_name": "rm1"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "description": "red-vrf",
    #             "disable": true,
    #             "name": "vrf-red",
    #             "table_id": 101,
    #             "vni": 1001
    #         }
    #     ]
    # },
    # "changed": true,
    # "commands": [
    #     "delete vrf name vrf-blue",
    #     "commit",
    #     "delete vrf name vrf-red",
    #     "commit",
    #     "set vrf name vrf-blue table 100",
    #     "set vrf name vrf-blue vni 1000",
    #     "set vrf name vrf-blue description blue-vrf",
    #     "set vrf name vrf-blue disable",
    #     "set vrf name vrf-red table 101",
    #     "set vrf name vrf-red vni 1001",
    #     "set vrf name vrf-red description red-vrf",
    #     "set vrf name vrf-red disable",
    #     "set vrf name vrf-red ip protocol kernel route-map rm1",
    #     "set vrf name vrf-red ip protocol rip route-map rm1"
    # ]

# After state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #   set vrf bind-to-all
    #   set vrf name vrf-blue description 'blue-vrf'
    #   set vrf name vrf-blue disable
    #   set vrf name vrf-blue table '100'
    #   set vrf name vrf-blue vni '1000'
    #   set vrf name vrf-red description 'red-vrf'
    #   set vrf name vrf-red disable
    #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
    #   set vrf name vrf-red ip protocol rip route-map 'rm1'
    #   set vrf name vrf-red table '101'
    #   set vrf name vrf-red vni '1001'
    # vyos@vyos:~$

# 4. Using gathered
# -------------------

# # Before state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #   set vrf bind-to-all
    #   set vrf name vrf-blue description 'blue-vrf'
    #   set vrf name vrf-blue table '100'
    #   set vrf name vrf-blue vni '1000'
    #   set vrf name vrf-red description 'red-vrf'
    #   set vrf name vrf-red disable
    #   set vrf name vrf-red ip disable-forwarding
    #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
    #   set vrf name vrf-red ip protocol rip route-map 'rm1'
    #   set vrf name vrf-red table '101'
    #   set vrf name vrf-red vni '1001'
    # vyos@vyos:~$

# Task
# -------------
# - name: Gather provided configuration with device configuration
#   vyos.vyos.vyos_vrf:
#     config:
#     state: gathered

# # Task output:
# # -------------
    # "gathered": {
    #     "bind_to_all": true,
    #     "instances": [
    #         {
    #             "description": "blue-vrf",
    #             "disable": false,
    #             "name": "vrf-blue",
    #             "table_id": 100,
    #             "vni": 1000
    #         },
    #         {
    #             "address_family": [
    #                 {
    #                     "afi": "ipv4",
    #                     "disable_forwarding": true,
    #                     "nht_no_resolve_via_default": false,
    #                     "route_maps": [
    #                         {
    #                             "protocol": "kernel",
    #                             "rm_name": "rm1"
    #                         },
    #                         {
    #                             "protocol": "rip",
    #                             "rm_name": "rm1"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "description": "red-vrf",
    #             "disable": true,
    #             "name": "vrf-red",
    #             "table_id": 101,
    #             "vni": 1001
    #         }
    #     ]
    # }

# After state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #   set vrf bind-to-all
    #   set vrf name vrf-blue description 'blue-vrf'
    #   set vrf name vrf-blue table '100'
    #   set vrf name vrf-blue vni '1000'
    #   set vrf name vrf-red description 'red-vrf'
    #   set vrf name vrf-red disable
    #   set vrf name vrf-red ip disable-forwarding
    #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
    #   set vrf name vrf-red ip protocol rip route-map 'rm1'
    #   set vrf name vrf-red table '101'
    #   set vrf name vrf-red vni '1001'
    # vyos@vyos:~$


# # -------------------
# # 5. Using deleted
# # -------------------

# # Before state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #   set vrf bind-to-all
    #   set vrf name vrf-blue description 'blue-vrf'
    #   set vrf name vrf-blue table '100'
    #   set vrf name vrf-blue vni '1000'
    #   set vrf name vrf-red description 'red-vrf'
    #   set vrf name vrf-red disable
    #   set vrf name vrf-red ip disable-forwarding
    #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
    #   set vrf name vrf-red ip protocol rip route-map 'rm1'
    #   set vrf name vrf-red table '101'
    #   set vrf name vrf-red vni '1001'
    # vyos@vyos:~$

# # Task
# # -------------
# - name: Replace provided configuration with device configuration
#   vyos.vyos.vyos_vrf:
#     config:
#       bind_to_all: false
#       instances:
#         - name: "vrf-blue"
#     state: deleted


# # Task output:
# # -------------
    # "after": {
    #     "bind_to_all": false,
    #     "instances": [
    #         {
    #             "address_family": [
    #                 {
    #                     "afi": "ipv4",
    #                     "disable_forwarding": true,
    #                     "nht_no_resolve_via_default": false,
    #                     "route_maps": [
    #                         {
    #                             "protocol": "kernel",
    #                             "rm_name": "rm1"
    #                         },
    #                         {
    #                             "protocol": "rip",
    #                             "rm_name": "rm1"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "description": "red-vrf",
    #             "disable": true,
    #             "name": "vrf-red",
    #             "table_id": 101,
    #             "vni": 1001
    #         }
    #     ]
    # },
    # "before": {
    #     "bind_to_all": true,
    #     "instances": [
    #         {
    #             "description": "blue-vrf",
    #             "disable": false,
    #             "name": "vrf-blue",
    #             "table_id": 100,
    #             "vni": 1000
    #         },
    #         {
    #             "address_family": [
    #                 {
    #                     "afi": "ipv4",
    #                     "disable_forwarding": true,
    #                     "nht_no_resolve_via_default": false,
    #                     "route_maps": [
    #                         {
    #                             "protocol": "kernel",
    #                             "rm_name": "rm1"
    #                         },
    #                         {
    #                             "protocol": "rip",
    #                             "rm_name": "rm1"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "description": "red-vrf",
    #             "disable": true,
    #             "name": "vrf-red",
    #             "table_id": 101,
    #             "vni": 1001
    #         }
    #     ]
    # },
    # "changed": true,
    # "commands": [
    #     "delete vrf bind-to-all",
    #     "delete vrf name vrf-blue"
    # ]

# After state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #   set vrf name vrf-red description 'red-vrf'
    #   set vrf name vrf-red disable
    #   set vrf name vrf-red ip disable-forwarding
    #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
    #   set vrf name vrf-red ip protocol rip route-map 'rm1'
    #   set vrf name vrf-red table '101'
    #   set vrf name vrf-red vni '1001'
    # vyos@vyos:~$

# # -------------------
# # 6. Using rendered
# # -------------------

# # Before state:
# # -------------
    # vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #   set vrf name vrf-red description 'red-vrf'
    #   set vrf name vrf-red disable
    #   set vrf name vrf-red ip disable-forwarding
    #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
    #   set vrf name vrf-red ip protocol rip route-map 'rm1'
    #   set vrf name vrf-red table '101'
    #   set vrf name vrf-red vni '1001'
    # vyos@vyos:~$

# Task
# -------------
    # - name: Render provided configuration with device configuration
    #   vyos.vyos.vyos_vrf:
    #     config:
    #       bind_to_all: true
    #       instances:
    #         - name: "vrf-green"
    #           description: "green-vrf"
    #           disabled: true
    #           table_id: 105
    #           vni: 1000
    #         - name: "vrf-amber"
    #           description: "amber-vrf"
    #           disable: false
    #           table_id: 111
    #           vni: 1001
    #           address_family:
    #             - afi: "ipv4"
    #               disable_forwarding: true
    #               route_maps:
    #                 - rm_name: "rm1"
    #                   protocol: "kernel"
    #                 - rm_name: "rm1"
    #                   protocol: "ospf"
    #             - afi: "ipv6"
    #               nht_no_resolve_via_default: false
    #     state: rendered

# # Task output:
# # -------------
  # "rendered": [
  #     "set vrf bind-to-all",
  #     "set vrf name vrf-green table 105",
  #     "set vrf name vrf-green vni 1000",
  #     "set vrf name vrf-green description green-vrf",
  #     "set vrf name vrf-green disable",
  #     "set vrf name vrf-amber table 111",
  #     "set vrf name vrf-amber vni 1001",
  #     "set vrf name vrf-amber description amber-vrf",
  #     "set vrf name vrf-amber ip protocol kernel route-map rm1",
  #     "set vrf name vrf-amber ip protocol ospf route-map rm1",
  #     "set vrf name vrf-amber ip disable-forwarding"
  # ]

# # -------------------
# # 7. Using parsed
# # -------------------

# # vrf_parsed.cfg:
# # -------------
# set vrf bind-to-all
# set vrf name vrf1 description 'red'
# set vrf name vrf1 disable
# set vrf name vrf1 table 101
# set vrf name vrf1 vni 501
# set vrf name vrf2 description 'blah2'
# set vrf name vrf2 disable
# set vrf name vrf2 table 102
# set vrf name vrf2 vni 102
# set vrf name vrf1 ip disable-forwarding
# set vrf name vrf1 ip nht no-resolve-via-default
# set vrf name vrf-red ip protocol kernel route-map 'rm1'
# set vrf name vrf-red ip protocol ospf route-map 'rm1'
# set vrf name vrf-red ipv6 nht no-resolve-via-default

# Task:
# -------------
# - name: Parse provided configuration with device configuration
#   vyos.vyos.vyos_vrf:
#     running_config: "{{ lookup('file', './vrf_parsed.cfg') }}"
#     state: parsed


# # Task output:
# # -------------
# "parsed": {
#         "bind_to_all": true,
#         "instances": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "disable_forwarding": true,
#                         "nht_no_resolve_via_default": true
#                     }
#                 ],
#                 "description": "red",
#                 "disable": true,
#                 "name": "vrf1"
#             },
#             {
#                 "description": "blah2",
#                 "disable": true,
#                 "name": "vrf2"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "disable_forwarding": false,
#                         "nht_no_resolve_via_default": false,
#                         "route_maps": [
#                             {
#                                 "protocol": "kernel",
#                                 "rm_name": "rm1"
#                             },
#                             {
#                                 "protocol": "ospf",
#                                 "rm_name": "rm1"
#                             }
#                         ]
#                     },
#                     {
#                         "afi": "ipv6",
#                         "disable_forwarding": false,
#                         "nht_no_resolve_via_default": true
#                     }
#                 ],
#                 "disable": false,
#                 "name": "vrf-red"
#             }
#         ]
#     }
"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - set system ntp server server1 dynamic
    - set system ntp server server1 prefer
    - set system ntp server server2 noselect
    - set system ntp server server2 preempt
    - set system ntp server server_add preempt
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set system ntp server server1 dynamic
    - set system ntp server server1 prefer
    - set system ntp server server2 noselect
    - set system ntp server server2 preempt
    - set system ntp server server_add preempt
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vrf.vrf import VrfArgs
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vrf.vrf import Vrf


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=VrfArgs.argument_spec,
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

    result = Vrf(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
