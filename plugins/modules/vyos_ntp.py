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
