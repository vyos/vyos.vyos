#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_ntp
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
  module: vyos_ntp
  version added: 2.4.0
  short_description:  Manages ntp modules of Vyos network devices
  description: 
  - This module manages ntp configuration on devices running Vyos
  author: Varshitha Yataluru (@YVarshitha)
  notes:
  - Tested against vyos 1.3
  - This module works with connection C(network_cli).
  options:
    config:
        description: List of configurations for ntp module
        type: dict
        suboptions:
            allow_clients:
                description: Network Time Protocol (NTP) server options
                type: list
                elements: str
            listen_addresses:
                description: local IP addresses for service to listen on
                type: list
                elements: str
            servers:
                description: Network Time Protocol (NTP) server
                type: list
                elements: dict
                suboptions:
                    name:
                        description: server name for NTP
                        type: str
                    options:
                        description: server options for NTP
                        type: list
                        elements: str
                        choices:
                            - noselect
                            - pool
                            - preempt
                            - prefer
    running_config:
        description:
        - This option is used only with state I(parsed).
        - The value of this option should be the output received from the VYOS device by
          executing the command B(show configuration commands | grep ntp).
        - The state I(parsed) reads the configuration from C(show configuration commands | grep ntp) option and
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
#   vyos@vyos:~$

# # Task
# # -------------
#            - name: Merge the provided configuration for the existing ntp config
#            vyos.vyos.vyos_ntp:
#                config:
#                allow_clients:
#                - 10.2.3.0/24
#                - 10.4.7.0/24
#                - 10.1.2.0/24
#                - 10.4.9.0/24
#                listen_addresses:
#                - 10.4.5.1
#                - 10.7.9.21
#                - 10.1.9.16
#                - 10.8.9.4
#                - 10.5.3.2
#                servers:
#                - name: server5
#
#                - name: server4
#                    options:
#                    - noselect
#                    - pool
#
#                - name: 10.3.6.5
#                    options:
#                    - noselect
#                    - preempt
#                    - pool
#                    - prefer
#
#                state: merged


# # Task output:
# # -------------
#    "after": {
#        "allow_clients": [
#            "10.4.9.0/24",
#            "10.1.2.0/24",
#            "10.4.7.0/24",
#            "10.2.3.0/24"
#        ],
#        "listen_addresses": [
#            "10.8.9.4",
#            "10.5.3.2",
#            "10.7.9.21",
#            "10.4.5.1",
#            "10.1.9.16"
#        ],
#        "servers": [
#            {
#                "name": "10.3.6.5",
#                "options": [
#                    "prefer",
#                    "preempt",
#                    "pool",
#                    "noselect"
#                ]
#            },
#            {
#                "name": "server4",
#                "options": [
#                    "pool",
#                    "noselect"
#                ]
#            },
#            {
#                "name": "server5"
#            }
#        ]
#    },
#    "before": {},
#    "changed": true,
#    "commands": [
#        "set system ntp allow-clients address 10.4.9.0/24",
#        "set system ntp server server4 pool",
#        "set system ntp listen-address 10.1.9.16",
#        "set system ntp allow-clients address 10.4.7.0/24",
#        "set system ntp listen-address 10.5.3.2",
#        "set system ntp server server5",
#        "set system ntp server 10.3.6.5 noselect",
#        "set system ntp server 10.3.6.5 pool",
#        "set system ntp listen-address 10.7.9.21",
#        "set system ntp server 10.3.6.5 preempt",
#        "set system ntp allow-clients address 10.1.2.0/24",
#        "set system ntp server server4 noselect",
#        "set system ntp allow-clients address 10.2.3.0/24",
#        "set system ntp listen-address 10.8.9.4",
#        "set system ntp listen-address 10.4.5.1",
#        "set system ntp server 10.3.6.5 prefer"
#    ]

# After state:
# # -------------
#    vyos@vyos:~$ show configuration commands | grep ntp
#    set system ntp allow-clients address '10.4.9.0/24'
#    set system ntp allow-clients address '10.4.7.0/24'
#    set system ntp allow-clients address '10.1.2.0/24'
#    set system ntp allow-clients address '10.2.3.0/24'
#    set system ntp listen-address '10.1.9.16'
#    set system ntp listen-address '10.5.3.2'
#    set system ntp listen-address '10.7.9.21'
#    set system ntp listen-address '10.8.9.4'
#    set system ntp listen-address '10.4.5.1'
#    set system ntp server 10.3.6.5 noselect
#    set system ntp server 10.3.6.5 pool
#    set system ntp server 10.3.6.5 preempt
#    set system ntp server 10.3.6.5 prefer
#    set system ntp server server4 noselect
#    set system ntp server server4 pool
#    set system ntp server server5
#    vyos@vyos:~$



