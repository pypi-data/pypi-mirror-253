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
option_2 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"expert", "mandatory"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"expert"}))
option_4 = ChoiceOption(name="enumvar", doc="multi", values=(None,), properties=frozenset({"expert"}))
option_4.impl_set_information('help', "bla bla bla")
optiondescription_3 = OptionDescription(name="enumfam", doc="enumfam", children=[option_4], properties=frozenset({"expert"}))
optiondescription_10 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1, optiondescription_3], properties=frozenset({"expert"}))
optiondescription_9 = OptionDescription(name="1", doc="1", children=[optiondescription_10])
option_6 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"expert", "mandatory"}))
optiondescription_5 = OptionDescription(name="general", doc="general", children=[option_6], properties=frozenset({"expert"}))
option_8 = ChoiceOption(name="enumvar", doc="multi", values=(None,), properties=frozenset({"expert"}))
option_8.impl_set_information('help', "bla bla bla")
optiondescription_7 = OptionDescription(name="enumfam", doc="enumfam", children=[option_8], properties=frozenset({"expert"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_5, optiondescription_7], properties=frozenset({"expert"}))
optiondescription_11 = OptionDescription(name="2", doc="2", children=[optiondescription_12])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_9, optiondescription_11])
