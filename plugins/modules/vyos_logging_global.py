#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_logging_global
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: vyos_logging_global
version_added: 2.4.0
short_description: Manages logging attributes of Vyos network devices
description: This module manages the logging attributes of Vyos network devices
author: Sagar Paul (@KB-perByte)
notes:
  - Tested against vyos 1.2
  - This module works with connection C(network_cli).
  - The Configuration defaults of the Vyos network devices
    are supposed to hinder idempotent behavior of plays
options:
  config:
    description: A list containing dictionary of logging options
    type: dict
    suboptions:
      console_params:
        description: logging to serial console
        type: list
        elements: dict
        suboptions:
          facility: &facility
            description: Facility for logging
            type: str
            choices:
              - all
              - auth
              - authpriv
              - cron
              - daemon
              - kern
              - lpr
              - mail
              - mark
              - news
              - protocols
              - security
              - syslog
              - user
              - uucp
              - local0
              - local1
              - local2
              - local3
              - local4
              - local5
              - local6
              - local7
          level: &level
            description: logging level
            type: str
            choices:
              - emerg
              - alert
              - crit
              - err
              - warning
              - notice
              - info
              - debug
              - all
      files:
        description: logging to file
        type: list
        elements: dict
        suboptions:
          path:
            description: file name or path
            type: str
          archive: &archive
            description: Log file size and rotation characteristics
            type: dict
            suboptions:
              file_num:
                description: Number of saved files (default is 5)
                type: str
              size:
                description: Size of log files (in kilobytes, default is 256)
                type: str
          params: &params
            description: List of supported params
            type: list
            elements: dict
            suboptions:
              facility: *facility
              level: *level
      global_params:
        description: logging to serial console
        elements: dict
        suboptions:
          archive: *archive
          params: *params
          marker_interval:
            description: time interval how often a mark message is being sent in seconds (default is 1200)
            type: str
          preserve_fqdn:
            description: uses FQDN for logging
            type: bool
      hosts:
        description: logging to serial console
        type: list
        elements: dict
        suboptions:
          port:
            description: Destination port (1-65535)
            type: str
          params:
            description: List of supported params
            type: list
            elements: dict
            suboptions:
              facility: *facility
              level: *level
              protocol:
                description: syslog communication protocol
                type: str
                choices:
                  - udp
                  - tcp
          hostname:
            description: Remote host name or IP address
            type: str
      users:
        description: logging to file
        type: list
        elements: dict
        suboptions:
          username:
            description: user login name
            type: str
          params: *params
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VYOS device by
        executing the command B(show configuration commands | grep syslog).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices:
      - merged
      - replaced
      - overridden
      - deleted
      - gathered
      - parsed
      - rendered
    default: merged
    description:
      - The state the configuration should be left in
    type: str
required_if:
  - ["state", "merged", ["config"]]
  - ["state", "replaced", ["config"]]
  - ["state", "overridden", ["config"]]
  - ["state", "rendered", ["config"]]
  - ["state", "parsed", ["running_config"]]
mutually_exclusive:
  - ["config", "running_config"]
supports_check_mode: True
"""
EXAMPLES = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.logging_global.logging_global import (
    Logging_globalArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.logging_global.logging_global import (
    Logging_global,
)

# import debugpy

# debugpy.listen(3001)
# debugpy.wait_for_client()


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Logging_globalArgs.argument_spec,
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

    result = Logging_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
