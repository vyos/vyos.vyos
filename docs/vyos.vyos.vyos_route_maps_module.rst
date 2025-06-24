.. _vyos.vyos.vyos_route_maps_module:


*************************
vyos.vyos.vyos_route_maps
*************************

**Route Map resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages route map configurations on devices running VYOS.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="6">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="6">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of route-map configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>entries</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route Map rules.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: rules</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>deny</li>
                                    <li>permit</li>
                        </ul>
                </td>
                <td>
                        <div>Action for matching routes</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>call</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>continue_sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Continue on a different entry within the route-map.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                        <div>Description for the rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route parameters to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set as-path.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP community attribute.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP community-list to match</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>exact_match</b>
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
                        <div>BGP community-list to match</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extcommunity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Extended community name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>First hop interface of a route to match.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP prefix parameters to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address of route to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>list_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>access-list</li>
                                    <li>prefix-list</li>
                        </ul>
                </td>
                <td>
                        <div>type of list</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>value of access-list and prefix list</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>next hop prefix list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>list_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>access-list</li>
                                    <li>prefix-list</li>
                        </ul>
                </td>
                <td>
                        <div>type of list</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>value of access-list and prefix list</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP route-source to match</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>list_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>access-list</li>
                                    <li>prefix-list</li>
                        </ul>
                </td>
                <td>
                        <div>type of list</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>value of access-list and prefix list</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 prefix parameters to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address of route to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>list_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>access-list</li>
                                    <li>prefix-list</li>
                        </ul>
                </td>
                <td>
                        <div>type of list</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>value of access-list and prefix list</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>next-hop ipv6 address IPv6 &lt;h:h:h:h:h:h:h:h&gt;.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>large_community_large_community_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP large-community-list to match.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Route metric &lt;1-65535&gt;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ebgp</li>
                                    <li>ibgp</li>
                                    <li>incomplete</li>
                        </ul>
                </td>
                <td>
                        <div>bgp origin.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Peer IP address &lt;x.x.x.x&gt;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>babel</li>
                                    <li>bgp</li>
                                    <li>connected</li>
                                    <li>isis</li>
                                    <li>kernel</li>
                                    <li>ospf</li>
                                    <li>ospfv3</li>
                                    <li>rip</li>
                                    <li>ripng</li>
                                    <li>static</li>
                                    <li>table</li>
                                    <li>vnc</li>
                        </ul>
                </td>
                <td>
                        <div>Source protocol to match.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rpki</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>notfound</li>
                                    <li>invalid</li>
                                    <li>valid</li>
                        </ul>
                </td>
                <td>
                        <div>RPKI validation value.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>on_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Exit policy on matches.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>goto</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Rule number to goto on match &lt;1-65535&gt;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next</b>
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
                        <div>Next sequence number to goto on match.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route map rule number &lt;1-65535&gt;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>set</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Route parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>aggregator</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Border Gateway Protocol (BGP) aggregator attribute.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AS number of an aggregation.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path_exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP AS path exclude string ex &quot;456 64500 45001&quot;</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>as_path_prepend</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Prepend string for a Border Gateway Protocol (BGP) AS-path attribute.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>atomic_aggregate</b>
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
                        <div>Border Gateway Protocol (BGP) atomic aggregate attribute.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bgp_extcommunity_rt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ExtCommunity in format AS:value</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>comm_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Border Gateway Protocol (BGP) communities matching a community-list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>comm_list</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>BGP communities with a community-list.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delete</b>
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
                        <div>Delete BGP communities matching the community-list.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Border Gateway Protocol (BGP) community attribute.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Community in 4 octet AS:value format or it can be from local-AS, no-advertise,no-expert,internet,additive,none.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extcommunity_bandwidth</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set Bandwidth of Origin value. 1-25600|cumulative|num-multipaths VPN extended community</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extcommunity_bandwidth_non_transitive</b>
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
                        <div>Set the bandwidth extended community encoded as non-transitive True/False VPN extended community</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extcommunity_rt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set route target value.ASN:nn_or_IP_address:nn VPN extended community.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>extcommunity_soo</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set Site of Origin value. ASN:nn_or_IP_address:nn VPN extended community</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6_next_hop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Nexthop IPv6 address.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>global</li>
                                    <li>local</li>
                        </ul>
                </td>
                <td>
                        <div>Global or Local</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ipv6 address</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>large_community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set BGP large community value.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_preference</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Border Gateway Protocol (BGP) local preference attribute.Example &lt;0-4294967295&gt;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination routing protocol metric. Example &lt;0-4294967295&gt;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>type-1</li>
                                    <li>type-2</li>
                        </ul>
                </td>
                <td>
                        <div>Open Shortest Path First (OSPF) external metric-type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>origin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>egp</li>
                                    <li>igp</li>
                                    <li>incomplete</li>
                        </ul>
                </td>
                <td>
                        <div>Set bgp origin.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>originator_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Border Gateway Protocol (BGP) originator ID attribute. Originator IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>src</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source address for route. Example &lt;x.x.x.x&gt; IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Set prefixes to table. Example &lt;1-200&gt;</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Tag value for routing protocol. Example &lt;1-65535&gt;</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>weight</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Border Gateway Protocol (BGP) weight attribute. Example &lt;0-4294967295&gt;</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                        <div>Route map name.</div>
                </td>
            </tr>

            <tr>
                <td colspan="6">
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
                        <div>The value of this option should be the output received from the VYOS device by executing the command <b>show configuration commands | grep route-map</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>show configuration commands | grep route-map</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="6">
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
                                    <li>overridden</li>
                                    <li>replaced</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025
   - This module works with connection ``network_cli``.



Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state

    # vyos@vyos:~$ show configuration commands |  match "set policy route-map"
    # vyos@vyos:~$
    - name: Merge the provided configuration with the existing running configuration
      register: result
      vyos.vyos.vyos_route_maps: &id001
        config:
          - route_map: test1
            entries:
              - sequence: 1
                description: "test"
                action: permit
                continue: 2
                on_match:
                  next: true
          - route_map: test3
            entries:
              - sequence: 1
                action: permit
                match:
                  rpki: invalid
                  metric: 1
                  peer: 192.0.2.32
                set:
                  local_preference: 4
                  metric: 5
                  metric_type: "type-1"
                  origin: egp
                  originator_id: 192.0.2.34
                  tag: 5
                  weight: 4
        state: merged
    # After State
    # vyos@vyos:~$ show configuration commands |  match "set policy route-maps"
    #   set policy route-map test1 rule 1 description test
    #   set policy route-map test1 rule 1 action permit
    #   set policy route-map test1 rule 1 continue 2
    #   set policy route-map test1 rule 1 on-match next
    #   set policy route-map test3 rule 1 action permit
    #   set policy route-map test3 rule 1 set local-preference 4
    #   set policy route-map test3 rule 1 set metric 5
    #   set policy route-map test3 rule 1 set metric-type type-1
    #   set policy route-map test3 rule 1 set origin egp
    #   set policy route-map test3 rule 1 set originator-id 192.0.2.34
    #   set policy route-map test3 rule 1 set tag 5
    #   set policy route-map test3 rule 1 set weight 4
    #   set policy route-map test3 rule 1 match metric 1
    #   set policy route-map test3 rule 1 match peer 192.0.2.32
    #   set policy route-map test3 rule 1 match rpki invalid

    # "after": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "continue_sequence": 2,
    #                     "description": "test",
    #                     "on_match": {
    #                         "next": true
    #                     },
    #                     "sequence": 1
    #                 }
    #             ],
    #             "route_map": "test1"
    #         },
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 1,
    #                         "peer": "192.0.2.32",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "local_preference": "4",
    #                         "metric": "5",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "5",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ],
    #     "before": [],
    #     "changed": true,
    #     "commands": [
    #         "set policy route-map test1 rule 1 description test",
    #         "set policy route-map test1 rule 1 action permit",
    #         "set policy route-map test1 rule 1 continue 2",
    #         "set policy route-map test1 rule 1 on-match next",
    #         "set policy route-map test3 rule 1 action permit",
    #         "set policy route-map test3 rule 1 set local-preference 4",
    #         "set policy route-map test3 rule 1 set metric 5",
    #         "set policy route-map test3 rule 1 set metric-type type-1",
    #         "set policy route-map test3 rule 1 set origin egp",
    #         "set policy route-map test3 rule 1 set originator-id 192.0.2.34",
    #         "set policy route-map test3 rule 1 set tag 5",
    #         "set policy route-map test3 rule 1 set weight 4",
    #         "set policy route-map test3 rule 1 match metric 1",
    #         "set policy route-map test3 rule 1 match peer 192.0.2.32",
    #         "set policy route-map test3 rule 1 match rpki invalid"
    #     ],

    # Using replaced:
    # --------------

    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set route-map policy"
    # set policy route-map test2 rule 1 action 'permit'
    # set policy route-map test2 rule 1 description 'test'
    # set policy route-map test2 rule 1 on-match next
    # set policy route-map test2 rule 2 action 'permit'
    # set policy route-map test2 rule 2 on-match goto '4'
    # set policy route-map test3 rule 1 action 'permit'
    # set policy route-map test3 rule 1 match metric '1'
    # set policy route-map test3 rule 1 match peer '192.0.2.32'
    # set policy route-map test3 rule 1 match rpki 'invalid'
    # set policy route-map test3 rule 1 set community 'internet'
    # set policy route-map test3 rule 1 set ip-next-hop '192.0.2.33'
    # set policy route-map test3 rule 1 set local-preference '4'
    # set policy route-map test3 rule 1 set metric '5'
    # set policy route-map test3 rule 1 set metric-type 'type-1'
    # set policy route-map test3 rule 1 set origin 'egp'
    # set policy route-map test3 rule 1 set originator-id '192.0.2.34'
    # set policy route-map test3 rule 1 set tag '5'
    # set policy route-map test3 rule 1 set weight '4'
    #
    #     - name: Replace  the provided configuration with the existing running configuration
    #       register: result
    #       vyos.vyos.vyos_route_maps: &id001
    #         config:
    #           - route_map: test3
    #             entries:
    #               - sequence: 1
    #                 action: permit
    #                 match:
    #                   rpki: invalid
    #                   metric: 3
    #                   peer: 192.0.2.35
    #                 set:
    #                   local_preference: 6
    #                   metric: 4
    #                   metric_type: "type-1"
    #                   origin: egp
    #                   originator_id: 192.0.2.34
    #                   tag: 4
    #                   weight: 4
    #         state: replaced
    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set policy route-map"
    # set policy route-map test3 rule 1 set local-preference 6
    # set policy route-map test3 rule 1 set metric 4
    # set policy route-map test3 rule 1 set tag 4
    # set policy route-map test3 rule 1 match metric 3
    # set policy route-map test3 rule 1 match peer 192.0.2.35
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "description": "test",
    #                     "on_match": {
    #                         "next": true
    #                     },
    #                     "sequence": 1
    #                 },
    #                 {
    #                     "action": "permit",
    #                     "on_match": {
    #                         "goto": 4
    #                     },
    #                     "sequence": 2
    #                 }
    #             ],
    #             "route_map": "test2"
    #         },
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 3,
    #                         "peer": "192.0.2.35",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "local_preference": "6",
    #                         "metric": "4",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "4",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ],
    #     "before": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "description": "test",
    #                     "on_match": {
    #                         "next": true
    #                     },
    #                     "sequence": 1
    #                 },
    #                 {
    #                     "action": "permit",
    #                     "on_match": {
    #                         "goto": 4
    #                     },
    #                     "sequence": 2
    #                 }
    #             ],
    #             "route_map": "test2"
    #         },
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 1,
    #                         "peer": "192.0.2.32",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "community": {
    #                             "value": "internet"
    #                         },
    #                         "ip_next_hop": "192.0.2.33",
    #                         "local_preference": "4",
    #                         "metric": "5",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "5",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy route-map test3 rule 1 set ip-next-hop 192.0.2.33",
    #         "set policy route-map test3 rule 1 set local-preference 6",
    #         "set policy route-map test3 rule 1 set metric 4",
    #         "set policy route-map test3 rule 1 set tag 4",
    #         "delete policy route-map test3 rule 1 set community internet",
    #         "set policy route-map test3 rule 1 match metric 3",
    #         "set policy route-map test3 rule 1 match peer 192.0.2.35"
    #     ],
    #
    # Using deleted:
    # -------------

    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set policy route-map"
    # set policy route-map test3 rule 1 set local-preference 6
    # set policy route-map test3 rule 1 set metric 4
    # set policy route-map test3 rule 1 set tag 4
    # set policy route-map test3 rule 1 match metric 3
    # set policy route-map test3 rule 1 match peer 192.0.2.35
    # vyos@vyos:~$
    #
    # - name: Delete the provided configuration
    #   register: result
    #   vyos.vyos.vyos_route_maps:
    #     config:
    #     state: deleted
    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set policy route-map"
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": [],
    #     "before": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 3,
    #                         "peer": "192.0.2.35",
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "local_preference": "6",
    #                         "metric": "4",
    #                         "tag": "4",
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy route-map test3"
    #     ],
    #
    # using gathered:
    # --------------
    #
    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set policy route-maps"
    #   set policy route-map test1 rule 1 description test
    #   set policy route-map test1 rule 1 action permit
    #   set policy route-map test1 rule 1 continue 2
    #   set policy route-map test1 rule 1 on-match next
    #   set policy route-map test3 rule 1 action permit
    #   set policy route-map test3 rule 1 set local-preference 4
    #   set policy route-map test3 rule 1 set metric 5
    #   set policy route-map test3 rule 1 set metric-type type-1
    #   set policy route-map test3 rule 1 set origin egp
    #   set policy route-map test3 rule 1 set originator-id 192.0.2.34
    #   set policy route-map test3 rule 1 set tag 5
    #   set policy route-map test3 rule 1 set weight 4
    #   set policy route-map test3 rule 1 match metric 1
    #   set policy route-map test3 rule 1 match peer 192.0.2.32
    #   set policy route-map test3 rule 1 match rpki invalid
    #
    # - name: gather configs
    #     vyos.vyos.vyos_route_maps:
    #       state: gathered

    # "gathered": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "continue_sequence": 2,
    #                     "description": "test",
    #                     "on_match": {
    #                         "next": true
    #                     },
    #                     "sequence": 1
    #                 }
    #             ],
    #             "route_map": "test1"
    #         },
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 1,
    #                         "peer": "192.0.2.32",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "local_preference": "4",
    #                         "metric": "5",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "5",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ]

    # Using parsed:
    # ------------

    # parsed.cfg
    # set policy route-map test1 rule 1 description test
    # set policy route-map test1 rule 1 action permit
    # set policy route-map test1 rule 1 continue 2
    # set policy route-map test1 rule 1 on-match next
    # set policy route-map test3 rule 1 action permit
    # set policy route-map test3 rule 1 set local-preference 4
    # set policy route-map test3 rule 1 set metric 5
    # set policy route-map test3 rule 1 set metric-type type-1
    # set policy route-map test3 rule 1 set origin egp
    # set policy route-map test3 rule 1 set originator-id 192.0.2.34
    # set policy route-map test3 rule 1 set tag 5
    # set policy route-map test3 rule 1 set weight 4
    # set policy route-map test3 rule 1 match metric 1
    # set policy route-map test3 rule 1 match peer 192.0.2.32
    # set policy route-map test3 rule 1 match rpki invalid
    #
    # - name: parse configs
    #   vyos.vyos.vyos_route_maps:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    #   tags:
    #     - parsed
    #
    # Module execution:
    # "parsed": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "continue_sequence": 2,
    #                     "description": "test",
    #                     "on_match": {
    #                         "next": true
    #                     },
    #                     "sequence": 1
    #                 }
    #             ],
    #             "route_map": "test1"
    #         },
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 1,
    #                         "peer": "192.0.2.32",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "local_preference": "4",
    #                         "metric": "5",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "5",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ]
    #
    #
    # Using rendered:
    # --------------
    # - name: Structure provided configuration into device specific commands
    #       register: result
    #       vyos.vyos.vyos_route_maps: &id001
    #         config:
    #           - route_map: test1
    #             entries:
    #               - sequence: 1
    #                 description: "test"
    #                 action: permit
    #                 continue_sequence: 2
    #                 on_match:
    #                   next: True
    #           - route_map: test3
    #             entries:
    #               - sequence: 1
    #                 action: permit
    #                 match:
    #                   rpki: invalid
    #                   metric: 1
    #                   peer: 192.0.2.32
    #                 set:
    #                   local_preference: 4
    #                   metric: 5
    #                   metric_type: "type-1"
    #                   origin: egp
    #                   originator_id: 192.0.2.34
    #                   tag: 5
    #                   weight: 4
    #         state: rendered
    # Module Execution:
    # "rendered": [
    #         "set policy route-map test1 rule 1 description test",
    #         "set policy route-map test1 rule 1 action permit",
    #         "set policy route-map test1 rule 1 continue 2",
    #         "set policy route-map test1 rule 1 on-match next",
    #         "set policy route-map test3 rule 1 action permit",
    #         "set policy route-map test3 rule 1 set local-preference 4",
    #         "set policy route-map test3 rule 1 set metric 5",
    #         "set policy route-map test3 rule 1 set metric-type type-1",
    #         "set policy route-map test3 rule 1 set origin egp",
    #         "set policy route-map test3 rule 1 set originator-id 192.0.2.34",
    #         "set policy route-map test3 rule 1 set tag 5",
    #         "set policy route-map test3 rule 1 set weight 4",
    #         "set policy route-map test3 rule 1 match metric 1",
    #         "set policy route-map test3 rule 1 match peer 192.0.2.32",
    #         "set policy route-map test3 rule 1 match rpki invalid"
    #     ]
    #
    #
    # Using overridden:
    # --------------
    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set policy route-map"
    # set policy route-map test2 rule 1 action 'permit'
    # set policy route-map test2 rule 1 description 'test'
    # set policy route-map test2 rule 1 on-match next
    # set policy route-map test2 rule 2 action 'permit'
    # set policy route-map test2 rule 2 on-match goto '4'
    # set policy route-map test3 rule 1 action 'permit'
    # set policy route-map test3 rule 1 match metric '1'
    # set policy route-map test3 rule 1 match peer '192.0.2.32'
    # set policy route-map test3 rule 1 match rpki 'invalid'
    # set policy route-map test3 rule 1 set community 'internet'
    # set policy route-map test3 rule 1 set ip-next-hop '192.0.2.33'
    # set policy route-map test3 rule 1 set local-preference '4'
    # set policy route-map test3 rule 1 set metric '5'
    # set policy route-map test3 rule 1 set metric-type 'type-1'
    # set policy route-map test3 rule 1 set origin 'egp'
    # set policy route-map test3 rule 1 set originator-id '192.0.2.34'
    # set policy route-map test3 rule 1 set tag '5'
    # set policy route-map test3 rule 1 set weight '4'
    #
    #     - name: Override the existing configuration with the provided running configuration
    #       register: result
    #       vyos.vyos.vyos_route_maps: &id001
    #         config:
    #           - route_map: test3
    #             entries:
    #               - sequence: 1
    #                 action: permit
    #                 match:
    #                   rpki: invalid
    #                   metric: 3
    #                   peer: 192.0.2.35
    #                 set:
    #                   local_preference: 6
    #                   metric: 4
    #                   metric_type: "type-1"
    #                   origin: egp
    #                   originator_id: 192.0.2.34
    #                   tag: 4
    #                   weight: 4
    #         state: overridden
    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set policy route-map"
    # set policy route-map test3 rule 1 set metric-type 'type-1'
    # set policy route-map test3 rule 1 set origin 'egp'
    # set policy route-map test3 rule 1 set originator-id '192.0.2.34'
    # set policy route-map test3 rule 1 set weight '4'
    # set policy route-map test3 rule 1 set local-preference 6
    # set policy route-map test3 rule 1 set metric 4
    # set policy route-map test3 rule 1 set tag 4
    # set policy route-map test3 rule 1 match metric 3
    # set policy route-map test3 rule 1 match peer 192.0.2.35
    # set policy route-map test3 rule 1 match rpki 'invalid'

    # Module Execution:
    # "after": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 3,
    #                         "peer": "192.0.2.35",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "local_preference": "6",
    #                         "metric": "4",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "4",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ],
    #     "before": [
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "description": "test",
    #                     "on_match": {
    #                         "next": true
    #                     },
    #                     "sequence": 1
    #                 },
    #                 {
    #                     "action": "permit",
    #                     "on_match": {
    #                         "goto": 4
    #                     },
    #                     "sequence": 2
    #                 }
    #             ],
    #             "route_map": "test2"
    #         },
    #         {
    #             "entries": [
    #                 {
    #                     "action": "permit",
    #                     "match": {
    #                         "metric": 1,
    #                         "peer": "192.0.2.32",
    #                         "rpki": "invalid"
    #                     },
    #                     "sequence": 1,
    #                     "set": {
    #                         "community": {
    #                             "value": "internet"
    #                         },
    #                         "ip_next_hop": "192.0.2.33",
    #                         "local_preference": "4",
    #                         "metric": "5",
    #                         "metric_type": "type-1",
    #                         "origin": "egp",
    #                         "originator_id": "192.0.2.34",
    #                         "tag": "5",
    #                         "weight": "4"
    #                     }
    #                 }
    #             ],
    #             "route_map": "test3"
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy route-map test2",
    #         "delete policy route-map test3 rule 1 set ip-next-hop 192.0.2.33",
    #         "set policy route-map test3 rule 1 set local-preference 6",
    #         "set policy route-map test3 rule 1 set metric 4",
    #         "set policy route-map test3 rule 1 set tag 4",
    #         "delete policy route-map test3 rule 1 set community internet",
    #         "set policy route-map test3 rule 1 match metric 3",
    #         "set policy route-map test3 rule 1 match peer 192.0.2.35"
    #     ],



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration after module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The configuration prior to the module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set policy route-map test3 rule 1 set local-preference 6&#x27;, &#x27;set policy route-map test3 rule 1 set metric 4&#x27;, &#x27;set policy route-map test3 rule 1 set tag 4&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>gathered</code></td>
                <td>
                            <div>Facts about the network resource gathered from the remote device as structured data.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>parsed</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>parsed</code></td>
                <td>
                            <div>The device native config provided in <em>running_config</em> option parsed into structured data as per module argspec.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>rendered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>rendered</code></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set policy route-map test3 rule 1 set local-preference 6&#x27;, &#x27;set policy route-map test3 rule 1 set metric 4&#x27;, &#x27;set policy route-map test3 rule 1 set tag 4&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)
