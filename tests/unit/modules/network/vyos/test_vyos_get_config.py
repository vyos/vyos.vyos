# Make coding more python3-ish
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import MagicMock, patch

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos import vyos

from .vyos_module import TestVyosModule


class TestVyosGetConfig(TestVyosModule):
    def setUp(self):
        super(TestVyosGetConfig, self).setUp()
        vyos._DEVICE_CONFIGS = None
        self.connection = MagicMock()
        self.connection.get_config.return_value = " set system host-name vyos \n"
        patcher = patch.object(vyos, "get_connection", return_value=self.connection)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(setattr, vyos, "_DEVICE_CONFIGS", None)

    @staticmethod
    def _module(match=None):
        module = MagicMock()
        module.params = {"match": match}
        return module

    def test_no_cache_initially(self):
        self.assertIsNone(vyos._DEVICE_CONFIGS)

    def test_full_read_populates_cache(self):
        cfg = vyos.get_config(self._module())
        self.assertEqual(cfg, "set system host-name vyos")
        self.assertEqual(vyos._DEVICE_CONFIGS, cfg)

    def test_cache_used_when_match_none(self):
        module = self._module(match="none")
        vyos.get_config(module)
        self.connection.get_config.return_value = "changed"
        self.assertEqual(vyos.get_config(module), "set system host-name vyos")
        self.assertEqual(self.connection.get_config.call_count, 1)

    def test_cache_not_used_when_match_not_none(self):
        module = self._module(match="line")
        vyos.get_config(module)
        self.connection.get_config.return_value = "changed"
        self.assertEqual(vyos.get_config(module), "changed")
        self.assertEqual(self.connection.get_config.call_count, 2)

    def test_cache_not_used_without_match_param(self):
        module = MagicMock()
        module.params = {}
        vyos.get_config(module)
        vyos.get_config(module)
        self.assertEqual(self.connection.get_config.call_count, 2)

    def test_flags_bypass_cache_and_do_not_populate_it(self):
        module = self._module(match="none")
        cfg = vyos.get_config(module, flags=["system login"])
        self.assertEqual(cfg, "set system host-name vyos")
        self.assertIsNone(vyos._DEVICE_CONFIGS)

    def test_flags_bypass_existing_cache(self):
        module = self._module(match="none")
        vyos.get_config(module)
        self.connection.get_config.return_value = "partial"
        self.assertEqual(vyos.get_config(module, flags=["system login"]), "partial")
        self.assertEqual(vyos._DEVICE_CONFIGS, "set system host-name vyos")

    def test_format_bypasses_cache_and_does_not_populate_it(self):
        module = self._module(match="none")
        vyos.get_config(module, format="set")
        self.assertIsNone(vyos._DEVICE_CONFIGS)
        self.connection.get_config.assert_called_with(flags=[], format="set")

    def test_connection_error_fails_module(self):
        module = self._module()
        module.fail_json.side_effect = SystemExit
        self.connection.get_config.side_effect = vyos.ConnectionError("boom")
        with self.assertRaises(SystemExit):
            vyos.get_config(module)
        module.fail_json.assert_called_once_with(msg="boom")
