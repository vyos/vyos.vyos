.. _vyos.vyos.vyos_firewall_global_module:


******************************
vyos.vyos.vyos_firewall_global
******************************

**Firewall global resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manage global policies or configurations for firewall on VyOS devices.




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
                        <div>A dictionary of Firewall global configuration options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config_trap</b>
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
                        <div>SNMP trap generation on firewall configuration changes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines a group of objects for referencing in firewall rules.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines a group of IP addresses for referencing in firewall rules.</div>
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
                                    <li><div style="color: blue"><b>ipv4</b>&nbsp;&larr;</div></li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies IP address type</div>
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
                        <div>Allows you to specify a brief description for the address group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Address-group members.</div>
                        <div>IPv4 address to match.</div>
                        <div>IPv4 range to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>IP address.</div>
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
                        <div>Name of the firewall address group.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>network_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines a group of networks for referencing in firewall rules.</div>
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
                                    <li><div style="color: blue"><b>ipv4</b>&nbsp;&larr;</div></li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies network address type</div>
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
                        <div>Allows you to specify a brief description for the network group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Adds an IPv4 network to the specified network group.</div>
                        <div>The format is ip-address/prefix.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>IP address.</div>
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
                        <div>Name of the firewall network group.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines a group of ports for referencing in firewall rules.</div>
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
                        <div>A brief description for the port group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port-group member.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specified port.</div>
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
                        <div>Name of the firewall port group.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_martians</b>
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
                        <div>Specifies whether or not to record packets with invalid addresses in the log.</div>
                        <div>(True) Logs packets with invalid addresses.</div>
                        <div>(False) Does not log packets with invalid addresses.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ping</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Policy for handling of all IPv4 ICMP echo requests.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>all</b>
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
                        <div>Enables or disables response to all IPv4 ICMP Echo Request (ping) messages.</div>
                        <div>The system responds to IPv4 ICMP Echo Request messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcast</b>
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
                        <div>Enables or disables response to broadcast IPv4 ICMP Echo Request and Timestamp Request messages.</div>
                        <div>IPv4 ICMP Echo and Timestamp Request messages are not processed.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_redirects</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of Firewall ICMP redirect and source route global configuration options.</div>
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
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies IP address type</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp_redirects</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies whether to allow sending/receiving of IPv4/v6 ICMP redirect messages.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>receive</b>
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
                        <div>Permits or denies receiving packets ICMP redirect messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>send</b>
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
                        <div>Permits or denies transmitting packets ICMP redirect messages.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip_src_route</b>
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
                        <div>Specifies whether or not to process source route IP options.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies global firewall state-policy.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>accept</li>
                                    <li>drop</li>
                                    <li>reject</li>
                        </ul>
                </td>
                <td>
                        <div>Action for packets part of an established connection.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>connection_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>established</li>
                                    <li>invalid</li>
                                    <li>related</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies connection type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log</b>
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
                        <div>Enable logging of packets part of an established connection.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emerg</li>
                                    <li>alert</li>
                                    <li>crit</li>
                                    <li>err</li>
                                    <li>warn</li>
                                    <li>notice</li>
                                    <li>info</li>
                                    <li>debug</li>
                        </ul>
                </td>
                <td>
                        <div>Specify log level for packets logged.</div>
                        <div>Only available in 1.4+</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>syn_cookies</b>
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
                        <div>Specifies policy for using TCP SYN cookies with IPv4.</div>
                        <div>(True) Enables TCP SYN cookies with IPv4.</div>
                        <div>(False) Disables TCP SYN cookies with IPv4.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>twa_hazards_protection</b>
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
                        <div>RFC1337 TCP TIME-WAIT assassination hazards protection.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>validation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>strict</li>
                                    <li>loose</li>
                                    <li>disable</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies a policy for source validation by reversed path, as defined in RFC 3704.</div>
                        <div>(disable) No source validation is performed.</div>
                        <div>(loose) Enable Loose Reverse Path Forwarding as defined in RFC3704.</div>
                        <div>(strict) Enable Strict Reverse Path Forwarding as defined in RFC3704.</div>
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
                        <div>The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The <em>running_config</em> argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command <code>show configuration commands | grep &#x27;firewall&#x27;</code></div>
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
   - Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025.
   - The provided examples of commands are valid for VyOS 1.4+
   - This module works with connection ``ansible.netcommon.network_cli``. See `the VyOS OS Platform Options <../network/user_guide/platform_vyos.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # vyos@vyos# run show  configuration commands | grep firewall
    #
    #
    - name: Merge the provided configuration with the existing running configuration
      vyos.vyos.vyos_firewall_global:
        config:
          validation: strict
          config_trap: true
          log_martians: true
          syn_cookies: true
          twa_hazards_protection: true
          ping:
            all: true
            broadcast: true
          state_policy:
            - connection_type: established
              action: accept
              log: true
              log_level: emerg
            - connection_type: invalid
              action: reject
          route_redirects:
            - afi: ipv4
              ip_src_route: true
              icmp_redirects:
                send: true
                receive: false
          group:
            address_group:
              - name: MGMT-HOSTS
                description: This group has the Management hosts address list
                members:
                  - address: 192.0.1.1
                  - address: 192.0.1.3
                  - address: 192.0.1.5
            network_group:
              - name: MGMT
                description: This group has the Management network addresses
                members:
                  - address: 192.0.1.0/24
        state: merged
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    # before": []
    #
    #    "commands": [
    #        "set firewall group address-group MGMT-HOSTS address 192.0.1.1",
    #        "set firewall group address-group MGMT-HOSTS address 192.0.1.3",
    #        "set firewall group address-group MGMT-HOSTS address 192.0.1.5",
    #        "set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'",
    #        "set firewall group address-group MGMT-HOSTS",
    #        "set firewall group network-group MGMT network 192.0.1.0/24",
    #        "set firewall group network-group MGMT description 'This group has the Management network addresses'",
    #        "set firewall group network-group MGMT",
    #        "set firewall global-options ip-src-route 'enable'",
    #        "set firewall global-options receive-redirects 'disable'",
    #        "set firewall global-options send-redirects 'enable'",
    #        "set firewall global-options config-trap 'enable'",
    #        "set firewall global-options state-policy established action 'accept'",
    #        "set firewall global-options state-policy established log,
    #        "set firewall global-options state-policy established log-level 'emerg'",
    #        "set firewall global-options state-policy invalid action 'reject'",
    #        "set firewall global-options broadcast-ping 'enable'",
    #        "set firewall global-options all-ping 'enable'",
    #        "set firewall global-options log-martians 'enable'",
    #        "set firewall global-options twa-hazards-protection 'enable'",
    #        "set firewall global-options syn-cookies 'enable'",
    #        "set firewall global-options source-validation 'strict'"
    #    ]
    #
    # "after": {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "This group has the Management hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.1"
    #                        },
    #                        {
    #                            "address": "192.0.1.3"
    #                        },
    #                        {
    #                            "address": "192.0.1.5"
    #                        }
    #                    ],
    #                    "name": "MGMT-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    #
    # After state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep firewall
    # set firewall global-options all-ping 'enable'
    # set firewall global-options broadcast-ping 'enable'
    # set firewall global-options config-trap 'enable'
    # set firewall global-options ip-src-route 'enable'
    # set firewall global-options log-martians 'enable'
    # set firewall global-options receive-redirects 'disable'
    # set firewall global-options send-redirects 'enable'
    # set firewall global-options source-validation 'strict'
    # set firewall global-options state-policy established action 'accept'
    # set firewall global-options state-policy established log 'enable'
    # set firewall global-options state-policy invalid action 'reject'
    # set firewall global-options syn-cookies 'enable'
    # set firewall global-options twa-hazards-protection 'enable'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.1'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.3'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.5'
    # set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'
    # set firewall group network-group MGMT description 'This group has the Management network addresses'
    # set firewall group network-group MGMT network '192.0.1.0/24'
    #
    #


    # Using parsed
    #
    #
    - name: Render the commands for provided  configuration
      vyos.vyos.vyos_firewall_global:
        running_config: |
           set firewall global-options all-ping 'enable'
           set firewall global-options broadcast-ping 'enable'
           set firewall global-options config-trap 'enable'
           set firewall global-options ip-src-route 'enable'
           set firewall global-options log-martians 'enable'
           set firewall global-options receive-redirects 'disable'
           set firewall global-options send-redirects 'enable'
           set firewall global-options source-validation 'strict'
           set firewall global-options state-policy established action 'accept'
           set firewall global-options state-policy established log 'enable'
           set firewall global-options state-policy invalid action 'reject'
           set firewall global-options syn-cookies 'enable'
           set firewall global-options twa-hazards-protection 'enable'"
           set firewall group address-group ENG-HOSTS address '192.0.3.1'
           set firewall group address-group ENG-HOSTS address '192.0.3.2'
           set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
           set firewall group address-group SALES-HOSTS address '192.0.2.1'
           set firewall group address-group SALES-HOSTS address '192.0.2.2'
           set firewall group address-group SALES-HOSTS address '192.0.2.3'
           set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
           set firewall group network-group MGMT description 'This group has the Management network addresses'
           set firewall group network-group MGMT network '192.0.1.0/24'
        state: parsed
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "parsed": {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.3.1"
    #                        },
    #                        {
    #                            "address": "192.0.3.2"
    #                        }
    #                    ],
    #                    "name": "ENG-HOSTS"
    #                },
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.2.1"
    #                        },
    #                        {
    #                            "address": "192.0.2.2"
    #                        },
    #                        {
    #                            "address": "192.0.2.3"
    #                        }
    #                    ],
    #                    "name": "SALES-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    # }
    #


    #
    # Using deleted
    #
    # Before state
    # -------------
    #
    # vyos@192# run show configuration commands | grep firewall
    # set firewall global-options all-ping 'enable'
    # set firewall global-options broadcast-ping 'enable'
    # set firewall global-options config-trap 'enable'
    # set firewall global-options ip-src-route 'enable'
    # set firewall global-options log-martians 'enable'
    # set firewall global-options receive-redirects 'disable'
    # set firewall global-options send-redirects 'enable'
    # set firewall global-options source-validation 'strict'
    # set firewall global-options state-policy established action 'accept'
    # set firewall global-options state-policy established log 'enable'
    # set firewall global-options state-policy invalid action 'reject'
    # set firewall global-options syn-cookies 'enable'
    # set firewall global-options twa-hazards-protection 'enable'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.1'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.3'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.5'
    # set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'
    # set firewall group network-group MGMT description 'This group has the Management network addresses'
    # set firewall group network-group MGMT network '192.0.1.0/24'

    - name: Delete attributes of firewall.
      vyos.vyos.vyos_firewall_global:
        config:
          state_policy:
          config_trap:
          log_martians:
          syn_cookies:
          twa_hazards_protection:
          route_redirects:
          ping:
          group:
        state: deleted

    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #    "before": {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "This group has the Management hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.1"
    #                        },
    #                        {
    #                            "address": "192.0.1.3"
    #                        },
    #                        {
    #                            "address": "192.0.1.5"
    #                        }
    #                    ],
    #                    "name": "MGMT-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    # "commands": [
    #        "delete firewall global-options source-validation",
    #        "delete firewall global-options group",
    #        "delete firewall global-options log-martians",
    #        "delete firewall global-options ip-src-route",
    #        "delete firewall global-options receive-redirects",
    #        "delete firewall global-options send-redirects",
    #        "delete firewall global-options config-trap",
    #        "delete firewall global-options state-policy",
    #        "delete firewall global-options syn-cookies",
    #        "delete firewall global-options broadcast-ping",
    #        "delete firewall global-options all-ping",
    #        "delete firewall global-options twa-hazards-protection"
    #    ]
    #
    # "after": []
    #
    # After state
    # ------------
    # vyos@192# run show configuration commands | grep firewall
    # set  'firewall'
    #


    #
    # Using replaced
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall global-options all-ping 'enable'
    # set firewall global-options broadcast-ping 'enable'
    # set firewall global-options config-trap 'enable'
    # set firewall global-options ip-src-route 'enable'
    # set firewall global-options log-martians 'enable'
    # set firewall global-options receive-redirects 'disable'
    # set firewall global-options send-redirects 'enable'
    # set firewall global-options source-validation 'strict'
    # set firewall global-options state-policy established action 'accept'
    # set firewall global-options state-policy established log 'enable'
    # set firewall global-options state-policy invalid action 'reject'
    # set firewall global-options syn-cookies 'enable'
    # set firewall global-options twa-hazards-protection 'enable'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.1'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.3'
    # set firewall group address-group MGMT-HOSTS address '192.0.1.5'
    # set firewall group address-group MGMT-HOSTS description 'This group has the Management hosts address list'
    # set firewall group network-group MGMT description 'This group has the Management network addresses'
    # set firewall group network-group MGMT network '192.0.1.0/24'

    - name: Replace firewall global attributes configuration.
      vyos.vyos.vyos_firewall_global:
        config:
          validation: strict
          config_trap: true
          log_martians: true
          syn_cookies: true
          twa_hazards_protection: true
          ping: null
          all: true
          broadcast: true
          state_policy:
            - connection_type: established
              action: accept
              log: true
            - connection_type: invalid
              action: reject
          route_redirects:
            - afi: ipv4
              ip_src_route: true
              icmp_redirects:
                send: true
                receive: false
          group:
            address_group:
              - name: SALES-HOSTS
                description: Sales office hosts address list
                members:
                  - address: 192.0.2.1
                  - address: 192.0.2.2
                  - address: 192.0.2.3
              - name: ENG-HOSTS
                description: Sales office hosts address list
                members:
                  - address: 192.0.3.1
                  - address: 192.0.3.2
            network_group:
              - name: MGMT
                description: This group has the Management network addresses
                members:
                  - address: 192.0.1.0/24
        state: replaced
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "before": {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "This group has the Management hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.1"
    #                        },
    #                        {
    #                            "address": "192.0.1.3"
    #                        },
    #                        {
    #                            "address": "192.0.1.5"
    #                        }
    #                    ],
    #                    "name": "MGMT-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    #
    # "commands": [
    #        "delete firewall group address-group MGMT-HOSTS",
    #        "set firewall group address-group SALES-HOSTS address 192.0.2.1",
    #        "set firewall group address-group SALES-HOSTS address 192.0.2.2",
    #        "set firewall group address-group SALES-HOSTS address 192.0.2.3",
    #        "set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'",
    #        "set firewall group address-group SALES-HOSTS",
    #        "set firewall group address-group ENG-HOSTS address 192.0.3.1",
    #        "set firewall group address-group ENG-HOSTS address 192.0.3.2",
    #        "set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'",
    #        "set firewall group address-group ENG-HOSTS"
    #    ]
    #
    #    "after": {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.3.1"
    #                        },
    #                        {
    #                            "address": "192.0.3.2"
    #                        }
    #                    ],
    #                    "name": "ENG-HOSTS"
    #                },
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.2.1"
    #                        },
    #                        {
    #                            "address": "192.0.2.2"
    #                        },
    #                        {
    #                            "address": "192.0.2.3"
    #                        }
    #                    ],
    #                   "name": "SALES-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    #
    # After state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep firewall
    # set firewall global-options all-ping 'enable'
    # set firewall global-options broadcast-ping 'enable'
    # set firewall global-options config-trap 'enable'
    # set firewall global-options ip-src-route 'enable'
    # set firewall global-options log-martians 'enable'
    # set firewall global-options receive-redirects 'disable'
    # set firewall global-options send-redirects 'enable'
    # set firewall global-options source-validation 'strict'
    # set firewall global-options state-policy established action 'accept'
    # set firewall global-options state-policy established log 'enable'
    # set firewall global-options state-policy invalid action 'reject'
    # set firewall global-options syn-cookies 'enable'
    # set firewall global-options twa-hazards-protection 'enable'
    # set firewall group address-group ENG-HOSTS address '192.0.3.1'
    # set firewall group address-group ENG-HOSTS address '192.0.3.2'
    # set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
    # set firewall group address-group SALES-HOSTS address '192.0.2.1'
    # set firewall group address-group SALES-HOSTS address '192.0.2.2'
    # set firewall group address-group SALES-HOSTS address '192.0.2.3'
    # set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
    # set firewall group network-group MGMT description 'This group has the Management network addresses'
    # set firewall group network-group MGMT network '192.0.1.0/24'
    #
    #


    # Using gathered
    #
    # Before state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep firewall
    # set firewall global-options all-ping 'enable'
    # set firewall global-options broadcast-ping 'enable'
    # set firewall global-options config-trap 'enable'
    # set firewall global-options ip-src-route 'enable'
    # set firewall global-options log-martians 'enable'
    # set firewall global-options receive-redirects 'disable'
    # set firewall global-options send-redirects 'enable'
    # set firewall global-options source-validation 'strict'
    # set firewall global-options state-policy established action 'accept'
    # set firewall global-options state-policy established log 'enable'
    # set firewall global-options state-policy invalid action 'reject'
    # set firewall global-options syn-cookies 'enable'
    # set firewall global-options twa-hazards-protection 'enable'
    # set firewall group address-group ENG-HOSTS address '192.0.3.1'
    # set firewall group address-group ENG-HOSTS address '192.0.3.2'
    # set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
    # set firewall group address-group SALES-HOSTS address '192.0.2.1'
    # set firewall group address-group SALES-HOSTS address '192.0.2.2'
    # set firewall group address-group SALES-HOSTS address '192.0.2.3'
    # set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
    # set firewall group network-group MGMT description 'This group has the Management network addresses'
    # set firewall group network-group MGMT network '192.0.1.0/24'

    - name: Gather firewall global config with provided configurations
      vyos.vyos.vyos_firewall_global:
        state: gathered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "gathered": [
    # {
    #        "config_trap": true,
    #        "group": {
    #            "address_group": [
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.3.1"
    #                        },
    #                        {
    #                            "address": "192.0.3.2"
    #                        }
    #                    ],
    #                    "name": "ENG-HOSTS"
    #                },
    #                {
    #                    "description": "Sales office hosts address list",
    #                    "members": [
    #                        {
    #                            "address": "192.0.2.1"
    #                        },
    #                        {
    #                            "address": "192.0.2.2"
    #                        },
    #                        {
    #                            "address": "192.0.2.3"
    #                        }
    #                    ],
    #                    "name": "SALES-HOSTS"
    #                }
    #            ],
    #            "network_group": [
    #                {
    #                    "description": "This group has the Management network addresses",
    #                    "members": [
    #                        {
    #                            "address": "192.0.1.0/24"
    #                        }
    #                    ],
    #                    "name": "MGMT"
    #                }
    #            ]
    #        },
    #        "log_martians": true,
    #        "ping": {
    #            "all": true,
    #            "broadcast": true
    #        },
    #        "route_redirects": [
    #            {
    #                "afi": "ipv4",
    #                "icmp_redirects": {
    #                    "receive": false,
    #                    "send": true
    #                },
    #                "ip_src_route": true
    #            }
    #        ],
    #        "state_policy": [
    #            {
    #                "action": "accept",
    #                "connection_type": "established",
    #                "log": true
    #            },
    #            {
    #                "action": "reject",
    #                "connection_type": "invalid"
    #            }
    #        ],
    #        "syn_cookies": true,
    #        "twa_hazards_protection": true,
    #        "validation": "strict"
    #    }
    #
    # After state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep firewall
    # set firewall global-options all-ping 'enable'
    # set firewall global-options broadcast-ping 'enable'
    # set firewall global-options config-trap 'enable'
    # set firewall global-options ip-src-route 'enable'
    # set firewall global-options log-martians 'enable'
    # set firewall global-options receive-redirects 'disable'
    # set firewall global-options send-redirects 'enable'
    # set firewall global-options source-validation 'strict'
    # set firewall global-options state-policy established action 'accept'
    # set firewall global-options state-policy established log 'enable'
    # set firewall global-options state-policy invalid action 'reject'
    # set firewall global-options syn-cookies 'enable'
    # set firewall global-options twa-hazards-protection 'enable'
    # set firewall group address-group ENG-HOSTS address '192.0.3.1'
    # set firewall group address-group ENG-HOSTS address '192.0.3.2'
    # set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'
    # set firewall group address-group SALES-HOSTS address '192.0.2.1'
    # set firewall group address-group SALES-HOSTS address '192.0.2.2'
    # set firewall group address-group SALES-HOSTS address '192.0.2.3'
    # set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'
    # set firewall group network-group MGMT description 'This group has the Management network addresses'
    # set firewall group network-group MGMT network '192.0.1.0/24'


    # Using rendered
    #
    #
    - name: Render the commands for provided  configuration
      vyos.vyos.vyos_firewall_global:
        config:
          validation: strict
          config_trap: true
          log_martians: true
          syn_cookies: true
          twa_hazards_protection: true
          ping: null
          all: true
          broadcast: true
          state_policy:
            - connection_type: established
              action: accept
              log: true
            - connection_type: invalid
              action: reject
          route_redirects:
            - afi: ipv4
              ip_src_route: true
              icmp_redirects: null
              send: true
              receive: false
          group:
            address_group:
              - name: SALES-HOSTS
                description: Sales office hosts address list
                members:
                  - address: 192.0.2.1
                  - address: 192.0.2.2
                  - address: 192.0.2.3
              - name: ENG-HOSTS
                description: Sales office hosts address list
                members:
                  - address: 192.0.3.1
                  - address: 192.0.3.2
            network_group:
              - name: MGMT
                description: This group has the Management network addresses
                members:
                  - address: 192.0.1.0/24
        state: rendered

    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "rendered": [
    #        "set firewall group address-group SALES-HOSTS address 192.0.2.1",
    #        "set firewall group address-group SALES-HOSTS address 192.0.2.2",
    #        "set firewall group address-group SALES-HOSTS address 192.0.2.3",
    #        "set firewall group address-group SALES-HOSTS description 'Sales office hosts address list'",
    #        "set firewall group address-group SALES-HOSTS",
    #        "set firewall group address-group ENG-HOSTS address 192.0.3.1",
    #        "set firewall group address-group ENG-HOSTS address 192.0.3.2",
    #        "set firewall group address-group ENG-HOSTS description 'Sales office hosts address list'",
    #        "set firewall group address-group ENG-HOSTS",
    #        "set firewall group network-group MGMT network 192.0.1.0/24",
    #        "set firewall group network-group MGMT description 'This group has the Management network addresses'",
    #        "set firewall group network-group MGMT",
    #        "set firewall global-options ip-src-route 'enable'",
    #        "set firewall global-options receive-redirects 'disable'",
    #        "set firewall global-options send-redirects 'enable'",
    #        "set firewall global-options config-trap 'enable'",
    #        "set firewall global-options state-policy established action 'accept'",
    #        "set firewall global-options state-policy established log,
    #        "set firewall global-options state-policy invalid action 'reject'",
    #        "set firewall global-options broadcast-ping 'enable'",
    #        "set firewall global-options all-ping 'enable'",
    #        "set firewall global-options log-martians 'enable'",
    #        "set firewall global-options twa-hazards-protection 'enable'",
    #        "set firewall global-options syn-cookies 'enable'",
    #        "set firewall global-options source-validation 'strict'"
    #    ]
    #



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
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set firewall group address-group ENG-HOSTS&#x27;, &#x27;set firewall group address-group ENG-HOSTS address 192.0.3.1&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set firewall group address-group ENG-HOSTS&#x27;, &#x27;set firewall group address-group ENG-HOSTS address 192.0.3.1&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
