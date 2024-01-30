"""Manage path to find objects

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
from typing import List
from .i18n import _
from .error import DictConsistencyError
from .utils import normalize_family


class Path:
    """Helper class to handle the `path` attribute.

    sample: path="creole.general.condition"
    """

    def __init__(
        self,
        rougailconfig: "RougailConfig",
    ) -> None:
        self.variables = {}
        self.families = {}
        # self.names = {}
        self.full_paths_families = {}
        self.full_paths_variables = {}
        self.full_dyn_paths_families = {}
        self.valid_enums = {}
        self.variable_namespace = rougailconfig["variable_namespace"]
        self.providers = {}
        self.suppliers = {}
        self.list_conditions = {}
        self.suffix = rougailconfig["suffix"]
        self.index = 0

    def set_path_prefix(self, prefix: str) -> None:
        self._path_prefix = prefix
        if prefix:
            if None in self.full_paths_families:
                raise DictConsistencyError(
                    _(f'prefix "{prefix}" cannot be set if a prefix "None" exists'),
                    39,
                    None,
                )
        else:
            for old_prefix in self.full_paths_families:
                if old_prefix != None:
                    raise DictConsistencyError(
                        _(f"no prefix cannot be set if a prefix exists"), 84, None
                    )
        if prefix in self.full_paths_families:
            raise DictConsistencyError(_(f'prefix "{prefix}" already exists'), 83, None)
        self.full_paths_families[prefix] = {}
        self.full_paths_variables[prefix] = {}
        self.valid_enums[prefix] = {}
        self.providers[prefix] = {}
        self.suppliers[prefix] = {}
        self.list_conditions[prefix] = {}

    def has_path_prefix(self) -> bool:
        return None not in self.full_paths_families

    def get_path_prefixes(self) -> list:
        return list(self.full_paths_families)

    def get_path_prefix(self) -> str:
        return self._path_prefix

    # Family
    def add_family(
        self,
        namespace: str,
        subpath: str,
        variableobj: str,
        is_dynamic: str,
        force_path_prefix: str = None,
    ) -> str:  # pylint: disable=C0111
        """Add a new family"""
        if force_path_prefix is None:
            force_path_prefix = self._path_prefix
        path = subpath + "." + variableobj.name
        if namespace == self.variable_namespace:
            if variableobj.name in self.full_paths_families[force_path_prefix]:
                msg = _(f'Duplicate family name "{variableobj.name}"')
                raise DictConsistencyError(msg, 55, variableobj.xmlfiles)
            self.full_paths_families[force_path_prefix][variableobj.name] = path
        if is_dynamic:
            if subpath in self.full_dyn_paths_families:
                dyn_subpath = self.full_dyn_paths_families[subpath]
            else:
                dyn_subpath = subpath
            self.full_dyn_paths_families[
                path
            ] = f"{dyn_subpath}.{variableobj.name}{{suffix}}"
        if path in self.families:
            msg = _(f'Duplicate family name "{path}"')
            raise DictConsistencyError(msg, 37, variableobj.xmlfiles)
        if path in self.variables:
            msg = _(f'A variable and a family has the same path "{path}"')
            raise DictConsistencyError(msg, 56, variableobj.xmlfiles)
        self.families[path] = dict(
            name=path,
            namespace=namespace,
            variableobj=variableobj,
        )
        self.set_name(variableobj, "optiondescription_")
        variableobj.path = path
        variableobj.path_prefix = force_path_prefix

    def get_family(
        self,
        path: str,
        current_namespace: str,
        path_prefix: str,
        allow_variable_namespace: bool = False,
    ) -> "Family":  # pylint: disable=C0111
        """Get a family"""
        if (
            current_namespace == self.variable_namespace or allow_variable_namespace
        ) and path in self.full_paths_families[path_prefix]:
            path = self.full_paths_families[path_prefix][path]
        elif allow_variable_namespace and path_prefix:
            path = f"{path_prefix}.{path}"
        if path not in self.families:
            raise DictConsistencyError(_(f'unknown option "{path}"'), 42, [])
        dico = self.families[path]
        if current_namespace != dico["namespace"] and (
            not allow_variable_namespace or current_namespace != self.variable_namespace
        ):
            msg = _(
                f'A family located in the "{dico["namespace"]}" namespace '
                f'shall not be used in the "{current_namespace}" namespace'
            )
            raise DictConsistencyError(msg, 38, [])
        return dico["variableobj"]

    def _get_dyn_path(
        self,
        subpath: str,
        name: bool,
    ) -> str:
        if subpath in self.full_dyn_paths_families:
            subpath = self.full_dyn_paths_families[subpath]
            path = f"{subpath}.{name}{{suffix}}"
        else:
            path = f"{subpath}.{name}"
        return path

    def set_provider(
        self,
        variableobj,
        name,
        family,
    ):
        if not hasattr(variableobj, "provider"):
            return
        p_name = "provider:" + variableobj.provider
        if "." in name:
            msg = f'provider "{p_name}" not allowed in extra'
            raise DictConsistencyError(msg, 82, variableobj.xmlfiles)
        if p_name in self.providers[variableobj.path_prefix]:
            msg = f'provider "{p_name}" declare multiple time'
            raise DictConsistencyError(msg, 79, variableobj.xmlfiles)
        self.providers[variableobj.path_prefix][p_name] = {
            "path": self._get_dyn_path(
                family,
                name,
            ),
            "option": variableobj,
        }

    def get_provider(
        self,
        name: str,
        path_prefix: str = None,
    ) -> "self.objectspace.variable":
        return self.providers[path_prefix][name]["option"]

    def get_providers_path(self, path_prefix=None):
        if path_prefix:
            return {
                name: option["path"].split(".", 1)[-1]
                for name, option in self.providers[path_prefix].items()
            }
        return {
            name: option["path"] for name, option in self.providers[path_prefix].items()
        }

    def set_supplier(
        self,
        variableobj,
        name,
        family,
    ):
        if not hasattr(variableobj, "supplier"):
            return
        s_name = "supplier:" + variableobj.supplier
        if "." in name:
            msg = f'supplier "{s_name}" not allowed in extra'
            raise DictConsistencyError(msg, 82, variableobj.xmlfiles)
        if s_name in self.suppliers[variableobj.path_prefix]:
            msg = f'supplier "{s_name}" declare multiple time'
            raise DictConsistencyError(msg, 79, variableobj.xmlfiles)
        self.suppliers[variableobj.path_prefix][s_name] = {
            "path": self._get_dyn_path(family, name),
            "option": variableobj,
        }

    def get_supplier(
        self,
        name: str,
        path_prefix: str = None,
    ) -> "self.objectspace.variable":
        return self.suppliers[path_prefix][name]["option"]

    def get_suppliers_path(self, path_prefix=None):
        if path_prefix:
            return {
                name: option["path"].split(".", 1)[-1]
                for name, option in self.suppliers[path_prefix].items()
            }
        return {
            name: option["path"] for name, option in self.suppliers[path_prefix].items()
        }

    # Variable
    def add_variable(
        self,  # pylint: disable=R0913
        namespace: str,
        subpath: str,
        variableobj: "self.objectspace.variable",
        is_dynamic: bool = False,
        is_leader: bool = False,
        force_path_prefix: str = None,
    ) -> str:  # pylint: disable=C0111
        """Add a new variable (with path)"""
        if force_path_prefix is None:
            force_path_prefix = self._path_prefix
        path = subpath + "." + variableobj.name
        if namespace == self.variable_namespace:
            self.full_paths_variables[force_path_prefix][variableobj.name] = path
        if path in self.families:
            msg = _(f'A family and a variable has the same path "{path}"')
            raise DictConsistencyError(msg, 57, variableobj.xmlfiles)
        if is_leader:
            leader = subpath
        else:
            leader = None
        self.variables[path] = dict(
            name=path,
            family=subpath,
            leader=leader,
            is_dynamic=is_dynamic,
            variableobj=variableobj,
        )
        variableobj.path = path
        variableobj.path_prefix = force_path_prefix
        self.set_name(variableobj, "option_")

    def set_name(
        self,
        variableobj,
        option_prefix,
    ):
        self.index += 1
        variableobj.reflector_name = f"{option_prefix}{self.index}{self.suffix}"

    def get_variable(
        self,
        name: str,
        namespace: str,
        xmlfiles: List[str] = [],
        allow_variable_namespace: bool = False,
        force_path_prefix: str = None,
        add_path_prefix: bool = False,
    ) -> "Variable":  # pylint: disable=C0111
        """Get variable object from a path"""
        if force_path_prefix is None:
            force_path_prefix = self._path_prefix
        try:
            variable, suffix = self._get_variable(
                name,
                namespace,
                with_suffix=True,
                xmlfiles=xmlfiles,
                path_prefix=force_path_prefix,
                add_path_prefix=add_path_prefix,
            )
        except DictConsistencyError as err:
            if (
                not allow_variable_namespace
                or err.errno != 42
                or namespace == self.variable_namespace
            ):
                raise err from err
            variable, suffix = self._get_variable(
                name,
                self.variable_namespace,
                with_suffix=True,
                xmlfiles=xmlfiles,
                path_prefix=force_path_prefix,
            )
        if suffix:
            raise DictConsistencyError(_(f"{name} is a dynamic variable"), 36, [])
        return variable["variableobj"]

    def get_variable_family_path(
        self,
        name: str,
        namespace: str,
        xmlfiles: List[str] = False,
        force_path_prefix: str = None,
    ) -> str:  # pylint: disable=C0111
        """Get the full path of a family"""
        if force_path_prefix is None:
            force_path_prefix = self._path_prefix
        return self._get_variable(
            name,
            namespace,
            xmlfiles=xmlfiles,
            path_prefix=force_path_prefix,
        )["family"]

    def get_variable_with_suffix(
        self,
        name: str,
        current_namespace: str,
        xmlfiles: List[str],
        path_prefix: str,
    ) -> str:  # pylint: disable=C0111
        """get full path of a variable"""
        try:
            dico, suffix = self._get_variable(
                name,
                current_namespace,
                with_suffix=True,
                xmlfiles=xmlfiles,
                path_prefix=path_prefix,
                add_path_prefix=True,
            )
        except DictConsistencyError as err:
            if err.errno != 42 or current_namespace == self.variable_namespace:
                raise err from err
            dico, suffix = self._get_variable(
                name,
                self.variable_namespace,
                with_suffix=True,
                xmlfiles=xmlfiles,
                path_prefix=path_prefix,
                add_path_prefix=True,
            )
        namespace = dico["variableobj"].namespace
        if (
            namespace not in [self.variable_namespace, "services"]
            and current_namespace != "services"
            and current_namespace != namespace
        ):
            msg = _(
                f'A variable located in the "{namespace}" namespace shall not be used '
                f'in the "{current_namespace}" namespace'
            )
            raise DictConsistencyError(msg, 41, xmlfiles)
        return dico["variableobj"], suffix

    def path_is_defined(
        self,
        path: str,
        namespace: str,
        force_path_prefix: str = None,
    ) -> str:  # pylint: disable=C0111
        """The path is a valid path"""
        if namespace == self.variable_namespace:
            if force_path_prefix is None:
                force_path_prefix = self._path_prefix
            return path in self.full_paths_variables[force_path_prefix]
        return path in self.variables

    def get_path(
        self,
        path: str,
        namespace: str,
    ) -> str:
        if namespace == self.variable_namespace:
            if path not in self.full_paths_variables[self._path_prefix]:
                return None
            path = self.full_paths_variables[self._path_prefix][path]
        else:
            path = f"{self._path_prefix}.{path}"
        return path

    def is_dynamic(self, variableobj) -> bool:
        """This variable is in dynamic family"""
        return self._get_variable(
            variableobj.path,
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )["is_dynamic"]

    def is_leader(self, variableobj):  # pylint: disable=C0111
        """Is the variable is a leader"""
        path = variableobj.path
        variable = self._get_variable(
            path,
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )
        if not variable["leader"]:
            return False
        leadership = self.get_family(
            variable["leader"],
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )
        return next(iter(leadership.variable.values())).path == path

    def is_follower(self, variableobj) -> bool:
        """Is the variable is a follower"""
        variable = self._get_variable(
            variableobj.path,
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )
        if not variable["leader"]:
            return False
        leadership = self.get_family(
            variable["leader"],
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )
        return next(iter(leadership.variable.values())).path != variableobj.path

    def get_leader(self, variableobj) -> str:
        variable = self._get_variable(
            variableobj.path,
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )
        if not variable["leader"]:
            raise Exception(f"cannot find leader for {variableobj.path}")
        leadership = self.get_family(
            variable["leader"],
            variableobj.namespace,
            path_prefix=variableobj.path_prefix,
        )
        return next(iter(leadership.variable.values()))

    def _get_variable(
        self,
        path: str,
        namespace: str,
        with_suffix: bool = False,
        xmlfiles: List[str] = [],
        path_prefix: str = None,
        add_path_prefix: bool = False,
    ) -> str:
        if namespace == self.variable_namespace:
            if path in self.full_paths_variables[path_prefix]:
                path = self.full_paths_variables[path_prefix][path]
            else:
                if with_suffix:
                    for var_name, full_path in self.full_paths_variables[
                        path_prefix
                    ].items():
                        if not path.startswith(var_name):
                            continue
                        variable = self._get_variable(
                            full_path, namespace, path_prefix=path_prefix
                        )
                        if not variable["is_dynamic"]:
                            continue
                        return variable, path[len(var_name) :]
                if path_prefix and add_path_prefix:
                    path = f"{path_prefix}.{path}"
        elif path_prefix and add_path_prefix:
            path = f"{path_prefix}.{path}"
        # FIXME with_suffix and variable in extra?
        if path not in self.variables:
            raise DictConsistencyError(_(f'unknown option "{path}"'), 42, xmlfiles)
        if with_suffix:
            return self.variables[path], None
        return self.variables[path]

    def set_valid_enums(
        self,
        path,
        values,
        path_prefix,
    ):
        self.valid_enums[path_prefix][path] = values

    def has_valid_enums(
        self,
        path: str,
        path_prefix: str,
    ) -> bool:
        return path in self.valid_enums[path_prefix]

    def get_valid_enums(
        self,
        path: str,
        path_prefix: str,
    ):
        return self.valid_enums[path_prefix][path]
