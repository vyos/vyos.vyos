.. _vyos.vyos.vyos_snmp_server_module:


**************************
vyos.vyos.vyos_snmp_server
**************************

**Manages snmp_server resource module**


Version added: 2.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the snmp server attributes of Vyos network devices




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
                        <div>SNMP server configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>communities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Community name configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authorization_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ro</li>
                                    <li>rw</li>
                        </ul>
                </td>
                <td>
                        <div>Authorization type (rw or ro)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>clients</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address of SNMP client allowed to contact system</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Community name</div>
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
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Subnet of SNMP client(s) allowed to contact system</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>contact</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Person to contact about the system.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Description information</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>listen_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP address to listen for incoming SNMP requests</div>
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
                        <div>IP address to listen for incoming SNMP requests.</div>
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
                        <div>Port for SNMP service</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>location</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Location information</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>smux_peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Register a subtree for SMUX-based processing.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>snmp_v3</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Simple Network Management Protocol (SNMP) v3</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>engine_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the EngineID as a hex value</div>
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
                        <div>Specifies the group with name groupname</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Specifies the group with name groupname</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ro</li>
                                    <li>rw</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the read/write access</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>seclevel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>auth</li>
                                    <li>priv</li>
                        </ul>
                </td>
                <td>
                        <div>Defines security level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>view</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the name of view</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_targets</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines SNMP target for inform or traps for IP</div>
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
                        <div>IP/IPv6 address of trap target</div>
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
                        <div>Defines the authentication</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the encrypted password for authentication</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>plaintext_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the clear text password for authentication</div>
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
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>md5</li>
                                    <li>sha</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the protocol using for authentication</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>engine_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the engineID.</div>
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
                        <div>Specifies the TCP/UDP port of a destination for SNMP traps/informs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>privacy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the privacy</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the encrypted password for privacy</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>plaintext_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the clear text password for privacy</div>
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
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>des</li>
                                    <li>aes</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the protocol using for privacy</div>
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
                                    <li>tcp</li>
                                    <li>udp</li>
                        </ul>
                </td>
                <td>
                        <div>Defines protocol for notification between TCP and UDP</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>inform</li>
                                    <li>trap</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of notification between inform and trap</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tsm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies that the snmpd uses encryption</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>local_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the server certificate fingerprint or key-file name.</div>
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
                        <div>Defines the port for tsm.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>users</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines username for authentication</div>
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
                        <div>Defines the authentication</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the encrypted password for authentication</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>plaintext_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the clear text password for authentication</div>
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
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>md5</li>
                                    <li>sha</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the protocol using for authentication</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>engine_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the engineID.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Specifies group for user name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ro</li>
                                    <li>rw</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the mode for access rights of user, read only or write</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>privacy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the privacy</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encrypted_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the encrypted password for privacy</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>plaintext_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines the clear text password for privacy</div>
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
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>des</li>
                                    <li>aes</li>
                        </ul>
                </td>
                <td>
                        <div>Defines the protocol using for privacy</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tsm_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies finger print or file name of TSM certificate.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the user with name username</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>views</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the view with name viewname</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>exclude</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Exclude is optional argument.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Defines a bit-mask that is indicating which subidentifiers of the associated subtree OID should be regarded as significant.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>oid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify oid</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>view</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>view name</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SNMP trap source address</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Address of trap target</div>
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
                        <div>Address of trap target</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>community</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Community used when sending trap information</div>
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
                        <div>Destination port used for trap notification</div>
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
                        <div>The state the configuration should be left in.</div>
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>Please refer to examples for more details.</div>
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
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                                    <li>rendered</li>
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
   - Tested against vyos 1.1.8
   - This module works with connection ``network_cli``.
   - The Configuration defaults of the Vyos network devices are supposed to hinder idempotent behavior of plays



Examples
--------

