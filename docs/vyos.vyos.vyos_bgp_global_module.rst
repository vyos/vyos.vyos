.. _vyos.vyos.vyos_bgp_global_module:


*************************
vyos.vyos.vyos_bgp_global
*************************

**BGP Global Resource Module.**


Version added: 2.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages BGP global configuration of interfaces on devices running VYOS.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dict of BGP global configuration for interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>aggregate_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP aggregate network.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_set</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Generate AS-set path information for this aggregate address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP aggregate network.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>summary_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Announce the aggregate summary network only.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AS number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bgp_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>always_compare_med</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Always compare MEDs from different neighbors</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bestpath</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Default bestpath selection mechanism</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>confed</li>
                                    <li>ignore</li>
                        </ul>
                </td>
                <td>
                        <div>AS-path attribute comparison parameters</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>compare_routerid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Compare the router-id for identical EBGP paths</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>med</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>confed</li>
                                    <li>missing-as-worst</li>
                        </ul>
                </td>
                <td>
                        <div>MED attribute comparison parameters</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cluster_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-reflector cluster-id</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>confederation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AS confederation parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>identifier</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Confederation AS identifier</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Peer ASs in the BGP confederation</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dampening</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable route-flap dampening</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>half_life</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Half-life penalty in seconds</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_suppress_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum duration to suppress a stable route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>re_use</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time to start reusing a route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start_suppress_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When to start suppressing a route</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP defaults</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_pref</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Default local preference</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_ipv4_unicast</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Deactivate IPv4 unicast for a peer by default</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>deterministic_med</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Compare MEDs between different peers in the same AS</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable_network_import_check</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable IGP route check for network statements</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>distance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Administrative distances for BGP routes</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Administrative distance for a specific BGP prefix</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>external</li>
                                    <li>internal</li>
                                    <li>local</li>
                        </ul>
                </td>
                <td>
                        <div>Type of route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>distance</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enforce_first_as</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Require first AS in the path to match peer&#x27;s AS</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>graceful_restart</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum time to hold onto restarting peer&#x27;s stale paths</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_neighbor_changes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Log neighbor up/down changes and reset reason</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_client_to_client_reflection</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable client to client route reflection</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_fast_external_failover</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable immediate session reset if peer&#x27;s connected link goes down</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>router_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP router-id</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>scan_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP route scanner interval</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maximum_paths</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP multipaths</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>No. of paths.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP multipaths</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neighbor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP neighbor</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP neighbor address (v4/v6).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertisement_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum interval for sending routing updates.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allowas_in</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of occurrences of AS number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_override</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>AS for routes sent to this neighbor to be the local AS.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>attribute_unchanged</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP attributes are sent unchanged.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>as_path</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>med</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>med</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>next_hop</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>capability</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Advertise capabilities to this neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dynamic</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Advertise dynamic capability to this neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>orf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>send</li>
                                    <li>receive</li>
                        </ul>
                </td>
                <td>
                        <div>Advertise ORF capability to this neighbor.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_originate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Send default route to this neighbor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>description text</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable_capability_negotiation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disbale capability negotiation with the neighbor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable_connected_check</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable check to see if EBGP peer&#x27;s address is a connected route.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable_send_community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>extended</li>
                                    <li>standard</li>
                        </ul>
                </td>
                <td>
                        <div>Disable sending community attributes to this neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>distribute_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Access-list to filter route updates to/from this neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Access-list number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>export</li>
                                    <li>import</li>
                        </ul>
                </td>
                <td>
                        <div>Access-list to filter outgoing/incoming route updates to this neighbor</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ebgp_multihop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allow this EBGP neighbor to not be on a directly connected network. Specify the number hops.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>As-path-list to filter route updates to/from this neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>export</li>
                                    <li>import</li>
                        </ul>
                </td>
                <td>
                        <div>filter outgoing/incoming route updates</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>As-path-list to filter</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_as</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>local as number not to be prepended to updates from EBGP peers</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maximum_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of prefixes to accept from this neighbor nexthop-self Nexthop for routes sent to this neighbor to be the local router.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nexthop_self</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Nexthop for routes sent to this neighbor to be the local router.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>override_capability</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Ignore capability negotiation with specified neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Do not initiate a session with this neighbor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP MD5 password</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>True if all the configs under this neighbor key is for peer group template.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_group_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 peer group for this peer</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Neighbor&#x27;s BGP port</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Prefix-list to filter route updates to/from this neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>export</li>
                                    <li>import</li>
                        </ul>
                </td>
                <td>
                        <div>filter outgoing/incoming route updates</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Prefix-list to filter</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_as</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Neighbor BGP AS number</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remove_private_as</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Remove private AS numbers from AS path in outbound route updates</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-map to filter route updates to/from this neighbor.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>export</li>
                                    <li>import</li>
                        </ul>
                </td>
                <td>
                        <div>filter outgoing/incoming route updates</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>route-map to filter</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_reflector_client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Neighbor as a route reflector client</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_server_client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Neighbor is route server client</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>shutdown</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Administratively shut down neighbor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>soft_reconfiguration</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Soft reconfiguration for neighbor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>strict_capability_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable strict capability negotiation</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Neighbor timers</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>connect</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP connect timer for this neighbor.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>holdtime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP hold timer for this neighbor</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>keepalive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP keepalive interval for this neighbor</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ttl_security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Ttl security mechanism for this BGP peer</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unsuppress_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-map to selectively unsuppress suppressed routes</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>update_source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source IP of routing updates</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Default weight for routes from this neighbor</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP network</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP network address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backdoor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Network as a backdoor route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route-map to modify route attributes</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>redistribute</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Redistribute routes from other protocols into BGP</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Metric for redistributed routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>connected</li>
                                    <li>kernel</li>
                                    <li>ospf</li>
                                    <li>rip</li>
                                    <li>static</li>
                        </ul>
                </td>
                <td>
                        <div>types of routes to be redistributed.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_map</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map to filter redistributed routes</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP protocol timers</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>holdtime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hold time interval</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>keepalive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Keepalive interval</div>
                </td>
            </tr>


            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option is used only with state <em>parsed</em>.</div>
                        <div>The value of this option should be the output received from the EOS device by executing the command <b>show running-config | section bgp</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>deleted</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>purged</li>
                                    <li>replaced</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                        <div>State <em>purged</em> removes all the BGP configurations from the target device. Use caution with this state.(&#x27;delete protocols bgp &lt;x&gt;&#x27;)</div>
                        <div>State <em>deleted</em> only removes BGP attributes that this modules manages and does not negate the BGP process completely. Thereby, preserving address-family related configurations under BGP context.</div>
                        <div>Running states <em>deleted</em> and <em>replaced</em> will result in an error if there are address-family configuration lines present under neighbor context that is is to be removed. Please use the  <span class='module'>vyos.vyos.vyos_bgp_address_family</span> module for prior cleanup.</div>
                        <div>Refer to examples for more details.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # vyos@vyos:~$

      - name: Merge provided configuration with device configuration
        vyos.vyos.vyos_bgp_global:
          config:
            as_number: "65536"
            aggregate_address:
              - prefix: "203.0.113.0/24"
                as_set: true
              - prefix: "192.0.2.0/24"
                summary_only: true
            network:
              - address: "192.1.13.0/24"
                backdoor: true
            redistribute:
              - protocol: "kernel"
                metric: 45
              - protocol: "connected"
                route_map: "map01"
            maximum_paths:
              - path: "ebgp"
                count: 20
              - path: "ibgp"
                count: 55
            timers:
              keepalive: 35
            bgp_params:
              bestpath:
                as_path: "confed"
                compare_routerid: true
              default:
                no_ipv4_unicast: true
              router_id: "192.1.2.9"
              confederation:
                - peers: 20
                - peers: 55
                - identifier: 66
            neighbor:
              - address: "192.0.2.25"
                disable_connected_check: true
                timers:
                  holdtime: 30
                  keepalive: 10
              - address: "203.0.113.5"
                attribute_unchanged:
                  as_path: true
                  med: true
                ebgp_multihop: 2
                remote_as: 101
                update_source: "192.0.2.25"
              - address: "5001::64"
                maximum_prefix: 34
                distribute_list:
                  - acl: 20
                    action: "export"
                  - acl: 40
                    action: "import"

          state: merged

    # After State
    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 aggregate-address 192.0.2.0/24 'summary-only'
    # set protocols bgp 65536 aggregate-address 203.0.113.0/24 'as-set'
    # set protocols bgp 65536 maximum-paths ebgp '20'
    # set protocols bgp 65536 maximum-paths ibgp '55'
    # set protocols bgp 65536 neighbor 192.0.2.25 'disable-connected-check'
    # set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime '30'
    # set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive '10'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'as-path'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'med'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'next-hop'
    # set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop '2'
    # set protocols bgp 65536 neighbor 203.0.113.5 remote-as '101'
    # set protocols bgp 65536 neighbor 203.0.113.5 update-source '192.0.2.25'
    # set protocols bgp 65536 neighbor 5001::64 distribute-list export '20'
    # set protocols bgp 65536 neighbor 5001::64 distribute-list import '40'
    # set protocols bgp 65536 neighbor 5001::64 maximum-prefix '34'
    # set protocols bgp 65536 network 192.1.13.0/24 'backdoor'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 parameters bestpath 'compare-routerid'
    # set protocols bgp 65536 parameters confederation identifier '66'
    # set protocols bgp 65536 parameters confederation peers '20'
    # set protocols bgp 65536 parameters confederation peers '55'
    # set protocols bgp 65536 parameters default 'no-ipv4-unicast'
    # set protocols bgp 65536 parameters router-id '192.1.2.9'
    # set protocols bgp 65536 redistribute connected route-map 'map01'
    # set protocols bgp 65536 redistribute kernel metric '45'
    # set protocols bgp 65536 timers keepalive '35'
    # vyos@vyos:~$
    #
    # # Module Execution:
    #
    # "after": {
    #         "aggregate_address": [
    #             {
    #                 "prefix": "192.0.2.0/24",
    #                 "summary_only": true
    #             },
    #             {
    #                 "prefix": "203.0.113.0/24",
    #                 "as_set": true
    #             }
    #         ],
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "bestpath": {
    #                 "as_path": "confed",
    #                 "compare_routerid": true
    #             },
    #             "confederation": [
    #                 {
    #                     "identifier": 66
    #                 },
    #                 {
    #                     "peers": 20
    #                 },
    #                 {
    #                     "peers": 55
    #                 }
    #             ],
    #             "default": {
    #                 "no_ipv4_unicast": true
    #             },
    #             "router_id": "192.1.2.9"
    #         },
    #         "maximum_paths": [
    #             {
    #                 "count": 20,
    #                 "path": "ebgp"
    #             },
    #             {
    #                 "count": 55,
    #                 "path": "ibgp"
    #             }
    #         ],
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.25",
    #                 "disable_connected_check": true,
    #                 "timers": {
    #                     "holdtime": 30,
    #                     "keepalive": 10
    #                 }
    #             },
    #             {
    #                 "address": "203.0.113.5",
    #                 "attribute_unchanged": {
    #                     "as_path": true,
    #                     "med": true,
    #                     "next_hop": true
    #                 },
    #                 "ebgp_multihop": 2,
    #                 "remote_as": 101,
    #                 "update_source": "192.0.2.25"
    #             },
    #             {
    #                 "address": "5001::64",
    #                 "distribute_list": [
    #                     {
    #                         "acl": 20,
    #                         "action": "export"
    #                     },
    #                     {
    #                         "acl": 40,
    #                         "action": "import"
    #                     }
    #                 ],
    #                 "maximum_prefix": 34
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "192.1.13.0/24",
    #                 "backdoor": true
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "connected",
    #                 "route_map": "map01"
    #             },
    #             {
    #                 "metric": 45,
    #                 "protocol": "kernel"
    #             }
    #         ],
    #         "timers": {
    #             "keepalive": 35
    #         }
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "set protocols bgp 65536 neighbor 192.0.2.25 disable-connected-check",
    #         "set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime 30",
    #         "set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive 10",
    #         "set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged as-path",
    #         "set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged med",
    #         "set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged next-hop",
    #         "set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop 2",
    #         "set protocols bgp 65536 neighbor 203.0.113.5 remote-as 101",
    #         "set protocols bgp 65536 neighbor 203.0.113.5 update-source 192.0.2.25",
    #         "set protocols bgp 65536 neighbor 5001::64 maximum-prefix 34",
    #         "set protocols bgp 65536 neighbor 5001::64 distribute-list export 20",
    #         "set protocols bgp 65536 neighbor 5001::64 distribute-list import 40",
    #         "set protocols bgp 65536 redistribute kernel metric 45",
    #         "set protocols bgp 65536 redistribute connected route-map map01",
    #         "set protocols bgp 65536 network 192.1.13.0/24 backdoor",
    #         "set protocols bgp 65536 aggregate-address 203.0.113.0/24 as-set",
    #         "set protocols bgp 65536 aggregate-address 192.0.2.0/24 summary-only",
    #         "set protocols bgp 65536 parameters bestpath as-path confed",
    #         "set protocols bgp 65536 parameters bestpath compare-routerid",
    #         "set protocols bgp 65536 parameters default no-ipv4-unicast",
    #         "set protocols bgp 65536 parameters router-id 192.1.2.9",
    #         "set protocols bgp 65536 parameters confederation peers 20",
    #         "set protocols bgp 65536 parameters confederation peers 55",
    #         "set protocols bgp 65536 parameters confederation identifier 66",
    #         "set protocols bgp 65536 maximum-paths ebgp 20",
    #         "set protocols bgp 65536 maximum-paths ibgp 55",
    #         "set protocols bgp 65536 timers keepalive 35"
    #     ],

    # Using replaced:
    # --------------

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 aggregate-address 192.0.2.0/24 'summary-only'
    # set protocols bgp 65536 aggregate-address 203.0.113.0/24 'as-set'
    # set protocols bgp 65536 maximum-paths ebgp '20'
    # set protocols bgp 65536 maximum-paths ibgp '55'
    # set protocols bgp 65536 neighbor 192.0.2.25 'disable-connected-check'
    # set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime '30'
    # set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive '10'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'as-path'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'med'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'next-hop'
    # set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop '2'
    # set protocols bgp 65536 neighbor 203.0.113.5 remote-as '101'
    # set protocols bgp 65536 neighbor 203.0.113.5 update-source '192.0.2.25'
    # set protocols bgp 65536 neighbor 5001::64 distribute-list export '20'
    # set protocols bgp 65536 neighbor 5001::64 distribute-list import '40'
    # set protocols bgp 65536 neighbor 5001::64 maximum-prefix '34'
    # set protocols bgp 65536 network 192.1.13.0/24 'backdoor'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 parameters bestpath 'compare-routerid'
    # set protocols bgp 65536 parameters confederation identifier '66'
    # set protocols bgp 65536 parameters confederation peers '20'
    # set protocols bgp 65536 parameters confederation peers '55'
    # set protocols bgp 65536 parameters default 'no-ipv4-unicast'
    # set protocols bgp 65536 parameters router-id '192.1.2.9'
    # set protocols bgp 65536 redistribute connected route-map 'map01'
    # set protocols bgp 65536 redistribute kernel metric '45'
    # set protocols bgp 65536 timers keepalive '35'
    # vyos@vyos:~$

      - name: Replace
        vyos.vyos.vyos_bgp_global:
          config:
            as_number: "65536"
            network:
              - address: "203.0.113.0/24"
                route_map: map01
            redistribute:
              - protocol: "static"
                route_map: "map01"
            neighbor:
              - address: "192.0.2.40"
                advertisement_interval: 72
                capability:
                  orf: "receive"
            bgp_params:
              bestpath:
                as_path: "confed"

          state: replaced
    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 neighbor 192.0.2.40 advertisement-interval '72'
    # set protocols bgp 65536 neighbor 192.0.2.40 capability orf prefix-list 'receive'
    # set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 redistribute static route-map 'map01'
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": {
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "bestpath": {
    #                 "as_path": "confed"
    #             }
    #         },
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.40",
    #                 "advertisement_interval": 72,
    #                 "capability": {
    #                     "orf": "receive"
    #                 }
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "203.0.113.0/24",
    #                 "route_map": "map01"
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "static",
    #                 "route_map": "map01"
    #             }
    #         ]
    #     },
    #     "before": {
    #         "aggregate_address": [
    #             {
    #                 "prefix": "192.0.2.0/24",
    #                 "summary_only": true
    #             },
    #             {
    #                 "prefix": "203.0.113.0/24",
    #                 "as_set": true
    #             }
    #         ],
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "bestpath": {
    #                 "as_path": "confed",
    #                 "compare_routerid": true
    #             },
    #             "confederation": [
    #                 {
    #                     "identifier": 66
    #                 },
    #                 {
    #                     "peers": 20
    #                 },
    #                 {
    #                     "peers": 55
    #                 }
    #             ],
    #             "default": {
    #                 "no_ipv4_unicast": true
    #             },
    #             "router_id": "192.1.2.9"
    #         },
    #         "maximum_paths": [
    #             {
    #                 "count": 20,
    #                 "path": "ebgp"
    #             },
    #             {
    #                 "count": 55,
    #                 "path": "ibgp"
    #             }
    #         ],
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.25",
    #                 "disable_connected_check": true,
    #                 "timers": {
    #                     "holdtime": 30,
    #                     "keepalive": 10
    #                 }
    #             },
    #             {
    #                 "address": "203.0.113.5",
    #                 "attribute_unchanged": {
    #                     "as_path": true,
    #                     "med": true,
    #                     "next_hop": true
    #                 },
    #                 "ebgp_multihop": 2,
    #                 "remote_as": 101,
    #                 "update_source": "192.0.2.25"
    #             },
    #             {
    #                 "address": "5001::64",
    #                 "distribute_list": [
    #                     {
    #                         "acl": 20,
    #                         "action": "export"
    #                     },
    #                     {
    #                         "acl": 40,
    #                         "action": "import"
    #                     }
    #                 ],
    #                 "maximum_prefix": 34
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "192.1.13.0/24",
    #                 "backdoor": true
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "connected",
    #                 "route_map": "map01"
    #             },
    #             {
    #                 "metric": 45,
    #                 "protocol": "kernel"
    #             }
    #         ],
    #         "timers": {
    #             "keepalive": 35
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete protocols bgp 65536 timers",
    #         "delete protocols bgp 65536 maximum-paths ",
    #         "delete protocols bgp 65536 maximum-paths ",
    #         "delete protocols bgp 65536 parameters router-id 192.1.2.9",
    #         "delete protocols bgp 65536 parameters default",
    #         "delete protocols bgp 65536 parameters confederation",
    #         "delete protocols bgp 65536 parameters bestpath compare-routerid",
    #         "delete protocols bgp 65536 aggregate-address",
    #         "delete protocols bgp 65536 network 192.1.13.0/24",
    #         "delete protocols bgp 65536 redistribute kernel",
    #         "delete protocols bgp 65536 redistribute kernel",
    #         "delete protocols bgp 65536 redistribute connected",
    #         "delete protocols bgp 65536 redistribute connected",
    #         "delete protocols bgp 65536 neighbor 5001::64",
    #         "delete protocols bgp 65536 neighbor 203.0.113.5",
    #         "delete protocols bgp 65536 neighbor 192.0.2.25",
    #         "set protocols bgp 65536 neighbor 192.0.2.40 advertisement-interval 72",
    #         "set protocols bgp 65536 neighbor 192.0.2.40 capability orf prefix-list receive",
    #         "set protocols bgp 65536 redistribute static route-map map01",
    #         "set protocols bgp 65536 network 203.0.113.0/24 route-map map01"
    #     ],

    # Using deleted:
    # -------------

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 neighbor 192.0.2.40 advertisement-interval '72'
    # set protocols bgp 65536 neighbor 192.0.2.40 capability orf prefix-list 'receive'
    # set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 redistribute static route-map 'map01'
    # vyos@vyos:~$

      - name: Delete configuration
        vyos.vyos.vyos_bgp_global:
          config:
            as_number: "65536"
          state: deleted

    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp '65536'
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": {
    #         "as_number": 65536
    #     },
    #     "before": {
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "bestpath": {
    #                 "as_path": "confed"
    #             }
    #         },
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.40",
    #                 "advertisement_interval": 72,
    #                 "capability": {
    #                     "orf": "receive"
    #                 }
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "203.0.113.0/24",
    #                 "route_map": "map01"
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "static",
    #                 "route_map": "map01"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete protocols bgp 65536 neighbor 192.0.2.40",
    #         "delete protocols bgp 65536 redistribute",
    #         "delete protocols bgp 65536 network",
    #         "delete protocols bgp 65536 parameters"
    #     ],

    # Using purged:

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 aggregate-address 192.0.2.0/24 'summary-only'
    # set protocols bgp 65536 aggregate-address 203.0.113.0/24 'as-set'
    # set protocols bgp 65536 maximum-paths ebgp '20'
    # set protocols bgp 65536 maximum-paths ibgp '55'
    # set protocols bgp 65536 neighbor 192.0.2.25 'disable-connected-check'
    # set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime '30'
    # set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive '10'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'as-path'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'med'
    # set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'next-hop'
    # set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop '2'
    # set protocols bgp 65536 neighbor 203.0.113.5 remote-as '101'
    # set protocols bgp 65536 neighbor 203.0.113.5 update-source '192.0.2.25'
    # set protocols bgp 65536 neighbor 5001::64 distribute-list export '20'
    # set protocols bgp 65536 neighbor 5001::64 distribute-list import '40'
    # set protocols bgp 65536 neighbor 5001::64 maximum-prefix '34'
    # set protocols bgp 65536 network 192.1.13.0/24 'backdoor'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 parameters bestpath 'compare-routerid'
    # set protocols bgp 65536 parameters confederation identifier '66'
    # set protocols bgp 65536 parameters confederation peers '20'
    # set protocols bgp 65536 parameters confederation peers '55'
    # set protocols bgp 65536 parameters default 'no-ipv4-unicast'
    # set protocols bgp 65536 parameters router-id '192.1.2.9'
    # set protocols bgp 65536 redistribute connected route-map 'map01'
    # set protocols bgp 65536 redistribute kernel metric '45'
    # set protocols bgp 65536 timers keepalive '35'
    # vyos@vyos:~$


      - name: Purge configuration
        vyos.vyos.vyos_bgp_global:
          config:
            as_number: "65536"
          state: purged

    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # vyos@vyos:~$
    #
    # Module Execution:
    #
    #     "after": {},
    #     "before": {
    #         "aggregate_address": [
    #             {
    #                 "prefix": "192.0.2.0/24",
    #                 "summary_only": true
    #             },
    #             {
    #                 "prefix": "203.0.113.0/24",
    #                 "as_set": true
    #             }
    #         ],
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "bestpath": {
    #                 "as_path": "confed",
    #                 "compare_routerid": true
    #             },
    #             "confederation": [
    #                 {
    #                     "identifier": 66
    #                 },
    #                 {
    #                     "peers": 20
    #                 },
    #                 {
    #                     "peers": 55
    #                 }
    #             ],
    #             "default": {
    #                 "no_ipv4_unicast": true
    #             },
    #             "router_id": "192.1.2.9"
    #         },
    #         "maximum_paths": [
    #             {
    #                 "count": 20,
    #                 "path": "ebgp"
    #             },
    #             {
    #                 "count": 55,
    #                 "path": "ibgp"
    #             }
    #         ],
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.25",
    #                 "disable_connected_check": true,
    #                 "timers": {
    #                     "holdtime": 30,
    #                     "keepalive": 10
    #                 }
    #             },
    #             {
    #                 "address": "203.0.113.5",
    #                 "attribute_unchanged": {
    #                     "as_path": true,
    #                     "med": true,
    #                     "next_hop": true
    #                 },
    #                 "ebgp_multihop": 2,
    #                 "remote_as": 101,
    #                 "update_source": "192.0.2.25"
    #             },
    #             {
    #                 "address": "5001::64",
    #                 "distribute_list": [
    #                     {
    #                         "acl": 20,
    #                         "action": "export"
    #                     },
    #                     {
    #                         "acl": 40,
    #                         "action": "import"
    #                     }
    #                 ],
    #                 "maximum_prefix": 34
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "192.1.13.0/24",
    #                 "backdoor": true
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "connected",
    #                 "route_map": "map01"
    #             },
    #             {
    #                 "metric": 45,
    #                 "protocol": "kernel"
    #             }
    #         ],
    #         "timers": {
    #             "keepalive": 35
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete protocols bgp 65536"
    #     ],


    # Deleted in presence of address family under neighbors:

    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval '72'
    # set protocols bgp 65536 neighbor 192.0.2.43 capability 'dynamic'
    # set protocols bgp 65536 neighbor 192.0.2.43 'disable-connected-check'
    # set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime '30'
    # set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive '10'
    # set protocols bgp 65536 neighbor 203.0.113.0 address-family 'ipv6-unicast'
    # set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list 'receive'
    # set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp 65536 parameters 'always-compare-med'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 parameters bestpath 'compare-routerid'
    # set protocols bgp 65536 parameters dampening half-life '33'
    # set protocols bgp 65536 parameters dampening max-suppress-time '20'
    # set protocols bgp 65536 parameters dampening re-use '60'
    # set protocols bgp 65536 parameters dampening start-suppress-time '5'
    # set protocols bgp 65536 parameters default 'no-ipv4-unicast'
    # set protocols bgp 65536 parameters distance global external '66'
    # set protocols bgp 65536 parameters distance global internal '20'
    # set protocols bgp 65536 parameters distance global local '10'
    # set protocols bgp 65536 redistribute static route-map 'map01'
    # vyos@vyos:~$ ^C
    # vyos@vyos:~$


      - name: Delete configuration
        vyos.vyos.vyos_bgp_global:
          config:
            as_number: "65536"
          state: deleted

    # Module Execution:
    #
    # "changed": false,
    #     "invocation": {
    #         "module_args": {
    #             "config": {
    #                 "aggregate_address": null,
    #                 "as_number": 65536,
    #                 "bgp_params": null,
    #                 "maximum_paths": null,
    #                 "neighbor": null,
    #                 "network": null,
    #                 "redistribute": null,
    #                 "timers": null
    #             },
    #             "running_config": null,
    #             "state": "deleted"
    #         }
    #     },
    #     "msg": "Use the _bgp_address_family module to delete the address_family under neighbor 203.0.113.0, before replacing/deleting the neighbor."
    # }

    # using gathered:
    # --------------

    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval '72'
    # set protocols bgp 65536 neighbor 192.0.2.43 capability 'dynamic'
    # set protocols bgp 65536 neighbor 192.0.2.43 'disable-connected-check'
    # set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime '30'
    # set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive '10'
    # set protocols bgp 65536 neighbor 203.0.113.0 address-family 'ipv6-unicast'
    # set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list 'receive'
    # set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp 65536 parameters 'always-compare-med'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 parameters bestpath 'compare-routerid'
    # set protocols bgp 65536 parameters dampening half-life '33'
    # set protocols bgp 65536 parameters dampening max-suppress-time '20'
    # set protocols bgp 65536 parameters dampening re-use '60'
    # set protocols bgp 65536 parameters dampening start-suppress-time '5'
    # set protocols bgp 65536 parameters default 'no-ipv4-unicast'
    # set protocols bgp 65536 parameters distance global external '66'
    # set protocols bgp 65536 parameters distance global internal '20'
    # set protocols bgp 65536 parameters distance global local '10'
    # set protocols bgp 65536 redistribute static route-map 'map01'
    # vyos@vyos:~$ ^C

      - name: gather configs
        vyos.vyos.vyos_bgp_global:
          state: gathered

    # Module Execution:
    # "gathered": {
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "always_compare_med": true,
    #             "bestpath": {
    #                 "as_path": "confed",
    #                 "compare_routerid": true
    #             },
    #             "default": {
    #                 "no_ipv4_unicast": true
    #             },
    #             "distance": [
    #                 {
    #                     "type": "external",
    #                     "value": 66
    #                 },
    #                 {
    #                     "type": "internal",
    #                     "value": 20
    #                 },
    #                 {
    #                     "type": "local",
    #                     "value": 10
    #                 }
    #             ]
    #         },
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.43",
    #                 "advertisement_interval": 72,
    #                 "capability": {
    #                     "dynamic": true
    #                 },
    #                 "disable_connected_check": true,
    #                 "timers": {
    #                     "holdtime": 30,
    #                     "keepalive": 10
    #                 }
    #             },
    #             {
    #                 "address": "203.0.113.0",
    #                 "capability": {
    #                     "orf": "receive"
    #                 }
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "203.0.113.0/24",
    #                 "route_map": "map01"
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "static",
    #                 "route_map": "map01"
    #             }
    #         ]
    #     },
    #

    # Using parsed:
    # ------------

    # parsed.cfg

    # set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval '72'
    # set protocols bgp 65536 neighbor 192.0.2.43 capability 'dynamic'
    # set protocols bgp 65536 neighbor 192.0.2.43 'disable-connected-check'
    # set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime '30'
    # set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive '10'
    # set protocols bgp 65536 neighbor 203.0.113.0 address-family 'ipv6-unicast'
    # set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list 'receive'
    # set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp 65536 parameters 'always-compare-med'
    # set protocols bgp 65536 parameters bestpath as-path 'confed'
    # set protocols bgp 65536 parameters bestpath 'compare-routerid'
    # set protocols bgp 65536 parameters dampening half-life '33'
    # set protocols bgp 65536 parameters dampening max-suppress-time '20'
    # set protocols bgp 65536 parameters dampening re-use '60'
    # set protocols bgp 65536 parameters dampening start-suppress-time '5'
    # set protocols bgp 65536 parameters default 'no-ipv4-unicast'
    # set protocols bgp 65536 parameters distance global external '66'
    # set protocols bgp 65536 parameters distance global internal '20'
    # set protocols bgp 65536 parameters distance global local '10'
    # set protocols bgp 65536 redistribute static route-map 'map01'

      - name: parse configs
        vyos.vyos.vyos_bgp_global:
          running_config: "{{ lookup('file', './parsed.cfg') }}"
          state: parsed
        tags:
          - parsed

    # Module execution:
    # "parsed": {
    #         "as_number": 65536,
    #         "bgp_params": {
    #             "always_compare_med": true,
    #             "bestpath": {
    #                 "as_path": "confed",
    #                 "compare_routerid": true
    #             },
    #             "default": {
    #                 "no_ipv4_unicast": true
    #             },
    #             "distance": [
    #                 {
    #                     "type": "external",
    #                     "value": 66
    #                 },
    #                 {
    #                     "type": "internal",
    #                     "value": 20
    #                 },
    #                 {
    #                     "type": "local",
    #                     "value": 10
    #                 }
    #             ]
    #         },
    #         "neighbor": [
    #             {
    #                 "address": "192.0.2.43",
    #                 "advertisement_interval": 72,
    #                 "capability": {
    #                     "dynamic": true
    #                 },
    #                 "disable_connected_check": true,
    #                 "timers": {
    #                     "holdtime": 30,
    #                     "keepalive": 10
    #                 }
    #             },
    #             {
    #                 "address": "203.0.113.0",
    #                 "capability": {
    #                     "orf": "receive"
    #                 }
    #             }
    #         ],
    #         "network": [
    #             {
    #                 "address": "203.0.113.0/24",
    #                 "route_map": "map01"
    #             }
    #         ],
    #         "redistribute": [
    #             {
    #                 "protocol": "static",
    #                 "route_map": "map01"
    #             }
    #         ]
    #     }
    #

    # Using rendered:
    # --------------

      - name: Render
        vyos.vyos.vyos_bgp_global:
          config:
            as_number: "65536"
            network:
              - address: "203.0.113.0/24"
                route_map: map01
            redistribute:
              - protocol: "static"
                route_map: "map01"
            bgp_params:
              always_compare_med: true
              dampening:
                start_suppress_time: 5
                max_suppress_time: 20
                half_life: 33
                re_use: 60
              distance:
                - type: "internal"
                  value: 20
                - type: "local"
                  value: 10
                - type: "external"
                  value: 66
              bestpath:
                as_path: "confed"
                compare_routerid: true
              default:
                no_ipv4_unicast: true
            neighbor:
              - address: "192.0.2.43"
                disable_connected_check: true
                advertisement_interval: 72
                capability:
                  dynamic: true
                timers:
                  holdtime: 30
                  keepalive: 10
              - address: "203.0.113.0"
                capability:
                  orf: "receive"

          state: rendered

    # Module Execution:
    # "rendered": [
    #         "set protocols bgp 65536 neighbor 192.0.2.43 disable-connected-check",
    #         "set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval 72",
    #         "set protocols bgp 65536 neighbor 192.0.2.43 capability dynamic",
    #         "set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime 30",
    #         "set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive 10",
    #         "set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list receive",
    #         "set protocols bgp 65536 redistribute static route-map map01",
    #         "set protocols bgp 65536 network 203.0.113.0/24 route-map map01",
    #         "set protocols bgp 65536 parameters always-compare-med",
    #         "set protocols bgp 65536 parameters dampening half-life 33",
    #         "set protocols bgp 65536 parameters dampening max-suppress-time 20",
    #         "set protocols bgp 65536 parameters dampening re-use 60",
    #         "set protocols bgp 65536 parameters dampening start-suppress-time 5",
    #         "set protocols bgp 65536 parameters distance global internal 20",
    #         "set protocols bgp 65536 parameters distance global local 10",
    #         "set protocols bgp 65536 parameters distance global external 66",
    #         "set protocols bgp 65536 parameters bestpath as-path confed",
    #         "set protocols bgp 65536 parameters bestpath compare-routerid",
    #         "set protocols bgp 65536 parameters default no-ipv4-unicast"
    #     ]




Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
