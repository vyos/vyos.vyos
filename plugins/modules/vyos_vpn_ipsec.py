#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_vpn_ipsec
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_vpn_ipsec
short_description: Manages global IPsec (ike-group, esp-group, profile, authentication, options) attributes of VyOS network devices.
description: This module manages global VPN IPsec configuration on VyOS devices
  -- IKE groups, ESP groups, PSK/PPK authentication, IPsec profiles, and global
  options. Site-to-site peers and IKEv2 remote-access connections are handled by
  separate modules.
version_added: 6.2.0
author: Evgeny Molotkov (@omnom62)
notes:
  - Tested against VyOS 1.4 and 1.5.
  - "Source of truth for field types/choices: device node.def templates under /opt/vyatta/share/vyatta-cfg/templates/vpn/ipsec/."
options:
  config:
    description: IPsec global configuration.
    type: dict
    suboptions:
      ike_group:
        description: List of IKE groups.
        type: list
        elements: dict
        suboptions:
          name:
            description: The name of the IKE group.
            type: str
            required: true
          close_action:
            description: Action to take if a child SA is unexpectedly closed.
            type: str
            choices: [none, trap, start]
          dead_peer_detection:
            description: Dead Peer Detection (DPD).
            type: dict
            suboptions:
              action:
                description: Keep-alive failure action.
                type: str
                choices: [trap, clear, restart]
              interval:
                description: Keep-alive interval in seconds.
                type: int
              timeout:
                description: Dead Peer Detection keep-alive timeout (IKEv1 only), in seconds.
                type: int
          disable_mobike:
            description: Disable MOBIKE support (IKEv2 only).
            type: bool
          ikev2_reauth:
            description: Re-authentication of the remote peer during an IKE re-key (IKEv2 only).
            type: bool
          key_exchange:
            description: IKE version.
            type: str
            choices: [ikev1, ikev2]
          lifetime:
            description: IKE lifetime in seconds.
            type: int
          mode:
            description: IKEv1 phase 1 mode.
            type: str
            choices: [main, aggressive]
          proposal:
            description: List of IKE proposals.
            type: list
            elements: dict
            suboptions:
              proposal_id:
                description: The proposal identifier.
                type: int
              dh_group:
                description: Diffie-Hellman group. See VyOS/strongSwan documentation for the
                  full set of valid values -- validated device-side, not enumerated here since
                  the set is version-dependent.
                type: int
              encryption:
                description: Encryption algorithm. See VyOS/strongSwan documentation for the
                  full set of valid values -- validated device-side, not enumerated here since
                  the set is version-dependent.
                type: str
              hash:
                description: Hash algorithm. See VyOS/strongSwan documentation for the
                  full set of valid values -- validated device-side.
                type: str
              prf:
                description: Pseudo-Random Function. See VyOS/strongSwan documentation for the
                  full set of valid values -- validated device-side.
                type: str
      esp_group:
        description: List of ESP groups.
        type: list
        elements: dict
        suboptions:
          name:
            description: The name of the ESP group.
            type: str
            required: true
          compression:
            description: Enable ESP compression.
            type: bool
          disable_rekey:
            description: Do not locally initiate a re-key of the SA; remote peer must re-key before expiration.
            type: bool
          life_bytes:
            description: Security Association byte count to expire.
            type: int
          life_packets:
            description: Security Association packet count to expire.
            type: int
          lifetime:
            description: Security Association time to expire, in seconds.
            type: int
          mode:
            description: ESP mode.
            type: str
            choices: [tunnel, transport]
          pfs:
            description: ESP Perfect Forward Secrecy. See VyOS/strongSwan documentation for the
              full set of valid values -- validated device-side, not enumerated here since
              the set is version-dependent.
            type: str
          proposal:
            description: List of ESP proposals.
            type: list
            elements: dict
            suboptions:
              proposal_id:
                description: The proposal identifier.
                type: int
              encryption:
                description: Encryption algorithm. See VyOS/strongSwan documentation for the
                  full set of valid values -- validated device-side, not enumerated here since
                  the set is version-dependent.
                type: str
              hash:
                description: Hash algorithm. See VyOS/strongSwan documentation for the
                  full set of valid values -- validated device-side.
                type: str
      authentication:
        description: Global pre-shared-key and post-quantum pre-shared-key definitions.
        type: dict
        suboptions:
          psk:
            description: List of pre-shared keys.
            type: list
            elements: dict
            suboptions:
              name:
                description: Pre-shared key name.
                type: str
                required: true
              id:
                description: ID(s) for authentication.
                type: list
                elements: str
              dhcp_interface:
                description: DHCP interface(s) supplying next-hop IP address.
                type: list
                elements: str
              secret:
                description: IKE pre-shared secret key.
                type: str
              secret_type:
                description: Secret encoding type.
                type: str
                choices: [base64, hex, plaintext]
          ppk:
            description: List of post-quantum pre-shared keys.
            type: list
            elements: dict
            suboptions:
              name:
                description: Post-quantum pre-shared key name.
                type: str
                required: true
              id:
                description: ID(s) for PPK.
                type: list
                elements: str
              secret:
                description: Post-quantum pre-shared secret key.
                type: str
              secret_type:
                description: Secret encoding type.
                type: str
                choices: [base64, hex, plaintext]
      profile:
        description: List of VPN IPsec profiles (used for e.g. DMVPN/GRE tunnel binding).
        type: list
        elements: dict
        suboptions:
          name:
            description: Profile name.
            type: str
            required: true
          authentication:
            description: Authentication settings for this profile.
            type: dict
            suboptions:
              mode:
                description: Authentication mode.
                type: str
                choices: [pre-shared-secret]
              pre_shared_secret:
                description: Pre-shared secret key.
                type: str
          bind_tunnel:
            description: Tunnel interface(s) associated with this profile.
            type: list
            elements: str
          disable:
            description: Disable this profile.
            type: bool
          esp_group:
            description: ESP group name to use for this profile.
            type: str
          ike_group:
            description: IKE group name to use for this profile.
            type: str
      interface:
        description: Interface(s) IPsec listens on. If omitted, listens on all interfaces.
        type: list
        elements: str
      log:
        description: IPsec logging settings.
        type: dict
        suboptions:
          level:
            description: Global IPsec logging level.
            type: int
          subsystem:
            description: Per-subsystem logging levels to enable.
            type: list
            elements: str
      options:
        description: Global IPsec options.
        type: dict
        suboptions:
          disable_route_autoinstall:
            description: Do not automatically install routes to remote networks.
            type: bool
          flexvpn:
            description: Allow FlexVPN vendor ID payload (IKEv2 only).
            type: bool
          interface:
            description: Single interface for IPsec options scope (distinct from top-level interface list).
            type: str
          retransmission:
            description: IPsec retransmission settings.
            type: dict
            suboptions:
              attempts:
                description: Maximum number of retransmissions.
                type: int
              base:
                description: Base of exponential backoff.
                type: float
              timeout:
                description: Timeout in seconds before the first retransmission.
                type: int
          virtual_ip:
            description: Allow install of virtual-ip addresses.
            type: bool
      disable_uniqreqids:
        description: Disable requirement for unique IDs in the Security Database.
        type: bool
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VyOS device by
        executing the command B(show configuration commands | match "vpn ipsec").
      - The states I(replaced) and I(overridden) have identical behaviour for this module
        with respect to named collections (ike_group, esp_group, profile, authentication),
        but differ in scope -- see the module description for detail.
      - The state I(parsed) reads the configuration from the C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec,
        returned in the I(parsed) key within the result.
    type: str
  state:
    description: The state the configuration should be left in.
    type: str
    choices: [merged, replaced, overridden, deleted, gathered, rendered, parsed]
    default: merged
