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
option_3 = StrOption(name="condition", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
option_4 = StrOption(name="mode_conteneur_actif1", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_5 = StrOption(name="mode_conteneur_actif2", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2, option_3, option_4, option_5], properties=frozenset({"normal"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_15 = FilenameOption(name="name", doc="name", default="/etc/file")
option_16 = StrOption(name="source", doc="source", default="file")
option_14 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_13 = OptionDescription(name="file", doc="file", children=[option_15, option_16, option_14])
optiondescription_12 = OptionDescription(name="files", doc="files", children=[optiondescription_13])
option_11 = BoolOption(name="activate", doc="activate", default=True)
option_17 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_28 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_12, option_11, option_17])
optiondescription_28.impl_set_information('type', "service")
optiondescription_27 = OptionDescription(name="services", doc="services", children=[optiondescription_28], properties=frozenset({"hidden"}))
optiondescription_25 = OptionDescription(name="1", doc="1", children=[optiondescription_26, optiondescription_27])
option_7 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
option_8 = StrOption(name="condition", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
option_9 = StrOption(name="mode_conteneur_actif1", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_10 = StrOption(name="mode_conteneur_actif2", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_6 = OptionDescription(name="general", doc="general", children=[option_7, option_8, option_9, option_10], properties=frozenset({"normal"}))
optiondescription_30 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_6], properties=frozenset({"normal"}))
option_22 = FilenameOption(name="name", doc="name", default="/etc/file")
option_23 = StrOption(name="source", doc="source", default="file")
option_21 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_20 = OptionDescription(name="file", doc="file", children=[option_22, option_23, option_21])
optiondescription_19 = OptionDescription(name="files", doc="files", children=[optiondescription_20])
option_18 = BoolOption(name="activate", doc="activate", default=True)
option_24 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_32 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_19, option_18, option_24])
optiondescription_32.impl_set_information('type', "service")
optiondescription_31 = OptionDescription(name="services", doc="services", children=[optiondescription_32], properties=frozenset({"hidden"}))
optiondescription_29 = OptionDescription(name="2", doc="2", children=[optiondescription_30, optiondescription_31])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_25, optiondescription_29])
