from importlib.machinery import SourceFileLoader as _SourceFileLoader
from importlib.util import spec_from_loader as _spec_from_loader, module_from_spec as _module_from_spec
class func:
    pass

def _load_functions(path):
    global _SourceFileLoader, _spec_from_loader, _module_from_spec, func
    loader = _SourceFileLoader('func', path)
    spec = _spec_from_loader(loader.name, loader)
    func_ = _module_from_spec(spec)
    loader.exec_module(func_)
    for function in dir(func_):
        if function.startswith('_'):
            continue
        setattr(func, function, getattr(func_, function))
_load_functions('tests/dictionaries/../eosfunc/test.py')
try:
    from tiramisu4 import *
    from tiramisu4.setting import ALLOWED_LEADER_PROPERTIES
except:
    from tiramisu import *
    from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("normal")
ALLOWED_LEADER_PROPERTIES.add("expert")
option_1 = FilenameOption(name="file_name", doc="file_name", multi=True, default=['/etc/mailname', '/etc/mailname2'], default_multi="/etc/mailname", properties=frozenset({"mandatory", "normal"}))
option_2 = FilenameOption(name="file_name2", doc="file_name2", multi=True, default=['/etc/mailname3', '/etc/mailname4'], default_multi="/etc/mailname3", properties=frozenset({"mandatory", "normal"}))
option_3 = StrOption(name="var", doc="var", multi=True, default=['mailname', 'mailname2'], default_multi="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_34 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2, option_3], properties=frozenset({"normal"}))
option_11 = SymLinkOption(name="name", opt=option_1)
option_12 = StrOption(name="source", doc="source", default="mailname")
option_13 = SymLinkOption(name="variable", opt=option_3)
option_10 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_9 = OptionDescription(name="mailname", doc="mailname", children=[option_11, option_12, option_13, option_10])
option_16 = SymLinkOption(name="name", opt=option_2)
option_17 = StrOption(name="source", doc="source", default="mailname2")
option_18 = SymLinkOption(name="variable", opt=option_3)
option_15 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_14 = OptionDescription(name="mailname2", doc="mailname2", children=[option_16, option_17, option_18, option_15])
optiondescription_14.impl_set_information('engine', "jinja")
optiondescription_8 = OptionDescription(name="files", doc="files", children=[optiondescription_9, optiondescription_14])
option_7 = BoolOption(name="activate", doc="activate", default=True)
option_19 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_36 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_8, option_7, option_19])
optiondescription_36.impl_set_information('type', "service")
optiondescription_35 = OptionDescription(name="services", doc="services", children=[optiondescription_36], properties=frozenset({"hidden"}))
optiondescription_33 = OptionDescription(name="1", doc="1", children=[optiondescription_34, optiondescription_35])
option_4 = FilenameOption(name="file_name", doc="file_name", multi=True, default=['/etc/mailname', '/etc/mailname2'], default_multi="/etc/mailname", properties=frozenset({"mandatory", "normal"}))
option_5 = FilenameOption(name="file_name2", doc="file_name2", multi=True, default=['/etc/mailname3', '/etc/mailname4'], default_multi="/etc/mailname3", properties=frozenset({"mandatory", "normal"}))
option_6 = StrOption(name="var", doc="var", multi=True, default=['mailname', 'mailname2'], default_multi="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_38 = OptionDescription(name="rougail", doc="Rougail", children=[option_4, option_5, option_6], properties=frozenset({"normal"}))
option_24 = SymLinkOption(name="name", opt=option_4)
option_25 = StrOption(name="source", doc="source", default="mailname")
option_26 = SymLinkOption(name="variable", opt=option_6)
option_23 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_22 = OptionDescription(name="mailname", doc="mailname", children=[option_24, option_25, option_26, option_23])
option_29 = SymLinkOption(name="name", opt=option_5)
option_30 = StrOption(name="source", doc="source", default="mailname2")
option_31 = SymLinkOption(name="variable", opt=option_6)
option_28 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_27 = OptionDescription(name="mailname2", doc="mailname2", children=[option_29, option_30, option_31, option_28])
optiondescription_27.impl_set_information('engine', "jinja")
optiondescription_21 = OptionDescription(name="files", doc="files", children=[optiondescription_22, optiondescription_27])
option_20 = BoolOption(name="activate", doc="activate", default=True)
option_32 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_40 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_21, option_20, option_32])
optiondescription_40.impl_set_information('type', "service")
optiondescription_39 = OptionDescription(name="services", doc="services", children=[optiondescription_40], properties=frozenset({"hidden"}))
optiondescription_37 = OptionDescription(name="2", doc="2", children=[optiondescription_38, optiondescription_39])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_33, optiondescription_37])
