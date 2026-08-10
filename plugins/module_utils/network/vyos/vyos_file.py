#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2026, VyOS maintainers and contributors
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import hashlib
import re


STAT_RE = re.compile(r"^(?P<mode>\d+)\s+(?P<owner>\S+)\s+(?P<group>\S+)\s+(?P<size>\d+)$")


def parse_stat(output):
    """Parse `stat --format='%a %U %G %s' <path>` output.
    Returns None if the path doesn't exist (caller checks rc/stderr first).
    """
    m = STAT_RE.match(output.strip())
    if not m:
        return None
    d = m.groupdict()
    return {
        "mode": d["mode"].zfill(4)[-4:],
        "owner": d["owner"],
        "group": d["group"],
        "size": int(d["size"]),
    }


def _normalize_mode(mode):
    if mode is None:
        return None
    return str(mode).zfill(4)[-4:]


def build_want(params, local_content_hash=None):
    return {
        "dest": params["dest"],
        "state": params.get("state", "present"),
        "owner": params.get("owner"),
        "group": params.get("group"),
        "mode": _normalize_mode(params.get("mode")),
        "content_hash": local_content_hash,
    }


def diff_want_have(want, have):
    """Returns dict of {field: (have_val, want_val)} for fields that differ.
    Identity is `dest`, not a config-tree path — this compares a stat-shaped
    dict, not config lines.
    """
    diff = {}
    if want["state"] == "absent":
        if have is not None:
            diff["state"] = (have, "absent")
        return diff

    if have is None:
        diff["state"] = (None, "present")
        for f in ("owner", "group", "mode"):
            if want.get(f) is not None:
                diff[f] = (None, want[f])
        if want.get("content_hash"):
            diff["content"] = (None, want["content_hash"])
        return diff

    for f in ("owner", "group"):
        if want.get(f) is not None and want[f] != have.get(f):
            diff[f] = (have.get(f), want[f])

    if want.get("mode") is not None:
        want_mode = want["mode"]
        have_mode = have.get("mode")
        if want_mode[0] == "0":
            # Caller didn't request specific setuid/setgid/sticky bits —
            # don't fight VyOS's own conventions (e.g. /config/auth is
            # deliberately setgid vyattacfg; see vyos.dev T2713). Compare
            # only the rwx digits unless the caller explicitly asked for a
            # non-zero leading digit.
            if want_mode[-3:] != have_mode[-3:]:
                diff["mode"] = (have_mode, want_mode)
        elif want_mode != have_mode:
            diff["mode"] = (have_mode, want_mode)

    if want.get("content_hash") and want["content_hash"] != have.get("content_hash"):
        diff["content"] = (have.get("content_hash"), want["content_hash"])

    return diff


def local_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
