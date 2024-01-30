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
option_4 = BoolOption(name="server_deployed", doc="server_deployed", default=False, properties=frozenset({"hidden", "mandatory", "normal"}))
option_2 = StrOption(name="my_var", doc="my_var", default="no", properties=frozenset({"basic", "force_store_value", "mandatory", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_4, notraisepropertyerror=True), 'expected': ParamValue(True)}), func.calc_value_property_help)}))
option_3 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="général", children=[option_2, option_3, option_4], properties=frozenset({"basic"}))
optiondescription_22 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"basic"}))
option_6 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "normal"}))
option_7 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default="none", properties=frozenset({"mandatory", "normal"}))
option_8 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_5 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_6, option_7, option_8], properties=frozenset({"normal"}))
optiondescription_23 = OptionDescription(name="extra", doc="extra", children=[optiondescription_5], properties=frozenset({"normal"}))
option_10 = StrOption(name="description", doc="description", default="test", properties=frozenset({"mandatory", "normal"}))
optiondescription_9 = OptionDescription(name="external", doc="external", children=[option_10], properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_6, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
optiondescription_24 = OptionDescription(name="extra1", doc="extra1", children=[optiondescription_9], properties=frozenset({"normal"}))
optiondescription_21 = OptionDescription(name="1", doc="1", children=[optiondescription_22, optiondescription_23, optiondescription_24])
option_14 = BoolOption(name="server_deployed", doc="server_deployed", default=False, properties=frozenset({"hidden", "mandatory", "normal"}))
option_12 = StrOption(name="my_var", doc="my_var", default="no", properties=frozenset({"basic", "force_store_value", "mandatory", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_14, notraisepropertyerror=True), 'expected': ParamValue(True)}), func.calc_value_property_help)}))
option_13 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_11 = OptionDescription(name="general", doc="général", children=[option_12, option_13, option_14], properties=frozenset({"basic"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_11], properties=frozenset({"basic"}))
option_16 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "normal"}))
option_17 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default="none", properties=frozenset({"mandatory", "normal"}))
option_18 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_15 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_16, option_17, option_18], properties=frozenset({"normal"}))
optiondescription_27 = OptionDescription(name="extra", doc="extra", children=[optiondescription_15], properties=frozenset({"normal"}))
option_20 = StrOption(name="description", doc="description", default="test", properties=frozenset({"mandatory", "normal"}))
optiondescription_19 = OptionDescription(name="external", doc="external", children=[option_20], properties=frozenset({"normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_16, notraisepropertyerror=True), 'expected': ParamValue("non")}), func.calc_value_property_help)}))
optiondescription_28 = OptionDescription(name="extra1", doc="extra1", children=[optiondescription_19], properties=frozenset({"normal"}))
optiondescription_25 = OptionDescription(name="2", doc="2", children=[optiondescription_26, optiondescription_27, optiondescription_28])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_21, optiondescription_25])
