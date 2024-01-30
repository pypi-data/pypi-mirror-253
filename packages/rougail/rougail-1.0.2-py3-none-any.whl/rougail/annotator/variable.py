"""Annotate variable

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

from rougail.i18n import _
from rougail.error import DictConsistencyError
from rougail.object_model import Calculation


def convert_boolean(value: str) -> bool:
    """Boolean coercion. The Rougail XML may contain srings like `True` or `False`"""
    if isinstance(value, bool):
        return value
    value = value.lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    raise Exception(f"unknown boolean value {value}")


CONVERT_OPTION = {
    "string": dict(opttype="StrOption"),
    "number": dict(opttype="IntOption", func=int),
    "float": dict(opttype="FloatOption", func=float),
    "boolean": dict(opttype="BoolOption", func=convert_boolean),
    "secret": dict(opttype="PasswordOption"),
    "mail": dict(opttype="EmailOption"),
    "unix_filename": dict(opttype="FilenameOption"),
    "date": dict(opttype="DateOption"),
    "unix_user": dict(opttype="UsernameOption"),
    "ip": dict(opttype="IPOption", initkwargs={"allow_reserved": True}),
    "cidr": dict(opttype="IPOption", initkwargs={"cidr": True}),
    "netmask": dict(opttype="NetmaskOption"),
    "network": dict(opttype="NetworkOption"),
    "network_cidr": dict(opttype="NetworkOption", initkwargs={"cidr": True}),
    "broadcast": dict(opttype="BroadcastOption"),
    "netbios": dict(
        opttype="DomainnameOption",
        initkwargs={"type": "netbios", "warnings_only": True},
    ),
    "domainname": dict(
        opttype="DomainnameOption", initkwargs={"type": "domainname", "allow_ip": False}
    ),
    "hostname": dict(
        opttype="DomainnameOption", initkwargs={"type": "hostname", "allow_ip": False}
    ),
    "web_address": dict(
        opttype="URLOption", initkwargs={"allow_ip": False, "allow_without_dot": True}
    ),
    "port": dict(opttype="PortOption", initkwargs={"allow_private": True}),
    "mac": dict(opttype="MACOption"),
    "unix_permissions": dict(
        opttype="PermissionsOption", initkwargs={"warnings_only": True}, func=int
    ),
    "choice": dict(opttype="ChoiceOption"),
    #
    "symlink": dict(opttype="SymLinkOption"),
}


class Walk:
    """Walk to objectspace to find variable or family"""

    objectspace = None

    def get_variables(self):
        """Iter all variables from the objectspace"""
        for path in self.objectspace.variables:
            yield self.objectspace.paths[path]

    #        yield from get_variables(self.objectspace)

    def get_families(self):
        """Iter all families from the objectspace"""
        for path in self.objectspace.families:
            yield self.objectspace.paths[path]


class Annotator(Walk):  # pylint: disable=R0903
    """Annotate variable"""

    level = 30

    def __init__(
        self,
        objectspace,
        *args,
    ):
        if not objectspace.paths:
            return
        self.objectspace = objectspace
        self.forbidden_name = [
            "services",
            self.objectspace.rougailconfig["variable_namespace"],
        ]
        for extra in self.objectspace.rougailconfig["extra_dictionaries"]:
            self.forbidden_name.append(extra)
        self.convert_variable()
        self.convert_test()
        self.convert_help()

    def convert_variable(self):
        """convert variable"""
        for variable in self.get_variables():
            if variable.type == "symlink":
                continue
            self._convert_variable(variable)

    def _convert_variable(
        self,
        variable: dict,
    ) -> None:
        # variable without description: description is the name
        if not variable.description:
            variable.description = variable.name
        if variable.path in self.objectspace.followers:
            if not variable.multi:
                self.objectspace.multis[variable.path] = True
            else:
                self.objectspace.multis[variable.path] = "submulti"
        elif variable.multi:
            self.objectspace.multis[variable.path] = True
        if variable.path in self.objectspace.leaders:
            if not self.objectspace.multis.get(variable.path, False):
                msg = _(f'the variable "{variable.path}" in a leadership must be multi')
                raise DictConsistencyError(msg, 32, variable.xmlfiles)
            family = self.objectspace.paths[variable.path.rsplit(".", 1)[0]]
            if variable.hidden:
                family.hidden = variable.hidden
            elif family.hidden:
                variable.hidden = family.hidden
            variable.hidden = None

    def convert_test(self):
        """Convert variable tests value"""
        for variable in self.get_variables():
            if variable.test is None:
                # with we want remove test, we set "" has test value
                continue
            self.objectspace.informations.add(
                variable.path, "test", tuple(variable.test)
            )

    def convert_help(self):
        """Convert variable help"""
        for variable in self.get_variables():
            if not hasattr(variable, "help") or not variable.help:
                continue
            self.objectspace.informations.add(variable.path, "help", variable.help)
            del variable.help
