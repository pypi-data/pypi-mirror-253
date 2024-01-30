"""
Config file for Rougail

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
from os.path import join, abspath, dirname


ROUGAILROOT = "/srv/rougail"
DTDDIR = join(dirname(abspath(__file__)), "data")


RougailConfig = {
    "dictionaries_dir": [join(ROUGAILROOT, "dictionaries")],
    "extra_dictionaries": {},
    "services_dir": [join(ROUGAILROOT, "services")],
    "patches_dir": join(ROUGAILROOT, "patches"),
    "templates_dir": join(ROUGAILROOT, "templates"),
    "destinations_dir": join(ROUGAILROOT, "destinations"),
    "tmp_dir": join(ROUGAILROOT, "tmp"),
    "dtdfilename": join(DTDDIR, "rougail.dtd"),
    "yamlschema_filename": join(DTDDIR, "rougail.yml"),
    "functions_file": join(ROUGAILROOT, "functions.py"),
    "system_service_directory": "/usr/lib/systemd/system",
    "systemd_service_destination_directory": "/usr/local/lib",
    "systemd_service_directory": "/systemd",
    "systemd_service_file": "rougail.conf",
    "systemd_service_ip_file": "rougail_ip.conf",
    "systemd_tmpfile_factory_dir": "/usr/local/lib",
    "systemd_tmpfile_directory": "/tmpfiles.d",
    "systemd_tmpfile_file": "0rougail.conf",
    "systemd_tmpfile_delete_before_create": False,
    "variable_namespace": "rougail",
    "variable_namespace_description": "Rougail",
    "auto_freeze_variable": "server_deployed",
    "internal_functions": [],
    "multi_functions": [],
    "extra_annotators": [],
    "modes_level": ["basic", "standard", "advanced"],
    "default_family_mode": "basic",
    "default_variable_mode": "standard",
    "default_files_engine": "jinja",
    "default_files_mode": 644,
    "default_files_owner": "root",
    "default_files_group": "root",
    "default_files_included": "no",
    "default_overrides_engine": "jinja",
    "default_service_names_engine": "none",
    "default_certificate_domain": "rougail.server_name",
    "base_option_name": "baseoption",
    "export_with_import": True,
    "force_convert_dyn_option_description": False,
    "suffix": "",
    "tiramisu_cache": None,
}
