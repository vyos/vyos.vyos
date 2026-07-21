#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_vpn_ipsec_s2s
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_vpn_ipsec_s2s
short_description: Manages IPsec site-to-site VPN peers on VyOS network devices.
description: This module manages VPN IPsec site-to-site peer configuration on VyOS
  devices -- policy-based tunnels and route-based (VTI) connections. IKE/ESP groups,
  PSK/PPK authentication, and IPsec profiles are managed by the separate vyos_vpn_ipsec
  module; peers here reference those by name.
version_added: 1.0.0
author: Evgeny Molotkov (@omnom62)
notes:
  - Tested against VyOS 1.4 and 1.5.
  - "Source of truth: vyos-1x's interface-definitions/vpn_ipsec.xml.in, resolved and
    drafted via this collection's fetch_vyos_xml_definition.py / parse_xml_definitions.py
    helper scripts, then hand-reviewed."
options:
  config:
    description: IPsec site-to-site configuration.
    type: dict
    suboptions:
      peer:
        description: List of site-to-site peers.
        type: list
        elements: dict
        suboptions:
          name:
            description: Connection name of the peer.
            type: str
            required: true
          disable:
            description: Disable this peer.
            type: bool
          authentication:
            description: Peer authentication settings.
            type: dict
            suboptions:
              local_id:
                description: Local ID for peer authentication.
                type: str
              remote_id:
                description: ID for remote authentication.
                type: str
              mode:
                description: Authentication mode.
                type: str
                choices: [pre-shared-secret, rsa, x509]
              use_x509_id:
                description: Use certificate common name as ID.
                type: bool
              ppk:
                description: Post-quantum preshared key reference for this peer.
                type: dict
                suboptions:
                  id:
                    description: Post-quantum preshared key ID for this connection.
                    type: str
                  required:
                    description: Require a valid PPK for the connection to establish.
                    type: bool
              rsa:
                description: RSA key authentication.
                type: dict
                suboptions:
                  local_key:
                    description: Name of the PKI key-pair with the local private key.
                    type: str
                  remote_key:
                    description: Name of the PKI key-pair with the remote public key.
                    type: str
                  passphrase:
                    description: Local private key passphrase.
                    type: str
              x509:
                description: X.509 certificate authentication.
                type: dict
                suboptions:
                  certificate:
                    description: Certificate in PKI configuration.
                    type: str
                  passphrase:
                    description: Private key passphrase.
                    type: str
                  ca_certificate:
                    description: Certificate Authority chain in PKI configuration.
                    type: list
                    elements: str
          childless:
            description: Childless IKE SA initiation support.
            type: str
            choices: [allow, prefer, force, never]
          connection_type:
            description: Connection type.
            type: str
            choices: [initiate, trap, none]
          default_esp_group:
            description: Default ESP group name for tunnels under this peer that
              don't specify their own.
            type: str
          description:
            description: Description.
            type: str
          dhcp_interface:
            description: DHCP interface supplying the next-hop IP address.
            type: str
          force_udp_encapsulation:
            description: Force UDP encapsulation.
            type: bool
          ike_group:
            description: IKE group name.
            type: str
          ikev2_reauth:
            description: Re-authentication of the remote peer during an IKE re-key
              (IKEv2 only).
            type: str
            choices: ["yes", "no", inherit]
          local_address:
            description: IPv4 or IPv6 address of a local interface to use for the
              VPN, or "any".
            type: str
          remote_address:
            description: IPv4 or IPv6 address(es) of the remote peer, or "any".
            type: list
            elements: str
          replay_window:
            description: IPsec replay window to configure for this CHILD_SA.
            type: int
          virtual_address:
            description: Initiator-requested virtual address(es) from the peer.
            type: list
            elements: str
          tunnel:
            description: Policy-based tunnel definitions for this peer.
            type: list
            elements: dict
            suboptions:
              tunnel_id:
                description: The tunnel identifier.
                type: int
                required: true
              disable:
                description: Disable this tunnel.
                type: bool
              esp_group:
                description: ESP group name for this tunnel (overrides the peer's
                  default_esp_group).
                type: str
              protocol:
                description: Protocol to match for this tunnel's traffic selector.
                type: str
              priority:
                description: Priority for this IPsec policy (lowest value is most
                  preferred).
                type: int
              local:
                description: Local traffic selector for this tunnel.
                type: dict
                suboptions:
                  port:
                    description: Local port to match.
                    type: int
                  prefix:
                    description: Local IPv4 or IPv6 prefix(es) to match.
                    type: list
                    elements: str
              remote:
                description: Remote traffic selector for this tunnel.
                type: dict
                suboptions:
                  port:
                    description: Remote port to match.
                    type: int
                  prefix:
                    description: Remote IPv4 or IPv6 prefix(es) to match.
                    type: list
                    elements: str
          vti:
            description: Route-based (VTI) connection settings for this peer.
            type: dict
            suboptions:
              bind:
                description: VTI tunnel interface associated with this connection.
                type: str
              esp_group:
                description: ESP group name for this VTI connection.
                type: str
              traffic_selector:
                description: Traffic selector for the VTI connection.
                type: dict
                suboptions:
                  local:
                    description: Local traffic-selector parameters.
                    type: dict
                    suboptions:
                      prefix:
                        description: Local IPv4 or IPv6 prefix(es).
                        type: list
                        elements: str
                  remote:
                    description: Remote traffic-selector parameters.
                    type: dict
                    suboptions:
                      prefix:
                        description: Remote IPv4 or IPv6 prefix(es).
                        type: list
                        elements: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VyOS device
        by executing the command B(show configuration commands | match "vpn ipsec
        site-to-site").
      - The state I(parsed) reads the configuration from the C(running_config) option
        and transforms it into Ansible structured data as per the resource module's
        argspec, returned in the I(parsed) key within the result.
    type: str
  state:
    description: The state the configuration should be left in.
    type: str
    choices: [merged, replaced, overridden, deleted, gathered, rendered, parsed]
    default: merged
"""

EXAMPLES = """
- name: Merge a site-to-site peer
  vyos.vyos.vyos_vpn_ipsec_s2s:
    config:
      peer:
        - name: PEER-TEST
          ike_group: IKE-TEST
          default_esp_group: ESP-TEST
          remote_address:
            - 203.0.113.1
    state: merged
"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden) or C(deleted)
  type: dict
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden) or C(deleted)
  type: list
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: dict
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vpn_ipsec_s2s.vpn_ipsec_s2s import (
    Vpn_ipsec_s2sArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vpn_ipsec_s2s.vpn_ipsec_s2s import (
    Vpn_ipsec_s2s,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Vpn_ipsec_s2sArgs.argument_spec,
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

    result = Vpn_ipsec_s2s(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
