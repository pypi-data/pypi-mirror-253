"""Annotate properties

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
from typing import Union
from rougail.i18n import _
from rougail.error import DictConsistencyError
from rougail.annotator.variable import Walk
from rougail.object_model import Calculation


PROPERTIES = (
    "hidden",
    "frozen",
    "force_default_on_freeze",
    "force_store_value",
    "disabled",
    "mandatory",
)


class Annotator(Walk):
    """Annotate properties"""

    level = 90

    def __init__(self, objectspace, *args) -> None:
        self.objectspace = objectspace
        self.frozen = {}
        if self.objectspace.paths:
            self.convert_family()
            self.convert_variable()

    def convert_family(self) -> None:
        """convert families"""
        for family in self.get_families():
            self._convert_property(family)
            # collect for force_default_on_freeze
            if family.hidden:
                self.set_variable_frozen(
                    family.path,
                    family.hidden,
                )

    def set_variable_frozen(
        self,
        family_path: str,
        hidden: Union[bool, Calculation],
    ) -> None:
        for variable_path in self.objectspace.parents[family_path]:
            if variable_path in self.objectspace.families:
                # it's a family
                self.set_variable_frozen(
                    variable_path,
                    hidden,
                )
            else:
                # it's a variable
                variable = self.objectspace.paths[variable_path]
                # if frozen is already true or hidden for variable is true => always frozen
                if (
                    self.frozen.get(variable.path) is True
                    or variable.hidden is True
                    or hidden is True
                ):
                    self.frozen[variable.path] = True
                elif variable.path in self.frozen:
                    self.frozen[variable.path].append(hidden)
                else:
                    self.frozen[variable.path] = [hidden]

    def convert_variable(self) -> None:
        """convert variables"""
        for variable in self.get_variables():
            if variable.path.startswith("services."):
                continue
            if variable.type == "symlink":
                continue
            self._convert_variable_property(variable)

    def _convert_variable_property(
        self,
        variable: dict,
    ) -> None:
        """convert properties"""
        path = variable.path
        self._convert_property(variable)
        if variable.hidden:
            if variable.hidden is True:
                self.frozen[variable.path] = True
            elif self.frozen.get(variable.path) is not True:
                self.frozen.setdefault(variable.path, []).append(variable.hidden)
        if variable.path in self.frozen:
            frozen = self.frozen[variable.path]
            if frozen is True:
                value = True
            else:
                value = []
                for calculation in frozen:
                    calculation_object = calculation.__class__
                    calculation_dict = calculation.model_dump().copy()
                    calculation_dict["attribute_name"] = "frozen"
                    calculation_dict["path"] = variable.path
                    value.append(calculation_object(**calculation_dict))
                if len(value) == 1:
                    value = value[0]
            self.objectspace.properties.add(path, "frozen", value)
            if not variable.auto_save:
                # if auto_save, save calculated value
                self.objectspace.properties.add(path, "force_default_on_freeze", True)
        if variable.mandatory and variable.multi:
            # a multi could not have "None" has value
            # to permit it, just add mandatory="False"
            self.objectspace.properties.add(path, "notempty", True)
        if variable.unique:
            self.objectspace.properties.add(path, "unique", True)
        if variable.unique is False:
            self.objectspace.properties.add(path, "notunique", True)
        if variable.auto_save:
            self.objectspace.properties.add(variable.path, "force_store_value", True)

    def _convert_property(
        self,
        obj: dict,
    ) -> None:
        for prop in PROPERTIES:
            if not hasattr(obj, prop):
                continue
            value = getattr(obj, prop)
            if not value:
                continue
            self.objectspace.properties.add(obj.path, prop, value)
        if obj.mode:
            self.objectspace.properties.add(obj.path, obj.mode, True)
