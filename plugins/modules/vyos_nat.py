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
- This module manages NAT configuration on devices running VyOS.
author:
- Evgeny Molotkov (@omnom62)
notes:
- Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025.
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
                description: Log CGNAT address allocations.
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
                            type: str
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
                    description: Source pool configuration for CGNAT translation.
                    suboptions:
                      pool:
                        type: str
                        description: Source pool name to use for CGNAT translation.
                  translation:
                    type: dict
                    description: Translation pool configuration for CGNAT.
                    suboptions:
                      pool:
                        type: str
                        description: Translation pool name to use for CGNAT translation.
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
                  protocol:
                    type: str
                    description: Protocol to NAT (default all).
                  packet_type:
                    type: str
                    description: Packet type to match.
                  exclude:
                    type: bool
                    description: Exclude packets matching this rule from NAT.
                  log:
                    type: bool
                    description: Log packets hitting this rule.
                  disable:
                    type: bool
                    description: Disable this destination NAT rule.
                  inbound_interface:
                    type: dict
                    description: Match inbound interface.
                    suboptions:
                      name:
                        type: str
                        description: Interface name to match.
                      group:
                        type: str
                        description: Interface group to match.
                  destination:
                    type: dict
                    description: Match criteria for destination NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address, subnet, or range to match.
                      fqdn:
                        type: str
                        description: Fully qualified domain name to match.
                      port:
                        type: str
                        description: Port number or range to match.
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
                  translation:
                    type: dict
                    description: Translation configuration for destination NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address or prefix to translate destination to.
                      port:
                        type: str
                        description: Port number or range to translate destination port to.
                      redirect_port:
                        type: str
                        description: Redirect to local port number.
                      address_mapping:
                        type: str
                        choices:
                          - random
                          - persistent
                        description: Address mapping mode for translation.
                      port_mapping:
                        type: str
                        choices:
                          - random
                          - none
                        description: Port mapping mode for translation.
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
                  protocol:
                    type: str
                    description: Protocol to NAT (default all).
                  packet_type:
                    type: str
                    description: Packet type to match.
                  exclude:
                    type: bool
                    description: Exclude packets matching this rule from NAT.
                  log:
                    type: bool
                    description: Log packets hitting this rule.
                  disable:
                    type: bool
                    description: Disable this source NAT rule.
                  outbound_interface:
                    type: dict
                    description: Match outbound interface.
                    suboptions:
                      name:
                        type: str
                        description: Interface name to match.
                      group:
                        type: str
                        description: Interface group to match.
                  destination:
                    type: dict
                    description: Destination match criteria for source NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address, subnet, or range to match.
                      fqdn:
                        type: str
                        description: Fully qualified domain name to match.
                      port:
                        type: str
                        description: Port number or range to match.
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
                  source:
                    type: dict
                    description: Source match criteria for source NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address, subnet, or range to match.
                      fqdn:
                        type: str
                        description: Fully qualified domain name to match.
                      port:
                        type: str
                        description: Port number or range to match.
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
                  translation:
                    type: dict
                    description: Translation configuration for source NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address or prefix to translate source to. Use masquerade to masquerade as the outbound interface address.
                      port:
                        type: str
                        description: Port number or range to translate source port to.
                      address_mapping:
                        type: str
                        choices:
                          - random
                          - persistent
                        description: Address mapping mode for translation.
                      port_mapping:
                        type: str
                        choices:
                          - random
                          - none
                        description: Port mapping mode for translation.
          static:
            type: dict
            description: Configuration for static one-to-one NAT rules.
            suboptions:
              rule:
                type: list
                elements: dict
                description: List of static NAT rules.
                suboptions:
                  id:
                    type: int
                    required: true
                    description: Rule number for static NAT.
                  description:
                    type: str
                    description: User-friendly description of the static NAT rule.
                  destination:
                    type: dict
                    description: Match criteria for static NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address, subnet, or range to match.
                  inbound_interface:
                    type: str
                    description: Inbound interface that this static NAT rule applies to.
                  log:
                    type: bool
                    description: Log packets hitting this static NAT rule.
                  translation:
                    type: dict
                    description: Translation configuration for static NAT.
                    suboptions:
                      address:
                        type: str
                        description: IP address or prefix to translate to.
      nat64:
        type: dict
        description: Configuration for NAT64 (IPv6-to-IPv4) rules.
        suboptions:
          source:
            type: dict
            description: Configuration for NAT64 source rules.
            suboptions:
              rule:
                type: list
                elements: dict
                description: List of NAT64 source rules.
                suboptions:
                  id:
                    type: int
                    required: true
                    description: Rule number for NAT64 source rule (1-999999).
                  description:
                    type: str
                    description: User-friendly description of the NAT64 source rule.
                  disable:
                    type: bool
                    description: Disable this NAT64 source rule.
                  match:
                    type: dict
                    description: Match criteria for NAT64 source rule.
                    suboptions:
                      mark:
                        type: str
                        description: Match on firewall mark value (1-2147483647).
                  source:
                    type: dict
                    description: IPv6 source prefix to match for NAT64 translation.
                    suboptions:
                      prefix:
                        type: str
                        description: IPv6 source prefix to match (h:h:h:h:h:h:h:h/x).
                  translation:
                    type: dict
                    description: Translation configuration for NAT64 source rule.
                    suboptions:
                      pool:
                        type: list
                        elements: dict
                        description: List of translation pools for NAT64.
                        suboptions:
                          id:
                            type: int
                            required: true
                            description: Pool number (1-999999).
                          address:
                            type: str
                            description: IPv4 address or prefix for translation pool.
                          description:
                            type: str
                            description: User-friendly description of the translation pool.
                          disable:
                            type: bool
                            description: Disable this translation pool.
                          port:
                            type: str
                            description: Port number or range for translation pool.
                          protocol:
                            type: str
                            choices:
                              - icmp
                              - tcp
                              - udp
                            description: Protocol for this translation pool entry.
      nat66:
        type: dict
        description: Configuration for NAT66 (IPv6-to-IPv6) rules.
        suboptions:
          destination:
            type: dict
            description: Configuration for NAT66 destination rules.
            suboptions:
              rule:
                type: list
                elements: dict
                description: List of NAT66 destination rules.
                suboptions:
                  id:
                    type: int
                    required: true
                    description: Rule number for NAT66 destination rule.
                  description:
                    type: str
                    description: User-friendly description of the NAT66 destination rule.
                  destination:
                    type: dict
                    description: Match criteria for NAT66 destination rule.
                    suboptions:
                      address:
                        type: str
                        description: IPv6 address or prefix to match.
                      port:
                        type: str
                        description: Port number or range to match.
                  disable:
                    type: bool
                    description: Disable this NAT66 destination rule.
                  exclude:
                    type: bool
                    description: Exclude packets matching this rule from NAT66.
                  inbound_interface:
                    type: dict
                    description: Inbound interface to match for NAT66 destination rule.
                    suboptions:
                      name:
                        type: str
                        description: Interface name to match.
                  log:
                    type: bool
                    description: Log packets hitting this NAT66 destination rule.
                  protocol:
                    type: str
                    description: Protocol to match.
                  source:
                    type: dict
                    description: Source match criteria for NAT66 destination rule.
                    suboptions:
                      address:
                        type: str
                        description: IPv6 source address or prefix to match.
                      port:
                        type: str
                        description: Source port number or range to match.
                  translation:
                    type: dict
                    description: Translation configuration for NAT66 destination rule.
                    suboptions:
                      address:
                        type: str
                        description: IPv6 address or prefix to translate destination to.
                      port:
                        type: str
                        description: Port number or range to translate destination port to.
          source:
            type: dict
            description: Configuration for NAT66 source rules.
            suboptions:
              rule:
                type: list
                elements: dict
                description: List of NAT66 source rules.
                suboptions:
                  id:
                    type: int
                    required: true
                    description: Rule number for NAT66 source rule.
                  description:
                    type: str
                    description: User-friendly description of the NAT66 source rule.
                  destination:
                    type: dict
                    description: Destination match criteria for NAT66 source rule.
                    suboptions:
                      port:
                        type: str
                        description: Destination port number or range to match.
                      prefix:
                        type: str
                        description: IPv6 destination prefix to match (h:h:h:h:h:h:h:h/x).
                  disable:
                    type: bool
                    description: Disable this NAT66 source rule.
                  exclude:
                    type: bool
                    description: Exclude packets matching this rule from NAT66.
                  log:
                    type: bool
                    description: Log packets hitting this NAT66 source rule.
                  outbound_interface:
                    type: dict
                    description: Outbound interface to match for NAT66 source rule.
                    suboptions:
                      name:
                        type: str
                        description: Interface name to match.
                  protocol:
                    type: str
                    description: Protocol to match.
                  source:
                    type: dict
                    description: Source match criteria for NAT66 source rule.
                    suboptions:
                      port:
                        type: str
                        description: Source port number or range to match.
                      prefix:
                        type: str
                        description: IPv6 source prefix to match (h:h:h:h:h:h:h:h/x).
                  translation:
                    type: dict
                    description: Translation configuration for NAT66 source rule.
                    suboptions:
                      address:
                        type: str
                        description: IPv6 address or prefix to translate source to. Use masquerade to masquerade as the outbound interface address.
                      port:
                        type: str
                        description: Port number or range to translate source port to.
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the VyOS device by
      executing the command B(show configuration commands | grep nat).
    - The state I(parsed) reads the configuration from C(show configuration commands | grep nat)
      and transforms it into Ansible structured data as per the module argspec.
      The value is then returned in the I(parsed) key within the result.
    - The states I(replaced) and I(overridden) have identical behaviour for this module.
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
# Using merged - configure CGNAT
- name: Merge CGNAT configuration
  vyos.vyos.vyos_nat:
    config:
      nat:
        cgnat:
          log_allocation: true
          pool:
            external:
              - name: ext-pool-1
                external_port_range: "10000-20000"
                per_user_limit:
                  port: "200"
                range:
                  - 203.0.113.0/24
            internal:
              - name: int-pool-1
                range:
                  - 10.0.0.0/24
          rule:
            - id: 1
              source:
                pool: int-pool-1
              translation:
                pool: ext-pool-1
    state: merged

