"""Rougail method

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
from tiramisu import Config

from .convert import RougailConvert
from .config import RougailConfig
from .update import RougailUpgrade


def tiramisu_display_name(kls) -> str:
    """Replace the Tiramisu display_name function to display path + description"""
    doc = kls.impl_get_information("doc", None)
    comment = f" ({doc})" if doc and doc != kls.impl_getname() else ""
    return f"{kls.impl_getpath()}{comment}"


class Rougail:
    """Main Rougail object"""

    def __init__(
        self,
        rougailconfig = None,
    ) -> None:
        if rougailconfig is None:
            rougailconfig = RougailConfig
        self.rougailconfig = rougailconfig
        self.converted = RougailConvert(self.rougailconfig)
        self.config = None

    def add_path_prefix(
        self,
        path_prefix: str,
    ) -> None:
        """Add a prefix"""
        self.converted.parse_directories(path_prefix)

    def get_config(self):
        """Get Tiramisu Config"""
        if not self.config:
            tiram_obj = self.converted.save(self.rougailconfig["tiramisu_cache"])
            optiondescription = {}
            exec(tiram_obj, None, optiondescription)  # pylint: disable=W0122
            self.config = Config(
                optiondescription["option_0"],
                display_name=tiramisu_display_name,
            )
            self.config.property.read_write()
        return self.config


__ALL__ = ("Rougail", "RougailConvert", "RougailConfig", "RougailUpgrade")
