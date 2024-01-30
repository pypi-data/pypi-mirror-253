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
option_2 = StrOption(name="mode_conteneur_actif", doc="leader", multi=True, default=['non'], default_multi="non", properties=frozenset({"mandatory", "normal"}))
option_4 = StrOption(name="leader", doc="leader", multi=True, default=['leader'], properties=frozenset({"mandatory", "normal"}))
option_5 = StrOption(name="follower1", doc="follower1", multi=submulti, default_multi=['value'], properties=frozenset({"mandatory", "normal"}))
option_6 = StrOption(name="follower2", doc="follower2", multi=submulti, default_multi=['value1', 'value2'], properties=frozenset({"mandatory", "normal"}))
optiondescription_3 = Leadership(name="leader", doc="leader", children=[option_4, option_5, option_6], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2, optiondescription_3], properties=frozenset({"normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
optiondescription_13 = OptionDescription(name="1", doc="1", children=[optiondescription_14])
option_8 = StrOption(name="mode_conteneur_actif", doc="leader", multi=True, default=['non'], default_multi="non", properties=frozenset({"mandatory", "normal"}))
option_10 = StrOption(name="leader", doc="leader", multi=True, default=['leader'], properties=frozenset({"mandatory", "normal"}))
option_11 = StrOption(name="follower1", doc="follower1", multi=submulti, default_multi=['value'], properties=frozenset({"mandatory", "normal"}))
option_12 = StrOption(name="follower2", doc="follower2", multi=submulti, default_multi=['value1', 'value2'], properties=frozenset({"mandatory", "normal"}))
optiondescription_9 = Leadership(name="leader", doc="leader", children=[option_10, option_11, option_12], properties=frozenset({"normal"}))
optiondescription_7 = OptionDescription(name="general", doc="general", children=[option_8, optiondescription_9], properties=frozenset({"normal"}))
optiondescription_16 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_7], properties=frozenset({"normal"}))
optiondescription_15 = OptionDescription(name="2", doc="2", children=[optiondescription_16])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_13, optiondescription_15])
