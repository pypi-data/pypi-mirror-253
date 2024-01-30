"""Annotate value

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
from rougail.annotator.variable import Walk

from rougail.i18n import _
from rougail.error import DictConsistencyError
from rougail.object_model import Calculation


class Annotator(Walk):  # pylint: disable=R0903
    """Annotate value"""

    level = 70

    def __init__(
        self,
        objectspace,
        *args,
    ) -> None:
        if not objectspace.paths:
            return
        self.objectspace = objectspace
        self.convert_value()
        self.add_choice_nil()

    def convert_value(self) -> None:
        """convert value"""
        for variable in self.get_variables():
            if variable.type == "symlink":
                continue
            self._convert_value(variable)

    def _convert_value(
        self,
        variable: dict,
    ) -> None:
        multi = self.objectspace.multis.get(variable.path, False)
        # a boolean must have value, the default value is "True"
        if variable.type == "boolean" and multi is False and variable.default is None:
            variable.default = True

        if variable.default is None:
            return
        has_value = False
        if isinstance(variable.default, Calculation):
            pass
        #            variable.default = variable.default.to_function(self.functions)
        elif isinstance(variable.default, list):
            if not multi:
                raise Exception(
                    f'The variable "{variable.path}" with a list has default value must have "multi" attribute'
                )
            if variable.path in self.objectspace.followers:
                if multi != "submulti" and len(variable.default) != 1:
                    msg = _(
                        f'the follower "{variable.name}" without multi attribute can only have one value'
                    )
                    raise DictConsistencyError(msg, 87, variable.xmlfiles)
            #            else:
            #                variable.default = [value.name for value in variable.default]
            if variable.path not in self.objectspace.leaders:
                if multi == "submulti":
                    self.objectspace.default_multi[
                        variable.path
                    ] = variable.default  # [value.name for value in variable.value]
                    variable.default = None
                else:
                    self.objectspace.default_multi[variable.path] = variable.default[
                        0
                    ]  # .name
            has_value = True
        elif variable.multi:
            # msg = _(f'the none multi variable "{variable.name}" cannot have '
            #        'more than one value')
            # raise DictConsistencyError(msg, 68, variable.xmlfiles)
            raise Exception("pfff")
        else:
            if variable.path in self.objectspace.followers:
                self.objectspace.default_multi[variable.path] = variable.default
                variable.default = None
            has_value = True

    def add_choice_nil(self) -> None:
        """A variable with type "Choice" that is not mandatory must has "nil" value"""
        for variable in self.get_variables():
            if variable.type != "choice":
                continue
            is_none = False
            if isinstance(variable.choices, Calculation):
                continue
            for choice in variable.choices:
                if choice is None:
                    is_none = True
                    break
            if not variable.mandatory and not is_none:
                variable.choices.append(None)
