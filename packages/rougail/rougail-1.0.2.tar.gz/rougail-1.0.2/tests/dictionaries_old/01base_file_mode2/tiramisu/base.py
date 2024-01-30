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
option_5 = FilenameOption(name="name", doc="name", default="/etc/file")
option_6 = FilenameOption(name="source", doc="source", default="/etc/file")
option_7 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_4 = OptionDescription(name="file", doc="file", children=[option_5, option_6, option_7])
optiondescription_4.impl_set_information('mode', 1755)
optiondescription_3 = OptionDescription(name="files", doc="files", children=[optiondescription_4])
option_8 = BoolOption(name="activate", doc="activate", default=True)
option_9 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_2 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_3, option_8, option_9])
optiondescription_2.impl_set_information('type', "service")
optiondescription_1 = OptionDescription(name="services", doc="services", children=[optiondescription_2], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