# # -------------------
# # 2. Using replaced
# # -------------------

# # Before state:
# # -------------
#    vyos@vyos:~$ show configuration commands | grep ntp
#    set system ntp allow-clients address '10.4.9.0/24'
#    set system ntp allow-clients address '10.4.7.0/24'
#    set system ntp allow-clients address '10.1.2.0/24'
#    set system ntp allow-clients address '10.2.3.0/24'
#    set system ntp listen-address '10.1.9.16'
#    set system ntp listen-address '10.5.3.2'
#    set system ntp listen-address '10.7.9.21'
#    set system ntp listen-address '10.8.9.4'
#    set system ntp listen-address '10.4.5.1'
#    set system ntp server 10.3.6.5 noselect
#    set system ntp server 10.3.6.5 pool
#    set system ntp server 10.3.6.5 preempt
#    set system ntp server 10.3.6.5 prefer
#    set system ntp server server4 noselect
#    set system ntp server server4 pool
#    set system ntp server server5
#    vyos@vyos:~$

# # Task
# # -------------
#        - name: Replace the existing ntp config with the new config
#            vyos.vyos.vyos_ntp:
#                config:
#                allow_clients:
#                    - 10.6.6.0/24
#                listen_addresses:
#                    - 10.1.3.1
#                servers:
#                    - name: ser
#                    options:
#                        - prefer
#                state: replaced


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
#                "name": "ser",
#                "options": [
#                    "prefer"
#                ]
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
#                "name": "10.3.6.5",
#                "options": [
#                    "pool",
#                    "noselect",
#                    "preempt",
#                    "prefer"
#                ]
#            },
#            {
#                "name": "server4",
#                "options": [
#                    "pool",
#                    "noselect"
#                ]
#            },
#            {
#                "name": "server5"
#            }
#        ]
#    },
#    "changed": true,
#    "commands": [
#        "delete system ntp allow-clients address 10.4.7.0/24",
#        "delete system ntp allow-clients address 10.2.3.0/24",
#        "delete system ntp allow-clients address 10.1.2.0/24",
#        "delete system ntp allow-clients address 10.4.9.0/24",
#        "delete system ntp listen-address 10.7.9.21",
#        "delete system ntp listen-address 10.4.5.1",
#        "delete system ntp listen-address 10.5.3.2",
#        "delete system ntp listen-address 10.8.9.4",
#        "delete system ntp listen-address 10.1.9.16",
#        "delete system ntp server 10.3.6.5",
#        "delete system ntp server server4",
#        "delete system ntp server server5",
#        "set system ntp allow-clients address 10.6.6.0/24",
#        "set system ntp listen-address 10.1.3.1",
#        "set system ntp server ser prefer"
#    ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.6.6.0/24'
#        set system ntp listen-address '10.1.3.1'
#        set system ntp server ser prefer
#        vyos@vyos:~$



# # -------------------
# # 3. Using overridden
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.6.6.0/24'
#        set system ntp listen-address '10.1.3.1'
#        set system ntp server ser prefer
#        vyos@vyos:~$

# # Task
# # -------------
#        - name: Gather ntp config
#            vyos.vyos.vyos_ntp:
#                config:
#                allow_clients:
#                - 10.3.3.0/24
#                listen_addresses:
#                - 10.7.8.1
#                servers:
#                - name: server1
#                    options:
#                    - pool
#                    - prefer
#
#                - name: server2
#                    options:
#                    - noselect
#                    - preempt
#
#                - name: serv
#                state: overridden



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
#                        "name": "serv"
#                    },
#                    {
#                        "name": "server1",
#                        "options": [
#                            "prefer",
#                            "pool"
#                        ]
#                    },
#                    {
#                        "name": "server2",
#                        "options": [
#                            "preempt",
#                            "noselect"
#                        ]
#                    }
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
#                        "name": "ser",
#                        "options": [
#                            "prefer"
#                        ]
#                    }
#                ]
#            },
#            "changed": true,
#            "commands": [
#                "delete system ntp allow-clients address 10.6.6.0/24",
#                "delete system ntp listen-address 10.1.3.1",
#                "delete system ntp server ser",
#                "set system ntp allow-clients address 10.3.3.0/24",
#                "set system ntp listen-address 10.7.8.1",
#                "set system ntp server server1 pool",
#                "set system ntp server server1 prefer",
#                "set system ntp server server2 noselect",
#                "set system ntp server server2 preempt",
#                "set system ntp server serv"
#            ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 pool
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        vyos@vyos:~$ 



