#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_vrrp
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = r"""
---
module: vyos_vrrp
author: Evgeny Molotkov (@omnom62)
short_description: Manage VRRP and load balancer configuration on VyOS
version_added: "1.0.0"
description:
  - This module configures VRRP groups, global VRRP parameters, VRRP sync groups,
    and LVS-style virtual servers on VyOS 1.4+.
  - Supports creation, modification, deletion, replacement, rendering, and parsing
    of VRRP-related configuration.

options:
  config:
    description:
      - Full VRRP and virtual server configuration.
    type: dict
    suboptions:
      disable:
        description:
          - Disable all VRRP and L4-LB configuration under this module.
        type: bool

      virtual_servers:
        description:
          - List of load balancer virtual server (LVS) definitions.
        type: list
        elements: dict
        suboptions:
          alias:
            description:
              - Unique identifier for the virtual server.
            type: str
            required: true
          address:
            description:
              - Virtual IP address for the server.
            type: str
          algorithm:
            description:
              - Load balancing algorithm used for dispatching connections.
            type: str
          delay_loop:
            description:
              - Delay loop interval in seconds.
            type: int
          forward_method:
            description:
              - Forwarding method used by LVS.
            type: str
            choices: [direct, nat]
          fwmark:
            description:
              - Firewall mark for LVS traffic classification.
            type: str
          persistence_timeout:
            description:
              - Client persistence timeout in seconds.
            type: str
          port:
            description:
              - TCP/UDP port provided by the virtual service.
            type: int
          protocol:
            description:
              - Transport protocol for the virtual server.
            type: str
            choices: [tcp, udp]

          real_servers:
            description:
              - Backend real servers behind the virtual service.
            type: list
            elements: dict
            suboptions:
              address:
                description:
                  - Real server IP address.
                type: str
                required: true
              port:
                description:
                  - Backend server port.
                type: int
              health_check_script:
                description:
                  - Path to health check script used for backend validation.
                type: str

      vrrp:
        description:
          - VRRP configuration including groups, global parameters, SNMP settings,
            and sync-groups.
        type: dict
        suboptions:

          global_parameters:
            description:
              - Global VRRP tuning parameters.
            type: dict
            suboptions:
              garp:
                description:
                  - Gratuitous ARP related configuration.
                type: dict
                suboptions:
                  interval:
                    description:
                      - GARP interval in seconds.
                    type: int
                  master_delay:
                    description:
                      - Delay before sending GARP as master.
                    type: int
                  master_refresh:
                    description:
                      - Refresh interval for master GARP announcements.
                    type: int
                  master_refresh_repeat:
                    description:
                      - Number of times to repeat refresh announcements.
                    type: int
                  master_repeat:
                    description:
                      - Number of GARP repeats when transitioning to master.
                    type: int

              startup_delay:
                description:
                  - Delay before VRRP starts after boot.
                type: int

              version:
                description:
                  - VRRP protocol version.
                type: str

          groups:
            description:
              - VRRP instance configuration groups.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                  - VRRP group name.
                type: str
                required: true
              address:
                description:
                  - Virtual router IP address.
                type: str
              advertise_interval:
                description:
                  - VRRP advertisement interval.
                type: int

              authentication:
                description:
                  - VRRP group authentication options.
                type: dict
                suboptions:
                  password:
                    description:
                      - Authentication password.
                    type: str
                  type:
                    description:
                      - Authentication type.
                    type: str

              description:
                description:
                  - Text description for the VRRP group.
                type: str

              disable:
                description:
                  - Disable this VRRP group.
                type: bool

              excluded_address:
                description:
                  - IP address excluded from source checks.
                type: str

              garp:
                description:
                  - GARP-specific settings for this group.
                type: dict
                suboptions:
                  interval:
                    description: GARP interval.
                    type: int
                  master_delay:
                    description: GARP master delay.
                    type: int
                  master_refresh:
                    description: GARP master refresh interval.
                    type: int
                  master_refresh_repeat:
                    description: Repeated refresh sends.
                    type: int
                  master_repeat:
                    description: GARP repeat count.
                    type: int

              health_check:
                description:
                  - VRRP group health check options.
                type: dict
                suboptions:
                  failure_count:
                    description: Allowed number of failed checks.
                    type: int
                  interval:
                    description: Health check interval.
                    type: int
                  ping:
                    description: Host to ping for checks.
                    type: str
                  script:
                    description: Script to execute for health checking.
                    type: str

              hello_source_address:
                description:
                  - Source address for VRRP hello packets.
                type: str

              interface:
                description:
                  - Interface used by the VRRP group.
                type: str

              no_preempt:
                description:
                  - Disable preemption.
                type: bool

              peer_address:
                description:
                  - Peer VRRP router address.
                type: str

              preempt_delay:
                description:
                  - Delay before taking master role.
                type: int

              priority:
                description:
                  - VRRP priority (higher = preferred master).
                type: int

              rfc3768_compatibility:
                description:
                  - Enable or disable RFC3768 compatibility mode.
                type: bool

              track:
                description:
                  - Track interface and VRRP behaviour.
                type: dict
                suboptions:
                  exclude_vrrp_interface:
                    description:
                      - Exclude VRRP interface from tracking.
                    type: bool
                  interface:
                    description:
                      - Interface to track.
                    type: str

              transition_script:
                description:
                  - Scripts executed during VRRP state transitions.
                type: dict
                suboptions:
                  backup:
                    description: Path to backup script.
                    type: str
                  fault:
                    description: Path to fault script.
                    type: str
                  master:
                    description: Path to master script.
                    type: str
                  stop:
                    description: Path to stop script.
                    type: str

              vrid:
                description:
                  - VRRP Virtual Router ID.
                type: int
                required: true

          snmp:
            description:
              - Enable SNMP support for VRRP.
            type: bool

          sync_groups:
            description:
              - VRRP sync-groups for coordinated failover.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                  - Sync-group name.
                type: str
                required: true

              health_check:
                description:
                  - Health check options for sync group.
                type: dict
                suboptions:
                  failure_count:
                    description: Allowed number of failures.
                    type: int
                  interval:
                    description: Health check interval.
                    type: int
                  ping:
                    description: Host to ping.
                    type: str
                  script:
                    description: Script to run for health checking.
                    type: str

              member:
                description:
                  - List of VRRP groups participating in this sync group.
                type: list
                elements: str

              transition_script:
                description:
                  - Transition scripts for sync group events.
                type: dict
                suboptions:
                  backup:
                    description: Backup state script.
                    type: str
                  fault:
                    description: Fault state script.
                    type: str
                  master:
                    description: Master state script.
                    type: str
                  stop:
                    description: Stop state script.
                    type: str

  state:
    description:
      - Desired end state of the VRRP configuration.
    type: str
    choices:
      - deleted
      - merged
      - purged
      - replaced
      - gathered
      - rendered
      - parsed
    default: merged

  running_config:
    description:
      - Used only when C(state=parsed). Must contain the output of
        C(show configuration commands | grep high-availability).
    type: str
"""

