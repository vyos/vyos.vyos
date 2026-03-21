.. _vyos.vyos.vyos_ha_module:


*****************
vyos.vyos.vyos_ha
*****************

**Manage VRRP and load balancer configuration on VyOS**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures VRRP groups, global VRRP parameters, VRRP sync groups, and LVS-style virtual servers on VyOS 1.4+.
- Supports creation, modification, deletion, replacement, rendering, and parsing of VRRP-related configuration.




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
                        <div>Full VRRP and virtual server configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable all VRRP and L4-LB configuration under this module.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>virtual_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of load balancer virtual server (LVS) definitions.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Virtual IP address for the server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>algorithm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Load balancing algorithm used for dispatching connections.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delay_loop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Delay loop interval in seconds.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>forward_method</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>direct</li>
                                    <li>nat</li>
                        </ul>
                </td>
                <td>
                        <div>Forwarding method used by LVS.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fwmark</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Firewall mark for LVS traffic classification.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Unique identifier for the virtual server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>persistence_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Client persistence timeout in seconds.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>TCP/UDP port provided by the virtual service.</div>
                </td>
            </tr>
            <tr>
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
                                    <li>tcp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>Transport protocol for the virtual server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>real_server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Backend real servers behind the virtual service.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Real server IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>connection_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Backend server connection timeout.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>health_check_script</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to health check script used for backend validation.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Backend server port.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrrp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP configuration including groups, global parameters, SNMP settings, and sync-groups.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>global_parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Global VRRP tuning parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>garp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Gratuitous ARP related configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>GARP interval in seconds.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Delay before sending GARP as master.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_refresh</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Refresh interval for master GARP announcements.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_refresh_repeat</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of times to repeat refresh announcements.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_repeat</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of GARP repeats when transitioning to master.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>startup_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Delay before VRRP starts after boot.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP protocol version.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP instance configuration groups.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Virtual router IP address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP advertisement interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP group authentication options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Authentication password.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                </td>
                <td>
                        <div>Authentication type.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Text description for the VRRP group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable this VRRP group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>excluded_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address excluded from source checks.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>garp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>GARP-specific settings for this group.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>GARP interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>GARP master delay.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_refresh</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>GARP master refresh interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_refresh_repeat</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Repeated refresh sends.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master_repeat</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>GARP repeat count.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>health_check</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP group health check options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>failure_count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allowed number of failed checks.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Health check interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ping</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Host to ping for checks.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>script</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Script to execute for health checking.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hello_source_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source address for VRRP hello packets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Interface used by the VRRP group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP group name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>no_preempt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable preemption.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Peer VRRP router address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preempt_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Delay before taking master role.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP priority (higher = preferred master).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rfc3768_compatibility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable RFC3768 compatibility mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>track</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Track interface and VRRP behaviour.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>exclude_vrrp_interface</b>
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
                        <div>Exclude VRRP interface from tracking.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface to track.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transition_script</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Scripts executed during VRRP state transitions.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to backup script.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fault</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to fault script.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to master script.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to stop script.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP Virtual Router ID.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>snmp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Enable SNMP support for VRRP.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sync_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRRP sync-groups for coordinated failover.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>health_check</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Health check options for sync group.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>failure_count</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allowed number of failures.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Health check interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ping</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Host to ping.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>script</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Script to run for health checking.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>member</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of VRRP groups participating in this sync group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sync-group name.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transition_script</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Transition scripts for sync group events.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Backup state script.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fault</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Fault state script.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Master state script.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stop</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Stop state script.</div>
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
                        <div>Used only when <code>state=parsed</code>. Must contain the output of <code>show configuration commands | grep high-availability</code>.</div>
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
                                    <li>deleted</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>purged</li>
                                    <li>replaced</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                                    <li>overridden</li>
                        </ul>
                </td>
                <td>
                        <div>Desired end state of the VRRP configuration.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state

    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # vyos@vyos:~$

    - name: Merge provided configuration with device configuration
      vyos.vyos.vyos_ha:
        config:
          disable: true
          virtual_servers:
            - name: s1
              address: 10.10.10.5
              algorithm: round-robin
              real_server:
                - address: 10.10.50.2
                  port: 8443
            - name: s2
              address: 10.10.10.2
              persistence_timeout: 30
              port: 81
              protocol: tcp
            - name: s3
              address: 10.10.10.3
              port: 88
              protocol: udp
          vrrp:
            snmp: enabled
            global_parameters:
              startup_delay: 30
              garp:
                master_repeat: 6
            groups:
              - name: "g1"
                peer_address: 192.168.1.3
                priority: 100
                disable: false
                no_preempt: false
                vrid: 20
            sync_groups:
              - name: "sg1"
                health_check:
                  failure_count: 5
        state: merged

    # After State
    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # set high-availability disable
    # set high-availability virtual-server s1 address '10.10.10.5'
    # set high-availability virtual-server s1 algorithm 'round-robin'
    # set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '30'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp global-parameters startup-delay '30'
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '5'
    # vyos@vyos:~$
    #
    # # Module Execution:
    #
    # "after": {
    #     "disable": true,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.5",
    #             "algorithm": "round-robin",
    #             "name": "s1",
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.2",
    #                     "port": 8443
    #                 }
    #             ]
    #         },
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 30,
    #             "port": 81,
    #             "protocol": "tcp"
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp"
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             },
    #             "startup_delay": 30
    #         },
    #         "groups": [
    #             {
    #                 "disable": false,
    #                 "name": "g1",
    #                 "no_preempt": false,
    #                 "peer_address": "192.168.1.3",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 5
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    # "before": {
    #     "disable": false
    # },
    # "changed": true,
    # "commands": [
    #     "set high-availability disable",
    #     "set high-availability virtual-server s1 address 10.10.10.5",
    #     "set high-availability virtual-server s1 algorithm round-robin",
    #     "set high-availability virtual-server s1 real-server 10.10.50.2 port 8443",
    #     "set high-availability virtual-server s2 address 10.10.10.2",
    #     "set high-availability virtual-server s2 persistence-timeout 30",
    #     "set high-availability virtual-server s2 port 81",
    #     "set high-availability virtual-server s2 protocol tcp",
    #     "set high-availability virtual-server s3 address 10.10.10.3",
    #     "set high-availability virtual-server s3 port 88",
    #     "set high-availability virtual-server s3 protocol udp",
    #     "set high-availability vrrp global-parameters garp master-repeat 6",
    #     "set high-availability vrrp global-parameters startup-delay 30",
    #     "set high-availability vrrp group g1 peer-address 192.168.1.3",
    #     "set high-availability vrrp group g1 priority 100",
    #     "set high-availability vrrp group g1 vrid 20",
    #     "set high-availability vrrp snmp",
    #     "set high-availability vrrp sync-group sg1 health-check failure-count 5"
    # ],

    # Using replaced:
    # --------------

    # Before state:
    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # set high-availability disable
    # set high-availability virtual-server s1 address '10.10.10.5'
    # set high-availability virtual-server s1 algorithm 'round-robin'
    # set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '30'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp global-parameters startup-delay '30'
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '5'
    # vyos@vyos:~$

    - name: Replace
      vyos.vyos.vyos_ha:
        config:
          disable: false
          virtual_servers:
            - name: s1
              address: 10.10.10.3
              algorithm: round-robin
              port: 8443
              real_server:
                - address: 10.10.50.3
                  port: 8443
            - name: s2
              address: 10.10.10.2
              persistence_timeout: 300
              port: 81
              protocol: tcp
              real_server:
                - address: 10.10.50.30
                  port: 8443
            - name: s3
              address: 10.10.10.3
              port: 88
              protocol: udp
              real_server:
                - address: 10.10.50.6
                  port: 8443
          vrrp:
            snmp: enabled
            global_parameters:
              startup_delay: 30
              garp:
                master_repeat: 6
            groups:
              - name: "g1"
                peer_address: 192.168.1.13
                priority: 100
                disable: false
                no_preempt: true
                interface: eth1
                address: 192.168.51.13
                vrid: 20
            sync_groups:
              - name: "sg1"
                health_check:
                  failure_count: 3
        state: replaced

    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # set high-availability virtual-server s1 address '10.10.10.3'
    # set high-availability virtual-server s1 algorithm 'round-robin'
    # set high-availability virtual-server s1 port '8443'
    # set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
    # set high-availability virtual-server s1 real-server 10.10.50.3 port '8443'
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '300'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s2 real-server 10.10.50.3 port '8443'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability virtual-server s3 real-server 10.10.50.6 port '8443'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp global-parameters startup-delay '30'
    # set high-availability vrrp group g1 address 192.168.51.13
    # set high-availability vrrp group g1 interface 'eth1'
    # set high-availability vrrp group g1 no-preempt
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 peer-address '192.168.1.13'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '3'
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": {
    #     "disable": false,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.3",
    #             "algorithm": "round-robin",
    #             "name": "s1",
    #             "port": 8443,
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.2",
    #                     "port": 8443
    #                 },
    #                 {
    #                     "address": "10.10.50.3",
    #                     "port": 8443
    #                 }
    #             ]
    #         },
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 300,
    #             "port": 81,
    #             "protocol": "tcp",
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.3",
    #                     "port": 8443
    #                 }
    #             ]
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp",
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.6",
    #                     "port": 8443
    #                 }
    #             ]
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             },
    #             "startup_delay": 30
    #         },
    #         "groups": [
    #             {
    #                 "address": "192.168.51.13",
    #                 "disable": false,
    #                 "interface": "eth1",
    #                 "name": "g1",
    #                 "no_preempt": true,
    #                 "peer_address": "192.168.1.13",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 3
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    # "before": {
    #     "disable": true,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.5",
    #             "algorithm": "round-robin",
    #             "name": "s1",
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.2",
    #                     "port": 8443
    #                 }
    #             ]
    #         },
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 30,
    #             "port": 81,
    #             "protocol": "tcp"
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp"
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             },
    #             "startup_delay": 30
    #         },
    #         "groups": [
    #             {
    #                 "disable": false,
    #                 "name": "g1",
    #                 "no_preempt": false,
    #                 "peer_address": "192.168.1.3",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 5
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    # "changed": true,
    # "commands": [
    #     "delete high-availability disable",
    #     "set high-availability virtual-server s1 address 10.10.10.3",
    #     "set high-availability virtual-server s1 port 8443",
    #     "set high-availability virtual-server s1 real-server 10.10.50.3 port 8443",
    #     "set high-availability virtual-server s2 persistence-timeout 300",
    #     "set high-availability virtual-server s2 real-server 10.10.50.3 port 8443",
    #     "set high-availability virtual-server s3 real-server 10.10.50.6 port 8443",
    #     "set high-availability vrrp group g1 address 192.168.51.13",
    #     "set high-availability vrrp group g1 interface eth1",
    #     "set high-availability vrrp group g1 no-preempt",
    #     "set high-availability vrrp group g1 peer-address 192.168.1.13",
    #     "set high-availability vrrp sync-group sg1 health-check failure-count 3"
    # ],

    # Using deleted:
    # -------------

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # set high-availability disable
    # set high-availability virtual-server s1 address '10.10.10.5'
    # set high-availability virtual-server s1 algorithm 'round-robin'
    # set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '30'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp global-parameters startup-delay '30'
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '5'
    # vyos@vyos:~$

    - name: Delete configuration
      vyos.vyos.vyos_ha:
        config:
          disable: false
          vrrp:
            snmp: disabled
            global_parameters:
              startup_delay: 32
              version: 3
          virtual_servers:
            - name: 's1'
              address: '10.10.10.1'
              algorithm: 'round-robin'
              delay_loop: 60
              forward_method: 'direct'
              persistence_timeout: 30
              port: 443
              protocol: 'tcp'
              real_server:
                - address: '10.10.10.1'
                  connection_timeout: 61
                  port: 443
        state: deleted

    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # set high-availability disable
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '30'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '5'

    # vyos@vyos:~$
    #
    #
    # Module Execution:
    #
    # "after": {
    #     "disable": true,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 30,
    #             "port": 81,
    #             "protocol": "tcp"
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp"
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             }
    #         },
    #         "groups": [
    #             {
    #                 "disable": false,
    #                 "name": "g1",
    #                 "no_preempt": false,
    #                 "peer_address": "192.168.1.3",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 5
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    # "before": {
    #     "disable": true,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.5",
    #             "algorithm": "round-robin",
    #             "name": "s1",
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.2",
    #                     "port": 8443
    #                 }
    #             ]
    #         },
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 30,
    #             "port": 81,
    #             "protocol": "tcp"
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp"
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             },
    #             "startup_delay": 30
    #         },
    #         "groups": [
    #             {
    #                 "disable": false,
    #                 "name": "g1",
    #                 "no_preempt": false,
    #                 "peer_address": "192.168.1.3",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 5
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    # "changed": true,
    # "commands": [
    #     "delete high-availability virtual-server s1",
    #     "delete high-availability vrrp global-parameters startup-delay"
    # ],

    # Using purged:

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # set high-availability disable
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '30'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '5'
    # vyos@vyos:~$


    - name: Purge configuration
      vyos.vyos.vyos_ha:
        config:
        state: purged

    # After state:

    # vyos@vyos:~$ show configuration commands |  match "set high-availability"
    # vyos@vyos:~$
    #
    # Module Execution:
    #
    # "after": {
    #     "disable": false
    # },
    # "before": {
    #     "disable": true,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 30,
    #             "port": 81,
    #             "protocol": "tcp"
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp"
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             }
    #         },
    #         "groups": [
    #             {
    #                 "disable": false,
    #                 "name": "g1",
    #                 "no_preempt": false,
    #                 "peer_address": "192.168.1.3",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 5
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    # "changed": true,
    # "commands": [
    #     "delete high-availability"
    # ],


    # using gathered:
    # --------------

    # Before state:
    # vyos@vyos:~$
    # show configuration commands |  match "set high-availability"
    # set high-availability disable
    # set high-availability virtual-server s1 address '10.10.10.5'
    # set high-availability virtual-server s1 algorithm 'round-robin'
    # set high-availability virtual-server s1 real-server 10.10.50.2 port '8443'
    # set high-availability virtual-server s2 address '10.10.10.2'
    # set high-availability virtual-server s2 persistence-timeout '30'
    # set high-availability virtual-server s2 port '81'
    # set high-availability virtual-server s2 protocol 'tcp'
    # set high-availability virtual-server s3 address '10.10.10.3'
    # set high-availability virtual-server s3 port '88'
    # set high-availability virtual-server s3 protocol 'udp'
    # set high-availability vrrp global-parameters garp master-repeat '6'
    # set high-availability vrrp global-parameters startup-delay '30'
    # set high-availability vrrp group g1 peer-address '192.168.1.3'
    # set high-availability vrrp group g1 priority '100'
    # set high-availability vrrp group g1 vrid '20'
    # set high-availability vrrp snmp
    # set high-availability vrrp sync-group sg1 health-check failure-count '5'
    # vyos@vyos:~$

    - name: gather configs
      vyos.vyos.vyos_ha:
        state: gathered

    # Module Execution:
    # "changed": false,
    # "gathered": {
    #     "disable": true,
    #     "virtual_servers": [
    #         {
    #             "address": "10.10.10.5",
    #             "algorithm": "round-robin",
    #             "name": "s1",
    #             "real_server": [
    #                 {
    #                     "address": "10.10.50.2",
    #                     "port": 8443
    #                 }
    #             ]
    #         },
    #         {
    #             "address": "10.10.10.2",
    #             "name": "s2",
    #             "persistence_timeout": 30,
    #             "port": 81,
    #             "protocol": "tcp"
    #         },
    #         {
    #             "address": "10.10.10.3",
    #             "name": "s3",
    #             "port": 88,
    #             "protocol": "udp"
    #         }
    #     ],
    #     "vrrp": {
    #         "global_parameters": {
    #             "garp": {
    #                 "master_repeat": 6
    #             },
    #             "startup_delay": 30
    #         },
    #         "groups": [
    #             {
    #                 "disable": false,
    #                 "name": "g1",
    #                 "no_preempt": false,
    #                 "peer_address": "192.168.1.3",
    #                 "priority": 100,
    #                 "rfc3768_compatibility": false,
    #                 "vrid": 20
    #             }
    #         ],
    #         "snmp": "enabled",
    #         "sync_groups": [
    #             {
    #                 "health_check": {
    #                     "failure_count": 5
    #                 },
    #                 "name": "sg1"
    #             }
    #         ]
    #     }
    # },
    #

    # Using parsed:
    # ------------

    # parsed.cfg
    # set high-availability vrrp group g1 interface eth2
    # set high-availability vrrp group g1 address 1.1.1.1
    # set high-availability vrrp group g1 disable
    # set high-availability vrrp group g1 no-preempt
    # set high-availability vrrp group g1 advertise-interval 10
    # set high-availability vrrp group g1 peer-address 2.2.2.2
    # set high-availability vrrp group g1 rfc3768-compatibility
    # set high-availability vrrp group g1 vrid 20

    - name: parse configs
      vyos.vyos.vyos_ha:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # Module execution:
    # "parsed": {
    #     "disable": false,
    #     "vrrp": {
    #         "groups": [
    #             {
    #                 "address": "1.1.1.1",
    #                 "advertise_interval": 10,
    #                 "disable": true,
    #                 "interface": "eth2",
    #                 "name": "g1",
    #                 "no_preempt": true,
    #                 "peer_address": "2.2.2.2",
    #                 "rfc3768_compatibility": true,
    #                 "vrid": 20
    #             }
    #         ]
    #     }
    # }
    #

    # Using rendered:
    # --------------

    - name: Render
      vyos.vyos.vyos_ha:
        config:
          disable: true
          vrrp:
            snmp: enabled
            global_parameters:
              startup_delay: 32
              version: 3
              garp:
                interval: 30
                master_delay: 11
                master_refresh: 100
                master_refresh_repeat: 200
                master_repeat: 5
        state: rendered

    # Module Execution:
    # "rendered": [
    #     "set high-availability disable",
    #     "set high-availability vrrp global-parameters garp interval 30",
    #     "set high-availability vrrp global-parameters garp master-delay 11",
    #     "set high-availability vrrp global-parameters garp master-refresh 100",
    #     "set high-availability vrrp global-parameters garp master-refresh-repeat 200",
    #     "set high-availability vrrp global-parameters garp master-repeat 5",
    #     "set high-availability vrrp global-parameters startup-delay 32",
    #     "set high-availability vrrp global-parameters version 3",
    #     "set high-availability vrrp snmp"
    # ]



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set high-availability vrrp group g1 address &#x27;1.1.1.1&#x27;&quot;, &quot;set high-availability vrrp group g1 advertise-interval &#x27;10&#x27;&quot;, &quot;set high-availability vrrp group g1 description &#x27;Group 1&#x27;&quot;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set high-availability vrrp global-parameters garp master-delay &#x27;10&#x27;&quot;, &quot;set high-availability vrrp global-parameters garp master-refresh &#x27;100&#x27;&quot;, &quot;set high-availability vrrp global-parameters garp master-refresh-repeat &#x27;200&#x27;&quot;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Evgeny Molotkov (@omnom62)
