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
_load_functions('tests/dictionaries_old/../eosfunc/test.py')
try:
    from tiramisu4 import *
    from tiramisu4.setting import ALLOWED_LEADER_PROPERTIES
except:
    from tiramisu import *
    from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("normal")
ALLOWED_LEADER_PROPERTIES.add("expert")
option_3 = StrOption(name="varname", doc="No change", multi=True, default=['a'], default_multi="a", properties=frozenset({"mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="général", children=[option_3], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_6 = StrOption(name="varname", doc="No change", multi=True, default=['a'], default_multi="a", properties=frozenset({"mandatory", "normal"}))
optiondescription_5 = OptionDescription(name="general", doc="général", children=[option_6], properties=frozenset({"normal"}))
option_8 = StrOption(name="mode", doc="mode", properties=frozenset({"normal"}))
optiondescription_7 = ConvertDynOptionDescription(name="ejabberd", doc="ejabberd", suffixes=Calculation(func.calc_value, Params((ParamOption(option_6, notraisepropertyerror=True)))), children=[option_8], properties=frozenset({"normal"}))
optiondescription_4 = OptionDescription(name="extra", doc="extra", children=[optiondescription_5, optiondescription_7], properties=frozenset({"normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_4])
