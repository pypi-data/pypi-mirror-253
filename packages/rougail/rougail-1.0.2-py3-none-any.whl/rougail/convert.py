"""Takes a bunch of Rougail XML dispatched in differents folders
as an input and outputs a Tiramisu's file.

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

Sample usage::

    >>> from rougail import RougailConvert
    >>> rougail = RougailConvert()
    >>> tiramisu = rougail.save('tiramisu.py')

The Rougail

- loads the XML into an internal RougailObjSpace representation
- visits/annotates the objects
- dumps the object space as Tiramisu string

The visit/annotation stage is a complex step that corresponds to the Rougail
procedures.
"""
import logging
from pathlib import Path
from typing import Optional, Union, get_type_hints, Any, Literal, List, Dict, Iterator, Tuple
from itertools import chain
from re import findall

from yaml import safe_load
from pydantic import ValidationError

from .i18n import _
from .annotator import SpaceAnnotator
from .tiramisureflector import TiramisuReflector
from .utils import get_realpath
from .object_model import (
    Family,
    Dynamic,
    Variable,
    Choice,
    SymLink,
    CALCULATION_TYPES,
    Calculation,
    PARAM_TYPES,
    AnyParam,
)
from .error import DictConsistencyError


property_types = Union[Literal[True], Calculation]
properties_types = Dict[str, property_types]


class Property:
    def __init__(self) -> None:
        self._properties: Dict[str, properties_types] = {}

    def add(
        self,
        path: str,
        property_: str,
        value: property_types,
    ) -> None:
        self._properties.setdefault(path, {})[property_] = value

    def __getitem__(
        self,
        path: str,
    ) -> properties_types:
        return self._properties.get(path, {})

    def __contains__(
        self,
        path: str,
    ) -> bool:
        return path in self._properties


class Paths:
    def __init__(self) -> None:
        self._data: Dict[str, Union[Variable, Family]] = {}
        self._dynamics: List[str] = []
        self.path_prefix = None

    def has_value(self) -> bool:
        return self._data != {}

    def add(
        self,
        path: str,
        data: Any,
        is_dynamic: bool,
        force: bool = False,
    ) -> None:
        self._data[path] = data
        if not force and is_dynamic:
            self._dynamics.append(path)

    def get_with_dynamic(
        self,
        path: str,
    ) -> Any:
        suffix = None
        dynamic_path = None
        dynamic_variable_path = None
        if not path in self._data:
            for dynamic in self._dynamics:
                if "{{ suffix }}" in dynamic:
                    regexp = "^" + dynamic.replace('{{ suffix }}', '(.*)') + '.'
                    finded = findall(regexp, path)
                    if len(finded) != 1:
                        continue
                    splitted_dynamic = dynamic.split('.')
                    splitted_path = path.split('.')
                    for idx, s in enumerate(splitted_dynamic):
                        if '{{ suffix }}' in s:
                            break

                    suffix_path = '.'.join(splitted_path[idx + 1:])
                    if suffix_path:
                        suffix_path = "." + suffix_path
                    suffix = splitted_path[idx] + suffix_path
                    dynamic_path = dynamic
                    dynamic_variable_path = dynamic + suffix_path
                    break
                elif path.startswith(dynamic):
                    subpaths = path[len(dynamic) :].split(".", 1)
                    if (
                        subpaths[0]
                        and len(subpaths) > 1
                        and dynamic + "." + subpaths[1] in self._dynamics
                    ):
                        suffix = (
                            dynamic.rsplit(".", 1)[-1] + subpaths[0] + "." + subpaths[1]
                        )
                        dynamic_path = dynamic
                        dynamic_variable_path = dynamic + "." + subpaths[1]
                        break
        if suffix is None and not path in self._data:
            return None, None, None
        dynamic = None
        if suffix and dynamic_variable_path:
            path = dynamic_variable_path
            dynamic = self._data[dynamic_path]
        return self._data[path], suffix, dynamic

    def __getitem__(
        self,
        path: str,
    ) -> Union[Family, Variable]:
        if not path in self._data:
            raise AttributeError(f"cannot find variable or family {path}")
        return self._data[path]

    def __contains__(
        self,
        path: str,
    ) -> bool:
        return path in self._data

    def __delitem__(
        self,
        path: str,
    ) -> None:
        logging.info("remove empty family %s", path)
        del self._data[path]

    def is_dynamic(self, path: str) -> bool:
        return path in self._dynamics

    def get(self):
        return self._data.values()


