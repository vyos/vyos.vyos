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
          name:
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
            type: int
          persistence_timeout:
            description:
              - Client persistence timeout in seconds.
            type: int
          port:
            description:
              - TCP/UDP port provided by the virtual service.
            type: int
          protocol:
            description:
              - Transport protocol for the virtual server.
            type: str
            choices: [tcp, udp]

          real_server:
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
              connection_timeout:
                description:
                  - Backend server connection timeout.
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
                default: false

              excluded_address:
                description:
                  - IP address excluded from source checks.
                type: list
                elements: str

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
                default: false

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
                default: false

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
                    type: list
                    elements: str

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

          snmp:
            description:
              - Enable SNMP support for VRRP.
            type: str
            choices: ['enabled', 'disabled']

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
      - overridden
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

# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# vyos@vyos:~$

- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_vrrp:
    config:
      disable: true
      virtual_servers:
        - name: s1
          address: 10.10.10.5
          algorithm: round-robin
          real_server:
            - address: 10.10.50.2
              port: 8443
        - name: s2
          address: 10.10.10.2
          persistence_timeout: 30
          port: 81
          protocol: tcp
        - name: s3
          address: 10.10.10.3
          port: 88
          protocol: udp
      vrrp:
        snmp: enabled
        global_parameters:
          startup_delay: 30
          garp:
            master_repeat: 6
        groups:
          - name: "g1"
            peer_address: 192.168.1.3
            priority: 100
            disable: false
            no_preempt: false
            vrid: 20
        sync_groups:
          - name: "sg1"
            health_check:
              failure_count: 5
    state: merged

# After State
# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# set high-availability disable
# set high-availability virtual-server s1 address '10.10.10.5'
# set high-availability virtual-server s1 algorithm 'round-robin'
# set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '30'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp global-parameters startup-delay '30'
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '5'
# vyos@vyos:~$
#
# # Module Execution:
#
# "after": {
#     "disable": true,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.5",
#             "algorithm": "round-robin",
#             "name": "s1",
#             "real_server": [
#                 {
#                     "address": "10.10.50.2",
#                     "port": 8443
#                 }
#             ]
#         },
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 30,
#             "port": 81,
#             "protocol": "tcp"
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp"
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             },
#             "startup_delay": 30
#         },
#         "groups": [
#             {
#                 "disable": false,
#                 "name": "g1",
#                 "no_preempt": false,
#                 "peer_address": "192.168.1.3",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 5
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
# "before": {
#     "disable": false
# },
# "changed": true,
# "commands": [
#     "set high-availability disable",
#     "set high-availability virtual-server s1 address 10.10.10.5",
#     "set high-availability virtual-server s1 algorithm round-robin",
#     "set high-availability virtual-server s1 real-server 10.10.50.2 port 8443",
#     "set high-availability virtual-server s2 address 10.10.10.2",
#     "set high-availability virtual-server s2 persistence-timeout 30",
#     "set high-availability virtual-server s2 port 81",
#     "set high-availability virtual-server s2 protocol tcp",
#     "set high-availability virtual-server s3 address 10.10.10.3",
#     "set high-availability virtual-server s3 port 88",
#     "set high-availability virtual-server s3 protocol udp",
#     "set high-availability vrrp global-parameters garp master-repeat 6",
#     "set high-availability vrrp global-parameters startup-delay 30",
#     "set high-availability vrrp group g1 peer-address 192.168.1.3",
#     "set high-availability vrrp group g1 priority 100",
#     "set high-availability vrrp group g1 vrid 20",
#     "set high-availability vrrp snmp",
#     "set high-availability vrrp sync-group sg1 health-check failure-count 5"
# ],

# Using replaced:
# --------------

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# set high-availability disable
# set high-availability virtual-server s1 address '10.10.10.5'
# set high-availability virtual-server s1 algorithm 'round-robin'
# set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '30'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp global-parameters startup-delay '30'
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '5'
# vyos@vyos:~$

