#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_vpp_acl
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_vpp_acl
version_added: 7.0.0
short_description: VPP dataplane ACL resource module
description:
  - This module manages the access control lists of the accelerated dataplane (VPP) on devices
    running VyOS - IP and MAC ACLs, and their bindings to dataplane interfaces.
author:
  - VyOS community (@vyos)
extends_documentation_fragment:
  - vyos.vyos.vyos
notes:
  - Tested against VyOS 1.5.1.
  - This module works with connection C(network_cli).
  - ACLs can only be bound to interfaces that are part of the dataplane (C(vpp settings interface)).
  - IP and MAC ACLs are handled independently. With I(state=replaced), the listed ACLs and
    interface bindings are replaced as given; with I(state=overridden), ACLs and bindings that
    are not listed are also deleted, bindings before ACLs.
  - When not configured, VyOS uses the protocol C(all) for IP rules and the mask
    C(ff:ff:ff:ff:ff:ff) for MAC rules; the module reports only configured values.
options:
  config:
    description: The VPP dataplane ACL configuration.
    type: dict
    suboptions:
      ip:
        description: IP ACLs and their bindings.
        type: dict
        suboptions:
          acls:
            description: IP ACLs (C(vpp acl ip tag-name)).
            type: list
            elements: dict
            suboptions:
              name:
                description: The ACL name.
                type: str
                required: true
              description:
                description:
                  - The ACL description.
                  - VyOS does not accept the single quote character in values.
                type: str
              rules:
                description: The ACL rules.
                type: list
                elements: dict
                suboptions:
                  number:
                    description: The rule number.
                    type: int
                    required: true
                  action:
                    description: The action for matching packets.
                    type: str
                    choices: ["permit", "deny", "permit-reflect"]
                  description:
                    description: The rule description.
                    type: str
                  protocol:
                    description: The protocol to match, as a name or number, or C(all).
                    type: str
                  source:
                    description: The source to match.
                    type: dict
                    suboptions:
                      prefix:
                        description: The IPv4 or IPv6 source prefix.
                        type: str
                      port:
                        description: The source port or port range, for example C(1024-65535).
                        type: str
                  destination:
                    description: The destination to match.
                    type: dict
                    suboptions:
                      prefix:
                        description: The IPv4 or IPv6 destination prefix.
                        type: str
                      port:
                        description: The destination port or port range.
                        type: str
                  tcp_flags:
                    description: The TCP flags to match.
                    type: dict
                    suboptions:
                      is_set:
                        description: The TCP flags that must be set.
                        type: list
                        elements: str
                        choices: ["ack", "cwr", "ecn", "fin", "psh", "rst", "syn", "urg"]
                      is_not_set:
                        description: The TCP flags that must not be set.
                        type: list
                        elements: str
                        choices: ["ack", "cwr", "ecn", "fin", "psh", "rst", "syn", "urg"]
          interfaces:
            description: The IP ACLs bound to dataplane interfaces.
            type: list
            elements: dict
            suboptions:
              name:
                description: The interface name, for example C(eth1).
                type: str
                required: true
              input:
                description: The ACLs applied to incoming traffic, in the order of I(acl_tag).
                type: list
                elements: dict
                suboptions:
                  acl_tag:
                    description: The position of the ACL in the list.
                    type: int
                    required: true
                  tag_name:
                    description: The name of the IP ACL.
                    type: str
                    required: true
              output:
                description: The ACLs applied to outgoing traffic, in the order of I(acl_tag).
                type: list
                elements: dict
                suboptions:
                  acl_tag:
                    description: The position of the ACL in the list.
                    type: int
                    required: true
                  tag_name:
                    description: The name of the IP ACL.
                    type: str
                    required: true
      mac:
        description: MAC ACLs and their bindings.
        type: dict
        suboptions:
          acls:
            description: MAC ACLs (C(vpp acl mac tag-name)).
            type: list
            elements: dict
            suboptions:
              name:
                description: The ACL name.
                type: str
                required: true
              description:
                description: The ACL description.
                type: str
              rules:
                description: The ACL rules.
                type: list
                elements: dict
                suboptions:
                  number:
                    description: The rule number.
                    type: int
                    required: true
                  action:
                    description: The action for matching packets.
                    type: str
                    choices: ["permit", "deny"]
                  description:
                    description: The rule description.
                    type: str
                  prefix:
                    description: The IPv4 or IPv6 prefix to match.
                    type: str
                  mac_address:
                    description: The MAC address to match.
                    type: str
                  mac_mask:
                    description: The mask applied to I(mac_address).
                    type: str
          interfaces:
            description: The MAC ACLs bound to dataplane interfaces, one per interface.
            type: list
            elements: dict
            suboptions:
              name:
                description: The interface name, for example C(eth1).
                type: str
                required: true
              tag_name:
                description: The name of the MAC ACL.
                type: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VyOS device by
        executing the command B(show configuration commands | grep 'vpp acl').
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
      - rendered
      - parsed
    default: merged