information_types = Dict[str, Union[str, int, float, bool]]


class Informations:
    def __init__(self) -> None:
        self._data: Dict[str, information_types] = {}

    def add(
        self,
        path: str,
        key: str,
        data: Any,
    ) -> None:
        if path not in self._data:
            self._data[path] = {}
        if key in self._data[path]:
            raise Exception(f"already key {key} in {path}")
        self._data[path][key] = data

    def get(
        self,
        path: str,
    ) -> information_types:
        return self._data.get(path, {})


class ParserVariable:
    def __init__(self, rougailconfig):
        self.paths = Paths()
        self.families = []
        self.variables = []
        self.parents = {".": []}
        self.index = 0
        self.reflector_names = {}
        self.leaders = []
        self.followers = []
        self.multis = {}
        self.default_multi = {}
        self.jinja = {}
        self.rougailconfig = rougailconfig
        #
        self.family = Family
        self.dynamic = Dynamic
        self.variable = Variable
        self.choice = Choice
        #
        self.exclude_imports = []
        self.informations = Informations()
        self.properties = Property()
        # self.choices = Appendable()
        self.has_dyn_option = False
        self.path_prefix = None
        self.is_init = False
        super().__init__()

    def init(self):
        if self.is_init:
            return
        hint = get_type_hints(self.dynamic)
        self.family_types = hint["type"].__args__  # pylint: disable=W0201
        self.family_attrs = frozenset(  # pylint: disable=W0201
            set(hint) | {"redefine"} - {"name", "path", "xmlfiles"}
        )
        self.family_calculations = self.search_calculation(  # pylint: disable=W0201
            hint
        )
        #
        hint = get_type_hints(self.variable)
        self.variable_types = hint["type"].__args__  # pylint: disable=W0201
        #
        hint = get_type_hints(self.choice)
        self.choice_attrs = frozenset(  # pylint: disable=W0201
            set(hint) | {"redefine", "exists"} - {"name", "path", "xmlfiles"}
        )
        self.choice_calculations = self.search_calculation(  # pylint: disable=W0201
            hint
        )
        self.is_init = True

    ###############################################################################################
    # determine if the object is a family or a variable
    ###############################################################################################
    def is_family_or_variable(
        self,
        path: str,
        obj: dict,
        family_is_leadership: bool,
    ) -> Literal["variable", "family"]:
        """Check object to determine if it's a variable or a family"""
        # it's already has a variable or a family
        if path in self.paths:
            if path in self.families:
                return "family"
            return "variable"
        # it's: "my_variable:"
        if not obj:
            return "variable"
        # check type attributes
        obj_type = self.get_family_or_variable_type(obj)
        if obj_type:
            if obj_type in self.family_types:
                return "family"
            if obj_type in self.variable_types:
                return "variable"
            raise Exception(f"unknown type {obj_type} for {path}")
        # in a leadership there is only variable
        if family_is_leadership:
            return "variable"
        # all attributes are in variable object
        # and values in attributes are not dict is not Calculation
        extra_keys = set(obj) - self.choice_attrs
        if not extra_keys:
            for key, value in obj.items():
                if isinstance(value, dict) and not self.is_calculation(
                    key,
                    value,
                    "variable",
                    False,
                ):
                    break
            else:
                return "variable"
        return "family"

    def get_family_or_variable_type(
        self,
        obj: dict,
    ) -> Optional[str]:
        """Check 'type' attributes"""
        if "_type" in obj:
            # only family has _type attributs
            return obj["_type"]
        if "type" in obj and isinstance(obj["type"], str):
            return obj["type"]
        return None

    ###############################################################################################
    # create, update or delete family or variable object
    ###############################################################################################
    def family_or_variable(
        self,
        filename: str,
        name: str,
        subpath: str,
        obj: dict,
        first_variable: bool = False,
        family_is_leadership: bool = False,
        family_is_dynamic: bool = False,
    ) -> None:
        if name.startswith("_"):
            raise Exception("forbidden!")
        path = f"{subpath}.{name}"
        typ = self.is_family_or_variable(
            path,
            obj,
            family_is_leadership,
        )
        logging.info("family_or_variable: %s is a %s", path, typ)
        if typ == "family":
            parser = self.parse_family
        else:
            parser = self.parse_variable
        parser(
            filename,
            name,
            path,
            obj,
            first_variable,
            family_is_leadership,
            family_is_dynamic,
        )

    def parse_family(
        self,
        filename: str,
        name: str,
        path: str,
        obj: Optional[Dict[str, Any]],
        first_variable: bool = False,
        family_is_leadership: bool = False,
        family_is_dynamic: bool = False,
    ) -> None:
        """ Parse a family
        """
        if obj is None:
            return
        family_obj = {}
        subfamily_obj = {}
        force_to_attrs = list(self.list_attributes(obj))
        for key, value in obj.items():
            if key in force_to_attrs:
                if key.startswith("_"):
                    key = key[1:]
                family_obj[key] = value
            else:
                subfamily_obj[key] = value
        if path in self.paths:
            if family_obj:
                if not obj.pop("redefine", False):
                    raise Exception(
                        "The family {path} already exists and she is not redefined"
                    )
                self.paths.add(
                    path,
                    self.paths[path].model_copy(update=obj),
                    family_is_dynamic,
                    force=True,
                )
            self.paths[path].xmlfiles.append(filename)
            force_not_first = True
            if self.paths[path].type == "dynamic":
                family_is_dynamic = True
        else:
            if "redefine" in obj and obj["redefine"]:
                raise Exception(
                    f'cannot redefine the inexisting family "{path}" in {filename}'
                )
            extra_attrs = set(family_obj) - self.family_attrs
            if extra_attrs:
                raise Exception(f"extra attrs ... {extra_attrs}")
            if self.get_family_or_variable_type(family_obj) == "dynamic":
                family_is_dynamic = True
            self.add_family(
                path,
                name,
                family_obj,
                filename,
                family_is_dynamic,
            )
            force_not_first = False
        if self.paths[path].type == "leadership":
            family_is_leadership = True
        for idx, key in enumerate(subfamily_obj):
            value = subfamily_obj[key]
            if not isinstance(value, dict) and value is not None:
                raise Exception(
                    f'the variable "{path}.{key}" has a wrong type "{type(value)}"'
                )
            first_variable = not force_not_first and idx == 0
            if value is None:
                value = {}
            self.family_or_variable(
                filename,
                key,
                path,
                value,
                first_variable,
                family_is_leadership,
                family_is_dynamic,
            )

    def list_attributes(
        self,
        obj: Dict[str, Any],
    ) -> Iterator[str]:
        """ List attributes
        """
        force_to_variable = []
        for key, value in obj.items():
            if key in force_to_variable:
                continue
            if key.startswith("_"):
                # if key starts with _, it's an attribute
                yield key
                # if same key without _ exists, it's a variable!
                true_key = key[1:]
                if true_key in obj:
                    force_to_variable.append(true_key)
                continue
            if isinstance(value, dict) and not self.is_calculation(
                key,
                value,
                "family",
                False,
            ):
                # it's a dict, so a new variables!
                continue
            if key in self.family_attrs:
                yield key

    def add_family(
        self,
        path: str,
        name: str,
        family: dict,
        filenames: Union[str, List[str]],
        family_is_dynamic: bool,
    ) -> None:
        """ Add a new family
        """
        family["path"] = path
        if not isinstance(filenames, list):
            filenames = [filenames]
        family["xmlfiles"] = filenames
        obj_type = self.get_family_or_variable_type(family)
        if obj_type == "dynamic":
            family_obj = self.dynamic
            if "variable" in family:
                family["variable"] = get_realpath(
                    family["variable"],
                    self.path_prefix,
                )
        else:
            family_obj = self.family
        # convert to Calculation objects
        for key, value in family.items():
            if not self.is_calculation(
                key,
                value,
                "family",
                False,
            ):
                continue
            try:
                self.set_calculation(
                    family,
                    key,
                    value,
                    path,
                )
            except ValidationError as err:
                raise Exception(
                    f'the family "{path}" in "{filenames}" has an invalid "{key}": {err}'
                ) from err
        try:
            self.paths.add(
                path,
                family_obj(name=name, **family),
                family_is_dynamic,
            )
        except ValidationError as err:
            raise Exception(f'invalid family "{path}" in "{filenames}": {err}') from err
        self.set_name(
            self.paths[path],
            "optiondescription_",
        )
        if "." not in path:
            parent = "."
        else:
            parent = path.rsplit(".", 1)[0]
        self.parents[parent].append(path)
        self.parents[path] = []
        self.families.append(path)

    def parse_variable(
        self,
        filename: str,
        name: str,
        path: str,
        obj: Optional[Dict[str, Any]],
        first_variable: bool = False,
        family_is_leadership: bool = False,
        family_is_dynamic: bool = False,
    ) -> None:
        """ Parse variable
        """
        if obj is None:
            obj = {}
        extra_attrs = set(obj) - self.choice_attrs
        if extra_attrs:
            raise Exception(
                f'"{path}" is not a valid variable, there are additional '
                f'attributes: "{", ".join(extra_attrs)}"'
            )
        self.parse_parameters(path, obj, filename)
        self.parse_params(path, obj)
        if path in self.paths:
            if "exists" in obj and not obj.pop("exists"):
                return
            if not obj.pop("redefine", False):
                raise Exception(f'Variable "{path}" already exists')
            self.paths.add(path, self.paths[path].model_copy(update=obj), False, force=True)
            self.paths[path].xmlfiles.append(filename)
        else:
            if "exists" in obj and obj.pop("exists"):
                # this variable must exist
                # but it's not the case
                # so do nothing
                return
            if "redefine" in obj and obj["redefine"]:
                raise Exception(
                    f'cannot redefine the inexisting variable "{path}" in {filename}'
                )
            obj["path"] = path
            self.add_variable(
                name,
                obj,
                filename,
                family_is_dynamic,
            )
            if family_is_leadership:
                if first_variable:
                    self.leaders.append(path)
                else:
                    self.followers.append(path)

    def parse_parameters(self, path, obj, filename):
        """Parse variable parameters"""
        for key, value in obj.items():
            if self.is_calculation(
                key,
                value,
                "variable",
                False,
            ):
                try:
                    self.set_calculation(
                        obj,
                        key,
                        value,
                        path,
                    )
                except ValidationError as err:
                    raise Exception(
                        f'the variable "{path}" in "{filename}" has an invalid "{key}": {err}'
                    ) from err
                continue
            if not isinstance(value, list) or key not in self.choice_calculations[0]:
                continue
            for idx, val in enumerate(value):
                if not self.is_calculation(
                    key,
                    val,
                    "variable",
                    True,
                ):
                    continue
                try:
                    self.set_calculation(
                        obj,
                        key,
                        val,
                        path,
                        inside_list=True,
                        index=idx,
                    )
                except ValidationError as err:
                    raise Exception(
                        f'the variable "{path}" in "{filename}" has an invalid "{key}" '
                        f"at index {idx}: {err}"
                    ) from err

    def parse_params(self, path, obj):
        """ Parse variable params
        """
        if "params" not in obj:
            return
        if not isinstance(obj["params"], dict):
            raise Exception(f"params must be a dict for {path}")
        params = []
        for key, val in obj["params"].items():
            try:
                params.append(AnyParam(key=key, value=val, type="any"))
            except ValidationError as err:
                raise Exception(f'"{key}" has an invalid "params" for {path}: {err}') from err
        obj["params"] = params

    def add_variable(
        self,
        name: str,
        variable: dict,
        filename: str,
        family_is_dynamic: bool,
    ) -> None:
        """Add a new variable"""
        if not isinstance(filename, list):
            filename = [filename]
        variable["xmlfiles"] = filename
        variable_type = self.get_family_or_variable_type(variable)
        obj = {
            "symlink": SymLink,
            "choice": self.choice,
        }.get(variable_type, self.variable)
        try:
            variable_obj = obj(name=name, **variable)
        except ValidationError as err:
            raise Exception(
                f'invalid variable "{variable.path}" in "{filename}": {err}'
            ) from err
        self.paths.add(
            variable["path"],
            variable_obj,
            family_is_dynamic,
        )
        self.variables.append(variable["path"])
        self.parents[variable["path"].rsplit(".", 1)[0]].append(variable["path"])
        self.set_name(
            variable_obj,
            "option_",
        )

    def del_family(
        self,
        path: str,
    ) -> None:
        """The family is empty, so delete it"""
        del self.paths[path]
        self.families.remove(path)
        del self.parents[path]
        parent = path.rsplit(".", 1)[0]
        self.parents[parent].remove(path)

    ###############################################################################################
    # set tiramisu file name
    ###############################################################################################
    def set_name(
        self,
        obj: Union[Variable, Family],
        option_prefix: str,
    ):
        """Set Tiramisu object name"""
        self.index += 1
        self.reflector_names[
            obj.path
        ] = f'{option_prefix}{self.index}{self.rougailconfig["suffix"]}'

    ###############################################################################################
    # calculations
    ###############################################################################################
    def is_calculation(
        self,
        attribute: str,
        value: dict,
        typ: Literal["variable", "family"],
        inside_list: bool,
    ):
        """Check if it's a calculation"""
        if typ == "variable":
            calculations = self.choice_calculations
        else:
            calculations = self.family_calculations
        if inside_list:
            calculations = calculations[0]
        else:
            calculations = calculations[1]
        return (
            attribute in calculations
            and isinstance(value, dict)
            and value.get("type") in CALCULATION_TYPES
        )

    def set_calculation(
        self,
        obj: dict,
        attribute: str,
        value: dict,
        path: str,
        *,
        inside_list: bool = False,
        index: int = None,
    ):
        """This variable is a calculation"""
        calculation_object = value.copy()
        typ = calculation_object.pop("type")

        calculation_object["attribute_name"] = attribute
        calculation_object["path_prefix"] = self.path_prefix
        calculation_object["path"] = path
        calculation_object["inside_list"] = inside_list
        #
        if "params" in calculation_object:
            if not isinstance(calculation_object["params"], dict):
                raise Exception("params must be a dict")
            params = []
            for key, val in calculation_object["params"].items():
                if not isinstance(val, dict) or "type" not in val:
                    param_typ = "any"
                    val = {
                        "value": val,
                        "type": "any",
                    }
                else:
                    param_typ = val["type"]
                val["key"] = key
                try:
                    params.append(PARAM_TYPES[param_typ](**val))
                except ValidationError as err:
                    raise Exception(
                        f'"{attribute}" has an invalid "{key}" for {path}: {err}'
                    ) from err
            calculation_object["params"] = params
        #
        return_type = calculation_object.get("return_type")
        if return_type:
            if return_type not in self.variable_types:
                raise Exception(
                    f'unknown "return_type" in {attribute} of variable "{path}"'
                )
        #
        if index is None:
            obj[attribute] = CALCULATION_TYPES[typ](**calculation_object)
        if index is not None:
            obj[attribute][index] = CALCULATION_TYPES[typ](**calculation_object)


