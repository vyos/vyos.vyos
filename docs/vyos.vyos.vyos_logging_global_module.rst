.. _vyos.vyos.vyos_logging_global_module:


*****************************
vyos.vyos.vyos_logging_global
*****************************

**Logging resource module**


Version added: 2.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the logging attributes of Vyos network devices




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list containing dictionary of logging options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>console</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>logging to serial console</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facilities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>facility configurations for console</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>auth</li>
                                    <li>authpriv</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>mark</li>
                                    <li>news</li>
                                    <li>protocols</li>
                                    <li>security</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                        </ul>
                </td>
                <td>
                        <div>Facility for logging</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emerg</li>
                                    <li>alert</li>
                                    <li>crit</li>
                                    <li>err</li>
                                    <li>warning</li>
                                    <li>notice</li>
                                    <li>info</li>
                                    <li>debug</li>
                                    <li>all</li>
                        </ul>
                </td>
                <td>
                        <div>logging level</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>enable or disable the command</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>files</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>logging to file</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Log file size and rotation characteristics</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file_num</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of saved files (default is 5)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Size of log files (in kilobytes, default is 256)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>enable or disable the command</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facilities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>facility configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>auth</li>
                                    <li>authpriv</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>mark</li>
                                    <li>news</li>
                                    <li>protocols</li>
                                    <li>security</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                        </ul>
                </td>
                <td>
                        <div>Facility for logging</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emerg</li>
                                    <li>alert</li>
                                    <li>crit</li>
                                    <li>err</li>
                                    <li>warning</li>
                                    <li>notice</li>
                                    <li>info</li>
                                    <li>debug</li>
                                    <li>all</li>
                        </ul>
                </td>
                <td>
                        <div>logging level</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>file name or path</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>global_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>logging to serial console</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Log file size and rotation characteristics</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file_num</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of saved files (default is 5)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Size of log files (in kilobytes, default is 256)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>enable or disable the command</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facilities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>facility configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>auth</li>
                                    <li>authpriv</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>mark</li>
                                    <li>news</li>
                                    <li>protocols</li>
                                    <li>security</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                        </ul>
                </td>
                <td>
                        <div>Facility for logging</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emerg</li>
                                    <li>alert</li>
                                    <li>crit</li>
                                    <li>err</li>
                                    <li>warning</li>
                                    <li>notice</li>
                                    <li>info</li>
                                    <li>debug</li>
                                    <li>all</li>
                        </ul>
                </td>
                <td>
                        <div>logging level</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>marker_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>time interval how often a mark message is being sent in seconds (default is 1200)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>preserve_fqdn</b>
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
                        <div>uses FQDN for logging</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>enable or disable the command</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>logging to serial console</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facilities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>facility configurations for host</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>auth</li>
                                    <li>authpriv</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>mark</li>
                                    <li>news</li>
                                    <li>protocols</li>
                                    <li>security</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                        </ul>
                </td>
                <td>
                        <div>Facility for logging</div>
                </td>
            </tr>
            <tr>
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
                                    <li>udp</li>
                                    <li>tcp</li>
                        </ul>
                </td>
                <td>
                        <div>syslog communication protocol</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emerg</li>
                                    <li>alert</li>
                                    <li>crit</li>
                                    <li>err</li>
                                    <li>warning</li>
                                    <li>notice</li>
                                    <li>info</li>
                                    <li>debug</li>
                                    <li>all</li>
                        </ul>
                </td>
                <td>
                        <div>logging level</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Remote host name or IP address</div>
                </td>
            </tr>
            <tr>
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
                        <div>Destination port (1-65535)</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>syslog</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>logging syslog</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>enable or disable the command</div>
                </td>
            </tr>

            <tr>
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
                        <div>logging to file</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facilities</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>facility configurations</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>all</li>
                                    <li>auth</li>
                                    <li>authpriv</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>mark</li>
                                    <li>news</li>
                                    <li>protocols</li>
                                    <li>security</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                        </ul>
                </td>
                <td>
                        <div>Facility for logging</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emerg</li>
                                    <li>alert</li>
                                    <li>crit</li>
                                    <li>err</li>
                                    <li>warning</li>
                                    <li>notice</li>
                                    <li>info</li>
                                    <li>debug</li>
                                    <li>all</li>
                        </ul>
                </td>
                <td>
                        <div>logging level</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>user login name</div>
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
                        <div>The value of this option should be the output received from the VYOS device by executing the command <b>show configuration commands | grep syslog</b>.</div>
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
                                    <li>parsed</li>
                                    <li>rendered</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>Refer to examples for more details.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against vyos 1.2
   - This module works with connection ``network_cli``.
   - The Configuration defaults of the Vyos network devices are supposed to hinder idempotent behavior of plays



