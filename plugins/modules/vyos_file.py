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
version_added: "1.0.0"
author:
  - Evgeny Molotkov (@omnom62)
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
        pushed to I(dest). Read locally and pushed as base64 via a single CLI
        command, since network_cli has no SFTP/SCP channel available to this
        module. Mutually exclusive with I(content).
    type: path
  content:
    description:
      - Inline text content to write to I(dest). Marked no_log, since this module
        is commonly used to push credential material. Mutually exclusive with
        I(src).
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
"""

RETURN = """
diff_fields:
  description: Fields that differed between requested and actual state and were converged.
  returned: always
  type: list
  elements: str
  sample: ["owner", "mode", "content"]
"""

import base64
import hashlib

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos import (
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

    responses = run_commands(
        module,
        ["{0}stat --format='%a %U %G %s' {1}".format(become, dest)],
        check_rc=False,
    )
    out = responses[0] if responses else ""
    if not out or "No such file" in out or ("stat:" in out and "cannot stat" in out):
        return None
    have = parse_stat(out)

    if need_content_hash and have is not None:

        hash_responses = run_commands(
            module,
            ["{0}sha256sum {1}".format(become, dest)],
            check_rc=False,
        )
        hash_out = hash_responses[0] if hash_responses else ""
        # sha256sum output format: "<hex digest>  <path>"
        parts = hash_out.strip().split()
        if parts:
            have["content_hash"] = parts[0]

    return have


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


def converge(module, become, dest, want, diff, params):
    cmds = []

    if want["state"] == "absent":
        cmds.append("{0}rm -rf {1}".format(become, dest))
        run_commands(module, cmds)
        post_have = get_have(module, become, dest)
        if post_have is not None:
            module.fail_json(
                msg="vyos_file: removal of {0} did not take effect".format(dest),
            )
        return

    if "content" in diff:
        data = read_local_bytes(params)
        b64 = base64.b64encode(data).decode()
        cmds.append(
            '{0}sh -c "echo {1} | base64 -d > {2}"'.format(become, b64, dest),
        )
    elif "state" in diff and have_is_missing(diff):
        cmds.append("{0}mkdir -p {1}".format(become, dest))

    if "owner" in diff and "group" in diff:
        cmds.append(
            "{0}chown {1}:{2} {3}".format(become, want["owner"], want["group"], dest),
        )
    elif "owner" in diff:
        cmds.append("{0}chown {1} {2}".format(become, want["owner"], dest))
    elif "group" in diff:
        cmds.append("{0}chgrp {1} {2}".format(become, want["group"], dest))

    if "mode" in diff:
        cmds.append("{0}chmod {1} {2}".format(become, want["mode"], dest))

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


def main():
    module = AnsibleModule(
        argument_spec=ARGUMENT_SPEC,
        mutually_exclusive=[["src", "content"]],
        supports_check_mode=True,
    )

    become = "sudo " if module.params.get("become", True) else ""
    dest = module.params["dest"]

    if not dest.startswith("/") or dest == "/":
        module.fail_json(msg="vyos_file: dest must be an absolute path and must not be '/'")
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
