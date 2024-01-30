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
option_2 = StrOption(name="mode_conteneur_actif", doc="Redefine description", multi=True, default=['non'], default_multi="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
optiondescription_6 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="1", doc="1", children=[optiondescription_6])
option_4 = StrOption(name="mode_conteneur_actif", doc="Redefine description", multi=True, default=['non'], default_multi="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"normal"}))
optiondescription_8 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_3], properties=frozenset({"normal"}))
optiondescription_7 = OptionDescription(name="2", doc="2", children=[optiondescription_8])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_5, optiondescription_7])
