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
option_1 = BoolOption(name="server_deployed", doc="server_deployed", default=True, properties=frozenset({"mandatory", "normal"}))
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"basic", "force_store_value", "mandatory"}))
optiondescription_2 = OptionDescription(name="general", doc="général", children=[option_3], properties=frozenset({"basic"}))
optiondescription_8 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, optiondescription_2], properties=frozenset({"basic"}))
optiondescription_7 = OptionDescription(name="1", doc="1", children=[optiondescription_8])
option_4 = BoolOption(name="server_deployed", doc="server_deployed", default=True, properties=frozenset({"mandatory", "normal"}))
option_6 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"basic", "force_store_value", "mandatory"}))
optiondescription_5 = OptionDescription(name="general", doc="général", children=[option_6], properties=frozenset({"basic"}))
optiondescription_10 = OptionDescription(name="rougail", doc="Rougail", children=[option_4, optiondescription_5], properties=frozenset({"basic"}))
optiondescription_9 = OptionDescription(name="2", doc="2", children=[optiondescription_10])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_7, optiondescription_9])
