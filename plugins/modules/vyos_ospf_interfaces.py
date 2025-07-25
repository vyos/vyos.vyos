#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_ospf_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_ospf_interfaces
version_added: 1.2.0
short_description: OSPF Interfaces Resource Module.
description:
- This module manages OSPF configuration of interfaces on devices running VYOS.
- The provided examples of commands are valid for VyOS 1.4+
author: Gomathi Selvi Srinivasan (@GomathiselviS)
options:
  config:
    description: A list of OSPF configuration for interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name/Identifier of the interface.
        type: str
      address_family:
        description:
        - OSPF settings on the interfaces in address-family context.
        type: list
        elements: dict
        suboptions:
          afi:
            description:
            - Address Family Identifier (AFI) for OSPF settings on the interfaces.
            type: str
            choices: ['ipv4', 'ipv6']
            required: true
          authentication:
            description:
            - Authentication settings on the interface.
            type: dict
            suboptions:
              plaintext_password:
                description:
                - Plain Text password.
                type: str
              md5_key:
                description:
                - md5 parameters.
                type: dict
                suboptions:
                  key_id:
                    description:
                    - key id.
                    type: int
                  key:
                    description:
                    - md5 key.
                    type: str
          bandwidth:
            description:
            -  Bandwidth of interface (kilobits/sec)
            type: int
          cost:
            description:
            - metric associated with interface.
            type: int
          dead_interval:
            description:
            - Time interval to detect a dead router.
            type: int
          hello_interval:
            description:
            - Timer interval between transmission of hello packets.
            type: int
          mtu_ignore:
            description:
            - if True, Disable MTU check for Database Description packets.
            type: bool
          network:
            description:
            - Interface type.
            type: str
          priority:
            description:
            - Interface priority.
            type: int
          retransmit_interval:
            description:
            - LSA retransmission interval.
            type: int
          transmit_delay:
            description:
            - LSA transmission delay.
            type: int
          ifmtu:
            description:
            - interface MTU.
            type: int
          instance:
            description:
            - Instance ID.
            type: str
          passive:
            description:
            - If True, disables forming adjacency.
            type: bool
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the VYOS device by
      executing the command B(show configuration commands |  match "set interfaces").
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - parsed
    - rendered
    default: merged
