"""Standard error classes

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
from .i18n import _


def display_xmlfiles(xmlfiles: list) -> str:
    """The function format xmlfiles informations to generate errors"""
    if len(xmlfiles) == 1:
        return '"' + xmlfiles[0] + '"'
    return '"' + '", "'.join(xmlfiles[:-1]) + '"' + " and " + '"' + xmlfiles[-1] + '"'


class ConfigError(Exception):
    """Standard error for templating"""


class FileNotFound(ConfigError):
    """Template file is not found"""


class TemplateError(ConfigError):
    """Templating generate an error"""


class TemplateDisabled(TemplateError):
    """Template is disabled."""


class SpaceObjShallNotBeUpdated(Exception):
    """Specific behavior in case of the presence or not
    of an object in the space object
    """


class DictConsistencyError(Exception):
    """It's not only that the Creole XML is valid against the Creole DTD
    it's that it is not consistent.
    """

    def __init__(self, msg, errno, xmlfiles):
        if xmlfiles:
            msg = _(f"{msg} in {display_xmlfiles(xmlfiles)}")
        super().__init__(msg)
        self.errno = errno


class UpgradeError(Exception):
    """Error during XML upgrade"""
