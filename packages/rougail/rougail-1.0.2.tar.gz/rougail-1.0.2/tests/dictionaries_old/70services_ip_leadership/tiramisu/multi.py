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
option_3 = NetmaskOption(name="nut_monitor_netmask", doc="nut_monitor_netmask", multi=True, default=['255.255.255.0'], properties=frozenset({"mandatory", "normal"}))
option_4 = NetworkOption(name="nut_monitor_host", doc="nut_monitor_host", multi=True, default_multi="192.168.1.0", properties=frozenset({"mandatory", "normal"}))
optiondescription_2 = Leadership(name="nut_monitor_netmask", doc="nut_monitor_netmask", children=[option_3, option_4], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="general", doc="général", children=[optiondescription_2], properties=frozenset({"normal"}))
optiondescription_24 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_13 = SymLinkOption(name="name", opt=option_4)
option_14 = SymLinkOption(name="netmask", opt=option_3)
option_12 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_11 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_13, option_14, option_12])
optiondescription_10 = OptionDescription(name="ip", doc="ip", children=[optiondescription_11])
option_9 = BoolOption(name="activate", doc="activate", default=True)
option_15 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_26 = OptionDescription(name="ntp_service", doc="ntp.service", children=[optiondescription_10, option_9, option_15])
optiondescription_26.impl_set_information('type', "service")
optiondescription_25 = OptionDescription(name="services", doc="services", children=[optiondescription_26], properties=frozenset({"hidden"}))
optiondescription_23 = OptionDescription(name="1", doc="1", children=[optiondescription_24, optiondescription_25])
option_7 = NetmaskOption(name="nut_monitor_netmask", doc="nut_monitor_netmask", multi=True, default=['255.255.255.0'], properties=frozenset({"mandatory", "normal"}))
option_8 = NetworkOption(name="nut_monitor_host", doc="nut_monitor_host", multi=True, default_multi="192.168.1.0", properties=frozenset({"mandatory", "normal"}))
optiondescription_6 = Leadership(name="nut_monitor_netmask", doc="nut_monitor_netmask", children=[option_7, option_8], properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="general", doc="général", children=[optiondescription_6], properties=frozenset({"normal"}))
optiondescription_28 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_5], properties=frozenset({"normal"}))
option_20 = SymLinkOption(name="name", opt=option_8)
option_21 = SymLinkOption(name="netmask", opt=option_7)
option_19 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_18 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_20, option_21, option_19])
optiondescription_17 = OptionDescription(name="ip", doc="ip", children=[optiondescription_18])
option_16 = BoolOption(name="activate", doc="activate", default=True)
option_22 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_30 = OptionDescription(name="ntp_service", doc="ntp.service", children=[optiondescription_17, option_16, option_22])
optiondescription_30.impl_set_information('type', "service")
optiondescription_29 = OptionDescription(name="services", doc="services", children=[optiondescription_30], properties=frozenset({"hidden"}))
optiondescription_27 = OptionDescription(name="2", doc="2", children=[optiondescription_28, optiondescription_29])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_23, optiondescription_27])
