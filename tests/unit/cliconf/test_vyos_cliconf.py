# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function


__metaclass__ = type

import unittest

from unittest.mock import MagicMock, patch

from ansible_collections.vyos.vyos.plugins.cliconf.vyos import Cliconf
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos import vyos


class TestVyosCliconfDeviceInfo(unittest.TestCase):
    def device_info(self, show_version):
        cliconf = Cliconf(MagicMock())
        cliconf.get = MagicMock(
            side_effect=lambda command: {
                "show version": show_version,
                "show host name": "vyos",
            }[command],
        )
        return cliconf.get_device_info()

    def test_1_3(self):
        info = self.device_info("Version:          VyOS 1.3.8\nHW model:         KVM\n")
        self.assertEqual(info["network_os_version"], "VyOS 1.3.8")
        self.assertEqual(info["network_os_major_version"], "1.3")
        self.assertEqual(info["network_os_model"], "KVM")

    def test_1_4(self):
        info = self.device_info("Version:          VyOS 1.4.1\nHardware model:   KVM\n")
        self.assertEqual(info["network_os_major_version"], "1.4")
        self.assertEqual(info["network_os_model"], "KVM")

    def test_1_5_rolling(self):
        info = self.device_info("Version:          VyOS 1.5-rolling-202409250007\n")
        self.assertEqual(info["network_os_major_version"], "1.5")

    def test_date_based_rolling(self):
        info = self.device_info("Version:          VyOS 2025.11.20-0019-rolling\n")
        self.assertEqual(info["network_os_version"], "VyOS 2025.11.20-0019-rolling")
        self.assertEqual(info["network_os_major_version"], "2025.11")

    def test_unparseable_version_fails_with_message(self):
        info = self.device_info("Version:          VyOS custom-build\n")
        self.assertEqual(info["network_os_version"], "VyOS custom-build")
        self.assertNotIn("network_os_major_version", info)

        module = MagicMock()
        module.fail_json.side_effect = SystemExit
        connection = MagicMock()
        connection.get_device_info.return_value = info
        with patch.object(vyos, "get_connection", return_value=connection):
            with self.assertRaises(SystemExit):
                vyos.get_os_version(module)
        self.assertIn("VyOS custom-build", module.fail_json.call_args[1]["msg"])

    def test_missing_version_line(self):
        info = self.device_info("Something unexpected\n")
        self.assertNotIn("network_os_version", info)
        self.assertNotIn("network_os_major_version", info)
