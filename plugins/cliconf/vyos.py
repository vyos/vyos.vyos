# (c) 2017 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
author: Ansible Networking Team (@ansible-network)
name: vyos
short_description: Use vyos cliconf to run command on VyOS platform
description:
- This vyos plugin provides low level abstraction apis for sending and receiving CLI
  commands from VyOS network devices.
version_added: 1.0.0
options:
  config_commands:
    description:
    - Specifies a list of commands that can make configuration changes
      to the target device.
    - When `ansible_network_single_user_mode` is enabled, if a command sent
      to the device is present in this list, the existing cache is invalidated.
    version_added: 2.0.0
    type: list
    elements: str
    default: []
    vars:
    - name: ansible_vyos_config_commands
"""

import json
import re

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Mapping
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.config import (
    NetworkConfig,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
from ansible_collections.ansible.netcommon.plugins.plugin_utils.cliconf_base import CliconfBase


class Cliconf(CliconfBase):
    __rpc__ = CliconfBase.__rpc__ + [
        "commit",
        "discard_changes",
        "get_diff",
        "run_commands",
    ]

    def __init__(self, *args, **kwargs):
        super(Cliconf, self).__init__(*args, **kwargs)
        self._device_info = {}

    def get_device_info(self):
        if not self._device_info:
            device_info = {}

            device_info["network_os"] = "vyos"
            reply = self.get("show version")
            data = to_text(reply, errors="surrogate_or_strict").strip()

            match = re.search(r"Version:\s*(.*)", data)
            if match:
                device_info["network_os_version"] = match.group(1)

            if device_info["network_os_version"]:
                match = re.search(r"VyOS\s*(\d+\.\d+)", device_info["network_os_version"])
                if match:
                    device_info["network_os_major_version"] = match.group(1)

            match = re.search(r"(?:HW|Hardware) model:\s*(\S+)", data)
            if match:
                device_info["network_os_model"] = match.group(1)

            reply = self.get("show host name")
            device_info["network_os_hostname"] = to_text(
                reply,
                errors="surrogate_or_strict",
            ).strip()

            self._device_info = device_info

        return self._device_info

    def get_config(self, flags=None, format=None):
        if format:
            option_values = self.get_option_values()
            if format not in option_values["format"]:
                raise ValueError(
                    "'format' value %s is invalid. Valid values of format are %s"
                    % (format, ", ".join(option_values["format"])),
                )

        if not flags:
            flags = []

        if format == "text":
            command = "show configuration"
        else:
            command = "show configuration commands"

        command += " ".join(to_list(flags))
        command = command.strip()

        out = self.send_command(command)
        return out

    def edit_config(
        self,
        candidate=None,
        commit=True,
        replace=None,
        diff=False,
        comment=None,
        confirm=None,
    ):
        resp = {}
        operations = self.get_device_operations()
        self.check_edit_config_capability(operations, candidate, commit, replace, comment)

        results = []
        requests = []
        self.send_command("configure")
        for cmd in to_list(candidate):
            if not isinstance(cmd, Mapping):
                cmd = {"command": cmd}

            results.append(self.send_command(**cmd))
            requests.append(cmd["command"])
        out = self.get("compare")
        out = to_text(out, errors="surrogate_or_strict")
        diff_config = out if not out.startswith("No changes") else None

        if diff_config:
            if commit:
                try:
                    self.commit(comment, confirm)
                except AnsibleConnectionFailure as e:
                    msg = "commit failed: %s" % e.message
                    self.discard_changes()
                    raise AnsibleConnectionFailure(msg)
                else:
                    self.send_command("exit")
            else:
                self.discard_changes()
        else:
            self.send_command("exit")
            if (
                to_text(self._connection.get_prompt(), errors="surrogate_or_strict")
                .strip()
                .endswith("#")
            ):
                self.discard_changes()

        if diff_config:
            resp["diff"] = diff_config
        resp["response"] = results
        resp["request"] = requests
        return resp

    def get(
        self,
        command=None,
        prompt=None,
        answer=None,
        sendonly=False,
        newline=True,
        output=None,
        check_all=False,
    ):
        if not command:
            raise ValueError("must provide value of command to execute")
        if output:
            raise ValueError("'output' value %s is not supported for get" % output)

        return self.send_command(
            command=command,
            prompt=prompt,
            answer=answer,
            sendonly=sendonly,
            newline=newline,
            check_all=check_all,
        )

    def commit(self, comment=None, confirm=None):
        if confirm:
            if comment:
                command = 'commit-confirm {0} comment "{1}"'.format(confirm, comment)
            else:
                command = "commit-confirm {0}".format(confirm)
            self.send_command(command, "Proceed?", "\n")
        else:
            if comment:
                command = 'commit comment "{0}"'.format(comment)
            else:
                command = "commit"
            self.send_command(command)

    def discard_changes(self):
        self.send_command("exit discard")

    def get_diff(
        self,
        candidate=None,
        running=None,
        diff_match="line",
        diff_ignore_lines=None,
        path=None,
        diff_replace=False,
    ):
        diff = {}
        device_operations = self.get_device_operations()
        option_values = self.get_option_values()

        if candidate is None and device_operations["supports_generate_diff"]:
            raise ValueError("candidate configuration is required to generate diff")

        if diff_match not in option_values["diff_match"]:
            raise ValueError(
                "'match' value %s in invalid, valid values are %s"
                % (diff_match, ", ".join(option_values["diff_match"])),
            )

        if diff_ignore_lines:
            raise ValueError("'diff_ignore_lines' in diff is not supported")

        if path:
            raise ValueError("'path' in diff is not supported")

        if diff_replace and diff_match == "none":
            # Module documentation states replace only works when match is
            # 'line'. Without this check, diff_replace silently has no
            # effect under match='none' (that branch returns before the
            # diff_replace logic below ever runs) -- failing loudly here
            # is safer than letting a user believe replace ran.
            raise ValueError("'replace' is not supported when 'match' is set to 'none'")

        set_format = candidate.startswith("set") or candidate.startswith("delete")
        candidate_obj = NetworkConfig(indent=4, contents=candidate)

        if not set_format:

            config = [c.line for c in candidate_obj.items]
            commands = list()
            # this filters out less specific lines
            for item in config:
                for index, entry in enumerate(commands):
                    if item.startswith(entry):
                        del commands[index]
                        break
                commands.append(item)

            candidate_commands = ["set %s" % cmd.replace(" {", "") for cmd in commands]

        else:

            candidate_commands = str(candidate).strip().split("\n")

        if diff_match == "none":
            diff["config_diff"] = list(candidate_commands)
            return diff

        if diff_replace:
            # `running` is hierarchical/brace text in replace mode (see the
            # tree-aware block below). It must be flattened to full-path
            # "set" commands the same way candidate is above -- naively
            # splitting on newlines here would compare raw brace-syntax
            # fragments (e.g. "    host-name router") against candidate's
            # flat commands and never match, making every candidate line
            # look incorrectly "missing".
            running_obj = NetworkConfig(indent=4, contents=running)
            running_lines = [c.line for c in running_obj.items]
            running_flat = list()
            for item in running_lines:
                for index, entry in enumerate(running_flat):
                    if item.startswith(entry):
                        del running_flat[index]
                        break
                running_flat.append(item)
            running_commands = ["set %s" % cmd.replace(" {", "") for cmd in running_flat]
        else:
            running_commands = [str(c).replace("'", "") for c in running.splitlines()]

        updates = list()
        visited = set()

        for line in candidate_commands:
            item = str(line).replace("'", "")

            if not item.startswith("set") and not item.startswith("delete"):
                raise ValueError("line must start with either `set` or `delete`")

            elif item.startswith("set"):
                if diff_replace:
                    # Quote-insensitive comparison is only needed for replace
                    # mode, where `running` values may be re-quoted before
                    # being compared here. Gating this behind diff_replace
                    # preserves the original exact-match idempotency check
                    # for all existing (non-replace) callers.
                    match = any(match_cmd(item, rline) for rline in running_commands)
                else:
                    match = item in running_commands
                if not match:
                    updates.append(line)

            elif item.startswith("delete"):

                if not running_commands:
                    updates.append(line)
                else:
                    item = re.sub(r"delete", "set", item)

                    for entry in running_commands:
                        if re.match(rf"^{re.escape(item)}\b", entry) and line not in visited:
                            updates.append(line)
                            visited.add(line)

        if diff_replace:
            # T6837: replace mode must operate on the config's actual tree
            # structure, not flat line text. `running` is required to be in
            # hierarchical/brace form here (get_config(..., format="text")),
            # so that intermediate nodes (e.g. a firewall rule) are visible
            # as distinct entities from their leaf values. Diffing on flat
            # "set" lines alone cannot tell "a whole node was removed" apart
            # from "a leaf's value changed", which is what caused both the
            # orphaned-node bug and the redundant-delete-on-value-change bug.
            if running.lstrip().startswith(("set ", "delete ")):
                raise ValueError(
                    "diff_replace requires 'running' in hierarchical config "
                    "format, not flat set/delete commands",
                )

            candidate_bodies = [
                _strip_cmd_prefix(c) for c in candidate_commands if c.startswith("set ")
            ]
            running_tree = NetworkConfig(indent=4, contents=running)

            replace_deletes = list()
            visited_nodes = set()

            for item in running_tree.items:
                prefix = _node_prefix(item)

                if item.children:
                    # intermediate node: does an equivalent structural path
                    # exist anywhere in candidate? If not, the whole subtree
                    # is missing -- emit a single delete for the node itself
                    # rather than descending into per-leaf deletes.
                    if not _candidate_has_prefix(prefix, candidate_bodies):
                        if not any(
                            prefix == v or prefix.startswith(v + " ") for v in visited_nodes
                        ):
                            replace_deletes.append("delete %s" % prefix)
                            visited_nodes.add(prefix)
                    continue

                # leaf node
                if any(match_cmd(body, prefix) for body in candidate_bodies):
                    continue  # exact match, nothing to do

                parent_prefix = " ".join(p.replace(" {", "") for p in item.parents)
                if any(
                    parent_prefix == v or parent_prefix.startswith(v + " ") for v in visited_nodes
                ):
                    continue  # already covered by an ancestor delete above

                # Leaf is either genuinely absent from candidate, or its
                # value changed. Delete it unconditionally -- there is no
                # reliable way to tell a coincidentally-single-valued
                # list-style attribute (e.g. a single 'name-server' entry)
                # apart from a genuinely scalar one (e.g. 'host-name') from
                # config text alone; treating them differently by observed
                # cardinality can leave stale values behind for list-style
                # attributes (see T6837 review discussion). This is made
                # safe by ordering: replace_deletes are placed before the
                # candidate-driven `set` commands below, so each delete
                # always targets the value that is still genuinely active,
                # never one a `set` has already superseded.
                replace_deletes.append("delete %s" % prefix)

        diff["config_diff"] = replace_deletes + list(updates) if diff_replace else list(updates)
        return diff

    def run_commands(self, commands=None, check_rc=True):
        if commands is None:
            raise ValueError("'commands' value is required")

        responses = list()
        for cmd in to_list(commands):
            if not isinstance(cmd, Mapping):
                cmd = {"command": cmd}

            output = cmd.pop("output", None)
            if output:
                raise ValueError("'output' value %s is not supported for run_commands" % output)

            try:
                out = self.send_command(**cmd)
            except AnsibleConnectionFailure as e:
                if check_rc:
                    raise
                out = getattr(e, "err", e)

            responses.append(out)

        return responses

    def get_device_operations(self):
        return {
            "supports_diff_replace": True,
            "supports_commit": True,
            "supports_rollback": False,
            "supports_defaults": False,
            "supports_onbox_diff": True,
            "supports_commit_comment": True,
            "supports_multiline_delimiter": False,
            "supports_diff_match": True,
            "supports_diff_ignore_lines": False,
            "supports_generate_diff": False,
            "supports_replace": True,
        }

    def get_option_values(self):
        return {
            "format": ["text", "set"],
            "diff_match": ["line", "none"],
            "diff_replace": [True, False],
            "output": [],
        }

    def get_capabilities(self):
        result = super(Cliconf, self).get_capabilities()
        result["device_operations"] = self.get_device_operations()
        result.update(self.get_option_values())
        return json.dumps(result)

    def set_cli_prompt_context(self):
        """
        Make sure we are in the operational cli mode
        :return: None
        """
        if self._connection.connected:
            self._update_cli_prompt_context(config_context="#", exit_command="exit discard")


def match_cmd(cmd1, cmd2):
    cmd1 = re.sub("['\"]", "", cmd1)
    cmd2 = re.sub("['\"]", "", cmd2)
    if cmd1 == cmd2:
        return True
    else:
        return False


def _strip_cmd_prefix(cmd):
    """Remove a leading 'set '/'delete ' keyword, leaving the bare config path."""
    if cmd.startswith("set "):
        return cmd[4:]
    if cmd.startswith("delete "):
        return cmd[7:]
    return cmd


def _node_prefix(item):
    """Full structural path for a config tree node: parents + own text,
    brace markers stripped, space-joined. Unambiguous for intermediate
    (non-leaf) nodes, since their .text is a pure identifier, never a
    key+value pair -- only leaf text mixes a keyword with a value."""
    parts = [p.replace(" {", "").strip() for p in item.parents]
    parts.append(item.text.replace(" {", "").strip())
    return " ".join(p for p in parts if p)


def _candidate_has_prefix(prefix, candidate_bodies):
    return any(body == prefix or body.startswith(prefix + " ") for body in candidate_bodies)
