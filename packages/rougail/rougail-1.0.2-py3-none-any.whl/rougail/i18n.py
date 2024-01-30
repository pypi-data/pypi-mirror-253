"""Internationalisation utilities
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
import gettext
import os
import sys
import locale

# Application Name
APP_NAME = "rougail"

# Traduction dir
APP_DIR = os.path.join(sys.prefix, "share")
LOCALE_DIR = os.path.join(APP_DIR, "locale")

# Default Lanugage
DEFAULT_LANG = os.environ.get("LANG", "").split(":")
DEFAULT_LANG += ["en_US"]

languages = []
lc, encoding = locale.getlocale()
if lc:
    languages = [lc]

languages += DEFAULT_LANG
mo_location = LOCALE_DIR

gettext.find(APP_NAME, mo_location)
gettext.textdomain(APP_NAME)
# gettext.bind_textdomain_codeset(APP_NAME, "UTF-8")
# gettext.translation(APP_NAME, fallback=True)

t = gettext.translation(APP_NAME, fallback=True)

_ = t.gettext
