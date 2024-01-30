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
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
optiondescription_3 = OptionDescription(name="general", doc="général", children=[option_4], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3], properties=frozenset({"standard"}))
option_7 = IntOption(name="delay", doc="délai en minutes avant lancement", default=0, properties=frozenset({"mandatory", "standard"}))
option_8 = IntOption(name="day", doc="day avant lancement", properties=frozenset({"basic", "mandatory"}))
optiondescription_6 = OptionDescription(name="test", doc="test", children=[option_7, option_8], properties=frozenset({"basic"}))
optiondescription_5 = OptionDescription(name="extra", doc="extra", children=[optiondescription_6], properties=frozenset({"basic"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2, optiondescription_5], properties=frozenset({"basic"}))
option_12 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
optiondescription_11 = OptionDescription(name="general", doc="général", children=[option_12], properties=frozenset({"standard"}))
optiondescription_10 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_11], properties=frozenset({"standard"}))
option_15 = IntOption(name="delay", doc="délai en minutes avant lancement", default=0, properties=frozenset({"mandatory", "standard"}))
option_16 = IntOption(name="day", doc="day avant lancement", properties=frozenset({"basic", "mandatory"}))
optiondescription_14 = OptionDescription(name="test", doc="test", children=[option_15, option_16], properties=frozenset({"basic"}))
optiondescription_13 = OptionDescription(name="extra", doc="extra", children=[optiondescription_14], properties=frozenset({"basic"}))
optiondescription_9 = OptionDescription(name="2", doc="2", children=[optiondescription_10, optiondescription_13], properties=frozenset({"basic"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_9])
