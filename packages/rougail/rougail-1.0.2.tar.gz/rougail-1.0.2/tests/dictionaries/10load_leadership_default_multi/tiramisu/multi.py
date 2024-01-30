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
option_4 = StrOption(name="mode_conteneur_actif", doc="leader", multi=True, default=["non"], default_multi="non", properties=frozenset({"mandatory", "notempty", "standard"}))
option_6 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"standard"}))
option_7 = StrOption(name="follower1", doc="follower1", multi=True, default_multi="value", properties=frozenset({"mandatory", "standard"}))
option_8 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"standard"}))
optiondescription_5 = Leadership(name="leader", doc="leader", children=[option_6, option_7, option_8], properties=frozenset({"standard"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4, optiondescription_5], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_12 = StrOption(name="mode_conteneur_actif", doc="leader", multi=True, default=["non"], default_multi="non", properties=frozenset({"mandatory", "notempty", "standard"}))
option_14 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"standard"}))
option_15 = StrOption(name="follower1", doc="follower1", multi=True, default_multi="value", properties=frozenset({"mandatory", "standard"}))
option_16 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"standard"}))
optiondescription_13 = Leadership(name="leader", doc="leader", children=[option_14, option_15, option_16], properties=frozenset({"standard"}))
optiondescription_11 = OptionDescription(name="general", doc="general", children=[option_12, optiondescription_13], properties=frozenset({"standard"}))
optiondescription_10 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_11], properties=frozenset({"standard"}))
optiondescription_9 = OptionDescription(name="2", doc="2", children=[optiondescription_10], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_9])
