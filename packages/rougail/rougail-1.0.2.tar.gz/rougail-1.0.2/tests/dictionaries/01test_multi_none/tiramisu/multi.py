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
option_4 = StrOption(name="mode_conteneur_actif", doc="mode_conteneur_actif", default="non", properties=frozenset({"mandatory", "standard"}))
option_4.impl_set_information('test', (None, 'test1', 'test2'))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_8 = StrOption(name="mode_conteneur_actif", doc="mode_conteneur_actif", default="non", properties=frozenset({"mandatory", "standard"}))
option_8.impl_set_information('test', (None, 'test1', 'test2'))
optiondescription_7 = OptionDescription(name="general", doc="general", children=[option_8], properties=frozenset({"standard"}))
optiondescription_6 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_7], properties=frozenset({"standard"}))
optiondescription_5 = OptionDescription(name="2", doc="2", children=[optiondescription_6], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_5])
