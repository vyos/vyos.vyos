#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_nat
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_nat
version_added: 1.0.0
short_description: NAT resource module
description:
- This module manages NAT configuration on devices running Vyos
author:
- Evgeny Molotkov (@omnom62)
notes:
- Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025
- This module works with connection C(network_cli).
options:
  config:
    description:
      - The desired configuration for the NAT resource represented as a dictionary.
    type: dict
    suboptions:
      nat:
        type: dict
        description: Configuration for NAT rules.
        suboptions:
        cgnat:
          type: dict
          description: Configuration for Carrier Grade NAT (CGNAT).
          suboptions:
            log_allocation:
              type: bool
              description: Whether to log CGNAT address allocations.
            pool:
              type: dict
              description: Configuration for CGNAT pools.
              suboptions:
                external:
                  type: list
                  elements: dict
                  description: List of external NAT pools for CGNAT.
                  suboptions:
                    name:
                      type: str
                      required: true
                      description: Name of the external NAT pool.
                    external_port_range:
                      type: str
                      description: Port range to use for NAT translations in this external pool.
                    per_user_limit:
                      type: dict
                      description: Per-user limit configuration for the external pool.
                      suboptions:
                        port:
                          type: int
                          description: Maximum number of ports allocated per user.
                    range:
                      type: list
                      elements: str
                      description: List of external IP addresses or prefixes in the pool.
                internal:
                  type: list
                  elements: dict
                  description: List of internal NAT pools for CGNAT.
                  suboptions:
                    name:
                      type: str
                      required: true
                      description: Name of the internal NAT pool.
                    range:
                      type: list
                      elements: str
                      description: List of internal IP addresses or prefixes in the pool.
            rule:
              type: list
              elements: dict
              description: List of CGNAT rules.
              suboptions:
                id:
                  type: int
                  required: true
                  description: Rule number for CGNAT.
                source:
                  type: dict
                  description: Source configuration for CGNAT translation.
                  suboptions:
                    pool:
                      type: str
                      description: Source pool to use for CGNAT translation.
                translation:
                  type: dict
                  description: Translation configuration for CGNAT.
                  suboptions:
                    pool:
                      type: str
                      description: Translation pool to use for CGNAT translation.
        destination:
          type: dict
          description: Configuration for destination NAT rules.
          suboptions:
            rule:
              type: list
              elements: dict
              description: List of destination NAT rules.
              suboptions:
                id:
                  type: int
                  required: true
                  description: Rule number for destination NAT.
                description:
                  type: str
                  description: User-friendly description of the destination NAT rule.
                destination:
                  type: dict
                  description: Match criteria for destination NAT.
                  suboptions:
                    address:
                      type: str
                      description: IP address, subnet, or range to match for destination NAT.
                    fqdn:
                      type: str
                      description: Fully qualified domain name to match for destination NAT.
                    group:
                      type: dict
                      description: Address/network/port group to match for destination NAT.
                      suboptions:
                        address_group:
                          type: str
                          description: Address group name to match.
                        domain_group:
                          type: str
                          description: Domain group name to match.
                        mac_group:
                          type: str
                          description: MAC address group name to match.
                        network_group:
                          type: str
                          description: Network group name to match.
                        port_group:
                          type: str
                          description: Port group name to match.
                    port:
                      type: str
                      description: Port number or range for destination NAT.
                    protocol:
                      type: str
                      description: Protocol to match (TCP, UDP, ICMP, etc.).
                    exclude:
                      type: bool
                      description: Exclude packets matching this rule from NAT.
                    log:
                      type: bool
                      description: Log packets hitting this destination NAT rule.
                    disable:
                      type: bool
                      description: Disable this destination NAT rule.
        source:
          type: dict
          description: Configuration for source NAT rules.
          suboptions:
            rule:
              type: list
              elements: dict
              description: List of source NAT rules.
              suboptions:
                id:
                  type: int
                  required: true
                  description: Rule number for source NAT.
                description:
                  type: str
                  description: User-friendly description of the source NAT rule.
                destination:
                  type: dict
                  description: Match criteria for source NAT.
                  suboptions:
                    address:
                      type: str
                      description: IP address, subnet, or range to match for source NAT.
                    fqdn:
                      type: str
                      description: Fully qualified domain name to match for source NAT.
                    group:
                      type: dict
                      description: Address/network/port group to match for source NAT.
                      suboptions:
                        address_group:
                          type: str
                          description: Address group name to match.
                        domain_group:
                          type: str
                          description: Domain group name to match.
                        mac_group:
                          type: str
                          description: MAC address group name to match.
                        network_group:
                          type: str
                          description: Network group name to match.
                        port_group:
                          type: str
                          description: Port group name to match.
                    port:
                      type: str
                      description: Port number or range for source NAT.
                    protocol:
                      type: str
                      description: Protocol to match (TCP, UDP, ICMP, etc.).
                    exclude:
                      type: bool
                      description: Exclude packets matching this rule from NAT.
                    log:
                      type: bool
                      description: Log packets hitting this source NAT rule.
                    disable:
                      type: bool
                      description: Disable this source NAT rule.
        static:
          type: dict
          description: Configuration for static NAT rules.
          suboptions:
            rule:
              type: list
              elements: dict
              description: List of static NAT rules.
              suboptions:
                id:
                  type: int
                  required: true
                  description: Rule number for static NAT (one-to-one).
                destination:
                  type: dict
                  description: Match criteria for static NAT.
                  suboptions:
                    address:
                      type: str
                      description: IP address, subnet, or range to match for static NAT.
                log:
                  type: bool
                  description: Log packets hitting this static NAT rule.
                disable:
                  type: bool
                  description: Disable this static NAT rule.
                description:
                  type: str
                  description: User-friendly description of the static NAT rule.
                inbound_interface:
                  type: list
                  elements: str
                  description: List of inbound interfaces that this static NAT rule applies to.
                translation:
                  type: dict
                  description: Translation configuration for static NAT.
                  suboptions:
                    address:
                      type: str
                      description: IP address or prefix to translate to.
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the VYOS device by
      executing the command B(show configuration commands | grep nat).
    - The states I(replaced) and I(overridden) have identical
      behaviour for this module.
    - The state I(parsed) reads the configuration from C(show configuration commands | grep nat) option and
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
# Using merged
- name: Merge NAT source rule
  vyos.vyos.vyos_nat:
    config:
      source:
        rule:
          - id: 100
            description: "Outbound masquerade"
    state: merged

# Using gathered
- name: Gather NAT config
  vyos.vyos.vyos_nat:
    state: gathered

# Using deleted
- name: Delete NAT config
  vyos.vyos.vyos_nat:
    state: deleted

# Using replaced
- name: Replace NAT config
  vyos.vyos.vyos_nat:
    config:
      source:
        rule:
          - id: 100
            description: "Replaced rule"
    state: replaced

# Using parsed
- name: Parse NAT config
  vyos.vyos.vyos_nat:
    running_config: "{{ lookup('file', './nat_config.cfg') }}"
    state: parsed

# Using rendered
- name: Render NAT config offline
  vyos.vyos.vyos_nat:
    config:
      source:
        rule:
          - id: 100
            description: "Rendered rule"
    state: rendered
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
    - set nat source rule 100 description 'Outbound masquerade'
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set nat source rule 100 description 'Rendered rule'
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

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.nat.nat import (
    NatArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.nat.nat import (
    Nat,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=NatArgs.argument_spec,
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

    result = Nat(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
