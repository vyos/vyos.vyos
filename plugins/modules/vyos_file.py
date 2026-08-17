#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2026, VyOS maintainers and contributors
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: vyos_file
short_description: Manage files, directories, and their ownership on VyOS devices
description:
  - Creates, updates, or removes a file or directory on a VyOS device, optionally
    pushing content from a local file (I(src)) or inline text (I(content)), and
    setting owner/group/mode via sudo chown/chmod.
  - This module does not touch the configuration tree (config.boot). It manages
    arbitrary filesystem paths such as certificates or auth files under
    /config/auth/, which are not tracked by commit/save/rollback.
  - All logic runs inside this module's main(), using the standard
    get_connection()/run_commands() pattern shared with vyos_command — there is
    no dedicated action plugin; this module uses the shared generic vyos action
    plugin like every other module in the collection.
version_added: "6.0.0"
author:
  - VyOS maintainers and contributors (@vyos)
options:
  dest:
    description: Absolute path to the remote file or directory to manage.
    type: path
    required: true
  state:
    description: Whether the path should exist (present) or be removed (absent).
    type: str
    choices: [present, absent]
    default: present
  src:
    description:
      - Path to a local file (on the Ansible controller) whose content should be
        pushed to I(dest). Transferred via a real SCP session over the
        connection's own persistent socket (the same mechanism
        M(ansible.netcommon.net_put) uses), never placed inside a command
        string. Mutually exclusive with I(content).
      - File bytes are uploaded exactly as they exist on disk — Ansible does
        not render Jinja expressions inside the file's contents for I(src),
        only in the option values of the task itself (e.g. a templated path
        string). To push templated text, render it first with the C(template)
        lookup and pass the result via I(content) instead.
    type: path
  content:
    description:
      - Inline text content to write to I(dest). Marked no_log, since this module
        is commonly used to push credential material. Mutually exclusive with
        I(src).
      - Since I(content) is a normal string-type module option, Ansible renders
        any Jinja expressions in it (e.g. C({{ my_var }})) before this module
        ever runs, the same as any other option value — no special templating
        support is implemented by this module itself.
    type: str
  owner:
    description: Name of the user that should own I(dest).
    type: str
  group:
    description: Name of the group that should own I(dest).
    type: str
  mode:
    description:
      - Permission bits for I(dest), as a string (e.g. '0600'). Compared against
        stat output after normalizing to 4 digits; '600' and '0600' are treated
        as equivalent.
    type: str
  become:
    description: Whether to prefix remote commands with sudo.
    type: bool
    default: true
notes:
  - This module works with connection C(ansible.netcommon.network_cli).
  - File state managed by this module is independent of VyOS's config revision
    system. A rollback to a previous config revision will not revert changes
    made by this module.
  - Paths under I(/config/auth) are deliberately setgid C(vyattacfg) by VyOS's
    own config-management convention (see vyos.dev T2713). If I(mode) is given
    with a leading digit of C(0) (e.g. C('0750')), this module compares only
    the rwx bits and will not report a diff for VyOS's own setgid bit. To
    manage the setgid/setuid/sticky bit explicitly, pass a non-zero leading
    digit (e.g. C('2750')).
"""

EXAMPLES = """
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

- name: push templated LDAP auth config (content is rendered by Ansible before this module runs)
  vyos.vyos.vyos_file:
    dest: /config/auth/office-vpn/ldap-auth.config
    content: "{{ lookup('template', 'ldap_auth.config.j2') }}"
    owner: openvpn
    group: openvpn
    mode: '0640'
"""

RETURN = """
diff_fields:
  description: Fields that differed between requested and actual state and were converged.
  returned: always
  type: list
  elements: str
  sample: ["owner", "mode", "content"]
