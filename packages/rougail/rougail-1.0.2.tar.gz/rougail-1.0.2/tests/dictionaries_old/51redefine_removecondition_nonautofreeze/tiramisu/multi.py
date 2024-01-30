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
option_5 = BoolOption(name="server_deployed", doc="server_deployed", default=False, properties=frozenset({"hidden", "mandatory", "normal"}))
option_1 = StrOption(name="my_var", doc="my_var", default="no", properties=frozenset({"basic", "force_store_value", "mandatory", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_5, notraisepropertyerror=True), 'expected': ParamValue(True)}), func.calc_value_property_help)}))
option_2 = StrOption(name="condition", doc="condition", default="no", properties=frozenset({"mandatory", "normal"}))
option_3 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_4 = StrOption(name="my_var2", doc="my_var2", default="no", properties=frozenset({"mandatory", "normal"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2, option_3, option_4, option_5], properties=frozenset({"basic"}))
optiondescription_11 = OptionDescription(name="1", doc="1", children=[optiondescription_12])
option_10 = BoolOption(name="server_deployed", doc="server_deployed", default=False, properties=frozenset({"hidden", "mandatory", "normal"}))
option_6 = StrOption(name="my_var", doc="my_var", default="no", properties=frozenset({"basic", "force_store_value", "mandatory", Calculation(func.calc_value, Params(ParamValue('frozen'), kwargs={'condition': ParamOption(option_10, notraisepropertyerror=True), 'expected': ParamValue(True)}), func.calc_value_property_help)}))
option_7 = StrOption(name="condition", doc="condition", default="no", properties=frozenset({"mandatory", "normal"}))
option_8 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_9 = StrOption(name="my_var2", doc="my_var2", default="no", properties=frozenset({"mandatory", "normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[option_6, option_7, option_8, option_9, option_10], properties=frozenset({"basic"}))
optiondescription_13 = OptionDescription(name="2", doc="2", children=[optiondescription_14])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_11, optiondescription_13])