.. code-block:: yaml

    # Using merged
    # Before State:

    # vyos@vyos:~$ show configuration commands | grep snmp
    # vyos@vyos:~$

    - name: Merge provided configuration with device configuration
      vyos.vyos.vyos_snmp_server:
        config:
          communities:
            - name: "switches"
              authorization_type: "rw"
            - name: "bridges"
              clients: ["1.1.1.1", "12.1.1.10"]
          contact: "admin2@ex.com"
          listen_addresses:
            - address: "20.1.1.1"
            - address: "100.1.2.1"
              port: 33
          snmp_v3:
            users:
              - user: admin_user
                authentication:
                  plaintext_key: "abc1234567"
                  type: "sha"
                privacy:
                  plaintext_key: "abc1234567"
                  type: "aes"
        state: merged

    # After State:

    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges client '1.1.1.1'
    # set service snmp community bridges client '12.1.1.10'
    # set service snmp community switches authorization 'rw'
    # set service snmp contact 'admin2@ex.com'
    # set service snmp listen-address 20.1.1.1
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'
    # vyos@vyos:~$
    #
    # Module Execution:
    #
    # "after": {
    #         "communities": [
    #             {
    #                 "clients": [
    #                     "1.1.1.1",
    #                     "12.1.1.10"
    #                 ],
    #                 "name": "bridges"
    #             },
    #             {
    #                 "authorization_type": "rw",
    #                 "name": "switches"
    #             }
    #         ],
    #         "contact": "admin2@ex.com",
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             },
    #             {
    #                 "address": "20.1.1.1"
    #             }
    #         ],
    #         "snmp_v3": {
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 }
    #             ]
    #         }
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "set service snmp community switches authorization rw",
    #         "set service snmp community bridges client 1.1.1.1",
    #         "set service snmp community bridges client 12.1.1.10",
    #         "set service snmp listen-address 20.1.1.1",
    #         "set service snmp listen-address 100.1.2.1 port 33",
    #         "set service snmp v3 user admin_user auth type sha",
    #         "set service snmp v3 user admin_user auth plaintext-key ********",
    #         "set service snmp v3 user admin_user privacy type aes",
    #         "set service snmp v3 user admin_user privacy plaintext-key ********",
    #         "set service snmp contact admin2@ex.com"
    #     ],
    #

    # Using replaced

    # Before State
    # -------------
    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges client '1.1.1.1'
    # set service snmp community bridges client '12.1.1.10'
    # set service snmp community switches authorization 'rw'
    # set service snmp contact 'admin2@ex.com'
    # set service snmp listen-address 20.1.1.1
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'

    - name: Replace SNMP Server configuration
      vyos.vyos.vyos_snmp_server:
        config:
          communities:
            - name: "bridges"
              networks: ["1.1.1.0/24", "12.1.1.0/24"]
          location: "RDU, NC"
          listen_addresses:
            - address: "100.1.2.1"
              port: 33
          snmp_v3:
            groups:
              - group: "default"
                view: "default"
            users:
              - user: admin_user
                authentication:
                  plaintext_key: "abc1234567"
                  type: "sha"
                privacy:
                  plaintext_key: "abc1234567"
                  type: "aes"
                group: "default"
              - user: guest_user2
                authentication:
                  plaintext_key: "opq1234567"
                  type: "sha"
                privacy:
                  plaintext_key: "opq1234567"
                  type: "aes"
            views:
              - view: "default"
                oid: 1

        state: replaced

    # After State:
    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges network '1.1.1.0/24'
    # set service snmp community bridges network '12.1.1.0/24'
    # set service snmp community switches
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp location 'RDU, NC'
    # set service snmp v3 group default view 'default'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user group 'default'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'
    # set service snmp v3 user guest_user2 auth plaintext-key 'opq1234567'
    # set service snmp v3 user guest_user2 auth type 'sha'
    # set service snmp v3 user guest_user2 privacy plaintext-key 'opq1234567'
    # set service snmp v3 user guest_user2 privacy type 'aes'
    # set service snmp v3 view default oid 1
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    # "after": {
    #         "communities": [
    #             {
    #                 "name": "bridges",
    #                 "networks": [
    #                     "1.1.1.0/24",
    #                     "12.1.1.0/24"
    #                 ]
    #             },
    #             {
    #                 "name": "switches"
    #             }
    #         ],
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             }
    #         ],
    #         "location": "RDU, NC",
    #         "snmp_v3": {
    #             "groups": [
    #                 {
    #                     "group": "default",
    #                     "view": "default"
    #                 }
    #             ],
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "group": "default",
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 },
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "guest_user2"
    #                 }
    #             ],
    #             "views": [
    #                 {
    #                     "oid": "1",
    #                     "view": "default"
    #                 }
    #             ]
    #         }
    #     },
    #     "before": {
    #         "communities": [
    #             {
    #                 "clients": [
    #                     "1.1.1.1",
    #                     "12.1.1.10"
    #                 ],
    #                 "name": "bridges"
    #             },
    #             {
    #                 "authorization_type": "rw",
    #                 "name": "switches"
    #             }
    #         ],
    #         "contact": "admin2@ex.com",
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             },
    #             {
    #                 "address": "20.1.1.1"
    #             }
    #         ],
    #         "snmp_v3": {
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 }
    #             ]
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete service snmp contact admin2@ex.com",
    #         "delete service snmp listen-address 20.1.1.1",
    #         "delete service snmp community switches authorization rw",
    #         "delete service snmp community bridges client 12.1.1.10",
    #         "delete service snmp community bridges client 1.1.1.1",
    #         "set service snmp community bridges network 1.1.1.0/24",
    #         "set service snmp community bridges network 12.1.1.0/24",
    #         "set service snmp v3 group default view default",
    #         "set service snmp v3 user admin_user group default",
    #         "set service snmp v3 user guest_user2 auth type sha",
    #         "set service snmp v3 user guest_user2 auth plaintext-key ********",
    #         "set service snmp v3 user guest_user2 privacy type aes",
    #         "set service snmp v3 user guest_user2 privacy plaintext-key ********",
    #         "set service snmp v3 view default oid 1",
    #         "set service snmp location 'RDU, NC'"
    #     ],

    # Using overridden:
    # Before State
    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges client '1.1.1.1'
    # set service snmp community bridges client '12.1.1.10'
    # set service snmp community switches authorization 'rw'
    # set service snmp contact 'admin2@ex.com'
    # set service snmp listen-address 20.1.1.1
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'

    - name: Override SNMP server config
      vyos.vyos.vyos_snmp_server:
        config:
          communities:
            - name: "bridges"
              networks: ["1.1.1.0/24", "12.1.1.0/24"]
          location: "RDU, NC"
          listen_addresses:
            - address: "100.1.2.1"
              port: 33
          snmp_v3:
            groups:
              - group: "default"
                view: "default"
            users:
              - user: admin_user
                authentication:
                  plaintext_key: "abc1234567"
                  type: "sha"
                privacy:
                  plaintext_key: "abc1234567"
                  type: "aes"
                group: "default"
              - user: guest_user2
                authentication:
                  plaintext_key: "opq1234567"
                  type: "sha"
                privacy:
                  plaintext_key: "opq1234567"
                  type: "aes"
            views:
              - view: "default"
                oid: 1
        state: overridden

    # After State:
    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges network '1.1.1.0/24'
    # set service snmp community bridges network '12.1.1.0/24'
    # set service snmp community switches
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp location 'RDU, NC'
    # set service snmp v3 group default view 'default'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user group 'default'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'
    # set service snmp v3 user guest_user2 auth plaintext-key 'opq1234567'
    # set service snmp v3 user guest_user2 auth type 'sha'
    # set service snmp v3 user guest_user2 privacy plaintext-key 'opq1234567'
    # set service snmp v3 user guest_user2 privacy type 'aes'
    # set service snmp v3 view default oid 1
    # vyos@vyos:~$
    #
    #
    # Module Execution:
    # "after": {
    #         "communities": [
    #             {
    #                 "name": "bridges",
    #                 "networks": [
    #                     "1.1.1.0/24",
    #                     "12.1.1.0/24"
    #                 ]
    #             },
    #             {
    #                 "name": "switches"
    #             }
    #         ],
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             }
    #         ],
    #         "location": "RDU, NC",
    #         "snmp_v3": {
    #             "groups": [
    #                 {
    #                     "group": "default",
    #                     "view": "default"
    #                 }
    #             ],
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "group": "default",
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 },
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "guest_user2"
    #                 }
    #             ],
    #             "views": [
    #                 {
    #                     "oid": "1",
    #                     "view": "default"
    #                 }
    #             ]
    #         }
    #     },
    #     "before": {
    #         "communities": [
    #             {
    #                 "clients": [
    #                     "1.1.1.1",
    #                     "12.1.1.10"
    #                 ],
    #                 "name": "bridges"
    #             },
    #             {
    #                 "authorization_type": "rw",
    #                 "name": "switches"
    #             }
    #         ],
    #         "contact": "admin2@ex.com",
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             },
    #             {
    #                 "address": "20.1.1.1"
    #             }
    #         ],
    #         "snmp_v3": {
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 }
    #             ]
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete service snmp contact admin2@ex.com",
    #         "delete service snmp listen-address 20.1.1.1",
    #         "delete service snmp community switches authorization rw",
    #         "delete service snmp community bridges client 12.1.1.10",
    #         "delete service snmp community bridges client 1.1.1.1",
    #         "set service snmp community bridges network 1.1.1.0/24",
    #         "set service snmp community bridges network 12.1.1.0/24",
    #         "set service snmp v3 group default view default",
    #         "set service snmp v3 user admin_user group default",
    #         "set service snmp v3 user guest_user2 auth type sha",
    #         "set service snmp v3 user guest_user2 auth plaintext-key ********",
    #         "set service snmp v3 user guest_user2 privacy type aes",
    #         "set service snmp v3 user guest_user2 privacy plaintext-key ********",
    #         "set service snmp v3 view default oid 1",
    #         "set service snmp location 'RDU, NC'"
    #     ],

    # Using deleted:

    # Before State:
    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges network '1.1.1.0/24'
    # set service snmp community bridges network '12.1.1.0/24'
    # set service snmp community switches
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp location 'RDU, NC'
    # set service snmp v3 group default view 'default'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user group 'default'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'
    # set service snmp v3 user guest_user2 auth plaintext-key 'opq1234567'
    # set service snmp v3 user guest_user2 auth type 'sha'
    # set service snmp v3 user guest_user2 privacy plaintext-key 'opq1234567'
    # set service snmp v3 user guest_user2 privacy type 'aes'
    # set service snmp v3 view default oid 1

    - name: Delete Config
      vyos.vyos.vyos_snmp_server:
        state: deleted

    # After State:
    # vyos@vyos:~$ show configuration commands | grep snmp
    # vyos@vyos:~$
    #
    # Module Execution:
    # "after": {},
    #     "before": {
    #         "communities": [
    #             {
    #                 "name": "bridges",
    #                 "networks": [
    #                     "1.1.1.0/24",
    #                     "12.1.1.0/24"
    #                 ]
    #             },
    #             {
    #                 "name": "switches"
    #             }
    #         ],
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             }
    #         ],
    #         "location": "RDU, NC",
    #         "snmp_v3": {
    #             "groups": [
    #                 {
    #                     "group": "default",
    #                     "view": "default"
    #                 }
    #             ],
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "group": "default",
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 },
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "guest_user2"
    #                 }
    #             ],
    #             "views": [
    #                 {
    #                     "oid": "1",
    #                     "view": "default"
    #                 }
    #             ]
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "delete service snmp"
    #     ],

    # Using rendered:
    - name: Render provided configuration
      vyos.vyos.vyos_snmp_server:
        config:
          communities:
            - name: "switches"
              authorization_type: "rw"
            - name: "bridges"
              clients: ["1.1.1.1", "12.1.1.10"]
          contact: "admin2@ex.com"
          listen_addresses:
            - address: "20.1.1.1"
            - address: "100.1.2.1"
              port: 33
          snmp_v3:
            users:
              - user: admin_user
                authentication:
                  plaintext_key: "abc1234567"
                  type: "sha"
                privacy:
                  plaintext_key: "abc1234567"
                  type: "aes"
        state: rendered

    # Module Execution:
    #  "rendered": [
    #         "set service snmp community switches authorization rw",
    #         "set service snmp community bridges client 1.1.1.1",
    #         "set service snmp community bridges client 12.1.1.10",
    #         "set service snmp listen-address 20.1.1.1",
    #         "set service snmp listen-address 100.1.2.1 port 33",
    #         "set service snmp v3 user admin_user auth type sha",
    #         "set service snmp v3 user admin_user auth plaintext-key ********",
    #         "set service snmp v3 user admin_user privacy type aes",
    #         "set service snmp v3 user admin_user privacy plaintext-key ********",
    #         "set service snmp contact admin2@ex.com"
    #     ]
    #

    # Using Gathered:
    # Before State:

    # vyos@vyos:~$ show configuration commands | grep snmp
    # set service snmp community bridges client '1.1.1.1'
    # set service snmp community bridges client '12.1.1.10'
    # set service snmp community switches authorization 'rw'
    # set service snmp contact 'admin2@ex.com'
    # set service snmp listen-address 20.1.1.1
    # set service snmp listen-address 100.1.2.1 port '33'
    # set service snmp v3 user admin_user auth plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user auth type 'sha'
    # set service snmp v3 user admin_user privacy plaintext-key 'abc1234567'
    # set service snmp v3 user admin_user privacy type 'aes'

    - name: Gather SNMP server config
      vyos.vyos.vyos_snmp_server:
        state: gathered

    # Module Execution:
    #   "gathered": {
    #         "communities": [
    #             {
    #                 "clients": [
    #                     "1.1.1.1",
    #                     "12.1.1.10"
    #                 ],
    #                 "name": "bridges"
    #             },
    #             {
    #                 "authorization_type": "rw",
    #                 "name": "switches"
    #             }
    #         ],
    #         "contact": "admin2@ex.com",
    #         "listen_addresses": [
    #             {
    #                 "address": "100.1.2.1",
    #                 "port": 33
    #             },
    #             {
    #                 "address": "20.1.1.1"
    #             }
    #         ],
    #         "snmp_v3": {
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "admin_user"
    #                 }
    #             ]
    #         }
    #     },

    # Using parsed:

    # _parsed_snmp.cfg
    # set service snmp community routers authorization 'ro'
    # set service snmp community routers client '203.0.113.10'
    # set service snmp community routers client '203.0.113.20'
    # set service snmp community routers network '192.0.2.0/24'
    # set service snmp community routers network '2001::/64'
    # set service snmp contact 'admin@example.com'
    # set service snmp listen-address 172.16.254.36 port '161'
    # set service snmp listen-address 2001::1
    # set service snmp location 'UK, London'
    # set service snmp trap-target 203.0.113.10
    # set service snmp v3 engineid '000000000000000000000002'
    # set service snmp v3 group default mode 'ro'
    # set service snmp v3 group default view 'default'
    # set service snmp v3 user vyos auth plaintext-key 'vyos12345678'
    # set service snmp v3 user vyos auth type 'sha'
    # set service snmp v3 user vyos group 'default'
    # set service snmp v3 user vyos privacy plaintext-key 'vyos12345678'
    # set service snmp v3 user vyos privacy type 'aes'
    # set service snmp v3 view default oid 1

    - name: Parse SNMP server config
      vyos.vyos.vyos_snmp_server:
        running_config: "{{ lookup('file', './_parsed_snmp.cfg') }}"
        state: parsed

    # Module Execution:
    # "parsed": {
    #         "communities": [
    #             {
    #                 "authorization_type": "ro",
    #                 "clients": [
    #                     "203.0.113.10",
    #                     "203.0.113.20"
    #                 ],
    #                 "name": "routers",
    #                 "networks": [
    #                     "192.0.2.0/24",
    #                     "2001::/64"
    #                 ]
    #             }
    #         ],
    #         "contact": "admin@example.com",
    #         "listen_addresses": [
    #             {
    #                 "address": "172.16.254.36",
    #                 "port": 161
    #             },
    #             {
    #                 "address": "2001::1"
    #             }
    #         ],
    #         "location": "UK, London",
    #         "snmp_v3": {
    #             "engine_id": "000000000000000000000002",
    #             "groups": [
    #                 {
    #                     "group": "default",
    #                     "mode": "ro",
    #                     "view": "default"
    #                 }
    #             ],
    #             "users": [
    #                 {
    #                     "authentication": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "sha"
    #                     },
    #                     "group": "default",
    #                     "privacy": {
    #                         "plaintext_key": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
    #                         "type": "aes"
    #                     },
    #                     "user": "vyos"
    #                 }
    #             ],
    #             "views": [
    #                 {
    #                     "oid": "1",
    #                     "view": "default"
    #                 }
    #             ]
    #         },
    #         "trap_target": {
    #             "address": "203.0.113.10"
    #         }
    #     }
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
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">set service snmp community routers authorization &#x27;ro&#x27; set service snmp community routers client &#x27;203.0.113.10&#x27; set service snmp community routers client &#x27;203.0.113.20&#x27; set service snmp community routers network &#x27;192.0.2.0/24&#x27;</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">set service snmp community routers authorization &#x27;ro&#x27; set service snmp community routers client &#x27;203.0.113.10&#x27; set service snmp community routers client &#x27;203.0.113.20&#x27; set service snmp community routers network &#x27;192.0.2.0/24&#x27;</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Gomathi Selvi Srinivasan (@GomathiselviS)
