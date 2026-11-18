# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The VyOS interfaces fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type
import platform
import re

from ansible.module_utils.common.text.converters import to_text
from ansible.module_utils.connection import ConnectionError

from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.vyos import (
    get_capabilities,
    get_connection,
    run_commands,
)


class LegacyFactsBase(object):
    COMMANDS = frozenset()

    def __init__(self, module):
        self.module = module
        self.facts = dict()
        self.warnings = list()
        self.responses = None

    def populate(self):
        self.responses = run_commands(self.module, list(self.COMMANDS))


class Default(LegacyFactsBase):
    COMMANDS = [
        "show version",
    ]

    def populate(self):
        super(Default, self).populate()
        data = self.responses[0]
        self.facts["serialnum"] = self.parse_serialnum(data)
        self.facts.update(self.platform_facts())
        secure_boot = self.secure_boot_facts()
        if secure_boot:
            self.facts["secure_boot"] = secure_boot

    def secure_boot_facts(self):
        """Secure Boot state, on images that have show secure-boot.

        Older images reject the command; the fact is then left out.
        """
        data = self.run_optional("show secure-boot")
        if data is None:
            return None
        match = re.search(r"^SecureBoot\s+(enabled|disabled)\s*$", data, re.M)
        if not match:
            return None
        facts = {
            "enabled": match.group(1) == "enabled",
            "uefi": "legacy BIOS mode" not in data,
        }
        if facts["enabled"]:
            detail = self.run_optional("show secure-boot detail") or ""
            facts["certificates"] = [
                {"issuer": issuer, "subject": subject}
                for issuer, subject in re.findall(
                    r"^Issuer:\s+(.+?)\s*\nSubject:\s+(.+?)\s*$",
                    detail,
                    re.M,
                )
            ]
        return facts

    def run_optional(self, command):
        """Output of a command the image may not have, or None when the device rejects it.

        Only "Invalid command" means the image lacks the command; other connection errors
        (timeouts, disconnects) fail the module as in run_commands.
        """
        try:
            return get_connection(self.module).run_commands(commands=[command])[0]
        except ConnectionError as exc:
            msg = to_text(exc, errors="surrogate_then_replace")
            if "Invalid command" in msg:
                return None
            self.module.fail_json(msg=msg)

    def parse_serialnum(self, data):
        match = re.search(r"(?:HW|Hardware) S/N:\s+(\S+)", data)
        if match:
            return match.group(1)

    def platform_facts(self):
        platform_facts = {}

        resp = get_capabilities(self.module)
        device_info = resp["device_info"]

        platform_facts["system"] = device_info["network_os"]

        for item in ("model", "image", "version", "platform", "hostname"):
            val = device_info.get("network_os_%s" % item)
            if val:
                platform_facts[item] = val

        platform_facts["api"] = resp["network_api"]
        platform_facts["python_version"] = platform.python_version()

        return platform_facts


class Config(LegacyFactsBase):
    COMMANDS = [
        "show configuration commands",
        "show system commit",
    ]

    def populate(self):
        super(Config, self).populate()

        self.facts["config"] = self.responses

        commits = self.responses[1]
        entries = list()
        entry = None

        for line in commits.split("\n"):
            match = re.match(r"(\d+)\s+(.+)by(.+)via(.+)", line)
            if match:
                if entry:
                    entries.append(entry)

                entry = dict(
                    revision=match.group(1),
                    datetime=match.group(2),
                    by=str(match.group(3)).strip(),
                    via=str(match.group(4)).strip(),
                    comment=None,
                )
            else:
                entry["comment"] = line.strip()

        self.facts["commits"] = entries


class Neighbors(LegacyFactsBase):
    COMMANDS = [
        "show lldp neighbors",
        "show lldp neighbors detail",
    ]

    def populate(self):
        super(Neighbors, self).populate()

        all_neighbors = self.responses[0]
        if "LLDP not configured" not in all_neighbors:
            neighbors = self.parse(self.responses[1])
            self.facts["neighbors"] = self.parse_neighbors(neighbors)

    def parse(self, data):
        parsed = list()
        values = None
        for line in data.split("\n"):
            if not line:
                continue
            if line[0] == " ":
                values += "\n%s" % line
            elif line.startswith("Interface"):
                if values:
                    parsed.append(values)
                values = line
        if values:
            parsed.append(values)
        return parsed

    def parse_neighbors(self, data):
        facts = dict()
        for item in data:
            interface = self.parse_interface(item)
            host = self.parse_host(item)
            port = self.parse_port(item)
            if interface not in facts:
                facts[interface] = list()
            facts[interface].append(dict(host=host, port=port))
        return facts

    def parse_interface(self, data):
        match = re.search(r"^Interface:\s+(\S+),", data)
        return match.group(1)

    def parse_host(self, data):
        match = re.search(r"SysName:\s+(.+)$", data, re.M)
        if match:
            return match.group(1)

    def parse_port(self, data):
        match = re.search(r"PortDescr:\s+(.+)$", data, re.M)
        if match:
            return match.group(1)
