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
option_1 = IPOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.1", allow_reserved=True, properties=frozenset({"disabled", "mandatory", "normal"}))
optiondescription_16 = OptionDescription(name="rougail", doc="Rougail", children=[option_1], properties=frozenset({"normal"}))
option_7 = SymLinkOption(name="name", opt=option_1)
option_6 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_5 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_7, option_6])
optiondescription_4 = OptionDescription(name="ip", doc="ip", children=[optiondescription_5])
option_3 = BoolOption(name="activate", doc="activate", default=True)
option_8 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_18 = OptionDescription(name="nut_service", doc="nut.service", children=[optiondescription_4, option_3, option_8])
optiondescription_18.impl_set_information('type', "service")
optiondescription_17 = OptionDescription(name="services", doc="services", children=[optiondescription_18], properties=frozenset({"hidden"}))
optiondescription_15 = OptionDescription(name="1", doc="1", children=[optiondescription_16, optiondescription_17])
option_2 = IPOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.1", allow_reserved=True, properties=frozenset({"disabled", "mandatory", "normal"}))
optiondescription_20 = OptionDescription(name="rougail", doc="Rougail", children=[option_2], properties=frozenset({"normal"}))
option_13 = SymLinkOption(name="name", opt=option_2)
option_12 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_11 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_13, option_12])
optiondescription_10 = OptionDescription(name="ip", doc="ip", children=[optiondescription_11])
option_9 = BoolOption(name="activate", doc="activate", default=True)
option_14 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_22 = OptionDescription(name="nut_service", doc="nut.service", children=[optiondescription_10, option_9, option_14])
optiondescription_22.impl_set_information('type', "service")
optiondescription_21 = OptionDescription(name="services", doc="services", children=[optiondescription_22], properties=frozenset({"hidden"}))
optiondescription_19 = OptionDescription(name="2", doc="2", children=[optiondescription_20, optiondescription_21])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_15, optiondescription_19])
