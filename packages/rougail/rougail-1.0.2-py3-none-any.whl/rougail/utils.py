"""Rougail's tools

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
from typing import List, Union
from unicodedata import normalize, combining
import re

from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec

from jinja2 import DictLoader, TemplateSyntaxError
from jinja2.sandbox import SandboxedEnvironment
from jinja2.parser import Parser
from jinja2.nodes import Getattr

from .i18n import _
from .error import DictConsistencyError

NAME_REGEXP = re.compile(r"^[a-z0-9_]*$")


def valid_variable_family_name(
    name: str,
    xmlfiles: List[str],
) -> None:
    match = NAME_REGEXP.search(name)
    if not match:
        msg = _(
            f'invalid variable or family name "{name}" must only contains '
            "lowercase ascii character, number or _"
        )
        raise DictConsistencyError(msg, 76, xmlfiles)


def normalize_family(family_name: str) -> str:
    """replace space, accent, uppercase, ... by valid character"""
    if not family_name:
        return
    family_name = family_name.replace("-", "_").replace(" ", "_").replace(".", "_")
    nfkd_form = normalize("NFKD", family_name)
    family_name = "".join([c for c in nfkd_form if not combining(c)])
    return family_name.lower()


def load_modules(eosfunc_file) -> List[str]:
    """list all functions in eosfunc"""
    loader = SourceFileLoader("eosfunc", eosfunc_file)
    spec = spec_from_loader(loader.name, loader)
    eosfunc = module_from_spec(spec)
    loader.exec_module(eosfunc)
    return eosfunc


def get_realpath(
    path: str,
    path_prefix: str,
) -> str:
    if path_prefix:
        return f"{path_prefix}.{path}"
    return path


def get_jinja_variable_to_param(
    jinja_text,
    objectspace,
    xmlfiles,
    functions,
    path_prefix,
):
    try:
        env = SandboxedEnvironment(loader=DictLoader({"tmpl": jinja_text}))
        env.filters = functions
        parsed_content = Parser(env, jinja_text, "", "").parse()

        def recurse_getattr(g: Getattr):
            if isinstance(g.node, Getattr):
                return recurse_getattr(g.node) + "." + g.attr
            return g.node.name + "." + g.attr

        variables = set()
        for g in parsed_content.find_all(Getattr):
            variables.add(recurse_getattr(g))
    except TemplateSyntaxError as err:
        msg = _(f'error in jinja "{jinja_text}": {err}')
        raise Exception(msg) from err
    variables = list(variables)
    variables.sort()
    for variable_path in variables:
        variable, suffix, dynamic = objectspace.paths.get_with_dynamic(
            get_realpath(variable_path, path_prefix)
        )
        if variable and variable.path in objectspace.variables:
            yield variable, suffix, variable_path, dynamic
