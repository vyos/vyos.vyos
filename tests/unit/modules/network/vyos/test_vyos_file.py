# tests/unit/modules/network/vyos/test_vyos_file.py
#
# Mocks run_commands() directly — the real call path this module uses via
# get_connection()/run_commands() in module_utils/network/vyos/vyos.py.
# This replaces an earlier draft that mocked a bespoke ActionModule; that
# design was abandoned once it turned out every module in this collection
# (vyos_command, vyos_config, etc.) shares one generic action plugin and
# puts real logic inside main() instead.

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import json

from unittest.mock import patch

from ansible_collections.vyos.vyos.plugins.modules import vyos_file
from ansible_collections.vyos.vyos.tests.unit.modules.network.vyos.vyos_module import (
    TestVyosModule,
)
from ansible_collections.vyos.vyos.tests.unit.modules.utils import (
    AnsibleExitJson,
    AnsibleFailJson,
    set_module_args,
)


class TestVyosFileModule(TestVyosModule):

    module = vyos_file

    def setUp(self):
        super(TestVyosFileModule, self).setUp()
        self.mock_run_commands = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_file.run_commands",
        )
        self.run_commands = self.mock_run_commands.start()

    def tearDown(self):
        super(TestVyosFileModule, self).tearDown()
        self.mock_run_commands.stop()

    # ---- helpers -----------------------------------------------------

    def _queue(self, *responses):
        """Queue successive return values, one per run_commands() call."""
        self.run_commands.side_effect = list(responses)

    def _run(self, args, expect_fail=False):
        set_module_args(args)
        exc = AnsibleFailJson if expect_fail else AnsibleExitJson
        with self.assertRaises(exc) as ctx:
            vyos_file.main()
        return ctx.exception.args[0]

    # ---- idempotency core ---------------------------------------------

    def test_creates_when_absent(self):
        # get_have() issues ONE stat call; converge() batches mkdir+chown+
        # chmod into a SINGLE run_commands() call (not one call per
        # command); the post-check issues one more stat call. Three total
        # run_commands() invocations, matching the module's actual batching.
        self._queue(
            ["stat: cannot statx '/config/auth/x': No such file or directory"],
            ["", "", ""],  # mkdir, chown, chmod — one batched call
            ["750 vyos vyattacfg 4096"],  # post-check stat
        )
        result = self._run(
            {"dest": "/config/auth/x", "owner": "vyos", "group": "vyattacfg", "mode": "0750"},
        )
        self.assertTrue(result["changed"])
        self.assertIn("state", result["diff_fields"])
        self.assertIn("owner", result["diff_fields"])

    def test_noop_when_converged(self):
        self._queue(["750 vyos vyattacfg 4096"])
        result = self._run(
            {"dest": "/config/auth/x", "owner": "vyos", "group": "vyattacfg", "mode": "0750"},
        )
        self.assertFalse(result["changed"])
        self.assertEqual(result["diff_fields"], [])

    def test_setgid_ignored_when_mode_leading_digit_is_zero(self):
        # /config/auth is deliberately setgid vyattacfg (vyos.dev T2713).
        # Requesting mode '0750' (leading digit 0) must NOT be reported as
        # different from an actual mode of 2750.
        self._queue(["2750 vyos vyattacfg 4096"])
        result = self._run({"dest": "/config/auth/x", "mode": "0750"})
        self.assertFalse(result["changed"], result.get("diff_fields"))

    def test_setgid_respected_when_explicitly_requested(self):
        # Explicit non-zero leading digit means the caller does care about
        # the special bits — since 2750 is requested and 2750 is already
        # there, this should be a no-op (only the initial stat call fires).
        self._queue(["2750 vyos vyattacfg 4096"])
        result = self._run({"dest": "/config/auth/x", "mode": "2750"})
        self.assertFalse(result["changed"])

    def test_mode_change_detected(self):
        # Only mode differs, so converge() batches a single chmod command
        # (one run_commands() call), then the post-check stat is a second.
        self._queue(
            ["600 vyos vyattacfg 10"],
            [""],  # chmod — the only mutating command needed
            ["640 vyos vyattacfg 10"],
        )
        result = self._run({"dest": "/config/auth/x/hello.txt", "mode": "0640"})
        self.assertTrue(result["changed"])
        self.assertEqual(result["diff_fields"], ["mode"])

    def test_mode_string_normalization(self):
        for requested in ("640", "0640", "00640"):
            with self.subTest(requested=requested):
                self._queue(["640 vyos vyattacfg 10"])
                result = self._run({"dest": "/config/auth/x/hello.txt", "mode": requested})
                self.assertFalse(
                    result["changed"],
                    "mode {0!r} incorrectly compared unequal to stat's '640'".format(requested),
                )

    # ---- content ---------------------------------------------------------

    def test_content_push_detected_and_verified(self):
        # need_content_hash is True (content was given), but get_have()
        # only actually hashes when the path already exists — on the
        # initial (absent) lookup it's skipped, so that first call is a
        # single stat. converge() batches base64-write + chown into one
        # call. The post-check, now that the file exists, issues stat AND
        # sha256sum as two separate calls. The queued hash must be the
        # REAL sha256("hi\n") hex digest, or the module's own post-check
        # will (correctly) call fail_json on a genuine mismatch.
        real_hash = "98ea6e4f216f2fb4b69fff9b3a44842c38686ca685f3f55dc48c5d3fb1107be4"
        self._queue(
            ["stat: cannot statx '/config/auth/x/hello.txt': No such file or directory"],
            ["", "", ""],  # base64 write, chown, chmod — batched (mode was also requested)
            ["600 vyos vyattacfg 10"],  # post-check stat
            ["{0}  /config/auth/x/hello.txt".format(real_hash)],  # post-check sha256sum
        )
        result = self._run(
            {
                "dest": "/config/auth/x/hello.txt",
                "content": "hi\n",
                "owner": "vyos",
                "mode": "0600",
            },
        )
        self.assertTrue(result["changed"])
        self.assertIn("content", result["diff_fields"])

    def test_content_hash_looked_up_only_when_relevant(self):
        # plain ownership/mode management on an existing path should never
        # trigger a sha256sum call — that's the whole point of the
        # need_content_hash gate.
        self._queue(["750 vyos vyattacfg 4096"])
        self._run({"dest": "/config/auth/x", "mode": "0750"})
        called_commands = [c.args[1] for c in self.run_commands.call_args_list]
        joined = " ".join(str(c) for c in called_commands)
        self.assertNotIn("sha256sum", joined)

    # ---- absent state ----------------------------------------------------

    def test_absent_on_existing_removes(self):
        self._queue(
            ["600 vyos vyattacfg 10"],
            [""],  # rm -rf
            ["stat: cannot statx '/config/auth/x/hello.txt': No such file or directory"],
        )
        result = self._run({"dest": "/config/auth/x/hello.txt", "state": "absent"})
        self.assertTrue(result["changed"])
        self.assertEqual(result["diff_fields"], ["state"])

    def test_absent_noop_when_already_gone(self):
        self._queue(["stat: cannot statx '/x': No such file or directory"])
        result = self._run({"dest": "/x", "state": "absent"})
        self.assertFalse(result["changed"])

    # ---- silent-failure detection (the real bug this caught on hardware) --

    def test_post_check_fails_module_when_chown_silently_no_ops(self):
        # Reproduces the real failure found on hardware: chown to a
        # nonexistent group prints an error but the CLI still reports the
        # line as "executed" with rc 0 — have must be re-verified.
        # converge() batches mkdir+chown into one call (mode wasn't
        # requested, so no chmod); the second queued item represents that
        # single batched call's two responses.
        self._queue(
            ["stat: cannot statx '/x': No such file or directory"],
            ["", "chown: invalid group: 'x:bogus'"],  # mkdir ok, chown failed
            ["root nogroup 4096"],  # post-check: neither owner nor group took
        )
        result = self._run({"dest": "/x", "owner": "vyos", "group": "bogus"}, expect_fail=True)
        self.assertIn("post-check", result["msg"])

    # ---- check_mode --------------------------------------------------------

    def test_check_mode_reports_diff_without_converging(self):
        self._queue(["600 vyos vyattacfg 10"])
        set_module_args({"dest": "/x", "mode": "0640", "_ansible_check_mode": True})
        with self.assertRaises(AnsibleExitJson) as ctx:
            vyos_file.main()
        result = ctx.exception.args[0]
        self.assertTrue(result["changed"])
        self.assertEqual(result["diff_fields"], ["mode"])
        # only the initial stat call should have happened — no chmod
        self.assertEqual(self.run_commands.call_count, 1)

    # ---- secrets discipline ------------------------------------------------

    def test_content_not_echoed_in_result(self):
        real_hash = "03767fbe485736bb40cc5d85e4c9bb10b12a415674b46faf005aa22188a39a10"
        self._queue(
            ["stat: cannot statx '/x': No such file or directory"],
            [""],  # single batched command: base64 write only (no owner/mode given)
            ["600 root root 4"],  # post-check stat
            ["{0}  /x".format(real_hash)],  # post-check sha256sum
        )
        result = self._run({"dest": "/x", "content": "super-secret-value"})
        self.assertNotIn("super-secret-value", json.dumps(result))
