#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The vyos_logging_global config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.facts.facts import (
    Facts,
)
from ansible_collections.vyos.vyos.plugins.module_utils.network.vyos.rm_templates.logging_global import (
    Logging_globalTemplate,
)


class Logging_global(ResourceModule):
    """
    The vyos_logging_global config class
    """

    def __init__(self, module):
        super(Logging_global, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="logging_global",
            tmplt=Logging_globalTemplate(),
        )
        self.parsers = [
            "console",
            "files.archive_size",
            "files.archive_file_num",
            "files_param",
            "global_params.state",
            "global_params.archive_file_num",
            "global_params.archive_size",
            "global_params.marker_interval",
            "global_params.preserve_fqdn",
            "global_params",
            # "hosts_port",
            # "hosts_params",
            # "hosts_protocol",
            "users",
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """
        if self.want:
            wantd = self.list_to_dict(self.want, "want")
        else:
            wantd = dict()
        if self.have:
            haved = self.list_to_dict(self.have, "have")
        else:
            haved = dict()

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {k: v for k, v in iteritems(haved) if k in wantd or not wantd}
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self._compare(want={}, have=have)

        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Logging_global network resource.
        """
        self.compare(parsers=self.parsers, want=want, have=have)

    def list_to_dict(self, param, op):
        _temp_param = {}
        _dict_vals = None
        primary_k = {"files": "path", "hosts": "hostname", "users": "username"}
        for element, val in iteritems(param):
            if element == "facilities":  # only with recursion call
                _tem_par = {}
                for par in val:
                    if par.get("facility") and par.get("level"):
                        _tem_par.update({par.get("facility") + par.get("level"): par})
                    elif par.get("facility") and par.get("protocol"):
                        _tem_par.update(
                            {par.get("facility") + par.get("protocol"): par}
                        )
                    else:
                        _tem_par.update({par.get("facility"): par})
                return _tem_par
            elif element == "console" or element == "global_params":
                if val.get("facilities"):
                    _dict_vals = self.list_to_dict(val, op)
                else:
                    _dict_vals = None
                _temp_param.update(self.make_linear_dicts(element, val, _dict_vals))
            elif element == "hosts" or element == "users" or element == "files":
                for v in val:
                    if v.get("facilities"):
                        # v["facilities"] = self.list_to_dict(v, op)
                        _dict_vals = self.list_to_dict(v, op)
                    else:
                        _dict_vals = None
                    _temp_param.update(self.make_linear_dicts(element, v, _dict_vals))
        return _temp_param

    def make_linear_dicts(self, element, val, _dict_vals):
        linear_dict = {}
        primary_k = {"files": "path", "hosts": "hostname", "users": "username"}
        tag = val.get(primary_k.get(element)) if primary_k.get(element) else ""
        if _dict_vals:
            for k, v in iteritems(_dict_vals):
                linear_dict.update({element + k + tag: {element: v}})
        if val.get("preserve_fqdn"):
            linear_dict.update(
                {
                    "preserve_fqdn": {
                        element: {"preserve_fqdn": val.get("preserve_fqdn")}
                    }
                }
            )
        if val.get("marker_interval"):
            linear_dict.update(
                {
                    "marker_interval": {
                        element: {"marker_interval": val.get("marker_interval")}
                    }
                }
            )
        if val.get("archive"):
            _archive = val.get("archive")
            if _archive.get("size"):
                linear_dict.update(
                    {
                        element
                        + "size"
                        + tag: {element: {"archive_size": _archive.get("size")}}
                    }
                )
            if _archive.get("file_num"):
                linear_dict.update(
                    {
                        element
                        + "file_num"
                        + tag: {element: {"archive_file_num": _archive.get("file_num")}}
                    }
                )
        return linear_dict