"""

EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#

# @vyos:~$ show configuration commands | match "ospf"

- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_ospf_interfaces:
    config:
      - name: "eth1"
        address_family:
          - afi: "ipv4"
            transmit_delay: 50
            priority: 26
            network: "point-to-point"
          - afi: "ipv6"
            dead_interval: 39
      - name: "bond2"
        address_family:
          - afi: "ipv4"
            transmit_delay: 45
            bandwidth: 70
            authentication:
              md5_key:
                key_id: 10
                key: "1111111111232345"
          - afi: "ipv6"
            passive: true
    state: merged

# After State:
# --------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'

# "after": [
#        "
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "md5_key": {
#                            "key": "1111111111232345",
#                            "key_id": 10
#                        }
#                    },
#                    "bandwidth": 70,
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "network": "point-to-point",
#                    "priority": 26,
#                    "transmit_delay": 50
#                },
#                {
#                    "afi": "ipv6",
#                    "dead_interval": 39
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "before": [
#        {
#            "name": "eth0"
#        },
#        {
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "changed": true,
#    "commands": [
#        "set protocols ospf interface eth1 transmit-delay 50",
#        "set protocols ospf interface eth1 priority 26",
#        "set protocols ospf interface eth1 network point-to-point",
#        "set protocols ospfv3 interface eth1 dead-interval 39",
#        "set protocols ospf interface bond2 transmit-delay 45",
#        "set protocols ospf interface bond2 bandwidth 70",
#        "set protocols ospf interface bond2 authentication md5 key-id 10 md5-key 1111111111232345",
#        "set protocols ospfv3 interface bond2 passive"
#    ],

# Using replaced:

# Before State:
# ------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'

- name: Replace provided configuration with device configuration
  vyos.vyos.vyos_ospf_interfaces:
    config:
      - name: "eth1"
        address_family:
          - afi: "ipv4"
            cost: 100
          - afi: "ipv6"
            ifmtu: 33
      - name: "bond2"
        address_family:
          - afi: "ipv4"
            transmit_delay: 45
          - afi: "ipv6"
            passive: true
    state: replaced

# After State:
# -----------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth1 cost '100'
# set protocols ospfv3 interface eth1 ifmtu '33'
# vyos@vyos:~$

# Module Execution
# ----------------
#    "after": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "cost": 100
#                },
#                {
#                    "afi": "ipv6",
#                    "ifmtu": 33
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "before": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "md5_key": {
#                            "key": "1111111111232345",
#                            "key_id": 10
#                        }
#                    },
#                    "bandwidth": 70,
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "network": "point-to-point",
#                    "priority": 26,
#                    "transmit_delay": 50
#                },
#                {
#                    "afi": "ipv6",
#                    "dead_interval": 39
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
#    "changed": true,
#    "commands": [
#        "set protocols ospf interface eth1 cost 100",
#        "set protocols ospfv3 interface eth1 ifmtu 33",
#        "delete protocols ospf interface eth1 network point-to-point",
#        "delete protocols ospf interface eth1 priority 26",
#        "delete protocols ospf interface eth1 transmit-delay 50",
#        "delete protocols ospfv3 interface eth1 dead-interval 39",
#        "delete protocols ospf interface bond2 authentication",
#        "delete protocols ospf interface bond2 bandwidth 70"
#    ],
#

# Using Overridden:
# -----------------

# Before State:
# ------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth1 cost '100'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'
# set protocols ospfv3 interface eth1 ifmtu '33'
# vyos@vyos:~$

- name: Override device configuration with provided configuration
  vyos.vyos.vyos_ospf_interfaces:
    config:
      - name: "eth0"
        address_family:
          - afi: "ipv4"
            cost: 100
          - afi: "ipv6"
            ifmtu: 33
            passive: true
    state: overridden

# After State:
# -----------

# 200~vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface eth0 cost '100'
# set protocols ospfv3 interface eth0 ifmtu '33'
# set protocols ospfv3 interface eth0 'passive'
# vyos@vyos:~$
#
#
#     "after": [
#         {
#             "name": "bond2"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 100
#                 },
#                 {
#                     "afi": "ipv6",
#                     "ifmtu": 33,
#                     "passive": true
#                 }
#             ],
#             "name": "eth0"
#         },
#         {
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 100,
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39,
#                     "ifmtu": 33
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete protocols ospf interface bond2",
#         "delete protocols ospfv3 interface bond2",
#         "delete protocols ospf interface eth1",
#         "delete protocols ospfv3 interface eth1",
#         "set protocols ospf interface eth0 cost 100",
#         "set protocols ospfv3 interface eth0 ifmtu 33",
#         "set protocols ospfv3 interface eth0 passive"
#     ],
#

# Using deleted:
# -------------

# before state:
# -------------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth0 cost '100'
# set protocols ospfv3 interface eth0 ifmtu '33'
# set protocols ospfv3 interface eth0 'passive'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'
# vyos@vyos:~$

- name: Delete device configuration
  vyos.vyos.vyos_ospf_interfaces:
    config:
      - name: "eth0"
    state: deleted

# After State:
# -----------

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'
# vyos@vyos:~$
#
#
# "after": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 100
#                 },
#                 {
#                     "afi": "ipv6",
#                     "ifmtu": 33,
#                     "passive": true
#                 }
#             ],
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "name": "eth2"
#         },
#         {
#             "name": "eth3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete protocols ospf interface eth0",
#         "delete protocols ospfv3 interface eth0"
#     ],
#
# Using parsed:
# parsed.cfg:

# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth0 cost '50'
# set protocols ospf interface eth0 priority '26'
# set protocols ospfv3 interface eth0 instance-id '33'
# set protocols ospfv3 interface eth0 'mtu-ignore'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'
#

- name: parse configs
  vyos.vyos.vyos_ospf_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Module Execution:
# ----------------

#  "parsed": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "md5_key": {
#                             "key": "1111111111232345",
#                             "key_id": 10
#                         }
#                     },
#                     "bandwidth": 70,
#                     "transmit_delay": 45
#                 },
#                 {
#                     "afi": "ipv6",
#                     "passive": true
#                 }
#             ],
#             "name": "bond2"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "cost": 50,
#                     "priority": 26
#                 },
#                 {
#                     "afi": "ipv6",
#                     "instance": "33",
#                     "mtu_ignore": true
#                 }
#             ],
#             "name": "eth0"
#         },
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "network": "point-to-point",
#                     "priority": 26,
#                     "transmit_delay": 50
#                 },
#                 {
#                     "afi": "ipv6",
#                     "dead_interval": 39
#                 }
#             ],
#             "name": "eth1"
#         }
#     ]

# Using rendered:
# --------------

- name: Render
  vyos.vyos.vyos_ospf_interfaces:
    config:
      - name: "eth1"
        address_family:
          - afi: "ipv4"
            transmit_delay: 50
            priority: 26
            network: "point-to-point"
          - afi: "ipv6"
            dead_interval: 39
      - name: "bond2"
        address_family:
          - afi: "ipv4"
            transmit_delay: 45
            bandwidth: 70
            authentication:
              md5_key:
                key_id: 10
                key: "1111111111232345"
          - afi: "ipv6"
            passive: true
    state: rendered

# Module Execution:
# ----------------

#    "rendered": [
#        "set protocols ospf interface eth1 transmit-delay 50",
#        "set protocols ospf interface eth1 priority 26",
#        "set protocols ospf interface eth1 network point-to-point",
#        "set protocols ospfv3 interface eth1 dead-interval 39",
#        "set protocols ospf interface bond2 transmit-delay 45",
#        "set protocols ospf interface bond2 bandwidth 70",
#        "set protocols ospf interface bond2 authentication md5 key-id 10 md5-key 1111111111232345",
#        "set protocols ospfv3 interface bond2 passive"
#    ]
#

# Using Gathered:
# --------------

# Native Config:

# vyos@vyos:~$ show configuration commands | match "ospf"
# set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'
# set protocols ospf interface bond2 bandwidth '70'
# set protocols ospf interface bond2 transmit-delay '45'
# set protocols ospfv3 interface bond2 'passive'
# set protocols ospf interface eth1 network 'point-to-point'
# set protocols ospf interface eth1 priority '26'
# set protocols ospf interface eth1 transmit-delay '50'
# set protocols ospfv3 interface eth1 dead-interval '39'
# vyos@vyos:~$

- name: gather configs
  vyos.vyos.vyos_ospf_interfaces:
    state: gathered

# Module Execution:
# -----------------

#    "gathered": [
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "authentication": {
#                        "md5_key": {
#                            "key": "1111111111232345",
#                            "key_id": 10
#                        }
#                    },
#                    "bandwidth": 70,
#                    "transmit_delay": 45
#                },
#                {
#                    "afi": "ipv6",
#                    "passive": true
#                }
#            ],
#            "name": "bond2"
#        },
#        {
#            "name": "eth0"
#        },
#        {
#            "address_family": [
#                {
#                    "afi": "ipv4",
#                    "network": "point-to-point",
#                    "priority": 26,
#                    "transmit_delay": 50
#                },
#                {
#                    "afi": "ipv6",
#                    "dead_interval": 39
#                }
#            ],
#            "name": "eth1"
#        },
#        {
#            "name": "eth2"
#        },
#        {
#            "name": "eth3"
#        }
#    ],
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
   - "set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'"
   - "set protocols ospf interface bond2 bandwidth '70'"
   - "set protocols ospf interface bond2 transmit-delay '45'"
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
   - "set protocols ospf interface bond2 authentication md5 key-id 10 md5-key '1111111111232345'"
   - "set protocols ospf interface bond2 bandwidth '70'"
   - "set protocols ospf interface bond2 transmit-delay '45'"
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

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.ospf_interfaces.ospf_interfaces import (
    Ospf_interfacesArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospf_interfaces.ospf_interfaces import (
    Ospf_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Ospf_interfacesArgs.argument_spec,
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

    result = Ospf_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