Examples
--------

.. code-block:: yaml

    # Using state: merged

    # Before state:
    # -------------

    # vyos:~$show configuration commands | grep syslog

    - name: Apply the provided configuration
      vyos.vyos.vyos_logging_global:
        config:
          console:
            facilities:
              - facility: local7
                severity: err
          files:
            - path: logFile
              archive:
                file_num: 2
              facilities:
                - facility: local6
                  severity: emerg
          hosts:
            - hostname: 172.16.0.1
              facilities:
                - facility: local7
                  severity: all
                - facility: all
                  protocol: udp
              port: 223
          users:
            - username: vyos
              facilities:
              - facility: local7
                severity: debug
          global_params:
            archive:
              file_num: 2
              size: 111
            facilities:
            - facility: cron
              severity: debug
            marker_interval: 111
            preserve_fqdn: true
        state: merged

    # Commands Fired:
    # ---------------

    # "commands": [
    #     "set system syslog console facility local7 level err",
    #     "set system syslog file logFile archive file 2",
    #     "set system syslog host 172.16.0.1 facility local7 level all",
    #     "set system syslog file logFile facility local6 level emerg",
    #     "set system syslog host 172.16.0.1 facility all protocol udp",
    #     "set system syslog user vyos facility local7 level debug",
    #     "set system syslog host 172.16.0.1 port 223",
    #     "set system syslog global facility cron level debug",
    #     "set system syslog global archive file 2",
    #     "set system syslog global archive size 111",
    #     "set system syslog global marker interval 111",
    #     "set system syslog global preserve-fqdn"
    # ],

    # After state:
    # ------------

    # vyos:~$ show configuration commands | grep syslog
    # set system syslog console facility local7 level 'err'
    # set system syslog file logFile archive file '2'
    # set system syslog file logFile facility local6 level 'emerg'
    # set system syslog global archive file '2'
    # set system syslog global archive size '111'
    # set system syslog global facility cron level 'debug'
    # set system syslog global marker interval '111'
    # set system syslog global preserve-fqdn
    # set system syslog host 172.16.0.1 facility all protocol 'udp'
    # set system syslog host 172.16.0.1 facility local7 level 'all'
    # set system syslog host 172.16.0.1 port '223'
    # set system syslog user vyos facility local7 level 'debug'

    # Using state: deleted

    # Before state:
    # -------------

    # vyos:~$show configuration commands | grep syslog
    # set system syslog console facility local7 level 'err'
    # set system syslog file logFile archive file '2'
    # set system syslog file logFile facility local6 level 'emerg'
    # set system syslog global archive file '2'
    # set system syslog global archive size '111'
    # set system syslog global facility cron level 'debug'
    # set system syslog global marker interval '111'
    # set system syslog global preserve-fqdn
    # set system syslog host 172.16.0.1 facility all protocol 'udp'
    # set system syslog host 172.16.0.1 facility local7 level 'all'
    # set system syslog host 172.16.0.1 port '223'
    # set system syslog user vyos facility local7 level 'debug'

    - name: delete the existing configuration
      vyos.vyos.vyos_logging_global:
        state: deleted

    # Commands Fired:
    # ---------------

    # "commands": [
    #     "delete system syslog"
    # ],

    # After state:
    # ------------

    # vyos:~$show configuration commands | grep syslog

    # Using state: overridden

    # Before state:
    # -------------

    # vyos:~$show configuration commands | grep syslog
    # set system syslog console facility local7 level 'err'
    # set system syslog file logFile archive file '2'
    # set system syslog file logFile facility local6 level 'emerg'
    # set system syslog global archive file '2'
    # set system syslog global archive size '111'
    # set system syslog global facility cron level 'debug'
    # set system syslog global marker interval '111'
    # set system syslog global preserve-fqdn
    # set system syslog host 172.16.0.1 facility all protocol 'udp'
    # set system syslog host 172.16.0.1 facility local7 level 'all'
    # set system syslog host 172.16.0.1 port '223'
    # set system syslog user vyos facility local7 level 'debug'

    - name: Override the current configuration
      vyos.vyos.vyos_logging_global:
        config:
          console:
            facilities:
              - facility: all
              - facility: local7
                severity: err
              - facility: news
                severity: debug
          files:
            - path: logFileNew
          hosts:
            - hostname: 172.16.0.2
              facilities:
                - facility: local5
                  severity: all
          global_params:
            archive:
              file_num: 10
        state: overridden

    # Commands Fired:
    # ---------------

    # "commands": [
    #     "delete system syslog file logFile",
    #     "delete system syslog global facility cron",
    #     "delete system syslog host 172.16.0.1",
    #     "delete system syslog user vyos",
    #     "set system syslog console facility all",
    #     "set system syslog console facility news level debug",
    #     "set system syslog file logFileNew",
    #     "set system syslog host 172.16.0.2 facility local5 level all",
    #     "set system syslog global archive file 10",
    #     "delete system syslog global archive size 111",
    #     "delete system syslog global marker",
    #     "delete system syslog global preserve-fqdn"
    # ],

    # After state:
    # ------------

    # vyos:~$show configuration commands | grep syslog
    # set system syslog console facility all
    # set system syslog console facility local7 level 'err'
    # set system syslog console facility news level 'debug'
    # set system syslog file logFileNew
    # set system syslog global archive file '10'
    # set system syslog host 172.16.0.2 facility local5 level 'all'

    # Using state: replaced

    # Before state:
    # -------------

    # vyos:~$show configuration commands | grep syslog
    # set system syslog console facility all
    # set system syslog console facility local7 level 'err'
    # set system syslog console facility news level 'debug'
    # set system syslog file logFileNew
    # set system syslog global archive file '10'
    # set system syslog host 172.16.0.2 facility local5 level 'all'

    - name: Replace with the provided configuration
      register: result
      vyos.vyos.vyos_logging_global:
        config:
          console:
            facilities:
              - facility: local6
          users:
            - username: paul
              facilities:
              - facility: local7
                severity: err
        state: replaced

    # Commands Fired:
    # ---------------

    # "commands": [
    #     "delete system syslog console facility all",
    #     "delete system syslog console facility local7",
    #     "delete system syslog console facility news",
    #     "delete system syslog file logFileNew",
    #     "delete system syslog global archive file 10",
    #     "delete system syslog host 172.16.0.2",
    #     "set system syslog console facility local6",
    #     "set system syslog user paul facility local7 level err"
    # ],

    # After state:
    # ------------

    # vyos:~$show configuration commands | grep syslog
    # set system syslog console facility local6
    # set system syslog user paul facility local7 level 'err'

    # Using state: gathered

    - name: Gather logging config
      vyos.vyos.vyos_logging_global:
        state: gathered

    # Module Execution Result:
    # ------------------------

    # "gathered": {
    #     "console": {
    #         "facilities": [
    #             {
    #                 "facility": "local6"
    #             },
    #             {
    #                 "facility": "local7",
    #                 "severity": "err"
    #             }
    #         ]
    #     },
    #     "files": [
    #         {
    #             "archive": {
    #                 "file_num": 2
    #             },
    #             "facilities": [
    #                 {
    #                     "facility": "local6",
    #                     "severity": "emerg"
    #                 }
    #             ],
    #             "path": "logFile"
    #         }
    #     ],
    #     "global_params": {
    #         "archive": {
    #             "file_num": 2,
    #             "size": 111
    #         },
    #         "facilities": [
    #             {
    #                 "facility": "cron",
    #                 "severity": "debug"
    #             }
    #         ],
    #         "marker_interval": 111,
    #         "preserve_fqdn": true
    #     },
    #     "hosts": [
    #         {
    #             "facilities": [
    #                 {
    #                     "facility": "all",
    #                     "protocol": "udp"
    #                 },
    #                 {
    #                     "facility": "local7",
    #                     "severity": "all"
    #                 }
    #             ],
    #             "hostname": "172.16.0.1",
    #             "port": 223
    #         }
    #     ],
    #     "users": [
    #         {
    #             "facilities": [
    #                 {
    #                     "facility": "local7",
    #                     "severity": "err"
    #                 }
    #             ],
    #             "username": "paul"
    #         },
    #         {
    #             "facilities": [
    #                 {
    #                     "facility": "local7",
    #                     "severity": "debug"
    #                 }
    #             ],
    #             "username": "vyos"
    #         }
    #     ]
    # },

    # After state:
    # ------------

    # vyos:~$show configuration commands | grep syslog
    # set system syslog console facility local6
    # set system syslog console facility local7 level 'err'
    # set system syslog file logFile archive file '2'
    # set system syslog file logFile facility local6 level 'emerg'
    # set system syslog global archive file '2'
    # set system syslog global archive size '111'
    # set system syslog global facility cron level 'debug'
    # set system syslog global marker interval '111'
    # set system syslog global preserve-fqdn
    # set system syslog host 172.16.0.1 facility all protocol 'udp'
    # set system syslog host 172.16.0.1 facility local7 level 'all'
    # set system syslog host 172.16.0.1 port '223'
    # set system syslog user paul facility local7 level 'err'
    # set system syslog user vyos facility local7 level 'debug'

    # Using state: rendered

    - name: Render the provided configuration
      vyos.vyos.vyos_logging_global:
        config:
          console:
            facilities:
              - facility: local7
                severity: err
          files:
            - path: logFile
              archive:
                file_num: 2
              facilities:
                - facility: local6
                  severity: emerg
          hosts:
            - hostname: 172.16.0.1
              facilities:
                - facility: local7
                  severity: all
                - facility: all
                  protocol: udp
              port: 223
          users:
            - username: vyos
              facilities:
                - facility: local7
                  severity: debug
          global_params:
            archive:
              file_num: 2
              size: 111
            facilities:
              - facility: cron
                severity: debug
            marker_interval: 111
            preserve_fqdn: true
        state: rendered

    # Module Execution Result:
    # ------------------------

    # "rendered": [
    #     "set system syslog console facility local7 level err",
    #     "set system syslog file logFile facility local6 level emerg",
    #     "set system syslog file logFile archive file 2",
    #     "set system syslog host 172.16.0.1 facility local7 level all",
    #     "set system syslog host 172.16.0.1 facility all protocol udp",
    #     "set system syslog host 172.16.0.1 port 223",
    #     "set system syslog user vyos facility local7 level debug",
    #     "set system syslog global facility cron level debug",
    #     "set system syslog global archive file 2",
    #     "set system syslog global archive size 111",
    #     "set system syslog global marker interval 111",
    #     "set system syslog global preserve-fqdn"
    # ]

    # Using state: parsed

    # File: parsed.cfg
    # ----------------

    # set system syslog console facility local6
    # set system syslog console facility local7 level 'err'
    # set system syslog file logFile archive file '2'
    # set system syslog file logFile facility local6 level 'emerg'
    # set system syslog global archive file '2'
    # set system syslog global archive size '111'
    # set system syslog global facility cron level 'debug'
    # set system syslog global marker interval '111'
    # set system syslog global preserve-fqdn
    # set system syslog host 172.16.0.1 facility all protocol 'udp'
    # set system syslog host 172.16.0.1 facility local7 level 'all'
    # set system syslog host 172.16.0.1 port '223'
    # set system syslog user paul facility local7 level 'err'
    # set system syslog user vyos facility local7 level 'debug'

    - name: Parse the provided configuration
      vyos.vyos.vyos_logging_global:
        running_config: "{{ lookup('file', 'parsed_vyos.cfg') }}"
        state: parsed

    # Module Execution Result:
    # ------------------------

    # "parsed": {
    #     "console": {
    #         "facilities": [
    #             {
    #                 "facility": "local6"
    #             },
    #             {
    #                 "facility": "local7",
    #                 "severity": "err"
    #             }
    #         ]
    #     },
    #     "files": [
    #         {
    #             "archive": {
    #                 "file_num": 2
    #             },
    #             "facilities": [
    #                 {
    #                     "facility": "local6",
    #                     "severity": "emerg"
    #                 }
    #             ],
    #             "path": "logFile"
    #         }
    #     ],
    #     "global_params": {
    #         "archive": {
    #             "file_num": 2,
    #             "size": 111
    #         },
    #         "facilities": [
    #             {
    #                 "facility": "cron",
    #                 "severity": "debug"
    #             }
    #         ],
    #         "marker_interval": 111,
    #         "preserve_fqdn": true
    #     },
    #     "hosts": [
    #         {
    #             "facilities": [
    #                 {
    #                     "facility": "all",
    #                     "protocol": "udp"
    #                 },
    #                 {
    #                     "facility": "local7",
    #                     "severity": "all"
    #                 }
    #             ],
    #             "hostname": "172.16.0.1",
    #             "port": 223
    #         }
    #     ],
    #     "users": [
    #         {
    #             "facilities": [
    #                 {
    #                     "facility": "local7",
    #                     "severity": "err"
    #                 }
    #             ],
    #             "username": "paul"
    #         },
    #         {
    #             "facilities": [
    #                 {
    #                     "facility": "local7",
    #                     "severity": "debug"
    #                 }
    #             ],
    #             "username": "vyos"
    #         }
    #     ]
    #   }
    # }



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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em> or <em>purged</em></td>
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em> or <em>purged</em></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set system syslog console facility local7 level err&#x27;, &#x27;set system syslog host 172.16.0.1 port 223&#x27;, &#x27;set system syslog global archive size 111&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;set system syslog host 172.16.0.1 port 223&#x27;, &#x27;set system syslog user vyos facility local7 level debug&#x27;, &#x27;set system syslog global facility cron level debug&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Sagar Paul (@KB-perByte)
