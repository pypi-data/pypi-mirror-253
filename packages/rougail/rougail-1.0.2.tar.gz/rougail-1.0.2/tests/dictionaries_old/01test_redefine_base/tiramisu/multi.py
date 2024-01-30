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
option_1 = StrOption(name="my_variable", doc="my_variable", properties=frozenset({"normal"}))
option_1.impl_set_information('test', ('test1',))
optiondescription_4 = OptionDescription(name="rougail", doc="Rougail", children=[option_1], properties=frozenset({"normal"}))
optiondescription_3 = OptionDescription(name="1", doc="1", children=[optiondescription_4])
option_2 = StrOption(name="my_variable", doc="my_variable", properties=frozenset({"normal"}))
option_2.impl_set_information('test', ('test1',))
optiondescription_6 = OptionDescription(name="rougail", doc="Rougail", children=[option_2], properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="2", doc="2", children=[optiondescription_6])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_3, optiondescription_5])
