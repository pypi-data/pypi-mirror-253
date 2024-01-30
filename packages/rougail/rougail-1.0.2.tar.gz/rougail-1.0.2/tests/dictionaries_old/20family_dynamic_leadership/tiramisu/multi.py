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
from rougail.tiramisu import ConvertDynOptionDescription
option_2 = StrOption(name="varname", doc="No change", multi=True, default=['val1', 'val2'], default_multi="val1", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
option_4 = StrOption(name="vardyn", doc="No change", properties=frozenset({"normal"}))
option_6 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal"}))
option_7 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"normal"}))
option_8 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"normal"}))
optiondescription_5 = Leadership(name="leadership", doc="leadership", children=[option_6, option_7, option_8], properties=frozenset({"normal"}))
optiondescription_3 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func.calc_value, Params((ParamOption(option_2, notraisepropertyerror=True)))), children=[option_4, optiondescription_5], properties=frozenset({"normal"}))
optiondescription_18 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1, optiondescription_3], properties=frozenset({"normal"}))
optiondescription_17 = OptionDescription(name="1", doc="1", children=[optiondescription_18])
option_10 = StrOption(name="varname", doc="No change", multi=True, default=['val1', 'val2'], default_multi="val1", properties=frozenset({"mandatory", "normal"}))
optiondescription_9 = OptionDescription(name="general", doc="general", children=[option_10], properties=frozenset({"normal"}))
option_12 = StrOption(name="vardyn", doc="No change", properties=frozenset({"normal"}))
option_14 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal"}))
option_15 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"normal"}))
option_16 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"normal"}))
optiondescription_13 = Leadership(name="leadership", doc="leadership", children=[option_14, option_15, option_16], properties=frozenset({"normal"}))
optiondescription_11 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func.calc_value, Params((ParamOption(option_10, notraisepropertyerror=True)))), children=[option_12, optiondescription_13], properties=frozenset({"normal"}))
optiondescription_20 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_9, optiondescription_11], properties=frozenset({"normal"}))
optiondescription_19 = OptionDescription(name="2", doc="2", children=[optiondescription_20])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_17, optiondescription_19])
