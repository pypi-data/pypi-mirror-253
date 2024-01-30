"""Annotate family

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
from rougail.i18n import _
from rougail.error import DictConsistencyError
from rougail.annotator.variable import Walk


class Mode:  # pylint: disable=R0903
    """Class to manage mode level"""

    def __init__(
        self,
        level: int,
    ) -> None:
        self.level = level

    def __gt__(
        self,
        other: int,
    ) -> bool:
        return other.level < self.level


class Annotator(Walk):
    """Annotate family"""

    level = 80

    def __init__(
        self,
        objectspace,
        *args,
    ):
        self.mode_auto = []
        self.objectspace = objectspace
        if not self.objectspace.paths:
            return
        self.modes = {
            name: Mode(idx)
            for idx, name in enumerate(self.objectspace.rougailconfig["modes_level"])
        }
        self.remove_empty_families()
        self.family_names()
        self.change_modes()
        self.dynamic_families()
        self.convert_help()

    def remove_empty_families(self) -> None:
        """Remove all families without any variable"""
        removed_families = []
        for family in self.get_families():
            if isinstance(family, self.objectspace.family) and not self._has_variable(
                family.path
            ):
                if "." in family.path:
                    removed_families.append(family.path)
        removed_families.reverse()
        for family in removed_families:
            self.objectspace.del_family(family)

    def _has_variable(
        self,
        family: str,
    ) -> bool:
        for variable in self.objectspace.parents[family]:
            if variable in self.objectspace.families:
                if self._has_variable(variable):
                    return True
            else:
                return True
        return False

    def family_names(self) -> None:
        """Set doc, path, ... to family"""
        for family in self.get_families():
            if not family.description:
                family.description = family.name

    #            family.doc = family.description
    #            del family.description

    def change_modes(self):
        """change the mode of variables"""
        modes_level = self.objectspace.rougailconfig["modes_level"]
        default_variable_mode = self.objectspace.rougailconfig["default_variable_mode"]
        if default_variable_mode not in modes_level:
            msg = _(
                f'default variable mode "{default_variable_mode}" is not a valid mode, '
                f"valid modes are {modes_level}"
            )
            raise DictConsistencyError(msg, 72, None)
        default_family_mode = self.objectspace.rougailconfig["default_family_mode"]
        if default_family_mode not in modes_level:
            msg = _(
                f'default family mode "{default_family_mode}" is not a valid mode, '
                f"valid modes are {modes_level}"
            )
            raise DictConsistencyError(msg, 73, None)
        families = list(self.get_families())
        for family in families:
            self.valid_mode(family)
            self._set_default_mode(family)
        families.reverse()
        for family in families:
            self._change_family_mode(family)

    def valid_mode(
        self,
        obj,
    ) -> None:
        modes_level = self.objectspace.rougailconfig["modes_level"]
        if self._has_mode(obj) and obj.mode not in modes_level:
            msg = _(
                f'mode "{obj.mode}" for "{obj.name}" is not a valid mode, '
                f"valid modes are {modes_level}"
            )
            raise DictConsistencyError(msg, 71, obj.xmlfiles)

    def _set_default_mode(
        self,
        family: "self.objectspace.family",
    ) -> None:
        children = self.objectspace.parents[family.path]
        if not children:
            return
        if self._has_mode(family):
            family_mode = family.mode
        else:
            family_mode = None
        leader = None
        for variable_path in children:
            variable = self.objectspace.paths[variable_path]
            if variable.type == "symlink":
                continue
            if leader is None and family.type == "leadership":
                leader = variable
            if variable_path in self.objectspace.families:
                # set default mode a subfamily
                if family_mode and not self._has_mode(variable):
                    self._set_auto_mode(variable, family_mode)
            else:
                # set default mode to a variable
                self.valid_mode(variable)
                if leader:
                    self._set_default_mode_leader(leader, variable)
                self._set_default_mode_variable(variable, family_mode)
        if leader:
            # here because follower can change leader mode
            self._set_auto_mode(family, leader.mode)

    def _has_mode(self, obj) -> bool:
        return obj.mode and not obj.path in self.mode_auto

    def _set_default_mode_variable(
        self,
        variable: "self.objectspace.variable",
        family_mode: Optional[str],
    ) -> None:
        # auto_save variable is set to 'basic' mode
        # if its mode is not defined by the user
        if not self._has_mode(variable) and variable.auto_save is True:
            variable.mode = self.objectspace.rougailconfig["modes_level"][0]
        # mandatory variable without value is a basic variable
        elif (
            not self._has_mode(variable)
            and variable.mandatory is True
            and variable.default is None
            and variable.path not in self.objectspace.default_multi
        ):
            variable_mode = self.objectspace.rougailconfig["modes_level"][0]
            if family_mode and self.modes[variable_mode] < self.modes[family_mode]:
                msg = _(
                    f'the variable "{variable.name}" is mandatory so in "{variable_mode}" mode '
                    f'but family has the higher family mode "{family_mode}"'
                )
                raise DictConsistencyError(msg, 36, variable.xmlfiles)

            variable.mode = variable_mode
        elif family_mode and not self._has_mode(variable):
            self._set_auto_mode(variable, family_mode)

    def _set_auto_mode(
        self,
        obj,
        mode: str,
    ) -> None:
        obj.mode = mode
        self.mode_auto.append(obj.path)

    def _set_default_mode_leader(
        self,
        leader: "self.objectspace.variable",
        follower: "self.objectspace.variable",
    ) -> None:
        if follower.auto_save is True:
            msg = _(f'leader/followers "{follower.name}" could not be auto_save')
            raise DictConsistencyError(msg, 29, follower.xmlfiles)
        if leader == follower:
            # it's a leader
            if not leader.mode:
                self._set_auto_mode(
                    leader, self.objectspace.rougailconfig["default_variable_mode"]
                )
            return
        if self._has_mode(follower):
            follower_mode = follower.mode
        else:
            follower_mode = self.objectspace.rougailconfig["default_variable_mode"]
        if self.modes[leader.mode] > self.modes[follower_mode]:
            if self._has_mode(follower) and not self._has_mode(leader):
                # if follower has mode but not the leader
                self._set_auto_mode(leader, follower_mode)
            else:
                # leader's mode is minimum level
                if self._has_mode(follower):
                    msg = _(
                        f'the follower "{follower.name}" is in "{follower_mode}" mode '
                        f'but leader have the higher mode "{leader.mode}"'
                    )
                    raise DictConsistencyError(msg, 63, follower.xmlfiles)
                self._set_auto_mode(follower, leader.mode)

    def _change_family_mode(
        self,
        family: "self.objectspace.family",
    ) -> None:
        if family.mode:
            family_mode = family.mode
        else:
            family_mode = self.objectspace.rougailconfig["default_family_mode"]
        min_variable_mode = self.objectspace.rougailconfig["modes_level"][-1]
        # change variable mode, but not if variables are not in a family
        is_leadership = family.type == "leadership"
        if family.path in self.objectspace.parents:
            for idx, variable_path in enumerate(self.objectspace.parents[family.path]):
                variable = self.objectspace.paths[variable_path]
                if variable.type == "symlink":
                    continue
                if variable_path in self.objectspace.families:
                    if not variable.mode:
                        variable.mode = self.objectspace.rougailconfig[
                            "default_family_mode"
                        ]
                else:
                    self._change_variable_mode(variable, family_mode, is_leadership)
                if self.modes[min_variable_mode] > self.modes[variable.mode]:
                    min_variable_mode = variable.mode
        if not family.mode:
            # set the lower variable mode to family
            self._set_auto_mode(family, min_variable_mode)

    def _change_variable_mode(
        self,
        variable,
        family_mode: str,
        is_follower: bool,
    ) -> None:
        if variable.mode:
            variable_mode = variable.mode
        else:
            variable_mode = self.objectspace.rougailconfig["default_variable_mode"]
        # none basic variable in high level family has to be in high level
        if not is_follower and self.modes[variable_mode] < self.modes[family_mode]:
            if self._has_mode(variable):
                msg = _(
                    f'the variable "{variable.name}" is in "{variable_mode}" mode '
                    f'but family has the higher family mode "{family_mode}"'
                )
                raise DictConsistencyError(msg, 61, variable.xmlfiles)
            self._set_auto_mode(variable, family_mode)
        if not variable.mode:
            variable.mode = variable_mode

    def dynamic_families(self):
        """link dynamic families to object"""
        for family in self.get_families():
            if family.type != "dynamic":
                continue
            try:
                family.variable = self.objectspace.paths[family.variable]
            except AttributeError as err:
                raise Exception(
                    f'cannot load the dynamic family "{family.path}", cannot find variable "{family.variable}"'
                )
            if not family.variable.multi:
                msg = _(
                    f'dynamic family "{family.name}" must be linked '
                    f"to multi variable"
                )
                raise DictConsistencyError(msg, 16, family.xmlfiles)
            for variable in self.objectspace.parents[family.path]:
                if (
                    isinstance(variable, self.objectspace.family)
                    and not variable.leadership
                ):
                    msg = _(
                        f'dynamic family "{family.name}" cannot contains another family'
                    )
                    raise DictConsistencyError(msg, 22, family.xmlfiles)

    def convert_help(self):
        """Convert variable help"""
        for family in self.get_families():
            if not family.help:
                continue
            self.objectspace.informations.add(family.path, "help", family.help)
            del family.help
