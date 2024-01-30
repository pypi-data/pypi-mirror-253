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
optiondescription_38 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_6 = StrOption(name="description", doc="description", multi=True, default=['test'], properties=frozenset({"mandatory", "normal"}))
option_7 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), multi=True, default_multi="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_5 = Leadership(name="description", doc="description", children=[option_6, option_7], properties=frozenset({"normal"}))
optiondescription_4 = OptionDescription(name="ejabberd", doc="ejabberd", children=[optiondescription_5], properties=frozenset({"normal"}))
optiondescription_39 = OptionDescription(name="extra", doc="extra", children=[optiondescription_4], properties=frozenset({"normal"}))
option_19 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_20 = StrOption(name="source", doc="source", default="mailname")
option_18 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_17 = OptionDescription(name="mailname", doc="mailname", children=[option_19, option_20, option_18])
option_23 = FilenameOption(name="name", doc="name", default="/etc/mailname2")
option_24 = StrOption(name="source", doc="source", default="mailname2")
option_22 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_21 = OptionDescription(name="mailname2", doc="mailname2", children=[option_23, option_24, option_22])
optiondescription_21.impl_set_information('engine', "jinja")
optiondescription_16 = OptionDescription(name="files", doc="files", children=[optiondescription_17, optiondescription_21])
option_15 = BoolOption(name="activate", doc="activate", default=True)
option_25 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_41 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_16, option_15, option_25])
optiondescription_41.impl_set_information('type', "service")
optiondescription_40 = OptionDescription(name="services", doc="services", children=[optiondescription_41], properties=frozenset({"hidden"}))
optiondescription_37 = OptionDescription(name="1", doc="1", children=[optiondescription_38, optiondescription_39, optiondescription_40])
option_9 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_10 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_8 = OptionDescription(name="general", doc="général", children=[option_9, option_10], properties=frozenset({"normal"}))
optiondescription_43 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_8], properties=frozenset({"normal"}))
option_13 = StrOption(name="description", doc="description", multi=True, default=['test'], properties=frozenset({"mandatory", "normal"}))
option_14 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), multi=True, default_multi="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_12 = Leadership(name="description", doc="description", children=[option_13, option_14], properties=frozenset({"normal"}))
optiondescription_11 = OptionDescription(name="ejabberd", doc="ejabberd", children=[optiondescription_12], properties=frozenset({"normal"}))
optiondescription_44 = OptionDescription(name="extra", doc="extra", children=[optiondescription_11], properties=frozenset({"normal"}))
option_30 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_31 = StrOption(name="source", doc="source", default="mailname")
option_29 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_28 = OptionDescription(name="mailname", doc="mailname", children=[option_30, option_31, option_29])
option_34 = FilenameOption(name="name", doc="name", default="/etc/mailname2")
option_35 = StrOption(name="source", doc="source", default="mailname2")
option_33 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_32 = OptionDescription(name="mailname2", doc="mailname2", children=[option_34, option_35, option_33])
optiondescription_32.impl_set_information('engine', "jinja")
optiondescription_27 = OptionDescription(name="files", doc="files", children=[optiondescription_28, optiondescription_32])
option_26 = BoolOption(name="activate", doc="activate", default=True)
option_36 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_46 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_27, option_26, option_36])
optiondescription_46.impl_set_information('type', "service")
optiondescription_45 = OptionDescription(name="services", doc="services", children=[optiondescription_46], properties=frozenset({"hidden"}))
optiondescription_42 = OptionDescription(name="2", doc="2", children=[optiondescription_43, optiondescription_44, optiondescription_45])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_37, optiondescription_42])
