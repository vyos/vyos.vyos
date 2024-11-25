.. _vyos.vyos.vyos_firewall_interfaces_module:


**********************************
vyos.vyos.vyos_firewall_interfaces
**********************************

**Firewall interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage firewall rules of interfaces on VyOS network devices. (1.3-)




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
                        <div>A list of firewall rules options for interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_rules</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies firewall rules attached to the interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specifies the AFI for the Firewall rules to be configured on this interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specifies the firewall rules for the provided AFI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>in</li>
                                    <li>local</li>
                                    <li>out</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the direction of packets that the firewall rule will be applied on.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Specifies the name of the IPv4/IPv6 Firewall rule for the interface.</div>
                </td>
            </tr>


            <tr>
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
                        <div>Name/Identifier for the interface.</div>
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
                        <div>The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook.  The <em>running_config</em> argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command <code>show configuration commands | grep &#x27;firewall&#x27;</code>.</div>
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
                                    <li>parsed</li>
                                    <li>rendered</li>
                                    <li>gathered</li>
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
   - Deprecated in VyOS 1.4+, firewalls are no longer connected directly to interfaces. See the Firewall Configuration documentation for how to establish a connection betwen the firewall rulesets and the flow, interface, or zone.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # vyos@192# run show configuration commands | grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    #
    - name: Merge the provided configuration with the existing running configuration
      vyos.vyos.vyos_firewall_interfaces:
        config:
          - access_rules:
              - afi: ipv4
                rules:
                  - name: INBOUND
                    direction: in
                  - name: OUTBOUND
                    direction: out
                  - name: LOCAL
                    direction: local
              - afi: ipv6
                rules:
                  - name: V6-LOCAL
                    direction: local
            name: eth1
          - access_rules:
              - afi: ipv4
                rules:
                  - name: INBOUND
                    direction: in
                  - name: OUTBOUND
                    direction: out
                  - name: LOCAL
                    direction: local
              - afi: ipv6
                rules:
                  - name: V6-LOCAL
                    direction: local
            name: eth3
        state: merged
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    # before": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "name": "eth3"
    #        }
    #    ]
    #
    #    "commands": [
    #       "set interfaces ethernet eth1 firewall in name 'INBOUND'",
    #       "set interfaces ethernet eth1 firewall out name 'OUTBOUND'",
    #       "set interfaces ethernet eth1 firewall local name 'LOCAL'",
    #       "set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'",
    #       "set interfaces ethernet eth3 firewall in name 'INBOUND'",
    #       "set interfaces ethernet eth3 firewall out name 'OUTBOUND'",
    #       "set interfaces ethernet eth3 firewall local name 'LOCAL'",
    #       "set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'"
    #    ]
    #
    # "after": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall in name 'INBOUND'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall local name 'LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth3 firewall local name 'LOCAL'
    # set interfaces ethernet eth3 firewall out name 'OUTBOUND'


    # Using merged

    # Before state:
    # -------------
    # vyos@vyos:~$ show configuration commands | grep interfaces
    # set interfaces bonding 'bond0'
    # set interfaces bonding 'bond1'
    # set interfaces bonding bond2 'ip'
    # set interfaces bonding bond2 'ipv6'
    # set interfaces ethernet eth0 address 'dhcp'
    # set interfaces ethernet eth0 duplex 'auto'
    # set interfaces ethernet eth0 'ip'
    # set interfaces ethernet eth0 'ipv6'
    # set interfaces ethernet eth0 smp_affinity 'auto'
    # set interfaces ethernet eth0 speed 'auto'
    # set interfaces ethernet 'eth1'
    # set interfaces ethernet 'eth2'

    - name: Merge provided configuration with device configuration
      vyos.vyos.vyos_interfaces:
        config:
          - name: eth2
            description: Configured by Ansible
            enabled: true
            vifs:
              - vlan_id: 200
                description: VIF 200 - ETH2
          - name: eth3
            description: Configured by Ansible
            mtu: 1500
          - name: bond1
            description: Bond - 1
            mtu: 1200
          - name: vti2
            description: VTI - 2
            enabled: false
        state: merged

    # Task Output
    # -----------
    # before:
    # - enabled: true
    #   name: lo
    # - enabled: true
    #   name: eth3
    # - enabled: true
    #   name: eth2
    # - enabled: true
    #   name: eth1
    # - duplex: auto
    #   enabled: true
    #   name: eth0
    #   speed: auto
    # commands:
    # - set interfaces ethernet eth2 description 'Configured by Ansible'
    # - set interfaces ethernet eth2 vif 200
    # - set interfaces ethernet eth2 vif 200 description 'VIF 200 - ETH2'
    # - set interfaces ethernet eth3 description 'Configured by Ansible'
    # - set interfaces ethernet eth3 mtu '1500'
    # - set interfaces bonding bond1
    # - set interfaces bonding bond1 description 'Bond - 1'
    # - set interfaces bonding bond1 mtu '1200'
    # - set interfaces vti vti2
    # - set interfaces vti vti2 description 'VTI - 2'
    # - set interfaces vti vti2 disable
    # after:
    # - description: Bond - 1
    #   enabled: true
    #   mtu: 1200
    #   name: bond1
    # - enabled: true
    #   name: lo
    # - description: VTI - 2
    #   enabled: false
    #   name: vti2
    # - description: Configured by Ansible
    #   enabled: true
    #   mtu: 1500
    #   name: eth3
    # - description: Configured by Ansible
    #   enabled: true
    #   name: eth2
    #   vifs:
    #   - description: VIF 200 - ETH2
    #     enabled: true
    #     vlan_id: '200'
    # - enabled: true
    #   name: eth1
    # - duplex: auto
    #   enabled: true
    #   name: eth0
    #   speed: auto

    # After state:
    # ------------
    # vyos@vyos:~$ show configuration commands | grep interfaces
    # set interfaces bonding bond1 description 'Bond - 1'
    # set interfaces bonding bond1 mtu '1200'
    # set interfaces ethernet eth0 address 'dhcp'
    # set interfaces ethernet eth0 address 'dhcpv6'
    # set interfaces ethernet eth0 duplex 'auto'
    # set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
    # set interfaces ethernet eth0 smp-affinity 'auto'
    # set interfaces ethernet eth0 speed 'auto'
    # set interfaces ethernet eth1 hw-id '08:00:27:ea:0f:b9'
    # set interfaces ethernet eth1 smp-affinity 'auto'
    # set interfaces ethernet eth2 description 'Configured by Ansible'
    # set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
    # set interfaces ethernet eth2 smp-affinity 'auto'
    # set interfaces ethernet eth2 vif 200 description 'VIF 200 - ETH2'
    # set interfaces ethernet eth3 description 'Configured by Ansible'
    # set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
    # set interfaces ethernet eth3 mtu '1500'
    # set interfaces loopback lo
    # set interfaces vti vti2 description 'VTI - 2'
    # set interfaces vti vti2 disable


    # Using replaced
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall in name 'INBOUND'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall local name 'LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth3 firewall local name 'LOCAL'
    # set interfaces ethernet eth3 firewall out name 'OUTBOUND'
    #
    - name: >-
        Replace device configurations of listed firewall interfaces with provided
        configurations
      vyos.vyos.vyos_firewall_interfaces:
        config:
          - name: eth1
            access_rules:
              - afi: ipv4
                rules:
                  - name: OUTBOUND
                    direction: out
              - afi: ipv6
                rules:
                  - name: V6-LOCAL
                    direction: local
          - name: eth3
            access_rules:
              - afi: ipv4
                rules:
                  - name: INBOUND
                    direction: in
        state: replaced
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "before": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #
    # "commands": [
    #        "delete interfaces ethernet eth1 firewall in name",
    #        "delete interfaces ethernet eth1 firewall local name",
    #        "delete interfaces ethernet eth3 firewall local name",
    #        "delete interfaces ethernet eth3 firewall out name",
    #        "delete interfaces ethernet eth3 firewall local ipv6-name"
    #    ]
    #
    #    "after": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall 'in'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall 'local'
    # set interfaces ethernet eth3 firewall 'out'


    # Using overridden
    #
    # Before state
    # --------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall 'in'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall 'local'
    # set interfaces ethernet eth3 firewall 'out'
    #
    - name: Overrides all device configuration with provided configuration
      vyos.vyos.vyos_firewall_interfaces:
        config:
          - name: eth3
            access_rules:
              - afi: ipv4
                rules:
                  - name: INBOUND
                    direction: out
        state: overridden
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    # "before":[
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #
    #    "commands": [
    #        "delete interfaces ethernet eth1 firewall",
    #        "delete interfaces ethernet eth3 firewall in name",
    #        "set interfaces ethernet eth3 firewall out name 'INBOUND'"
    #    ]
    #
    #    "after": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "out",
    #                            "name": "INBOUND"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #
    #
    # After state
    # ------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall 'in'
    # set interfaces ethernet eth3 firewall 'local'
    # set interfaces ethernet eth3 firewall out name 'INBOUND'


    # Using deleted per interface name
    #
    # Before state
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall in name 'INBOUND'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall local name 'LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth3 firewall local name 'LOCAL'
    # set interfaces ethernet eth3 firewall out name 'OUTBOUND'
    #
    - name: Delete firewall interfaces based on interface name.
      vyos.vyos.vyos_firewall_interfaces:
        config:
          - name: eth1
          - name: eth3
        state: deleted
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    # "before": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #    "commands": [
    #        "delete interfaces ethernet eth1 firewall",
    #        "delete interfaces ethernet eth3 firewall"
    #    ]
    #
    #    "after" : []
    # After state
    # ------------
    # vyos@vyos# run show configuration commands | grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'


    # Using deleted per afi
    #
    # Before state
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall in name 'INBOUND'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall local name 'LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth3 firewall local name 'LOCAL'
    # set interfaces ethernet eth3 firewall out name 'OUTBOUND'
    #
    - name: Delete firewall interfaces config per afi.
      vyos.vyos.vyos_firewall_interfaces:
        config:
          - name: eth1
            access_rules:
              - afi: ipv4
              - afi: ipv6
        state: deleted
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #    "commands": [
    #        "delete interfaces ethernet eth1 firewall in name",
    #        "delete interfaces ethernet eth1 firewall out name",
    #        "delete interfaces ethernet eth1 firewall local name",
    #        "delete interfaces ethernet eth1 firewall local ipv6-name"
    #    ]
    #
    # After state
    # ------------
    # vyos@vyos# run show configuration commands | grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'


    # Using deleted without config
    #
    # Before state
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall in name 'INBOUND'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall local name 'LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth3 firewall local name 'LOCAL'
    # set interfaces ethernet eth3 firewall out name 'OUTBOUND'
    #
    - name: Delete firewall interfaces config when empty config provided.
      vyos.vyos.vyos_firewall_interfaces:
        state: deleted
    # After state
    # ------------
    # vyos@vyos# run show configuration commands | grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    #
    #
    # ------------------------
    # Module Execution Results
    # ------------------------
    #
    #    "commands": [
    #        "delete interfaces ethernet eth1 firewall",
    #        "delete interfaces ethernet eth1 firewall"
    #    ]
    #


    # Using parsed
    #
    #
    - name: Parse the provided  configuration
      vyos.vyos.vyos_firewall_interfaces:
        running_config:
          "set interfaces ethernet eth1 firewall in name 'INBOUND'
           set interfaces ethernet eth1 firewall out name 'OUTBOUND'
           set interfaces ethernet eth1 firewall local name 'LOCAL'
           set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
           set interfaces ethernet eth2 firewall in name 'INBOUND'
           set interfaces ethernet eth2 firewall out name 'OUTBOUND'
           set interfaces ethernet eth2 firewall local name 'LOCAL'
           set interfaces ethernet eth2 firewall local ipv6-name 'V6-LOCAL'"
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
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        },
    #                        {
    #                            "direction": "local",
    #                            "name": "LOCAL"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth2"
    #        },
    #        {
    #            "name": "eth3"
    #        }
    #    ]


    # Using gathered
    #
    # Before state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall 'in'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall 'local'
    # set interfaces ethernet eth3 firewall 'out'
    #
    - name: Gather listed firewall interfaces.
      vyos.vyos.vyos_firewall_interfaces:
        state: gathered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #    "gathered": [
    #        {
    #            "name": "eth0"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "out",
    #                            "name": "OUTBOUND"
    #                        }
    #                    ]
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "rules": [
    #                        {
    #                            "direction": "local",
    #                            "name": "V6-LOCAL"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth1"
    #        },
    #        {
    #            "name": "eth2"
    #        },
    #        {
    #            "access_rules": [
    #                {
    #                    "afi": "ipv4",
    #                    "rules": [
    #                        {
    #                            "direction": "in",
    #                            "name": "INBOUND"
    #                        }
    #                    ]
    #                }
    #            ],
    #            "name": "eth3"
    #        }
    #    ]
    #
    #
    # After state:
    # -------------
    #
    # vyos@vyos:~$ show configuration commands| grep firewall
    # set firewall ipv6-name 'V6-LOCAL'
    # set firewall name 'INBOUND'
    # set firewall name 'LOCAL'
    # set firewall name 'OUTBOUND'
    # set interfaces ethernet eth1 firewall 'in'
    # set interfaces ethernet eth1 firewall local ipv6-name 'V6-LOCAL'
    # set interfaces ethernet eth1 firewall out name 'OUTBOUND'
    # set interfaces ethernet eth3 firewall in name 'INBOUND'
    # set interfaces ethernet eth3 firewall 'local'
    # set interfaces ethernet eth3 firewall 'out'


    # Using rendered
    #
    #
    - name: Render the commands for provided  configuration
      vyos.vyos.vyos_firewall_interfaces:
        config:
          - name: eth2
            access_rules:
              - afi: ipv4
                rules:
                  - name: INGRESS
                    direction: in
                  - name: OUTGRESS
                    direction: out
                  - name: DROP
                    direction: local
        state: rendered
    #
    #
    # -------------------------
    # Module Execution Result
    # -------------------------
    #
    #
    # "rendered": [
    #        "set interfaces ethernet eth2 firewall in name 'INGRESS'",
    #        "set interfaces ethernet eth2 firewall out name 'OUTGRESS'",
    #        "set interfaces ethernet eth2 firewall local name 'DROP'",
    #        "set interfaces ethernet eth2 firewall local ipv6-name 'LOCAL'"
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set interfaces ethernet eth1 firewall local ipv6-name &#x27;V6-LOCAL&#x27;&quot;, &quot;set interfaces ethernet eth3 firewall in name &#x27;INBOUND&#x27;&quot;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&quot;set interfaces ethernet eth1 firewall local ipv6-name &#x27;V6-LOCAL&#x27;&quot;, &quot;set interfaces ethernet eth3 firewall in name &#x27;INBOUND&#x27;&quot;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Rohit Thakur (@rohitthakur2590)
