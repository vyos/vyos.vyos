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
            "console_params",
            "file_archive_size",
            "files_archive_num",
            "files_param",
            "global_archive_num",
            "global_archive_size",
            "global_marker_interval",
            "global_preserve_fqdn",
            "global_params",
            "hosts_port",
            "hosts_params",
            "hosts_protocol",
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

    # def list_to_dict(self, param, op):
    #     _temp_param = {}
    #     primary_k = {"files": "path", "hosts": "hostname", "users": "username"}
    #     for element, val in iteritems(param):
    #         if element == "params":  # only with recursion call
    #             _tem_par = {}
    #             for par in val:
    #                 if par.get("facility") and par.get("level"):
    #                     _tem_par.update({par.get("facility") + par.get("level"): par})
    #                 elif par.get("facility") and par.get("protocol"):
    #                     _tem_par.update(
    #                         {par.get("facility") + par.get("protocol"): par}
    #                     )
    #                 else:
    #                     _tem_par.update({par.get("facility"): par})
    #             return _tem_par

    #         if element == "console_params":
    #             _temp = {}
    #             for con in val:
    #                 _temp.update({con.get("facility"): {element: con}})
    #             _temp_param.update(_temp)
    #         elif element == "global_params":
    #             if val.get("params"):
    #                 val["params"] = self.list_to_dict({"params": val.get("params")}, op)
    #             _temp_param.update({element: val})
    #         else:  # handle host/user/files
    #             _temp = {}
    #             for v in val:
    #                 if v.get("params"):
    #                     v["params"] = self.list_to_dict({"params": v.get("params")}, op)
    #                 _temp.update({v.get(primary_k.get(element)): {element: v}})
    #             _temp_param.update(_temp)
    #     return _temp_param

    def list_to_dict(self, param, op):
        _temp_param = {}
        primary_k = {"files": "path", "hosts": "hostname", "users": "username"}
        for element, val in iteritems(param):
            if element == "params":  # only with recursion call
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

            if element == "console_params":
                _temp = {}
                for con in val:
                    _temp.update({con.get("facility"): {element: con}})
                _temp_param.update(_temp)

            elif element == "global_params":
                if val.get("params"):
                    par = self.list_to_dict(val, op)
                    for k, v in iteritems(par):
                        _temp_param.update({k + "gp": {element: v}})
                if val.get("preserve_fqdn"):
                    _temp_param.update(
                        {
                            "preserve_fqdn": {
                                "global_preserve_fqdn": val.get("preserve_fqdn")
                            }
                        }
                    )
                if val.get("marker_interval"):
                    _temp_param.update(
                        {
                            "marker_interval": {
                                "global_marker_interval": val.get("marker_interval")
                            }
                        }
                    )
                if val.get("archive"):
                    if val.get("archive").get("size"):
                        _temp_param.update(
                            {"global_size": {"global_archive_size": val.get("archive")}}
                        )
                    if val.get("archive").get("file_num"):
                        _temp_param.update(
                            {
                                "global_file_num": {
                                    "global_archive_num": val.get("archive")
                                }
                            }
                        )

            elif element == "users":
                for v in val:
                    if v.get("params"):
                        par = self.list_to_dict(v, op)
                        for m, n in iteritems(par):
                            n["username"] = v.get("username")
                            _temp_param.update({m + v.get("username"): {element: n}})

            elif element == "hosts":
                for v in val:
                    if v.get("params"):
                        par = self.list_to_dict(v, op)
                        for m, n in iteritems(par):
                            n["hostname"] = v.get("hostname")
                            tag = "hosts_params" if n.get("level") else "hosts_protocol"
                            _temp_param.update({m + v.get("hostname"): {tag: n}})
                    if v.get("port"):
                        tag = "hosts_port"
                        arc = {"hostname": v.get("hostname"), "port": v.get("port")}
                        _temp_param.update({"port" + v.get("hostname"): {tag: arc}})

            elif element == "files":
                for v in val:
                    if v.get("params"):
                        par = self.list_to_dict(v, op)
                        for m, n in iteritems(par):
                            n["path"] = v.get("path")
                            _temp_param.update({m + v.get("path"): {"files_param": n}})
                    if v.get("archive"):
                        if v.get("archive").get("size"):
                            arc = {
                                "size": v.get("archive").get("size"),
                                "path": v.get("path"),
                            }
                            _temp_param.update(
                                {
                                    "file_size"
                                    + v.get("path"): {"file_archive_size": arc}
                                }
                            )
                        if v.get("archive").get("file_num"):
                            arc = {
                                "file_num": v.get("archive").get("file_num"),
                                "path": v.get("path"),
                            }
                            _temp_param.update(
                                {"file_num" + v.get("path"): {"files_archive_num": arc}}
                            )
        return _temp_param
