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
option_5 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('force_default_on_freeze'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
option_6 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('force_default_on_freeze'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
option_7 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('force_default_on_freeze'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
optiondescription_4 = Leadership(name="leader", doc="leader", children=[option_5, option_6, option_7], properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('hidden'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
optiondescription_3 = OptionDescription(name="leadermode", doc="leadermode", children=[optiondescription_4], properties=frozenset({"normal"}))
optiondescription_16 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1, optiondescription_3], properties=frozenset({"normal"}))
optiondescription_15 = OptionDescription(name="1", doc="1", children=[optiondescription_16])
option_9 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"expert", "mandatory"}))
optiondescription_8 = OptionDescription(name="general", doc="general", children=[option_9], properties=frozenset({"expert"}))
option_12 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('force_default_on_freeze'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
option_13 = StrOption(name="follower1", doc="follower1", multi=True, properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('force_default_on_freeze'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
option_14 = StrOption(name="follower2", doc="follower2", multi=True, properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('force_default_on_freeze'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
optiondescription_11 = Leadership(name="leader", doc="leader", children=[option_12, option_13, option_14], properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('hidden'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
optiondescription_10 = OptionDescription(name="leadermode", doc="leadermode", children=[optiondescription_11], properties=frozenset({"normal"}))
optiondescription_18 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_8, optiondescription_10], properties=frozenset({"normal"}))
optiondescription_17 = OptionDescription(name="2", doc="2", children=[optiondescription_18])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_15, optiondescription_17])
