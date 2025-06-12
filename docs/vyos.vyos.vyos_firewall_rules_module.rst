.. _vyos.vyos.vyos_firewall_rules_module:


*****************************
vyos.vyos.vyos_firewall_rules
*****************************

**Firewall rules resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages firewall rule-set attributes on VyOS devices




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
                        <div>A dictionary of Firewall rule-set options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                        <div>Specifies the type of rule-set.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rule_sets</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The Firewall rule-set list.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>drop</li>
                                    <li>reject</li>
                                    <li>accept</li>
                                    <li>jump</li>
                        </ul>
                </td>
                <td>
                        <div>Default action for rule-set.</div>
                        <div>drop (Drop if no prior rules are hit (default))</div>
                        <div>reject (Drop and notify source if no prior rules are hit)</div>
                        <div>accept (Accept if no prior rules are hit)</div>
                        <div>jump (Jump to another rule-set, 1.4+)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_jump_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Default jump target if the default action is jump.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Only valid when default_action = jump.</div>
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
                        <div>Rule set description.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_default_log</b>
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
                        <div>Option to log packets hitting default-action.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>input</li>
                                    <li>output</li>
                                    <li>forward</li>
                        </ul>
                </td>
                <td>
                        <div>Filter type (exclusive to &quot;name&quot;).</div>
                        <div>Supported in 1.4 and later.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Firewall rule set name.</div>
                        <div>Required for 1.3- and optional for 1.4+.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary that specifies the rule-set configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                                    <li>drop</li>
                                    <li>reject</li>
                                    <li>accept</li>
                                    <li>inspect</li>
                                    <li>continue</li>
                                    <li>return</li>
                                    <li>jump</li>
                                    <li>queue</li>
                                    <li>synproxy</li>
                        </ul>
                </td>
                <td>
                        <div>Specifying the action.</div>
                        <div>inspect is available  &lt; 1.4</div>
                        <div>continue, return, jump, queue, synproxy are available &gt;= 1.4</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Description of this rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifying the destination parameters.</div>
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
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination ip address subnet or range.</div>
                        <div>IPv4/6 address, subnet or range to match.</div>
                        <div>Match everything except the specified address, subnet or range.</div>
                        <div>Destination ip address subnet or range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Destination group.</div>
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
                    <b>address_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of addresses.</div>
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
                    <b>network_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of networks.</div>
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
                    <b>port_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of ports.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Multiple destination ports can be specified as a comma-separated list.</div>
                        <div>The whole list can also be &quot;negated&quot; using &#x27;!&#x27;.</div>
                        <div>For example:&#x27;!22,telnet,http,123,1001-1005&#x27;.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable</b>
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
                        <div>Option to disable firewall rule.</div>
                        <div>aliased to disabled</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: disabled</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fragment</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>match-frag</li>
                                    <li>match-non-frag</li>
                        </ul>
                </td>
                <td>
                        <div>IP fragment match.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>icmp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ICMP type and code information.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>code</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ICMP code.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ICMP type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>any</li>
                                    <li>echo-reply</li>
                                    <li>destination-unreachable</li>
                                    <li>network-unreachable</li>
                                    <li>host-unreachable</li>
                                    <li>protocol-unreachable</li>
                                    <li>port-unreachable</li>
                                    <li>fragmentation-needed</li>
                                    <li>source-route-failed</li>
                                    <li>network-unknown</li>
                                    <li>host-unknown</li>
                                    <li>network-prohibited</li>
                                    <li>host-prohibited</li>
                                    <li>TOS-network-unreachable</li>
                                    <li>TOS-host-unreachable</li>
                                    <li>communication-prohibited</li>
                                    <li>host-precedence-violation</li>
                                    <li>precedence-cutoff</li>
                                    <li>source-quench</li>
                                    <li>redirect</li>
                                    <li>network-redirect</li>
                                    <li>host-redirect</li>
                                    <li>TOS-network-redirect</li>
                                    <li>TOS-host-redirect</li>
                                    <li>echo-request</li>
                                    <li>router-advertisement</li>
                                    <li>router-solicitation</li>
                                    <li>time-exceeded</li>
                                    <li>ttl-zero-during-transit</li>
                                    <li>ttl-zero-during-reassembly</li>
                                    <li>parameter-problem</li>
                                    <li>ip-header-bad</li>
                                    <li>required-option-missing</li>
                                    <li>timestamp-request</li>
                                    <li>timestamp-reply</li>
                                    <li>address-mask-request</li>
                                    <li>address-mask-reply</li>
                                    <li>ping</li>
                                    <li>pong</li>
                                    <li>ttl-exceeded</li>
                        </ul>
                </td>
                <td>
                        <div>ICMP type-name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>inbound_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inbound interface.</div>
                        <div>Only valid in 1.4 and later.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface name.</div>
                        <div>Can have wildcards</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipsec</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>match-ipsec</li>
                                    <li>match-none</li>
                                    <li>match-ipsec-in</li>
                                    <li>match-ipsec-out</li>
                                    <li>match-none-in</li>
                                    <li>match-none-out</li>
                        </ul>
                </td>
                <td>
                        <div>Inbound ip sec packets.</div>
                        <div>VyOS 1.4 and older match-ipsec/match-none</div>
                        <div>VyOS 1.5 and later require -in/-out suffixes</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>jump_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Jump target if the action is jump.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Only valid when action = jump.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Rate limit using a token bucket filter.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>burst</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of packets to allow in excess of rate.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>format for rate (integer/time unit).</div>
                        <div>any one of second, minute, hour or day may be used to specify time unit.</div>
                        <div>eg. 1/second implies rule to be matched at an average of once per second.</div>
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
                    <b>number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This is the integer value.</div>
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
                    <b>unit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This is the time unit.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>disable</li>
                                    <li>enable</li>
                        </ul>
                </td>
                <td>
                        <div>Option to log packets matching rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Rule number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>outbound_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Match outbound interface.</div>
                        <div>Only valid in 1.4 and later.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface group.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface name.</div>
                        <div>Can have wildcards</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>packet_length</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Packet length match.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Multiple values from 1 to 65535 and ranges are supported</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>length</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Packet length or range.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>packet_length_exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Packet length match.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Multiple values from 1 to 65535 and ranges are supported</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>length</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Packet length or range.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>packet_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>broadcast</li>
                                    <li>multicast</li>
                                    <li>host</li>
                                    <li>other</li>
                        </ul>
                </td>
                <td>
                        <div>Packet type match.</div>
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
                </td>
                <td>
                        <div>Protocol to match (protocol name in /etc/protocols or protocol number or all).</div>
                        <div>&lt;text&gt; IP protocol name from /etc/protocols (e.g. &quot;tcp&quot; or &quot;udp&quot;).</div>
                        <div>&lt;0-255&gt; IP protocol number.</div>
                        <div>tcp_udp Both TCP and UDP.</div>
                        <div>all All IP protocols.</div>
                        <div>(!)All IP protocols except for the specified name or number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>queue</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Queue options.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Only valid when action = queue.</div>
                        <div>Can be a queue number or range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>queue_options</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>bypass</li>
                                    <li>fanout</li>
                        </ul>
                </td>
                <td>
                        <div>Queue options.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Only valid when action = queue.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>recent</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Parameters for matching recently seen sources.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Source addresses seen more than N times.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source addresses seen in the last N seconds.</div>
                        <div>Since 1.4, this is a string of second/minute/hour</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source parameters.</div>
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
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Source ip address subnet or range.</div>
                        <div>IPv4/6 address, subnet or range to match.</div>
                        <div>Match everything except the specified address, subnet or range.</div>
                        <div>Source ip address subnet or range.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fqdn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Fully qualified domain name.</div>
                        <div>Available in 1.4 and later.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Source group.</div>
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
                    <b>address_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of addresses.</div>
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
                    <b>network_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of networks.</div>
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
                    <b>port_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Group of ports.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>&lt;MAC address&gt; MAC address to match.</div>
                        <div>&lt;!MAC address&gt; Match everything except the specified MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Multiple source ports can be specified as a comma-separated list.</div>
                        <div>The whole list can also be &quot;negated&quot; using &#x27;!&#x27;.</div>
                        <div>For example:&#x27;!22,telnet,http,123,1001-1005&#x27;.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Session state.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>established</b>
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
                        <div>Established state.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>invalid</b>
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
                        <div>Invalid state.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>new</b>
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
                        <div>New state.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>related</b>
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
                        <div>Related state.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>synproxy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SYN proxy options.</div>
                        <div>Only valid in 1.4 and later.</div>
                        <div>Only valid when action = synproxy.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mss</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Adjust MSS (501-65535)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>window_scale</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Window scale (1-14).</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tcp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>TCP flags to match.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>flags</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>list of tcp flags to be matched</div>
                        <div>5.0 breaking change to support 1.4+ and 1.3-</div>
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
                    <b>flag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ack</li>
                                    <li>cwr</li>
                                    <li>ecn</li>
                                    <li>fin</li>
                                    <li>psh</li>
                                    <li>rst</li>
                                    <li>syn</li>
                                    <li>urg</li>
                                    <li>all</li>
                        </ul>
                </td>
                <td>
                        <div>TCP flag to be matched.</div>
                        <div>syn, ack, fin, rst, urg, psh, all (1.3-)</div>
                        <div>syn, ack, fin, rst, urg, psh, cwr, ecn (1.4+)</div>
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
                    <b>invert</b>
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
                        <div>Invert the match.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time to match rule.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>monthdays</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Monthdays to match rule on.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>startdate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Date to start matching rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>starttime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time of day to start matching rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stopdate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Date to stop matching rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stoptime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time of day to stop matching rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>utc</b>
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
                        <div>Interpret times for startdate, stopdate, starttime and stoptime to be UTC.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>weekdays</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Weekdays to match rule on.</div>
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
                        <div>The value of this option should be the output received from the VyOS device by executing the command <b>show configuration commands | grep firewall</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
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
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
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

    # Using deleted to delete firewall rules based on rule-set name
    #
    # Before state
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv4 name Downlink default-action 'accept'
    # set firewall ipv4 name Downlink description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name Downlink rule 501 action 'accept'
    # set firewall ipv4 name Downlink rule 501 description 'Rule 501 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 501 ipsec 'match-ipsec'
    # set firewall ipv4 name Downlink rule 502 action 'reject'
    # set firewall ipv4 name Downlink rule 502 description 'Rule 502 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 502 ipsec 'match-ipsec'

    - name: Delete attributes of given firewall rules.
      vyos.vyos.vyos_firewall_rules:
        config:
          - afi: ipv4
            rule_sets:
              - name: Downlink
        state: deleted
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #    "before": [
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "Downlink",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 501 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 501
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 502 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 502
    #                        }
    #                    ]
    #               }
    #            ]
    #        }
    #    ]
    #    "commands": [
    #        "delete firewall ipv4 name Downlink"
    #    ]
    #
    # "after": []
    # After state
    # ------------
    # vyos@vyos# run show configuration commands | grep firewall
    # set firewall group address-group 'inbound'


    # Using deleted to delete firewall rules based on afi
    #
    # Before state
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv6 name UPLINK rule 1 action 'accept'
    # set firewall ipv6 name UPLINK rule 1
    # set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'
    # set firewall ipv6 name UPLINK rule 2 action 'accept'
    # set firewall ipv6 name UPLINK rule 2
    # set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'
    # set firewall group address-group 'inbound'
    # set firewall ipv4 name Downlink default-action 'accept'
    # set firewall ipv4 name Downlink description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name Downlink rule 501 action 'accept'
    # set firewall ipv4 name Downlink rule 501 description 'Rule 501 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 501 ipsec 'match-ipsec'
    # set firewall ipv4 name Downlink rule 502 action 'reject'
    # set firewall ipv4 name Downlink rule 502 description 'Rule 502 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 502 ipsec 'match-ipsec'

    - name: Delete attributes of given firewall rules.
      vyos.vyos.vyos_firewall_rules:
        config:
          - afi: ipv4
        state: deleted
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #    "before": [
    #        {
    #            "afi": "ipv6",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "This is ipv6 specific rule-set",
    #                    "name": "UPLINK",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 1 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 1
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 2 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 2
    #                        }
    #                    ]
    #                }
    #            ]
    #        },
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "Downlink",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 501 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 501
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 502 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 502
    #                        }
    #                    ]
    #               }
    #            ]
    #        }
    #    ]
    #    "commands": [
    #        "delete firewall ipv4 name"
    #    ]
    #
    # "after": []
    # After state
    # ------------
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv6 name UPLINK rule 1 action 'accept'
    # set firewall ipv6 name UPLINK rule 1
    # set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'
    # set firewall ipv6 name UPLINK rule 2 action 'accept'
    # set firewall ipv6 name UPLINK rule 2
    # set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'


    # Using deleted to delete all the the firewall rules when provided config is empty
    #
    # Before state
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv4 name Downlink default-action 'accept'
    # set firewall ipv4 name Downlink description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name Downlink rule 501 action 'accept'
    # set firewall ipv4 name Downlink rule 501 description 'Rule 501 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 501 ipsec 'match-ipsec'
    # set firewall ipv4 name Downlink rule 502 action 'reject'
    # set firewall ipv4 name Downlink rule 502 description 'Rule 502 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 502 ipsec 'match-ipsec'
    #
    - name: Delete attributes of given firewall rules.
      vyos.vyos.vyos_firewall_rules:
        state: deleted
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #    "before": [
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "Downlink",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 501 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 501
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 502 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 502
    #                        }
    #                    ]
    #               }
    #            ]
    #        }
    #    ]
    #    "commands": [
    #        "delete firewall ipv4 name"
    #    ]
    #
    # "after": []
    # After state
    # ------------
    # vyos@vyos# run show configuration commands | grep firewall
    # set firewall group address-group 'inbound'


    # Using merged
    #
    # Before state:
    # -------------
    #
    # vyos@vyos# run show  configuration commands | grep firewall
    # set firewall group address-group 'inbound'
    #
    - name: Merge the provided configuration with the existing running configuration
      vyos.vyos.vyos_firewall_rules:
        config:
          - afi: ipv6
            rule_sets:
              - name: UPLINK
                description: This is ipv6 specific rule-set
                default_action: accept
                rules:
                  - number: 1
                    action: accept
                    description: Fwipv6-Rule 1 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 2
                    action: accept
                    description: Fwipv6-Rule 2 is configured by Ansible
                    ipsec: match-ipsec
          - afi: ipv4
            rule_sets:
              - name: INBOUND
                description: IPv4 INBOUND rule set
                default_action: accept
                rules:
                  - number: 101
                    action: accept
                    description: Rule 101 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 102
                    action: reject
                    description: Rule 102 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 103
                    action: accept
                    description: Rule 103 is configured by Ansible
                    destination:
                      group:
                        address_group: inbound
                    source:
                      address: 192.0.2.0
                    state:
                      established: true
                      new: false
                      invalid: false
                      related: true
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
    #       "set firewall ipv6 name UPLINK default-action 'accept'",
    #       "set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'",
    #       "set firewall ipv6 name UPLINK rule 1 action 'accept'",
    #       "set firewall ipv6 name UPLINK rule 1",
    #       "set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'",
    #       "set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'",
    #       "set firewall ipv6 name UPLINK rule 2 action 'accept'",
    #       "set firewall ipv6 name UPLINK rule 2",
    #       "set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'",
    #       "set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'",
    #       "set firewall ipv4 name INBOUND default-action 'accept'",
    #       "set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'",
    #       "set firewall ipv4 name INBOUND rule 101 action 'accept'",
    #       "set firewall ipv4 name INBOUND rule 101",
    #       "set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
    #       "set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'",
    #       "set firewall ipv4 name INBOUND rule 102 action 'reject'",
    #       "set firewall ipv4 name INBOUND rule 102",
    #       "set firewall ipv4 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
    #       "set firewall ipv4 name INBOUND rule 102 ipsec 'match-ipsec'",
    #       "set firewall ipv4 name INBOUND rule 103 description 'Rule 103 is configured by Ansible'",
    #       "set firewall ipv4 name INBOUND rule 103 destination group address-group inbound",
    #       "set firewall ipv4 name INBOUND rule 103",
    #       "set firewall ipv4 name INBOUND rule 103 source address 192.0.2.0",
    #       "set firewall ipv4 name INBOUND rule 103 state established",
    #       "set firewall ipv4 name INBOUND rule 103 state related",
    #       "set firewall ipv4 name INBOUND rule 103 action 'accept'"
    #    ]
    #
    # "after": [
    #        {
    #            "afi": "ipv6",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "This is ipv6 specific rule-set",
    #                    "name": "UPLINK",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 1 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 1
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 2 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 2
    #                        }
    #                    ]
    #                }
    #            ]
    #        },
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "INBOUND",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 101 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 101
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 102 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 102
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 103 is configured by Ansible",
    #                            "destination": {
    #                                "group": {
    #                                    "address_group": "inbound"
    #                                }
    #                            },
    #                            "number": 103,
    #                            "source": {
    #                                "address": "192.0.2.0"
    #                            },
    #                            "state": {
    #                                "established": true,
    #                                "invalid": false,
    #                                "new": false,
    #                                "related": true
    #                            }
    #                        }
    #                    ]
    #                }
    #            ]
    #        }
    #    ]
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv6 name UPLINK rule 1 action 'accept'
    # set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'
    # set firewall ipv6 name UPLINK rule 2 action 'accept'
    # set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND default-action 'accept'
    # set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name INBOUND rule 101 action 'accept'
    # set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 102 action 'reject'
    # set firewall ipv4 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 102 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 103 action 'accept'
    # set firewall ipv4 name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 103 destination group address-group 'inbound'
    # set firewall ipv4 name INBOUND rule 103 source address '192.0.2.0'
    # set firewall ipv4 name INBOUND rule 103 state established
    # set firewall ipv4 name INBOUND rule 103 state related


    # Using replaced
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv6 name UPLINK rule 1 action 'accept'
    # set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'
    # set firewall ipv6 name UPLINK rule 2 action 'accept'
    # set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND default-action 'accept'
    # set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name INBOUND rule 101 action 'accept'
    # set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 102 action 'reject'
    # set firewall ipv4 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 102 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 103 action 'accept'
    # set firewall ipv4 name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 103 destination group address-group 'inbound'
    # set firewall ipv4 name INBOUND rule 103 source address '192.0.2.0'
    # set firewall ipv4 name INBOUND rule 103 state established
    # set firewall ipv4 name INBOUND rule 103 state related
    #
    - name: >-
        Replace device configurations of listed firewall rules with provided
        configurations
      vyos.vyos.vyos_firewall_rules:
        config:
          - afi: ipv6
            rule_sets:
              - name: UPLINK
                description: This is ipv6 specific rule-set
                default_action: accept
          - afi: ipv4
            rule_sets:
              - name: INBOUND
                description: IPv4 INBOUND rule set
                default_action: accept
                rules:
                  - number: 101
                    action: accept
                    description: Rule 101 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 104
                    action: reject
                    description: Rule 104 is configured by Ansible
                    ipsec: match-none
        state: replaced
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "before": [
    #        {
    #            "afi": "ipv6",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "This is ipv6 specific rule-set",
    #                    "name": "UPLINK",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 1 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 1
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 2 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 2
    #                        }
    #                    ]
    #                }
    #            ]
    #        },
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "INBOUND",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 101 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 101
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 102 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 102
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 103 is configured by Ansible",
    #                            "destination": {
    #                                "group": {
    #                                    "address_group": "inbound"
    #                                }
    #                            },
    #                            "number": 103,
    #                            "source": {
    #                                "address": "192.0.2.0"
    #                            },
    #                            "state": {
    #                                "established": true,
    #                                "invalid": false,
    #                                "new": false,
    #                                "related": true
    #                            }
    #                        }
    #                    ]
    #                }
    #            ]
    #        }
    #    ]
    #
    # "commands": [
    #        "delete firewall ipv6 name UPLINK rule 1",
    #        "delete firewall ipv6 name UPLINK rule 2",
    #        "delete firewall ipv4 name INBOUND rule 102",
    #        "delete firewall ipv4 name INBOUND rule 103",
    #        "set firewall ipv4 name INBOUND rule 104 action 'reject'",
    #        "set firewall ipv4 name INBOUND rule 104 description 'Rule 104 is configured by Ansible'",
    #        "set firewall ipv4 name INBOUND rule 104",
    #        "set firewall ipv4 name INBOUND rule 104 ipsec 'match-none'"
    #    ]
    #
    #    "after": [
    #        {
    #            "afi": "ipv6",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "This is ipv6 specific rule-set",
    #                    "name": "UPLINK"
    #                }
    #            ]
    #        },
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "INBOUND",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 101 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 101
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 104 is configured by Ansible",
    #                            "ipsec": "match-none",
    #                            "number": 104
    #                        }
    #                    ]
    #                }
    #            ]
    #        }
    #    ]
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv4 name INBOUND default-action 'accept'
    # set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name INBOUND rule 101 action 'accept'
    # set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 104 action 'reject'
    # set firewall ipv4 name INBOUND rule 104 description 'Rule 104 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 104 ipsec 'match-none'


    # Using overridden
    #
    # Before state
    # --------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv4 name INBOUND default-action 'accept'
    # set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name INBOUND rule 101 action 'accept'
    # set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 104 action 'reject'
    # set firewall ipv4 name INBOUND rule 104 description 'Rule 104 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 104 ipsec 'match-none'
    #
    - name: Overrides all device configuration with provided configuration
      vyos.vyos.vyos_firewall_rules:
        config:
          - afi: ipv4
            rule_sets:
              - name: Downlink
                description: IPv4 INBOUND rule set
                default_action: accept
                rules:
                  - number: 501
                    action: accept
                    description: Rule 501 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 502
                    action: reject
                    description: Rule 502 is configured by Ansible
                    ipsec: match-ipsec
        state: overridden
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    # "before": [
    #        {
    #            "afi": "ipv6",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "This is ipv6 specific rule-set",
    #                    "name": "UPLINK"
    #                }
    #            ]
    #        },
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "INBOUND",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 101 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 101
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 104 is configured by Ansible",
    #                            "ipsec": "match-none",
    #                            "number": 104
    #                        }
    #                    ]
    #                }
    #            ]
    #        }
    #    ]
    #
    #    "commands": [
    #        "delete firewall ipv6 name UPLINK",
    #        "delete firewall ipv4 name INBOUND",
    #        "set firewall ipv4 name Downlink default-action 'accept'",
    #        "set firewall ipv4 name Downlink description 'IPv4 INBOUND rule set'",
    #        "set firewall ipv4 name Downlink rule 501 action 'accept'",
    #        "set firewall ipv4 name Downlink rule 501",
    #        "set firewall ipv4 name Downlink rule 501 description 'Rule 501 is configured by Ansible'",
    #        "set firewall ipv4 name Downlink rule 501 ipsec 'match-ipsec'",
    #        "set firewall ipv4 name Downlink rule 502 action 'reject'",
    #        "set firewall ipv4 name Downlink rule 502",
    #        "set firewall ipv4 name Downlink rule 502 description 'Rule 502 is configured by Ansible'",
    #        "set firewall ipv4 name Downlink rule 502 ipsec 'match-ipsec'"
    #
    #
    #    "after": [
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "Downlink",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 501 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 501
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 502 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 502
    #                        }
    #                    ]
    #               }
    #            ]
    #        }
    #    ]
    #
    #
    # After state
    # ------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv4 name Downlink default-action 'accept'
    # set firewall ipv4 name Downlink description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name Downlink rule 501 action 'accept'
    # set firewall ipv4 name Downlink rule 501 description 'Rule 501 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 501 ipsec 'match-ipsec'
    # set firewall ipv4 name Downlink rule 502 action 'reject'
    # set firewall ipv4 name Downlink rule 502 description 'Rule 502 is configured by Ansible'
    # set firewall ipv4 name Downlink rule 502 ipsec 'match-ipsec'


    # Using gathered
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv6 name UPLINK rule 1 action 'accept'
    # set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'
    # set firewall ipv6 name UPLINK rule 2 action 'accept'
    # set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND default-action 'accept'
    # set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name INBOUND rule 101 action 'accept'
    # set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 102 action 'reject'
    # set firewall ipv4 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 102 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 103 action 'accept'
    # set firewall ipv4 name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 103 destination group address-group 'inbound'
    # set firewall ipv4 name INBOUND rule 103 source address '192.0.2.0'
    # set firewall ipv4 name INBOUND rule 103 state established
    # set firewall ipv4 name INBOUND rule 103 state related
    #
    - name: Gather listed firewall rules with provided configurations
      vyos.vyos.vyos_firewall_rules:
        config:
        state: gathered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "gathered": [
    #        {
    #            "afi": "ipv6",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "This is ipv6 specific rule-set",
    #                    "name": "UPLINK",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 1 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 1
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Fwipv6-Rule 2 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 2
    #                        }
    #                    ]
    #                }
    #            ]
    #        },
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "INBOUND",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 101 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 101
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 102 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 102
    #                        },
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 103 is configured by Ansible",
    #                            "destination": {
    #                                "group": {
    #                                    "address_group": "inbound"
    #                                }
    #                            },
    #                            "number": 103,
    #                            "source": {
    #                                "address": "192.0.2.0"
    #                            },
    #                            "state": {
    #                                "established": true,
    #                                "invalid": false,
    #                                "new": false,
    #                                "related": true
    #                            }
    #                        }
    #                    ]
    #                }
    #            ]
    #        }
    #    ]
    #
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall group address-group 'inbound'
    # set firewall ipv6 name UPLINK default-action 'accept'
    # set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'
    # set firewall ipv6 name UPLINK rule 1 action 'accept'
    # set firewall ipv6 name UPLINK rule 1 description 'Fwipv6-Rule 1 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 1 ipsec 'match-ipsec'
    # set firewall ipv6 name UPLINK rule 2 action 'accept'
    # set firewall ipv6 name UPLINK rule 2 description 'Fwipv6-Rule 2 is configured by Ansible'
    # set firewall ipv6 name UPLINK rule 2 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND default-action 'accept'
    # set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'
    # set firewall ipv4 name INBOUND rule 101 action 'accept'
    # set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 102 action 'reject'
    # set firewall ipv4 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 102 ipsec 'match-ipsec'
    # set firewall ipv4 name INBOUND rule 103 action 'accept'
    # set firewall ipv4 name INBOUND rule 103 description 'Rule 103 is configured by Ansible'
    # set firewall ipv4 name INBOUND rule 103 destination group address-group 'inbound'
    # set firewall ipv4 name INBOUND rule 103 source address '192.0.2.0'
    # set firewall ipv4 name INBOUND rule 103 state established
    # set firewall ipv4 name INBOUND rule 103 state related


    # Using rendered
    #
    #
    - name: Render the commands for provided  configuration
      vyos.vyos.vyos_firewall_rules:
        config:
          - afi: ipv6
            rule_sets:
              - name: UPLINK
                description: This is ipv6 specific rule-set
                default_action: accept
          - afi: ipv4
            rule_sets:
              - name: INBOUND
                description: IPv4 INBOUND rule set
                default_action: accept
                rules:
                  - number: 101
                    action: accept
                    description: Rule 101 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 102
                    action: reject
                    description: Rule 102 is configured by Ansible
                    ipsec: match-ipsec
                  - number: 103
                    action: accept
                    description: Rule 103 is configured by Ansible
                    destination:
                      group:
                        address_group: inbound
                    source:
                      address: 192.0.2.0
                    state:
                      established: true
                      new: false
                      invalid: false
                      related: true
        state: rendered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "rendered": [
    #        "set firewall ipv6 name UPLINK default-action 'accept'",
    #        "set firewall ipv6 name UPLINK description 'This is ipv6 specific rule-set'",
    #        "set firewall ipv4 name INBOUND default-action 'accept'",
    #        "set firewall ipv4 name INBOUND description 'IPv4 INBOUND rule set'",
    #        "set firewall ipv4 name INBOUND rule 101 action 'accept'",
    #        "set firewall ipv4 name INBOUND rule 101",
    #        "set firewall ipv4 name INBOUND rule 101 description 'Rule 101 is configured by Ansible'",
    #        "set firewall ipv4 name INBOUND rule 101 ipsec 'match-ipsec'",
    #        "set firewall ipv4 name INBOUND rule 102 action 'reject'",
    #        "set firewall ipv4 name INBOUND rule 102",
    #        "set firewall ipv4 name INBOUND rule 102 description 'Rule 102 is configured by Ansible'",
    #        "set firewall ipv4 name INBOUND rule 102 ipsec 'match-ipsec'",
    #        "set firewall ipv4 name INBOUND rule 103 description 'Rule 103 is configured by Ansible'",
    #        "set firewall ipv4 name INBOUND rule 103 destination group address-group inbound",
    #        "set firewall ipv4 name INBOUND rule 103",
    #        "set firewall ipv4 name INBOUND rule 103 source address 192.0.2.0",
    #        "set firewall ipv4 name INBOUND rule 103 state established",
    #        "set firewall ipv4 name INBOUND rule 103 state related",
    #        "set firewall ipv4 name INBOUND rule 103 action 'accept'"
    #    ]


    # Using parsed
    #
    #
    - name: Parse the commands for provided configuration
      vyos.vyos.vyos_firewall_rules:
        running_config:
          "set firewall group address-group 'inbound'
           set firewall ipv4 name Downlink default-action 'accept'
           set firewall ipv4 name Downlink description 'IPv4 INBOUND rule set'
           set firewall ipv4 name Downlink rule 501 action 'accept'
           set firewall ipv4 name Downlink rule 501 description 'Rule 501 is configured by Ansible'
           set firewall ipv4 name Downlink rule 501 ipsec 'match-ipsec'
           set firewall ipv4 name Downlink rule 502 action 'reject'
           set firewall ipv4 name Downlink rule 502 description 'Rule 502 is configured by Ansible'
           set firewall ipv4 name Downlink rule 502 ipsec 'match-ipsec'"
        state: parsed
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "parsed": [
    #        {
    #            "afi": "ipv4",
    #            "rule_sets": [
    #                {
    #                    "default_action": "accept",
    #                    "description": "IPv4 INBOUND rule set",
    #                    "name": "Downlink",
    #                    "rules": [
    #                        {
    #                            "action": "accept",
    #                            "description": "Rule 501 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 501
    #                        },
    #                        {
    #                            "action": "reject",
    #                            "description": "Rule 502 is configured by Ansible",
    #                            "ipsec": "match-ipsec",
    #                            "number": 502
    #                        }
    #                    ]
    #                }
    #            ]
    #        }
    #    ]



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set firewall ipv4 name Downlink default-action &#x27;accept&#x27;&quot;, &quot;set firewall ipv4 name Downlink description &#x27;IPv4 INBOUND rule set&#x27;&quot;, &quot;set firewall ipv4 name Downlink rule 501 action &#x27;accept&#x27;&quot;, &quot;set firewall ipv4 name Downlink rule 502 description &#x27;Rule 502 is configured by Ansible&#x27;&quot;, &quot;set firewall ipv4 name Downlink rule 502 ipsec &#x27;match-ipsec&#x27;&quot;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set firewall ipv4 name Downlink default-action &#x27;accept&#x27;&quot;, &quot;set firewall ipv4 name Downlink description &#x27;IPv4 INBOUND rule set&#x27;&quot;, &quot;set firewall ipv4 name Downlink rule 501 action &#x27;accept&#x27;&quot;, &quot;set firewall ipv4 name Downlink rule 502 description &#x27;Rule 502 is configured by Ansible&#x27;&quot;, &quot;set firewall ipv4 name Downlink rule 502 ipsec &#x27;match-ipsec&#x27;&quot;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
- Gaige B. Paulsen (@gaige)