"""

EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep 'vpp acl'
#

- name: Permit HTTPS from partners into eth1
  vyos.vyos.vyos_vpp_acl:
    config:
      ip:
        acls:
          - name: WEB-IN
            description: Inbound web traffic
            rules:
              - number: 10
                action: permit
                protocol: tcp
                source:
                  prefix: 192.0.2.0/24
                destination:
                  prefix: 198.51.100.10/32
                  port: "443"
              - number: 20
                action: deny
        interfaces:
          - name: eth1
            input:
              - acl_tag: 1
                tag_name: WEB-IN
    state: merged

# Task output
# -----------
#
#    commands:
#      - set vpp acl ip tag-name WEB-IN description 'Inbound web traffic'
#      - set vpp acl ip tag-name WEB-IN rule 10 action permit
#      - set vpp acl ip tag-name WEB-IN rule 10 protocol tcp
#      - set vpp acl ip tag-name WEB-IN rule 10 source prefix 192.0.2.0/24
#      - set vpp acl ip tag-name WEB-IN rule 10 destination prefix 198.51.100.10/32
#      - set vpp acl ip tag-name WEB-IN rule 10 destination port 443
#      - set vpp acl ip tag-name WEB-IN rule 20 action deny
#      - set vpp acl ip interface eth1 input acl-tag 1 tag-name WEB-IN

# Using merged, MAC ACL

- name: Permit one vendor's MAC addresses on eth1
  vyos.vyos.vyos_vpp_acl:
    config:
      mac:
        acls:
          - name: MAC-FILTER
            rules:
              - number: 10
                action: permit
                mac_address: 00:11:22:00:00:00
                mac_mask: ff:ff:ff:00:00:00
        interfaces:
          - name: eth1
            tag_name: MAC-FILTER
    state: merged

# Using replaced

# Before state:
# -------------
#
# set vpp acl ip tag-name WEB-IN rule 10 action 'permit'
# set vpp acl ip tag-name WEB-IN rule 10 protocol 'tcp'
# set vpp acl ip tag-name WEB-IN rule 20 action 'deny'

- name: Replace the rules of WEB-IN
  vyos.vyos.vyos_vpp_acl:
    config:
      ip:
        acls:
          - name: WEB-IN
            rules:
              - number: 10
                action: permit
    state: replaced

# Task output
# -----------
#
#    commands:
#      - delete vpp acl ip tag-name WEB-IN rule 10 protocol
#      - delete vpp acl ip tag-name WEB-IN rule 20

# Using overridden

- name: Keep only the WEB-IN ACL and its binding
  vyos.vyos.vyos_vpp_acl:
    config:
      ip:
        acls:
          - name: WEB-IN
            rules:
              - number: 10
                action: permit
        interfaces:
          - name: eth1
            input:
              - acl_tag: 1
                tag_name: WEB-IN
    state: overridden

# Using deleted

- name: Remove the ACL bindings of eth1 and the WEB-IN ACL
  vyos.vyos.vyos_vpp_acl:
    config:
      ip:
        acls:
          - name: WEB-IN
        interfaces:
          - name: eth1
    state: deleted

- name: Delete all dataplane ACL configuration
  vyos.vyos.vyos_vpp_acl:
    state: deleted

# Task output (all ACL configuration)
# -----------------------------------
#
#    commands:
#      - delete vpp acl

# Using gathered

- name: Gather the dataplane ACL configuration
  vyos.vyos.vyos_vpp_acl:
    state: gathered

# Using rendered

- name: Render the commands for a MAC ACL
  vyos.vyos.vyos_vpp_acl:
    config:
      mac:
        acls:
          - name: MAC-FILTER
            rules:
              - number: 10
                action: deny
                mac_address: 00:11:22:33:44:55
    state: rendered

# Task output
# -----------
#
#    rendered:
#      - set vpp acl mac tag-name MAC-FILTER rule 10 action deny
#      - set vpp acl mac tag-name MAC-FILTER rule 10 mac-address 00:11:22:33:44:55

# Using parsed

- name: Parse dataplane ACL configuration from device output
  vyos.vyos.vyos_vpp_acl:
    running_config: |
      set vpp acl ip tag-name WEB-IN rule 10 action 'permit'
      set vpp acl ip tag-name WEB-IN rule 10 tcp-flags is-set 'syn'
    state: parsed

# Task output
# -----------
#
#    parsed:
#      ip:
#        acls:
#          - name: WEB-IN
#            rules:
#              - number: 10
#                action: permit
#                tcp_flags:
#                  is_set:
#                    - syn
"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden) or C(deleted)
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
  returned: when I(state) is C(merged), C(replaced), C(overridden) or C(deleted)
  type: list
  sample:
    - set vpp acl ip tag-name WEB-IN rule 10 action permit
    - set vpp acl ip interface eth1 input acl-tag 1 tag-name WEB-IN
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set vpp acl mac tag-name MAC-FILTER rule 10 action deny
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vpp_acl.vpp_acl import (
    Vpp_aclArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vpp_acl.vpp_acl import (
    Vpp_acl,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Vpp_aclArgs.argument_spec,
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

    result = Vpp_acl(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
