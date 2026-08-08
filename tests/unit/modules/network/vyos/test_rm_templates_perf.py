# -*- coding: utf-8 -*-
# Copyright 2026 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Performance budget tests for rm_templates parsers.

These tests guard against re-introducing catastrophic regex backtracking
in the rm_template parsers (T8609).  Pre-fix, parse() over realistic
device-output input could take 50+ seconds because of `(group)*`
quantifiers on groups containing `\\S+`.  Post-fix, the same input
parses in single-digit milliseconds.

A 1-second budget is comfortably above post-fix runtime and well below
the pre-regression cliff, so the test fails sharply if the bug returns.
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import time

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.bgp_address_family_14 import (
    Bgp_address_familyTemplate14,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.bgp_global_14 import (
    Bgp_globalTemplate14,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.route_maps_14 import (
    Route_mapsTemplate14,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.snmp_server import (
    Snmp_serverTemplate,
)


PARSE_BUDGET_SECONDS = 1.0


def _time_parse(parser_class, lines):
    """Time a single ``parse()`` call against ``lines``; returns elapsed seconds."""
    parser = parser_class(lines=lines)
    t0 = time.perf_counter()
    parser.parse()
    return time.perf_counter() - t0


def test_route_maps_14_parse_budget():
    """Realistic route-map config: parse() must finish under 1s.

    Pre-T8609: ~50s.  Post-fix: <50ms.  Inputs use 20+ char names
    because the backtracking is exponential in the first \\S+ run
    after the prefix.
    """
    lines = [
        "set policy route-map ADVERTISE-ANYCAST-v6 rule 10 action 'permit'",
        "set policy route-map ADVERTISE-ANYCAST-v6 rule 10 match ipv6 address prefix-list 'ANYCAST-AGGREGATE-v6'",
        "set policy route-map DEFAULT-ORIGINATE-SENTINEL-v6 rule 10 action 'permit'",
        "set policy route-map DEFAULT-ORIGINATE-SENTINEL-v6 rule 10 match ipv6 address prefix-list 'AS64496-SENTINEL-v6'",
        "set policy route-map DEFAULT-ORIGINATE-SENTINEL-v6 rule 10 set local-preference '120'",
        "set policy route-map IXP-PEER-INGRESS-v4 rule 10 action 'permit'",
        "set policy route-map IXP-PEER-INGRESS-v4 rule 10 match ip address prefix-list 'IXP-INBOUND-v4'",
        "set policy route-map IXP-PEER-INGRESS-v4 rule 10 set community 'additive 65000:100'",
        "set policy route-map TRANSIT-EGRESS-v4 rule 100 action 'permit'",
        "set policy route-map TRANSIT-EGRESS-v4 rule 100 match ip address prefix-list 'CUSTOMER-PREFIXES-v4'",
        "set policy route-map TRANSIT-EGRESS-v4 rule 100 set as-path prepend '65000 65000'",
        "set policy route-map UPSTREAM-INGRESS-v4 rule 10 action 'permit'",
    ]
    elapsed = _time_parse(Route_mapsTemplate14, lines)
    assert elapsed < PARSE_BUDGET_SECONDS, (
        "Route_mapsTemplate14.parse() took %.2fs (budget %.2fs); "
        "possible regression of T8609 (rm_templates regex backtracking)."
        % (elapsed, PARSE_BUDGET_SECONDS)
    )


def test_bgp_global_14_parse_budget():
    """Realistic BGP neighbor/address-family config: parse() under 1s."""
    lines = [
        "set protocols bgp 65001 neighbor 2001:db8:abcd:1234::1 remote-as '65002'",
        "set protocols bgp 65001 neighbor 2001:db8:abcd:1234::1 description 'IXP-PEER-1'",
        "set protocols bgp 65001 neighbor 2001:db8:abcd:1234::1 address-family ipv6-unicast route-map import 'IXP-INGRESS-v6'",
        "set protocols bgp 65001 neighbor 2001:db8:abcd:1234::1 address-family ipv6-unicast route-map export 'IXP-EGRESS-v6'",
        "set protocols bgp 65001 neighbor 192.0.2.1 remote-as '65003'",
        "set protocols bgp 65001 neighbor 192.0.2.1 description 'TRANSIT-PROVIDER-1'",
        "set protocols bgp 65001 neighbor 192.0.2.1 address-family ipv4-unicast route-map import 'TRANSIT-INGRESS-v4'",
        "set protocols bgp 65001 neighbor 192.0.2.1 address-family ipv4-unicast route-map export 'TRANSIT-EGRESS-v4'",
    ]
    elapsed = _time_parse(Bgp_globalTemplate14, lines)
    assert elapsed < PARSE_BUDGET_SECONDS, (
        "Bgp_globalTemplate14.parse() took %.2fs (budget %.2fs); "
        "possible regression of T8609 (rm_templates regex backtracking)."
        % (elapsed, PARSE_BUDGET_SECONDS)
    )


def test_snmp_server_parse_budget():
    """Realistic SNMP v3 config: parse() under 1s."""
    lines = [
        "set service snmp community PUBLIC-COMMUNITY-NAME-1 authorization 'ro'",
        "set service snmp community PUBLIC-COMMUNITY-NAME-1 client '192.0.2.0/24'",
        "set service snmp v3 trap-target TRAP-TARGET-LONG-NAME-1 user 'monitor'",
        "set service snmp v3 trap-target TRAP-TARGET-LONG-NAME-1 protocol 'udp'",
        "set service snmp v3 trap-target TRAP-TARGET-LONG-NAME-1 port '162'",
        "set service snmp v3 user TRAP-USER-LONG-NAME-1 mode 'auth'",
        "set service snmp v3 user TRAP-USER-LONG-NAME-1 group 'monitor'",
    ]
    elapsed = _time_parse(Snmp_serverTemplate, lines)
    assert elapsed < PARSE_BUDGET_SECONDS, (
        "Snmp_serverTemplate.parse() took %.2fs (budget %.2fs); "
        "possible regression of T8609 (rm_templates regex backtracking)."
        % (elapsed, PARSE_BUDGET_SECONDS)
    )


def test_bgp_address_family_14_parse_budget():
    """Realistic BGP address-family aggregate config: parse() under 1s."""
    lines = [
        "set protocols bgp 65001 address-family ipv4-unicast network 198.51.100.0/24 backdoor",
        "set protocols bgp 65001 address-family ipv4-unicast network 198.51.100.0/24 path-limit '4'",
        "set protocols bgp 65001 address-family ipv4-unicast network 198.51.100.0/24 route-map 'NET-IN-v4'",
        "set protocols bgp 65001 address-family ipv4-unicast aggregate-address 203.0.113.0/24 as-set",
        "set protocols bgp 65001 address-family ipv4-unicast aggregate-address 203.0.113.0/24 summary-only",
        "set protocols bgp 65001 address-family ipv6-unicast network 2001:db8:abcd:1234::/64 backdoor",
        "set protocols bgp 65001 address-family ipv6-unicast network 2001:db8:abcd:1234::/64 route-map 'NET-IN-v6'",
        "set protocols bgp 65001 address-family ipv6-unicast aggregate-address 2001:db8::/32 as-set",
        "set protocols bgp 65001 address-family ipv6-unicast aggregate-address 2001:db8::/32 summary-only",
    ]
    elapsed = _time_parse(Bgp_address_familyTemplate14, lines)
    assert elapsed < PARSE_BUDGET_SECONDS, (
        "Bgp_address_familyTemplate14.parse() took %.2fs (budget %.2fs); "
        "possible regression of T8609 (rm_templates regex backtracking)."
        % (elapsed, PARSE_BUDGET_SECONDS)
    )


def test_route_maps_14_set_comm_list_delete_matches_setval():
    """Round-trip check: the `set_comm_list_delete` parser must match the line its setval generates.

    `set_comm_list_delete`'s setval emits `set policy route-map X rule N set
    comm-list delete` with no token after `delete`.  Pre-T8609 the getval
    happened to match this by accident (a `*` quantifier on the trailing
    `(?P<delete>\\S+)` made the group optional after VERBOSE-strip).  An
    earlier draft of T8609's fix made the group required, causing the
    parser to silently ignore its own output.  This test guards the
    round-trip.
    """
    line = "set policy route-map MY-MAP rule 10 set comm-list delete"
    parser = Route_mapsTemplate14(lines=[line])
    result = parser.parse()
    rm = result.get("route_maps", {}).get("MY-MAP")
    assert rm is not None, (
        "route_maps_14: set_comm_list_delete parser failed to match its "
        "own setval-generated line %r; the parser is broken." % line
    )
    entry = rm.get("entries", {}).get(10, {})
    comm_list = entry.get("set", {}).get("comm_list", {})
    assert comm_list.get("delete"), (
        "route_maps_14: set_comm_list_delete matched the line but did not "
        "populate set.comm_list.delete; check the result template."
    )
