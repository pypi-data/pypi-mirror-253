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
option_2 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
option_5 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal"}))
option_6 = StrOption(name="follower1", doc="follower1", multi=True, default=Calculation(func.calc_val, Params((), kwargs={'valeur': ParamValue("valfill")})), properties=frozenset({"normal"}))
option_7 = StrOption(name="follower2", doc="follower2", multi=True, default=Calculation(func.calc_val, Params((ParamOption(option_6)))), properties=frozenset({"normal"}))
optiondescription_4 = Leadership(name="leader", doc="leader", children=[option_5, option_6, option_7], properties=frozenset({"normal"}))
option_9 = StrOption(name="leader1", doc="leader", multi=True, properties=frozenset({"normal"}))
option_10 = StrOption(name="follower11", doc="follower1", multi=True, properties=frozenset({"normal"}))
option_11 = StrOption(name="follower21", doc="follower2", multi=True, properties=frozenset({"normal"}))
optiondescription_8 = Leadership(name="leader1", doc="leader", children=[option_9, option_10, option_11], properties=frozenset({"normal"}))
optiondescription_3 = OptionDescription(name="general1", doc="general1", children=[optiondescription_4, optiondescription_8], properties=frozenset({"normal"}))
optiondescription_24 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1, optiondescription_3], properties=frozenset({"normal"}))
optiondescription_23 = OptionDescription(name="1", doc="1", children=[optiondescription_24])
option_13 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_12 = OptionDescription(name="general", doc="general", children=[option_13], properties=frozenset({"normal"}))
option_16 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal"}))
option_17 = StrOption(name="follower1", doc="follower1", multi=True, default=Calculation(func.calc_val, Params((), kwargs={'valeur': ParamValue("valfill")})), properties=frozenset({"normal"}))
option_18 = StrOption(name="follower2", doc="follower2", multi=True, default=Calculation(func.calc_val, Params((ParamOption(option_17)))), properties=frozenset({"normal"}))
optiondescription_15 = Leadership(name="leader", doc="leader", children=[option_16, option_17, option_18], properties=frozenset({"normal"}))
option_20 = StrOption(name="leader1", doc="leader", multi=True, properties=frozenset({"normal"}))
option_21 = StrOption(name="follower11", doc="follower1", multi=True, properties=frozenset({"normal"}))
option_22 = StrOption(name="follower21", doc="follower2", multi=True, properties=frozenset({"normal"}))
optiondescription_19 = Leadership(name="leader1", doc="leader", children=[option_20, option_21, option_22], properties=frozenset({"normal"}))
optiondescription_14 = OptionDescription(name="general1", doc="general1", children=[optiondescription_15, optiondescription_19], properties=frozenset({"normal"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_12, optiondescription_14], properties=frozenset({"normal"}))
optiondescription_25 = OptionDescription(name="2", doc="2", children=[optiondescription_26])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_23, optiondescription_25])
