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
option_1 = StrOption(name="condition", doc="condition", default="no", properties=frozenset({"mandatory", "normal"}))
optiondescription_8 = OptionDescription(name="rougail", doc="Rougail", children=[option_1], properties=frozenset({"normal"}))
option_3 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_1, notraisepropertyerror=True), 'expected_0': ParamValue("yes")})))
option_4 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_10 = OptionDescription(name="test_service", doc="test.service", children=[option_3, option_4])
optiondescription_10.impl_set_information('type', "service")
optiondescription_9 = OptionDescription(name="services", doc="services", children=[optiondescription_10], properties=frozenset({"hidden"}))
optiondescription_7 = OptionDescription(name="1", doc="1", children=[optiondescription_8, optiondescription_9])
option_2 = StrOption(name="condition", doc="condition", default="no", properties=frozenset({"mandatory", "normal"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[option_2], properties=frozenset({"normal"}))
option_5 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_2, notraisepropertyerror=True), 'expected_0': ParamValue("yes")})))
option_6 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_14 = OptionDescription(name="test_service", doc="test.service", children=[option_5, option_6])
optiondescription_14.impl_set_information('type', "service")
optiondescription_13 = OptionDescription(name="services", doc="services", children=[optiondescription_14], properties=frozenset({"hidden"}))
optiondescription_11 = OptionDescription(name="2", doc="2", children=[optiondescription_12, optiondescription_13])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_7, optiondescription_11])
