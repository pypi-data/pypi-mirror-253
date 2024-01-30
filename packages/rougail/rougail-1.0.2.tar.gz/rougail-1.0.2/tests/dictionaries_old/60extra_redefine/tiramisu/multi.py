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
option_3 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="général", children=[option_2, option_3], properties=frozenset({"normal"}))
optiondescription_16 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_5 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_6 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default=Calculation(func.calc_multi_condition, Params((ParamValue("non")), kwargs={'condition_1': ParamOption(option_3, notraisepropertyerror=True), 'match': ParamValue("none"), 'mismatch': ParamValue("daily")})), properties=frozenset({"mandatory", "normal"}))
option_7 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_4 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_5, option_6, option_7], properties=frozenset({"normal"}))
optiondescription_17 = OptionDescription(name="extra", doc="extra", children=[optiondescription_4], properties=frozenset({"normal"}))
optiondescription_15 = OptionDescription(name="1", doc="1", children=[optiondescription_16, optiondescription_17])
option_9 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_10 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_8 = OptionDescription(name="general", doc="général", children=[option_9, option_10], properties=frozenset({"normal"}))
optiondescription_19 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_8], properties=frozenset({"normal"}))
option_12 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_13 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default=Calculation(func.calc_multi_condition, Params((ParamValue("non")), kwargs={'condition_1': ParamOption(option_10, notraisepropertyerror=True), 'match': ParamValue("none"), 'mismatch': ParamValue("daily")})), properties=frozenset({"mandatory", "normal"}))
option_14 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_11 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_12, option_13, option_14], properties=frozenset({"normal"}))
optiondescription_20 = OptionDescription(name="extra", doc="extra", children=[optiondescription_11], properties=frozenset({"normal"}))
optiondescription_18 = OptionDescription(name="2", doc="2", children=[optiondescription_19, optiondescription_20])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_15, optiondescription_18])
