.. _vyos.vyos.vyos_ntp_global_module:


*************************
vyos.vyos.vyos_ntp_global
*************************

**Manages ntp modules of Vyos network devices**


Version added: 2.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages ntp configuration on devices running Vyos




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
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
                        <div>List of configurations for ntp module</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_clients</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Network Time Protocol (NTP) server options</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>listen_addresses</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>local IP addresses for service to listen on</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Network Time Protocol (NTP) server</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>options</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>noselect</li>
                                    <li>dynamic</li>
                                    <li>pool</li>
                                    <li>preempt</li>
                                    <li>prefer</li>
                        </ul>
                </td>
                <td>
                        <div>server options for NTP</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>server name for NTP</div>
                </td>
            </tr>


            <tr>
                <td colspan="3">
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
                        <div>The value of this option should be the output received from the VYOS device by executing the command <b>show configuration commands | grep ntp</b>.</div>
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>show configuration commands | grep ntp</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
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
   - Tested against vyos 1.3
   - This module works with connection ``network_cli``.



Examples
--------

.. code-block:: yaml

    # # -------------------
    # # 1. Using merged
    # # -------------------

    # # Before state:
    # # -------------
    #   vyos@vyos:~$ show configuration commands | grep ntp
    #     set system ntp server time1.vyos.net
    #     set system ntp server time2.vyos.net
    #     set system ntp server time3.vyos.net
    #   vyos@vyos:~$

    # # Task
    # # -------------
    - name: Replace the existing ntp config with the new config
      vyos.vyos.vyos_ntp_global:
        config:
          allow_clients:
            - 10.6.6.0/24
          listen_addresses:
            - 10.1.3.1
          servers:
            - server: 203.0.113.0
              options:
                - prefer


    # Task output:
    # -------------
    #        "after": {
    #         "allow_clients": [
    #            "10.6.6.0/24"
    #        ],
    #        "listen_addresses": [
    #            "10.1.3.1"
    #        ],
    #        "servers": [
    #            {
    #                "server": "ser",
    #                "options": [
    #                    "prefer"
    #                ]
    #            },
    #            {
    #                "server": "time1.vyos.net"
    #            },
    #            {
    #                "server": "time2.vyos.net"
    #            },
    #            {
    #                "server": "time3.vyos.net"
    #            }
    #        ]
    #    },
    #    "before": {
    #    },
    #    "changed": true,
    #    "commands": [
    #        "set system ntp allow-clients address 10.6.6.0/24",
    #        "set system ntp listen-address 10.1.3.1",
    #        "set system ntp server 203.0.113.0 prefer"
    #    ]

    # After state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.6.6.0/24'
    #        set system ntp listen-address '10.1.3.1'
    #        set system ntp server 203.0.113.0 prefer,
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$


    # # -------------------
    # # 2. Using replaced
    # # -------------------

    # # Before state:
    # # -------------
    #    vyos@vyos:~$ show configuration commands | grep ntp
    #    set system ntp allow-clients address '10.4.9.0/24'
    #    set system ntp allow-clients address '10.4.7.0/24'
    #    set system ntp allow-clients address '10.1.2.0/24'
    #    set system ntp allow-clients address '10.2.3.0/24'
    #    set system ntp listen-address '10.1.9.16'
    #    set system ntp listen-address '10.5.3.2'
    #    set system ntp listen-address '10.7.9.21'
    #    set system ntp listen-address '10.8.9.4'
    #    set system ntp listen-address '10.4.5.1'
    #    set system ntp server 10.3.6.5 noselect
    #    set system ntp server 10.3.6.5 dynamic
    #    set system ntp server 10.3.6.5 preempt
    #    set system ntp server 10.3.6.5 prefer
    #    set system ntp server server4 noselect
    #    set system ntp server server4 dynamic
    #    set system ntp server server5
    #    set system ntp server time1.vyos.net
    #    set system ntp server time2.vyos.net
    #    set system ntp server time3.vyos.net
    #    vyos@vyos:~$

    # # Task
    # # -------------
    - name: Replace the existing ntp config with the new config
      vyos.vyos.vyos_ntp_global:
        config:
          allow_clients:
            - 10.6.6.0/24
          listen_addresses:
            - 10.1.3.1
          servers:
            - server: 203.0.113.0
              options:
                - prefer
        state: replaced


    # # Task output:
    # # -------------
    #        "after": {
    #         "allow_clients": [
    #            "10.6.6.0/24"
    #        ],
    #        "listen_addresses": [
    #            "10.1.3.1"
    #        ],
    #        "servers": [
    #            {
    #                "server": "ser",
    #                "options": [
    #                    "prefer"
    #                ]
    #            },
    #            {
    #                "server": "time1.vyos.net"
    #            },
    #            {
    #                "server": "time2.vyos.net"
    #            },
    #            {
    #                "server": "time3.vyos.net"
    #            }
    #        ]
    #    },
    #    "before": {
    #        "allow_clients": [
    #            "10.4.7.0/24",
    #            "10.2.3.0/24",
    #            "10.1.2.0/24",
    #            "10.4.9.0/24"
    #        ],
    #        "listen_addresses": [
    #            "10.7.9.21",
    #            "10.4.5.1",
    #            "10.5.3.2",
    #            "10.8.9.4",
    #            "10.1.9.16"
    #        ],
    #        "servers": [
    #            {
    #                "server": "10.3.6.5",
    #                "options": [
    #                    "noselect",
    #                    "dynamic",
    #                    "preempt",
    #                    "prefer"
    #                ]
    #            },
    #            {
    #                "server": "server4",
    #                "options": [
    #                    "noselect",
    #                    "dynamic"
    #                ]
    #            },
    #            {
    #                "server": "server5"
    #            },
    #            {
    #                "server": "time1.vyos.net"
    #            },
    #            {
    #                "server": "time2.vyos.net"
    #            },
    #            {
    #                "server": "time3.vyos.net"
    #            }
    #        ]
    #    },
    #    "changed": true,
    #    "commands": [
    #        "delete system ntp allow-clients address 10.4.7.0/24",
    #        "delete system ntp allow-clients address 10.2.3.0/24",
    #        "delete system ntp allow-clients address 10.1.2.0/24",
    #        "delete system ntp allow-clients address 10.4.9.0/24",
    #        "delete system ntp listen-address 10.7.9.21",
    #        "delete system ntp listen-address 10.4.5.1",
    #        "delete system ntp listen-address 10.5.3.2",
    #        "delete system ntp listen-address 10.8.9.4",
    #        "delete system ntp listen-address 10.1.9.16",
    #        "delete system ntp server 10.3.6.5",
    #        "delete system ntp server server4",
    #        "delete system ntp server server5",
    #        "set system ntp allow-clients address 10.6.6.0/24",
    #        "set system ntp listen-address 10.1.3.1",
    #        "set system ntp server 203.0.113.0 prefer"
    #    ]

    # After state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.6.6.0/24'
    #        set system ntp listen-address '10.1.3.1'
    #        set system ntp server 203.0.113.0 prefer,
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$

    # # -------------------
    # # 3. Using overridden
    # # -------------------

    # # Before state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.6.6.0/24'
    #        set system ntp listen-address '10.1.3.1'
    #        set system ntp server 203.0.113.0 prefer,
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$

    # Task
    # -------------
    - name: Override ntp config
      vyos.vyos.vyos_ntp_global:
        config:
          allow_clients:
            - 10.3.3.0/24
          listen_addresses:
            - 10.7.8.1
          servers:
            - server: server1
              options:
                - dynamic
                - prefer

            - server: server2
              options:
                - noselect
                - preempt

            - server: serv
        state: overridden

    # # Task output:
    # # -------------
    #            "after": {
    #                "allow_clients": [
    #                    "10.3.3.0/24"
    #                ],
    #                "listen_addresses": [
    #                    "10.7.8.1"
    #                ],
    #                "servers": [
    #                    {
    #                "server": "serv"
    #            },
    #            {
    #                "server": "server1",
    #                "options": [
    #                    "dynamic",
    #                    "prefer"
    #                ]
    #            },
    #            {
    #                "server": "server2",
    #                "options": [
    #                    "noselect",
    #                    "preempt"
    #                ]
    #            },
    #            {
    #                "server": "time1.vyos.net"
    #            },
    #            {
    #                "server": "time2.vyos.net"
    #            },
    #            {
    #                "server": "time3.vyos.net"
    #            }
    #                ]
    #            },
    #            "before": {
    #                "allow_clients": [
    #                    "10.6.6.0/24"
    #                ],
    #                "listen_addresses": [
    #                    "10.1.3.1"
    #                ],
    #                "servers": [
    #                    {
    #                        "server": "ser",
    #                        "options": [
    #                            "prefer"
    #                        ]
    #                    },
    #                    {
    #                        "server": "time1.vyos.net"
    #                    },
    #                    {
    #                        "server": "time2.vyos.net"
    #                    },
    #                    {
    #                        "server": "time3.vyos.net"
    #                    }
    #                ]
    #            },
    #            "changed": true,
    #            "commands": [
    #                "delete system ntp allow-clients address 10.6.6.0/24",
    #                "delete system ntp listen-address 10.1.3.1",
    #                "delete system ntp server ser",
    #                "set system ntp allow-clients address 10.3.3.0/24",
    #                "set system ntp listen-address 10.7.8.1",
    #                "set system ntp server server1 dynamic",
    #                "set system ntp server server1 prefer",
    #                "set system ntp server server2 noselect",
    #                "set system ntp server server2 preempt",
    #                "set system ntp server serv"
    #            ]

    # After state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.3.3.0/24'
    #        set system ntp listen-address '10.7.8.1'
    #        set system ntp server serv
    #        set system ntp server server1 dynamic
    #        set system ntp server server1 prefer
    #        set system ntp server server2 noselect
    #        set system ntp server server2 preempt
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$

    # 4. Using gathered
    # -------------------

    # # Before state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.3.3.0/24'
    #        set system ntp listen-address '10.7.8.1'
    #        set system ntp server serv
    #        set system ntp server server1 dynamic
    #        set system ntp server server1 prefer
    #        set system ntp server server2 noselect
    #        set system ntp server server2 preempt
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$

    # Task
    # -------------
    - name: Gather ntp config
      vyos.vyos.vyos_ntp_global:
        state: gathered

    # # Task output:
    # # -------------
    #        "gathered": {
    #                "allow_clients": [
    #                    "10.3.3.0/24"
    #                ],
    #                "listen_addresses": [
    #                    "10.7.8.1"
    #                ],
    #                "servers": [
    #                    {
    #                        "server": "serv"
    #                    },
    #                    {
    #                        "server": "server1",
    #                        "options": [
    #                            "dynamic",
    #                            "prefer"
    #                        ]
    #                    },
    #                    {
    #                         "server": "server2",
    #                         "options": [
    #                             "noselect",
    #                             "preempt"
    #                         ]
    #                     },
    #                     {
    #                          "server": "time1.vyos.net"
    #                     },
    #                     {
    #                         "server": "time2.vyos.net"
    #                     },
    #                     {
    #                         "server": "time3.vyos.net"
    #                     }
    #                ]
    #            }

    # After state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.3.3.0/24'
    #        set system ntp listen-address '10.7.8.1'
    #        set system ntp server serv
    #        set system ntp server server1 dynamic
    #        set system ntp server server1 prefer
    #        set system ntp server server2 noselect
    #        set system ntp server server2 preempt
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$


    # # -------------------
    # # 5. Using deleted
    # # -------------------

    # # Before state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp allow-clients address '10.3.3.0/24'
    #        set system ntp listen-address '10.7.8.1'
    #        set system ntp server serv
    #        set system ntp server server1 dynamic
    #        set system ntp server server1 prefer
    #        set system ntp server server2 noselect
    #        set system ntp server server2 preempt
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$

    # # Task
    # # -------------
    - name: Delete ntp config
      vyos.vyos.vyos_ntp_global:
        state: deleted


    # # Task output:
    # # -------------
    #            "after": {
    #                "servers": [
    #                    {
    #                        "server": "time1.vyos.net"
    #                    },
    #                    {
    #                       "server": "time2.vyos.net"
    #                    },
    #                    {
    #                        "server": "time3.vyos.net"
    #                    }
    #                ]
    #            },
    #            "before": {
    #                "allow_clients": [
    #                    "10.3.3.0/24"
    #                ],
    #                "listen_addresses": [
    #                    "10.7.8.1"
    #                ],
    #                "servers": [
    #                    {
    #                        "server": "serv"
    #                    },
    #                    {
    #                        "server": "server1",
    #                        "options": [
    #                            "dynamic",
    #                            "prefer"
    #                        ]
    #                    },
    #                    {
    #                          "server": "server2",
    #                          "options": [
    #                              "noselect",
    #                              "preempt"
    #                          ]
    #                      },
    #                      {
    #                          "server": "time1.vyos.net"
    #                      },
    #                      {
    #                          "server": "time2.vyos.net"
    #                      },
    #                      {
    #                          "server": "time3.vyos.net"
    #                      }
    #                ]
    #            },
    #            "changed": true,
    #            "commands": [
    #                "delete system ntp allow-clients",
    #                "delete system ntp listen-address",
    #                "delete system ntp server serv",
    #                "delete system ntp server server1",
    #                "delete system ntp server server2"
    #
    #            ]

    # After state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$


    # # -------------------
    # # 6. Using rendered
    # # -------------------

    # # Before state:
    # # -------------
    #        vyos@vyos:~$ show configuration commands | grep ntp
    #        set system ntp server time1.vyos.net
    #        set system ntp server time2.vyos.net
    #        set system ntp server time3.vyos.net
    #        vyos@vyos:~$

    # Task
    # -------------
    - name: Render ntp config
      vyos.vyos.vyos_ntp_global:
        config:
          allow_clients:
            - 10.7.7.0/24
            - 10.8.8.0/24
          listen_addresses:
            - 10.7.9.1
          servers:
            - server: server7
            - server: server45
              options:
                - noselect
                - prefer
                - pool
            - server: time1.vyos.net
            - server: time2.vyos.net
            - server: time3.vyos.net
          state: rendered

    # # Task output:
    # # -------------
    #           "rendered": [
    #                "set system ntp allow-clients address 10.7.7.0/24",
    #                "set system ntp allow-clients address 10.8.8.0/24",
    #                "set system ntp listen-address 10.7.9.1",
    #                "set system ntp server server7",
    #                "set system ntp server server45 noselect",
    #                "set system ntp server server45 prefer",
    #                "set system ntp server server45 pool",
    #                "set system ntp server time1.vyos.net",
    #                "set system ntp server time2.vyos.net",
    #                "set system ntp server time3.vyos.net"
    #            ]


    # # -------------------
    # # 7. Using parsed
    # # -------------------

    # # sample_config.cfg:
    # # -------------
    #           "set system ntp allow-clients address 10.7.7.0/24",
    #           "set system ntp listen-address 10.7.9.1",
    #           "set system ntp server server45 noselect",
    #           "set system ntp allow-clients addres 10.8.6.0/24",
    #           "set system ntp listen-address 10.5.4.1",
    #           "set system ntp server server45 dynamic",
    #           "set system ntp server time1.vyos.net",
    #           "set system ntp server time2.vyos.net",
    #           "set system ntp server time3.vyos.net"

    # Task:
    # -------------
    - name: Parse externally provided ntp configuration
      vyos.vyos.vyos_ntp_global:
        running_config: "{{ lookup('file', './sample_config.cfg') }}"
        state: parsed

    # # Task output:
    # # -------------
    #           parsed = {
    #                "allow_clients": [
    #                    "10.7.7.0/24",
    #                    "10.8.6.0/24
    #                ],
    #                "listen_addresses": [
    #                    "10.5.4.1",
    #                    "10.7.9.1"
    #                ],
    #                "servers": [
    #                    {
    #                        "server": "server45",
    #                        "options": [
    #                            "noselect",
    #                            "dynamic"
    #
    #                        ]
    #                    },
    #                    {
    #                        "server": "time1.vyos.net"
    #                    },
    #                    {
    #                        "server": "time2.vyos.net"
    #                    },
    #                    {
    #                        "server": "time3.vyos.net"
    #                    }
    #
    #                ]
    #            }



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

- Varshitha Yataluru (@YVarshitha)