class RougailConvert(ParserVariable):
    """Main Rougail conversion"""

    supported_version = ["1.0"]

    def __init__(self, rougailconfig) -> None:
        self.annotator = False
        super().__init__(rougailconfig)

    def search_calculation(
        self,
        hint: dict,
    ) -> Tuple[List[Any], List[Any]]:
        """attribute is calculated if typing is like: Union[Calculation, xxx]"""
        inside_list = []
        outside_list = []
        for key, value in hint.items():
            if "Union" in value.__class__.__name__ and Calculation in value.__args__:
                outside_list.append(key)
            if (
                "Union" in value.__class__.__name__
                and "_GenericAlias" in value.__args__[0].__class__.__name__
                and Calculation in value.__args__[0].__args__
            ):
                inside_list.append(key)
            if (
                "Union" in value.__class__.__name__
                and value.__args__[0].__class__.__name__ == "_GenericAlias"
                and "Union" in value.__args__[0].__args__[0].__class__.__name__
                and Calculation in value.__args__[0].__args__[0].__args__
            ):
                inside_list.append(key)
        return inside_list, outside_list

    def parse_directories(
        self,
        path_prefix: Optional[str] = None,
    ) -> None:
        """Parse directories content"""
        self.init()
        if path_prefix:
            if path_prefix in self.parents:
                raise Exception("pfffff")
            root_parent = path_prefix
            self.path_prefix = path_prefix
            self.add_family(
                path_prefix,
                path_prefix,
                {},
                "",
                False,
            )
        else:
            root_parent = "."
        directory_dict = chain(
            (
                (
                    self.rougailconfig["variable_namespace"],
                    self.rougailconfig["dictionaries_dir"],
                ),
            ),
            self.rougailconfig["extra_dictionaries"].items(),
        )
        for namespace, extra_dirs in directory_dict:
            if root_parent == ".":
                namespace_path = namespace
            else:
                namespace_path = f"{root_parent}.{namespace}"
            if namespace_path in self.parents:
                raise Exception("pfff")
            for filename in self.get_sorted_filename(extra_dirs):
                self.parse_variable_file(
                    filename,
                    namespace,
                    namespace_path,
                )
        if path_prefix:
            self.path_prefix = None

    def parse_variable_file(
        self,
        filename: str,
        namespace: str,
        path: str,
    ) -> None:
        """Parse file"""
        with open(filename, encoding="utf8") as file_fh:
            objects = safe_load(file_fh)
        self.validate_file_version(
            objects,
            filename,
        )
        self.parse_family(
            filename,
            namespace,
            path,
            {},
        )
        for name, obj in objects.items():
            self.family_or_variable(
                filename,
                name,
                path,
                obj,
            )

    def get_sorted_filename(
        self,
        directories: Union[str, List[str]],
    ) -> Iterator[str]:
        """Sort filename"""
        if not isinstance(directories, list):
            directories = [directories]
        for directory_name in directories:
            directory = Path(directory_name)
            if not directory.is_dir():
                continue
            filenames = {}
            for file_path in directory.iterdir():
                if not file_path.suffix == ".yml":
                    continue
                if file_path.name in filenames:
                    raise DictConsistencyError(
                        _(f"duplicate dictionary file name {file_path.name}"),
                        78,
                        [filenames[file_path.name][1]],
                    )
                filenames[file_path.name] = str(file_path)
            for filename in sorted(filenames):
                yield filenames[filename]

    def validate_file_version(
        self,
        obj: dict,
        filename: str,
    ) -> None:
        """version is mandatory in YAML file"""
        if "version" not in obj:
            raise Exception(f'"version" attribut is mandatory in yaml file {filename}')
        version = obj.pop("version")
        if version not in self.supported_version:
            raise Exception(
                f"pffff version ... {version} not in {self.supported_version}"
            )

    def annotate(self):
        """Apply annotation"""
        if not self.paths.has_value():
            self.parse_directories()
        if self.annotator:
            raise DictConsistencyError(
                _("Cannot execute annotate multiple time"), 85, None
            )
        SpaceAnnotator(self)
        self.annotator = True

    def reflect(self) -> None:
        """Apply TiramisuReflector"""
        functions_file = self.rougailconfig["functions_file"]
        if not isinstance(functions_file, list):
            functions_file = [functions_file]
        functions_file = [
            func for func in functions_file if func not in self.exclude_imports
        ]
        self.reflector = TiramisuReflector(
            self,
            functions_file,
        )

    def save(
        self,
        filename: None,
    ):
        """Return tiramisu object declaration as a string"""
        self.annotate()
        self.reflect()
        output = self.reflector.get_text() + "\n"
        if filename:
            with open(filename, "w", encoding="utf-8") as tiramisu:
                tiramisu.write(output)
        #        print(output)
        return output
