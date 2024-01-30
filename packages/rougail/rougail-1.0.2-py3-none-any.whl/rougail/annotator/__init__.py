"""Annotate dictionaries

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
from .variable import CONVERT_OPTION
import importlib.resources
from os.path import isfile
from ..utils import load_modules


ANNOTATORS = None
#
#
# if not 'files' in dir(importlib.resources):
#    # old python version
#    class fake_files:
#        def __init__(self, package):
#            self.mod = []
#            dir_package = dirname(importlib.resources._get_package(package).__file__)
#            for mod in importlib.resources.contents(package):
#                self.mod.append(join(dir_package, mod))
#
#        def iterdir(self):
#            return self.mod
#    importlib.resources.files = fake_files


def get_level(module):
    return module.level


def get_annotators(annotators, module_name):
    annotators[module_name] = []
    for pathobj in importlib.resources.files(module_name).iterdir():
        path = str(pathobj)
        if not path.endswith(".py") or path.endswith("__.py"):
            continue
        module = load_modules(path)
        if "Annotator" not in dir(module):
            continue
        annotators[module_name].append(module.Annotator)


class SpaceAnnotator:  # pylint: disable=R0903
    """Transformations applied on a object instance"""

    def __init__(
        self,
        objectspace,
    ):
        global ANNOTATORS
        if ANNOTATORS is None:
            ANNOTATORS = {}
            get_annotators(ANNOTATORS, "rougail.annotator")
        for extra_annotator in objectspace.rougailconfig["extra_annotators"]:
            if extra_annotator in ANNOTATORS:
                continue
            get_annotators(ANNOTATORS, extra_annotator)
        annotators = ANNOTATORS["rougail.annotator"].copy()
        for extra_annotator in objectspace.rougailconfig["extra_annotators"]:
            annotators.extend(ANNOTATORS[extra_annotator])
        annotators = sorted(annotators, key=get_level)
        functions = {}
        functions_files = objectspace.rougailconfig["functions_file"]
        if not isinstance(functions_files, list):
            functions_files = [functions_files]
        for functions_file in functions_files:
            if isfile(functions_file):
                loaded_modules = load_modules(functions_file)
                for function in dir(loaded_modules):
                    if function.startswith("_"):
                        continue
                    functions[function] = getattr(loaded_modules, function)
        objectspace.functions = functions
        for annotator in annotators:
            annotator(objectspace)


__all__ = ("SpaceAnnotator", "CONVERT_OPTION")
