.. _vyos.vyos.vyos_system_module:


*********************
vyos.vyos.vyos_system
*********************

**Run `set system` commands on VyOS devices**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Runs one or more commands on remote devices running VyOS. This module can also be introspected to validate key parameters before returning successfully.




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
                    <b>domain_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The new domain name to apply to the device.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain_search</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of domain names to search. Mutually exclusive with <em>name_server</em></div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the device hostname parameter. This option takes an ASCII string value.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of name servers to use with the device. Mutually exclusive with <em>domain_search</em></div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: name_servers</div>
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
                        <div>Whether to apply (<code>present</code>) or remove (<code>absent</code>) the settings.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against VyOS 1.1.8 (helium).
   - This module works with connection ``ansible.netcommon.network_cli``. See `the VyOS OS Platform Options <../network/user_guide/platform_vyos.html>`_.
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`



Examples
--------

.. code-block:: yaml

    - name: configure hostname and domain-name
      vyos.vyos.vyos_system:
        host_name: vyos01
        domain_name: test.example.com

    - name: remove all configuration
      vyos.vyos.vyos_system:
        state: absent

    - name: configure name servers
      vyos.vyos.vyos_system: name_servers - 8.8.8.8 - 8.8.4.4
    - name: configure domain search suffixes
      vyos.vyos.vyos_system:
        domain_search:
          - sub1.example.com
          - sub2.example.com



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
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The list of configuration mode commands to send to the device</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set system hostname vyos01&#x27;, &#x27;set system domain-name foo.example.com&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nathaniel Case (@Qalthos)
