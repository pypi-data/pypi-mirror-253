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
option_1 = StrOption(name="variable1", doc="variable1", properties=frozenset({"normal"}))
option_3 = StrOption(name="variable2", doc="variable2", properties=frozenset({"normal"}))
option_5 = StrOption(name="variable3", doc="variable3", properties=frozenset({"normal"}))
optiondescription_4 = OptionDescription(name="subfamily", doc="subfamily", children=[option_5], properties=frozenset({"normal"}))
option_6 = StrOption(name="variable4", doc="variable4", properties=frozenset({"normal"}))
optiondescription_2 = OptionDescription(name="base", doc="base", children=[option_3, optiondescription_4, option_6], properties=frozenset({"normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, optiondescription_2], properties=frozenset({"normal"}))
optiondescription_13 = OptionDescription(name="1", doc="1", children=[optiondescription_14])
option_7 = StrOption(name="variable1", doc="variable1", properties=frozenset({"normal"}))
option_9 = StrOption(name="variable2", doc="variable2", properties=frozenset({"normal"}))
option_11 = StrOption(name="variable3", doc="variable3", properties=frozenset({"normal"}))
optiondescription_10 = OptionDescription(name="subfamily", doc="subfamily", children=[option_11], properties=frozenset({"normal"}))
option_12 = StrOption(name="variable4", doc="variable4", properties=frozenset({"normal"}))
optiondescription_8 = OptionDescription(name="base", doc="base", children=[option_9, optiondescription_10, option_12], properties=frozenset({"normal"}))
optiondescription_16 = OptionDescription(name="rougail", doc="Rougail", children=[option_7, optiondescription_8], properties=frozenset({"normal"}))
optiondescription_15 = OptionDescription(name="2", doc="2", children=[optiondescription_16])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_13, optiondescription_15])
