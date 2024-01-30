"""Rougail object model

Silique (https://www.silique.fr)
Copyright (C) 2023-2024

distribued with GPL-2 or later license

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from typing import Optional, Union, get_type_hints, Any, Literal, List, Dict, Iterator
from pydantic import BaseModel, StrictBool, StrictInt, StrictFloat, StrictStr
from .utils import get_jinja_variable_to_param, get_realpath


BASETYPE = Union[StrictBool, StrictInt, StrictFloat, StrictStr, None]


class Param(BaseModel):
    key: str


class AnyParam(Param):
    type: str
    value: BASETYPE


class VariableParam(Param):
    type: str
    variable: str
    propertyerror: bool = True
    optional: bool = False


class SuffixParam(Param):
    type: str


class InformationParam(Param):
    type: str
    information: str
    variable: Optional[str] = None


class IndexParam(Param):
    type: str


PARAM_TYPES = {
    "any": AnyParam,
    "variable": VariableParam,
    "suffix": SuffixParam,
    "information": InformationParam,
    "index": IndexParam,
}


class Calculation(BaseModel):
    path_prefix: Optional[str]
    path: str

    def get_realpath(
        self,
        path: str,
    ) -> str:
        return get_realpath(path, self.path_prefix)

    def get_params(self, objectspace):
        if not self.params:
            return {}
        params = {}
        for param_obj in self.params:
            param = param_obj.model_dump()
            if param.get("type") == "variable":
                variable_path = self.get_realpath(param["variable"])
                variable, suffix, dynamic = objectspace.paths.get_with_dynamic(variable_path)
                if not variable:
                    if not param.get("optional"):
                        raise Exception(f"cannot find {variable_path}")
                    continue
                if not isinstance(variable, objectspace.variable):
                    raise Exception("pfff it's a family")
                param["variable"] = variable
                if suffix:
                    param["suffix"] = suffix
                    param["dynamic"] = dynamic
            if param.get("type") == "information":
                if param["variable"]:
                    variable_path = self.get_realpath(param["variable"])
                    param["variable"] = objectspace.paths[variable_path]
                    if not param["variable"]:
                        raise Exception("pffff")
                else:
                    del param["variable"]
            params[param.pop("key")] = param
        return params


class JinjaCalculation(Calculation):
    attribute_name: Literal[
        "frozen", "hidden", "mandatory", "disabled", "default", "validators", "choices"
    ]
    jinja: StrictStr
    params: Optional[List[Param]] = None
    return_type: BASETYPE = None
    inside_list: bool

    def _jinja_to_function(
        self,
        function,
        return_type,
        multi,
        objectspace,
        *,
        add_help=False,
        params: Optional[dict] = None,
    ):
        variable = objectspace.paths[self.path]
        jinja_path = f"{self.attribute_name}_{self.path}"
        idx = 0
        while jinja_path in objectspace.jinja:
            jinja_path = f"{self.attribute_name}_{self.path}_{idx}"
            idx += 1
        objectspace.jinja[jinja_path] = self.jinja
        default = {
            "function": function,
            "params": {
                "__internal_jinja": jinja_path,
                "__internal_type": return_type,
                "__internal_multi": multi,
            },
        }
        if add_help:
            default["help"] = function + "_help"
        if self.params:
            default["params"] |= self.get_params(objectspace)
        if params:
            default["params"] |= params
        for sub_variable, suffix, true_path, dynamic in get_jinja_variable_to_param(
            self.jinja,
            objectspace,
            variable.xmlfiles,
            objectspace.functions,
            self.path_prefix,
        ):
            if isinstance(sub_variable, objectspace.variable):
                default["params"][true_path] = {
                    "type": "variable",
                    "variable": sub_variable,
                }
                if suffix:
                    default["params"][true_path]["suffix"] = suffix
                    default["params"][true_path]["dynamic"] = dynamic
        return default

    def to_function(
        self,
        objectspace,
    ) -> dict:
        if self.attribute_name == "default":
            if self.return_type:
                raise Exception("return_type not allowed!")
            variable = objectspace.paths[self.path]
            return_type = variable.type
            if self.inside_list:
                multi = False
            elif self.path in objectspace.followers:
                multi = objectspace.multis[self.path] == "submulti"
            else:
                multi = self.path in objectspace.multis
            return self._jinja_to_function(
                "jinja_to_function",
                return_type,
                multi,
                objectspace,
            )
        elif self.attribute_name == "validators":
            if self.return_type:
                raise Exception("pfff")
            return self._jinja_to_function(
                "valid_with_jinja",
                "string",
                False,
                objectspace,
            )
        elif self.attribute_name in ["frozen", "hidden", "disabled", "mandatory"]:
            if self.return_type:
                raise Exception("return_type not allowed!")
            return self._jinja_to_function(
                "jinja_to_property",
                "string",
                False,
                objectspace,
                add_help=True,
                params={None: [self.attribute_name]},
            )
        elif self.attribute_name == "choices":
            return_type = self.return_type
            if return_type is None:
                return_type = "string"
            return self._jinja_to_function(
                "jinja_to_function",
                return_type,
                not self.inside_list,
                objectspace,
            )
        raise Exception("hu?")


class VariableCalculation(Calculation):
    attribute_name: Literal[
        "frozen", "hidden", "mandatory", "disabled", "default", "choices"
    ]
    variable: StrictStr
    propertyerror: bool = True
    inside_list: bool

    def to_function(
        self,
        objectspace,
    ) -> dict:
        variable_path = self.get_realpath(self.variable)
        variable, suffix, dynamic = objectspace.paths.get_with_dynamic(variable_path)
        if not variable:
            raise Exception(f"pffff {variable_path}")
        if not isinstance(variable, objectspace.variable):
            raise Exception("pfff it's a family")
        param = {
            "type": "variable",
            "variable": variable,
            "propertyerror": self.propertyerror,
        }
        if suffix:
            param["suffix"] = suffix
            param["dynamic"] = dynamic
        params = {None: [param]}
        function = "calc_value"
        help_function = None
        if self.attribute_name in ["frozen", "hidden", "disabled", "mandatory"]:
            function = "variable_to_property"
            help_function = "variable_to_property"
            if variable.type != "boolean":
                raise Exception("only boolean!")
            params[None].insert(0, self.attribute_name)
        elif (
            self.attribute_name != "default" and variable.path not in objectspace.multis
        ):
            raise Exception("pffff")
        if not self.inside_list and self.path in objectspace.multis:
            if (
                not objectspace.paths.is_dynamic(variable_path)
                and variable_path not in objectspace.multis
            ):
                params["multi"] = True
            params["allow_none"] = True
        if self.inside_list and variable.path in objectspace.multis:
            raise Exception("pfff")
        ret = {
            "function": function,
            "params": params,
        }
        if help_function:
            ret["help"] = help_function
        return ret


class InformationCalculation(Calculation):
    attribute_name: Literal["default"]
    information: StrictStr
    variable: Optional[StrictStr]
    inside_list: bool

    def to_function(
        self,
        objectspace,
    ) -> dict:
        param = {
            "type": "information",
            "information": self.information,
        }
        if self.variable:
            variable_path = self.get_realpath(self.variable)
            variable = objectspace.paths[variable_path]
            if variable is None:
                raise Exception("pfff")
            param["variable"] = variable
        return {
            "function": "calc_value",
            "params": {None: [param]},
        }


class SuffixCalculation(Calculation):
    attribute_name: Literal["default"]

    def to_function(
        self,
        objectspace,
    ) -> dict:
        return {
            "function": "calc_value",
            "params": {None: [{"type": "suffix"}]},
        }


class IndexCalculation(Calculation):
    attribute_name: Literal["default"]

    def to_function(
        self,
        objectspace,
    ) -> dict:
        return {
            "function": "calc_value",
            "params": {None: [{"type": "index"}]},
        }


CALCULATION_TYPES = {
    "jinja": JinjaCalculation,
    "variable": VariableCalculation,
    "information": InformationCalculation,
    "suffix": SuffixCalculation,
    "index": IndexCalculation,
}
BASETYPE_CALC = Union[StrictBool, StrictInt, StrictFloat, StrictStr, None, Calculation]


class Family(BaseModel):
    name: str
    description: Optional[str] = None
    type: Literal["family", "leadership", "dynamic"] = "family"
    help: Optional[str] = None
    mode: Optional[str] = None
    hidden: Union[bool, Calculation] = False
    disabled: Union[bool, Calculation] = False
    xmlfiles: List[str] = []
    path: str

    class ConfigDict:
        arbitrary_types_allowed = True


class Dynamic(Family):
    variable: str


class Variable(BaseModel):
    name: str
    type: Literal[
        "number",
        "float",
        "string",
        "password",
        "secret",
        "mail",
        "boolean",
        "unix_filename",
        "date",
        "unix_user",
        "ip",
        "local_ip",
        "netmask",
        "network",
        "broadcast",
        "netbios",
        "domainname",
        "hostname",
        "web_address",
        "port",
        "mac",
        "cidr",
        "network_cidr",
        "choice",
        "unix_permissions",
    ] = "string"
    description: Optional[str] = None
    default: Union[List[BASETYPE_CALC], BASETYPE_CALC] = None
    params: Optional[List[Param]] = None
    validators: Optional[List[Calculation]] = None
    multi: bool = False
    unique: Optional[bool] = None
    help: Optional[str] = None
    hidden: Union[bool, Calculation] = False
    disabled: Union[bool, Calculation] = False
    mandatory: Union[None, bool, Calculation] = True
    auto_save: bool = False
    mode: Optional[str] = None
    test: Optional[list] = None
    xmlfiles: List[str] = []
    path: str

    class ConfigDict:
        arbitrary_types_allowed = True


class Choice(Variable):
    choices: Union[List[BASETYPE_CALC], Calculation]


class SymLink(BaseModel):
    name: str
    type: str = "symlink"
    opt: Variable
    xmlfiles: List[str] = []
    path: str
