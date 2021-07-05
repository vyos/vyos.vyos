.. _vyos.vyos.vyos_prefix_lists_module:


***************************
vyos.vyos.vyos_prefix_lists
***************************

**Prefix-Lists resource module for VyOS**


Version added: 2.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages prefix-lists configuration on devices running VyOS




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
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of prefix-list options</div>
                </td>
            </tr>
                                <tr>
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
                        <div>The Address Family Indicator (AFI) for the prefix-lists</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_lists</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of prefix-list configurations</div>
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
                        <div>A brief text description for the prefix-list</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Rule configurations for the prefix-list</div>
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
                                    <li>permit</li>
                                    <li>deny</li>
                        </ul>
                </td>
                <td>
                        <div>The action to be taken for packets matching a prefix list rule</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>A brief text description for the prefix list rule</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ge</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Minimum prefix length to be matched</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>le</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum prefix list length to be matched</div>
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
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A numeric identifier for the rule</div>
                </td>
            </tr>

            <tr>
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
                        <div>The name of a defined prefix-list</div>
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
                        <div>The value of this option should be the output received from the VyOS device by executing the command <b>show configuration commands | grep prefix-list</b>.</div>
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
   - Tested against VyOS 1.1.8 (helium)
   - This module works with connection ``network_cli``



Examples
--------

