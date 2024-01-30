"""Redefine Tiramisu object

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
try:
    from tiramisu4 import DynOptionDescription
except ModuleNotFoundError:
    from tiramisu import DynOptionDescription
from .utils import normalize_family


class ConvertDynOptionDescription(DynOptionDescription):
    """Suffix could be an integer, we should convert it in str
    Suffix could also contain invalid character, so we should "normalize" it
    """

    def convert_suffix_to_path(self, suffix):
        if suffix is None:
            return suffix
        if not isinstance(suffix, str):
            suffix = str(suffix)
        return normalize_family(suffix)

    def impl_getname(
        self,
        suffix=None,
    ) -> str:
        """get name"""
        name = super().impl_getname(None)
        if suffix is None:
            return name
        path_suffix = self.convert_suffix_to_path(suffix)
        if "{{ suffix }}" in name:
            return name.replace("{{ suffix }}", path_suffix)
        return name + path_suffix
