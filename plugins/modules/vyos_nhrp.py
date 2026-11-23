#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for vyos_nhrp
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_nhrp
version_added: 7.0.0
short_description: NHRP resource module
description:
  - This module manages the Next Hop Resolution Protocol (NHRP) configuration of
    tunnel interfaces on devices running VyOS, as used for DMVPN.
author:
  - Evgeny Molotkov (@omnom62)
notes:
  - Tested against VyOS 1.5.1.
  - This module works with connection C(network_cli).
  - The tunnel interfaces themselves (encapsulation, source, addresses) are managed with
    M(vyos.vyos.vyos_interfaces) and M(vyos.vyos.vyos_l3_interfaces), and their IPsec
    protection with M(vyos.vyos.vyos_vpn_ipsec).
  - VyOS requires tunnels used by NHRP to have a /32 address.
options:
  config:
    description: The NHRP configuration.
    type: dict
    suboptions:
      tunnels:
        description: NHRP configuration per tunnel interface.
        type: list
        elements: dict
        suboptions:
          name:
            description: The tunnel interface name, for example C(tun0).
            type: str
            required: true
          authentication:
            description:
              - The authentication password, sent in clear text in NHRP packets.
              - Up to 8 characters, without spaces.
            type: str
          holdtime:
            description: The holding time of NHRP registrations and resolutions, in seconds (1-65000).
            type: int
          mtu:
            description: The MTU advertised in NHRP registrations (68-16000).
            type: int
          network_id:
            description: The NHRP network identifier of the tunnel.
            type: int
          multicast:
            description:
              - Where multicast traffic is sent, as protocol addresses or C(dynamic) for all
                dynamically learned peers.
              - A hub typically uses C(dynamic), so that routing protocols reach all spokes.
            type: list
            elements: str
          redirect:
            description: Whether to send NHRP traffic indication (redirect) messages, typically on a hub.
            type: bool
          shortcut:
            description: Whether to create shortcut routes from NHRP redirects, typically on a spoke.
            type: bool
          registration_no_unique:
            description: Whether to allow a peer to register with a changing NBMA address.
            type: bool
          map:
            description: Static mappings of tunnel addresses to NBMA addresses.
            type: list
            elements: dict
            suboptions:
              tunnel_ip:
                description: The tunnel (protocol) address of the peer.
                type: str
                required: true
              nbma:
                description: The NBMA (underlay) address of the peer, or C(local) for this router.
                type: str
          nhs:
            description: The next hop servers (hubs) this router registers with.
            type: list
            elements: dict
            suboptions:
              tunnel_ip:
                description: The tunnel address of the server, or C(dynamic) to learn it from the server.
                type: str
                required: true
              nbma:
                description: The NBMA (underlay) addresses of the server.
                type: list
                elements: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the VyOS device by
        executing the command B(show configuration commands | grep 'protocols nhrp').
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
# vyos@vyos:~$ show configuration commands | grep 'protocols nhrp'
#

- name: Configure a DMVPN hub tunnel
  vyos.vyos.vyos_nhrp:
    config:
      tunnels:
        - name: tun0
          authentication: secret
          holdtime: 300
          multicast:
            - dynamic
          redirect: true
          registration_no_unique: true
    state: merged

# Task output
# -----------
#
#    commands:
#      - set protocols nhrp tunnel tun0 authentication 'secret'
#      - set protocols nhrp tunnel tun0 holdtime 300
#      - set protocols nhrp tunnel tun0 redirect
#      - set protocols nhrp tunnel tun0 registration-no-unique
#      - set protocols nhrp tunnel tun0 multicast dynamic

# Using merged, on a spoke

- name: Configure a DMVPN spoke tunnel
  vyos.vyos.vyos_nhrp:
    config:
      tunnels:
        - name: tun0
          authentication: secret
          shortcut: true
          nhs:
            - tunnel_ip: dynamic
              nbma:
                - 192.0.2.1
          multicast:
            - dynamic
    state: merged

# Task output
# -----------
#
#    commands:
#      - set protocols nhrp tunnel tun0 authentication 'secret'
#      - set protocols nhrp tunnel tun0 shortcut
#      - set protocols nhrp tunnel tun0 multicast dynamic
#      - set protocols nhrp tunnel tun0 nhs tunnel-ip dynamic nbma 192.0.2.1

# Using replaced

# Before state:
# -------------
#
# set protocols nhrp tunnel tun0 authentication 'secret'
# set protocols nhrp tunnel tun0 holdtime '300'
# set protocols nhrp tunnel tun0 multicast 'dynamic'
# set protocols nhrp tunnel tun0 redirect

- name: Replace the configuration of tun0
  vyos.vyos.vyos_nhrp:
    config:
      tunnels:
        - name: tun0
          authentication: secret
          multicast:
            - dynamic
    state: replaced

# Task output
# -----------
#
#    commands:
#      - delete protocols nhrp tunnel tun0 holdtime
#      - delete protocols nhrp tunnel tun0 redirect

# Using overridden

# Before state:
# -------------
#
# set protocols nhrp tunnel tun0 authentication 'secret'
# set protocols nhrp tunnel tun1 shortcut

- name: Override the NHRP configuration with one tunnel
  vyos.vyos.vyos_nhrp:
    config:
      tunnels:
        - name: tun0
          authentication: secret
    state: overridden

# Task output
# -----------
#
#    commands:
#      - delete protocols nhrp tunnel tun1

# Using deleted

- name: Delete the NHRP configuration of one tunnel
  vyos.vyos.vyos_nhrp:
    config:
      tunnels:
        - name: tun1
    state: deleted

- name: Delete all NHRP configuration
  vyos.vyos.vyos_nhrp:
    state: deleted

# Task output (all NHRP configuration)
# ------------------------------------
#
#    commands:
#      - delete protocols nhrp

# Using gathered

- name: Gather the NHRP configuration
  vyos.vyos.vyos_nhrp:
    state: gathered

# Task output
# -----------
#
#    gathered:
#      tunnels:
#        - name: tun0
#          authentication: secret
#          holdtime: 300
#          multicast:
#            - dynamic
#          redirect: true

# Using rendered

- name: Render the commands for a spoke tunnel
  vyos.vyos.vyos_nhrp:
    config:
      tunnels:
        - name: tun0
          nhs:
            - tunnel_ip: 10.0.0.1
              nbma:
                - 192.0.2.1
    state: rendered

# Task output
# -----------
#
#    rendered:
#      - set protocols nhrp tunnel tun0 nhs tunnel-ip 10.0.0.1 nbma 192.0.2.1

# Using parsed

- name: Parse NHRP configuration from device output
  vyos.vyos.vyos_nhrp:
    running_config: |
      set protocols nhrp tunnel tun0 map tunnel-ip '10.0.0.2' nbma '192.0.2.2'
      set protocols nhrp tunnel tun0 shortcut
    state: parsed

# Task output
# -----------
#
#    parsed:
#      tunnels:
#        - name: tun0
#          map:
#            - tunnel_ip: 10.0.0.2
#              nbma: 192.0.2.2
#          shortcut: true
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
    - set protocols nhrp tunnel tun0 authentication 'secret'
    - set protocols nhrp tunnel tun0 nhs tunnel-ip dynamic nbma 192.0.2.1
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - set protocols nhrp tunnel tun0 shortcut
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

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.argspec.nhrp.nhrp import (
    NhrpArgs,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.nhrp.nhrp import (
    Nhrp,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=NhrpArgs.argument_spec,
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

    result = Nhrp(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
