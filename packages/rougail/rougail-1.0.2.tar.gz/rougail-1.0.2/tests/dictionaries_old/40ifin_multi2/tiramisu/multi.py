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
option_2 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
option_4 = StrOption(name="mode_conteneur_actif2", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_5 = StrOption(name="mode_conteneur_actif3", doc="No change", default="non", properties=frozenset({"mandatory", "normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_4, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help)}))
optiondescription_3 = OptionDescription(name="general2", doc="general2", children=[option_4, option_5], properties=frozenset({"hidden", "normal"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1, optiondescription_3], properties=frozenset({"normal"}))
optiondescription_11 = OptionDescription(name="1", doc="1", children=[optiondescription_12])
option_7 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_6 = OptionDescription(name="general", doc="general", children=[option_7], properties=frozenset({"normal"}))
option_9 = StrOption(name="mode_conteneur_actif2", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_10 = StrOption(name="mode_conteneur_actif3", doc="No change", default="non", properties=frozenset({"mandatory", "normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_7, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help), Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_9, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help)}))
optiondescription_8 = OptionDescription(name="general2", doc="general2", children=[option_9, option_10], properties=frozenset({"hidden", "normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_6, optiondescription_8], properties=frozenset({"normal"}))
optiondescription_13 = OptionDescription(name="2", doc="2", children=[optiondescription_14])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_11, optiondescription_13])
