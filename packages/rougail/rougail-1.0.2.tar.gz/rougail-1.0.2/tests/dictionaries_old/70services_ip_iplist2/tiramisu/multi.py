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
option_1 = StrOption(name="condition", doc="condition", default="yes", properties=frozenset({"mandatory", "normal"}))
option_2 = NetworkOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.0/24", cidr=True, properties=frozenset({"mandatory", "normal"}))
optiondescription_18 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2], properties=frozenset({"normal"}))
option_9 = SymLinkOption(name="name", opt=option_2)
option_8 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_1, notraisepropertyerror=True), 'expected_0': ParamValue("yes")})))
optiondescription_7 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_9, option_8])
optiondescription_6 = OptionDescription(name="ip", doc="ip", children=[optiondescription_7])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_10 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_20 = OptionDescription(name="nut_service", doc="nut.service", children=[optiondescription_6, option_5, option_10])
optiondescription_20.impl_set_information('type', "service")
optiondescription_19 = OptionDescription(name="services", doc="services", children=[optiondescription_20], properties=frozenset({"hidden"}))
optiondescription_17 = OptionDescription(name="1", doc="1", children=[optiondescription_18, optiondescription_19])
option_3 = StrOption(name="condition", doc="condition", default="yes", properties=frozenset({"mandatory", "normal"}))
option_4 = NetworkOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.0/24", cidr=True, properties=frozenset({"mandatory", "normal"}))
optiondescription_22 = OptionDescription(name="rougail", doc="Rougail", children=[option_3, option_4], properties=frozenset({"normal"}))
option_15 = SymLinkOption(name="name", opt=option_4)
option_14 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_3, notraisepropertyerror=True), 'expected_0': ParamValue("yes")})))
optiondescription_13 = OptionDescription(name="nut_monitor_host", doc="nut_monitor_host", children=[option_15, option_14])
optiondescription_12 = OptionDescription(name="ip", doc="ip", children=[optiondescription_13])
option_11 = BoolOption(name="activate", doc="activate", default=True)
option_16 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_24 = OptionDescription(name="nut_service", doc="nut.service", children=[optiondescription_12, option_11, option_16])
optiondescription_24.impl_set_information('type', "service")
optiondescription_23 = OptionDescription(name="services", doc="services", children=[optiondescription_24], properties=frozenset({"hidden"}))
optiondescription_21 = OptionDescription(name="2", doc="2", children=[optiondescription_22, optiondescription_23])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_17, optiondescription_21])
