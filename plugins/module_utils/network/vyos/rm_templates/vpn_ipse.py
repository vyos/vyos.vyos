# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Vpn_ipsec parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.

NOTE: this is a first pass, built only against the fixture lines
actually captured on target150 so far:

    set vpn ipsec authentication psk PSK-TEST id 'local@example.com'
    set vpn ipsec authentication psk PSK-TEST id 'remote@example.com'
    set vpn ipsec authentication psk PSK-TEST secret 'test-not-real-secret'
    set vpn ipsec esp-group ESP-TEST proposal 1 encryption 'aes256'
    set vpn ipsec esp-group ESP-TEST proposal 1 hash 'sha256'
    set vpn ipsec ike-group IKE-TEST key-exchange 'ikev2'
    set vpn ipsec ike-group IKE-TEST proposal 1 dh-group '14'
    set vpn ipsec ike-group IKE-TEST proposal 1 encryption 'aes256'
    set vpn ipsec ike-group IKE-TEST proposal 1 hash 'sha256'
    set vpn ipsec profile testprofile authentication mode 'pre-shared-secret'
    set vpn ipsec profile testprofile authentication pre-shared-secret 'test-not-real-secret'
    set vpn ipsec profile testprofile bind tunnel 'tun0'
    set vpn ipsec profile testprofile esp-group 'ESP-TEST'
    set vpn ipsec profile testprofile ike-group 'IKE-TEST'

Remaining fields from the docstring (dead_peer_detection, lifetime, mode,
pfs, disable_rekey, compression, log, options, disable_uniqreqids,
esp_group/ike_group bare-tag-only lines) are NOT covered here yet —
need a second fixture pass exercising those before this is complete.
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
            "setval": "vpn ipsec profile {{ name }} authentication mode {{ authentication.mode }}",
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
            "setval": "vpn ipsec profile {{ name }} authentication pre-shared-secret '{{ authentication.pre_shared_secret }}'",
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
    ]
    # fmt: on
