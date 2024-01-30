from tiramisu import *
from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("standard")
ALLOWED_LEADER_PROPERTIES.add("advanced")
from importlib.machinery import SourceFileLoader as _SourceFileLoader
from importlib.util import spec_from_loader as _spec_from_loader, module_from_spec as _module_from_spec
global func
func = {'calc_value': calc_value}

def _load_functions(path):
    global _SourceFileLoader, _spec_from_loader, _module_from_spec, func
    loader = _SourceFileLoader('func', path)
    spec = _spec_from_loader(loader.name, loader)
    func_ = _module_from_spec(spec)
    loader.exec_module(func_)
    for function in dir(func_):
        if function.startswith('_'):
            continue
        func[function] = getattr(func_, function)
_load_functions('tests/dictionaries/../eosfunc/test.py')
option_3 = StrOption(name="variable1", doc="variable1", properties=frozenset({"standard"}))
option_5 = StrOption(name="variable2", doc="variable2", properties=frozenset({"standard"}))
option_7 = StrOption(name="variable3", doc="variable3", properties=frozenset({"standard"}))
optiondescription_6 = OptionDescription(name="subfamily", doc="subfamily", children=[option_7], properties=frozenset({"standard"}))
option_8 = StrOption(name="variable4", doc="variable4", properties=frozenset({"standard"}))
optiondescription_4 = OptionDescription(name="base", doc="base", children=[option_5, optiondescription_6, option_8], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[option_3, optiondescription_4], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_11 = StrOption(name="variable1", doc="variable1", properties=frozenset({"standard"}))
option_13 = StrOption(name="variable2", doc="variable2", properties=frozenset({"standard"}))
option_15 = StrOption(name="variable3", doc="variable3", properties=frozenset({"standard"}))
optiondescription_14 = OptionDescription(name="subfamily", doc="subfamily", children=[option_15], properties=frozenset({"standard"}))
option_16 = StrOption(name="variable4", doc="variable4", properties=frozenset({"standard"}))
optiondescription_12 = OptionDescription(name="base", doc="base", children=[option_13, optiondescription_14, option_16], properties=frozenset({"standard"}))
optiondescription_10 = OptionDescription(name="rougail", doc="rougail", children=[option_11, optiondescription_12], properties=frozenset({"standard"}))
optiondescription_9 = OptionDescription(name="2", doc="2", children=[optiondescription_10], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_9])
