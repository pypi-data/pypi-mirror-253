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
option_2 = BoolOption(name="server_deployed", doc="No change", default=True, properties=frozenset({"mandatory", "normal"}))
option_3 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="général", children=[option_2, option_3], properties=frozenset({"normal"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_5 = StrOption(name="mode", doc="mode", default="pre", properties=frozenset({"basic", "force_store_value", "mandatory", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue(True)}), func.calc_value_property_help)}))
optiondescription_4 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_5], properties=frozenset({"basic"}))
optiondescription_13 = OptionDescription(name="extra", doc="extra", children=[optiondescription_4], properties=frozenset({"basic"}))
optiondescription_11 = OptionDescription(name="1", doc="1", children=[optiondescription_12, optiondescription_13])
option_7 = BoolOption(name="server_deployed", doc="No change", default=True, properties=frozenset({"mandatory", "normal"}))
option_8 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_6 = OptionDescription(name="general", doc="général", children=[option_7, option_8], properties=frozenset({"normal"}))
optiondescription_15 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_6], properties=frozenset({"normal"}))
option_10 = StrOption(name="mode", doc="mode", default="pre", properties=frozenset({"basic", "force_store_value", "mandatory", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_7, notraisepropertyerror=True), 'expected': ParamValue(True)}), func.calc_value_property_help)}))
optiondescription_9 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_10], properties=frozenset({"basic"}))
optiondescription_16 = OptionDescription(name="extra", doc="extra", children=[optiondescription_9], properties=frozenset({"basic"}))
optiondescription_14 = OptionDescription(name="2", doc="2", children=[optiondescription_15, optiondescription_16])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_11, optiondescription_14])
