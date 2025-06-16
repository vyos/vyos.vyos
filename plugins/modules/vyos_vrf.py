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
- Tested against vyos 1.5-stream-2025-Q1
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
  - name: Merge provided configuration with device configuration
    vyos.vyos.vyos_vrf:
      config:
        instances:
          - name: "vrf-green"
            description: "green-vrf"
            table_id: 110
            vni: 1010

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
  - name: Merge provided configuration with device configuration
    vyos.vyos.vyos_vrf:
      config:
        bind_to_all: true
        instances:
          - name: "vrf-blue"
            description: "blue-vrf"
            disable: false
            table_id: 100
            vni: 1002
          - name: "vrf-red"
            description: "red-vrf"
            disable: false
            table_id: 101
            vni: 1001
            address_family:
              - afi: "ipv4"
                disable_forwarding: false
                route_maps:
                  - rm_name: "rm1"
                    protocol: "kernel"
                  - rm_name: "rm1"
                    protocol: "ospf"
              - afi: "ipv6"
                nht_no_resolve_via_default: true
      state: replaced

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
  - name: Overridden provided configuration with device configuration
    vyos.vyos.vyos_vrf:
      config:
        bind_to_all: true
        instances:
          - name: "vrf-blue"
            description: "blue-vrf"
            disable: true
            table_id: 100
            vni: 1000
          - name: "vrf-red"
            description: "red-vrf"
            disable: true
            table_id: 101
            vni: 1001
            address_family:
              - afi: "ipv4"
                disable_forwarding: false
                route_maps:
                  - rm_name: "rm1"
                    protocol: "kernel"
                  - rm_name: "rm1"
                    protocol: "rip"
              - afi: "ipv6"
                nht_no_resolve_via_default: false
      state: overridden

# # Task output:
# # -------------
    "after": {
        "bind_to_all": true,
        "instances": [
            {
                "description": "blue-vrf",
                "disable": true,
                "name": "vrf-blue",
                "table_id": 100,
                "vni": 1000
            },
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "disable_forwarding": false,
                        "nht_no_resolve_via_default": false,
                        "route_maps": [
                            {
                                "protocol": "kernel",
                                "rm_name": "rm1"
                            },
                            {
                                "protocol": "rip",
                                "rm_name": "rm1"
                            }
                        ]
                    }
                ],
                "description": "red-vrf",
                "disable": true,
                "name": "vrf-red",
                "table_id": 101,
                "vni": 1001
            }
        ]
    },
    "before": {
        "bind_to_all": true,
        "instances": [
            {
                "description": "blue-vrf",
                "disable": false,
                "name": "vrf-blue",
                "table_id": 100,
                "vni": 1000
            },
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "disable_forwarding": true,
                        "nht_no_resolve_via_default": false,
                        "route_maps": [
                            {
                                "protocol": "kernel",
                                "rm_name": "rm1"
                            },
                            {
                                "protocol": "rip",
                                "rm_name": "rm1"
                            }
                        ]
                    }
                ],
                "description": "red-vrf",
                "disable": true,
                "name": "vrf-red",
                "table_id": 101,
                "vni": 1001
            }
        ]
    },
    "changed": true,
    "commands": [
        "delete vrf name vrf-blue",
        "commit",
        "delete vrf name vrf-red",
        "commit",
        "set vrf name vrf-blue table 100",
        "set vrf name vrf-blue vni 1000",
        "set vrf name vrf-blue description blue-vrf",
        "set vrf name vrf-blue disable",
        "set vrf name vrf-red table 101",
        "set vrf name vrf-red vni 1001",
        "set vrf name vrf-red description red-vrf",
        "set vrf name vrf-red disable",
        "set vrf name vrf-red ip protocol kernel route-map rm1",
        "set vrf name vrf-red ip protocol rip route-map rm1"
    ]

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
- name: Gather provided configuration with device configuration
  vyos.vyos.vyos_vrf:
    config:
    state: gathered

# # Task output:
# # -------------
    "gathered": {
        "bind_to_all": true,
        "instances": [
            {
                "description": "blue-vrf",
                "disable": false,
                "name": "vrf-blue",
                "table_id": 100,
                "vni": 1000
            },
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "disable_forwarding": true,
                        "nht_no_resolve_via_default": false,
                        "route_maps": [
                            {
                                "protocol": "kernel",
                                "rm_name": "rm1"
                            },
                            {
                                "protocol": "rip",
                                "rm_name": "rm1"
                            }
                        ]
                    }
                ],
                "description": "red-vrf",
                "disable": true,
                "name": "vrf-red",
                "table_id": 101,
                "vni": 1001
            }
        ]
    }

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
- name: Replace provided configuration with device configuration
  vyos.vyos.vyos_vrf:
    config:
      bind_to_all: false
      instances:
        - name: "vrf-blue"
    state: deleted


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
    - name: Render provided configuration with device configuration
      vyos.vyos.vyos_vrf:
        config:
          bind_to_all: true
          instances:
            - name: "vrf-green"
              description: "green-vrf"
              disabled: true
              table_id: 105
              vni: 1000
            - name: "vrf-amber"
              description: "amber-vrf"
              disable: false
              table_id: 111
              vni: 1001
              address_family:
                - afi: "ipv4"
                  disable_forwarding: true
                  route_maps:
                    - rm_name: "rm1"
                      protocol: "kernel"
                    - rm_name: "rm1"
                      protocol: "ospf"
                - afi: "ipv6"
                  nht_no_resolve_via_default: false
        state: rendered

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
- name: Parse provided configuration with device configuration
  vyos.vyos.vyos_vrf:
    running_config: "{{ lookup('file', './vrf_parsed.cfg') }}"
    state: parsed


# # Task output:
# # -------------
"parsed": {
        "bind_to_all": true,
        "instances": [
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "disable_forwarding": true,
                        "nht_no_resolve_via_default": true
                    }
                ],
                "description": "red",
                "disable": true,
                "name": "vrf1"
            },
            {
                "description": "blah2",
                "disable": true,
                "name": "vrf2"
            },
            {
                "address_family": [
                    {
                        "afi": "ipv4",
                        "disable_forwarding": false,
                        "nht_no_resolve_via_default": false,
                        "route_maps": [
                            {
                                "protocol": "kernel",
                                "rm_name": "rm1"
                            },
                            {
                                "protocol": "ospf",
                                "rm_name": "rm1"
                            }
                        ]
                    },
                    {
                        "afi": "ipv6",
                        "disable_forwarding": false,
                        "nht_no_resolve_via_default": true
                    }
                ],
                "disable": false,
                "name": "vrf-red"
            }
        ]
    }
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