- name: Replace
  vyos.vyos.vyos_vrrp:
    config:
      disable: false
      virtual_servers:
        - name: s1
          address: 10.10.10.3
          algorithm: round-robin
          port: 8443
          real_server:
            - address: 10.10.50.3
              port: 8443
        - name: s2
          address: 10.10.10.2
          persistence_timeout: 300
          port: 81
          protocol: tcp
          real_server:
            - address: 10.10.50.30
              port: 8443
        - name: s3
          address: 10.10.10.3
          port: 88
          protocol: udp
          real_server:
            - address: 10.10.50.6
              port: 8443
      vrrp:
        snmp: enabled
        global_parameters:
          startup_delay: 30
          garp:
            master_repeat: 6
        groups:
          - name: "g1"
            peer_address: 192.168.1.13
            priority: 100
            disable: false
            no_preempt: true
            interface: eth1
            address: 192.168.51.13
            vrid: 20
        sync_groups:
          - name: "sg1"
            health_check:
              failure_count: 3
    state: replaced

# After state:

# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# set high-availability virtual-server s1 address '10.10.10.3'
# set high-availability virtual-server s1 algorithm 'round-robin'
# set high-availability virtual-server s1 port '8443'
# set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
# set high-availability virtual-server s1 real-server 10.10.50.3 port '8443'
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '300'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s2 real-server 10.10.50.3 port '8443'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability virtual-server s3 real-server 10.10.50.6 port '8443'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp global-parameters startup-delay '30'
# set high-availability vrrp group g1 address 192.168.51.13
# set high-availability vrrp group g1 interface 'eth1'
# set high-availability vrrp group g1 no-preempt
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 peer-address '192.168.1.13'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '3'
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#     "disable": false,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.3",
#             "algorithm": "round-robin",
#             "name": "s1",
#             "port": 8443,
#             "real_server": [
#                 {
#                     "address": "10.10.50.2",
#                     "port": 8443
#                 },
#                 {
#                     "address": "10.10.50.3",
#                     "port": 8443
#                 }
#             ]
#         },
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 300,
#             "port": 81,
#             "protocol": "tcp",
#             "real_server": [
#                 {
#                     "address": "10.10.50.3",
#                     "port": 8443
#                 }
#             ]
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp",
#             "real_server": [
#                 {
#                     "address": "10.10.50.6",
#                     "port": 8443
#                 }
#             ]
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             },
#             "startup_delay": 30
#         },
#         "groups": [
#             {
#                 "address": "192.168.51.13",
#                 "disable": false,
#                 "interface": "eth1",
#                 "name": "g1",
#                 "no_preempt": true,
#                 "peer_address": "192.168.1.13",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 3
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
# "before": {
#     "disable": true,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.5",
#             "algorithm": "round-robin",
#             "name": "s1",
#             "real_server": [
#                 {
#                     "address": "10.10.50.2",
#                     "port": 8443
#                 }
#             ]
#         },
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 30,
#             "port": 81,
#             "protocol": "tcp"
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp"
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             },
#             "startup_delay": 30
#         },
#         "groups": [
#             {
#                 "disable": false,
#                 "name": "g1",
#                 "no_preempt": false,
#                 "peer_address": "192.168.1.3",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 5
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
# "changed": true,
# "commands": [
#     "delete high-availability disable",
#     "set high-availability virtual-server s1 address 10.10.10.3",
#     "set high-availability virtual-server s1 port 8443",
#     "set high-availability virtual-server s1 real-server 10.10.50.3 port 8443",
#     "set high-availability virtual-server s2 persistence-timeout 300",
#     "set high-availability virtual-server s2 real-server 10.10.50.3 port 8443",
#     "set high-availability virtual-server s3 real-server 10.10.50.6 port 8443",
#     "set high-availability vrrp group g1 address 192.168.51.13",
#     "set high-availability vrrp group g1 interface eth1",
#     "set high-availability vrrp group g1 no-preempt",
#     "set high-availability vrrp group g1 peer-address 192.168.1.13",
#     "set high-availability vrrp sync-group sg1 health-check failure-count 3"
# ],