# # -------------------
# # 4. Using gathered
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 pool
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        vyos@vyos:~$ 

# # Task
# # -------------
#        - name: Gather ntp config
#            vyos.vyos.vyos_ntp:
#                config:
#                state: gathered

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
#                        "name": "serv"
#                    },
#                    {
#                        "name": "server1",
#                        "options": [
#                            "pool",
#                            "prefer"
#                        ]
#                    },
#                    {
#                        "name": "server2",
#                        "options": [
#                            "preempt",
#                            "noselect"
#                        ]
#                    }
#                ]
#            }

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 pool
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        vyos@vyos:~$ 


# # -------------------
# # 5. Using deleted
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp allow-clients address '10.3.3.0/24'
#        set system ntp listen-address '10.7.8.1'
#        set system ntp server serv
#        set system ntp server server1 pool
#        set system ntp server server1 prefer
#        set system ntp server server2 noselect
#        set system ntp server server2 preempt
#        vyos@vyos:~$ 

# # Task
# # -------------
  - name: Gather ntp config
      vyos.vyos.vyos_ntp:
        config:
          allow_clients:
            - 10.7.7.0/24
            - 10.8.8.0/24
          listen_addresses:
            - 10.7.9.1
          servers:
            - name: server7

            - name: server45
              options:
                - noselect
                - prefer

        state: rendered


# # Task output:
# # -------------
#            "after": {},
#            "before": {
#                "allow_clients": [
#                    "10.3.3.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.8.1"
#                ],
#                "servers": [
#                    {
#                        "name": "serv"
#                    },
#                    {
#                        "name": "server1",
#                        "options": [
#                            "pool",
#                            "prefer"
#                        ]
#                    },
#                    {
#                        "name": "server2",
#                        "options": [
#                            "preempt",
#                            "noselect"
#                        ]
#                    }
#                ]
#            },
#            "changed": true,
#            "commands": [
#                "delete system ntp allow-clients",
#                "delete system ntp listen-address",
#                "delete system ntp server"
#            ]

# After state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp
#        vyos@vyos:~$ 




# # -------------------
# # 6. Using rendered
# # -------------------

# # Before state:
# # -------------
#        vyos@vyos:~$ show configuration commands | grep ntp
#        set system ntp
#        vyos@vyos:~$

# # Task
# # -------------
#        - name: Gather ntp config
#            vyos.vyos.vyos_ntp:
#                config:
#                allow_clients:
#                    - 10.7.7.0/24
#                    - 10.8.8.0/24
#                listen_addresses:
#                    - 10.7.9.1
#                servers:
#                    - name: server7
#
#                    - name: server45
#                    options:
#                        - noselect
#                        - prefer
#
#                state: rendered


# # Task output:
# # -------------
#           "rendered": [
#                "set system ntp allow-clients address 10.7.7.0/24",
#                "set system ntp allow-clients address 10.8.8.0/24",
#                "set system ntp listen-address 10.7.9.1",
#                "set system ntp server server7",
#                "set system ntp server server45 noselect",
#                "set system ntp server server45 prefer"
#            ]


# # -------------------
# # 7. Using parsed
# # -------------------

# # sample_config.cfg:
# # -------------
#           "set system ntp allow-clients address 10.7.7.0/24",
#           "set system ntp listen-address 10.7.9.1",
#           "set system ntp server server45 noselect"
# # Task:
# # -------------
#     - name: Parse externally provided ntp configuration
#       vyos.vyos.vyos_ntp:
#         running_config: "{{ lookup('file', './sample_config.cfg') }}"
#         state: parsed

# # Task output:
# # -------------
#           parsed = {
#                "allow_clients": [
#                    "10.7.7.0/24"
#                ],
#                "listen_addresses": [
#                    "10.7.9.1"
#                ],
#                "servers": [
#                    {
#                        "name": "server46",
#                        "options": [
#                            "noselect"
#                                                      
#                        ]
#                    }
#                ]
#            }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.ntp.ntp import (
    NtpArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ntp.ntp import (
    Ntp,
)



def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=NtpArgs.argument_spec,
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

    result = Ntp(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
