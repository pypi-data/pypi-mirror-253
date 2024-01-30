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
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", properties=frozenset({"basic", "mandatory"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"basic"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3], properties=frozenset({"basic"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"basic"}))
option_8 = StrOption(name="mode_conteneur_actif", doc="No change", properties=frozenset({"basic", "mandatory"}))
optiondescription_7 = OptionDescription(name="general", doc="general", children=[option_8], properties=frozenset({"basic"}))
optiondescription_6 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_7], properties=frozenset({"basic"}))
optiondescription_5 = OptionDescription(name="2", doc="2", children=[optiondescription_6], properties=frozenset({"basic"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_5])
