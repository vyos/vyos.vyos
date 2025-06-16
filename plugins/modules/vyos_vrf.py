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
                choices:
                - ipv4
                - ipv6
              disable_forwarding:
                default: false
                description: Disable forwarding for this address family
                type: bool
              nht_no_resolve_via_default:
                default: false
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
#   vyos@vyos:~$ show configuration commands | grep ntp
#     set service ntp server time1.vyos.net
#     set service ntp server time2.vyos.net
#     set service ntp server time3.vyos.net
#   vyos@vyos:~$

# # Task
# # -------------
- name: Replace the existing ntp config with the new config
  vyos.vyos.vyos_ntp_global:
    config:
      allow_clients:
        - 10.6.6.0/24
      listen_addresses:
        - 10.1.3.1
      servers:
        - server: 203.0.113.0
          options:
            - prefer


# Task output:
# -------------
#        "after": {
#         "allow_clients": [
#            "10.6.6.0/24"
#        ],
#        "listen_addresses": [
#            "10.1.3.1"
#        ],
#        "servers": [
#            {
#                "server": "ser",
#                "options": [
#                    "prefer"
#                ]
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#        ]
#    },
#    "before": {
#    },
#    "changed": true,
#    "commands": [
#        "set service ntp allow-clients address 10.6.6.0/24",
#        "set service ntp listen-address 10.1.3.1",
#        "set service ntp server 203.0.113.0 prefer"
#    ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.6.6.0/24'
#        set service ntp listen-address '10.1.3.1'
#        set service ntp server 203.0.113.0 prefer,
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$


# # -------------------
# # 2. Using replaced
# # -------------------

# # Before state:
# # -------------
#    vyos@vyos:~$ show configuration commands | grep ntp
#    set service ntp allow-clients address '10.4.9.0/24'
#    set service ntp allow-clients address '10.4.7.0/24'
#    set service ntp allow-clients address '10.1.2.0/24'
#    set service ntp allow-clients address '10.2.3.0/24'
#    set service ntp listen-address '10.1.9.16'
#    set service ntp listen-address '10.5.3.2'
#    set service ntp listen-address '10.7.9.21'
#    set service ntp listen-address '10.8.9.4'
#    set service ntp listen-address '10.4.5.1'
#    set service ntp server 10.3.6.5 noselect
#    set service ntp server 10.3.6.5 dynamic
#    set service ntp server 10.3.6.5 preempt
#    set service ntp server 10.3.6.5 prefer
#    set service ntp server server4 noselect
#    set service ntp server server4 dynamic
#    set service ntp server server5
#    set service ntp server time1.vyos.net
#    set service ntp server time2.vyos.net
#    set service ntp server time3.vyos.net
#    vyos@vyos:~$

# # Task
# # -------------
- name: Replace the existing ntp config with the new config
  vyos.vyos.vyos_ntp_global:
    config:
      allow_clients:
        - 10.6.6.0/24
      listen_addresses:
        - 10.1.3.1
      servers:
        - server: 203.0.113.0
          options:
            - prefer
    state: replaced


# # Task output:
# # -------------
#        "after": {
#         "allow_clients": [
#            "10.6.6.0/24"
#        ],
#        "listen_addresses": [
#            "10.1.3.1"
#        ],
#        "servers": [
#            {
#                "server": "ser",
#                "options": [
#                    "prefer"
#                ]
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#        ]
#    },
#    "before": {
#        "allow_clients": [
#            "10.4.7.0/24",
#            "10.2.3.0/24",
#            "10.1.2.0/24",
#            "10.4.9.0/24"
#        ],
#        "listen_addresses": [
#            "10.7.9.21",
#            "10.4.5.1",
#            "10.5.3.2",
#            "10.8.9.4",
#            "10.1.9.16"
#        ],
#        "servers": [
#            {
#                "server": "10.3.6.5",
#                "options": [
#                    "noselect",
#                    "dynamic",
#                    "preempt",
#                    "prefer"
#                ]
#            },
#            {
#                "server": "server4",
#                "options": [
#                    "noselect",
#                    "dynamic"
#                ]
#            },
#            {
#                "server": "server5"
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#        ]
#    },
#    "changed": true,
#    "commands": [
#        "delete service ntp allow-clients address 10.4.7.0/24",
#        "delete service ntp allow-clients address 10.2.3.0/24",
#        "delete service ntp allow-clients address 10.1.2.0/24",
#        "delete service ntp allow-clients address 10.4.9.0/24",
#        "delete service ntp listen-address 10.7.9.21",
#        "delete service ntp listen-address 10.4.5.1",
#        "delete service ntp listen-address 10.5.3.2",
#        "delete service ntp listen-address 10.8.9.4",
#        "delete service ntp listen-address 10.1.9.16",
#        "delete service ntp server 10.3.6.5",
#        "delete service ntp server server4",
#        "delete service ntp server server5",
#        "set service ntp allow-clients address 10.6.6.0/24",
#        "set service ntp listen-address 10.1.3.1",
#        "set service ntp server 203.0.113.0 prefer"
#    ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.6.6.0/24'
#        set service ntp listen-address '10.1.3.1'
#        set service ntp server 203.0.113.0 prefer,
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$

