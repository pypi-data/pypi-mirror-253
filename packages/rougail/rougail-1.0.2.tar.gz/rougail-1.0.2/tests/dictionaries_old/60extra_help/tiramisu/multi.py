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
optiondescription_30 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_5 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "normal"}))
option_6 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default=Calculation(func.calc_multi_condition, Params((ParamValue("non")), kwargs={'condition_1': ParamOption(option_3, notraisepropertyerror=True), 'match': ParamValue("none"), 'mismatch': ParamValue("daily")})), properties=frozenset({"mandatory", "normal"}))
option_6.impl_set_information('help', "Test help")
option_7 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_4 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_5, option_6, option_7], properties=frozenset({"normal"}))
optiondescription_31 = OptionDescription(name="extra", doc="extra", children=[optiondescription_4], properties=frozenset({"normal"}))
option_19 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_20 = StrOption(name="source", doc="source", default="mailname")
option_18 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_17 = OptionDescription(name="mailname", doc="mailname", children=[option_19, option_20, option_18])
optiondescription_16 = OptionDescription(name="files", doc="files", children=[optiondescription_17])
option_15 = BoolOption(name="activate", doc="activate", default=True)
option_21 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_33 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_16, option_15, option_21])
optiondescription_33.impl_set_information('type', "service")
optiondescription_32 = OptionDescription(name="services", doc="services", children=[optiondescription_33], properties=frozenset({"hidden"}))
optiondescription_29 = OptionDescription(name="1", doc="1", children=[optiondescription_30, optiondescription_31, optiondescription_32])
option_9 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_10 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_8 = OptionDescription(name="general", doc="général", children=[option_9, option_10], properties=frozenset({"normal"}))
optiondescription_35 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_8], properties=frozenset({"normal"}))
option_12 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "normal"}))
option_13 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default=Calculation(func.calc_multi_condition, Params((ParamValue("non")), kwargs={'condition_1': ParamOption(option_10, notraisepropertyerror=True), 'match': ParamValue("none"), 'mismatch': ParamValue("daily")})), properties=frozenset({"mandatory", "normal"}))
option_13.impl_set_information('help', "Test help")
option_14 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_11 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_12, option_13, option_14], properties=frozenset({"normal"}))
optiondescription_36 = OptionDescription(name="extra", doc="extra", children=[optiondescription_11], properties=frozenset({"normal"}))
option_26 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_27 = StrOption(name="source", doc="source", default="mailname")
option_25 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_24 = OptionDescription(name="mailname", doc="mailname", children=[option_26, option_27, option_25])
optiondescription_23 = OptionDescription(name="files", doc="files", children=[optiondescription_24])
option_22 = BoolOption(name="activate", doc="activate", default=True)
option_28 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_38 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_23, option_22, option_28])
optiondescription_38.impl_set_information('type', "service")
optiondescription_37 = OptionDescription(name="services", doc="services", children=[optiondescription_38], properties=frozenset({"hidden"}))
optiondescription_34 = OptionDescription(name="2", doc="2", children=[optiondescription_35, optiondescription_36, optiondescription_37])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_29, optiondescription_34])