"""

EXAMPLES = """
# -------------------
# Using merged
# -------------------

# Before state:
# -------------
# vyos@vyos:~$ show configuration commands | match "vpn ipsec"
# (empty)

# Task
# -------------
# - name: Merge provided configuration with device configuration
#   vyos.vyos.vyos_vpn_ipsec:
#     config:
#       esp_group:
#         - name: ESP-TEST
#           proposal:
#             - proposal_id: 1
#               encryption: aes256
#               hash: sha256
#       ike_group:
#         - name: IKE-TEST
#           key_exchange: ikev2
#           proposal:
#             - proposal_id: 1
#               encryption: aes256
#               hash: sha256
#               dh_group: 14
#     state: merged

# Task output:
# -------------
# "commands": [
#     "set vpn ipsec esp-group ESP-TEST",
#     "set vpn ipsec esp-group ESP-TEST proposal 1",
#     "set vpn ipsec esp-group ESP-TEST proposal 1 encryption aes256",
#     "set vpn ipsec esp-group ESP-TEST proposal 1 hash sha256",
#     "set vpn ipsec ike-group IKE-TEST",
#     "set vpn ipsec ike-group IKE-TEST key-exchange ikev2",
#     "set vpn ipsec ike-group IKE-TEST proposal 1",
#     "set vpn ipsec ike-group IKE-TEST proposal 1 encryption aes256",
#     "set vpn ipsec ike-group IKE-TEST proposal 1 hash sha256",
#     "set vpn ipsec ike-group IKE-TEST proposal 1 dh-group 14"
# ]

# -------------------
# Using gathered
# -------------------

# Task
# -------------
# - name: Gather current vpn_ipsec configuration
#   vyos.vyos.vyos_vpn_ipsec:
#     state: gathered

# -------------------
# Using deleted
# -------------------

# Task
# -------------
# - name: Remove all vpn_ipsec configuration
#   vyos.vyos.vyos_vpn_ipsec:
#     state: deleted

# -------------------
# Using rendered
# -------------------

# Task
# -------------
# - name: Render configuration without touching the device
#   vyos.vyos.vyos_vpn_ipsec:
#     config:
#       esp_group:
#         - name: ESP-TEST
#           proposal:
#             - proposal_id: 1
#               encryption: aes256
#               hash: sha256
#     state: rendered

# -------------------
# Using parsed
# -------------------

# Task
# -------------
# - name: Parse raw config text into structured facts
#   vyos.vyos.vyos_vpn_ipsec:
#     running_config: "{{ lookup('file', './vpn_ipsec.cfg') }}"
#     state: parsed
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
    - set vpn ipsec esp-group ESP-TEST proposal 1 encryption aes256
    - set vpn ipsec ike-group IKE-TEST key-exchange ikev2
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set vpn ipsec esp-group ESP-TEST proposal 1 encryption aes256
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

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.vpn_ipsec.vpn_ipsec import (
    Vpn_ipsecArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.vpn_ipsec.vpn_ipsec import (
    Vpn_ipsec,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Vpn_ipsecArgs.argument_spec,
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

    result = Vpn_ipsec(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