.. code-block:: yaml

    # # -------------------
    # # 1. Using merged
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   vyos@vyos:~$

    # # Task
    # # -------------
    #     - name: Merge the provided configuration with the existing running configuration
    #         vyos.vyos.vyos_prefix_lists:
    #             config:
    #             - afi: "ipv4"
    #                 prefix_lists:
    #                 - name: "AnsibleIPv4PrefixList"
    #                     description: "PL configured by ansible"
    #                     entries:
    #                     - sequence: 2
    #                         description: "Rule 2 given by ansible"
    #                         action: "permit"
    #                         prefix: "92.168.10.0/26"
    #                         le: 32

    #                     - sequence: 3
    #                         description: "Rule 3"
    #                         action: "deny"
    #                         prefix: "72.168.2.0/24"
    #                         ge: 26

    #             - afi: "ipv6"
    #                 prefix_lists:
    #                 - name: "AllowIPv6Prefix"
    #                     description: "Configured by ansible for allowing IPv6 networks"
    #                     entries:
    #                     - sequence: 5
    #                         description: "Permit rule"
    #                         action: "permit"
    #                         prefix: "2001:db8:8000::/35"
    #                         le: 37

    #                 - name: DenyIPv6Prefix
    #                     description: "Configured by ansible for disallowing IPv6 networks"
    #                     entries:
    #                     - sequence: 8
    #                         action: deny
    #                         prefix: "2001:db8:2000::/35"
    #                         le: 37
    #             state: merged

    # # Task output:
    # # -------------
    #     "after": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [],
    #     "changed": true,
    #     "commands": [
    #         "set policy prefix-list AnsibleIPv4PrefixList",
    #         "set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'",
    #         "set policy prefix-list6 AllowIPv6Prefix",
    #         "set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'",
    #         "set policy prefix-list6 DenyIPv6Prefix",
    #         "set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'"
    #     ]

    # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$


    # # -------------------
    # # 2. Using replaced
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$

    # # Task:
    # # -------------
    #     - name: Replace prefix-lists configurations of listed prefix-lists with provided configurations
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #           - afi: "ipv4"
    #             prefix_lists:
    #               - name: "AnsibleIPv4PrefixList"
    #                 description: "Configuration replaced by ansible"
    #                 entries:
    #                   - sequence: 3
    #                     description: "Rule 3 replaced by ansible"
    #                     action: "permit"
    #                     prefix: "82.168.2.0/24"
    #                     ge: 26
    #         state: replaced

    # # Task output:
    # # -------------
    #     "after": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configuration replaced by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 3 replaced by ansible",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "82.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "set policy prefix-list AnsibleIPv4PrefixList description 'Configuration replaced by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'permit'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3 replaced by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '82.168.2.0/24'",
    #         "delete policy prefix-list AnsibleIPv4PrefixList rule 2"
    #     ]

    # # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'Configuration replaced by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3 replaced by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '82.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$


    # # -------------------
    # # 3. Using overridden
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$

    # # Task:
    # # -------------
    #     - name: Override all prefix-lists configuration with provided configuration
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #           - afi: "ipv4"
    #             prefix_lists:
    #               - name: "AnsibleIPv4PrefixList"
    #                 description: Rule 2 overridden by ansible
    #                 entries:
    #                   - sequence: 2
    #                     action: "deny"
    #                     ge: 26
    #                     prefix: "82.168.2.0/24"

    #               - name: "OverriddenPrefixList"
    #                 description: Configuration overridden by ansible
    #                 entries:
    #                   - sequence: 10
    #                     action: permit
    #                     prefix: "203.0.113.96/27"
    #                     le: 32
    #         state: overridden

    # # Task output:
    # # -------------
    #     "after": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Rule 2 overridden by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "ge": 26,
    #                             "sequence": 2,
    #                             "prefix": "82.168.2.0/24"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configuration overridden by ansible",
    #                     "name": "OverriddenPrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "sequence": 10,
    #                             "le": 32,
    #                             "prefix": "203.0.113.96/27"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy prefix-list6 AllowIPv6Prefix",
    #         "delete policy prefix-list6 DenyIPv6Prefix",
    #         "set policy prefix-list AnsibleIPv4PrefixList description 'Rule 2 overridden by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'deny'",
    #         "delete policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 ge '26'",
    #         "delete policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '82.168.2.0/24'",
    #         "delete policy prefix-list AnsibleIPv4PrefixList rule 3",
    #         "set policy prefix-list OverriddenPrefixList",
    #         "set policy prefix-list OverriddenPrefixList description 'Configuration overridden by ansible'",
    #         "set policy prefix-list OverriddenPrefixList rule 10",
    #         "set policy prefix-list OverriddenPrefixList rule 10 action 'permit'",
    #         "set policy prefix-list OverriddenPrefixList rule 10 le '32'",
    #         "set policy prefix-list OverriddenPrefixList rule 10 prefix '203.0.113.96/27'"
    #     ]

    # # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'Rule 2 overridden by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '82.168.2.0/24'
    #   set policy prefix-list OverriddenPrefixList description 'Configuration overridden by ansible'
    #   set policy prefix-list OverriddenPrefixList rule 10 action 'permit'
    #   set policy prefix-list OverriddenPrefixList rule 10 le '32'
    #   set policy prefix-list OverriddenPrefixList rule 10 prefix '203.0.113.96/27'
    #   vyos@vyos:~$


    # # -------------------
    # # 4(i). Using deleted (to delete all prefix lists from the device)
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$

    # # Task:
    # # -------------
    #     - name: Delete all prefix-lists
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #         state: deleted

    # # Task output:
    # # -------------
    #     "after": [],
    #     "before": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy prefix-list AnsibleIPv4PrefixList",
    #         "delete policy prefix-list6 AllowIPv6Prefix",
    #         "delete policy prefix-list6 DenyIPv6Prefix"
    #     ]

    # # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   vyos@vyos:~$


    # # -------------------
    # # 4(ii). Using deleted (to delete all prefix lists for an AFI)
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$

    # # Task:
    # # -------------
    #     - name: Delete all prefix-lists for IPv6 AFI
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #           - afi: "ipv6"
    #         state: deleted

    # # Task output:
    # # -------------
    #     "after": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy prefix-list6 AllowIPv6Prefix",
    #         "delete policy prefix-list6 DenyIPv6Prefix"
    #     ]

    # # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   vyos@vyos:~$


    # # -------------------
    # # 4(iii). Using deleted (to delete single prefix list by name in different AFIs)
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    #   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    #   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
    #   vyos@vyos:~$

    # # Task:
    # # -------------
    #     - name: Delete a single prefix-list from different AFIs
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #           - afi: "ipv4"
    #             prefix_lists:
    #               - name: "AnsibleIPv4PrefixList"
    #           - afi: "ipv6"
    #             prefix_lists:
    #               - name: "DenyIPv6Prefix"
    #         state: deleted

    # # Task output:
    # # -------------
    #     "after": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "delete policy prefix-list AnsibleIPv4PrefixList",
    #         "delete policy prefix-list6 DenyIPv6Prefix"
    #     ]

    # # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep prefix-list
    #   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    #   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    #   vyos@vyos:~$


    # # -------------------
    # # 5. Using gathered
    # # -------------------

    # # Task:
    # # -------------
    #     - name: Gather prefix-lists configurations
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #         state: gathered

    # # Task output:
    # # -------------
    #     "gathered": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
    #     ]


    # # -------------------
    # # 6. Using rendered
    # # -------------------

    # # Task:
    # # -------------
    #     - name: Render commands externally for the described prefix-list configurations
    #       vyos.vyos.vyos_prefix_lists:
    #         config:
    #           - afi: "ipv4"
    #             prefix_lists:
    #               - name: "AnsibleIPv4PrefixList"
    #                 description: "PL configured by ansible"
    #                 entries:
    #                   - sequence: 2
    #                     description: "Rule 2 given by ansible"
    #                     action: "permit"
    #                     prefix: "92.168.10.0/26"
    #                     le: 32

    #                   - sequence: 3
    #                     description: "Rule 3"
    #                     action: "deny"
    #                     prefix: "72.168.2.0/24"
    #                     ge: 26

    #           - afi: "ipv6"
    #             prefix_lists:
    #               - name: "AllowIPv6Prefix"
    #                 description: "Configured by ansible for allowing IPv6 networks"
    #                 entries:
    #                   - sequence: 5
    #                     description: "Permit rule"
    #                     action: "permit"
    #                     prefix: "2001:db8:8000::/35"
    #                     le: 37

    #               - name: DenyIPv6Prefix
    #                 description: "Configured by ansible for disallowing IPv6 networks"
    #                 entries:
    #                   - sequence: 8
    #                     action: deny
    #                     prefix: "2001:db8:2000::/35"
    #                     le: 37
    #         state: rendered

    # # Task output:
    # # -------------
    #     "rendered": [
    #         "set policy prefix-list AnsibleIPv4PrefixList",
    #         "set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'",
    #         "set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'",
    #         "set policy prefix-list6 AllowIPv6Prefix",
    #         "set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'",
    #         "set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'",
    #         "set policy prefix-list6 DenyIPv6Prefix",
    #         "set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'",
    #         "set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'"
    #     ]


    # # -------------------
    # # 7. Using parsed
    # # -------------------

    # # sample_config.cfg:
    # # -------------
    # set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
    # set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
    # set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
    # set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
    # set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
    # set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
    # set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
    # set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
    # set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
    # set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
    # set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
    # set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
    # set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
    # set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
    # set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
    # set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
    # set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
    # set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'

    # # Task:
    # # -------------
    #     - name: Parse externally provided prefix-lists configuration
    #       vyos.vyos.vyos_prefix_lists:
    #         running_config: "{{ lookup('file', './sample_config.cfg') }}"
    #         state: parsed

    # # Task output:
    # # -------------
    #     "parsed": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "description": "PL configured by ansible",
    #                     "name": "AnsibleIPv4PrefixList",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Rule 2 given by ansible",
    #                             "sequence": 2,
    #                             "le": 32,
    #                             "prefix": "92.168.10.0/26"
    #                         },
    #                         {
    #                             "action": "deny",
    #                             "description": "Rule 3",
    #                             "ge": 26,
    #                             "sequence": 3,
    #                             "prefix": "72.168.2.0/24"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "description": "Configured by ansible for allowing IPv6 networks",
    #                     "name": "AllowIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "description": "Permit rule",
    #                             "sequence": 5,
    #                             "le": 37,
    #                             "prefix": "2001:db8:8000::/35"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "description": "Configured by ansible for disallowing IPv6 networks",
    #                     "name": "DenyIPv6Prefix",
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "sequence": 8,
    #                             "le": 37,
    #                             "prefix": "2001:db8:2000::/35"
    #                         }
    #                     ]
    #                 }
    #             ]
    #         }
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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration after the module invocation.</div>
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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em> or <em>deleted</em></td>
                <td>
                            <div>The configuration prior to the module invocation.</div>
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em> or <em>deleted</em></td>
                <td>
                            <div>The set of commands pushed to the remote device for the required configurations to take place.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set policy prefix-list AnsibleIPv4PrefixList description &#x27;PL configured by ansible&#x27;&quot;, &quot;set policy prefix-list AnsibleIPv4PrefixList rule 2 action &#x27;permit&#x27;&quot;, &quot;set policy prefix-list6 AllowIPv6Prefix description &#x27;Configured by ansible for allowing IPv6 networks&#x27;&quot;]</div>
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
                <td>when state is <em>gathered</em></td>
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
                <td>when state is <em>parsed</em></td>
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
                <td>when state is <em>rendered</em></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set policy prefix-list AnsibleIPv4PrefixList description &#x27;PL configured by ansible&#x27;&quot;, &quot;set policy prefix-list AnsibleIPv4PrefixList rule 2 action &#x27;permit&#x27;&quot;, &quot;set policy prefix-list6 AllowIPv6Prefix description &#x27;Configured by ansible for allowing IPv6 networks&#x27;&quot;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Priyam Sahoo (@priyamsahoo)
