.. _vyos.vyos.vyos_vrrp_module:


*******************
vyos.vyos.vyos_vrrp
*******************

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
                        <span style="color: purple">string</span>
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
                        <span style="color: purple">string</span>
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
                    <b>real_servers</b>
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
                        <span style="color: purple">string</span>
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
                                    <li>no</li>
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
                                    <li>no</li>
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
                        <span style="color: purple">string</span>
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
                         / <span style="color: red">required</span>
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

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # vyos@vyos:~$

    - name: Merge provided configuration with device configuration
      vyos.vyos.vyos_vrrp:
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
    # set protocols bgp system-as 65536
    # set protocols bgp aggregate-address 192.0.2.0/24 'summary-only'
    # set protocols bgp aggregate-address 203.0.113.0/24 'as-set'
    # set protocols bgp maximum-paths ebgp '20'
    # set protocols bgp maximum-paths ibgp '55'
    # set protocols bgp neighbor 192.0.2.25 'disable-connected-check'
    # set protocols bgp neighbor 192.0.2.25 timers holdtime '30'
    # set protocols bgp neighbor 192.0.2.25 timers keepalive '10'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'as-path'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'med'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'next-hop'
    # set protocols bgp neighbor 203.0.113.5 ebgp-multihop '2'
    # set protocols bgp neighbor 203.0.113.5 remote-as '101'
    # set protocols bgp neighbor 203.0.113.5 update-source '192.0.2.25'
    # set protocols bgp neighbor 5001::64 distribute-list export '20'
    # set protocols bgp neighbor 5001::64 distribute-list import '40'
    # set protocols bgp neighbor 5001::64 maximum-prefix '34'
    # set protocols bgp network 192.1.13.0/24 'backdoor'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp parameters bestpath 'compare-routerid'
    # set protocols bgp parameters confederation identifier '66'
    # set protocols bgp parameters confederation peers '20'
    # set protocols bgp parameters confederation peers '55'
    # set protocols bgp parameters default 'no-ipv4-unicast'
    # set protocols bgp parameters router-id '192.1.2.9'
    # set protocols bgp redistribute connected route-map 'map01'
    # set protocols bgp redistribute kernel metric '45'
    # set protocols bgp timers keepalive '35'
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
    #         "set protocols bgp neighbor 192.0.2.25 disable-connected-check",
    #         "set protocols bgp neighbor 192.0.2.25 timers holdtime 30",
    #         "set protocols bgp neighbor 192.0.2.25 timers keepalive 10",
    #         "set protocols bgp neighbor 203.0.113.5 attribute-unchanged as-path",
    #         "set protocols bgp neighbor 203.0.113.5 attribute-unchanged med",
    #         "set protocols bgp neighbor 203.0.113.5 attribute-unchanged next-hop",
    #         "set protocols bgp neighbor 203.0.113.5 ebgp-multihop 2",
    #         "set protocols bgp neighbor 203.0.113.5 remote-as 101",
    #         "set protocols bgp neighbor 203.0.113.5 update-source 192.0.2.25",
    #         "set protocols bgp neighbor 5001::64 maximum-prefix 34",
    #         "set protocols bgp neighbor 5001::64 distribute-list export 20",
    #         "set protocols bgp neighbor 5001::64 distribute-list import 40",
    #         "set protocols bgp redistribute kernel metric 45",
    #         "set protocols bgp redistribute connected route-map map01",
    #         "set protocols bgp network 192.1.13.0/24 backdoor",
    #         "set protocols bgp aggregate-address 203.0.113.0/24 as-set",
    #         "set protocols bgp aggregate-address 192.0.2.0/24 summary-only",
    #         "set protocols bgp parameters bestpath as-path confed",
    #         "set protocols bgp parameters bestpath compare-routerid",
    #         "set protocols bgp parameters default no-ipv4-unicast",
    #         "set protocols bgp parameters router-id 192.1.2.9",
    #         "set protocols bgp parameters confederation peers 20",
    #         "set protocols bgp parameters confederation peers 55",
    #         "set protocols bgp parameters confederation identifier 66",
    #         "set protocols bgp maximum-paths ebgp 20",
    #         "set protocols bgp maximum-paths ibgp 55",
    #         "set protocols bgp timers keepalive 35"
    #     ],

    # Using replaced:
    # --------------

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp system-as 65536
    # set protocols bgp aggregate-address 192.0.2.0/24 'summary-only'
    # set protocols bgp aggregate-address 203.0.113.0/24 'as-set'
    # set protocols bgp maximum-paths ebgp '20'
    # set protocols bgp maximum-paths ibgp '55'
    # set protocols bgp neighbor 192.0.2.25 'disable-connected-check'
    # set protocols bgp neighbor 192.0.2.25 timers holdtime '30'
    # set protocols bgp neighbor 192.0.2.25 timers keepalive '10'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'as-path'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'med'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'next-hop'
    # set protocols bgp neighbor 203.0.113.5 ebgp-multihop '2'
    # set protocols bgp neighbor 203.0.113.5 remote-as '101'
    # set protocols bgp neighbor 203.0.113.5 update-source '192.0.2.25'
    # set protocols bgp neighbor 5001::64 distribute-list export '20'
    # set protocols bgp neighbor 5001::64 distribute-list import '40'
    # set protocols bgp neighbor 5001::64 maximum-prefix '34'
    # set protocols bgp network 192.1.13.0/24 'backdoor'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp parameters bestpath 'compare-routerid'
    # set protocols bgp parameters confederation identifier '66'
    # set protocols bgp parameters confederation peers '20'
    # set protocols bgp parameters confederation peers '55'
    # set protocols bgp parameters default 'no-ipv4-unicast'
    # set protocols bgp parameters router-id '192.1.2.9'
    # set protocols bgp redistribute connected route-map 'map01'
    # set protocols bgp redistribute kernel metric '45'
    # set protocols bgp timers keepalive '35'
    # vyos@vyos:~$

    - name: Replace
      vyos.vyos.vyos_vrrp:
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
    # set protocols bgp system-as 65536
    # set protocols bgp neighbor 192.0.2.40 advertisement-interval '72'
    # set protocols bgp neighbor 192.0.2.40 capability orf prefix-list 'receive'
    # set protocols bgp network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp redistribute static route-map 'map01'
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
    #         "delete protocols bgp timers",
    #         "delete protocols bgp maximum-paths ",
    #         "delete protocols bgp maximum-paths ",
    #         "delete protocols bgp parameters router-id 192.1.2.9",
    #         "delete protocols bgp parameters default",
    #         "delete protocols bgp parameters confederation",
    #         "delete protocols bgp parameters bestpath compare-routerid",
    #         "delete protocols bgp aggregate-address",
    #         "delete protocols bgp network 192.1.13.0/24",
    #         "delete protocols bgp redistribute kernel",
    #         "delete protocols bgp redistribute kernel",
    #         "delete protocols bgp redistribute connected",
    #         "delete protocols bgp redistribute connected",
    #         "delete protocols bgp neighbor 5001::64",
    #         "delete protocols bgp neighbor 203.0.113.5",
    #         "delete protocols bgp neighbor 192.0.2.25",
    #         "set protocols bgp neighbor 192.0.2.40 advertisement-interval 72",
    #         "set protocols bgp neighbor 192.0.2.40 capability orf prefix-list receive",
    #         "set protocols bgp redistribute static route-map map01",
    #         "set protocols bgp network 203.0.113.0/24 route-map map01"
    #     ],

    # Using deleted:
    # -------------

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp system-as 65536
    # set protocols bgp neighbor 192.0.2.40 advertisement-interval '72'
    # set protocols bgp neighbor 192.0.2.40 capability orf prefix-list 'receive'
    # set protocols bgp network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp redistribute static route-map 'map01'
    # vyos@vyos:~$

    - name: Delete configuration
      vyos.vyos.vyos_vrrp:
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
    #         "delete protocols bgp neighbor 192.0.2.40",
    #         "delete protocols bgp redistribute",
    #         "delete protocols bgp network",
    #         "delete protocols bgp parameters"
    #     ],

    # Using purged:

    # Before state:

    # vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
    # set protocols bgp system-as 65536
    # set protocols bgp aggregate-address 192.0.2.0/24 'summary-only'
    # set protocols bgp aggregate-address 203.0.113.0/24 'as-set'
    # set protocols bgp maximum-paths ebgp '20'
    # set protocols bgp maximum-paths ibgp '55'
    # set protocols bgp neighbor 192.0.2.25 'disable-connected-check'
    # set protocols bgp neighbor 192.0.2.25 timers holdtime '30'
    # set protocols bgp neighbor 192.0.2.25 timers keepalive '10'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'as-path'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'med'
    # set protocols bgp neighbor 203.0.113.5 attribute-unchanged 'next-hop'
    # set protocols bgp neighbor 203.0.113.5 ebgp-multihop '2'
    # set protocols bgp neighbor 203.0.113.5 remote-as '101'
    # set protocols bgp neighbor 203.0.113.5 update-source '192.0.2.25'
    # set protocols bgp neighbor 5001::64 distribute-list export '20'
    # set protocols bgp neighbor 5001::64 distribute-list import '40'
    # set protocols bgp neighbor 5001::64 maximum-prefix '34'
    # set protocols bgp network 192.1.13.0/24 'backdoor'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp parameters bestpath 'compare-routerid'
    # set protocols bgp parameters confederation identifier '66'
    # set protocols bgp parameters confederation peers '20'
    # set protocols bgp parameters confederation peers '55'
    # set protocols bgp parameters default 'no-ipv4-unicast'
    # set protocols bgp parameters router-id '192.1.2.9'
    # set protocols bgp redistribute connected route-map 'map01'
    # set protocols bgp redistribute kernel metric '45'
    # set protocols bgp timers keepalive '35'
    # vyos@vyos:~$


    - name: Purge configuration
      vyos.vyos.vyos_vrrp:
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
    # set protocols bgp system-as 65536
    # set protocols bgp neighbor 192.0.2.43 advertisement-interval '72'
    # set protocols bgp neighbor 192.0.2.43 capability 'dynamic'
    # set protocols bgp neighbor 192.0.2.43 'disable-connected-check'
    # set protocols bgp neighbor 192.0.2.43 timers holdtime '30'
    # set protocols bgp neighbor 192.0.2.43 timers keepalive '10'
    # set protocols bgp neighbor 203.0.113.0 address-family 'ipv6-unicast'
    # set protocols bgp neighbor 203.0.113.0 capability orf prefix-list 'receive'
    # set protocols bgp network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp parameters 'always-compare-med'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp parameters bestpath 'compare-routerid'
    # set protocols bgp parameters dampening half-life '33'
    # set protocols bgp parameters dampening max-suppress-time '20'
    # set protocols bgp parameters dampening re-use '60'
    # set protocols bgp parameters dampening start-suppress-time '5'
    # set protocols bgp parameters default 'no-ipv4-unicast'
    # set protocols bgp parameters distance global external '66'
    # set protocols bgp parameters distance global internal '20'
    # set protocols bgp parameters distance global local '10'
    # set protocols bgp redistribute static route-map 'map01'
    # vyos@vyos:~$ ^C
    # vyos@vyos:~$

    - name: Delete configuration
      vyos.vyos.vyos_vrrp:
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
    # set protocols bgp system-as 65536
    # set protocols bgp neighbor 192.0.2.43 advertisement-interval '72'
    # set protocols bgp neighbor 192.0.2.43 capability 'dynamic'
    # set protocols bgp neighbor 192.0.2.43 'disable-connected-check'
    # set protocols bgp neighbor 192.0.2.43 timers holdtime '30'
    # set protocols bgp neighbor 192.0.2.43 timers keepalive '10'
    # set protocols bgp neighbor 203.0.113.0 address-family 'ipv6-unicast'
    # set protocols bgp neighbor 203.0.113.0 capability orf prefix-list 'receive'
    # set protocols bgp network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp parameters 'always-compare-med'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp parameters bestpath 'compare-routerid'
    # set protocols bgp parameters dampening half-life '33'
    # set protocols bgp parameters dampening max-suppress-time '20'
    # set protocols bgp parameters dampening re-use '60'
    # set protocols bgp parameters dampening start-suppress-time '5'
    # set protocols bgp parameters default 'no-ipv4-unicast'
    # set protocols bgp parameters distance global external '66'
    # set protocols bgp parameters distance global internal '20'
    # set protocols bgp parameters distance global local '10'
    # set protocols bgp redistribute static route-map 'map01'
    # vyos@vyos:~$ ^C

    - name: gather configs
      vyos.vyos.vyos_vrrp:
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

    # set protocols bgp neighbor 192.0.2.43 advertisement-interval '72'
    # set protocols bgp neighbor 192.0.2.43 capability 'dynamic'
    # set protocols bgp neighbor 192.0.2.43 'disable-connected-check'
    # set protocols bgp neighbor 192.0.2.43 timers holdtime '30'
    # set protocols bgp neighbor 192.0.2.43 timers keepalive '10'
    # set protocols bgp neighbor 203.0.113.0 address-family 'ipv6-unicast'
    # set protocols bgp neighbor 203.0.113.0 capability orf prefix-list 'receive'
    # set protocols bgp network 203.0.113.0/24 route-map 'map01'
    # set protocols bgp parameters 'always-compare-med'
    # set protocols bgp parameters bestpath as-path 'confed'
    # set protocols bgp parameters bestpath 'compare-routerid'
    # set protocols bgp parameters dampening half-life '33'
    # set protocols bgp parameters dampening max-suppress-time '20'
    # set protocols bgp parameters dampening re-use '60'
    # set protocols bgp parameters dampening start-suppress-time '5'
    # set protocols bgp parameters default 'no-ipv4-unicast'
    # set protocols bgp parameters distance global external '66'
    # set protocols bgp parameters distance global internal '20'
    # set protocols bgp parameters distance global local '10'
    # set protocols bgp redistribute static route-map 'map01'

    - name: parse configs
      vyos.vyos.vyos_vrrp:
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
      vyos.vyos.vyos_vrrp:
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
    #         "set protocols bgp neighbor 192.0.2.43 disable-connected-check",
    #         "set protocols bgp neighbor 192.0.2.43 advertisement-interval 72",
    #         "set protocols bgp neighbor 192.0.2.43 capability dynamic",
    #         "set protocols bgp neighbor 192.0.2.43 timers holdtime 30",
    #         "set protocols bgp neighbor 192.0.2.43 timers keepalive 10",
    #         "set protocols bgp neighbor 203.0.113.0 capability orf prefix-list receive",
    #         "set protocols bgp redistribute static route-map map01",
    #         "set protocols bgp network 203.0.113.0/24 route-map map01",
    #         "set protocols bgp parameters always-compare-med",
    #         "set protocols bgp parameters dampening half-life 33",
    #         "set protocols bgp parameters dampening max-suppress-time 20",
    #         "set protocols bgp parameters dampening re-use 60",
    #         "set protocols bgp parameters dampening start-suppress-time 5",
    #         "set protocols bgp parameters distance global internal 20",
    #         "set protocols bgp parameters distance global local 10",
    #         "set protocols bgp parameters distance global external 66",
    #         "set protocols bgp parameters bestpath as-path confed",
    #         "set protocols bgp parameters bestpath compare-routerid",
    #         "set protocols bgp parameters default no-ipv4-unicast"
    #     ]



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set protocols bgp redistribute static route-map map01&#x27;, &#x27;set protocols bgp network 203.0.113.0/24 route-map map01&#x27;, &#x27;set protocols bgp parameters always-compare-med&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set protocols bgp redistribute static route-map map01&#x27;, &#x27;set protocols bgp network 203.0.113.0/24 route-map map01&#x27;, &#x27;set protocols bgp parameters always-compare-med&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Evgeny Molotkov (@omnom62)
