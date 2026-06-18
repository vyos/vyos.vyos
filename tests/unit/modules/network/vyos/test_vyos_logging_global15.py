#
# (c) 2021, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_logging_global
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args

from .vyos_module import TestVyosModule


class TestVyosLoggingGlobalModule(TestVyosModule):
    module = vyos_logging_global

    def setUp(self):
        super(TestVyosLoggingGlobalModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.logging_global.logging_global.Logging_globalFacts.get_logging_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

        self.mock_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.config.logging_global.logging_global.get_os_version",
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "1.5"

        self.mock_facts_get_os_version = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.logging_global.logging_global.get_os_version",
        )
        self.get_facts_os_version = self.mock_facts_get_os_version.start()
        self.get_facts_os_version.return_value = "1.5"

    def tearDown(self):
        super(TestVyosLoggingGlobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()
        self.mock_get_os_version.stop()
        self.mock_facts_get_os_version.stop()

    def test_vyos_logging_global_merged_idempotent(self):
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog console facility local7 level 'err'
            set system syslog console facility news level 'debug'
            set system syslog local facility cron level 'debug'
            set system syslog local facility local7 level 'debug'
            set system syslog marker interval '111'
            set system syslog preserve-fqdn
            set system syslog remote 10.0.2.12 facility all
            set system syslog remote 10.0.2.15 facility all level 'all'
            set system syslog remote 10.0.2.15 port '122'
            """,
        )
        playbook = dict(
            config=dict(
                console=dict(
                    facilities=[
                        dict(facility="all"),
                        dict(facility="local7", severity="err"),
                        dict(facility="news", severity="debug"),
                    ],
                ),
                hosts=[
                    dict(
                        hostname="10.0.2.15",
                        port=122,
                        facilities=[dict(facility="all", severity="all")],
                    ),
                    dict(
                        hostname="10.0.2.12",
                        facilities=[dict(facility="all")],
                    ),
                ],
                global_params=dict(
                    marker_interval=111,
                    preserve_fqdn=True,
                    facilities=[
                        dict(facility="cron", severity="debug"),
                        dict(facility="local7", severity="debug"),
                    ],
                ),
            ),
        )
        compare_cmds = []
        playbook["state"] = "merged"
        set_module_args(playbook)
        result = self.execute_module()
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_merged(self):
        self.execute_show_command.return_value = dedent(
            """\
            """,
        )
        playbook = dict(
            config=dict(
                console=dict(
                    facilities=[
                        dict(facility="all"),
                        dict(facility="local7", severity="err"),
                        dict(facility="news", severity="debug"),
                    ],
                ),
                hosts=[
                    dict(
                        hostname="10.0.2.15",
                        port=122,
                        facilities=[dict(facility="all", severity="all")],
                    ),
                    dict(
                        hostname="10.0.2.12",
                        facilities=[dict(facility="all", severity="info")],
                    ),
                ],
                global_params=dict(
                    marker_interval=111,
                    preserve_fqdn=True,
                    facilities=[
                        dict(facility="cron", severity="debug"),
                        dict(facility="local7", severity="debug"),
                    ],
                ),
            ),
        )
        compare_cmds = [
            "set system syslog console facility all",
            "set system syslog console facility local7 level err",
            "set system syslog console facility news level debug",
            "set system syslog local facility cron level debug",
            "set system syslog local facility local7 level debug",
            "set system syslog marker interval 111",
            "set system syslog preserve-fqdn",
            "set system syslog remote 10.0.2.15 facility all level all",
            "set system syslog remote 10.0.2.15 port 122",
            "set system syslog remote 10.0.2.12 facility all level info",
        ]
        playbook["state"] = "merged"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_deleted(self):
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog console facility local7 level 'err'
            set system syslog local facility cron level 'debug'
            set system syslog local facility local7 level 'debug'
            set system syslog marker interval '111'
            set system syslog preserve-fqdn
            set system syslog remote 10.0.2.12 facility all
            set system syslog remote 10.0.2.15 facility all level 'all'
            set system syslog remote 10.0.2.15 port '122'
            """,
        )
        playbook = dict(config=dict())
        compare_cmds = ["delete system syslog"]
        playbook["state"] = "deleted"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_replaced(self):
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog console facility local7 level 'err'
            set system syslog console facility news level 'debug'
            set system syslog local facility cron level 'debug'
            set system syslog local facility local7 level 'debug'
            set system syslog marker interval '111'
            set system syslog preserve-fqdn
            set system syslog remote 10.0.2.12 facility all
            set system syslog remote 10.0.2.15 facility all level 'all'
            set system syslog remote 10.0.2.15 port '122'
            """,
        )
        playbook = dict(
            config=dict(
                console=dict(
                    facilities=[dict(facility="local7", severity="emerg")],
                ),
                hosts=[
                    dict(
                        hostname="10.0.2.15",
                        port=122,
                        facilities=[dict(facility="all", severity="all")],
                    ),
                ],
            ),
        )
        compare_cmds = [
            "delete system syslog console facility all",
            "delete system syslog console facility local7",
            "delete system syslog console facility news",
            "delete system syslog local facility cron",
            "delete system syslog local facility local7",
            "delete system syslog marker",
            "delete system syslog preserve-fqdn",
            "delete system syslog remote 10.0.2.12",
            "set system syslog console facility local7 level emerg",
        ]
        playbook["state"] = "replaced"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_replaced_idempotent(self):
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility local6
            """,
        )
        playbook = dict(config=dict(console=dict(facilities=[dict(facility="local6")])))
        compare_cmds = []
        playbook["state"] = "replaced"
        set_module_args(playbook)
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_overridden(self):
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console
            set system syslog local
            """,
        )
        playbook = dict(
            config=dict(
                console=dict(
                    facilities=[dict(facility="local7", severity="emerg")],
                ),
                global_params=dict(
                    facilities=[dict(facility="all", severity="info")],
                ),
            ),
        )
        compare_cmds = [
            "set system syslog console facility local7 level emerg",
            "set system syslog local facility all level info",
        ]
        playbook["state"] = "overridden"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_rendered(self):
        playbook = dict(
            config=dict(
                console=dict(facilities=[dict(facility="all")]),
                hosts=[
                    dict(
                        hostname="10.0.2.16",
                        facilities=[dict(facility="local6")],
                    ),
                ],
                global_params=dict(
                    preserve_fqdn=True,
                    facilities=[dict(facility="all", severity="info")],
                ),
            ),
        )
        compare_cmds = [
            "set system syslog console facility all",
            "set system syslog remote 10.0.2.16 facility local6",
            "set system syslog preserve-fqdn",
            "set system syslog local facility all level info",
        ]
        playbook["state"] = "rendered"
        set_module_args(playbook)
        result = self.execute_module()
        self.maxDiff = None
        self.assertEqual(sorted(result["rendered"]), sorted(compare_cmds))

    def test_vyos_logging_global_parsed(self):
        set_module_args(
            dict(
                running_config=dedent(
                    """\
                    set system syslog console facility all
                    set system syslog local facility all level 'info'
                    set system syslog remote 10.0.2.1 facility all level 'info'
                    set system syslog remote 10.0.2.1 port '514'
                    """,
                ),
                state="parsed",
            ),
        )
        parsed = dict(
            console=dict(facilities=[dict(facility="all")]),
            global_params=dict(facilities=[dict(facility="all", severity="info")]),
            hosts=[
                dict(
                    hostname="10.0.2.1",
                    port=514,
                    facilities=[dict(facility="all", severity="info")],
                ),
            ],
        )
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(result["parsed"], parsed)

    def test_vyos_logging_global_gathered(self):
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog local facility all level 'info'
            set system syslog remote 10.0.2.1 facility all level 'info'
            """,
        )
        set_module_args(dict(state="gathered"))
        gathered = dict(
            console=dict(facilities=[dict(facility="all")]),
            global_params=dict(facilities=[dict(facility="all", severity="info")]),
            hosts=[
                dict(
                    hostname="10.0.2.1",
                    facilities=[dict(facility="all", severity="info")],
                ),
            ],
        )
        result = self.execute_module(changed=False)
        self.maxDiff = None
        self.assertEqual(result["gathered"], gathered)
