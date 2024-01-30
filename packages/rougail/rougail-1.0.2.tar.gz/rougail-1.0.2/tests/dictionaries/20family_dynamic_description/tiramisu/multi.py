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
from rougail.tiramisu import ConvertDynOptionDescription
option_4 = StrOption(name="varname", doc="No change", multi=True, default=["val1", "val2"], default_multi="val1", properties=frozenset({"mandatory", "notempty", "standard"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"standard"}))
option_6 = StrOption(name="vardyn", doc="No change", properties=frozenset({"standard"}))
optiondescription_5 = ConvertDynOptionDescription(name="dyn", doc="Dyn ", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_4, notraisepropertyerror=True)))), children=[option_6], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3, optiondescription_5], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_10 = StrOption(name="varname", doc="No change", multi=True, default=["val1", "val2"], default_multi="val1", properties=frozenset({"mandatory", "notempty", "standard"}))
optiondescription_9 = OptionDescription(name="general", doc="general", children=[option_10], properties=frozenset({"standard"}))
option_12 = StrOption(name="vardyn", doc="No change", properties=frozenset({"standard"}))
optiondescription_11 = ConvertDynOptionDescription(name="dyn", doc="Dyn ", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_10, notraisepropertyerror=True)))), children=[option_12], properties=frozenset({"standard"}))
optiondescription_8 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_9, optiondescription_11], properties=frozenset({"standard"}))
optiondescription_7 = OptionDescription(name="2", doc="2", children=[optiondescription_8], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_7])
