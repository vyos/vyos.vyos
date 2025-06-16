.. _vyos.vyos.vyos_vrf_module:


******************
vyos.vyos.vyos_vrf
******************

**VRF resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages vrf configuration on devices running Vyos




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
                        <div>List of vrf configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bind_to_all</b>
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
                        <div>Enable binding services to all VRFs</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>instances</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Virtual Routing and Forwarding instance</div>
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
                        <div>Address family configuration</div>
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
                        <div>Address family identifier</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable_forwarding</b>
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
                        <div>Disable forwarding for this address family</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nht_no_resolve_via_default</b>
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
                        <div>Disable next-hop resolution via default route</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_maps</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of route maps for this address family</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>any</li>
                                    <li>babel</li>
                                    <li>bgp</li>
                                    <li>connected</li>
                                    <li>eigrp</li>
                                    <li>isis</li>
                                    <li>kernel</li>
                                    <li>ospf</li>
                                    <li>rip</li>
                                    <li>static</li>
                                    <li>table</li>
                        </ul>
                </td>
                <td>
                        <div>Protocol to which the route map applies</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rm_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
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
                        <div>Description</div>
                </td>
            </tr>
            <tr>
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
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Administratively disable interface</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: disabled</div>
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
                        <div>VRF instance name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>table_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Routing table associated with this instance</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vni</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Virtual Network Identifier</div>
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
                        <div>The value of this option should be the output received from the VYOS device by executing the command <b>show configuration commands |  match &quot;set vrf&quot;</b>.</div>
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>show configuration commands |  match &quot;set vrf&quot;</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
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
   - Tested against vyos 1.5-stream-2025-Q1
   - This module works with connection ``network_cli``.



Examples
--------

