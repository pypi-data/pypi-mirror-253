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
_load_functions('tests/dictionaries_old/../eosfunc/test.py')
try:
    from tiramisu4 import *
    from tiramisu4.setting import ALLOWED_LEADER_PROPERTIES
except:
    from tiramisu import *
    from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("normal")
ALLOWED_LEADER_PROPERTIES.add("expert")
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"expert", "mandatory"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3], properties=frozenset({"expert"}))
option_6 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"force_default_on_freeze", "frozen", "normal", "notempty"}))
option_7 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"force_default_on_freeze", "frozen", "normal"}))
option_8 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"force_default_on_freeze", "frozen", "normal"}))
optiondescription_5 = Leadership(name="leader", doc="leader", children=[option_6, option_7, option_8], properties=frozenset({"normal"}))
optiondescription_4 = OptionDescription(name="leadermode", doc="leadermode", children=[optiondescription_5], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2, optiondescription_4], properties=frozenset({"normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
