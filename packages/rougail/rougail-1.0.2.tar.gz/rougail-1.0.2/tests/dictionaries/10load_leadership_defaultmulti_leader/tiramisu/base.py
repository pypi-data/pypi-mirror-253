from tiramisu import *
from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("standard")
ALLOWED_LEADER_PROPERTIES.add("advanced")
from importlib.machinery import SourceFileLoader as _SourceFileLoader
from importlib.util import spec_from_loader as _spec_from_loader, module_from_spec as _module_from_spec
global func
func = {'calc_value': calc_value}

def _load_functions(path):
    global _SourceFileLoader, _spec_from_loader, _module_from_spec, func
    loader = _SourceFileLoader('func', path)
    spec = _spec_from_loader(loader.name, loader)
    func_ = _module_from_spec(spec)
    loader.exec_module(func_)
    for function in dir(func_):
        if function.startswith('_'):
            continue
        func[function] = getattr(func_, function)
_load_functions('tests/dictionaries/../eosfunc/test.py')
option_3 = StrOption(name="mode_conteneur_actif", doc="leader", multi=True, default=["non"], default_multi="non", properties=frozenset({"mandatory", "notempty", "standard"}))
option_5 = StrOption(name="leader", doc="leader", multi=True, default=["value"], properties=frozenset({"mandatory", "notempty", "standard"}))
option_6 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"standard"}))
option_7 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"standard"}))
optiondescription_4 = Leadership(name="leader", doc="leader", children=[option_5, option_6, option_7], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3, optiondescription_4], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
