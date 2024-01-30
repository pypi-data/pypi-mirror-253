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
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "standard"}))
option_4 = StrOption(name="condition", doc="No change", default="non", properties=frozenset({"mandatory", "standard"}))
option_5 = StrOption(name="mode_conteneur_actif1", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
option_6 = StrOption(name="mode_conteneur_actif2", doc="No change", default="non", properties=frozenset({"mandatory", "standard"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3, option_4, option_5, option_6], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
