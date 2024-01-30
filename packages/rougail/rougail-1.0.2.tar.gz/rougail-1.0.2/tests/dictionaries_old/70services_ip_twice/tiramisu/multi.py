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
option_1 = IPOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.1", allow_reserved=True, properties=frozenset({"mandatory", "normal"}))
option_2 = IPOption(name="nut_monitor_host2", doc="nut_monitor_host2", default="192.168.0.2", allow_reserved=True, properties=frozenset({"mandatory", "normal"}))
optiondescription_24 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2], properties=frozenset({"normal"}))
option_9 = SymLinkOption(name="name", opt=option_1)
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_9, option_8])
option_12 = SymLinkOption(name="name", opt=option_2)
option_11 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_10 = OptionDescription(name="nut_monitor_host2", doc="nut_monitor_host2", children=[option_12, option_11])
optiondescription_6 = OptionDescription(name="ip", doc="ip", children=[optiondescription_7, optiondescription_10])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_13 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_26 = OptionDescription(name="nut_service", doc="nut.service", children=[optiondescription_6, option_5, option_13])
optiondescription_26.impl_set_information('type', "service")
optiondescription_25 = OptionDescription(name="services", doc="services", children=[optiondescription_26], properties=frozenset({"hidden"}))
optiondescription_23 = OptionDescription(name="1", doc="1", children=[optiondescription_24, optiondescription_25])
option_3 = IPOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.1", allow_reserved=True, properties=frozenset({"mandatory", "normal"}))
option_4 = IPOption(name="nut_monitor_host2", doc="nut_monitor_host2", default="192.168.0.2", allow_reserved=True, properties=frozenset({"mandatory", "normal"}))
optiondescription_28 = OptionDescription(name="rougail", doc="Rougail", children=[option_3, option_4], properties=frozenset({"normal"}))
option_18 = SymLinkOption(name="name", opt=option_3)
option_17 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_16 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_18, option_17])
option_21 = SymLinkOption(name="name", opt=option_4)
option_20 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_19 = OptionDescription(name="nut_monitor_host2", doc="nut_monitor_host2", children=[option_21, option_20])
optiondescription_15 = OptionDescription(name="ip", doc="ip", children=[optiondescription_16, optiondescription_19])
option_14 = BoolOption(name="activate", doc="activate", default=True)
option_22 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_30 = OptionDescription(name="nut_service", doc="nut.service", children=[optiondescription_15, option_14, option_22])
optiondescription_30.impl_set_information('type', "service")
optiondescription_29 = OptionDescription(name="services", doc="services", children=[optiondescription_30], properties=frozenset({"hidden"}))
optiondescription_27 = OptionDescription(name="2", doc="2", children=[optiondescription_28, optiondescription_29])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_23, optiondescription_27])
