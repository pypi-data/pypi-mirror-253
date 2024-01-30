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
option_4 = StrOption(name="vardyn", doc="No change", default="val", properties=frozenset({"mandatory", "normal"}))
optiondescription_3 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func.calc_value, Params((ParamOption(option_2, notraisepropertyerror=True)))), children=[option_4], properties=frozenset({"normal"}))
option_6 = StrOption(name="newvar", doc="No change", default=Calculation(func.calc_val, Params((ParamDynOption(option_4, 'val1', optiondescription_3)))), properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="new", doc="new", children=[option_6], properties=frozenset({"normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1, optiondescription_3, optiondescription_5], properties=frozenset({"normal"}))
optiondescription_13 = OptionDescription(name="1", doc="1", children=[optiondescription_14])
option_8 = StrOption(name="varname", doc="No change", multi=True, default=['val1', 'val2'], default_multi="val1", properties=frozenset({"mandatory", "normal"}))
optiondescription_7 = OptionDescription(name="general", doc="general", children=[option_8], properties=frozenset({"normal"}))
option_10 = StrOption(name="vardyn", doc="No change", default="val", properties=frozenset({"mandatory", "normal"}))
optiondescription_9 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func.calc_value, Params((ParamOption(option_8, notraisepropertyerror=True)))), children=[option_10], properties=frozenset({"normal"}))
option_12 = StrOption(name="newvar", doc="No change", default=Calculation(func.calc_val, Params((ParamDynOption(option_10, 'val1', optiondescription_9)))), properties=frozenset({"normal"}))
optiondescription_11 = OptionDescription(name="new", doc="new", children=[option_12], properties=frozenset({"normal"}))
optiondescription_16 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_7, optiondescription_9, optiondescription_11], properties=frozenset({"normal"}))
optiondescription_15 = OptionDescription(name="2", doc="2", children=[optiondescription_16])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_13, optiondescription_15])
