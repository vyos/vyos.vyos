#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_prefix_lists
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: vyos_prefix_lists
short_description: Prefix-Lists resource module for VyOS
description:
  - This module manages prefix-lists configuration on devices running VyOS
version_added: 2.3.1
author: Priyam Sahoo (@priyamsahoo)
notes:
  - Tested against VyOS 1.1.8 (helium)
  - This module works with connection C(network_cli)
options:
  config:
    description: A list of prefix-list options
    type: list
    elements: dict
    suboptions:
      afi:
        description: The Address Family Indicator (AFI) for the prefix-lists
        type: str
        choices: ["ipv4", "ipv6"]
        required: true
      prefix_lists:
        description: A list of prefix-list configurations
        type: list
        elements: dict
        suboptions:
          name:
            description: The name of a defined prefix-list
            type: str
            required: true
          description:
            description: A brief text description for the prefix-list
            type: str
          rules:
            description: Rule configurations for the prefix-list
            type: list
            elements: dict
            suboptions:
              id:
                description: A numeric identifier for the rule
                type: int
                required: true
              description:
                description: A brief text description for the prefix list rule
                type: str
              action:
                description: The action to be taken for packets matching a prefix list rule
                type: str
                choices: ["permit", "deny"]
              ge:
                description: Minimum prefix length to be matched
                type: int
              le:
                description: Maximum prefix list length to be matched
                type: int
              prefix:
                description: IPv4 or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format
                type: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VyOS device
        by executing the command B(show configuration commands | grep prefix-list).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
      - The state the configuration should be left in
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
      - gathered
      - rendered
      - parsed
    default: merged
"""
EXAMPLES = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.prefix_lists.prefix_lists import (
    Prefix_listsArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.prefix_lists.prefix_lists import (
    Prefix_lists,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Prefix_listsArgs.argument_spec,
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

    result = Prefix_lists(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