# Using deleted:
# -------------

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# set high-availability disable
# set high-availability virtual-server s1 address '10.10.10.5'
# set high-availability virtual-server s1 algorithm 'round-robin'
# set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '30'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp global-parameters startup-delay '30'
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '5'
# vyos@vyos:~$

- name: Delete configuration
  vyos.vyos.vyos_vrrp:
    config:
      disable: false
      vrrp:
        snmp: disabled
        global_parameters:
          startup_delay: 32
          version: 3
      virtual_servers:
        - name: 's1'
          address: '10.10.10.1'
          algorithm: 'round-robin'
          delay_loop: 60
          forward_method: 'direct'
          persistence_timeout: 30
          port: 443
          protocol: 'tcp'
          real_server:
            - address: '10.10.10.1'
              connection_timeout: 61
              port: 443
    state: deleted

# After state:

# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# set high-availability disable
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '30'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '5'

# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#     "disable": true,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 30,
#             "port": 81,
#             "protocol": "tcp"
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp"
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             }
#         },
#         "groups": [
#             {
#                 "disable": false,
#                 "name": "g1",
#                 "no_preempt": false,
#                 "peer_address": "192.168.1.3",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 5
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
# "before": {
#     "disable": true,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.5",
#             "algorithm": "round-robin",
#             "name": "s1",
#             "real_server": [
#                 {
#                     "address": "10.10.50.2",
#                     "port": 8443
#                 }
#             ]
#         },
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 30,
#             "port": 81,
#             "protocol": "tcp"
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp"
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             },
#             "startup_delay": 30
#         },
#         "groups": [
#             {
#                 "disable": false,
#                 "name": "g1",
#                 "no_preempt": false,
#                 "peer_address": "192.168.1.3",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 5
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
# "changed": true,
# "commands": [
#     "delete high-availability virtual-server s1",
#     "delete high-availability vrrp global-parameters startup-delay"
# ],

# Using purged:

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# set high-availability disable
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '30'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '5'
# vyos@vyos:~$


- name: Purge configuration
  vyos.vyos.vyos_vrrp:
    config:
    state: purged

# After state:

# vyos@vyos:~$ show configuration commands |  match "set high-availability"
# vyos@vyos:~$
#
# Module Execution:
#
# "after": {
#     "disable": false
# },
# "before": {
#     "disable": true,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 30,
#             "port": 81,
#             "protocol": "tcp"
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp"
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             }
#         },
#         "groups": [
#             {
#                 "disable": false,
#                 "name": "g1",
#                 "no_preempt": false,
#                 "peer_address": "192.168.1.3",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 5
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
# "changed": true,
# "commands": [
#     "delete high-availability"
# ],


# using gathered:
# --------------

# Before state:
# vyos@vyos:~$
# show configuration commands |  match "set high-availability"
# set high-availability disable
# set high-availability virtual-server s1 address '10.10.10.5'
# set high-availability virtual-server s1 algorithm 'round-robin'
# set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
# set high-availability virtual-server s2 address '10.10.10.2'
# set high-availability virtual-server s2 persistence-timeout '30'
# set high-availability virtual-server s2 port '81'
# set high-availability virtual-server s2 protocol 'tcp'
# set high-availability virtual-server s3 address '10.10.10.3'
# set high-availability virtual-server s3 port '88'
# set high-availability virtual-server s3 protocol 'udp'
# set high-availability vrrp global-parameters garp master-repeat '6'
# set high-availability vrrp global-parameters startup-delay '30'
# set high-availability vrrp group g1 peer-address '192.168.1.3'
# set high-availability vrrp group g1 priority '100'
# set high-availability vrrp group g1 vrid '20'
# set high-availability vrrp snmp
# set high-availability vrrp sync-group sg1 health-check failure-count '5'
# vyos@vyos:~$