# Using merged - configure destination NAT
- name: Merge destination NAT rule
  vyos.vyos.vyos_nat:
    config:
      nat:
        destination:
          rule:
            - id: 100
              description: "Web server NAT"
              protocol: tcp
              log: true
              destination:
                address: 198.51.100.10
                port: "80"
              translation:
                address: 192.168.1.10
                port: "8080"
    state: merged

# Using merged - configure source NAT
- name: Merge source NAT rule
  vyos.vyos.vyos_nat:
    config:
      nat:
        source:
          rule:
            - id: 200
              description: "Outbound masquerade"
              protocol: tcp
              log: true
              outbound_interface:
                name: eth0
              translation:
                address: masquerade
    state: merged

# Using merged - configure static NAT
- name: Merge static NAT rule
  vyos.vyos.vyos_nat:
    config:
      nat:
        static:
          rule:
            - id: 300
              description: "Static mapping"
              inbound_interface: eth2
              destination:
                address: 198.51.100.20
              translation:
                address: 192.168.1.20
              log: true
    state: merged

# Using merged - configure NAT64
- name: Merge NAT64 source rule
  vyos.vyos.vyos_nat:
    config:
      nat64:
        source:
          rule:
            - id: 10
              description: "NAT64 example"
              source:
                prefix: 2001:db8::/96
              match:
                mark: "100"
              translation:
                pool:
                  - id: 1
                    address: 192.168.100.10
                    port: "1-65535"
                    protocol: udp
    state: merged

