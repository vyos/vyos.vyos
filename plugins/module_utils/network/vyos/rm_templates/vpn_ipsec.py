# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The VPN IPSEC parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class Vpn_ipsecTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Vpn_ipsecTemplate, self).__init__(
            lines=lines,
            tmplt=self,
            prefix=prefix,
            module=module,
        )

    # fmt: off
    PARSERS = [
        # ---------------------------------------------------------------
        # esp-group
        # ---------------------------------------------------------------
        {
            "name": "esp_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                    },
                },
            },
        },
        {
            "name": "esp_group.proposal",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} proposal {{ proposal_id }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "esp_group.proposal.encryption",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \sencryption\s'?(?P<encryption>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} proposal {{ proposal_id }} encryption {{ encryption }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                                "encryption": "{{ encryption }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "esp_group.proposal.hash",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \shash\s'?(?P<hash>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} proposal {{ proposal_id }} hash {{ hash }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                                "hash": "{{ hash }}",
                            },
                        },
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # ike-group
        # ---------------------------------------------------------------
        {
            "name": "ike_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                    },
                },
            },
        },
        {
            "name": "ike_group.key_exchange",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \skey-exchange\s'?(?P<key_exchange>\w+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} key-exchange {{ key_exchange }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "key_exchange": "{{ key_exchange }}",
                    },
                },
            },
        },
        {
            "name": "ike_group.proposal",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} proposal {{ proposal_id }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "ike_group.proposal.dh_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \sdh-group\s'?(?P<dh_group>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} proposal {{ proposal_id }} dh-group {{ dh_group }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                                "dh_group": "{{ dh_group }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "ike_group.proposal.encryption",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \sencryption\s'?(?P<encryption>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} proposal {{ proposal_id }} encryption {{ encryption }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                                "encryption": "{{ encryption }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "ike_group.proposal.hash",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sproposal\s(?P<proposal_id>\d+)
                \shash\s'?(?P<hash>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} proposal {{ proposal_id }} hash {{ hash }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "proposal": {
                            "{{ proposal_id }}": {
                                "proposal_id": "{{ proposal_id }}",
                                "hash": "{{ hash }}",
                            },
                        },
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # authentication psk
        # ---------------------------------------------------------------
        {
            "name": "authentication.psk",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\spsk\s(?P<psk>\S+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication psk {{ name }}",
            "result": {
                "authentication": {
                    "psk": {
                        "{{ psk }}": {
                            "name": "{{ psk }}",
                        },
                    },
                },
            },
        },
        {
            "name": "authentication.psk.id",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\spsk\s(?P<psk>\S+)
                \sid\s'?(?P<id>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication psk {{ name }} id {{ id }}",
            "result": {
                "authentication": {
                    "psk": {
                        "{{ psk }}": {
                            "name": "{{ psk }}",
                            "id": ["{{ id }}"],
                        },
                    },
                },
            },
        },
        {
            "name": "authentication.psk.secret",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\spsk\s(?P<psk>\S+)
                \ssecret\s'?(?P<secret>[^']+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication psk {{ name }} secret '{{ secret }}'",
            "result": {
                "authentication": {
                    "psk": {
                        "{{ psk }}": {
                            "name": "{{ psk }}",
                            "secret": "{{ secret }}",
                        },
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # profile
        # ---------------------------------------------------------------
        {
            "name": "profile",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }}",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                    },
                },
            },
        },
        {
            "name": "profile.authentication.mode",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \sauthentication\smode\s'?(?P<mode>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }} authentication mode {{ mode }}",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                        "authentication": {
                            "mode": "{{ mode }}",
                        },
                    },
                },
            },
        },
        {
            "name": "profile.authentication.pre_shared_secret",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \sauthentication\spre-shared-secret\s'?(?P<pre_shared_secret>[^']+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }} authentication pre-shared-secret '{{ pre_shared_secret }}'",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                        "authentication": {
                            "pre_shared_secret": "{{ pre_shared_secret }}",
                        },
                    },
                },
            },
        },
        {
            "name": "profile.bind_tunnel",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \sbind\stunnel\s'?(?P<bind_tunnel>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }} bind tunnel {{ bind_tunnel }}",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                        "bind_tunnel": ["{{ bind_tunnel }}"],
                    },
                },
            },
        },
        {
            "name": "profile.esp_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \sesp-group\s'?(?P<esp_group>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }} esp-group {{ esp_group }}",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                        "esp_group": "{{ esp_group }}",
                    },
                },
            },
        },
        {
            "name": "profile.ike_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \sike-group\s'?(?P<ike_group>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }} ike-group {{ ike_group }}",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                        "ike_group": "{{ ike_group }}",
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # ike-group: remaining fields
        # ---------------------------------------------------------------
        {
            "name": "ike_group.close_action",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sclose-action\s'?(?P<close_action>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} close-action {{ close_action }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "close_action": "{{ close_action }}",
                    },
                },
            },
        },
        {
            "name": "ike_group.dead_peer_detection.action",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sdead-peer-detection\saction\s'?(?P<action>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} dead-peer-detection action {{ action }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "dead_peer_detection": {"action": "{{ action }}"},
                    },
                },
            },
        },
        {
            "name": "ike_group.dead_peer_detection.interval",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sdead-peer-detection\sinterval\s'?(?P<interval>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} dead-peer-detection interval {{ interval }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "dead_peer_detection": {"interval": "{{ interval }}"},
                    },
                },
            },
        },
        {
            "name": "ike_group.dead_peer_detection.timeout",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sdead-peer-detection\stimeout\s'?(?P<timeout>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} dead-peer-detection timeout {{ timeout }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "dead_peer_detection": {"timeout": "{{ timeout }}"},
                    },
                },
            },
        },
        {
            "name": "ike_group.disable_mobike",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sdisable-mobike
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} disable-mobike",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "disable_mobike": True,
                    },
                },
            },
        },
        {
            "name": "ike_group.ikev2_reauth",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \sikev2-reauth
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} ikev2-reauth",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "ikev2_reauth": True,
                    },
                },
            },
        },
        {
            "name": "ike_group.lifetime",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \slifetime\s'?(?P<lifetime>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} lifetime {{ lifetime }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "lifetime": "{{ lifetime }}",
                    },
                },
            },
        },
        {
            "name": "ike_group.mode",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sike-group\s(?P<ike_group>\S+)
                \smode\s'?(?P<mode>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec ike-group {{ name }} mode {{ mode }}",
            "result": {
                "ike_group": {
                    "{{ ike_group }}": {
                        "name": "{{ ike_group }}",
                        "mode": "{{ mode }}",
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # esp-group: remaining fields
        # ---------------------------------------------------------------
        {
            "name": "esp_group.compression",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \scompression
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} compression",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "compression": True,
                    },
                },
            },
        },
        {
            "name": "esp_group.disable_rekey",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \sdisable-rekey
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} disable-rekey",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "disable_rekey": True,
                    },
                },
            },
        },
        {
            "name": "esp_group.life_bytes",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \slife-bytes\s'?(?P<life_bytes>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} life-bytes {{ life_bytes }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "life_bytes": "{{ life_bytes }}",
                    },
                },
            },
        },
        {
            "name": "esp_group.life_packets",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \slife-packets\s'?(?P<life_packets>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} life-packets {{ life_packets }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "life_packets": "{{ life_packets }}",
                    },
                },
            },
        },
        {
            "name": "esp_group.lifetime",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \slifetime\s'?(?P<lifetime>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} lifetime {{ lifetime }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "lifetime": "{{ lifetime }}",
                    },
                },
            },
        },
        {
            "name": "esp_group.mode",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \smode\s'?(?P<mode>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} mode {{ mode }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "mode": "{{ mode }}",
                    },
                },
            },
        },
        {
            "name": "esp_group.pfs",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sesp-group\s(?P<esp_group>\S+)
                \spfs\s'?(?P<pfs>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec esp-group {{ name }} pfs {{ pfs }}",
            "result": {
                "esp_group": {
                    "{{ esp_group }}": {
                        "name": "{{ esp_group }}",
                        "pfs": "{{ pfs }}",
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # authentication.psk: remaining fields
        # ---------------------------------------------------------------
        {
            "name": "authentication.psk.secret_type",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\spsk\s(?P<psk>\S+)
                \ssecret-type\s'?(?P<secret_type>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication psk {{ name }} secret-type {{ secret_type }}",
            "result": {
                "authentication": {
                    "psk": {
                        "{{ psk }}": {
                            "name": "{{ psk }}",
                            "secret_type": "{{ secret_type }}",
                        },
                    },
                },
            },
        },
        {
            "name": "authentication.psk.dhcp_interface",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\spsk\s(?P<psk>\S+)
                \sdhcp-interface\s'?(?P<dhcp_interface>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication psk {{ name }} dhcp-interface {{ dhcp_interface }}",
            "result": {
                "authentication": {
                    "psk": {
                        "{{ psk }}": {
                            "name": "{{ psk }}",
                            "dhcp_interface": ["{{ dhcp_interface }}"],
                        },
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # authentication.ppk
        # ---------------------------------------------------------------
        {
            "name": "authentication.ppk",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\sppk\s(?P<ppk>\S+)
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication ppk {{ name }}",
            "result": {
                "authentication": {
                    "ppk": {
                        "{{ ppk }}": {
                            "name": "{{ ppk }}",
                        },
                    },
                },
            },
        },
        {
            "name": "authentication.ppk.id",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\sppk\s(?P<ppk>\S+)
                \sid\s'?(?P<id>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication ppk {{ name }} id {{ id }}",
            "result": {
                "authentication": {
                    "ppk": {
                        "{{ ppk }}": {
                            "name": "{{ ppk }}",
                            "id": ["{{ id }}"],
                        },
                    },
                },
            },
        },
        {
            "name": "authentication.ppk.secret",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\sppk\s(?P<ppk>\S+)
                \ssecret\s'?(?P<secret>[^']+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication ppk {{ name }} secret '{{ secret }}'",
            "result": {
                "authentication": {
                    "ppk": {
                        "{{ ppk }}": {
                            "name": "{{ ppk }}",
                            "secret": "{{ secret }}",
                        },
                    },
                },
            },
        },
        {
            "name": "authentication.ppk.secret_type",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sauthentication\sppk\s(?P<ppk>\S+)
                \ssecret-type\s'?(?P<secret_type>[\w-]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec authentication ppk {{ name }} secret-type {{ secret_type }}",
            "result": {
                "authentication": {
                    "ppk": {
                        "{{ ppk }}": {
                            "name": "{{ ppk }}",
                            "secret_type": "{{ secret_type }}",
                        },
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # profile: remaining fields
        # ---------------------------------------------------------------
        {
            "name": "profile.disable",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sprofile\s(?P<profile>\S+)
                \sdisable
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec profile {{ name }} disable",
            "result": {
                "profile": {
                    "{{ profile }}": {
                        "name": "{{ profile }}",
                        "disable": True,
                    },
                },
            },
        },

        # ---------------------------------------------------------------
        # top-level: interface, log, options, disable_uniqreqids
        # ---------------------------------------------------------------
        {
            "name": "interface",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sinterface\s'?(?P<interface>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec interface {{ interface }}",
            "result": {
                "interface": ["{{ interface }}"],
            },
        },
        {
            "name": "log.level",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\slog\slevel\s'?(?P<level>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec log level {{ level }}",
            "result": {
                "log": {"level": "{{ level }}"},
            },
        },
        {
            "name": "log.subsystem",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\slog\ssubsystem\s'?(?P<subsystem>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec log subsystem {{ subsystem }}",
            "result": {
                "log": {"subsystem": ["{{ subsystem }}"]},
            },
        },
        {
            "name": "options.disable_route_autoinstall",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\sdisable-route-autoinstall
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options disable-route-autoinstall",
            "result": {
                "options": {"disable_route_autoinstall": True},
            },
        },
        {
            "name": "options.flexvpn",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\sflexvpn
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options flexvpn",
            "result": {
                "options": {"flexvpn": True},
            },
        },
        {
            "name": "options.interface",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\sinterface\s'?(?P<interface>\S+?)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options interface {{ interface }}",
            "result": {
                "options": {"interface": "{{ interface }}"},
            },
        },
        {
            "name": "options.retransmission.attempts",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\sretransmission\sattempts\s'?(?P<attempts>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options retransmission attempts {{ attempts }}",
            "result": {
                "options": {"retransmission": {"attempts": "{{ attempts }}"}},
            },
        },
        {
            "name": "options.retransmission.base",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\sretransmission\sbase\s'?(?P<base>[\d.]+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options retransmission base {{ base }}",
            "result": {
                "options": {"retransmission": {"base": "{{ base }}"}},
            },
        },
        {
            "name": "options.retransmission.timeout",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\sretransmission\stimeout\s'?(?P<timeout>\d+)'?
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options retransmission timeout {{ timeout }}",
            "result": {
                "options": {"retransmission": {"timeout": "{{ timeout }}"}},
            },
        },
        {
            "name": "options.virtual_ip",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\soptions\svirtual-ip
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec options virtual-ip",
            "result": {
                "options": {"virtual_ip": True},
            },
        },
        {
            "name": "disable_uniqreqids",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\sdisable-uniqreqids
                \s*$""", re.VERBOSE,
            ),
            "setval": "vpn ipsec disable-uniqreqids",
            "result": {
                "disable_uniqreqids": True,
            },
        },
    ]
    # fmt: on
