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
option_1 = FilenameOption(name="file_name", doc="file_name", default="/etc/mailname", properties=frozenset({"mandatory", "normal"}))
option_2 = StrOption(name="var", doc="var", default="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_22 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2], properties=frozenset({"normal"}))
option_9 = SymLinkOption(name="name", opt=option_1)
option_10 = StrOption(name="source", doc="source", default="mailname")
option_11 = SymLinkOption(name="variable", opt=option_2)
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="mailname", doc="mailname", children=[option_9, option_10, option_11, option_8])
optiondescription_6 = OptionDescription(name="files", doc="files", children=[optiondescription_7])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_12 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_24 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_6, option_5, option_12])
optiondescription_24.impl_set_information('type', "service")
optiondescription_23 = OptionDescription(name="services", doc="services", children=[optiondescription_24], properties=frozenset({"hidden"}))
optiondescription_21 = OptionDescription(name="1", doc="1", children=[optiondescription_22, optiondescription_23])
option_3 = FilenameOption(name="file_name", doc="file_name", default="/etc/mailname", properties=frozenset({"mandatory", "normal"}))
option_4 = StrOption(name="var", doc="var", default="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[option_3, option_4], properties=frozenset({"normal"}))
option_17 = SymLinkOption(name="name", opt=option_3)
option_18 = StrOption(name="source", doc="source", default="mailname")
option_19 = SymLinkOption(name="variable", opt=option_4)
option_16 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_15 = OptionDescription(name="mailname", doc="mailname", children=[option_17, option_18, option_19, option_16])
optiondescription_14 = OptionDescription(name="files", doc="files", children=[optiondescription_15])
option_13 = BoolOption(name="activate", doc="activate", default=True)
option_20 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_28 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_14, option_13, option_20])
optiondescription_28.impl_set_information('type', "service")
optiondescription_27 = OptionDescription(name="services", doc="services", children=[optiondescription_28], properties=frozenset({"hidden"}))
optiondescription_25 = OptionDescription(name="2", doc="2", children=[optiondescription_26, optiondescription_27])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_21, optiondescription_25])