# # -------------------
# # 3. Using overridden
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.6.6.0/24'
#        set service ntp listen-address '10.1.3.1'
#        set service ntp server 203.0.113.0 prefer,
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$

# Task
# -------------
- name: Override ntp config
  vyos.vyos.vyos_ntp_global:
    config:
      allow_clients:
        - 10.3.3.0/24
      listen_addresses:
        - 10.7.8.1
      servers:
        - server: server1
          options:
            - dynamic
            - prefer

        - server: server2
          options:
            - noselect
            - preempt

        - server: serv
    state: overridden

# # Task output:
# # -------------
#            "after": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                "server": "serv"
#            },
#            {
#                "server": "server1",
#                "options": [
#                    "dynamic",
#                    "prefer"
#                ]
#            },
#            {
#                "server": "server2",
#                "options": [
#                    "noselect",
#                    "preempt"
#                ]
#            },
#            {
#                "server": "time1.vyos.net"
#            },
#            {
#                "server": "time2.vyos.net"
#            },
#            {
#                "server": "time3.vyos.net"
#            }
#                ]
#            },
#            "before": {
#                "allow_clients": [
#                    "10.6.6.0/24"
#                ],
#                "listen_addresses": [
#                    "10.1.3.1"
#                ],
#                "servers": [
#                    {
#                        "server": "ser",
#                        "options": [
#                            "prefer"
#                        ]
#                    },
#                    {
#                        "server": "time1.vyos.net"
#                    },
#                    {
#                        "server": "time2.vyos.net"
#                    },
#                    {
#                        "server": "time3.vyos.net"
#                    }
#                ]
#            },
#            "changed": true,
#            "commands": [
#                "delete service ntp allow-clients address 10.6.6.0/24",
#                "delete service ntp listen-address 10.1.3.1",
#                "delete service ntp server ser",
#                "set service ntp allow-clients address 10.3.3.0/24",
#                "set service ntp listen-address 10.7.8.1",
#                "set service ntp server server1 dynamic",
#                "set service ntp server server1 prefer",
#                "set service ntp server server2 noselect",
#                "set service ntp server server2 preempt",
#                "set service ntp server serv"
#            ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.3.3.0/24'
#        set service ntp listen-address '10.7.8.1'
#        set service ntp server serv
#        set service ntp server server1 dynamic
#        set service ntp server server1 prefer
#        set service ntp server server2 noselect
#        set service ntp server server2 preempt
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$

# 4. Using gathered
# -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.3.3.0/24'
#        set service ntp listen-address '10.7.8.1'
#        set service ntp server serv
#        set service ntp server server1 dynamic
#        set service ntp server server1 prefer
#        set service ntp server server2 noselect
#        set service ntp server server2 preempt
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$

# Task
# -------------
- name: Gather ntp config
  vyos.vyos.vyos_ntp_global:
    state: gathered

# # Task output:
# # -------------
#        "gathered": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                        "server": "serv"
#                    },
#                    {
#                        "server": "server1",
#                        "options": [
#                            "dynamic",
#                            "prefer"
#                        ]
#                    },
#                    {
#                         "server": "server2",
#                         "options": [
#                             "noselect",
#                             "preempt"
#                         ]
#                     },
#                     {
#                          "server": "time1.vyos.net"
#                     },
#                     {
#                         "server": "time2.vyos.net"
#                     },
#                     {
#                         "server": "time3.vyos.net"
#                     }
#                ]
#            }

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.3.3.0/24'
#        set service ntp listen-address '10.7.8.1'
#        set service ntp server serv
#        set service ntp server server1 dynamic
#        set service ntp server server1 prefer
#        set service ntp server server2 noselect
#        set service ntp server server2 preempt
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$