.. code-block:: yaml

    # # -------------------
    # # 1. Using merged
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #      set vrf name vrf-blue description 'blue-vrf'
    #      set vrf name vrf-blue disable
    #      set vrf name vrf-blue table '100'
    #      set vrf name vrf-blue vni '1000'
    #   vyos@vyos:~$

    # # Task
    # # -------------
      - name: Merge provided configuration with device configuration
        vyos.vyos.vyos_vrf:
          config:
            instances:
              - name: "vrf-green"
                description: "green-vrf"
                table_id: 110
                vni: 1010

    # Task output:
    # -------------
        # "after": {
        #     "bind_to_all": false,
        #     "instances": [
        #         {
        #             "description": "blue-vrf",
        #             "disable": true,
        #             "name": "vrf-blue",
        #             "table_id": 100,
        #             "vni": 1000
        #         },
        #         {
        #             "description": "green-vrf",
        #             "disable": false,
        #             "name": "vrf-green",
        #             "table_id": 110,
        #             "vni": 1010
        #         }
        #     ]
        # },
        # "before": {
        #     "bind_to_all": false,
        #     "instances": [
        #         {
        #             "description": "blue-vrf",
        #             "disable": true,
        #             "name": "vrf-blue",
        #             "table_id": 100,
        #             "vni": 1000
        #         }
        #     ]
        # },
        # "changed": true,
        # "commands": [
        #     "set vrf name vrf-green table 110",
        #     "set vrf name vrf-green vni 1010",
        #     "set vrf name vrf-green description green-vrf"
        # ]

    # After state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands |  match 'set vrf'
    #     set vrf name vrf-blue description 'blue-vrf'
    #     set vrf name vrf-blue disable
    #     set vrf name vrf-blue table '100'
    #     set vrf name vrf-blue vni '1000'
    #     set vrf name vrf-green description 'green-vrf'
    #     set vrf name vrf-green table '110'
    #     set vrf name vrf-green vni '1010'
    #   vyos@vyos:~$

    # # -------------------
    # # 2. Using replaced
    # # -------------------

    # # Before state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
          # set vrf bind-to-all
          # set vrf name vrf-blue description 'blue-vrf'
          # set vrf name vrf-blue table '100'
          # set vrf name vrf-blue vni '1000'
          # set vrf name vrf-red description 'red-vrf'
          # set vrf name vrf-red disable
          # set vrf name vrf-red ip disable-forwarding
          # set vrf name vrf-red ip protocol kernel route-map 'rm1'
          # set vrf name vrf-red ip protocol rip route-map 'rm1'
          # set vrf name vrf-red table '101'
          # set vrf name vrf-red vni '1001'
          # vyos@vyos:~$


    # # Task
    # # -------------
      - name: Merge provided configuration with device configuration
        vyos.vyos.vyos_vrf:
          config:
            bind_to_all: true
            instances:
              - name: "vrf-blue"
                description: "blue-vrf"
                disable: false
                table_id: 100
                vni: 1002
              - name: "vrf-red"
                description: "red-vrf"
                disable: false
                table_id: 101
                vni: 1001
                address_family:
                  - afi: "ipv4"
                    disable_forwarding: false
                    route_maps:
                      - rm_name: "rm1"
                        protocol: "kernel"
                      - rm_name: "rm1"
                        protocol: "ospf"
                  - afi: "ipv6"
                    nht_no_resolve_via_default: true
          state: replaced

    # # Task output:
    # # -------------
      # "after": {
      #     "bind_to_all": true,
      #     "instances": [
      #         {
      #             "description": "blue-vrf",
      #             "disable": false,
      #             "name": "vrf-blue",
      #             "table_id": 100,
      #             "vni": 1002
      #         },
      #         {
      #             "address_family": [
      #                 {
      #                     "afi": "ipv4",
      #                     "disable_forwarding": false,
      #                     "nht_no_resolve_via_default": false,
      #                     "route_maps": [
      #                         {
      #                             "protocol": "kernel",
      #                             "rm_name": "rm1"
      #                         },
      #                         {
      #                             "protocol": "ospf",
      #                             "rm_name": "rm1"
      #                         },
      #                         {
      #                             "protocol": "rip",
      #                             "rm_name": "rm1"
      #                         }
      #                     ]
      #                 },
      #                 {
      #                     "afi": "ipv6",
      #                     "disable_forwarding": false,
      #                     "nht_no_resolve_via_default": true
      #                 }
      #             ],
      #             "description": "red-vrf",
      #             "disable": false,
      #             "name": "vrf-red",
      #             "table_id": 101,
      #             "vni": 1001
      #         }
      #     ]
      # },
      # "before": {
      #     "bind_to_all": true,
      #     "instances": [
      #         {
      #             "description": "blue-vrf",
      #             "disable": false,
      #             "name": "vrf-blue",
      #             "table_id": 100,
      #             "vni": 1000
      #         },
      #         {
      #             "address_family": [
      #                 {
      #                     "afi": "ipv4",
      #                     "disable_forwarding": true,
      #                     "nht_no_resolve_via_default": false,
      #                     "route_maps": [
      #                         {
      #                             "protocol": "kernel",
      #                             "rm_name": "rm1"
      #                         },
      #                         {
      #                             "protocol": "rip",
      #                             "rm_name": "rm1"
      #                         }
      #                     ]
      #                 }
      #             ],
      #             "description": "red-vrf",
      #             "disable": true,
      #             "name": "vrf-red",
      #             "table_id": 101,
      #             "vni": 1001
      #         }
      #     ]
      # },
      # "changed": true,
      # "commands": [
      #     "set vrf name vrf-blue vni 1002",
      #     "delete vrf name vrf-red disable",
      #     "set vrf name vrf-red ip protocol ospf route-map rm1",
      #     "delete vrf name vrf-red ip disable-forwarding",
      #     "set vrf name vrf-red ipv6 nht no-resolve-via-default"
      # ]

    # After state:
    # # -------------
        # vyos@vyos:~$
          # set vrf bind-to-all
          # set vrf name vrf-blue description 'blue-vrf'
          # set vrf name vrf-blue table '100'
          # set vrf name vrf-blue vni '1002'
          # set vrf name vrf-red description 'red-vrf'
          # set vrf name vrf-red ip protocol kernel route-map 'rm1'
          # set vrf name vrf-red ip protocol ospf route-map 'rm1'
          # set vrf name vrf-red ip protocol rip route-map 'rm1'
          # set vrf name vrf-red ipv6 nht no-resolve-via-default
          # set vrf name vrf-red table '101'
          # set vrf name vrf-red vni '1001'
        # vyos@vyos:~$


    # # -------------------
    # # 3. Using overridden
    # # -------------------

    # # Before state:
    # # -------------
      # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        # set vrf bind-to-all
        # set vrf name vrf-blue description 'blue-vrf'
        # set vrf name vrf-blue table '100'
        # set vrf name vrf-blue vni '1000'
        # set vrf name vrf-red description 'red-vrf'
        # set vrf name vrf-red disable
        # set vrf name vrf-red ip disable-forwarding
        # set vrf name vrf-red ip protocol kernel route-map 'rm1'
        # set vrf name vrf-red ip protocol rip route-map 'rm1'
        # set vrf name vrf-red table '101'
        # set vrf name vrf-red vni '1001'
      # vyos@vyos:~$

    # Task
    # -------------
      - name: Overridden provided configuration with device configuration
        vyos.vyos.vyos_vrf:
          config:
            bind_to_all: true
            instances:
              - name: "vrf-blue"
                description: "blue-vrf"
                disable: true
                table_id: 100
                vni: 1000
              - name: "vrf-red"
                description: "red-vrf"
                disable: true
                table_id: 101
                vni: 1001
                address_family:
                  - afi: "ipv4"
                    disable_forwarding: false
                    route_maps:
                      - rm_name: "rm1"
                        protocol: "kernel"
                      - rm_name: "rm1"
                        protocol: "rip"
                  - afi: "ipv6"
                    nht_no_resolve_via_default: false
          state: overridden

    # # Task output:
    # # -------------
        "after": {
            "bind_to_all": true,
            "instances": [
                {
                    "description": "blue-vrf",
                    "disable": true,
                    "name": "vrf-blue",
                    "table_id": 100,
                    "vni": 1000
                },
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": false,
                            "nht_no_resolve_via_default": false,
                            "route_maps": [
                                {
                                    "protocol": "kernel",
                                    "rm_name": "rm1"
                                },
                                {
                                    "protocol": "rip",
                                    "rm_name": "rm1"
                                }
                            ]
                        }
                    ],
                    "description": "red-vrf",
                    "disable": true,
                    "name": "vrf-red",
                    "table_id": 101,
                    "vni": 1001
                }
            ]
        },
        "before": {
            "bind_to_all": true,
            "instances": [
                {
                    "description": "blue-vrf",
                    "disable": false,
                    "name": "vrf-blue",
                    "table_id": 100,
                    "vni": 1000
                },
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": true,
                            "nht_no_resolve_via_default": false,
                            "route_maps": [
                                {
                                    "protocol": "kernel",
                                    "rm_name": "rm1"
                                },
                                {
                                    "protocol": "rip",
                                    "rm_name": "rm1"
                                }
                            ]
                        }
                    ],
                    "description": "red-vrf",
                    "disable": true,
                    "name": "vrf-red",
                    "table_id": 101,
                    "vni": 1001
                }
            ]
        },
        "changed": true,
        "commands": [
            "delete vrf name vrf-blue",
            "commit",
            "delete vrf name vrf-red",
            "commit",
            "set vrf name vrf-blue table 100",
            "set vrf name vrf-blue vni 1000",
            "set vrf name vrf-blue description blue-vrf",
            "set vrf name vrf-blue disable",
            "set vrf name vrf-red table 101",
            "set vrf name vrf-red vni 1001",
            "set vrf name vrf-red description red-vrf",
            "set vrf name vrf-red disable",
            "set vrf name vrf-red ip protocol kernel route-map rm1",
            "set vrf name vrf-red ip protocol rip route-map rm1"
        ]

    # After state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        #   set vrf bind-to-all
        #   set vrf name vrf-blue description 'blue-vrf'
        #   set vrf name vrf-blue disable
        #   set vrf name vrf-blue table '100'
        #   set vrf name vrf-blue vni '1000'
        #   set vrf name vrf-red description 'red-vrf'
        #   set vrf name vrf-red disable
        #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
        #   set vrf name vrf-red ip protocol rip route-map 'rm1'
        #   set vrf name vrf-red table '101'
        #   set vrf name vrf-red vni '1001'
        # vyos@vyos:~$

    # 4. Using gathered
    # -------------------

    # # Before state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        #   set vrf bind-to-all
        #   set vrf name vrf-blue description 'blue-vrf'
        #   set vrf name vrf-blue table '100'
        #   set vrf name vrf-blue vni '1000'
        #   set vrf name vrf-red description 'red-vrf'
        #   set vrf name vrf-red disable
        #   set vrf name vrf-red ip disable-forwarding
        #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
        #   set vrf name vrf-red ip protocol rip route-map 'rm1'
        #   set vrf name vrf-red table '101'
        #   set vrf name vrf-red vni '1001'
        # vyos@vyos:~$

    # Task
    # -------------
    - name: Gather provided configuration with device configuration
      vyos.vyos.vyos_vrf:
        config:
        state: gathered

    # # Task output:
    # # -------------
        "gathered": {
            "bind_to_all": true,
            "instances": [
                {
                    "description": "blue-vrf",
                    "disable": false,
                    "name": "vrf-blue",
                    "table_id": 100,
                    "vni": 1000
                },
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": true,
                            "nht_no_resolve_via_default": false,
                            "route_maps": [
                                {
                                    "protocol": "kernel",
                                    "rm_name": "rm1"
                                },
                                {
                                    "protocol": "rip",
                                    "rm_name": "rm1"
                                }
                            ]
                        }
                    ],
                    "description": "red-vrf",
                    "disable": true,
                    "name": "vrf-red",
                    "table_id": 101,
                    "vni": 1001
                }
            ]
        }

    # After state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        #   set vrf bind-to-all
        #   set vrf name vrf-blue description 'blue-vrf'
        #   set vrf name vrf-blue table '100'
        #   set vrf name vrf-blue vni '1000'
        #   set vrf name vrf-red description 'red-vrf'
        #   set vrf name vrf-red disable
        #   set vrf name vrf-red ip disable-forwarding
        #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
        #   set vrf name vrf-red ip protocol rip route-map 'rm1'
        #   set vrf name vrf-red table '101'
        #   set vrf name vrf-red vni '1001'
        # vyos@vyos:~$


    # # -------------------
    # # 5. Using deleted
    # # -------------------

    # # Before state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        #   set vrf bind-to-all
        #   set vrf name vrf-blue description 'blue-vrf'
        #   set vrf name vrf-blue table '100'
        #   set vrf name vrf-blue vni '1000'
        #   set vrf name vrf-red description 'red-vrf'
        #   set vrf name vrf-red disable
        #   set vrf name vrf-red ip disable-forwarding
        #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
        #   set vrf name vrf-red ip protocol rip route-map 'rm1'
        #   set vrf name vrf-red table '101'
        #   set vrf name vrf-red vni '1001'
        # vyos@vyos:~$

    # # Task
    # # -------------
    - name: Replace provided configuration with device configuration
      vyos.vyos.vyos_vrf:
        config:
          bind_to_all: false
          instances:
            - name: "vrf-blue"
        state: deleted


    # # Task output:
    # # -------------
        # "after": {
        #     "bind_to_all": false,
        #     "instances": [
        #         {
        #             "address_family": [
        #                 {
        #                     "afi": "ipv4",
        #                     "disable_forwarding": true,
        #                     "nht_no_resolve_via_default": false,
        #                     "route_maps": [
        #                         {
        #                             "protocol": "kernel",
        #                             "rm_name": "rm1"
        #                         },
        #                         {
        #                             "protocol": "rip",
        #                             "rm_name": "rm1"
        #                         }
        #                     ]
        #                 }
        #             ],
        #             "description": "red-vrf",
        #             "disable": true,
        #             "name": "vrf-red",
        #             "table_id": 101,
        #             "vni": 1001
        #         }
        #     ]
        # },
        # "before": {
        #     "bind_to_all": true,
        #     "instances": [
        #         {
        #             "description": "blue-vrf",
        #             "disable": false,
        #             "name": "vrf-blue",
        #             "table_id": 100,
        #             "vni": 1000
        #         },
        #         {
        #             "address_family": [
        #                 {
        #                     "afi": "ipv4",
        #                     "disable_forwarding": true,
        #                     "nht_no_resolve_via_default": false,
        #                     "route_maps": [
        #                         {
        #                             "protocol": "kernel",
        #                             "rm_name": "rm1"
        #                         },
        #                         {
        #                             "protocol": "rip",
        #                             "rm_name": "rm1"
        #                         }
        #                     ]
        #                 }
        #             ],
        #             "description": "red-vrf",
        #             "disable": true,
        #             "name": "vrf-red",
        #             "table_id": 101,
        #             "vni": 1001
        #         }
        #     ]
        # },
        # "changed": true,
        # "commands": [
        #     "delete vrf bind-to-all",
        #     "delete vrf name vrf-blue"
        # ]

    # After state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        #   set vrf name vrf-red description 'red-vrf'
        #   set vrf name vrf-red disable
        #   set vrf name vrf-red ip disable-forwarding
        #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
        #   set vrf name vrf-red ip protocol rip route-map 'rm1'
        #   set vrf name vrf-red table '101'
        #   set vrf name vrf-red vni '1001'
        # vyos@vyos:~$

    # # -------------------
    # # 6. Using rendered
    # # -------------------

    # # Before state:
    # # -------------
        # vyos@vyos:~$ show configuration commands |  match 'set vrf'
        #   set vrf name vrf-red description 'red-vrf'
        #   set vrf name vrf-red disable
        #   set vrf name vrf-red ip disable-forwarding
        #   set vrf name vrf-red ip protocol kernel route-map 'rm1'
        #   set vrf name vrf-red ip protocol rip route-map 'rm1'
        #   set vrf name vrf-red table '101'
        #   set vrf name vrf-red vni '1001'
        # vyos@vyos:~$

    # Task
    # -------------
        - name: Render provided configuration with device configuration
          vyos.vyos.vyos_vrf:
            config:
              bind_to_all: true
              instances:
                - name: "vrf-green"
                  description: "green-vrf"
                  disabled: true
                  table_id: 105
                  vni: 1000
                - name: "vrf-amber"
                  description: "amber-vrf"
                  disable: false
                  table_id: 111
                  vni: 1001
                  address_family:
                    - afi: "ipv4"
                      disable_forwarding: true
                      route_maps:
                        - rm_name: "rm1"
                          protocol: "kernel"
                        - rm_name: "rm1"
                          protocol: "ospf"
                    - afi: "ipv6"
                      nht_no_resolve_via_default: false
            state: rendered

    # # Task output:
    # # -------------
      # "rendered": [
      #     "set vrf bind-to-all",
      #     "set vrf name vrf-green table 105",
      #     "set vrf name vrf-green vni 1000",
      #     "set vrf name vrf-green description green-vrf",
      #     "set vrf name vrf-green disable",
      #     "set vrf name vrf-amber table 111",
      #     "set vrf name vrf-amber vni 1001",
      #     "set vrf name vrf-amber description amber-vrf",
      #     "set vrf name vrf-amber ip protocol kernel route-map rm1",
      #     "set vrf name vrf-amber ip protocol ospf route-map rm1",
      #     "set vrf name vrf-amber ip disable-forwarding"
      # ]

    # # -------------------
    # # 7. Using parsed
    # # -------------------

    # # vrf_parsed.cfg:
    # # -------------
    # set vrf bind-to-all
    # set vrf name vrf1 description 'red'
    # set vrf name vrf1 disable
    # set vrf name vrf1 table 101
    # set vrf name vrf1 vni 501
    # set vrf name vrf2 description 'blah2'
    # set vrf name vrf2 disable
    # set vrf name vrf2 table 102
    # set vrf name vrf2 vni 102
    # set vrf name vrf1 ip disable-forwarding
    # set vrf name vrf1 ip nht no-resolve-via-default
    # set vrf name vrf-red ip protocol kernel route-map 'rm1'
    # set vrf name vrf-red ip protocol ospf route-map 'rm1'
    # set vrf name vrf-red ipv6 nht no-resolve-via-default

    # Task:
    # -------------
    - name: Parse provided configuration with device configuration
      vyos.vyos.vyos_vrf:
        running_config: "{{ lookup('file', './vrf_parsed.cfg') }}"
        state: parsed


    # # Task output:
    # # -------------
    "parsed": {
            "bind_to_all": true,
            "instances": [
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": true,
                            "nht_no_resolve_via_default": true
                        }
                    ],
                    "description": "red",
                    "disable": true,
                    "name": "vrf1"
                },
                {
                    "description": "blah2",
                    "disable": true,
                    "name": "vrf2"
                },
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "disable_forwarding": false,
                            "nht_no_resolve_via_default": false,
                            "route_maps": [
                                {
                                    "protocol": "kernel",
                                    "rm_name": "rm1"
                                },
                                {
                                    "protocol": "ospf",
                                    "rm_name": "rm1"
                                }
                            ]
                        },
                        {
                            "afi": "ipv6",
                            "disable_forwarding": false,
                            "nht_no_resolve_via_default": true
                        }
                    ],
                    "disable": false,
                    "name": "vrf-red"
                }
            ]
        }



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set system ntp server server1 dynamic&#x27;, &#x27;set system ntp server server1 prefer&#x27;, &#x27;set system ntp server server2 noselect&#x27;, &#x27;set system ntp server server2 preempt&#x27;, &#x27;set system ntp server server_add preempt&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set system ntp server server1 dynamic&#x27;, &#x27;set system ntp server server1 prefer&#x27;, &#x27;set system ntp server server2 noselect&#x27;, &#x27;set system ntp server server2 preempt&#x27;, &#x27;set system ntp server server_add preempt&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Evgeny Molotkov (@omnom62)
