# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Route_maps parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

class Route_mapsTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        prefix = {"set": "set", "remove": "delete"}
        super(Route_mapsTemplate, self).__init__(lines=lines, tmplt=self, prefix=prefix)

    # fmt: off
    PARSERS = [
        {
            "name": "route_map",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "route_map",
            "setval": "policy route-map {{route_map}}",
            "remval": "policy route-map {{route_map}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                    }
                }
            },
        },
        {
            "name": "rule_number",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "rule_number",
            "setval": "policy route-map {{route_map}} rule {{rule_number}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}"
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "call",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\scall\s(?P<call>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "rule_number",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} call {{call}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} call {{call}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "call": "{{call}}"
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sdescription\s(?P<description>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "rule_number",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} description {{description}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} description {{description}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "description": "{{description}}"
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "action",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\saction\s(?P<action>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "rule_number",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} action {{action}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} action {{action}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "action": "{{action}}"
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "continue",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\scontinue\s(?P<continue>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "rule_number",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} continue {{continue}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} continue {{continue}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "continue": "{{continue}}"
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "on_match_next",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\son-match\snext(?P<next>)
                *$""",
                re.VERBOSE,
            ),
            "compval": "on_match.next",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} on-match next",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} on-match next",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "on_match": {
                                        "next": "{{True if next is defined}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "on_match_goto",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\son-match\sgoto\s(?P<goto>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "on_match.next",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} on-match goto {{on_match.goto}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} on-match next {{on_match.goto}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "on_match": {
                                        "goto": "{{goto}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_aggregator_ip",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\saggregator\sip\s(?P<ip>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.aggregator",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} set aggregator ip {{aggregator.ip}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} set aggregator ip {{aggregator.ip}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "aggregator": {
                                            "ip": "{{ip}}"
                                        }
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_aggregator_as",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\saggregator\sas\s(?P<as>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.aggregator",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} set aggregator as {{aggregator.as}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} set aggregator as {{aggregator.as}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "aggregator": {
                                            "as": "{{as}}"
                                        }
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_as_path_exclude",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sas-path-exclude\s(?P<as>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.as_path_exclude",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} set as-path-exclude {{as_path_exclude}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} set as-path-exclude {{as_path_exclude}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "as_path_exclude": "{{as}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_as_path_prepend",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sas-path-prepend\s(?P<as>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.as_path_prepend",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} set as-path-prepend {{as_path_prepend}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} set as-path-prepend {{as_path_exclude}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "as_path_prepend": "{{as}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_atomic_aggregate",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\satomic-aggregate(?P<as>)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.atomic-aggregate",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} set atomic-aggregate",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} set atomic-aggregate",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "atomic_aggregate": "{{True if as is defined}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_bgp_extcommunity_rt",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sbgp-extcommunity-rt\s(?P<bgp>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.bgp_extcommunity_rt",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set bgp-extcommunity-rt {{bgp_extcommunity_rt}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set bgp-extcommunity-rt {{bgp_extcommunity_rt}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "bgp_extcommunity_rt": "{{bgp}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_comm_list",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\scomm-list\scomm-list\s(?P<comm_list>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.comm_list.comm_list",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set comm-list comm-list {{comm_list}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set comm-list comm-list {{comm_list}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "comm_list": {"comm_list": "{{comm_list}}"}
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_comm_list_delete",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\scomm-list\sdelete(?P<delete>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.comm_list.comm_list",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set comm-list delete",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set comm-list delete",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "comm_list": {"delete": "{{True if delete is defined}}"}
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_extcommunity_rt",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sextcommunity-rt\s(?P<extcommunity_rt>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.extcommunity_rt",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set extcommunity-rt {{extcommunity_rt}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set extcommunity-rt {{extcommunity_rt}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "extcommunity_rt": "{{extcommunity_rt}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_extcommunity_soo",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sextcommunity-soo\s(?P<extcommunity_soo>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.extcommunity_soo",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set extcommunity-soo {{extcommunity_soo}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set extcommunity-soo {{extcommunity_soo}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "extcommunity_soo": "{{extcommunity_soo}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_ip_next_hop",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sip-next-hop\s(?P<ip_next_hop>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.ip_next_hop",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set ip-next-hop {{ip_next_hop}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set ip-next-hop {{ip_next_hop}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "ip_next_hop": "{{ip_next_hop}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_ipv6_next_hop",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sipv6-next-hop\s(?P<ipv6_next_hop>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.ipv6_next_hop",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set ipv6-next-hop {{ipv6_next_hop}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set ipv6-next-hop {{ipv6_next_hop}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "ipv6_next_hop": "{{ipv6_next_hop}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_large_community",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\slarge-community\s(?P<large_community>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.large_community",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set large-community {{large_community}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set large-community {{large_community}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "large_community": "{{large_community}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_local_preference",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\slocal-preference\s(?P<local_preference>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.local_preference",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set local-preference {{local_preference}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set local_preference {{local_preference}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "local_preference": "{{local_preference}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_metric",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\smetric\s(?P<metric>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.metric",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set metric {{metric}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set metric {{metric}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "metric": "{{metric}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_metric_type",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\smetric_type\s(?P<metric_type>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.metric_type",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set metric-type {{metric_type}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set metric-type {{metric_type}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "metric_type": "{{metric_type}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_origin",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sorigin\s(?P<origin>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.origin",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set origin {{origin}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set origin {{origin}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "origin": "{{origin}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_originator_id",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\soriginator-id\s(?P<originator_id>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.originator_id",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set originator-id {{originator_id}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set originator-id {{originator_id}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "originator_id": "{{originator_id}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_src",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\ssrc\s(?P<src>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.src",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set src {{src}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set src {{src}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "src": "{{src}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_tag",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\stag\s(?P<tag>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.tag",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set tag {{tag}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set tag {{tag}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "tag": "{{tag}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "set_weight",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\sset\sweight\s(?P<weight>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "set.weight",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set weight {{weight}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "set weight {{weight}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "set": {
                                        "weight": "{{weight}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_as_path",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\sas-path\s(?P<as_path>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.as_path",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match as-path {{as_path}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match as-path {{as_path}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "as_path": "{{as_path}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_community_community_list",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\scommunity\scommunity-list\s(?P<community_list>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.community.community_list",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match community community-list {{community_list}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match community community-list {{community_list}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "community": {"community_list": "{{community_list}}"}
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_community_exact_match",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\scommunity\sexact_match(?P<exact_match>)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.community.exact_match",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match community exact-match",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match community exact-match",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "community": {"exact_match": "{{True if exact_match is defined}}"}
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_extcommunity",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\sextcommunity\s(?P<extcommunity>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.extcommunity",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match extcommunity {{extcommunity}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match extcommunity {{extcommunity}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "extcommunity": "{{extcommunity}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_interface",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\sinterface\s(?P<interface>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.interface",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match interface {{interface}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match interface {{interface}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "interface": "{{interface}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_large_community_large_community_list",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\slarge-community\slarge-community-list\s(?P<lc>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.large_community_large_community_list",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match large-community large-community-list {{lc}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match large-community large-community-list {{lc}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "large_community_large_community_list": "{{large_community_large_community_list}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_metric",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\smetric\s(?P<metric>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.metric",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match metric {{metric}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match metric {{metric}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "metric": "{{metric}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_origin",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\sorigin\s(?P<origin>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.origin",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match origin {{origin}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match origin {{origin}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "origin": "{{origin}}"
                                    }
                                }
                        }
                    }
                }
            }
        },
        {
            "name": "match_peer",
            "getval": re.compile(
                r"""
                ^set\spolicy\sroute-map\s(?P<route_map>\S+)\srule\s(?P<rule_number>\d+)\smatch\speer\s(?P<peer>\S+)
                *$""",
                re.VERBOSE,
            ),
            "compval": "match.peer",
            "setval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match peer {{peer}}",
            "remval": "policy route-map {{route_map}} rule {{rule_number}} "
                      "match peer {{peer}}",
            "result": {
                "route_maps": {
                    "{{ route_map }}": {
                        "route_map": '{{ route_map }}',
                        "entries": {
                            "{{rule_number}}":
                                {
                                    "rule_number": "{{rule_number}}",
                                    "match": {
                                        "peer": "{{peer}}"
                                    }
                                }
                        }
                    }
                }
            }
        },

    ]
    # fmt: on