# # -------------------
# # 5. Using deleted
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp allow-clients address '10.3.3.0/24'
#        set service ntp listen-address '10.7.8.1'
#        set service ntp server serv
#        set service ntp server server1 dynamic
#        set service ntp server server1 prefer
#        set service ntp server server2 noselect
#        set service ntp server server2 preempt
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$

# # Task
# # -------------
- name: Delete ntp config
  vyos.vyos.vyos_ntp_global:
    state: deleted


# # Task output:
# # -------------
#            "after": {
#                "servers": [
#                    {
#                        "server": "time1.vyos.net"
#                    },
#                    {
#                       "server": "time2.vyos.net"
#                    },
#                    {
#                        "server": "time3.vyos.net"
#                    }
#                ]
#            },
#            "before": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                        "server": "serv"
#                    },
#                    {
#                        "server": "server1",
#                        "options": [
#                            "dynamic",
#                            "prefer"
#                        ]
#                    },
#                    {
#                          "server": "server2",
#                          "options": [
#                              "noselect",
#                              "preempt"
#                          ]
#                      },
#                      {
#                          "server": "time1.vyos.net"
#                      },
#                      {
#                          "server": "time2.vyos.net"
#                      },
#                      {
#                          "server": "time3.vyos.net"
#                      }
#                ]
#            },
#            "changed": true,
#            "commands": [
#                "delete service ntp allow-clients",
#                "delete service ntp listen-address",
#                "delete service ntp server serv",
#                "delete service ntp server server1",
#                "delete service ntp server server2"
#
#            ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$


# # -------------------
# # 6. Using rendered
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set service ntp server time1.vyos.net
#        set service ntp server time2.vyos.net
#        set service ntp server time3.vyos.net
#        vyos@vyos:~$

# Task
# -------------
- name: Render ntp config
  vyos.vyos.vyos_ntp_global:
    config:
      allow_clients:
        - 10.7.7.0/24
        - 10.8.8.0/24
      listen_addresses:
        - 10.7.9.1
      servers:
        - server: server7
        - server: server45
          options:
            - noselect
            - prefer
            - pool
        - server: time1.vyos.net
        - server: time2.vyos.net
        - server: time3.vyos.net
      state: rendered

# # Task output:
# # -------------
#           "rendered": [
#                "set service ntp allow-clients address 10.7.7.0/24",
#                "set service ntp allow-clients address 10.8.8.0/24",
#                "set service ntp listen-address 10.7.9.1",
#                "set service ntp server server7",
#                "set service ntp server server45 noselect",
#                "set service ntp server server45 prefer",
#                "set service ntp server server45 pool",
#                "set service ntp server time1.vyos.net",
#                "set service ntp server time2.vyos.net",
#                "set service ntp server time3.vyos.net"
#            ]


# # -------------------
# # 7. Using parsed
# # -------------------

# # sample_config.cfg:
# # -------------
#           "set service ntp allow-clients address 10.7.7.0/24",
#           "set service ntp listen-address 10.7.9.1",
#           "set service ntp server server45 noselect",
#           "set service ntp allow-clients addres 10.8.6.0/24",
#           "set service ntp listen-address 10.5.4.1",
#           "set service ntp server server45 dynamic",
#           "set service ntp server time1.vyos.net",
#           "set service ntp server time2.vyos.net",
#           "set service ntp server time3.vyos.net"

# Task:
# -------------
- name: Parse externally provided ntp configuration
  vyos.vyos.vyos_ntp_global:
    running_config: "{{ lookup('file', './sample_config.cfg') }}"
    state: parsed

# # Task output:
# # -------------
#           parsed = {
#                "allow_clients": [
#                    "10.7.7.0/24",
#                    "10.8.6.0/24
#                ],
#                "listen_addresses": [
#                    "10.5.4.1",
#                    "10.7.9.1"
#                ],
#                "servers": [
#                    {
#                        "server": "server45",
#                        "options": [
#                            "noselect",
#                            "dynamic"
#
#                        ]
#                    },
#                    {
#                        "server": "time1.vyos.net"
#                    },
#                    {
#                        "server": "time2.vyos.net"
#                    },
#                    {
#                        "server": "time3.vyos.net"
#                    }
#
#                ]
#            }
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
