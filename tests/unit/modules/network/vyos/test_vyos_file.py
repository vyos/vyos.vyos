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

import hashlib
import json
import os
import tempfile

from unittest.mock import MagicMock, patch

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

        # content/src transfer now goes through a real SCP call via
        # get_connection(module).copy_file(...) — never through
        # run_commands() — so it needs its own mock, separate from the
        # command-based stat/chown/chmod/rm path above.
        self.mock_get_connection = patch(
            "ansible_collections.vyos.vyos.plugins.modules.vyos_file.get_connection",
        )
        self.get_connection = self.mock_get_connection.start()
        self.mock_connection = MagicMock()
        self.mock_connection.get_option.return_value = 30
        self.get_connection.return_value = self.mock_connection

    def tearDown(self):
        super(TestVyosFileModule, self).tearDown()
        self.mock_run_commands.stop()
        self.mock_get_connection.stop()

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
        # "00640" (5 digits) is deliberately excluded here — it's now
        # correctly rejected by the strict [0-7]{3,4} validation (see
        # test_rejects_mode_with_extra_leading_digit), even though its
        # value is harmless. Only genuinely valid 3-4 digit forms of the
        # same value are expected to normalize equivalently.
        for requested in ("640", "0640"):
            with self.subTest(requested=requested):
                self._queue(["640 vyos vyattacfg 10"])
                result = self._run({"dest": "/config/auth/x/hello.txt", "mode": requested})
                self.assertFalse(
                    result["changed"],
                    "mode {0!r} incorrectly compared unequal to stat's '640'".format(requested),
                )

    def test_implicit_mode_uses_symbolic_chmod_preserving_special_bits(self):
        # Real bug found in review: a plain numeric chmod ALWAYS explicitly
        # sets the special-bits digit (even a bare 3-digit form implies a
        # leading 0), so it would silently clear an existing setgid/setuid
        # bit the moment any rwx change is needed — directly contradicting
        # the "special bits are unmanaged for implicit mode" guarantee this
        # module's own diff comparison already promises. Symbolic chmod
        # (u=,g=,o=) is the only form that genuinely leaves them untouched.
        self._queue(
            ["2770 vyos vyattacfg 10"],  # existing: setgid + rwxrwx---
            [""],  # the single batched chmod command
            ["2750 vyos vyattacfg 10"],  # post-check: rwx fixed, setgid survived
        )
        result = self._run({"dest": "/x", "mode": "0750"})
        self.assertTrue(result["changed"])
        self.assertEqual(result["diff_fields"], ["mode"])

        converge_call = self.run_commands.call_args_list[1]
        chmod_cmd = converge_call.args[1][0]
        self.assertIn("u=", chmod_cmd, "expected symbolic chmod for an implicit mode request")
        self.assertNotRegex(
            chmod_cmd,
            r"chmod\s+0?750\b",
            "must not use a numeric chmod for an implicit mode request — it would "
            "clear the existing setgid bit",
        )

    def test_explicit_mode_uses_numeric_chmod(self):
        # A non-zero leading digit means the caller explicitly wants control
        # over special bits too — numeric chmod is correct here, unlike the
        # implicit case above.
        self._queue(
            ["0750 vyos vyattacfg 10"],  # existing: no special bits
            [""],
            ["2750 vyos vyattacfg 10"],  # post-check: matches the explicit request
        )
        result = self._run({"dest": "/x", "mode": "2750"})
        self.assertTrue(result["changed"])

        converge_call = self.run_commands.call_args_list[1]
        chmod_cmd = converge_call.args[1][0]
        self.assertIn("2750", chmod_cmd)
        self.assertNotIn("u=", chmod_cmd, "explicit mode should use numeric chmod, not symbolic")

    # ---- content ---------------------------------------------------------

    def test_content_push_detected_and_verified(self):
        # Content transfer now stages to a /tmp path via copy_file(), then
        # relocates into `dest` via a sudo-prefixed mv (run_commands call).
        # That mv is now a separate run_commands() call inserted between
        # the initial stat and the chown+chmod batch.
        real_hash = "98ea6e4f216f2fb4b69fff9b3a44842c38686ca685f3f55dc48c5d3fb1107be4"
        self._queue(
            ["stat: cannot statx '/config/auth/x/hello.txt': No such file or directory"],
            [""],  # mv staging path -> dest
            ["", ""],  # chown, chmod — batched
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
        self.mock_connection.copy_file.assert_called_once()
        # copy_file's destination is now the /tmp staging path, NOT the
        # final dest — the mv (with become applied) does the real placement.
        staged_dest = self.mock_connection.copy_file.call_args.kwargs["destination"]
        self.assertTrue(staged_dest.startswith("/tmp/.vyos_file_staging_"))
        mv_call = self.run_commands.call_args_list[1]
        mv_cmd = mv_call.args[1][0]
        self.assertIn("mv", mv_cmd)
        self.assertIn(staged_dest, mv_cmd)
        self.assertIn("/config/auth/x/hello.txt", mv_cmd)

    def test_src_upload_reads_local_file_and_pushes_content(self):
        # src takes a different code path from content (read_local_bytes()
        # opens the local path rather than encoding an inline string), and
        # had no direct test coverage — this exercises that path explicitly
        # using a real temporary file, since local_content_hash()/
        # read_local_bytes() do plain open() calls that aren't mockable
        # through run_commands.
        with tempfile.NamedTemporaryFile(mode="w", suffix=".pem", delete=False) as f:
            f.write("-----BEGIN CERTIFICATE-----\nfakecertdata\n-----END CERTIFICATE-----\n")
            local_path = f.name
        try:
            real_hash = hashlib.sha256(
                b"-----BEGIN CERTIFICATE-----\nfakecertdata\n-----END CERTIFICATE-----\n",
            ).hexdigest()
            self._queue(
                ["stat: cannot statx '/config/auth/x/client.pem': No such file or directory"],
                [""],  # mv staging path -> dest
                ["", ""],  # chown, chmod — batched
                ["600 vyos vyattacfg 10"],
                ["{0}  /config/auth/x/client.pem".format(real_hash)],
            )
            result = self._run(
                {
                    "dest": "/config/auth/x/client.pem",
                    "src": local_path,
                    "owner": "vyos",
                    "mode": "0600",
                },
            )
            self.assertTrue(result["changed"])
            self.assertIn("content", result["diff_fields"])
            self.mock_connection.copy_file.assert_called_once()
            self.assertEqual(
                self.mock_connection.copy_file.call_args.kwargs["source"],
                local_path,
            )
        finally:
            os.unlink(local_path)

    def test_src_upload_idempotent_on_matching_remote_content(self):
        # have already matches want entirely -> diff is empty -> converge()
        # (and therefore push_content_via_scp/mv) never runs at all, so
        # this stays at 1 run_commands call, unaffected by the staging change.
        data = b"identical content\n"
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
            f.write(data)
            local_path = f.name
        try:
            real_hash = hashlib.sha256(data).hexdigest()
            self._queue(
                ["600 vyos vyattacfg 10"],
                ["{0}  /x".format(real_hash)],
            )
            result = self._run({"dest": "/x", "src": local_path, "owner": "vyos", "mode": "0600"})
            self.assertFalse(result["changed"], result.get("diff_fields"))
            self.mock_connection.copy_file.assert_not_called()
        finally:
            os.unlink(local_path)

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

    def test_real_stat_error_fails_loudly_instead_of_treated_as_missing(self):
        # Permission denied (or any other real stat failure) must NOT be
        # silently treated the same as "doesn't exist" — that could lead
        # the module to attempt mkdir/chown/chmod against a path it
        # actually has no real visibility into.
        self._queue(["stat: cannot statx '/x': Permission denied"])
        result = self._run({"dest": "/x", "mode": "0750"}, expect_fail=True)
        self.assertIn("unexpected stat output", result["msg"])

    # ---- destination path validation ---------------------------------

    def test_rejects_relative_path(self):
        # No run_commands() calls should even be attempted for an invalid
        # dest — validation must happen before any stat/converge logic.
        result = self._run({"dest": "relative/path"}, expect_fail=True)
        self.assertIn("absolute path", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_root_path(self):
        result = self._run({"dest": "/", "state": "absent"}, expect_fail=True)
        self.assertIn("root filesystem", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_double_slash_root_bypass(self):
        # os.path.normpath preserves "//" as-is (a POSIX quirk for exactly
        # two leading slashes) rather than collapsing it to "/" — a naive
        # `normalized == "/"` check would miss this and let it through.
        result = self._run({"dest": "//", "state": "absent"}, expect_fail=True)
        self.assertIn("root filesystem", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_dot_path_that_normalizes_to_root(self):
        result = self._run({"dest": "/.", "state": "absent"}, expect_fail=True)
        self.assertIn("root filesystem", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    # ---- mode validation -----------------------------------------------

    def test_rejects_mode_with_extra_leading_digit(self):
        # The exact real bug found in review: _normalize_mode()'s
        # zfill(4)[-4:] would silently truncate "10640" into "0640" rather
        # than rejecting an obviously malformed 5-digit value — applying
        # permissions the caller never actually asked for.
        result = self._run({"dest": "/x", "mode": "10640"}, expect_fail=True)
        self.assertIn("octal string", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_non_octal_digits(self):
        result = self._run({"dest": "/x", "mode": "0890"}, expect_fail=True)
        self.assertIn("octal string", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_non_numeric_mode(self):
        result = self._run({"dest": "/x", "mode": "abcd"}, expect_fail=True)
        self.assertIn("octal string", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_too_short_mode(self):
        result = self._run({"dest": "/x", "mode": "07"}, expect_fail=True)
        self.assertIn("octal string", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_accepts_valid_3_and_4_digit_modes(self):
        # Sanity check that the new strict validation doesn't reject
        # legitimate input alongside the malformed cases above.
        for valid_mode in ("750", "0750", "2750", "0000", "7777"):
            with self.subTest(valid_mode=valid_mode):
                self._queue([" ".join([valid_mode.zfill(4), "vyos", "vyattacfg", "10"])])
                result = self._run({"dest": "/x", "mode": valid_mode})
                self.assertFalse(result["changed"])

    # ---- src validation --------------------------------------------------

    def test_rejects_missing_src_file(self):
        # Without this check, open() inside local_content_hash() would
        # raise an unhandled FileNotFoundError instead of a clean module
        # error — and this happens even under check_mode, since content
        # hashing runs before the check-mode short-circuit.
        result = self._run(
            {"dest": "/x", "src": "/definitely/does/not/exist/x.pem"},
            expect_fail=True,
        )
        self.assertIn("src not found", result["msg"])
        self.assertEqual(self.run_commands.call_count, 0)

    def test_rejects_src_that_is_a_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = self._run({"dest": "/x", "src": tmpdir}, expect_fail=True)
            self.assertIn("directory", result["msg"])
            self.assertEqual(self.run_commands.call_count, 0)

    def test_malformed_sha256sum_output_does_not_get_recorded_as_a_hash(self):
        # If sha256sum itself errors (e.g. a race where the file vanished
        # between stat and sha256sum), the garbage output must not be
        # silently trusted as a real content hash — that would corrupt the
        # comparison instead of surfacing as a real, visible diff.
        # check_mode=True keeps this isolated to have/diff computation only,
        # without needing to model a full converge cycle.
        self._queue(
            ["600 vyos vyattacfg 10"],
            ["sha256sum: /x: No such file or directory"],
        )
        set_module_args({"dest": "/x", "content": "hi\n", "_ansible_check_mode": True})
        with self.assertRaises(AnsibleExitJson) as ctx:
            vyos_file.main()
        result = ctx.exception.args[0]
        # have.content_hash stays unset -> compared against a real want hash
        # -> reported as a genuine diff, not silently accepted as converged.
        self.assertIn("content", result.get("diff_fields", []))

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
            ["644 root nogroup 4096"],  # post-check: neither owner nor group took
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

    def test_content_push_via_scp_creates_and_cleans_up_temp_file_for_inline_content(self):
        # For `content` (no src), a real local temp file must be created to
        # hand to copy_file() (SCP needs a real source path — it can't
        # stream an in-memory string), and that temp file must be removed
        # again afterward regardless of outcome, since it briefly holds
        # secret material on the controller's local disk.
        captured_path = {}

        def fake_copy_file(source, destination, proto, timeout):
            captured_path["source"] = source
            # the temp file must exist at the moment copy_file is invoked
            self.assertTrue(os.path.exists(source))
            with open(source, "rb") as f:
                self.assertEqual(f.read(), b"hi\n")

        self.mock_connection.copy_file.side_effect = fake_copy_file
        self._queue(
            ["stat: cannot statx '/x': No such file or directory"],
            [""],  # mv staging path -> dest (now unconditional, even with no owner/mode)
            ["600 vyos vyattacfg 10"],
            [hashlib.sha256(b"hi\n").hexdigest() + "  /x"],
        )
        self._run({"dest": "/x", "content": "hi\n"})
        # cleaned up after the transfer completes — nothing sensitive left
        # sitting on the controller's local disk
        self.assertFalse(os.path.exists(captured_path["source"]))

    def test_content_push_via_scp_uses_src_path_directly_without_a_temp_file(self):
        # When src is given, the provided path IS the source — no temp
        # file should be created or deleted for it.
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write("real file content\n")
            local_path = f.name
        try:
            self._queue(
                ["stat: cannot statx '/x': No such file or directory"],
                [""],  # mv staging path -> dest
                ["600 vyos vyattacfg 10"],
                [hashlib.sha256(b"real file content\n").hexdigest() + "  /x"],
            )
            self._run({"dest": "/x", "src": local_path})
            self.assertEqual(
                self.mock_connection.copy_file.call_args.kwargs["source"],
                local_path,
            )
            # the caller's own file must still exist — this module must
            # never delete a user-provided src path
            self.assertTrue(os.path.exists(local_path))
        finally:
            os.unlink(local_path)

    def test_content_not_echoed_in_result(self):
        # No owner/group/mode requested here, so converge()'s cmds list
        # stays empty — but push_content_via_scp's mv is unconditional
        # regardless, so it's still 4 run_commands calls total: initial
        # stat, mv, post-check stat, post-check sha256sum.
        real_hash = "03767fbe485736bb40cc5d85e4c9bb10b12a415674b46faf005aa22188a39a10"
        self._queue(
            ["stat: cannot statx '/x': No such file or directory"],
            [""],  # mv staging path -> dest
            ["600 root root 4"],  # post-check stat
            ["{0}  /x".format(real_hash)],  # post-check sha256sum
        )
        result = self._run({"dest": "/x", "content": "super-secret-value"})
        self.assertNotIn("super-secret-value", json.dumps(result))
        # the secret must not leak into the copy_file() call args either —
        # only a real local temp-file path should appear there
        for call in self.mock_connection.copy_file.call_args_list:
            self.assertNotIn("super-secret-value", str(call))
        # nor into any run_commands() call — the mv only ever references
        # paths (staging path, dest), never file content
        for call in self.run_commands.call_args_list:
            self.assertNotIn("super-secret-value", str(call))
