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
option_1 = FloatOption(name="float", doc="Description", properties=frozenset({"normal"}))
optiondescription_8 = OptionDescription(name="rougail", doc="Rougail", children=[option_1], properties=frozenset({"normal"}))
option_3 = StrOption(name="description", doc="description", properties=frozenset({"normal"}))
optiondescription_2 = OptionDescription(name="example", doc="example", children=[option_3], properties=frozenset({"normal"}))
optiondescription_9 = OptionDescription(name="extra", doc="extra", children=[optiondescription_2], properties=frozenset({"normal"}))
optiondescription_7 = OptionDescription(name="1", doc="1", children=[optiondescription_8, optiondescription_9])
optiondescription_7.impl_set_information('provider:example', "extra.example.description")
option_4 = FloatOption(name="float", doc="Description", properties=frozenset({"normal"}))
optiondescription_11 = OptionDescription(name="rougail", doc="Rougail", children=[option_4], properties=frozenset({"normal"}))
option_6 = StrOption(name="description", doc="description", properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="example", doc="example", children=[option_6], properties=frozenset({"normal"}))
optiondescription_12 = OptionDescription(name="extra", doc="extra", children=[optiondescription_5], properties=frozenset({"normal"}))
optiondescription_10 = OptionDescription(name="2", doc="2", children=[optiondescription_11, optiondescription_12])
optiondescription_10.impl_set_information('provider:example', "extra.example.description")
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_7, optiondescription_10])
