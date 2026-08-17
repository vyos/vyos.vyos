.. _vyos.vyos.vyos_file_module:


*******************
vyos.vyos.vyos_file
*******************

**Manage files, directories, and their ownership on VyOS devices**


Version added: 6.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Creates, updates, or removes a file or directory on a VyOS device, optionally pushing content from a local file (*src*) or inline text (*content*), and setting owner/group/mode via sudo chown/chmod.
- This module does not touch the configuration tree (config.boot). It manages arbitrary filesystem paths such as certificates or auth files under /config/auth/, which are not tracked by commit/save/rollback.
- All logic runs inside this module's main(), using the standard get_connection()/run_commands() pattern shared with vyos_command — there is no dedicated action plugin; this module uses the shared generic vyos action plugin like every other module in the collection.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>become</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Whether to prefix remote commands with sudo.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>content</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Inline text content to write to <em>dest</em>. Marked no_log, since this module is commonly used to push credential material. Mutually exclusive with <em>src</em>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dest</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Absolute path to the remote file or directory to manage.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
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
                        <div>Name of the group that should own <em>dest</em>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Permission bits for <em>dest</em>, as a string (e.g. &#x27;0600&#x27;). Compared against stat output after normalizing to 4 digits; &#x27;600&#x27; and &#x27;0600&#x27; are treated as equivalent.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>owner</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the user that should own <em>dest</em>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>src</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to a local file (on the Ansible controller) whose content should be pushed to <em>dest</em>. Read locally and pushed as base64 via a single CLI command, since network_cli has no SFTP/SCP channel available to this module. Mutually exclusive with <em>content</em>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Whether the path should exist (present) or be removed (absent).</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module works with connection ``ansible.netcommon.network_cli``.
   - Tested against VyOS 1.4.2 and 1.5.0.
   - File state managed by this module is independent of VyOS's config revision system. A rollback to a previous config revision will not revert changes made by this module.
   - Paths under */config/auth* are deliberately setgid ``vyattacfg`` by VyOS's own config-management convention (see vyos.dev T2713). If *mode* is given with a leading digit of ``0`` (e.g. ``'0750'``), this module compares only the rwx bits and will not report a diff for VyOS's own setgid bit. To manage the setgid/setuid/sticky bit explicitly, pass a non-zero leading digit (e.g. ``'2750'``).
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`



Examples
--------

.. code-block:: yaml

    - name: ensure the auth directory exists with correct ownership
      vyos.vyos.vyos_file:
        dest: /config/auth/office-vpn
        owner: openvpn
        group: openvpn
        mode: '0750'

    - name: push a client certificate with correct ownership
      vyos.vyos.vyos_file:
        dest: /config/auth/office-vpn/client.pem
        src: files/office-vpn-client.pem
        owner: openvpn
        group: openvpn
        mode: '0600'

    - name: remove a stale cert
      vyos.vyos.vyos_file:
        dest: /config/auth/old-vpn/client.pem
        state: absent



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
                    <b>diff_fields</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>Fields that differed between requested and actual state and were converged.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;owner&#x27;, &#x27;mode&#x27;, &#x27;content&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- VyOS maintainers and contributors (@vyos)
