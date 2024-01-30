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
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
optiondescription_20 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_9 = FilenameOption(name="name", doc="name", default="/etc/file")
option_10 = StrOption(name="source", doc="source", default="file")
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="file", doc="file", children=[option_9, option_10, option_8])
optiondescription_7.impl_set_information('engine', "none")
optiondescription_6 = OptionDescription(name="files", doc="files", children=[optiondescription_7])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_11 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_22 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_6, option_5, option_11])
optiondescription_22.impl_set_information('type', "service")
optiondescription_21 = OptionDescription(name="services", doc="services", children=[optiondescription_22], properties=frozenset({"hidden"}))
optiondescription_19 = OptionDescription(name="1", doc="1", children=[optiondescription_20, optiondescription_21])
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"normal"}))
optiondescription_24 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_3], properties=frozenset({"normal"}))
option_16 = FilenameOption(name="name", doc="name", default="/etc/file")
option_17 = StrOption(name="source", doc="source", default="file")
option_15 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_14 = OptionDescription(name="file", doc="file", children=[option_16, option_17, option_15])
optiondescription_14.impl_set_information('engine', "none")
optiondescription_13 = OptionDescription(name="files", doc="files", children=[optiondescription_14])
option_12 = BoolOption(name="activate", doc="activate", default=True)
option_18 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_26 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_13, option_12, option_18])
optiondescription_26.impl_set_information('type', "service")
optiondescription_25 = OptionDescription(name="services", doc="services", children=[optiondescription_26], properties=frozenset({"hidden"}))
optiondescription_23 = OptionDescription(name="2", doc="2", children=[optiondescription_24, optiondescription_25])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_19, optiondescription_23])