- name: gather configs
  vyos.vyos.vyos_vrrp:
    state: gathered

# Module Execution:
# "changed": false,
# "gathered": {
#     "disable": true,
#     "virtual_servers": [
#         {
#             "address": "10.10.10.5",
#             "algorithm": "round-robin",
#             "name": "s1",
#             "real_server": [
#                 {
#                     "address": "10.10.50.2",
#                     "port": 8443
#                 }
#             ]
#         },
#         {
#             "address": "10.10.10.2",
#             "name": "s2",
#             "persistence_timeout": 30,
#             "port": 81,
#             "protocol": "tcp"
#         },
#         {
#             "address": "10.10.10.3",
#             "name": "s3",
#             "port": 88,
#             "protocol": "udp"
#         }
#     ],
#     "vrrp": {
#         "global_parameters": {
#             "garp": {
#                 "master_repeat": 6
#             },
#             "startup_delay": 30
#         },
#         "groups": [
#             {
#                 "disable": false,
#                 "name": "g1",
#                 "no_preempt": false,
#                 "peer_address": "192.168.1.3",
#                 "priority": 100,
#                 "rfc3768_compatibility": false,
#                 "vrid": 20
#             }
#         ],
#         "snmp": "enabled",
#         "sync_groups": [
#             {
#                 "health_check": {
#                     "failure_count": 5
#                 },
#                 "name": "sg1"
#             }
#         ]
#     }
# },
#

# Using parsed:
# ------------

# parsed.cfg
# set high-availability vrrp group g1 interface eth2
# set high-availability vrrp group g1 address 1.1.1.1
# set high-availability vrrp group g1 disable
# set high-availability vrrp group g1 no-preempt
# set high-availability vrrp group g1 advertise-interval 10
# set high-availability vrrp group g1 peer-address 2.2.2.2
# set high-availability vrrp group g1 rfc3768-compatibility
# set high-availability vrrp group g1 vrid 20

- name: parse configs
  vyos.vyos.vyos_vrrp:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Module execution:
# "parsed": {
#     "disable": false,
#     "vrrp": {
#         "groups": [
#             {
#                 "address": "1.1.1.1",
#                 "advertise_interval": 10,
#                 "disable": true,
#                 "interface": "eth2",
#                 "name": "g1",
#                 "no_preempt": true,
#                 "peer_address": "2.2.2.2",
#                 "rfc3768_compatibility": true,
#                 "vrid": 20
#             }
#         ]
#     }
# }
#

# Using rendered:
# --------------

- name: Render
  vyos.vyos.vyos_vrrp:
    config:
      disable: true
      vrrp:
        snmp: enabled
        global_parameters:
          startup_delay: 32
          version: 3
          garp:
            interval: 30
            master_delay: 11
            master_refresh: 100
            master_refresh_repeat: 200
            master_repeat: 5
    state: rendered

# Module Execution:
# "rendered": [
#     "set high-availability disable",
#     "set high-availability vrrp global-parameters garp interval 30",
#     "set high-availability vrrp global-parameters garp master-delay 11",
#     "set high-availability vrrp global-parameters garp master-refresh 100",
#     "set high-availability vrrp global-parameters garp master-refresh-repeat 200",
#     "set high-availability vrrp global-parameters garp master-repeat 5",
#     "set high-availability vrrp global-parameters startup-delay 32",
#     "set high-availability vrrp global-parameters version 3",
#     "set high-availability vrrp snmp"
# ]
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
    - set high-availability vrrp group g1 address '1.1.1.1'
    - set high-availability vrrp group g1 advertise-interval '10'
    - set high-availability vrrp group g1 description 'Group 1'
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set high-availability vrrp global-parameters garp master-delay '10'
    - set high-availability vrrp global-parameters garp master-refresh '100'
    - set high-availability vrrp global-parameters garp master-refresh-repeat '200'
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
