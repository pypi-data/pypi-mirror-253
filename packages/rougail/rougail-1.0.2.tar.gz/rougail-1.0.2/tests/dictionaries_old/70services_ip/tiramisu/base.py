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
option_2 = IPOption(name="nut_monitor_host", doc="nut_monitor_host", default="192.168.0.1", allow_reserved=True, properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[option_2], properties=frozenset({"normal"}))
option_7 = SymLinkOption(name="name", opt=option_2)
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_6 = OptionDescription(name="rougail_nut_monitor_host", doc="rougail_nut_monitor_host", children=[option_7, option_8])
optiondescription_5 = OptionDescription(name="ip", doc="ip", children=[optiondescription_6])
option_9 = BoolOption(name="activate", doc="activate", default=True)
option_10 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_4 = OptionDescription(name="nut_service", doc="nut_service", children=[optiondescription_5, option_9, option_10])
optiondescription_4.impl_set_information('type', "service")
optiondescription_3 = OptionDescription(name="services", doc="services", children=[optiondescription_4], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_3])
