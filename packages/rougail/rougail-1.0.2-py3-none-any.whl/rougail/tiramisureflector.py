"""loader
flattened XML specific

Created by:
EOLE (http://eole.orion.education.fr)
Copyright (C) 2005-2018

Forked by:
Cadoles (http://www.cadoles.com)
Copyright (C) 2019-2021

Silique (https://www.silique.fr)
Copyright (C) 2022-2024

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
from typing import Optional
from json import dumps
from os.path import isfile, basename

from .i18n import _
from .annotator import CONVERT_OPTION
from .error import DictConsistencyError
from .utils import normalize_family
from .object_model import Calculation


class BaseElt:  # pylint: disable=R0903
    """Base element"""

    path = "."
    type = "family"


def sorted_func_name(func_name):
    s_func_name = func_name.split("/")
    s_func_name.reverse()
    return "/".join(s_func_name)


class TiramisuReflector:
    """Convert object to tiramisu representation"""

    def __init__(
        self,
        objectspace,
        funcs_paths,
    ):
        self.rougailconfig = objectspace.rougailconfig
        self.jinja_added = False
        self.reflector_objects = {}
        self.text = {
            "header": [],
            "option": [],
        }
        if self.rougailconfig["export_with_import"]:
            if self.rougailconfig["internal_functions"]:
                for func in self.rougailconfig["internal_functions"]:
                    self.text["header"].append(f"func[func] = func")
            self.text["header"].extend(
                [
                    "from tiramisu import *",
                    "from tiramisu.setting import ALLOWED_LEADER_PROPERTIES",
                ]
            )
            for mode in self.rougailconfig["modes_level"]:
                self.text["header"].append(f'ALLOWED_LEADER_PROPERTIES.add("{mode}")')
        if funcs_paths:
            if self.rougailconfig["export_with_import"]:
                self.text["header"].extend(
                    [
                        "from importlib.machinery import SourceFileLoader as _SourceFileLoader",
                        "from importlib.util import spec_from_loader as _spec_from_loader, module_from_spec as _module_from_spec",
                        "global func",
                        "func = {'calc_value': calc_value}",
                        "",
                        "def _load_functions(path):",
                        "    global _SourceFileLoader, _spec_from_loader, _module_from_spec, func",
                        "    loader = _SourceFileLoader('func', path)",
                        "    spec = _spec_from_loader(loader.name, loader)",
                        "    func_ = _module_from_spec(spec)",
                        "    loader.exec_module(func_)",
                        "    for function in dir(func_):",
                        "        if function.startswith('_'):",
                        "            continue",
                        "        func[function] = getattr(func_, function)",
                    ]
                )
            for funcs_path in sorted(funcs_paths, key=sorted_func_name):
                if not isfile(funcs_path):
                    continue
                self.text["header"].append(f"_load_functions('{funcs_path}')")
        self.objectspace = objectspace
        self.make_tiramisu_objects()
        if self.rougailconfig["export_with_import"] and (
            self.rougailconfig["force_convert_dyn_option_description"]
            or self.objectspace.has_dyn_option is True
        ):
            self.text["header"].append(
                "from rougail.tiramisu import ConvertDynOptionDescription"
            )
        for key, value in self.objectspace.jinja.items():
            self.add_jinja_to_function(key, value)

    def add_jinja_support(self):
        if not self.jinja_added:
            self.text["header"].extend(
                [
                    "from jinja2 import StrictUndefined, DictLoader",
                    "from jinja2.sandbox import SandboxedEnvironment",
                    "from rougail.annotator.variable import CONVERT_OPTION",
                    "from tiramisu.error import ValueWarning",
                    "def jinja_to_function(__internal_jinja, __internal_type, __internal_multi, **kwargs):",
                    "    global ENV, CONVERT_OPTION",
                    "    kw = {}",
                    "    for key, value in kwargs.items():",
                    "        if '.' in key:",
                    "            c_kw = kw",
                    "            path, var = key.rsplit('.', 1)",
                    "            for subkey in path.split('.'):",
                    "                c_kw = c_kw.setdefault(subkey, {})",
                    "            c_kw[var] = value",
                    "        else:",
                    "            kw[key] = value",
                    "    values = ENV.get_template(__internal_jinja).render(kw, **func).strip()",
                    "    convert = CONVERT_OPTION[__internal_type].get('func', str)",
                    "    if __internal_multi:",
                    "        return [convert(val) for val in values.split()]",
                    "    values = convert(values)",
                    "    return values if values != '' and values != 'None' else None",
                    "def variable_to_property(prop, value):",
                    "    return prop if value else None",
                    "def jinja_to_property(prop, **kwargs):",
                    "    value = func['jinja_to_function'](**kwargs)",
                    "    return func['variable_to_property'](prop, value is not None)",
                    "def jinja_to_property_help(prop, **kwargs):",
                    "    value = func['jinja_to_function'](**kwargs)",
                    "    return (prop, f'\"{prop}\" ({value})')",
                    "def valid_with_jinja(warnings_only=False, **kwargs):",
                    "    global ValueWarning",
                    "    value = func['jinja_to_function'](**kwargs)",
                    "    if value:",
                    "       if warnings_only:",
                    "           raise ValueWarning(value)",
                    "       else:",
                    "           raise ValueError(value)",
                    "func['jinja_to_function'] = jinja_to_function",
                    "func['jinja_to_property'] = jinja_to_property",
                    "func['jinja_to_property_help'] = jinja_to_property_help",
                    "func['variable_to_property'] = variable_to_property",
                    "func['valid_with_jinja'] = valid_with_jinja",
                    "dict_env = {}",
                ]
            )
            self.jinja_added = True

    def add_jinja_to_function(
        self,
        variable_name: str,
        jinja: str,
    ) -> None:
        self.add_jinja_support()
        jinja_text = dumps(jinja, ensure_ascii=False)
        self.text["header"].append(f"dict_env['{variable_name}'] = {jinja_text}")

    def make_tiramisu_objects(self) -> None:
        """make tiramisu objects"""
        baseelt = BaseElt()
        self.objectspace.reflector_names[
            baseelt.path
        ] = f'option_0{self.rougailconfig["suffix"]}'
        basefamily = Family(
            baseelt,
            self,
        )
        # FIXMEif not self.objectspace.paths.has_path_prefix():
        if 1:
            #            for elt in self.reorder_family(self.objectspace.space):
            for elt in self.objectspace.paths.get():
                if elt.path in self.objectspace.families:
                    Family(
                        elt,
                        self,
                    )
                else:
                    Variable(
                        elt,
                        self,
                    )
        else:
            path_prefixes = self.objectspace.paths.get_path_prefixes()
            for path_prefix in path_prefixes:
                space = self.objectspace.space.variables[path_prefix]
                self.set_name(space)
                baseprefix = Family(
                    space,
                    self,
                )
                basefamily.add(baseprefix)
                for elt in self.reorder_family(space):
                    self.populate_family(
                        baseprefix,
                        elt,
                    )
                if not hasattr(baseprefix.elt, "information"):
                    baseprefix.elt.information = self.objectspace.information(
                        baseprefix.elt.xmlfiles
                    )
                for key, value in self.objectspace.paths.get_providers_path(
                    path_prefix
                ).items():
                    setattr(baseprefix.elt.information, key, value)
                for key, value in self.objectspace.paths.get_suppliers_path(
                    path_prefix
                ).items():
                    setattr(baseprefix.elt.information, key, value)
        baseelt.name = normalize_family(self.rougailconfig["base_option_name"])
        baseelt.description = self.rougailconfig["base_option_name"]
        self.reflector_objects[baseelt.path].get(
            [], baseelt.description
        )  # pylint: disable=E1101

    def set_name(
        self,
        elt,
    ):
        """Set name"""
        if elt.path not in self.objectspace.reflector_names:
            self.objectspace.set_name(elt, "optiondescription_")
        return self.objectspace.reflector_names[elt.path]

    def get_text(self):
        """Get text"""
        if self.jinja_added:
            self.text["header"].extend(
                [
                    "ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)",
                    "ENV.filters = func",
                    "ENV.compile_templates('jinja_caches', zip=None)",
                ]
            )
        return "\n".join(self.text["header"] + self.text["option"])


class Common:
    """Common function for variable and family"""

    def __init__(
        self,
        elt,
        tiramisu,
    ):
        self.objectspace = tiramisu.objectspace
        self.elt = elt
        self.option_name = None
        self.tiramisu = tiramisu
        tiramisu.reflector_objects[elt.path] = self
        self.object_type = None

    def get(self, calls, parent_name):
        """Get tiramisu's object"""
        self_calls = calls.copy()
        if self.elt.path in self_calls:
            msg = f'"{self.elt.path}" will make an infinite loop'
            raise DictConsistencyError(msg, 80, self.elt.xmlfiles)
        self_calls.append(self.elt.path)
        self.calls = self_calls
        if self.option_name is None:
            self.option_name = self.objectspace.reflector_names[self.elt.path]
            self.populate_attrib()
            self.populate_informations()
        return self.option_name

    def populate_attrib(self):
        """Populate attributes"""
        keys = {"name": self.convert_str(self.elt.name)}
        if hasattr(self.elt, "description") and self.elt.description:
            keys["doc"] = self.convert_str(self.elt.description)
        self._populate_attrib(keys)
        if self.elt.path in self.objectspace.properties:
            keys["properties"] = self.properties_to_string(
                self.objectspace.properties[self.elt.path]
            )
        attrib = ", ".join([f"{key}={value}" for key, value in keys.items()])
        self.tiramisu.text["option"].append(
            f"{self.option_name} = {self.object_type}({attrib})"
        )

    def _populate_attrib(
        self,
        keys: dict,
    ) -> None:  # pragma: no cover
        raise NotImplementedError()

    @staticmethod
    def convert_str(value):
        """convert string"""
        if value is None:
            return "None"
        return dumps(value, ensure_ascii=False)

    def properties_to_string(
        self,
        values: list,
    ) -> None:
        """Change properties to string"""
        properties = []
        calc_properties = []
        for property_, value in values.items():
            if value is True:
                properties.append(self.convert_str(property_))
            else:
                if isinstance(value, list):
                    for val in value:
                        calc_properties.append(self.calculation_value(val))
                else:
                    calc_properties.append(self.calculation_value(value))
        return "frozenset({" + ", ".join(sorted(properties) + calc_properties) + "})"

    def calc_properties(
        self,
        prop,
        calculation,
    ) -> str:
        """Populate properties"""
        option_name = self.tiramisu.reflector_objects[child.source.path].get(
            self.calls, self.elt.path
        )
        kwargs = (
            f"'condition': ParamOption({option_name}, notraisepropertyerror=True), "
            f"'expected': {self.populate_param(child.expected)}"
        )
        if child.inverse:
            kwargs += ", 'reverse_condition': ParamValue(True)"
        return (
            f"Calculation(func['calc_value'], Params(ParamValue('{child.name}'), "
            f"kwargs={{{kwargs}}}), func['calc_value_property_help'])"
        )

    def populate_informations(self):
        """Populate Tiramisu's informations"""
        informations = self.objectspace.informations.get(self.elt.path)
        if not informations:
            return
        for key, value in informations.items():
            if isinstance(value, str):
                value = self.convert_str(value)
            self.tiramisu.text["option"].append(
                f"{self.option_name}.impl_set_information('{key}', {value})"
            )

    def populate_param(
        self,
        param,
    ):
        """Populate variable parameters"""
        if not isinstance(param, dict):
            if isinstance(param, str):
                value = self.convert_str(param)
            else:
                value = param
            return f"ParamValue({value})"
        if param["type"] == "information":
            if self.elt.multi:
                default = []
            else:
                default = None
            if "variable" in param:
                if param["variable"].path == self.elt.path:
                    return f'ParamSelfInformation("{param["information"]}", {default})'
                return f'ParamInformation("{param["information"]}", {default}, option={self.tiramisu.reflector_objects[param["variable"].path].get(self.calls, self.elt.path)})'
            return f'ParamInformation("{param["information"]}", {default})'
        if param["type"] == "suffix":
            return "ParamSuffix()"
        if param["type"] == "index":
            return "ParamIndex()"
        if param["type"] == "variable":
            return self.build_option_param(
                param["variable"],
                param.get("propertyerror", True),
                param.get("suffix"),
                param.get("dynamic"),
            )
        if param["type"] == "any":
            if isinstance(param["value"], str):
                value = self.convert_str(param["value"])
            else:
                value = str(param["value"])
            return "ParamValue(" + value + ")"
        raise Exception("pfff")

    def build_option_param(
        self,
        param,
        propertyerror,
        suffix: Optional[str],
        dynamic,
    ) -> str:
        """build variable parameters"""
        if param.path == self.elt.path:
            return "ParamSelfOption(whole=False)"
        option_name = self.tiramisu.reflector_objects[param.path].get(
            self.calls, self.elt.path
        )
        params = [f"{option_name}"]
        if suffix is not None:
            param_type = "ParamDynOption"
            family = self.tiramisu.reflector_objects[dynamic.path].get(
                self.calls, self.elt.path
            )
            params.extend([f"'{suffix}'", f"{family}"])
        else:
            param_type = "ParamOption"
        if not propertyerror:
            params.append("notraisepropertyerror=True")
        return f'{param_type}({", ".join(params)})'

    def calculation_value(
        self,
        function,
    ) -> str:
        """Generate calculated value"""
        self.tiramisu.add_jinja_support()
        child = function.to_function(self.objectspace)
        new_args = []
        kwargs = []
        if "params" in child:
            for key, value in child["params"].items():
                if not key:
                    for val in value:
                        new_args.append(self.populate_param(val))
                else:
                    kwargs.append(f"'{key}': " + self.populate_param(value))
        ret = (
            f"Calculation(func['{child['function']}'], Params(("
            + ", ".join(new_args)
            + ")"
        )
        if kwargs:
            ret += ", kwargs={" + ", ".join(kwargs) + "}"
        ret += ")"
        if hasattr(child, "warnings_only"):
            print("HU????")
            ret += f", warnings_only={child.warnings_only}"
        if "help" in child:
            ret += f", help_function=func['{child['help']}']"
        ret = ret + ")"
        return ret


