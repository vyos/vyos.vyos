.. _vyos.vyos.vyos_bgp_address_family_module:


*********************************
vyos.vyos.vyos_bgp_address_family
*********************************

**BGP Address Family Resource Module.**


Version added: 2.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages BGP address family configuration of interfaces on devices running VYOS.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
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
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP address-family parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>BGP address family settings.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>networks</b>
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
                        <div>Network as a backdoor route.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AS path hop count limit</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>BGP network address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                                    <li>ospfv3</li>
                                    <li>rip</li>
                                    <li>ripng</li>
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
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>table</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Redistribute non-main Kernel Routing Table.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neighbors</b>
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
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_family</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>address family.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>BGP neighbor parameters.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>as_path attribute</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>med attribute</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>next_hop attribute</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nexthop_local</b>
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
                        <div>Nexthop attributes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_group</b>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unsupress_map</b>
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
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>neighbor_address</b>
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
                <td colspan="5">
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
                        <div>The value of this option should be the output received from the VYOS device by executing the command <b>show configuration command | match bgp</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                                    <li>rendered</li>
                                    <li>purged</li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
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
      vyos.vyos.vyos_bgp_address_family:
        config:
          as_number: "100"
          address_family:
            - afi: "ipv4"
              redistribute:
                - protocol: "static"
                  metric: 50
          neighbors:
            - neighbor_address: "20.33.1.1/24"
              address_family:
                - afi: "ipv4"
                  allowas_in: 4
                  as_override: true
                  attribute_unchanged:
                    med: true
                - afi: "ipv6"
                  default_originate: "map01"
                  distribute_list:
                    - action: "export"
                      acl: 10
            - neighbor_address: "100.11.34.12"
              address_family:
                - afi: "ipv4"
                  maximum_prefix: 45
                  nexthop_self: true
                  route_map:
                    - action: "export"
                      route_map: "map01"
                    - action: "import"
                      route_map: "map01"
                  weight: 50

    # After State:
    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map 'map01'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export '10'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast weight '50'
    # vyos@vyos:~$
    #
    # Module Execution:
    #
    # "after": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true,
    #                         "route_map": [
    #                             {
    #                                 "action": "export",
    #                                 "route_map": "map01"
    #                             },
    #                             {
    #                                 "action": "import",
    #                                 "route_map": "map01"
    #                             }
    #                         ],
    #                         "weight": 50
    #                     }
    #                 ],
    #                 "neighbor_address": "100.11.34.12"
    #             },
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "default_originate": "map01",
    #                         "distribute_list": [
    #                             {
    #                                 "acl": 10,
    #                                 "action": "export"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "set protocols bgp 100 address-family ipv4-unicast redistribute static metric 50",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number 4",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast as-override",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map map01",
    #         "set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export 10",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix 45",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self",
    #         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export map01",
    #         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import map01",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast weight 50"
    #     ],
    #

    # Using replaced:

    # Before state:

    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map 'map01'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export '10'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast weight '50'
    # vyos@vyos:~$

    - name: Replace provided configuration with device configuration
      vyos.vyos.vyos_bgp_address_family:
        config:
          as_number: "100"
          neighbors:
            - neighbor_address: "100.11.34.12"
              address_family:
                - afi: "ipv4"
                  allowas_in: 4
                  as_override: true
                  attribute_unchanged:
                    med: true
                - afi: "ipv6"
                  default_originate: "map01"
                  distribute_list:
                    - action: "export"
                      acl: 10
            - neighbor_address: "20.33.1.1/24"
              address_family:
                - afi: "ipv6"
                  maximum_prefix: 45
                  nexthop_self: true
        state: replaced

    # After State:
    #
    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast default-originate route-map 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast distribute-list export '10'
    # vyos@vyos:~$
    #
    #
    # # Module Execution:
    # "after": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "default_originate": "map01",
    #                         "distribute_list": [
    #                             {
    #                                 "acl": 10,
    #                                 "action": "export"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "100.11.34.12"
    #             },
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4"
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]
    #     },
    #     "before": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true,
    #                         "route_map": [
    #                             {
    #                                 "action": "export",
    #                                 "route_map": "map01"
    #                             },
    #                             {
    #                                 "action": "import",
    #                                 "route_map": "map01"
    #                             }
    #                         ],
    #                         "weight": 50
    #                     }
    #                 ],
    #                 "neighbor_address": "100.11.34.12"
    #             },
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "default_originate": "map01",
    #                         "distribute_list": [
    #                             {
    #                                 "acl": 10,
    #                                 "action": "export"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list",
    #         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate",
    #         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged",
    #         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast as-override",
    #         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast weight",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast route-map",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast allowas-in number 4",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast as-override",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged med",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast default-originate route-map map01",
    #         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast distribute-list export 10",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast maximum-prefix 45",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast nexthop-self"
    #     ],


    # Using overridden
    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast network 35.1.1.0/24 backdoor
    # set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
    # set protocols bgp 100 address-family ipv6-unicast aggregate-address 6601:1:1:1::/64 summary-only
    # set protocols bgp 100 address-family ipv6-unicast network 5001:1:1:1::/64 route-map 'map01'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast default-originate route-map 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast distribute-list export '10'
    # vyos@vyos:~$

    - name: Override
      vyos.vyos.vyos_bgp_address_family:
        config:
          as_number: "100"
          neighbors:
            - neighbor_address: "100.11.34.12"
              address_family:
                - afi: "ipv6"
                  maximum_prefix: 45
                  nexthop_self: true
                  route_map:
                    - action: "import"
                      route_map: "map01"
          address_family:
            - afi: "ipv4"
              aggregate_address:
                - prefix: "60.9.2.0/24"
                  summary_only: true
            - afi: "ipv6"
              redistribute:
                - protocol: "static"
                  metric: 50
        state: overridden

    # After State

    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast aggregate-address 60.9.2.0/24 summary-only
    # set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast route-map import 'map01'
    # vyos@vyos:~$


    # Module Execution:

    # "after": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "aggregate_address": [
    #                     {
    #                         "prefix": "60.9.2.0/24",
    #                         "summary_only": true
    #                     }
    #                 ]
    #             },
    #             {
    #                 "afi": "ipv6",
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4"
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true,
    #                         "route_map": [
    #                             {
    #                                 "action": "import",
    #                                 "route_map": "map01"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "100.11.34.12"
    #             }
    #         ]
    #     },
    #     "before": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "networks": [
    #                     {
    #                         "backdoor": true,
    #                         "prefix": "35.1.1.0/24"
    #                     }
    #                 ],
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             },
    #             {
    #                 "afi": "ipv6",
    #                 "aggregate_address": [
    #                     {
    #                         "prefix": "6601:1:1:1::/64",
    #                         "summary_only": true
    #                     }
    #                 ],
    #                 "networks": [
    #                     {
    #                         "prefix": "5001:1:1:1::/64",
    #                         "route_map": "map01"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "default_originate": "map01",
    #                         "distribute_list": [
    #                             {
    #                                 "acl": 10,
    #                                 "action": "export"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "100.11.34.12"
    #             },
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4"
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete protocols bgp 100 neighbor 20.33.1.1/24 address-family",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast distribute-list",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast default-originate",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast as-override",
    #         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast allowas-in",
    #         "delete protocols bgp 100 address-family ipv6 aggregate-address",
    #         "delete protocols bgp 100 address-family ipv6 network",
    #         "delete protocols bgp 100 address-family ipv4 network",
    #         "delete protocols bgp 100 address-family ipv4 redistribute",
    #         "set protocols bgp 100 address-family ipv4-unicast aggregate-address 60.9.2.0/24 summary-only",
    #         "set protocols bgp 100 address-family ipv6-unicast redistribute static metric 50",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast maximum-prefix 45",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast nexthop-self",
    #         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast route-map import map01"
    #     ],
    #

    # Using deleted:

    # Before State:

    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast aggregate-address 60.9.2.0/24 summary-only
    # set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
    # set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map 'map01'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export '10'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import 'map01'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast weight '50'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast maximum-prefix '45'
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast nexthop-self
    # set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast route-map import 'map01'
    # vyos@vyos:~$

    - name: Delete
      vyos.vyos.vyos_bgp_address_family:
        config:
          as_number: "100"
          neighbors:
            - neighbor_address: "20.33.1.1/24"
              address_family:
                - afi: "ipv6"
            - neighbor_address: "100.11.34.12"
          address_family:
            - afi: "ipv4"
        state: deleted


    # After State:

    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 100.11.34.12
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv6",
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]
    #     },
    #     "before": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "aggregate_address": [
    #                     {
    #                         "prefix": "60.9.2.0/24",
    #                         "summary_only": true
    #                     }
    #                 ],
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             },
    #             {
    #                 "afi": "ipv6",
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true,
    #                         "route_map": [
    #                             {
    #                                 "action": "export",
    #                                 "route_map": "map01"
    #                             },
    #                             {
    #                                 "action": "import",
    #                                 "route_map": "map01"
    #                             }
    #                         ],
    #                         "weight": 50
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "maximum_prefix": 45,
    #                         "nexthop_self": true,
    #                         "route_map": [
    #                             {
    #                                 "action": "import",
    #                                 "route_map": "map01"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "100.11.34.12"
    #             },
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     },
    #                     {
    #                         "afi": "ipv6",
    #                         "default_originate": "map01",
    #                         "distribute_list": [
    #                             {
    #                                 "acl": 10,
    #                                 "action": "export"
    #                             }
    #                         ]
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete protocols bgp 100 address-family ipv4-unicast",
    #         "delete protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast",
    #         "delete protocols bgp 100 neighbor 100.11.34.12 address-family"
    #     ],
    #

    # using parsed:

    # parsed.cfg
    # set protocols bgp 65536 address-family ipv4-unicast aggregate-address 192.0.2.0/24 as-set
    # set protocols bgp 65536 address-family ipv4-unicast network 192.1.13.0/24 route-map 'map01'
    # set protocols bgp 65536 address-family ipv4-unicast network 192.2.13.0/24 backdoor
    # set protocols bgp 65536 address-family ipv6-unicast redistribute ripng metric '20'
    # set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast route-map export 'map01'
    # set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast soft-reconfiguration inbound
    # set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv6-unicast attribute-unchanged next-hop


    - name: parse configs
      vyos.vyos.vyos_bgp_address_family:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # Module execution result:
    #
    # "parsed": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "aggregate_address": [
    #                     {
    #                         "as_set": true,
    #                         "prefix": "192.0.2.0/24"
    #                     }
    #                 ],
    #                 "networks": [
    #                     {
    #                         "prefix": "192.1.13.0/24",
    #                         "route_map": "map01"
    #                     },
    #                     {
    #                         "backdoor": true,
    #                         "prefix": "192.2.13.0/24"
    #                     }
    #                 ]
    #             },
    #             {
    #                 "afi": "ipv6",
    #                 "redistribute": [
    #                     {
    #                         "metric": 20,
    #                         "protocol": "ripng"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 65536,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "route_map": [
    #                             {
    #                                 "action": "export",
    #                                 "route_map": "map01"
    #                             }
    #                         ],
    #                         "soft_reconfiguration": true
    #                     }
    #                 ],
    #                 "neighbor_address": "192.0.2.25"
    #             },
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv6",
    #                         "attribute_unchanged": {
    #                             "next_hop": true
    #                         }
    #                     }
    #                 ],
    #                 "neighbor_address": "203.0.113.5"
    #             }
    #         ]
    #

    # Using gathered:

    # Native config:

    # vyos@vyos:~$ show configuration commands | match "set protocols bgp"
    # set protocols bgp 100 address-family ipv4-unicast network 35.1.1.0/24 backdoor
    # set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
    # set protocols bgp 100 address-family ipv6-unicast aggregate-address 6601:1:1:1::/64 summary-only
    # set protocols bgp 100 address-family ipv6-unicast network 5001:1:1:1::/64 route-map 'map01'
    # set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
    # set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
    # set protocols bgp 100 neighbor 100.11.34.12

    - name: gather configs
      vyos.vyos.vyos_bgp_address_family:
        state: gathered

    # Module execution result:
    #
    # "gathered": {
    #         "address_family": [
    #             {
    #                 "afi": "ipv4",
    #                 "networks": [
    #                     {
    #                         "backdoor": true,
    #                         "prefix": "35.1.1.0/24"
    #                     }
    #                 ],
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             },
    #             {
    #                 "afi": "ipv6",
    #                 "aggregate_address": [
    #                     {
    #                         "prefix": "6601:1:1:1::/64",
    #                         "summary_only": true
    #                     }
    #                 ],
    #                 "networks": [
    #                     {
    #                         "prefix": "5001:1:1:1::/64",
    #                         "route_map": "map01"
    #                     }
    #                 ],
    #                 "redistribute": [
    #                     {
    #                         "metric": 50,
    #                         "protocol": "static"
    #                     }
    #                 ]
    #             }
    #         ],
    #         "as_number": 100,
    #         "neighbors": [
    #             {
    #                 "address_family": [
    #                     {
    #                         "afi": "ipv4",
    #                         "allowas_in": 4,
    #                         "as_override": true,
    #                         "attribute_unchanged": {
    #                             "med": true
    #                         }
    #                     }
    #                 ],
    #                 "neighbor_address": "20.33.1.1/24"
    #             }
    #         ]

    # Using rendered:

    - name: Render
      vyos.vyos.vyos_bgp_address_family:
        config:
          as_number: "100"
          address_family:
            - afi: "ipv4"
              redistribute:
                - protocol: "static"
                  metric: 50
          neighbors:
            - neighbor_address: "20.33.1.1/24"
              address_family:
                - afi: "ipv4"
                  allowas_in: 4
                  as_override: true
                  attribute_unchanged:
                    med: true
                - afi: "ipv6"
                  default_originate: "map01"
                  distribute_list:
                    - action: "export"
                      acl: 10
            - neighbor_address: "100.11.34.12"
              address_family:
                - afi: "ipv4"
                  maximum_prefix: 45
                  nexthop_self: true
                  route_map:
                    - action: "export"
                      route_map: "map01"
                    - action: "import"
                      route_map: "map01"
                  weight: 50
        state: rendered

    # Module Execution:

    # "rendered": [
    #         "set protocols bgp 100 address-family ipv4-unicast redistribute static metric 50",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number 4",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast as-override",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med",
    #         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map map01",
    #         "set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export 10",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix 45",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self",
    #         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export map01",
    #         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import map01",
    #         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast weight 50"
    #     ]




Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
