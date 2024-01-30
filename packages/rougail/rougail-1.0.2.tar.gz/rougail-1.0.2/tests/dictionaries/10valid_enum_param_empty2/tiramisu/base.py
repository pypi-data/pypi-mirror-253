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
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"advanced", "mandatory"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3], properties=frozenset({"advanced"}))
option_5 = ChoiceOption(name="enumvar", doc="multi", values=(None,), properties=frozenset({"advanced"}))
option_5.impl_set_information('help', "bla bla bla")
optiondescription_4 = OptionDescription(name="enumfam", doc="enumfam", children=[option_5], properties=frozenset({"advanced"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2, optiondescription_4], properties=frozenset({"advanced"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
