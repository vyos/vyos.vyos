#
# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class Vpn_ipsec_s2sTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Vpn_ipsec_s2sTemplate, self).__init__(
            lines=lines,
            tmplt=self,
            module=module,
            prefix=prefix,
        )

    # fmt: off
    PARSERS = [
        {
            "name": "peer",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }}",
            "result": {
                "site_to_site": {
                    "peer": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                        },
                    },
                },
            },
        },
        {
            "name": "peer.disable",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)\sdisable$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} disable",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "disable": True}}},
            },
        },
        {
            "name": "peer.authentication.local_id",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\slocal-id\s'(?P<local_id>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication local-id '{{ local_id }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"local_id": "{{ local_id }}"}}},
                },
            },
        },
        {
            "name": "peer.authentication.remote_id",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\sremote-id\s'(?P<remote_id>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication remote-id '{{ remote_id }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"remote_id": "{{ remote_id }}"}}},
                },
            },
        },
        {
            "name": "peer.authentication.mode",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\smode\s'(?P<mode>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication mode '{{ mode }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"mode": "{{ mode }}"}}},
                },
            },
        },
        {
            "name": "peer.authentication.use_x509_id",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\suse-x509-id$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication use-x509-id",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"use_x509_id": True}}},
                },
            },
        },
        {
            "name": "peer.authentication.ppk.id",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\sppk\sid\s'(?P<id>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication ppk id '{{ id }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"ppk": {"id": "{{ id }}"}}}},
                },
            },
        },
        {
            "name": "peer.authentication.ppk.required",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\sppk\srequired$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication ppk required",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"ppk": {"required": True}}}},
                },
            },
        },
        {
            "name": "peer.authentication.rsa.local_key",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\srsa\slocal-key\s'(?P<local_key>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication rsa local-key '{{ local_key }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"rsa": {"local_key": "{{ local_key }}"}}}},
                },
            },
        },
        {
            "name": "peer.authentication.rsa.remote_key",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\srsa\sremote-key\s'(?P<remote_key>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication rsa remote-key '{{ remote_key }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"rsa": {"remote_key": "{{ remote_key }}"}}}},
                },
            },
        },
        {
            "name": "peer.authentication.rsa.passphrase",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\srsa\spassphrase\s'(?P<passphrase>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication rsa passphrase '{{ passphrase }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"rsa": {"passphrase": "{{ passphrase }}"}}}},
                },
            },
        },
        {
            "name": "peer.authentication.x509.certificate",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\sx509\scertificate\s'(?P<certificate>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication x509 certificate '{{ certificate }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"x509": {"certificate": "{{ certificate }}"}}}},
                },
            },
        },
        {
            "name": "peer.authentication.x509.passphrase",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\sx509\spassphrase\s'(?P<passphrase>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication x509 passphrase '{{ passphrase }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"x509": {"passphrase": "{{ passphrase }}"}}}},
                },
            },
        },
        {
            "name": "peer.authentication.x509.ca_certificate",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sauthentication\sx509\sca-certificate\s'(?P<ca_certificate>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} authentication x509 ca-certificate '{{ ca_certificate }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "authentication": {"x509": {"ca_certificate": ["{{ ca_certificate }}"]}}}},
                },
            },
        },
        {
            "name": "peer.childless",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \schildless\s'(?P<childless>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} childless '{{ childless }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "childless": "{{ childless }}"}}},
            },
        },
        {
            "name": "peer.connection_type",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sconnection-type\s'(?P<connection_type>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} connection-type '{{ connection_type }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "connection_type": "{{ connection_type }}"}}},
            },
        },
        {
            "name": "peer.default_esp_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sdefault-esp-group\s'(?P<default_esp_group>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} default-esp-group '{{ default_esp_group }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "default_esp_group": "{{ default_esp_group }}"}}},
            },
        },
        {
            "name": "peer.description",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sdescription\s'(?P<description>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} description '{{ description }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "description": "{{ description }}"}}},
            },
        },
        {
            "name": "peer.dhcp_interface",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sdhcp-interface\s'(?P<dhcp_interface>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} dhcp-interface '{{ dhcp_interface }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "dhcp_interface": "{{ dhcp_interface }}"}}},
            },
        },
        {
            "name": "peer.force_udp_encapsulation",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sforce-udp-encapsulation$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} force-udp-encapsulation",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "force_udp_encapsulation": True}}},
            },
        },
        {
            "name": "peer.ike_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sike-group\s'(?P<ike_group>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} ike-group '{{ ike_group }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "ike_group": "{{ ike_group }}"}}},
            },
        },
        {
            "name": "peer.ikev2_reauth",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sikev2-reauth\s'(?P<ikev2_reauth>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} ikev2-reauth '{{ ikev2_reauth }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "ikev2_reauth": "{{ ikev2_reauth }}"}}},
            },
        },
        {
            "name": "peer.local_address",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \slocal-address\s'(?P<local_address>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} local-address '{{ local_address }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "local_address": "{{ local_address }}"}}},
            },
        },
        {
            "name": "peer.remote_address",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sremote-address\s'(?P<remote_address>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} remote-address '{{ remote_address }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "remote_address": ["{{ remote_address }}"]}}},
            },
        },
        {
            "name": "peer.replay_window",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \sreplay-window\s'(?P<replay_window>\d+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} replay-window '{{ replay_window }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "replay_window": "{{ replay_window }}"}}},
            },
        },
        {
            "name": "peer.virtual_address",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \svirtual-address\s'(?P<virtual_address>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} virtual-address '{{ virtual_address }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "virtual_address": ["{{ virtual_address }}"]}}},
            },
        },
        {
            "name": "peer.tunnel",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }}",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}"}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.disable",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\sdisable$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} disable",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "disable": True}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.esp_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\sesp-group\s'(?P<esp_group>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} esp-group '{{ esp_group }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "esp_group": "{{ esp_group }}"}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.protocol",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\sprotocol\s'(?P<protocol>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} protocol '{{ protocol }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "protocol": "{{ protocol }}"}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.priority",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\spriority\s'(?P<priority>\d+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} priority '{{ priority }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "priority": "{{ priority }}"}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.local.port",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\slocal\sport\s'(?P<port>\d+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} local port '{{ port }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "local": {"port": "{{ port }}"}}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.local.prefix",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\slocal\sprefix\s'(?P<prefix>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} local prefix '{{ prefix }}'",
            "result": {
                "site_to_site": {
                    "peer": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "local": {"prefix": ["{{ prefix }}"]}}},
                        },
                    },
                },
            },
        },
        {
            "name": "peer.tunnel.remote.port",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\sremote\sport\s'(?P<port>\d+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} remote port '{{ port }}'",
            "result": {
                "site_to_site": {
                    "peer": {"{{ name }}": {"name": "{{ name }}", "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "remote": {"port": "{{ port }}"}}}}},
                },
            },
        },
        {
            "name": "peer.tunnel.remote.prefix",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \stunnel\s(?P<tunnel_id>\d+)\sremote\sprefix\s'(?P<prefix>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} tunnel {{ tunnel_id }} remote prefix '{{ prefix }}'",
            "result": {
                "site_to_site": {
                    "peer": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "tunnel": {"{{ tunnel_id }}": {"tunnel_id": "{{ tunnel_id }}", "remote": {"prefix": ["{{ prefix }}"]}}},
                        },
                    },
                },
            },
        },
        {
            "name": "peer.vti.bind",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \svti\sbind\s'(?P<bind>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} vti bind '{{ bind }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "vti": {"bind": "{{ bind }}"}}}},
            },
        },
        {
            "name": "peer.vti.esp_group",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \svti\sesp-group\s'(?P<esp_group>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} vti esp-group '{{ esp_group }}'",
            "result": {
                "site_to_site": {"peer": {"{{ name }}": {"name": "{{ name }}", "vti": {"esp_group": "{{ esp_group }}"}}}},
            },
        },
        {
            "name": "peer.vti.traffic_selector.local.prefix",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \svti\straffic-selector\slocal\sprefix\s'(?P<prefix>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} vti traffic-selector local prefix '{{ prefix }}'",
            "result": {
                "site_to_site": {
                    "peer": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "vti": {"traffic_selector": {"local": {"prefix": ["{{ prefix }}"]}}},
                        },
                    },
                },
            },
        },
        {
            "name": "peer.vti.traffic_selector.remote.prefix",
            "getval": re.compile(
                r"""
                ^set\svpn\sipsec\ssite-to-site\speer\s(?P<name>\S+)
                \svti\straffic-selector\sremote\sprefix\s'(?P<prefix>[^']+)'$
                """, re.VERBOSE,
            ),
            "setval": "vpn ipsec site-to-site peer {{ name }} vti traffic-selector remote prefix '{{ prefix }}'",
            "result": {
                "site_to_site": {
                    "peer": {
                        "{{ name }}": {
                            "name": "{{ name }}",
                            "vti": {"traffic_selector": {"remote": {"prefix": ["{{ prefix }}"]}}},
                        },
                    },
                },
            },
        },
    ]
    # fmt: on
