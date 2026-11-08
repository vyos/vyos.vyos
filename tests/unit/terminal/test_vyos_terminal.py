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

import unittest

from ansible_collections.vyos.vyos.plugins.terminal.vyos import TerminalModule


def strip(data):
    """Apply ansi_re in order, the same way network_cli._strip() does."""
    for regex in TerminalModule.ansi_re:
        data = regex.sub(b"", data)
    return data


class TestBracketedPaste(unittest.TestCase):
    """Rolling vbash runs readline with enable-bracketed-paste on."""

    def test_command_echo(self):
        raw = b"\x1b[?2004l\r\x1b[?1h\x1b=\r" b"Version:          VyOS 999.202609232109\x1b[m\r\n"
        out = strip(raw)
        self.assertNotIn(b"2004", out)
        self.assertIn(b"Version:          VyOS 999.202609232109", out)

    def test_prompt(self):
        raw = b"\x1b[?2004h\x1b]0;vyos@vyos: ~\x07vyos@vyos:~$ "
        out = strip(raw)
        self.assertEqual(out, b"vyos@vyos:~$ ")
        self.assertTrue(any(r.search(out) for r in TerminalModule.terminal_stdout_re))

    def test_empty_output(self):
        self.assertEqual(strip(b"\x1b[?2004l\r\n").strip(), b"")


class TestWrapArtefact(unittest.TestCase):
    """At each terminal-width wrap the stream carries ESC[m, space, backspace, char."""

    def test_wrap_lts(self):
        raw = b'"ti\x1b[m \x08me3.vyos.net": {}'
        self.assertEqual(strip(raw), b'"time3.vyos.net": {}')

    def test_wrap_rolling_quote(self):
        raw = b'"ssh": {}}, \x1b[m \x08"system": {'
        self.assertEqual(strip(raw), b'"ssh": {}}, "system": {')

    def test_wrap_rolling_letter(self):
        raw = b'"al\x1b[m \x08l": {"level": "info"}'
        self.assertEqual(strip(raw), b'"all": {"level": "info"}')
