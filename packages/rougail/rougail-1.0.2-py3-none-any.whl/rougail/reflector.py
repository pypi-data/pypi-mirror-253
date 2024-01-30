"""load XML and YAML file from directory

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
from typing import List
from os.path import join, isfile
from os import listdir

from lxml.etree import DTD, parse, XMLSyntaxError  # pylint: disable=E0611
from pykwalify.compat import yml
from pykwalify.core import Core
from pykwalify.errors import SchemaError


from .i18n import _
from .error import DictConsistencyError


FORCE_SUBYAML = ["override"]
SCHEMA_DATA = {}


class Reflector:
    """Helper class for loading the Creole XML file,
    parsing it, validating against the Creole DTD
    """

    def __init__(
        self,
        rougailconfig: "RougailConfig",
    ) -> None:
        """Loads the Creole DTD

        :raises IOError: if the DTD is not found

        :param dtdfilename: the full filename of the Creole DTD
        """
        dtdfilename = rougailconfig["dtdfilename"]
        yamlschema_filename = rougailconfig["yamlschema_filename"]
        if not isfile(dtdfilename):
            raise IOError(_(f"no such DTD file: {dtdfilename}"))
        with open(dtdfilename, "r") as dtdfd:
            self.dtd = DTD(dtdfd)
        if not isfile(yamlschema_filename):
            raise IOError(_(f"no such YAML Schema file: {yamlschema_filename}"))
        self.yamlschema_filename = yamlschema_filename
        self.schema_data = None

    def load_dictionaries_from_folders(
        self,
        folders: List[str],
        just_doc: bool,
    ):
        """Loads all the dictionary files located in the folders' list

        :param folders: list of full folder's name
        """
        filenames = {}
        for folder in folders:
            for filename in listdir(folder):
                if filename.endswith(".xml"):
                    ext = "xml"
                    full_filename = join(folder, filename)
                elif filename.endswith(".yml"):
                    ext = "yml"
                    full_filename = join(folder, filename)
                else:
                    continue
                if filename in filenames:
                    raise DictConsistencyError(
                        _(f"duplicate dictionary file name {filename}"),
                        78,
                        [filenames[filename][1], full_filename],
                    )
                filenames[filename] = (ext, full_filename)
        if not filenames and not just_doc:
            raise DictConsistencyError(_("there is no dictionary file"), 77, folders)
        file_names = list(filenames.keys())
        file_names.sort()
        for filename in file_names:
            ext, filename = filenames[filename]
            if ext == "xml":
                yield self.load_xml_file(filename)
            else:
                yield self.load_yml_file(filename)

    def load_xml_file(
        self,
        filename: str,
    ):
        try:
            document = parse(filename)
        except XMLSyntaxError as err:
            raise DictConsistencyError(
                _(f"not a XML file: {err}"), 52, [filename]
            ) from err
        if not self.dtd.validate(document):
            dtd_error = self.dtd.error_log.filter_from_errors()[0]
            msg = _(f"not a valid XML file: {dtd_error}")
            raise DictConsistencyError(msg, 43, [filename])
        return filename, document.getroot()

    def load_yml_file(
        self,
        filename: str,
    ):
        global SCHEMA_DATA
        if self.yamlschema_filename not in SCHEMA_DATA:
            with open(self.yamlschema_filename, "r") as fh:
                SCHEMA_DATA[self.yamlschema_filename] = yml.load(fh)
        try:
            document = Core(
                source_file=filename,
                schema_data=SCHEMA_DATA[self.yamlschema_filename],
            )
        except XMLSyntaxError as err:
            raise DictConsistencyError(
                _(f"not a XML file: {err}"), 52, [filename]
            ) from err
        try:
            return filename, YParser(document.validate(raise_exception=True))
        except SchemaError as yaml_error:
            msg = _(f"not a valid YAML file: {yaml_error}")
            raise DictConsistencyError(msg, 43, [filename])


class SubYAML:
    def __init__(self, key, value):
        if value is None:
            value = {}
        self.tag = key
        self.dico = value
        if "text" in value:
            self.text = value["text"]
        else:
            self.text = None
        if isinstance(value, list):
            self.attrib = {}
        else:
            self.attrib = {
                k: v
                for k, v in value.items()
                if not isinstance(v, list) and k not in FORCE_SUBYAML
            }

    def __str__(self):
        return f"<SubYAML {self.tag} at {id(self)}>"

    def __iter__(self):
        if isinstance(self.dico, list):
            lists = []
            for dico in self.dico:
                for key, value in dico.items():
                    if not isinstance(value, list):
                        value = [value]
                    lists.append((key, value))
        else:
            lists = []
            for key, values in self.dico.items():
                if key == "variables":
                    for v in values:
                        if "variable" in v:
                            lists.append(("variable", v["variable"]))
                        if "family" in v:
                            lists.append(("family", v["family"]))
                else:
                    lists.append((key, values))
        for key, values in lists:
            if key not in FORCE_SUBYAML and not isinstance(values, list):
                continue
            if values is None:
                values = [None]
            for value in values:
                yield SubYAML(key, value)

    def __len__(self):
        length = 0
        for _ in self.__iter__():
            length += 1
        return length


class YParser:
    def __init__(self, dico):
        self.dico = dico

    def __iter__(self):
        for key, values in self.dico.items():
            if not isinstance(values, list):
                continue
            if key == "variables":
                yield SubYAML(key, values)
            else:
                for val in values:
                    yield SubYAML(key, val)
