=============================
Vyos Collection Release Notes
=============================

.. contents:: Topics


v2.2.0
======

Security Fixes
--------------

- Mask values of sensitive keys in module result.

v2.1.0
======

Minor Changes
-------------

- Add regex for delete failures to terminal_stderr_re
- Add vyos BGP address_family resource module (https://github.com/ansible-collections/vyos.vyos/pull/132).
- Enabled addition and parsing of wireguard interface.

New Modules
-----------

- vyos_bgp_address_family - BGP Address Family Resource Module.

v2.0.0
======

Major Changes
-------------

- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`
- ipaddress is no longer in ansible.netcommon. For Python versions without ipaddress (< 3.0), the ipaddress package is now required.

Minor Changes
-------------

- Add support for configuration caching (single_user_mode).
- Add vyos BGP global resource module.(https://github.com/ansible-collections/vyos.vyos/pull/125).
- Re-use device_info dictionary in cliconf.

Bugfixes
--------

- Update docs to clarify the idemptonecy releated caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)
- cliconf plugin - Prevent `get_capabilities()` from getting larger every time it is called

New Modules
-----------

ansible.collections.ansible_collections.vyos.vyos.plugins.modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- vyos_bgp_global - BGP Global Resource Module.

v1.1.1
======

Bugfixes
--------

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Enable configuring an interface which is not present in the running config.
- vyos_config - Only process src files as commands when they actually contain commands. This fixes an issue were the whitespace preceding a configuration key named 'set' was stripped, tripping up the parser.

v1.1.0
======

Minor Changes
-------------

- Added ospf_interfaces resource module.

New Modules
-----------

- vyos_ospf_interfaces - OSPF Interfaces resource module

v1.0.5
======

Bugfixes
--------

- Added openvpn vtu interface support.
- Update network integration auth timeout for connection local.
- terminal plugin - Overhaul ansi_re to remove more escape sequences

v1.0.4
======

Minor Changes
-------------

- Moved intent testcases from integration suite to unit tests.
- Reformatted files with latest version of Black (20.8b1).

v1.0.3
======

v1.0.2
======

Minor Changes
-------------

- Fixed the typo in the modulename of ospfv2 and ospfv3 unit tests.
- Updated docs.
- terminal plugin - Added additional escape sequence to be removed from terminal output.

Bugfixes
--------

- Added workaround to avoid set_fact dynamically assigning value. This behavior seems to have been broken after ansible2.9.
- Make `src`, `backup` and `backup_options` in vyos_config work when module alias is used (https://github.com/ansible-collections/vyos.vyos/pull/67).
- vyos_config - fixed issue where config could be saved while in check mode (https://github.com/ansible-collections/vyos.vyos/pull/53)

v1.0.1
======

Minor Changes
-------------

- Add doc plugin fixes (https://github.com/ansible-collections/vyos.vyos/pull/51)

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- vyos - Use vyos cliconf to run command on VyOS platform

New Modules
-----------

- vyos_banner - Manage multiline banners on VyOS devices
- vyos_command - Run one or more commands on VyOS devices
- vyos_config - Manage VyOS configuration on remote device
- vyos_facts - Get facts about vyos devices.
- vyos_firewall_global - FIREWALL global resource module
- vyos_firewall_interfaces - FIREWALL interfaces resource module
- vyos_firewall_rules - FIREWALL rules resource module
- vyos_interface - (deprecated, removed after 2022-06-01) Manage Interface on VyOS network devices
- vyos_interfaces - Interfaces resource module
- vyos_l3_interface - (deprecated, removed after 2022-06-01) Manage L3 interfaces on VyOS network devices
- vyos_l3_interfaces - L3 interfaces resource module
- vyos_lag_interfaces - LAG interfaces resource module
- vyos_linkagg - (deprecated, removed after 2022-06-01) Manage link aggregation groups on VyOS network devices
- vyos_lldp - (deprecated, removed after 2022-06-01) Manage LLDP configuration on VyOS network devices
- vyos_lldp_global - LLDP global resource module
- vyos_lldp_interface - (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on VyOS network devices
- vyos_lldp_interfaces - LLDP interfaces resource module
- vyos_logging - Manage logging on network devices
- vyos_ospfv2 - OSPFv2 resource module
- vyos_ospfv3 - OSPFV3 resource module
- vyos_ping - Tests reachability using ping from VyOS network devices
- vyos_static_route - (deprecated, removed after 2022-06-01) Manage static IP routes on Vyatta VyOS network devices
- vyos_static_routes - Static routes resource module
- vyos_system - Run `set system` commands on VyOS devices
- vyos_user - Manage the collection of local users on VyOS device
- vyos_vlan - Manage VLANs on VyOS network devices
