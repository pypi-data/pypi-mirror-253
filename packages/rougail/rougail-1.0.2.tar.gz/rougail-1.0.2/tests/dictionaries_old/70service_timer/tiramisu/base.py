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
option_3 = BoolOption(name="activate", doc="activate", default=True)
option_4 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_2 = OptionDescription(name="testsrv_service", doc="testsrv_service", children=[option_3, option_4])
optiondescription_2.impl_set_information('type', "service")
option_6 = BoolOption(name="activate", doc="activate", default=True)
option_7 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_5 = OptionDescription(name="testsrv_timer", doc="testsrv_timer", children=[option_6, option_7])
optiondescription_5.impl_set_information('type', "timer")
optiondescription_1 = OptionDescription(name="services", doc="services", children=[optiondescription_2, optiondescription_5], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
