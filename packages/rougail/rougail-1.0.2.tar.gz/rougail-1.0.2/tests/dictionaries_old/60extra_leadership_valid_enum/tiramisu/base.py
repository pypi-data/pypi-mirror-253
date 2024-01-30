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
_load_functions('tests/dictionaries_old/../eosfunc/test.py')
try:
    from tiramisu4 import *
    from tiramisu4.setting import ALLOWED_LEADER_PROPERTIES
except:
    from tiramisu import *
    from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("normal")
ALLOWED_LEADER_PROPERTIES.add("expert")
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_4 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="général", children=[option_3, option_4], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_8 = StrOption(name="description", doc="description", multi=True, default=['test'], properties=frozenset({"mandatory", "normal"}))
option_9 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), multi=True, default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_7 = Leadership(name="description", doc="description", children=[option_8, option_9], properties=frozenset({"normal"}))
optiondescription_6 = OptionDescription(name="ejabberd", doc="ejabberd", children=[optiondescription_7], properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="extra", doc="extra", children=[optiondescription_6], properties=frozenset({"normal"}))
option_14 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_15 = FilenameOption(name="source", doc="source", default="/etc/mailname")
option_16 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_13 = OptionDescription(name="mailname", doc="mailname", children=[option_14, option_15, option_16])
option_18 = FilenameOption(name="name", doc="name", default="/etc/mailname2")
option_19 = FilenameOption(name="source", doc="source", default="/etc/mailname2")
option_20 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_17 = OptionDescription(name="mailname2", doc="mailname2", children=[option_18, option_19, option_20])
optiondescription_17.impl_set_information('engine', "jinja")
optiondescription_12 = OptionDescription(name="files", doc="files", children=[optiondescription_13, optiondescription_17])
option_21 = BoolOption(name="activate", doc="activate", default=True)
option_22 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_11 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_12, option_21, option_22])
optiondescription_11.impl_set_information('type', "service")
optiondescription_10 = OptionDescription(name="services", doc="services", children=[optiondescription_11], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_5, optiondescription_10])