class Variable(Common):
    """Manage variable"""

    def __init__(
        self,
        elt,
        tiramisu,
    ):
        super().__init__(elt, tiramisu)
        self.object_type = CONVERT_OPTION[elt.type]["opttype"]

    def _populate_attrib(
        self,
        keys: dict,
    ):
        if self.elt.type == "symlink":
            keys["opt"] = self.tiramisu.reflector_objects[self.elt.opt.path].get(
                self.calls, self.elt.path
            )
        if self.elt.type == "choice":
            choices = self.elt.choices
            if isinstance(choices, Calculation):
                keys["values"] = self.calculation_value(choices)
            else:
                new_values = []
                for value in choices:
                    if isinstance(value, Calculation):
                        new_values.append(self.calculation_value(value))
                    elif isinstance(value, str):
                        new_values.append(self.convert_str(value))
                    else:
                        new_values.append(str(value))
                keys["values"] = "(" + ", ".join(new_values)
                if len(new_values) <= 1:
                    keys["values"] += ","
                keys["values"] += ")"
        if self.elt.path in self.objectspace.multis:
            keys["multi"] = self.objectspace.multis[self.elt.path]
        if hasattr(self.elt, "default") and self.elt.default is not None:
            value = self.elt.default
            if isinstance(value, str):
                value = self.convert_str(value)
            elif isinstance(value, Calculation):
                value = self.calculation_value(value)
            elif isinstance(value, list):
                value = value.copy()
                for idx, val in enumerate(value):
                    if isinstance(val, Calculation):
                        value[idx] = self.calculation_value(val)
                    else:
                        value[idx] = self.convert_str(val)
                value = "[" + ", ".join(value) + "]"
            keys["default"] = value
        if self.elt.path in self.objectspace.default_multi:
            value = self.objectspace.default_multi[self.elt.path]
            if isinstance(value, str):
                value = self.convert_str(value)
            elif isinstance(value, Calculation):
                value = self.calculation_value(value)
            keys["default_multi"] = value
        if self.elt.validators:
            validators = []
            for val in self.elt.validators:
                if isinstance(val, Calculation):
                    validators.append(self.calculation_value(val))
                else:
                    validators.append(val)
            keys["validators"] = "[" + ", ".join(validators) + "]"
        for key, value in CONVERT_OPTION[self.elt.type].get("initkwargs", {}).items():
            if isinstance(value, str):
                value = f"'{value}'"
            keys[key] = value
        if self.elt.params:
            for param in self.elt.params:
                value = param.value
                if isinstance(value, str):
                    value = self.convert_str(value)
                keys[param.key] = value


class Family(Common):
    """Manage family"""

    def __init__(
        self,
        elt,
        tiramisu,
    ):
        super().__init__(elt, tiramisu)
        if self.elt.type == "dynamic":
            self.tiramisu.objectspace.has_dyn_option = True
            self.object_type = "ConvertDynOptionDescription"
        elif self.elt.type == "leadership":
            self.object_type = "Leadership"
        else:
            self.object_type = "OptionDescription"
        self.children = []

    def add(self, child):
        """Add a child"""
        self.children.append(child)

    def _populate_attrib(
        self,
        keys: list,
    ) -> None:
        if self.elt.type == "dynamic":
            dyn = self.tiramisu.reflector_objects[self.elt.variable.path].get(
                self.calls, self.elt.path
            )
            keys[
                "suffixes"
            ] = f"Calculation(func['calc_value'], Params((ParamOption({dyn}, notraisepropertyerror=True))))"
        children = []
        for path in self.objectspace.parents[self.elt.path]:
            children.append(self.objectspace.paths[path])
        keys["children"] = (
            "["
            + ", ".join(
                [
                    self.tiramisu.reflector_objects[child.path].get(
                        self.calls, self.elt.path
                    )
                    for child in children
                ]
            )
            + "]"
        )
