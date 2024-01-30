"""Update Rougail XML file to new version

Cadoles (http://www.cadoles.com)
Copyright (C) 2021

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

from typing import List, Any, Optional, Tuple
from os.path import join, isfile, isdir, basename
from os import listdir, makedirs
try:
    from lxml.etree import parse, XMLParser, XMLSyntaxError  # pylint: disable=E0611
    from lxml.etree import Element, SubElement, tostring
except ModuleNotFoundError as err:
    parse = None

# from ast import parse as ast_parse
from json import dumps
from yaml import safe_load, dump, SafeDumper
from pathlib import Path

from .i18n import _
from .error import UpgradeError

from .utils import normalize_family
from .config import RougailConfig
from .annotator.variable import CONVERT_OPTION


VERSIONS = ["0.10", "1.0"]

FIXME_PRINT_FILENAME = True
FIXME_PRINT_FILENAME = False
FIXME_PRINT_FILE = True
FIXME_PRINT_FILE = False
FIXME_PRINT_UNKNOWN_VAR = True
FIXME_PRINT_UNKNOWN_VAR = False
FIXME_PRINT_REMOVE = True
FIXME_PRINT_REMOVE = False


def get_function_name(version):
    version = version.replace(".", "_")
    return f"update_{version}"


FUNCTION_VERSIONS = [(version, get_function_name(version)) for version in VERSIONS]


class NoAliasDumper(SafeDumper):
    def ignore_aliases(self, data):
        return True


class upgrade_010_to_100:
    def __init__(
        self,
        dico: dict,
        namespace: str,
        xmlsrc: str,
    ) -> None:
        if FIXME_PRINT_FILE:
            from pprint import pprint

            pprint(dico)
        self.xmlsrc = xmlsrc
        self.paths = {"family": {}, "variable": {}}
        self.lists = {
            "service": {},
            "ip": {},
            "certificate": {},
            "file": {},
        }
        self.flatten_paths = {"family": {}, "variable": {}}
        self.variables = self.parse_variables(dico, namespace)
        self.parse_variables_with_path()
        self.parse_services(dico)
        self.parse_constraints(dico)
        if FIXME_PRINT_FILE:
            print("==")
            pprint(self.variables)
            pprint(self.services)

    def parse_variables(
        self,
        family: dict,
        sub_path: str,
    ) -> dict:
        new_families = {}
        if "variables" in family:
            for subelt in family["variables"]:
                for typ, obj in subelt.items():
                    for subobj in obj:
                        getattr(self, f"convert_{typ}")(subobj, new_families, sub_path)
            family.pop("variables")
        return new_families

    def convert_family(
        self,
        family: dict,
        new_families: dict,
        sub_path: str,
    ) -> None:
        # name is the key, do not let it in values
        name = family.pop("name")
        if sub_path:
            sub_path = sub_path + "." + name
        else:
            sub_path = name
        # leadership and dynamic are no more attribute, it's now a type
        for typ in ["leadership", "dynamic"]:
            if typ in family:
                value = family.pop(typ)
                if value:
                    family["type"] = typ
                if typ == "dynamic":
                    family["variable"] = self.get_variable_path(value)
        # add sub families and sub variables
        sub_families = self.parse_variables(family, sub_path)
        for sub_name, sub_family in sub_families.copy().items():
            if sub_name not in family:
                continue
            family[f"_{sub_name}"] = family.pop(sub_name)
        # store converted family
        family.update(sub_families)
        new_families[name] = family
        self.flatten_paths["family"][name] = sub_path
        self.paths["family"][sub_path] = family

    def convert_variable(
        self,
        variable: dict,
        new_families: dict,
        sub_path: str,
    ) -> dict:
        name = variable.pop("name")
        if sub_path:
            sub_path = sub_path + "." + name
        else:
            sub_path = name
        new_families[name] = variable
        self.flatten_paths["variable"][name] = sub_path
        self.paths["variable"][sub_path] = variable
        if "redefine" not in variable and "value" not in variable and "mandatory" not in variable and ("type" not in variable or variable["type"] != "boolean"):
            variable["mandatory"] = False
        if "remove_condition" in variable and variable.pop("remove_condition"):
            if FIXME_PRINT_REMOVE:
                print(
                    f"variable {name} in file {self.xmlsrc} has remove_condition, all properties (hidden, disabled and mandatory) are set to False"
                )
            for prop in ["hidden", "disabled", "mandatory"]:
                if prop not in variable:
                    variable[prop] = False
        if "remove_choice" in variable:
            if "choice" not in variable:
                variable["choice"] = None
            variable.pop("remove_choice")
        if "remove_check" in variable:
            variable.pop("remove_check")
            if "validators" not in variable:
                variable["validators"] = None
        if "remove_fill" in variable:
            variable.pop("remove_fill")
            variable["value"] = None
        if "auto_freeze" in variable:
            variable.pop("auto_freeze")
        if "test" in variable:
            tests = []
            for test in variable["test"].split("|"):
                if test == "":
                    tests.append(None)
                else:
                    tests.append(
                        CONVERT_OPTION.get(variable.get("type", "string"), {}).get(
                            "func", str
                        )(test)
                    )
            variable["test"] = tests

    def parse_variables_with_path(self):
        for variable in self.paths["variable"].values():
            if "value" in variable:
                default = variable.pop("value")
                if default is not None:
                    if not variable.get("multi", False) and len(default) == 1:
                        variable["default"] = self.get_value(default[0])
                    else:
                        variable["default"] = [
                            self.get_value(value) for value in default
                        ]
            if "choice" in variable:
                if not variable["choice"]:
                    variable["choices"] = variable.pop("choice")
                else:
                    variable["choices"] = [
                        self.get_value(choice) for choice in variable.pop("choice")
                    ]

    def parse_services(
        self,
        dico: dict,
    ) -> None:
        self.services = {}
        if "services" in dico:
            for root_services in dico["services"]:
                for services in root_services.values():
                    for service in services:
                        new_service = {}
                        for typ in ["ip", "file", "certificate"]:
                            if typ != "ip":
                                typ_plurial = typ + "s"
                            else:
                                typ_plurial = typ
                            if typ in service:
                                new_service[typ_plurial] = {}
                                for elt in service[typ]:
                                    name, new_elt = getattr(self, f"parse_{typ}")(elt)
                                    new_service[typ_plurial][name] = new_elt
                        if "override" in service:
                            if isinstance(service["override"], list):
                                new_service["override"] = service["override"][0]
                            else:
                                new_service["override"] = service["override"]
                        if "servicelist" in service:
                            self.lists["service"].setdefault(
                                service["servicelist"], []
                            ).append(new_service)
                        name = (
                            service.pop("name") + "." + service.get("type", "service")
                        )
                        self.services[name] = new_service

    def parse_ip(self, ip: dict) -> None:
        name = self.get_variable_path(ip.pop("text"))
        if "iplist" in ip:
            self.lists["ip"].setdefault(ip.pop("iplist"), []).append(ip)
        if "netmask" in ip:
            ip["netmask"] = self.get_variable_path(ip["netmask"])
        return name, ip

    def parse_file(self, file: dict) -> None:
        name = file.pop("text")
        if "file_type" in file:
            file["type"] = file.pop("file_type")
            if file["type"] == "variable":
                name = self.get_variable_path(name)
        if "variable_type" in file:
            file.pop("variable_type")
        if "filelist" in file:
            self.lists["file"].setdefault(file.pop("filelist"), []).append(file)
        for typ in ["source", "owner", "group"]:
            if f"{typ}_type" in file:
                obj_type = file.pop(f"{typ}_type")
                if obj_type == "variable" and typ in file:
                    file[typ] = {
                        "name": self.get_variable_path(file[typ]),
                        "type": "variable",
                    }
        if "variable" in file:
            file["variable"] = self.get_variable_path(file["variable"])
        return name, file

    def parse_certificate(self, certificate: dict) -> None:
        name = certificate.pop("text")
        if "variable" in certificate:
            certificate["rougail_variable"] = certificate["variable"]
        if "certificate_type" in certificate:
            if certificate.pop("certificate_type") == "variable":
                certificate["variable"] = True
                name = self.get_variable_path(name)
        if "certificatelist" in certificate:
            self.lists["certificate"].setdefault(
                certificate.pop("certificatelist"), []
            ).append(certificate)
        for typ in ["owner", "group", "server", "domain", "provider"]:
            if f"{typ}_type" in certificate:
                obj_type = certificate.pop(f"{typ}_type")
                if obj_type == "variable" and typ in certificate:
                    certificate[typ] = {
                        "name": self.get_variable_path(certificate[typ]),
                        "type": "variable",
                    }
        return name, certificate

    def parse_constraints(
        self,
        dico: dict,
    ) -> None:
        if "constraints" not in dico:
            return
        for constraint in dico["constraints"]:
            if "condition" in constraint:
                for condition in constraint["condition"]:
                    self.parse_condition(condition)
            if "check" in constraint:
                for check in constraint["check"]:
                    self.parse_check(check)
            if "fill" in constraint:
                for fill in constraint["fill"]:
                    self.parse_fill(fill)

    def parse_condition(
        self,
        condition: dict,
    ) -> None:
        if "apply_on_fallback" in condition:
            apply_on_fallback = condition.pop("apply_on_fallback")
        else:
            apply_on_fallback = False
        source = self.get_variable_path(condition["source"])
        if not source:
            source = f'__{condition["source"]}'
        name = condition.pop("name")
        prop = name.split("_", 1)[0]
        if apply_on_fallback:
            condition_value = True
        else:
            condition_value = self.params_condition_to_jinja(
                source, condition["param"], name.endswith("if_in")
            )
        for target in condition["target"]:
            typ = target.get("type", "variable")
            if typ == "variable":
                variable_path = self.get_variable_path(target["text"])
                if variable_path is None:
                    if FIXME_PRINT_UNKNOWN_VAR and not target.get("optional", False):
                        print(
                            f'pffff la target {target["text"]} de la condition n\'est pas trouvable'
                        )
                    continue
                variable = self.paths["variable"][variable_path]
                variable[prop] = condition_value
            elif typ == "family":
                family_path = self.get_family_path(target["text"])
                if family_path is None:
                    if FIXME_PRINT_UNKNOWN_VAR and not target.get("optional", False):
                        print(
                            f'pffff la target {target["text"]} de la condition n\'est pas trouvable'
                        )
                    continue
                family = self.paths["family"][family_path]
                family[prop] = condition_value
            elif typ == "iplist":
                list_name = target["text"]
                if list_name in self.lists["ip"]:
                    for ip in self.lists["ip"].pop(list_name):
                        ip[prop] = condition_value
            elif typ == "filelist":
                list_name = target["text"]
                if list_name in self.lists["file"]:
                    for ip in self.lists["file"].pop(list_name):
                        ip[prop] = condition_value
            elif typ == "servicelist":
                list_name = target["text"]
                if list_name in self.lists["service"]:
                    for service in self.lists["service"].pop(list_name):
                        service[prop] = condition_value
            elif typ == "certificatelist":
                list_name = target["text"]
                if list_name in self.lists["certificate"]:
                    for certificat in self.lists["certificate"].pop(list_name):
                        certificat[prop] = condition_value

    def parse_check(
        self,
        check: dict,
    ) -> None:
        for target in check["target"]:
            variable_path = self.get_variable_path(target["text"])
            if variable_path is None:
                if FIXME_PRINT_UNKNOWN_VAR and not target.get("optional", False):
                    print(
                        f'pffff la target {target["text"]} dans le check n\'est pas trouvable'
                    )
                continue
            variable = self.paths["variable"][variable_path]
            if "validators" in variable and variable["validators"] is None:
                variable.pop("validators")
            if check.get("type") == "jinja":
                check_value = check["name"]
            else:
                check["param"] = [
                    {"text": variable_path, "type": "variable"}
                ] + check.get("param", [])
                check_value = self.convert_param_function(check)
            variable.setdefault("validators", []).append(check_value)

    def parse_fill(
        self,
        fill: dict,
    ) -> None:
        for target in fill.pop("target"):
            params = []
            variable_path = self.get_variable_path(target["text"])
            if variable_path is None:
                if FIXME_PRINT_UNKNOWN_VAR and not target.get("optional", False):
                    print(
                        f'pffff la target {target["text"]} dans le fill n\'est pas trouvable'
                    )
                continue
            variable = self.paths["variable"][variable_path]
            if fill.get("type") == "jinja":
                fill_value = {
                    "type": "jinja",
                    "jinja": fill["name"],
                }
            else:
                fill_value = self.convert_param_function(fill)
            variable["default"] = fill_value

    def params_condition_to_jinja(
        self,
        path: str,
        params: List[dict],
        if_in: bool,
    ) -> str:
        new_params = {}
        jinja = "{% if "
        for idx, param in enumerate(params):
            if idx:
                jinja += " or "

            new_param, value = self.get_jinja_param_and_value(param)
            if value:
                jinja += path + " == " + value
            if new_param:
                new_params |= new_param
        if if_in:
            jinja += " %}true{% else %}false{% endif %}"
        else:
            jinja += " %}false{% else %}true{% endif %}"
        ret = {
            "type": "jinja",
            "jinja": jinja,
        }
        if new_params:
            ret["params"] = new_params
        return ret

    def get_value(
        self,
        param: dict,
    ) -> Any:
        # <!ATTLIST type (string|number|nil|space|boolean|variable|function|information|suffix|index) "string">
        typ = param.get("type", "string")
        if typ == "string":
            value = param["text"]
        #            value = dumps(value, ensure_ascii=False)
        elif typ == "number":
            value = int(param["text"])
        elif typ == "nil":
            value = None
        elif typ == "space":
            value = " "
        elif typ == "boolean":
            value = param["text"]
        elif typ == "variable":
            variable_path = self.get_variable_path(param["text"])
            if variable_path is None:
                variable_path = "__" + param["text"]
            value = {
                "type": "variable",
                "variable": variable_path,
            }
            if "optional" in param:
                value["optional"] = param["optional"]
            if "propertyerror" in param:
                value["propertyerror"] = param["propertyerror"]
        elif typ == "function":
            value = self.convert_param_function(param)
        elif typ == "information":
            value = {
                "type": "information",
                "information": param["text"],
            }
            if "variable" in param:
                variable_path = self.get_variable_path(param["variable"])
                value["variable"] = variable_path
        elif typ == "suffix":
            value = param
        elif typ == "index":
            value = param
        return value

    def get_jinja_param_and_value(
        self,
        param,
    ) -> Tuple[list, Any]:
        new_param = None
        typ = param.get("type", "string")
        value = self.get_value(param)
        if isinstance(value, dict):
            if typ == "information":
                key = normalize_family(value["information"])
                if "variable" in value:
                    attr_name = f'{value["variable"]}.{key}'
                else:
                    attr_name = key
                attr_name = f"__information.{attr_name}"
                new_param = {attr_name: value}
                value = attr_name
            elif typ in ["index", "suffix"]:
                attr_name = f"__{typ}"
                new_param = {attr_name: value}
                value = attr_name
            elif "propertyerror" in param or "optional" in param:
                attr_name = value["variable"]
                new_param = {attr_name: value}
                value = value[typ]
            else:
                value = value[typ]
            if not value:
                return
        else:
            value = dumps(value, ensure_ascii=False)
        return new_param, value

    def convert_param_function(
        self,
        param: dict,
    ) -> str:
        text = param["name"]
        params = {}
        if "param" in param and param["param"]:
            first, *others = param["param"]
            new_param, first = self.get_jinja_param_and_value(first)
            text = f"{first} | {text}"
            if new_param:
                params |= new_param
            if others:
                values = []
                for param in others:
                    new_param, value = self.get_jinja_param_and_value(param)
                    if new_param:
                        params |= new_param
                    #                    if param.get('type') != 'variable' or value is not None:
                    if "name" in param:
                        values.append(f'{param["name"]}={value}')
                    else:
                        values.append(value)
                text += "("
                text += ", ".join(values)
                text += ")"
        else:
            text += "()"
        text = "{{ " + text + " }}"
        ret = {"type": "jinja", "jinja": text}
        if params:
            ret["params"] = params
        return ret

    def get_variable_path(
        self,
        path: str,
    ) -> dict:
        if (
            path not in self.paths["variable"]
            and path in self.flatten_paths["variable"]
        ):
            path = self.flatten_paths["variable"][path]
        if path not in self.paths["variable"]:
            if FIXME_PRINT_UNKNOWN_VAR:
                print("pffff impossible de trouver la variable", path)
            return
        return path

    def get_family_path(
        self,
        path: str,
    ) -> dict:
        if path not in self.paths["family"] and path in self.flatten_paths["family"]:
            path = self.flatten_paths["family"][path]
        if path not in self.paths["family"]:
            if FIXME_PRINT_UNKNOWN_VAR:
                print("pffff impossible de trouver la famille", path)
            return
        return path

    def get(self) -> dict:
        return self.variables, self.services


class RougailUpgrade:
    def __init__(
        self,
        test=False,
        upgrade_help=None,
        rougailconfig: RougailConfig = None,
    ) -> None:
        self.test = test
        if upgrade_help is None:
            upgrade_help = {}
        self.upgrade_help = upgrade_help
        if rougailconfig is None:
            rougailconfig = RougailConfig
        self.rougailconfig = rougailconfig

    def load_dictionaries(
        self,
        #                          srcfolder: str,
        dstfolder: str,
        services_dstfolder: Optional[str],
        extra_dstfolder: Optional[str] = None,
        #                          namespace: str,
        #                          display: bool=True,
    ):
        if extra_dstfolder is None:
            extra_dstfolder = dstfolder
        self._load_dictionaries(
            self.rougailconfig["dictionaries_dir"],
            dstfolder,
            services_dstfolder,
            self.rougailconfig["variable_namespace"],
        )
        for namespace, extra_dirs in self.rougailconfig["extra_dictionaries"].items():
            extra_dstsubfolder = join(extra_dstfolder, namespace)
            if not isdir(extra_dstsubfolder):
                makedirs(extra_dstsubfolder)
            for extra_dir in extra_dirs:
                self._load_dictionaries(
                    extra_dir,
                    extra_dstsubfolder,
                    None,
                    namespace,
                )

    def _load_dictionaries(
        self,
        srcfolder: str,
        dstfolder: str,
        services_dstfolder: Optional[str],
        namespace: str,
    ) -> None:
        filenames = [
            filename
            for filename in listdir(srcfolder)
            if filename.endswith(".xml") or filename.endswith(".yml")
        ]
        filenames.sort()
        for filename in filenames:
            xmlsrc = Path(srcfolder) / Path(filename)
            ymlfile = filename[:-3] + "yml"
            xmldst = Path(dstfolder) / Path(ymlfile)
            if xmldst.is_file():
                raise Exception(
                    f'cannot update "{xmlsrc}" destination file "{xmldst}" already exists'
                )
            if services_dstfolder:
                ymldst_services = Path(services_dstfolder) / ymlfile
                if ymldst_services.is_file():
                    raise Exception(
                        f'cannot update "{xmlsrc}" destination file "{ymldst_services}" already exists'
                    )
            if filename.endswith(".xml"):
                if parse is None:
                    raise Exception('XML module is not installed')
                try:
                    parser = XMLParser(remove_blank_text=True)
                    document = parse(xmlsrc, parser)
                except XMLSyntaxError as err:
                    raise Exception(_(f"not a XML file: {err}")) from err
                root = document.getroot()
                search_function_name = get_function_name(
                    root.attrib.get("version", "1")
                )
                ext = "xml"
            else:
                with xmlsrc.open() as xml_fh:
                    root = safe_load(xml_fh)
                search_function_name = get_function_name(root["version"])
                ext = "yml"
            function_found = False
            if FIXME_PRINT_FILENAME:
                print(
                    "========================================================================"
                )
                print(xmlsrc)
                print(
                    "========================================================================"
                )
            for version, function_version in FUNCTION_VERSIONS:
                if function_found and hasattr(self, function_version):
                    #                    if display:
                    #                        print(f'  - convert {filename} to version {version}')
                    upgrade_help = self.upgrade_help.get(function_version, {}).get(
                        filename, {}
                    )
                    if upgrade_help.get("remove") is True:
                        continue
                    root, root_services, new_type = getattr(self, function_version)(
                        root, upgrade_help, namespace, xmlsrc, ext
                    )
                if function_version == search_function_name:
                    function_found = True
            if root:
                root["version"] = version
                xmldst.parent.mkdir(parents=True, exist_ok=True)
                with xmldst.open("w") as ymlfh:
                    dump(
                        root,
                        ymlfh,
                        allow_unicode=True,
                        sort_keys=False,
                        Dumper=NoAliasDumper,
                    )
            if root_services and services_dstfolder:
                root_services["version"] = version
                ymldst_services.parent.mkdir(parents=True, exist_ok=True)
                with ymldst_services.open("w") as ymlfh:
                    dump(
                        root_services,
                        ymlfh,
                        allow_unicode=True,
                        sort_keys=False,
                        Dumper=NoAliasDumper,
                    )

    #            if not self.dtd.validate(document):
    #                dtd_error = self.dtd.error_log.filter_from_errors()[0]
    #                msg = _(f'not a valid XML file: {dtd_error}')
    #                raise DictConsistencyError(msg, 43, [xmlfile])
    #            yield xmlfile, document.getroot()

    def _attribut_to_bool(self, variable):
        for prop in [
            "mandatory",
            "hidden",
            "redefine",
            "multi",
            "leadership",
            "optional",
            "unique",
            "auto_save",
            "remove_check",
            "manage",
            "exists",
            "disabled",
            "undisable",
            "remove_choice",
            "propertyerror",
            "apply_on_fallback",
            "remove_fill",
            "remove_condition",
        ]:
            if prop in variable:
                variable[prop] = {"True": True, "False": False}[variable[prop]]

    def _attribut_to_int(self, variable):
        for prop in ["mode"]:
            if prop in variable:
                if variable[prop] in ['expert', 'normal']:
                    variable[prop] = {'expert': 'advanced',
                                      'normal': 'standard',
                                      }.get(variable[prop])
                    continue
                try:
                    variable[prop] = int(variable[prop])
                except ValueError:
                    pass

    def _xml_to_yaml(
        self,
        objects,
        obj_name,
        variables,
        path,
        variable_type="string",
        variable_choices=[],
    ):
        if obj_name in ["variables", "family"]:
            dico = []
        else:
            dico = {}
        for obj in objects:
            obj_type = obj.tag
            if not isinstance(obj_type, str):
                # doesn't proceed the XML commentaries
                continue
            new_dico = dict(obj.attrib)
            if obj_type in ["variable", "family"]:
                if path:
                    path += "." + obj.attrib["name"]
                else:
                    path = obj.attrib["name"]
            choices = []
            if obj_type == "variable":
                var_type = obj.attrib.get("type", "string")
                variables[obj.attrib["name"]] = {"type": var_type}
                variables[path] = {"type": var_type}
            elif obj_type == "condition":
                var_type = variables.get(obj.attrib["source"], {}).get("type", "string")
                if var_type == "choice":
                    choices = variables.get(obj.attrib["source"], {}).get("choices", [])
            else:
                var_type = None
            new_objects = self._xml_to_yaml(
                obj, obj.tag, variables, path, var_type, choices
            )
            if obj.text:
                text = obj.text
                if isinstance(text, str):
                    text = text.strip()
                if text:
                    if obj_type in ["choice", "value"]:
                        value_type = obj.attrib.get("type")
                        if not value_type and obj_type == "value":
                            value_type = variable_type
                        text = CONVERT_OPTION.get(value_type, {}).get("func", str)(text)
                        if obj_type == "choice":
                            variables[path.rsplit(".", 1)[-1]].setdefault(
                                "choices", []
                            ).append({"type": value_type, "value": text})
                            variables[path].setdefault("choices", []).append(
                                {"type": value_type, "value": text}
                            )
                    if obj_type in ["param", "value"]:
                        if obj.attrib.get("type") == "variable":
                            var_type = variables.get(obj.attrib.get("name"), {}).get(
                                "type", "string"
                            )
                            value_type = obj.attrib.get("type", var_type)
                            text = CONVERT_OPTION.get(value_type, {}).get("func", str)(
                                text
                            )
                        elif "type" in obj.attrib:
                            var_type = obj.attrib.get("type")
                            text = CONVERT_OPTION.get(var_type, {}).get("func", str)(
                                text
                            )
                        elif obj_type == "param" and variable_type:
                            if variable_type == "choice":
                                for choice in variable_choices:
                                    if choice["value"] == CONVERT_OPTION.get(
                                        choice.get("type"), {}
                                    ).get("func", str)(text):
                                        text = choice["value"]
                                        break
                            else:
                                text = CONVERT_OPTION.get(variable_type, {}).get(
                                    "func", str
                                )(text)
                    new_dico["text"] = text
            if isinstance(new_objects, list):
                if new_objects:
                    for new_obj in new_objects:
                        new_dico.update(new_obj)
            elif new_objects is not None and list(new_objects.values())[0]:
                new_dico.update(new_objects)
            self._attribut_to_bool(new_dico)
            self._attribut_to_int(new_dico)
            if not new_dico:
                new_dico = None
            if obj_type == "override" and not new_dico:
                new_dico = None
            if isinstance(dico, list):
                if dico and obj_type in dico[-1]:
                    dico[-1][obj_type].append(new_dico)
                else:
                    dico.append({obj_type: [new_dico]})
            elif new_dico is None:
                dico[obj_type] = new_dico
            else:
                dico.setdefault(obj_type, []).append(new_dico)
        if dico == {}:
            dico = None
        elif isinstance(dico, dict):
            dico = [dico]
        if obj_name in ["service", "condition", "fill", "choice", "check"]:
            pass
        elif obj_name in ["variables", "family"]:
            dico = {"variables": dico}
        elif obj_name != "variable":
            dico = {obj_name: dico}
        return dico

    def update_1_0(
        self,
        root: "Element",
        upgrade_help: dict,
        namespace: str,
        xmlsrc: str,
        ext: str,
    ) -> "Element":
        if ext == "xml":
            new_root = {"version": root.attrib["version"]}
            variables = {}
            for typ in ["services", "variables", "constraints"]:
                objects = root.find(typ)
                if objects is None:
                    objects = []
                new_objects = self._xml_to_yaml(objects, typ, variables, "")
                if new_objects[typ]:
                    new_root.update(new_objects)
        #            services = root.find('services')
        #            if services is None:
        #                services = []
        #            new_services = self._xml_to_yaml_service(services)
        #            if new_services:
        #                new_root['services'] = new_services
        #        paths = self._get_path_variables(variables,
        #                                         namespace == 'configuration',
        #                                         namespace,
        #                                         )
        else:
            new_root = root
        variables, services = upgrade_010_to_100(new_root, namespace, xmlsrc).get()
        return variables, services, "yml"

    def update_0_10(
        self,
        root: "Element",
        upgrade_help: dict,
        namespace: str,
        xmlsrc: str,
        ext: str,
    ) -> "Element":
        variables = root.find("variables")
        if variables is None:
            return root
        paths = self._get_path_variables(
            variables,
            namespace == "configuration",
            namespace,
        )
        constraints = root.find("constraints")
        # convert schedule and schedulemod
        for variable in paths.values():
            variable = variable["variable"]
            if variable.tag != "variable":
                continue
            if "type" in variable.attrib and variable.attrib["type"] in [
                "schedule",
                "schedulemod",
            ]:
                if variable.attrib["type"] == "schedule":
                    choices = ("none", "daily", "weekly", "monthly")
                else:
                    choices = ("pre", "post")
                variable.attrib["type"] = "choice"
                has_value = False
                for value in variable:
                    if value.tag == "value":
                        has_value = True
                        break
                for name in choices:
                    choice = SubElement(variable, "choice")
                    choice.text = name
                if not has_value:
                    value = SubElement(variable, "value")
                    value.text = choices[0]
                variable.attrib["mandatory"] = "True"

        # convert group to leadership
        groups = []
        if constraints is not None:
            for constraint in constraints:
                if constraint.tag == "group":
                    constraints.remove(constraint)
                    groups.append(constraint)
        for group in groups:
            if group.attrib["leader"] in paths:
                leader_obj = paths[group.attrib["leader"]]
                # FIXME name peut avoir "." il faut le virer
                # FIXME si extra c'est un follower !
                if "name" in group.attrib:
                    grpname = group.attrib["name"]
                    if "description" in group.attrib:
                        description = group.attrib["description"]
                    else:
                        description = grpname
                else:
                    grpname = leader_obj["variable"].attrib["name"]
                    if "." in grpname:
                        grpname = grpname.rsplit(".", 1)[-1]
                    if "description" in group.attrib:
                        description = group.attrib["description"]
                    elif "description" in leader_obj["variable"].attrib:
                        description = leader_obj["variable"].attrib["description"]
                    else:
                        description = grpname
                family = SubElement(
                    leader_obj["parent"],
                    "family",
                    name=grpname,
                    description=description,
                    leadership="True",
                )
                leader_obj["parent"].remove(leader_obj["variable"])
                family.append(leader_obj["variable"])
            else:
                # append in group
                follower = next(iter(group))
                leader_name = group.attrib["leader"]
                if "." in leader_name:
                    leader_path = leader_name.rsplit(".", 1)[0]
                    follower_path = leader_path + "." + follower.text
                else:
                    follower_path = follower.text
                obj = paths[follower_path]
                family = SubElement(
                    obj["parent"], "family", name=leader_name, leadership="True"
                )
                grpname = leader_name
            for follower in group:
                leader_name = group.attrib["leader"]
                if "." in leader_name:
                    leader_path = leader_name.rsplit(".", 1)[0]
                    follower_path = leader_path + "." + follower.text
                else:
                    follower_path = follower.text
                follower_obj = paths[follower_path]
                follower_obj["parent"].remove(follower_obj["variable"])
                family.append(follower_obj["variable"])
                if "." in follower_path:
                    new_path = (
                        follower_path.rsplit(".", 1)[0]
                        + "."
                        + grpname
                        + "."
                        + follower_path.rsplit(".", 1)[1]
                    )
                    paths[new_path] = paths[follower_path]

        # convert choice option
        valid_enums = []
        if constraints is not None:
            for constraint in constraints:
                if (
                    constraint.tag == "check"
                    and constraint.attrib["name"] == "valid_enum"
                ):
                    constraints.remove(constraint)
                    valid_enums.append(constraint)
        for valid_enum in valid_enums:
            targets = []
            for target in valid_enum:
                if target.tag != "target":
                    continue
                if target.text in paths:
                    # not in paths if it's optional
                    # but not check it
                    targets.append(paths[target.text]["variable"])
            params = []
            function_param = None
            for param in valid_enum:
                if param.tag != "param":
                    continue
                if "type" in param.attrib and param.attrib["type"] == "function":
                    function_param = param.text
                    continue
                params.append(param)
            first_choice = None
            for target in targets:
                if function_param is not None:
                    function = SubElement(
                        target, "choice", type="function", name=function_param
                    )
                for param in params:
                    if function_param is not None:
                        function.append(param)
                    else:
                        choice = SubElement(target, "choice")
                        if first_choice is None and (
                            "type" not in param.attrib
                            or param.attrib["type"] != "variable"
                        ):
                            first_choice = choice
                        choice.text = param.text
                        if "type" not in param.attrib and param.text is None:
                            choice_type = "nil"
                        elif "type" in param.attrib:
                            choice_type = param.attrib["type"]
                        elif "type" in target.attrib:
                            choice_type = target.attrib["type"]
                        else:
                            choice_type = "string"
                        choice.attrib["type"] = choice_type
            has_value = False
            for target in targets:
                if "remove_check" in target.attrib:
                    target.attrib["remove_choice"] = target.attrib["remove_check"]
            for target in targets:
                for value in target:
                    if value.tag == "value":
                        has_value = True
                        if "type" in target.attrib:
                            value.attrib["type"] = target.attrib["type"]
            if first_choice is not None and not has_value:
                value = SubElement(target, "value")
                value.attrib["type"] = first_choice.attrib["type"]
                value.text = first_choice.text
            for target in targets:
                if (
                    "remove_choice" not in target.attrib
                    or target.attrib["remove_choice"] != "True"
                ):
                    target.attrib["type"] = "choice"
        return root, None, "xml"

    def _get_path_variables(self, variables, is_variable_namespace, path, dico=None):
        if dico is None:
            dico = {}
        for variable in variables:
            if not is_variable_namespace and path:
                subpath = path + "."
            else:
                subpath = ""
            if variable.tag not in ["variable", "family"]:
                continue
            subpath += variable.attrib["name"]
            if variable.tag == "family":
                self._get_path_variables(variable, is_variable_namespace, subpath, dico)
            elif variable.tag == "variable":
                dico[subpath] = {"variable": variable, "parent": variables}
        return dico

    @staticmethod
    def move(elt, src, dst, optional=False):
        if src == "text":
            value = elt.text
            elt.text = None
        else:
            if optional and src not in elt.attrib:
                return
            value = elt.attrib[src]
            del elt.attrib[src]
        #
        if dst == "text":
            elt.text = value
        else:
            elt.attrib[dst] = value

    @staticmethod
    def remove(elt, src, optional=False):
        if optional and src not in elt.attrib:
            return
        del elt.attrib[src]

    @staticmethod
    def create_service(services, service_name, service_elt, servicelists, upgrade_help):
        if service_name in service_elt:
            return service_elt[service_name]
        service = SubElement(services, "service")
        service.attrib["name"] = service_name
        if service_name == "unknown":
            service.attrib["manage"] = "False"
        if service_name in upgrade_help.get("services", {}).get("unmanage", []):
            service.attrib["manage"] = "False"
        service_elt[service_name] = service
        if upgrade_help.get("servicelists", {}).get(service_name):
            service.attrib["servicelist"] = upgrade_help.get("servicelists", {}).get(
                service_name
            )
        elif service_name in servicelists:
            service.attrib["servicelist"] = servicelists[service_name]
        return service

    def upgrade_container(
        self, elt, current_service, files, ip, servicelists, upgrade_help
    ):
        if elt.tag == "file":
            self.move(elt, "name", "text")
            self.remove(elt, "del_comment", optional=True)
            elt.attrib["engine"] = "creole_legacy"
            if (
                not "instance_mode" in elt.attrib
                or elt.attrib["instance_mode"] != "when_container"
            ) and elt.text not in upgrade_help.get("files", {}).get("remove", {}):
                if elt.attrib.get("filelist") in upgrade_help.get("services", {}).get(
                    "filelist_service", {}
                ):
                    elt_service = upgrade_help.get("services", {}).get(
                        "filelist_service", {}
                    )[elt.attrib["filelist"]]
                    if elt_service in files:
                        service = elt_service
                    else:
                        service = current_service
                else:
                    service = current_service
                files[service][elt.text] = elt
        elif elt.tag in [
            "host",
            "disknod",
            "fstab",
            "interface",
            "package",
            "service_access",
        ]:
            pass
        elif elt.tag == "service_restriction":
            for restriction in elt:
                if restriction.tag == "ip" and restriction.text != "0.0.0.0":
                    self.remove(restriction, "ip_type", optional=True)
                    self.remove(restriction, "netmask_type", optional=True)
                    if elt.attrib["service"] in upgrade_help.get("services", {}).get(
                        "rename", {}
                    ):
                        elt_service = upgrade_help.get("services", {}).get(
                            "rename", {}
                        )[elt.attrib["service"]]
                    else:
                        elt_service = elt.attrib["service"]
                    if elt_service in ip:
                        service = elt_service
                    else:
                        service = current_service
                    ip[service].append(restriction)
        elif elt.tag == "service":
            new_name = elt.text
            if current_service == "unknown":
                if new_name in files:
                    raise Exception("hu?")
                files[new_name] = files[current_service]
                del files[current_service]
                ip[new_name] = ip[current_service]
                del ip[current_service]
            elif new_name not in files:
                files[new_name] = {}
                ip[new_name] = []
            current_service = new_name
            if "servicelist" in elt.attrib:
                servicelists[current_service] = elt.attrib["servicelist"]
        else:
            raise Exception(f"unknown containers tag {elt.tag}")
        return current_service
