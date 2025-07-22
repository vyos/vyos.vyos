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
            type: dict
            elements: dict
            description: Protocol configuration
            suboptions:
              bgp:
                type: dict
                description: BGP configuration
                suboptions:
                  as_number:
                    description:
                    - AS number
                    type: int
                  address_family:
                    description: BGP address-family parameters.
                    type: list
                    elements: dict
                    suboptions:
                      afi:
                        description: BGP address family settings.
                        type: str
                        choices: ['ipv4', 'ipv6']
                      aggregate_address:
                        description:
                          - BGP aggregate network.
                        type: list
                        elements: dict
                        suboptions:
                          prefix:
                            description: BGP aggregate network.
                            type: str
                          as_set:
                            description: Generate AS-set path information for this aggregate address.
                            type: bool
                          summary_only:
                            description: Announce the aggregate summary network only.
                            type: bool
                      networks:
                        description: BGP network
                        type: list
                        elements: dict
                        suboptions:
                          prefix:
                            description: BGP network address
                            type: str
                          path_limit:
                            description: AS path hop count limit
                            type: int
                          backdoor:
                            description: Network as a backdoor route.
                            type: bool
                          route_map:
                            description: Route-map to modify route attributes
                            type: str
                      redistribute:
                        description: Redistribute routes from other protocols into BGP
                        type: list
                        elements: dict
                        suboptions:
                          protocol:
                            description: types of routes to be redistributed.
                            type: str
                            choices: ['connected', 'kernel', 'ospf', 'ospfv3', 'rip', 'ripng', 'static']
                          table:
                            description: Redistribute non-main Kernel Routing Table.
                            type: str
                          route_map:
                            description: Route map to filter redistributed routes
                            type: str
                          metric:
                            description: Metric for redistributed routes.
                            type: int
                  neighbors:
                    description: BGP neighbor
                    type: list
                    elements: dict
                    suboptions:
                      neighbor_address:
                        description: BGP neighbor address (v4/v6).
                        type: str
                      address_family:
                        description: address family.
                        type: list
                        elements: dict
                        suboptions:
                          afi:
                            description: BGP neighbor parameters.
                            type: str
                            choices: ['ipv4', 'ipv6']
                          allowas_in:
                            description: Number of occurrences of AS number.
                            type: int
                          as_override:
                            description:  AS for routes sent to this neighbor to be the local AS.
                            type: bool
                          attribute_unchanged:
                            description: BGP attributes are sent unchanged.
                            type: dict
                            suboptions:
                                as_path:
                                  description: as_path attribute
                                  type: bool
                                med:
                                  description: med attribute
                                  type: bool
                                next_hop:
                                  description: next_hop attribute
                                  type: bool
                          capability:
                            description: Advertise capabilities to this neighbor.
                            type: dict
                            suboptions:
                              dynamic:
                                description: Advertise dynamic capability to this neighbor.
                                type: bool
                              orf:
                                description: Advertise ORF capability to this neighbor.
                                type: str
                                choices: ['send', 'receive']
                          default_originate:
                            description: Send default route to this neighbor
                            type: str
                          distribute_list:
                            description:  Access-list to filter route updates to/from this neighbor.
                            type: list
                            elements: dict
                            suboptions:
                              action:
                                description:  Access-list to filter outgoing/incoming route updates to this neighbor
                                type: str
                                choices: ['export', 'import']
                              acl:
                                description: Access-list number.
                                type: int
                          filter_list:
                            description: As-path-list to filter route updates to/from this neighbor.
                            type: list
                            elements: dict
                            suboptions:
                              action:
                                description: filter outgoing/incoming route updates
                                type: str
                                choices: ['export', 'import']
                              path_list:
                                description: As-path-list to filter
                                type: str
                          maximum_prefix:
                            description:  Maximum number of prefixes to accept from this neighbor
                              nexthop-self Nexthop for routes sent to this neighbor to be the local router.
                            type: int
                          nexthop_local:
                            description:  Nexthop attributes.
                            type: bool
                          nexthop_self:
                            description:  Nexthop for routes sent to this neighbor to be the local router.
                            type: bool
                          peer_group:
                            description:  IPv4 peer group for this peer
                            type: str
                          prefix_list:
                            description: Prefix-list to filter route updates to/from this neighbor.
                            type: list
                            elements: dict
                            suboptions:
                              action:
                                description: filter outgoing/incoming route updates
                                type: str
                                choices: ['export', 'import']
                              prefix_list:
                                description: Prefix-list to filter
                                type: str
                          remove_private_as:
                            description: Remove private AS numbers from AS path in outbound route updates
                            type: bool
                          route_map:
                            description: Route-map to filter route updates to/from this neighbor.
                            type: list
                            elements: dict
                            suboptions:
                              action:
                                description: filter outgoing/incoming route updates
                                type: str
                                choices: ['export', 'import']
                              route_map:
                                description: route-map to filter
                                type: str
                          route_reflector_client:
                            description: Neighbor as a route reflector client
                            type: bool
                          route_server_client:
                            description: Neighbor is route server client
                            type: bool
                          soft_reconfiguration:
                            description: Soft reconfiguration for neighbor
                            type: bool
                          unsupress_map:
                            description:  Route-map to selectively unsuppress suppressed routes
                            type: str
                          weight:
                            description: Default weight for routes from this neighbor
                            type: int
              ospf:
                type: dict
                description: OSPFv2 configuration
                elements: dict
              ospfv3:
                type: dict
                description: OSPFv3 configuration
                elements: dict
              static:
                type: dict
                description: Static routes configuration
                elements: dict
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