"""

import hashlib
import os
import re
import shlex
import tempfile

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos import (
    get_connection,
    run_commands,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos_file import (
    build_want,
    diff_want_have,
    parse_stat,
)


ARGUMENT_SPEC = dict(
    dest=dict(type="path", required=True),
    state=dict(type="str", choices=["present", "absent"], default="present"),
    src=dict(type="path"),
    content=dict(type="str", no_log=True),
    owner=dict(type="str"),
    group=dict(type="str"),
    mode=dict(type="str"),
    become=dict(type="bool", default=True),
)


def get_have(module, become, dest, need_content_hash=False):
    quoted_dest = shlex.quote(dest)
    # check_rc=False is required here: a missing path is a normal, expected
    # outcome on first-run creation, not a failure. With the default
    # check_rc=True, run_commands() would call module.fail_json() on every
    # "file doesn't exist yet" case, which is exactly the case we need to
    # handle gracefully to build `have`.
    responses = run_commands(
        module,
        ["{0}stat --format='%a %U %G %s' {1}".format(become, quoted_dest)],
        check_rc=False,
    )
    out = responses[0] if responses else ""

    if not out:
        return None
    if "No such file" in out:
        return None

    have = parse_stat(out)
    if have is None:
        # Anything that isn't the specific "doesn't exist" message and
        # doesn't parse as valid stat output is a real problem — permission
        # denied, I/O error, unexpected format, etc. Fail loudly rather than
        # silently treating it as "create it", which could otherwise lead
        # this module to attempt mkdir/chown/chmod against a path it
        # actually has no real visibility into.
        module.fail_json(
            msg="vyos_file: unexpected stat output for {0}: {1}".format(dest, out.strip()),
        )

    if need_content_hash:
        # Only hash when content comparison actually matters (src/content
        # given) — no need to pay this cost for plain directory/ownership
        # management. Without this, `have["content_hash"]` would always be
        # None, so `content` would show as "different" forever, even right
        # after a successful write.
        hash_responses = run_commands(
            module,
            ["{0}sha256sum {1}".format(become, quoted_dest)],
            check_rc=False,
        )
        hash_out = hash_responses[0] if hash_responses else ""
        # sha256sum output format: "<hex digest>  <path>"
        parts = hash_out.strip().split()
        if parts and len(parts[0]) == 64 and all(c in "0123456789abcdef" for c in parts[0].lower()):
            have["content_hash"] = parts[0]
        # else: leave content_hash unset — a malformed/errored sha256sum
        # (e.g. the file vanished in a race between stat and sha256sum)
        # should surface as a real diff on the next comparison, not get
        # silently recorded as a bogus "hash".

    return have


_OCTAL_DIGIT_TO_SYMBOLIC = {
    "0": "",
    "1": "x",
    "2": "w",
    "3": "wx",
    "4": "r",
    "5": "rx",
    "6": "rw",
    "7": "rwx",
}


def _rwx_digits_to_symbolic_mode(mode4):
    """Convert the last 3 digits of a normalized 4-digit mode string into a
    symbolic chmod argument (e.g. "0750" -> "u=rwx,g=rx,o="). Symbolic mode
    assignment for u/g/o only touches those classes — unlike any numeric
    chmod form, it leaves existing setuid/setgid/sticky bits untouched
    unless explicitly referenced (u+s, g+s, +t), which is exactly the
    "special bits are unmanaged for implicit mode requests" guarantee this
    module's docs and diff logic already promise but a plain numeric chmod
    would silently violate.
    """
    u, g, o = mode4[-3], mode4[-2], mode4[-1]
    return "u={0},g={1},o={2}".format(
        _OCTAL_DIGIT_TO_SYMBOLIC[u],
        _OCTAL_DIGIT_TO_SYMBOLIC[g],
        _OCTAL_DIGIT_TO_SYMBOLIC[o],
    )


def _build_chmod_command(become, mode4, quoted_dest):
    if mode4[0] == "0":
        # Implicit special bits (caller didn't ask for them): use symbolic
        # mode so existing setuid/setgid/sticky bits survive. A numeric
        # chmod here — even a bare 3-digit form — always explicitly sets
        # the special-bits digit to 0, silently clearing e.g. VyOS's own
        # setgid convention on /config/auth (vyos.dev T2713) the moment any
        # rwx change is needed, rather than genuinely leaving it unmanaged.
        symbolic = _rwx_digits_to_symbolic_mode(mode4)
        return "{0}chmod {1} {2}".format(become, shlex.quote(symbolic), quoted_dest)
    # Explicit non-zero leading digit: caller wants exact control over
    # special bits too, so a plain numeric chmod is correct here.
    return "{0}chmod {1} {2}".format(become, shlex.quote(mode4), quoted_dest)


def local_content_hash(params):
    if params.get("src"):
        h = hashlib.sha256()
        with open(params["src"], "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    if params.get("content") is not None:
        return hashlib.sha256(params["content"].encode()).hexdigest()
    return None


def read_local_bytes(params):
    if params.get("src"):
        with open(params["src"], "rb") as f:
            return f.read()
    if params.get("content") is not None:
        return params["content"].encode()
    return None


def push_content_via_scp(module, connection, dest, params):
    # Real SCP transfer over the connection's own persistent SSH session —
    # content/src bytes never appear inside a command string sent through
    # run_commands(). The earlier base64-in-a-shell-command approach was
    # only ever encoded, not encrypted, and remained fully readable to
    # anything logging connection traffic (e.g. persistent connection
    # logging), regardless of no_log on the task — a real problem given
    # this module's actual purpose (VPN certs, LDAP credentials).
    #
    # net_put's own action plugin uses this exact mechanism — connection
    # here is get_connection(module), the same Connection(module._socket_path)
    # JSON-RPC proxy net_put builds via Connection(socket_path) — so this is
    # not action-plugin-only, despite that being true historically for some
    # other network_cli file-transfer patterns.
    cleanup_local = False
    if params.get("src"):
        local_path = params["src"]
    else:
        data = read_local_bytes(params)
        fd, local_path = tempfile.mkstemp(prefix="vyos_file_")
        cleanup_local = True
        try:
            with os.fdopen(fd, "wb") as f:
                f.write(data)
        except Exception:
            os.remove(local_path)
            raise

    try:
        timeout = connection.get_option("persistent_command_timeout")
        connection.copy_file(
            source=local_path,
            destination=dest,
            proto="scp",
            timeout=timeout,
        )
    finally:
        if cleanup_local:
            os.remove(local_path)


def converge(module, become, dest, want, diff, params):
    cmds = []
    quoted_dest = shlex.quote(dest)

    if want["state"] == "absent":
        cmds.append("{0}rm -rf {1}".format(become, quoted_dest))
        run_commands(module, cmds)
        post_have = get_have(module, become, dest)
        if post_have is not None:
            module.fail_json(
                msg="vyos_file: removal of {0} did not take effect".format(dest),
            )
        return

    if "content" in diff:
        connection = get_connection(module)
        push_content_via_scp(module, connection, dest, params)
    elif "state" in diff and have_is_missing(diff):
        cmds.append("{0}mkdir -p {1}".format(become, quoted_dest))

    if "owner" in diff and "group" in diff:
        cmds.append(
            "{0}chown {1}:{2} {3}".format(
                become,
                shlex.quote(want["owner"]),
                shlex.quote(want["group"]),
                quoted_dest,
            ),
        )
    elif "owner" in diff:
        cmds.append(
            "{0}chown {1} {2}".format(become, shlex.quote(want["owner"]), quoted_dest),
        )
    elif "group" in diff:
        cmds.append(
            "{0}chgrp {1} {2}".format(become, shlex.quote(want["group"]), quoted_dest),
        )

    if "mode" in diff:
        cmds.append(_build_chmod_command(become, want["mode"], quoted_dest))

    if cmds:
        run_commands(module, cmds)

    # run_commands() only confirms the CLI accepted each command line
    # syntactically — it does NOT confirm the underlying binary succeeded.
    # A chown against a nonexistent group, for example, prints an error to
    # stdout but the CLI wrapper still reports the line as "executed"; we
    # would otherwise report changed=true for a write that silently did
    # nothing. Re-stat and compare against `want` to catch this class of
    # failure before returning success.
    post_have = get_have(
        module,
        become,
        dest,
        need_content_hash=want.get("content_hash") is not None,
    )
    post_diff = diff_want_have(want, post_have)
    if post_diff:
        module.fail_json(
            msg=(
                "vyos_file converged but post-check found remaining "
                "differences — one or more commands likely failed silently "
                "at the OS level (e.g. chown to a nonexistent user/group): "
                "{0}".format(post_diff)
            ),
        )


def have_is_missing(diff):
    return diff.get("state") == (None, "present")


def validate_dest(module, dest):
    # dest is type=path in ARGUMENT_SPEC, which expands ~ and env vars but
    # does NOT enforce absoluteness — a relative value would resolve against
    # whatever the underlying shell's cwd happens to be, an unintended and
    # unpredictable target. And since this module issues raw `rm -rf`,
    # `chmod`, `chown` against dest with no config-tree safety net, a
    # dest of "/" (or anything that normalizes to it) combined with
    # state=absent would attempt to recursively remove the entire
    # filesystem. Both must be rejected before any stat/converge runs.
    if not os.path.isabs(dest):
        module.fail_json(
            msg="vyos_file: dest must be an absolute path, got {0!r}".format(dest),
        )
    normalized = os.path.normpath(dest)
    # normalized == "/" alone is insufficient: os.path.normpath preserves
    # "//" as-is (a POSIX quirk permitting implementation-defined behavior
    # for exactly two leading slashes), so dest="//" would otherwise bypass
    # this check entirely. Stripping all slashes catches "/", "//", "///",
    # etc. uniformly.
    if normalized.strip("/") == "":
        module.fail_json(
            msg=(
                "vyos_file: refusing to manage the root filesystem path "
                "(dest normalized to {0!r}): {1!r}".format(normalized, dest)
            ),
        )


_MODE_RE = re.compile(r"^[0-7]{3,4}$")


def validate_mode(module, mode):
    # _normalize_mode() (module_utils) does str(mode).zfill(4)[-4:], which
    # for genuinely invalid input silently mangles it into something that
    # LOOKS valid rather than rejecting it — e.g. "10640" (5 digits, an
    # obvious typo for a 4-digit mode) becomes "0640" by truncation, and
    # the module would silently apply permissions the caller never actually
    # asked for. Validate strictly here, before that normalization ever
    # runs, so malformed input fails loudly instead of being reinterpreted.
    if mode is None:
        return
    if not _MODE_RE.match(mode):
        module.fail_json(
            msg=(
                "vyos_file: mode must be an octal string of 3 or 4 digits "
                "(0-7 only), got {0!r}".format(mode)
            ),
        )


def validate_src(module, src):
    # local_content_hash()/read_local_bytes() do plain open(src, "rb")
    # calls with no existence/type/permission check. A missing file, a
    # directory passed where a file is expected, or an unreadable path
    # would otherwise surface as an unhandled Python traceback instead of
    # a clean module error — and this happens even under check_mode, since
    # content-hashing runs before the check-mode short-circuit.
    if src is None:
        return
    if not os.path.exists(src):
        module.fail_json(msg="vyos_file: src not found: {0!r}".format(src))
    if os.path.isdir(src):
        module.fail_json(
            msg="vyos_file: src is a directory, expected a file: {0!r}".format(src),
        )
    if not os.access(src, os.R_OK):
        module.fail_json(msg="vyos_file: src is not readable: {0!r}".format(src))


def main():
    module = AnsibleModule(
        argument_spec=ARGUMENT_SPEC,
        mutually_exclusive=[["src", "content"]],
        supports_check_mode=True,
    )

    dest = module.params["dest"]
    validate_dest(module, dest)
    validate_mode(module, module.params.get("mode"))
    validate_src(module, module.params.get("src"))

    become = "sudo " if module.params.get("become", True) else ""

    want = build_want(module.params, local_content_hash(module.params))
    have = get_have(
        module,
        become,
        dest,
        need_content_hash=want.get("content_hash") is not None,
    )
    diff = diff_want_have(want, have)

    result = {"changed": bool(diff), "diff_fields": list(diff.keys())}

    if module.check_mode or not diff:
        module.exit_json(**result)

    converge(module, become, dest, want, diff, module.params)
    module.exit_json(**result)


if __name__ == "__main__":
    main()
