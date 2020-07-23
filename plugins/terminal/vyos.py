#
# (c) 2016 Red Hat Inc.
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

import os
import re

from ansible.plugins.terminal import TerminalBase
from ansible.errors import AnsibleConnectionFailure


class TerminalModule(TerminalBase):

    terminal_stdout_re = [
        re.compile(br"[\r\n]?[\w+\-\.:\/\[\]]+(?:\([^\)]+\)){,3}(?:>|#) ?$"),
        re.compile(br"\@[\w\-\.]+:\S+?[>#\$] ?$"),
    ]

    terminal_stderr_re = [
        re.compile(br"\n\s*Invalid command:"),
        re.compile(br"\nCommit failed"),
        re.compile(br"\n\s+Set failed"),
    ]

    ansi_re = [
        re.compile(br"\x1b\[\?1h\x1b="),  # CSI ? 1 h ESC =
        re.compile(br"\x08."),  # [Backspace] .
        re.compile(br"\x1b\[m"),  # ANSI reset code
    ]

    try:
        terminal_length = os.getenv("ANSIBLE_VYOS_TERMINAL_LENGTH", 10000)
        terminal_length = int(terminal_length)
    except ValueError:
        raise AnsibleConnectionFailure(
            "Invalid value set for vyos terminal length '%s', value should be a valid integer string"
            % terminal_length
        )

    def on_open_shell(self):
        try:
            for cmd in (b"set terminal length 0", b"set terminal width 512"):
                self._exec_cli_command(cmd)
            self._exec_cli_command(
                b"set terminal length %d" % self.terminal_length
            )
        except AnsibleConnectionFailure:
            raise AnsibleConnectionFailure("unable to set terminal parameters")
