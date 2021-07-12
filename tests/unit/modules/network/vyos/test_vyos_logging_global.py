#
# (c) 2021, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from textwrap import dedent
from ansible_collections.vyos.vyos.tests.unit.compat.mock import patch
from ansible_collections.vyos.vyos.plugins.modules import vyos_logging_global
from ansible_collections.vyos.vyos.tests.unit.modules.utils import set_module_args
from .vyos_module import TestVyosModule


class TestVyosLoggingGlobalModule(TestVyosModule):

    module = vyos_logging_global

    def setUp(self):
        super(TestVyosLoggingGlobalModule, self).setUp()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
        )
        self.get_resource_connection_facts = (
            self.mock_get_resource_connection_facts.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.logging_global.logging_global.Logging_globalFacts.get_logging_data"
        )

        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestVyosLoggingGlobalModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_execute_show_command.stop()

    def test_vyos_logging_global_merged_idempotent(self):
        """
        passing all commands as have and expecting [] commands
        """
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog console facility local7 level 'err'
            set system syslog console facility news level 'debug'
            set system syslog file xyz
            set system syslog file abc archive size '125'
            set system syslog file def archive file '2'
            set system syslog file def facility local6 level 'emerg'
            set system syslog file def facility local7 level 'emerg'
            set system syslog global archive file '2'
            set system syslog global archive size '111'
            set system syslog global facility cron level 'debug'
            set system syslog global facility local7 level 'debug'
            set system syslog global marker interval '111'
            set system syslog global preserve-fqdn
            set system syslog host 10.0.2.12 facility all protocol 'udp'
            set system syslog host 10.0.2.15 facility all level 'all'
            set system syslog host 10.0.2.15 facility all protocol 'udp'
            set system syslog host 10.0.2.15 port '122'
            set system syslog user paul facility local7 level 'err'
            set system syslog user vyos facility local6 level 'alert'
            set system syslog user vyos facility local7 level 'debug'
            """
        )
        playbook = dict(
            config=dict(
                console=dict(
                    facilities=[
                        dict(facility="all"),
                        dict(facility="local7", level="err"),
                        dict(facility="news", level="debug"),
                    ]
                ),
                files=[
                    dict(path="xyz"),
                    dict(path="abc", archive=dict(size=125)),
                    dict(
                        path="def",
                        archive=dict(file_num=2),
                        facilities=[
                            dict(facility="local6", level="emerg"),
                            dict(facility="local7", level="emerg"),
                        ],
                    ),
                ],
                hosts=[
                    dict(
                        hostname="10.0.2.15",
                        port=122,
                        facilities=[
                            dict(facility="all", level="all"),
                            dict(facility="all", protocol="udp"),
                        ],
                    ),
                    dict(
                        hostname="10.0.2.12",
                        facilities=[dict(facility="all", protocol="udp")],
                    ),
                ],
                users=[
                    dict(
                        username="vyos",
                        facilities=[
                            dict(facility="local7", level="debug"),
                            dict(facility="local6", level="alert"),
                        ],
                    ),
                    dict(
                        username="paul",
                        facilities=[dict(facility="local7", level="err")],
                    ),
                ],
                global_params=dict(
                    archive=dict(size=111, file_num=2),
                    marker_interval=111,
                    preserve_fqdn="True",
                    facilities=[
                        dict(facility="cron", level="debug"),
                        dict(facility="local7", level="debug"),
                    ],
                ),
            )
        )
        compare_cmds = []
        playbook["state"] = "merged"
        set_module_args(playbook)
        result = self.execute_module()

        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_merged(self):
        """
        passing all commands as have and expecting [] commands
        """
        self.execute_show_command.return_value = dedent(
            """\
            """
        )
        playbook = dict(
            config=dict(
                console=dict(
                    facilities=[
                        dict(facility="all"),
                        dict(facility="local7", level="err"),
                        dict(facility="news", level="debug"),
                    ]
                ),
                files=[
                    dict(path="xyz"),
                    dict(path="abc", archive=dict(size=125)),
                    dict(
                        path="def",
                        archive=dict(file_num=2),
                        facilities=[
                            dict(facility="local6", level="emerg"),
                            dict(facility="local7", level="emerg"),
                        ],
                    ),
                ],
                hosts=[
                    dict(
                        hostname="10.0.2.15",
                        port=122,
                        facilities=[
                            dict(facility="all", level="all"),
                            dict(facility="all", protocol="udp"),
                        ],
                    ),
                    dict(
                        hostname="10.0.2.12",
                        facilities=[dict(facility="all", protocol="udp")],
                    ),
                ],
                users=[
                    dict(
                        username="vyos",
                        facilities=[
                            dict(facility="local7", level="debug"),
                            dict(facility="local6", level="alert"),
                        ],
                    ),
                    dict(
                        username="paul",
                        facilities=[dict(facility="local7", level="err")],
                    ),
                ],
                global_params=dict(
                    archive=dict(size=111, file_num=2),
                    marker_interval=111,
                    preserve_fqdn="True",
                    facilities=[
                        dict(facility="cron", level="debug"),
                        dict(facility="local7", level="debug"),
                    ],
                ),
            )
        )
        compare_cmds = [
            "set system syslog user paul facility local7 level err",
            "set system syslog host 10.0.2.15 facility all protocol udp",
            "set system syslog global marker interval 111",
            "set system syslog file def archive file 2",
            "set system syslog file abc archive size 125",
            "set system syslog console facility local7 level err",
            "set system syslog host 10.0.2.12 facility all protocol udp",
            "set system syslog global facility local7 level debug",
            "set system syslog host 10.0.2.15 facility all level all",
            "set system syslog global preserve-fqdn",
            "set system syslog global archive file 2",
            "set system syslog console facility all",
            "set system syslog file xyz",
            "set system syslog file def facility local7 level emerg",
            "set system syslog console facility news level debug",
            "set system syslog user vyos facility local6 level alert",
            "set system syslog global facility cron level debug",
            "set system syslog file def facility local6 level emerg",
            "set system syslog global archive size 111",
            "set system syslog host 10.0.2.15 port 122",
            "set system syslog user vyos facility local7 level debug",
        ]
        playbook["state"] = "merged"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        # print(result["commands"])
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_deleted(self):
        """
        passing all commands as have and expecting [] commands
        """
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog console facility local7 level 'err'
            set system syslog console facility news level 'debug'
            set system syslog file xyz
            set system syslog file abc archive size '125'
            set system syslog file def archive file '2'
            set system syslog file def facility local6 level 'emerg'
            set system syslog file def facility local7 level 'emerg'
            set system syslog global archive file '2'
            set system syslog global archive size '111'
            set system syslog global facility cron level 'debug'
            set system syslog global facility local7 level 'debug'
            set system syslog global marker interval '111'
            set system syslog global preserve-fqdn
            set system syslog host 10.0.2.12 facility all protocol 'udp'
            set system syslog host 10.0.2.15 facility all level 'all'
            set system syslog host 10.0.2.15 facility all protocol 'udp'
            set system syslog host 10.0.2.15 port '122'
            set system syslog user paul facility local7 level 'err'
            set system syslog user vyos facility local6 level 'alert'
            set system syslog user vyos facility local7 level 'debug'
            """
        )
        playbook = dict(config=dict())
        compare_cmds = [
            "delete system syslog console",
            "delete system syslog file",
            "delete system syslog global",
            "delete system syslog host",
            "delete system syslog user",
        ]
        playbook["state"] = "deleted"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_replaced(self):
        """
        passing all commands as have and expecting [] commands
        """
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console facility all
            set system syslog console facility local7 level 'err'
            set system syslog console facility news level 'debug'
            set system syslog file xyz
            set system syslog file abc archive size '125'
            set system syslog file def archive file '2'
            set system syslog file def facility local6 level 'emerg'
            set system syslog file def facility local7 level 'emerg'
            set system syslog global archive file '2'
            set system syslog global archive size '111'
            set system syslog global facility cron level 'debug'
            set system syslog global facility local7 level 'debug'
            set system syslog global marker interval '111'
            set system syslog global preserve-fqdn
            set system syslog host 10.0.2.12 facility all protocol 'udp'
            set system syslog host 10.0.2.15 facility all level 'all'
            set system syslog host 10.0.2.15 facility all protocol 'udp'
            set system syslog host 10.0.2.15 port '122'
            set system syslog user paul facility local7 level 'err'
            set system syslog user vyos facility local6 level 'alert'
            set system syslog user vyos facility local7 level 'debug'
            """
        )
        playbook = dict(
            config=dict(
                console=dict(facilities=[dict(facility="local7", level="emerg")]),
                files=[
                    dict(
                        path="abc",
                        archive=dict(file_num=2),
                        facilities=[
                            dict(facility="local6", level="err"),
                            dict(facility="local7", level="emerg"),
                        ],
                    )
                ],
            )
        )
        compare_cmds = [
            "delete system syslog console",
            "delete system syslog file",
            "delete system syslog global",
            "delete system syslog host",
            "delete system syslog user",
            "set system syslog console facility local7 level emerg",
            "set system syslog file abc facility local6 level err",
            "set system syslog file abc facility local7 level emerg",
            "set system syslog file abc archive file 2",
        ]
        playbook["state"] = "replaced"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        print(result["commands"])
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_overridden(self):
        """
        passing all commands as have and expecting [] commands
        """
        self.execute_show_command.return_value = dedent(
            """\
            set system syslog console
            set system syslog global
            """
        )
        playbook = dict(
            config=dict(
                console=dict(facilities=[dict(facility="local7", level="emerg")]),
                files=[
                    dict(
                        path="abc",
                        archive=dict(file_num=2),
                        facilities=[
                            dict(facility="local6", level="err"),
                            dict(facility="local7", level="emerg"),
                        ],
                    )
                ],
            )
        )
        compare_cmds = [
            "delete system syslog console",
            "delete system syslog global",
            "set system syslog console facility local7 level emerg",
            "set system syslog file abc facility local6 level err",
            "set system syslog file abc facility local7 level emerg",
            "set system syslog file abc archive file 2",
        ]
        playbook["state"] = "overridden"
        set_module_args(playbook)
        result = self.execute_module(changed=True)
        print(result["commands"])
        self.maxDiff = None
        self.assertEqual(sorted(result["commands"]), sorted(compare_cmds))

    def test_vyos_logging_global_rendered(self):
        """
        passing all commands as have and expecting [] commands
        """
        playbook = dict(
            config=dict(
                console=dict(facilities=[dict(facility="all")]),
                hosts=[
                    dict(hostname="10.0.2.16", facilities=[dict(facility="local6")])
                ],
                users=[
                    dict(username="vyos"),
                    dict(username="paul", facilities=[dict(facility="local7")]),
                ],
            )
        )
        compare_cmds = [
            "set system syslog console facility all",
            "set system syslog host 10.0.2.16 facility local6",
            "set system syslog user vyos",
            "set system syslog user paul facility local7",
        ]
        playbook["state"] = "rendered"
        set_module_args(playbook)
        result = self.execute_module()
        self.maxDiff = None
        self.assertEqual(sorted(result["rendered"]), sorted(compare_cmds))
