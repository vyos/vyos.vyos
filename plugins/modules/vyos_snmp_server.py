#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_snmp_server
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: vyos_snmp_serve
version_added: 2.7.0
short_description: Manages snmp_server resource module
description: This module manages the snmp server attributes of Vyos network devices
author: Gomathi Selvi Srinivasan (@GomathiselviS)
notes:
  - Tested against vyos 1.1.8
  - This module works with connection C(network_cli).
  - The Configuration defaults of the Vyos network devices
    are supposed to hinder idempotent behavior of plays
options:
  config:
    description: SNMP server configuration.
    type: dict
    suboptions:
      communities:
        description: Community name configuration.
        type: list
        elements: dict
        suboptions:
          name:
            description: Community name
            type: str
          client:
            description: IP address of SNMP client allowed to contact system
            type: str
          network:
            description: Subnet of SNMP client(s) allowed to contact system
            type: str
          authorization_type:
            description: Authorization type (rw or ro)
            type: str
            choices: ['ro', 'rw']
      contact:
        description: Person to contact about the system.
        type: str
      description:
        description: Description information
        type: str
      listen_address:
        description: IP address to listen for incoming SNMP requests
        type: dict
        suboptions:
          address:
            description: IP address to listen for incoming SNMP requests.
            type: str
          port:
            description: Port for SNMP service
            type: int
      location:
        description: Location information
        type: str
      smux_peer:
        description: Register a subtree for SMUX-based processing.
        type: str
      trap_source:
        description:  SNMP trap source address
        type: str
      trap_target:
        description: Address of trap target
        type: dict
        suboptions:
          address:
            description: Address of trap target
            type: str
          community:
            description: Community used when sending trap information
            type: str
          port:
            description: Destination port used for trap notification
            type: int
      snmp_v3:
        description: Simple Network Management Protocol (SNMP) v3
        type: dict
        suboptions:
          engine_id:
            description: Specifies the EngineID as a hex value
            type: str
          groups:
            description: Specifies the group with name groupname
            type: list
            elements: dict
            suboptions:
              group:
                description: Specifies the group with name groupname
                type: str
              mode:
                description: Defines the read/write access
                type: str
                choices: ['ro', 'rw']
              seclevel:
                description: Defines security level
                type: str
                choices: ['auth', 'priv']
              view:
                description: Defines the name of view
                type: str
          trap_targets:
            description: Defines SNMP target for inform or traps for IP
            type: list
            elements: dict
            suboptions:
              address:
                description: IP/IPv6 address of trap target
                type: str
              authentication:
                description: Defines the authentication
                type: dict
                suboptions:
                  type:
                    description: Defines the protocol using for authentication
                    type: str
                    choices: ['md5', 'sha']
                  encrypted_key:
                    description: Defines the encrypted password for authentication
                    type: str
                  plaintext_key:
                    description: Defines the clear text password for authentication
                    type: str
              engine_id:
                description: Defines the engineID.
                type: str
              port:
                description: Specifies the TCP/UDP port of a destination for SNMP traps/informs.
                type: int
              privacy:
                description: Defines the privacy
                type: dict
                suboptions:
                  type:
                    description: Defines the protocol using for privacy
                    type: str
                    choices: ['des', 'aes']
                  encrypted_key:
                    description: Defines the encrypted password for privacy
                    type: str
                  plaintext_key:
                    description: Defines the clear text password for privacy
                    type: str
              protocol:
                description: Defines protocol for notification between TCP and UDP
                type: str
                choices: ['tcp', 'udp']
              type:
                description: Specifies the type of notification between inform and trap
                type: str
                choices: ['inform', 'trap']
          tsm:
            description: Specifies that the snmpd uses encryption
            type: dict
            suboptions:
              local_key:
                description: Defines the server certificate fingerprint or key-file name.
                type: str
              port:
                description: Defines the port for tsm.
                type: int
          users:
            description: Defines username for authentication
            type: list
            elements: dict
            suboptions:
              user:
                description: Specifies the user with name username
                type: str
              authentication:
                description: Defines the authentication
                type: dict
                suboptions:
                  type:
                    description: Defines the protocol using for authentication
                    type: str
                    choices: ['md5', 'sha']
                  encrypted_key:
                    description: Defines the encrypted password for authentication
                    type: str
                  plaintext_key:
                    description: Defines the clear text password for authentication
                    type: str
              engine_id:
                description: Defines the engineID.
                type: str
              group:
                description: Specifies group for user name
                type: str
              mode:
                description: Specifies the mode for access rights of user, read only or write
                type: str
                choices: ['ro', 'rw']
              privacy:
                description: Defines the privacy
                type: dict
                suboptions:
                  type:
                    description: Defines the protocol using for privacy
                    type: str
                    choices: ['des', 'aes']
              tsm_key:
                description: Specifies finger print or file name of TSM certificate.
                type: str
          views:
            desscription: Specifies the view with name viewname
            type: list
            elements: dict
            suboptions:
              view:
                description: view name
                type: str
              oid:
                description: Specify oid
                type: str
              exclude:
                description: Exclude is optional argument.
                type: bool
              mask:
                description: Defines a bit-mask that is indicating which subidentifiers of the associated subtree OID should be regarded as significant.
                type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the vyos device by
      executing the command B("show configuration commands | grep snmp").
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
"""

EXAMPLES = """

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
    - sample command 1
    - sample command 2
    - sample command 3
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
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
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.snmp_server.snmp_server import (
    Snmp_serverArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.snmp_server.snmp_server import (
    Snmp_server,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Snmp_serverArgs.argument_spec,
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

    result = Snmp_server(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
