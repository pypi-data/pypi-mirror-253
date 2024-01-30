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
option_3 = StrOption(name="varname", doc="No change", multi=True, default=["val1", "val2"], default_multi="val1", properties=frozenset({"mandatory", "notempty", "standard"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3], properties=frozenset({"standard"}))
option_5 = StrOption(name="vardyn", doc="No change", properties=frozenset({"standard"}))
option_7 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"standard"}))
option_8 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"standard"}))
option_9 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"standard"}))
optiondescription_6 = Leadership(name="leadership", doc="leadership", children=[option_7, option_8, option_9], properties=frozenset({"standard"}))
optiondescription_4 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_3, notraisepropertyerror=True)))), children=[option_5, optiondescription_6], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2, optiondescription_4], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
