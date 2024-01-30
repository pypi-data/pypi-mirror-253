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
option_1 = StrOption(name="var", doc="var", default="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_18 = OptionDescription(name="rougail", doc="Rougail", children=[option_1], properties=frozenset({"normal"}))
option_7 = FilenameOption(name="name", doc="name", default="/tmp/test")
option_8 = StrOption(name="source", doc="source", default="test")
option_6 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_5 = OptionDescription(name="test", doc="test", children=[option_7, option_8, option_6])
optiondescription_4 = OptionDescription(name="files", doc="files", children=[optiondescription_5])
option_3 = BoolOption(name="activate", doc="activate", default=True)
option_9 = BoolOption(name="manage", doc="manage", default=False)
optiondescription_20 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_4, option_3, option_9])
optiondescription_20.impl_set_information('type', "none")
optiondescription_19 = OptionDescription(name="services", doc="services", children=[optiondescription_20], properties=frozenset({"hidden"}))
optiondescription_17 = OptionDescription(name="1", doc="1", children=[optiondescription_18, optiondescription_19])
option_2 = StrOption(name="var", doc="var", default="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_22 = OptionDescription(name="rougail", doc="Rougail", children=[option_2], properties=frozenset({"normal"}))
option_14 = FilenameOption(name="name", doc="name", default="/tmp/test")
option_15 = StrOption(name="source", doc="source", default="test")
option_13 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_12 = OptionDescription(name="test", doc="test", children=[option_14, option_15, option_13])
optiondescription_11 = OptionDescription(name="files", doc="files", children=[optiondescription_12])
option_10 = BoolOption(name="activate", doc="activate", default=True)
option_16 = BoolOption(name="manage", doc="manage", default=False)
optiondescription_24 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_11, option_10, option_16])
optiondescription_24.impl_set_information('type', "none")
optiondescription_23 = OptionDescription(name="services", doc="services", children=[optiondescription_24], properties=frozenset({"hidden"}))
optiondescription_21 = OptionDescription(name="2", doc="2", children=[optiondescription_22, optiondescription_23])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_17, optiondescription_21])