# Using merged - configure NAT66
- name: Merge NAT66 destination rule
  vyos.vyos.vyos_nat:
    config:
      nat66:
        destination:
          rule:
            - id: 20
              description: "NAT66 DNAT"
              protocol: tcp
              inbound_interface:
                name: eth1
              destination:
                address: 2001:db8::1
              translation:
                address: 2001:db8:1::10
                port: "8443"
    state: merged

# Using gathered
- name: Gather NAT config
  vyos.vyos.vyos_nat:
    state: gathered

# Using deleted
- name: Delete all NAT config
  vyos.vyos.vyos_nat:
    state: deleted

# Using replaced
- name: Replace NAT source rules
  vyos.vyos.vyos_nat:
    config:
      nat:
        source:
          rule:
            - id: 200
              description: "Replaced outbound rule"
              translation:
                address: masquerade
    state: replaced

# Using parsed
- name: Parse NAT config from file
  vyos.vyos.vyos_nat:
    running_config: "{{ lookup('file', './nat_config.cfg') }}"
    state: parsed

# Using rendered
- name: Render NAT config offline
  vyos.vyos.vyos_nat:
    config:
      nat:
        source:
          rule:
            - id: 200
              description: "Rendered rule"
              translation:
                address: masquerade
    state: rendered
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
