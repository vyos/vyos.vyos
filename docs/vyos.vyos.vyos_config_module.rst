.. _vyos.vyos.vyos_config_module:


*********************
vyos.vyos.vyos_config
*********************

**Manage VyOS configuration on remote device**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides configuration file management of VyOS devices. It provides arguments for managing both the configuration file and state of the active configuration. All configuration statements are based on `set` and `delete` commands in the device configuration.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_password_change</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li><div style="color: blue"><b>plaintext</b>&nbsp;&larr;</div></li>
                                    <li>encrypted</li>
                                    <li>none</li>
                        </ul>
                </td>
                <td>
                        <div>The <code>allow_password_change</code> argument specifies whether any configuration lines which would change a user&#x27;s password should be filtered out.  By default only plaintext password changes are allowed and any encrypted-password keys are filtered out. In order to allow all password updates, both plaintext and encrypted, set this argument to <code>all</code>.</div>
                        <div>Not applied when <code>replace</code> is set to <code>config</code>; the candidate is loaded as-is via VyOS&#x27;s native <code>load</code>, which has no equivalent filtering mechanism.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup</b>
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
                        <div>The <code>backup</code> argument will backup the current devices active configuration to the Ansible control host prior to making any changes. If the <code>backup_options</code> value is not given, the backup file will be located in the backup folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>backup_options</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This is a dict object containing configurable options related to backup file path. The value of this option is read only when <code>backup</code> is set to <em>yes</em>, if <code>backup</code> is set to <em>no</em> this option will be silently ignored.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dir_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of <code>filename</code> or default filename as described in <code>filename</code> options description. If the path value is not given in that case a <em>backup</em> directory will be created in the current working directory and backup configuration will be copied in <code>filename</code> within <em>backup</em> directory.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filename</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by &lt;hostname&gt;_config.&lt;current-date&gt;@&lt;current-time&gt;</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>comment</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"configured by vyos_config"</div>
                </td>
                <td>
                        <div>Allows a commit description to be specified to be included when the configuration is committed.  If the configuration is not changed or committed, this argument is ignored.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The <code>config</code> argument specifies the base configuration to use to compare against the desired configuration.  If this value is not specified, the module will automatically retrieve the current active configuration from the remote device. The configuration lines in the option value should be similar to how it will appear if present in the running-configuration of the device including indentation to ensure idempotency and correct diff.</div>
                        <div>Ignored when <code>replace</code> is set to <code>config</code>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>confirm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>automatic</li>
                                    <li>manual</li>
                                    <li><div style="color: blue"><b>none</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>The <code>confirm</code> argument will tell vyos to revert to the previous configuration if not explicitly confirmed after applying the new config. When set to <code>automatic</code> this module will automatically confirm the configuration, if the current session remains working with the new config. When set to <code>manual</code>, this module does not issue the confirmation itself.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>confirm_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">10</div>
                </td>
                <td>
                        <div>Minutes to wait for confirmation before reverting the configuration. Does not apply when <code>confirm</code> is set to <code>none</code> .</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>lines</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config as found in the device running-config to ensure idempotency and correct diff. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser.</div>
                        <div>Not supported when <code>replace</code> is set to <code>config</code> -- see <code>replace</code> below.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>line</b>&nbsp;&larr;</div></li>
                                    <li>none</li>
                        </ul>
                </td>
                <td>
                        <div>The <code>match</code> argument controls the method used to match against the current active configuration.  By default, the desired config is matched against the active config and the deltas are loaded.  If the <code>match</code> argument is set to <code>none</code> the active configuration is ignored and the configuration is always loaded.</div>
                        <div>Ignored when <code>replace</code> is set to <code>config</code>, since no line-level diff is computed in that mode.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>replace</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>line</b>&nbsp;&larr;</div></li>
                                    <li>config</li>
                        </ul>
                </td>
                <td>
                        <div>Controls how the module applies configuration to the device.</div>
                        <div>When set to <code>line</code> (default), the module computes a set/delete command diff and pushes only the changed lines -- this is the existing behavior, unchanged.</div>
                        <div>When set to <code>config</code>, the module uploads the full candidate configuration (<code>src</code>) to the device and issues VyOS&#x27;s native <code>load</code> command in configuration mode, which replaces the running configuration wholesale with the candidate&#x27;s exact contents. VyOS&#x27;s own configuration engine performs the reconciliation, rather than the module computing per-line deltas. This mirrors the mechanism offered by <code>cisco.iosxr.iosxr_config</code>&#x27;s <code>replace=config</code>.</div>
                        <div><code>replace=config</code> requires <code>src</code> and does not accept <code>lines</code> -- there is no way to convert flat set/delete commands into the hierarchical form <code>load</code> requires without re-implementing VyOS&#x27;s own config-tree builder.</div>
                        <div>As with <code>src</code> in the default <code>line</code> mode, the module does not validate the candidate&#x27;s contents or format under <code>replace=config</code> -- supplying a well-formed, complete configuration is the caller&#x27;s responsibility.</div>
                        <div><code>replace=config</code> requires the device to accept file transfer (SCP) over the same <code>network_cli</code> SSH session used for configuration commands.</div>
                        <div><code>replace=config</code> writes the candidate to a fixed path on the device (overwritten on each run, matching <code>cisco.iosxr.iosxr_config</code>&#x27;s own <code>replace=config</code> precedent). Running <code>replace=config</code> concurrently against the same host is not supported.</div>
                        <div>Any configuration present on the device but omitted from the candidate will be removed, including management interfaces, SSH access, and login users if they are omitted. Always supply a complete configuration, never a partial one.</div>
                        <div>When capturing a candidate from the device&#x27;s own output (for example via <code>show configuration</code>) rather than from a trusted, separately maintained source, be aware that VyOS may return masked placeholder values (for example a run of literal asterisks) in place of local users&#x27; <code>encrypted-password</code>/<code>plaintext-password</code> values when queried through automation, even though the identical command returns the real value when typed interactively at a terminal. Pushing a masked capture back through <code>replace=config</code> sends the literal placeholder as the new password value; VyOS&#x27;s own commit-time validation is expected to reject an obviously malformed hash, but a masked value that happens to pass basic format validation could apply silently. Prefer sourcing <code>replace=config</code> candidates from a trusted, version-controlled artifact rather than a live automated capture whenever the configuration contains local password-based users.</div>
                        <div>Even under <code>check_mode</code>, the candidate is written to a temporary file on the device so that VyOS&#x27;s own <code>compare</code> can produce an accurate preview diff. No <code>commit</code> occurs in check mode.</div>
                        <div>When combined with <code>backup=yes</code>, the value of <code>changed</code> reflects whether the backup file&#x27;s content changed on the Ansible control node, not whether the device configuration changed -- this is existing behavior in the shared netcommon action plugin backing config-family modules across collections, not specific to <code>replace=config</code>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>save</b>
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
                        <div>The <code>save</code> argument controls whether or not changes made to the active configuration are saved to disk.  This is independent of committing the config.  When set to True, the active configuration is saved.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                        <div>The <code>src</code> argument specifies the path to the source config file to load.  The source config file can either be in bracket format or set format.  The source file can include Jinja2 template variables. The configuration lines in the source file should be similar to how it will appear if present in the running-configuration of the device including indentation to ensure idempotency and correct diff.</div>
                        <div>When <code>replace</code> is set to <code>config</code>, <code>src</code> is required and must contain a complete configuration in hierarchical/bracket format -- the same format produced by <code>show configuration</code> or found in <code>/config/config.boot</code>. Flat <code>set</code>/<code>delete</code> command format (as produced by <code>show configuration commands</code>) is not accepted in that mode; VyOS&#x27;s native <code>load</code> command rejects it with a parse error.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against VyOS 1.3.8, 1.4.2, the upcoming 1.5, and the rolling release of spring 2025.
   - This module works with connection ``ansible.netcommon.network_cli``. See `the VyOS OS Platform Options <../network/user_guide/platform_vyos.html>`_.
   - To ensure idempotency and correct diff the configuration lines in the relevant module options should be similar to how they appear if present in the running configuration on device including the indentation.
   - ``replace=config`` currently has no way to scope its effect to part of the configuration; it always operates against the entire device configuration. There is no ``path`` parameter to constrain it to a subtree.
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`



Examples
--------

.. code-block:: yaml

    - name: configure the remote device
      vyos.vyos.vyos_config:
        lines:
          - set system host-name {{ inventory_hostname }}
          - set service lldp
          - delete service dhcp-server

    - name: backup and load from file
      vyos.vyos.vyos_config:
        src: vyos.cfg
        backup: true

    - name: render a Jinja2 template onto the VyOS router
      vyos.vyos.vyos_config:
        src: vyos_template.j2

    - name: revert after ten minutes, if connection is lost
      vyos.vyos.vyos_config:
        src: vyos_template.j2
        confirm: automatic

    - name: for idempotency, use full-form commands
      vyos.vyos.vyos_config:
        lines:
          # - set int eth eth2 description 'OUTSIDE'
          - set interface ethernet eth2 description 'OUTSIDE'

    - name: configurable backup path
      vyos.vyos.vyos_config:
        backup: true
        backup_options:
          filename: backup.cfg
          dir_path: /home/user

    - name: replace the entire running config with a full candidate (native load)
      # replace=config requires the complete desired configuration in
      # hierarchical/bracket format -- never a partial one, and never flat
      # set-command format. A safe pattern is to back up the current config,
      # edit it, then replace with the edited whole, as shown here.
      vyos.vyos.vyos_config:
        backup: true
        backup_options:
          filename: pre_replace_backup.cfg
      register: backup_result

    - name: (edit backup_result's backup file as needed, then)
      vyos.vyos.vyos_config:
        src: /home/user/pre_replace_backup_edited.cfg
        replace: config



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
                    <b>backup_path</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when backup is yes</td>
                <td>
                            <div>The full path to the backup file</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">/playbooks/ansible/backup/vyos_config.2016-07-16@22:28:34</div>
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
                            <div>In <code>replace=line</code> mode (default), the list of set/delete commands sent to the device.</div>
                            <div>In <code>replace=config</code> mode, contains only the single <code>load &lt;path&gt;</code> command actually issued to the device -- not an itemized diff. See <code>diff</code> for the actual change content, sourced from VyOS&#x27;s own <code>compare</code> output.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;...&#x27;, &#x27;...&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>date</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when backup is yes</td>
                <td>
                            <div>The date extracted from the backup file name</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">2016-07-16</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>filename</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when backup is yes and filename is not specified in backup options</td>
                <td>
                            <div>The name of the backup file</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">vyos_config.2016-07-16@22:28:34</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>filtered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The list of configuration commands removed to avoid a load failure. Not populated when <code>replace</code> is set to <code>config</code>.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;...&#x27;, &#x27;...&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>shortname</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when backup is yes and filename is not specified in backup options</td>
                <td>
                            <div>The full path to the backup file excluding the timestamp</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">/playbooks/ansible/backup/vyos_config</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>time</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>when backup is yes</td>
                <td>
                            <div>The time extracted from the backup file name</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">22:28:34</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nathaniel Case (@Qalthos)
