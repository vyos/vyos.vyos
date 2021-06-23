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
  description: This module manages ntp configuration on devices running Vyos
  author: Varshitha Yataluru (@YVarshitha)
  options:
    config:
        description: List of configurations for ntp module
        type: list
        elements: dict
        suboptions:
            allow_clients:
                description: Network Time Protocol (NTP) server options
                type: dict
                suboptions:
                    address:
                        description: IP address
                        type: list
                        choices:
                            - Ip
                            - IPv6
            listen_address:
                description: local IP addresses for service to listen on
                type: str
                choices:
                    - Ip
                    - IPv6
            server:
                description: Network Time Protocol (NTP) server
                type: dict
                suboptions:
                    server_name:
                        description: server options for NTP
                        type: dict
                        suboptions:
                            server_options:
                                description: server options for NTP
                                type: list
                                choices:
                                    - noselect
                                    - pool
                                    - preempt
                                    - prefer
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
