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
option_2 = StrOption(name="mode_conteneur_actif", doc="Description", default="non", properties=frozenset({"mandatory", "normal"}))
option_3 = UsernameOption(name="owner", doc="owner", default="nobody", properties=frozenset({"mandatory", "normal"}))
option_4 = UsernameOption(name="group", doc="group", default="nobody", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2, option_3, option_4], properties=frozenset({"normal"}))
optiondescription_40 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_13 = SymLinkOption(name="group", opt=option_4)
option_14 = FilenameOption(name="name", doc="name", default="/etc/file")
option_15 = SymLinkOption(name="owner", opt=option_3)
option_16 = StrOption(name="source", doc="source", default="file")
option_12 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_11 = OptionDescription(name="file", doc="file", children=[option_13, option_14, option_15, option_16, option_12])
option_19 = SymLinkOption(name="group", opt=option_4)
option_20 = FilenameOption(name="name", doc="name", default="/etc/file2")
option_21 = SymLinkOption(name="owner", opt=option_3)
option_22 = StrOption(name="source", doc="source", default="file2")
option_18 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_17 = OptionDescription(name="file2", doc="file2", children=[option_19, option_20, option_21, option_22, option_18])
optiondescription_17.impl_set_information('engine', "jinja")
optiondescription_10 = OptionDescription(name="files", doc="files", children=[optiondescription_11, optiondescription_17])
option_9 = BoolOption(name="activate", doc="activate", default=True)
option_23 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_42 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_10, option_9, option_23])
optiondescription_42.impl_set_information('type', "service")
optiondescription_41 = OptionDescription(name="services", doc="services", children=[optiondescription_42], properties=frozenset({"hidden"}))
optiondescription_39 = OptionDescription(name="1", doc="1", children=[optiondescription_40, optiondescription_41])
option_6 = StrOption(name="mode_conteneur_actif", doc="Description", default="non", properties=frozenset({"mandatory", "normal"}))
option_7 = UsernameOption(name="owner", doc="owner", default="nobody", properties=frozenset({"mandatory", "normal"}))
option_8 = UsernameOption(name="group", doc="group", default="nobody", properties=frozenset({"mandatory", "normal"}))
optiondescription_5 = OptionDescription(name="general", doc="general", children=[option_6, option_7, option_8], properties=frozenset({"normal"}))
optiondescription_44 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_5], properties=frozenset({"normal"}))
option_28 = SymLinkOption(name="group", opt=option_8)
option_29 = FilenameOption(name="name", doc="name", default="/etc/file")
option_30 = SymLinkOption(name="owner", opt=option_7)
option_31 = StrOption(name="source", doc="source", default="file")
option_27 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_26 = OptionDescription(name="file", doc="file", children=[option_28, option_29, option_30, option_31, option_27])
option_34 = SymLinkOption(name="group", opt=option_8)
option_35 = FilenameOption(name="name", doc="name", default="/etc/file2")
option_36 = SymLinkOption(name="owner", opt=option_7)
option_37 = StrOption(name="source", doc="source", default="file2")
option_33 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_32 = OptionDescription(name="file2", doc="file2", children=[option_34, option_35, option_36, option_37, option_33])
optiondescription_32.impl_set_information('engine', "jinja")
optiondescription_25 = OptionDescription(name="files", doc="files", children=[optiondescription_26, optiondescription_32])
option_24 = BoolOption(name="activate", doc="activate", default=True)
option_38 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_46 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_25, option_24, option_38])
optiondescription_46.impl_set_information('type', "service")
optiondescription_45 = OptionDescription(name="services", doc="services", children=[optiondescription_46], properties=frozenset({"hidden"}))
optiondescription_43 = OptionDescription(name="2", doc="2", children=[optiondescription_44, optiondescription_45])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_39, optiondescription_43])
