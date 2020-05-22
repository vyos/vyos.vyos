#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for vyos_ospfv3
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: vyos_ospfv3
short_description: OSPFV3 resource module
description: This resource module configures and manages attributes of OSPFv3 routes
  on VyOS network devices.
version_added: 1.0.0
notes:
- Tested against VyOS 1.1.8 (helium).
- This module works with connection C(network_cli). See L(the VyOS OS Platform Options,../network/user_guide/platform_vyos.html).
author:
- Rohit Thakur (@rohitthakur2590)
options:
  config:
    description: A provided OSPFv3 route configuration.
    type: dict
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
        descriptions: OSPFv3 specific parameters.
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
            choices: [bgp, connected, kernel, ripng, static]
          route_map:
            description: Route map references.
            type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the VyOS device
      by executing the command B(show configuration commands | grep ospfv3).
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
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged

"""
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos# run show  configuration commands | grep ospfv3
#
#
- name: Merge the provided configuration with the exisiting running configuration
  vyos.vyos.vyos_ospfv3:
    config:
      redistribute:
      - route_type: bgp
      parameters:
        router_id: 192.0.2.10
      areas:
      - area_id: '2'
        export_list: export1
        import_list: import1
        range:
        - address: 2001:db10::/32
        - address: 2001:db20::/32
        - address: 2001:db30::/32
      - area_id: '3'
        range:
        - address: 2001:db40::/32
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": {}
#
#    "commands": [
#       "set protocols ospfv3 redistribute bgp",
#       "set protocols ospfv3 parameters router-id '192.0.2.10'",
#       "set protocols ospfv3 area 2 range 2001:db10::/32",
#       "set protocols ospfv3 area 2 range 2001:db20::/32",
#       "set protocols ospfv3 area 2 range 2001:db30::/32",
#       "set protocols ospfv3 area '2'",
#       "set protocols ospfv3 area 2 export-list export1",
#       "set protocols ospfv3 area 2 import-list import1",
#       "set protocols ospfv3 area '3'",
#       "set protocols ospfv3 area 3 range 2001:db40::/32"
#    ]
#
# "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'


# Using replaced
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'
#
- name: Replace ospfv3 routes attributes configuration.
  vyos.vyos.vyos_ospfv3:
    config:
      redistribute:
      - route_type: bgp
      parameters:
        router_id: 192.0.2.10
      areas:
      - area_id: '2'
        export_list: export1
        import_list: import1
        range:
        - address: 2001:db10::/32
        - address: 2001:db30::/32
        - address: 2001:db50::/32
      - area_id: '4'
        range:
        - address: 2001:db60::/32
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# "commands": [
#     "delete protocols ospfv3 area 2 range 2001:db20::/32",
#     "delete protocols ospfv3 area 3",
#     "set protocols ospfv3 area 2 range 2001:db50::/32",
#     "set protocols ospfv3 area '4'",
#     "set protocols ospfv3 area 4 range 2001:db60::/32"
#    ]
#
#    "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    },
#                    {
#                        "address": "2001:db50::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "4",
#                "range": [
#                    {
#                        "address": "2001:db60::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 2 range '2001:db50::/32'
# set protocols ospfv3 area 4 range '2001:db60::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'


# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_ospfv3:
    config:
      redistribute:
      - route_type: bgp
      parameters:
        router_id: 192.0.2.10
      areas:
      - area_id: '2'
        export_list: export1
        import_list: import1
        range:
        - address: 2001:db10::/32
        - address: 2001:db20::/32
        - address: 2001:db30::/32
      - area_id: '3'
        range:
        - address: 2001:db40::/32
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        [
#       "set protocols ospfv3 redistribute bgp",
#       "set protocols ospfv3 parameters router-id '192.0.2.10'",
#       "set protocols ospfv3 area 2 range 2001:db10::/32",
#       "set protocols ospfv3 area 2 range 2001:db20::/32",
#       "set protocols ospfv3 area 2 range 2001:db30::/32",
#       "set protocols ospfv3 area '2'",
#       "set protocols ospfv3 area 2 export-list export1",
#       "set protocols ospfv3 area 2 import-list import1",
#       "set protocols ospfv3 area '3'",
#       "set protocols ospfv3 area 3 range 2001:db40::/32"
#    ]


# Using parsed
#
#
- name: Parse the commands to provide structured configuration.
  vyos.vyos.vyos_ospfv3:
    running_config: set protocols ospfv3 area 2 export-list 'export1' set protocols
      ospfv3 area 2 import-list 'import1' set protocols ospfv3 area 2 range '2001:db10::/32'
      set protocols ospfv3 area 2 range '2001:db20::/32' set protocols ospfv3 area
      2 range '2001:db30::/32' set protocols ospfv3 area 3 range '2001:db40::/32'
      set protocols ospfv3 parameters router-id '192.0.2.10' set protocols ospfv3
      redistribute 'bgp'
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }


# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'
#
- name: Gather ospfv3 routes config with provided configurations
  vyos.vyos.vyos_ospfv3:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'


# Using deleted
#
# Before state
# -------------
#
# vyos@192# run show configuration commands | grep ospfv3
# set protocols ospfv3 area 2 export-list 'export1'
# set protocols ospfv3 area 2 import-list 'import1'
# set protocols ospfv3 area 2 range '2001:db10::/32'
# set protocols ospfv3 area 2 range '2001:db20::/32'
# set protocols ospfv3 area 2 range '2001:db30::/32'
# set protocols ospfv3 area 3 range '2001:db40::/32'
# set protocols ospfv3 parameters router-id '192.0.2.10'
# set protocols ospfv3 redistribute 'bgp'
#
- name: Delete attributes of ospfv3 routes.
  vyos.vyos.vyos_ospfv3:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "export_list": "export1",
#                "import_list": "import1",
#                "range": [
#                    {
#                        "address": "2001:db10::/32"
#                    },
#                    {
#                        "address": "2001:db20::/32"
#                    },
#                    {
#                        "address": "2001:db30::/32"
#                    }
#                ]
#            },
#            {
#                "area_id": "3",
#                "range": [
#                    {
#                        "address": "2001:db40::/32"
#                    }
#                ]
#            }
#        ],
#        "parameters": {
#            "router_id": "192.0.2.10"
#        },
#        "redistribute": [
#            {
#                "route_type": "bgp"
#            }
#        ]
#    }
# "commands": [
#        "delete protocols ospfv3"
#    ]
#
# "after": {}
# After state
# ------------
# vyos@192# run show configuration commands | grep ospfv3


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - "set protocols ospf parameters router-id 192.0.1.1"
    - "set protocols ospfv3 area 2 range '2001:db10::/32'"
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.ospfv3.ospfv3 import (
    Ospfv3Args,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.ospfv3.ospfv3 import (
    Ospfv3,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=Ospfv3Args.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Ospfv3(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