EXAMPLES = """
# Using merged
# Before state

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# vyos@vyos:~$

- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_vrrp:
    config:
      as_number: "65536"
      aggregate_address:
        - prefix: "203.0.113.0/24"
          as_set: true
        - prefix: "192.0.2.0/24"
          summary_only: true
      network:
        - address: "192.1.13.0/24"
          backdoor: true
      redistribute:
        - protocol: "kernel"
          metric: 45
        - protocol: "connected"
          route_map: "map01"
      maximum_paths:
        - path: "ebgp"
          count: 20
        - path: "ibgp"
          count: 55
      timers:
        keepalive: 35
      bgp_params:
        bestpath:
          as_path: "confed"
          compare_routerid: true
        default:
          no_ipv4_unicast: true
        router_id: "192.1.2.9"
        confederation:
          - peers: 20
          - peers: 55
          - identifier: 66
      neighbor:
        - address: "192.0.2.25"
          disable_connected_check: true
          timers:
            holdtime: 30
            keepalive: 10
        - address: "203.0.113.5"
          attribute_unchanged:
            as_path: true
            med: true
          ebgp_multihop: 2
          remote_as: 101
          update_source: "192.0.2.25"
        - address: "5001::64"
          maximum_prefix: 34
          distribute_list:
            - acl: 20
              action: "export"
            - acl: 40
              action: "import"
    state: merged

# After State
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp aggregate-address 192.0.2.0/24 'summary-only'
# set protocols bgp aggregate-address 203.0.113.0/24 'as-set'
# set protocols bgp maximum-paths ebgp '20'
# set protocols bgp maximum-paths ibgp '55'
# set protocols bgp neighbor 192.0.2.25 'disable-connected-check'
# set protocols bgp neighbor 192.0.2.25 timers holdtime '30'
# set protocols bgp neighbor 192.0.2.25 timers keepalive '10'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'as-path'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'med'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'next-hop'
# set protocols bgp neighbor 203.0.113.5 ebgp-multihop '2'
# set protocols bgp neighbor 203.0.113.5 remote-as '101'
# set protocols bgp neighbor 203.0.113.5 update-source '192.0.2.25'
# set protocols bgp neighbor 5001::64 distribute-list export '20'
# set protocols bgp neighbor 5001::64 distribute-list import '40'
# set protocols bgp neighbor 5001::64 maximum-prefix '34'
# set protocols bgp network 192.1.13.0/24 'backdoor'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp parameters bestpath 'compare-routerid'
# set protocols bgp parameters confederation identifier '66'
# set protocols bgp parameters confederation peers '20'
# set protocols bgp parameters confederation peers '55'
# set protocols bgp parameters default 'no-ipv4-unicast'
# set protocols bgp parameters router-id '192.1.2.9'
# set protocols bgp redistribute connected route-map 'map01'
# set protocols bgp redistribute kernel metric '45'
# set protocols bgp timers keepalive '35'
# vyos@vyos:~$
#
# # Module Execution:
#
# "after": {
#         "aggregate_address": [
#             {
#                 "prefix": "192.0.2.0/24",
#                 "summary_only": true
#             },
#             {
#                 "prefix": "203.0.113.0/24",
#                 "as_set": true
#             }
#         ],
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "confederation": [
#                 {
#                     "identifier": 66
#                 },
#                 {
#                     "peers": 20
#                 },
#                 {
#                     "peers": 55
#                 }
#             ],
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "router_id": "192.1.2.9"
#         },
#         "maximum_paths": [
#             {
#                 "count": 20,
#                 "path": "ebgp"
#             },
#             {
#                 "count": 55,
#                 "path": "ibgp"
#             }
#         ],
#         "neighbor": [
#             {
#                 "address": "192.0.2.25",
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.5",
#                 "attribute_unchanged": {
#                     "as_path": true,
#                     "med": true,
#                     "next_hop": true
#                 },
#                 "ebgp_multihop": 2,
#                 "remote_as": 101,
#                 "update_source": "192.0.2.25"
#             },
#             {
#                 "address": "5001::64",
#                 "distribute_list": [
#                     {
#                         "acl": 20,
#                         "action": "export"
#                     },
#                     {
#                         "acl": 40,
#                         "action": "import"
#                     }
#                 ],
#                 "maximum_prefix": 34
#             }
#         ],
#         "network": [
#             {
#                 "address": "192.1.13.0/24",
#                 "backdoor": true
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "connected",
#                 "route_map": "map01"
#             },
#             {
#                 "metric": 45,
#                 "protocol": "kernel"
#             }
#         ],
#         "timers": {
#             "keepalive": 35
#         }
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "set protocols bgp neighbor 192.0.2.25 disable-connected-check",
#         "set protocols bgp neighbor 192.0.2.25 timers holdtime 30",
#         "set protocols bgp neighbor 192.0.2.25 timers keepalive 10",
#         "set protocols bgp neighbor 203.0.113.5 attribute-unchanged as-path",
#         "set protocols bgp neighbor 203.0.113.5 attribute-unchanged med",
#         "set protocols bgp neighbor 203.0.113.5 attribute-unchanged next-hop",
#         "set protocols bgp neighbor 203.0.113.5 ebgp-multihop 2",
#         "set protocols bgp neighbor 203.0.113.5 remote-as 101",
#         "set protocols bgp neighbor 203.0.113.5 update-source 192.0.2.25",
#         "set protocols bgp neighbor 5001::64 maximum-prefix 34",
#         "set protocols bgp neighbor 5001::64 distribute-list export 20",
#         "set protocols bgp neighbor 5001::64 distribute-list import 40",
#         "set protocols bgp redistribute kernel metric 45",
#         "set protocols bgp redistribute connected route-map map01",
#         "set protocols bgp network 192.1.13.0/24 backdoor",
#         "set protocols bgp aggregate-address 203.0.113.0/24 as-set",
#         "set protocols bgp aggregate-address 192.0.2.0/24 summary-only",
#         "set protocols bgp parameters bestpath as-path confed",
#         "set protocols bgp parameters bestpath compare-routerid",
#         "set protocols bgp parameters default no-ipv4-unicast",
#         "set protocols bgp parameters router-id 192.1.2.9",
#         "set protocols bgp parameters confederation peers 20",
#         "set protocols bgp parameters confederation peers 55",
#         "set protocols bgp parameters confederation identifier 66",
#         "set protocols bgp maximum-paths ebgp 20",
#         "set protocols bgp maximum-paths ibgp 55",
#         "set protocols bgp timers keepalive 35"
#     ],

# Using replaced:
# --------------

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp aggregate-address 192.0.2.0/24 'summary-only'
# set protocols bgp aggregate-address 203.0.113.0/24 'as-set'
# set protocols bgp maximum-paths ebgp '20'
# set protocols bgp maximum-paths ibgp '55'
# set protocols bgp neighbor 192.0.2.25 'disable-connected-check'
# set protocols bgp neighbor 192.0.2.25 timers holdtime '30'
# set protocols bgp neighbor 192.0.2.25 timers keepalive '10'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'as-path'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'med'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'next-hop'
# set protocols bgp neighbor 203.0.113.5 ebgp-multihop '2'
# set protocols bgp neighbor 203.0.113.5 remote-as '101'
# set protocols bgp neighbor 203.0.113.5 update-source '192.0.2.25'
# set protocols bgp neighbor 5001::64 distribute-list export '20'
# set protocols bgp neighbor 5001::64 distribute-list import '40'
# set protocols bgp neighbor 5001::64 maximum-prefix '34'
# set protocols bgp network 192.1.13.0/24 'backdoor'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp parameters bestpath 'compare-routerid'
# set protocols bgp parameters confederation identifier '66'
# set protocols bgp parameters confederation peers '20'
# set protocols bgp parameters confederation peers '55'
# set protocols bgp parameters default 'no-ipv4-unicast'
# set protocols bgp parameters router-id '192.1.2.9'
# set protocols bgp redistribute connected route-map 'map01'
# set protocols bgp redistribute kernel metric '45'
# set protocols bgp timers keepalive '35'
# vyos@vyos:~$

- name: Replace
  vyos.vyos.vyos_vrrp:
    config:
      as_number: "65536"
      network:
        - address: "203.0.113.0/24"
          route_map: map01
      redistribute:
        - protocol: "static"
          route_map: "map01"
      neighbor:
        - address: "192.0.2.40"
          advertisement_interval: 72
          capability:
            orf: "receive"
      bgp_params:
        bestpath:
          as_path: "confed"
    state: replaced
# After state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp neighbor 192.0.2.40 advertisement-interval '72'
# set protocols bgp neighbor 192.0.2.40 capability orf prefix-list 'receive'
# set protocols bgp network 203.0.113.0/24 route-map 'map01'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp redistribute static route-map 'map01'
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed"
#             }
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.40",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     },
#     "before": {
#         "aggregate_address": [
#             {
#                 "prefix": "192.0.2.0/24",
#                 "summary_only": true
#             },
#             {
#                 "prefix": "203.0.113.0/24",
#                 "as_set": true
#             }
#         ],
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "confederation": [
#                 {
#                     "identifier": 66
#                 },
#                 {
#                     "peers": 20
#                 },
#                 {
#                     "peers": 55
#                 }
#             ],
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "router_id": "192.1.2.9"
#         },
#         "maximum_paths": [
#             {
#                 "count": 20,
#                 "path": "ebgp"
#             },
#             {
#                 "count": 55,
#                 "path": "ibgp"
#             }
#         ],
#         "neighbor": [
#             {
#                 "address": "192.0.2.25",
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.5",
#                 "attribute_unchanged": {
#                     "as_path": true,
#                     "med": true,
#                     "next_hop": true
#                 },
#                 "ebgp_multihop": 2,
#                 "remote_as": 101,
#                 "update_source": "192.0.2.25"
#             },
#             {
#                 "address": "5001::64",
#                 "distribute_list": [
#                     {
#                         "acl": 20,
#                         "action": "export"
#                     },
#                     {
#                         "acl": 40,
#                         "action": "import"
#                     }
#                 ],
#                 "maximum_prefix": 34
#             }
#         ],
#         "network": [
#             {
#                 "address": "192.1.13.0/24",
#                 "backdoor": true
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "connected",
#                 "route_map": "map01"
#             },
#             {
#                 "metric": 45,
#                 "protocol": "kernel"
#             }
#         ],
#         "timers": {
#             "keepalive": 35
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp timers",
#         "delete protocols bgp maximum-paths ",
#         "delete protocols bgp maximum-paths ",
#         "delete protocols bgp parameters router-id 192.1.2.9",
#         "delete protocols bgp parameters default",
#         "delete protocols bgp parameters confederation",
#         "delete protocols bgp parameters bestpath compare-routerid",
#         "delete protocols bgp aggregate-address",
#         "delete protocols bgp network 192.1.13.0/24",
#         "delete protocols bgp redistribute kernel",
#         "delete protocols bgp redistribute kernel",
#         "delete protocols bgp redistribute connected",
#         "delete protocols bgp redistribute connected",
#         "delete protocols bgp neighbor 5001::64",
#         "delete protocols bgp neighbor 203.0.113.5",
#         "delete protocols bgp neighbor 192.0.2.25",
#         "set protocols bgp neighbor 192.0.2.40 advertisement-interval 72",
#         "set protocols bgp neighbor 192.0.2.40 capability orf prefix-list receive",
#         "set protocols bgp redistribute static route-map map01",
#         "set protocols bgp network 203.0.113.0/24 route-map map01"
#     ],

# Using deleted:
# -------------

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp neighbor 192.0.2.40 advertisement-interval '72'
# set protocols bgp neighbor 192.0.2.40 capability orf prefix-list 'receive'
# set protocols bgp network 203.0.113.0/24 route-map 'map01'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp redistribute static route-map 'map01'
# vyos@vyos:~$

- name: Delete configuration
  vyos.vyos.vyos_vrrp:
    config:
      as_number: "65536"
    state: deleted

# After state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp '65536'
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#         "as_number": 65536
#     },
#     "before": {
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed"
#             }
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.40",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp neighbor 192.0.2.40",
#         "delete protocols bgp redistribute",
#         "delete protocols bgp network",
#         "delete protocols bgp parameters"
#     ],

# Using purged:

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp aggregate-address 192.0.2.0/24 'summary-only'
# set protocols bgp aggregate-address 203.0.113.0/24 'as-set'
# set protocols bgp maximum-paths ebgp '20'
# set protocols bgp maximum-paths ibgp '55'
# set protocols bgp neighbor 192.0.2.25 'disable-connected-check'
# set protocols bgp neighbor 192.0.2.25 timers holdtime '30'
# set protocols bgp neighbor 192.0.2.25 timers keepalive '10'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'as-path'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'med'
# set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'next-hop'
# set protocols bgp neighbor 203.0.113.5 ebgp-multihop '2'
# set protocols bgp neighbor 203.0.113.5 remote-as '101'
# set protocols bgp neighbor 203.0.113.5 update-source '192.0.2.25'
# set protocols bgp neighbor 5001::64 distribute-list export '20'
# set protocols bgp neighbor 5001::64 distribute-list import '40'
# set protocols bgp neighbor 5001::64 maximum-prefix '34'
# set protocols bgp network 192.1.13.0/24 'backdoor'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp parameters bestpath 'compare-routerid'
# set protocols bgp parameters confederation identifier '66'
# set protocols bgp parameters confederation peers '20'
# set protocols bgp parameters confederation peers '55'
# set protocols bgp parameters default 'no-ipv4-unicast'
# set protocols bgp parameters router-id '192.1.2.9'
# set protocols bgp redistribute connected route-map 'map01'
# set protocols bgp redistribute kernel metric '45'
# set protocols bgp timers keepalive '35'
# vyos@vyos:~$


- name: Purge configuration
  vyos.vyos.vyos_vrrp:
    config:
      as_number: "65536"
    state: purged

# After state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# vyos@vyos:~$
#
# Module Execution:
#
#     "after": {},
#     "before": {
#         "aggregate_address": [
#             {
#                 "prefix": "192.0.2.0/24",
#                 "summary_only": true
#             },
#             {
#                 "prefix": "203.0.113.0/24",
#                 "as_set": true
#             }
#         ],
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "confederation": [
#                 {
#                     "identifier": 66
#                 },
#                 {
#                     "peers": 20
#                 },
#                 {
#                     "peers": 55
#                 }
#             ],
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "router_id": "192.1.2.9"
#         },
#         "maximum_paths": [
#             {
#                 "count": 20,
#                 "path": "ebgp"
#             },
#             {
#                 "count": 55,
#                 "path": "ibgp"
#             }
#         ],
#         "neighbor": [
#             {
#                 "address": "192.0.2.25",
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.5",
#                 "attribute_unchanged": {
#                     "as_path": true,
#                     "med": true,
#                     "next_hop": true
#                 },
#                 "ebgp_multihop": 2,
#                 "remote_as": 101,
#                 "update_source": "192.0.2.25"
#             },
#             {
#                 "address": "5001::64",
#                 "distribute_list": [
#                     {
#                         "acl": 20,
#                         "action": "export"
#                     },
#                     {
#                         "acl": 40,
#                         "action": "import"
#                     }
#                 ],
#                 "maximum_prefix": 34
#             }
#         ],
#         "network": [
#             {
#                 "address": "192.1.13.0/24",
#                 "backdoor": true
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "connected",
#                 "route_map": "map01"
#             },
#             {
#                 "metric": 45,
#                 "protocol": "kernel"
#             }
#         ],
#         "timers": {
#             "keepalive": 35
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 65536"
#     ],


# Deleted in presence of address family under neighbors:

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp neighbor 192.0.2.43 advertisement-interval '72'
# set protocols bgp neighbor 192.0.2.43 capability 'dynamic'
# set protocols bgp neighbor 192.0.2.43 'disable-connected-check'
# set protocols bgp neighbor 192.0.2.43 timers holdtime '30'
# set protocols bgp neighbor 192.0.2.43 timers keepalive '10'
# set protocols bgp neighbor 203.0.113.0 address-family 'ipv6-unicast'
# set protocols bgp neighbor 203.0.113.0 capability orf prefix-list 'receive'
# set protocols bgp network 203.0.113.0/24 route-map 'map01'
# set protocols bgp parameters 'always-compare-med'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp parameters bestpath 'compare-routerid'
# set protocols bgp parameters dampening half-life '33'
# set protocols bgp parameters dampening max-suppress-time '20'
# set protocols bgp parameters dampening re-use '60'
# set protocols bgp parameters dampening start-suppress-time '5'
# set protocols bgp parameters default 'no-ipv4-unicast'
# set protocols bgp parameters distance global external '66'
# set protocols bgp parameters distance global internal '20'
# set protocols bgp parameters distance global local '10'
# set protocols bgp redistribute static route-map 'map01'
# vyos@vyos:~$ ^C
# vyos@vyos:~$

- name: Delete configuration
  vyos.vyos.vyos_vrrp:
    config:
      as_number: "65536"
    state: deleted

# Module Execution:
#
# "changed": false,
#     "invocation": {
#         "module_args": {
#             "config": {
#                 "aggregate_address": null,
#                 "as_number": 65536,
#                 "bgp_params": null,
#                 "maximum_paths": null,
#                 "neighbor": null,
#                 "network": null,
#                 "redistribute": null,
#                 "timers": null
#             },
#             "running_config": null,
#             "state": "deleted"
#         }
#     },
#     "msg": "Use the _bgp_address_family module to delete the address_family under neighbor 203.0.113.0, before replacing/deleting the neighbor."
# }

# using gathered:
# --------------

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp system-as 65536
# set protocols bgp neighbor 192.0.2.43 advertisement-interval '72'
# set protocols bgp neighbor 192.0.2.43 capability 'dynamic'
# set protocols bgp neighbor 192.0.2.43 'disable-connected-check'
# set protocols bgp neighbor 192.0.2.43 timers holdtime '30'
# set protocols bgp neighbor 192.0.2.43 timers keepalive '10'
# set protocols bgp neighbor 203.0.113.0 address-family 'ipv6-unicast'
# set protocols bgp neighbor 203.0.113.0 capability orf prefix-list 'receive'
# set protocols bgp network 203.0.113.0/24 route-map 'map01'
# set protocols bgp parameters 'always-compare-med'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp parameters bestpath 'compare-routerid'
# set protocols bgp parameters dampening half-life '33'
# set protocols bgp parameters dampening max-suppress-time '20'
# set protocols bgp parameters dampening re-use '60'
# set protocols bgp parameters dampening start-suppress-time '5'
# set protocols bgp parameters default 'no-ipv4-unicast'
# set protocols bgp parameters distance global external '66'
# set protocols bgp parameters distance global internal '20'
# set protocols bgp parameters distance global local '10'
# set protocols bgp redistribute static route-map 'map01'
# vyos@vyos:~$ ^C

- name: gather configs
  vyos.vyos.vyos_vrrp:
    state: gathered

# Module Execution:
# "gathered": {
#         "as_number": 65536,
#         "bgp_params": {
#             "always_compare_med": true,
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "distance": [
#                 {
#                     "type": "external",
#                     "value": 66
#                 },
#                 {
#                     "type": "internal",
#                     "value": 20
#                 },
#                 {
#                     "type": "local",
#                     "value": 10
#                 }
#             ]
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.43",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "dynamic": true
#                 },
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.0",
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     },
#

# Using parsed:
# ------------

# parsed.cfg

# set protocols bgp neighbor 192.0.2.43 advertisement-interval '72'
# set protocols bgp neighbor 192.0.2.43 capability 'dynamic'
# set protocols bgp neighbor 192.0.2.43 'disable-connected-check'
# set protocols bgp neighbor 192.0.2.43 timers holdtime '30'
# set protocols bgp neighbor 192.0.2.43 timers keepalive '10'
# set protocols bgp neighbor 203.0.113.0 address-family 'ipv6-unicast'
# set protocols bgp neighbor 203.0.113.0 capability orf prefix-list 'receive'
# set protocols bgp network 203.0.113.0/24 route-map 'map01'
# set protocols bgp parameters 'always-compare-med'
# set protocols bgp parameters bestpath as-path 'confed'
# set protocols bgp parameters bestpath 'compare-routerid'
# set protocols bgp parameters dampening half-life '33'
# set protocols bgp parameters dampening max-suppress-time '20'
# set protocols bgp parameters dampening re-use '60'
# set protocols bgp parameters dampening start-suppress-time '5'
# set protocols bgp parameters default 'no-ipv4-unicast'
# set protocols bgp parameters distance global external '66'
# set protocols bgp parameters distance global internal '20'
# set protocols bgp parameters distance global local '10'
# set protocols bgp redistribute static route-map 'map01'

- name: parse configs
  vyos.vyos.vyos_vrrp:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
  tags:
    - parsed

# Module execution:
# "parsed": {
#         "as_number": 65536,
#         "bgp_params": {
#             "always_compare_med": true,
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "distance": [
#                 {
#                     "type": "external",
#                     "value": 66
#                 },
#                 {
#                     "type": "internal",
#                     "value": 20
#                 },
#                 {
#                     "type": "local",
#                     "value": 10
#                 }
#             ]
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.43",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "dynamic": true
#                 },
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.0",
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     }
#

# Using rendered:
# --------------

- name: Render
  vyos.vyos.vyos_vrrp:
    config:
      as_number: "65536"
      network:
        - address: "203.0.113.0/24"
          route_map: map01
      redistribute:
        - protocol: "static"
          route_map: "map01"
      bgp_params:
        always_compare_med: true
        dampening:
          start_suppress_time: 5
          max_suppress_time: 20
          half_life: 33
          re_use: 60
        distance:
          - type: "internal"
            value: 20
          - type: "local"
            value: 10
          - type: "external"
            value: 66
        bestpath:
          as_path: "confed"
          compare_routerid: true
        default:
          no_ipv4_unicast: true
      neighbor:
        - address: "192.0.2.43"
          disable_connected_check: true
          advertisement_interval: 72
          capability:
            dynamic: true
          timers:
            holdtime: 30
            keepalive: 10
        - address: "203.0.113.0"
          capability:
            orf: "receive"
    state: rendered

# Module Execution:
# "rendered": [
#         "set protocols bgp neighbor 192.0.2.43 disable-connected-check",
#         "set protocols bgp neighbor 192.0.2.43 advertisement-interval 72",
#         "set protocols bgp neighbor 192.0.2.43 capability dynamic",
#         "set protocols bgp neighbor 192.0.2.43 timers holdtime 30",
#         "set protocols bgp neighbor 192.0.2.43 timers keepalive 10",
#         "set protocols bgp neighbor 203.0.113.0 capability orf prefix-list receive",
#         "set protocols bgp redistribute static route-map map01",
#         "set protocols bgp network 203.0.113.0/24 route-map map01",
#         "set protocols bgp parameters always-compare-med",
#         "set protocols bgp parameters dampening half-life 33",
#         "set protocols bgp parameters dampening max-suppress-time 20",
#         "set protocols bgp parameters dampening re-use 60",
#         "set protocols bgp parameters dampening start-suppress-time 5",
#         "set protocols bgp parameters distance global internal 20",
#         "set protocols bgp parameters distance global local 10",
#         "set protocols bgp parameters distance global external 66",
#         "set protocols bgp parameters bestpath as-path confed",
#         "set protocols bgp parameters bestpath compare-routerid",
#         "set protocols bgp parameters default no-ipv4-unicast"
#     ]
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
    - set protocols bgp redistribute static route-map map01
    - set protocols bgp network 203.0.113.0/24 route-map map01
    - set protocols bgp parameters always-compare-med
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set protocols bgp redistribute static route-map map01
    - set protocols bgp network 203.0.113.0/24 route-map map01
    - set protocols bgp parameters always-compare-med
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

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vrrp.vrrp import (
    VrrpArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vrrp.vrrp import (
    Vrrp,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=VrrpArgs.argument_spec,
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

    result = Vrrp(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
