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
option_2 = StrOption(name="mode_conteneur_actif", doc="Description", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
optiondescription_28 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_9 = FilenameOption(name="name", doc="name", default="/etc/file")
option_10 = StrOption(name="source", doc="source", default="file")
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="file", doc="file", children=[option_9, option_10, option_8])
option_13 = FilenameOption(name="name", doc="name", default="/etc/file2")
option_14 = StrOption(name="source", doc="source", default="file2")
option_12 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_11 = OptionDescription(name="file2", doc="file2", children=[option_13, option_14, option_12])
optiondescription_11.impl_set_information('engine', "jinja")
optiondescription_6 = OptionDescription(name="files", doc="files", children=[optiondescription_7, optiondescription_11])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_15 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_30 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_6, option_5, option_15])
optiondescription_30.impl_set_information('type', "service")
optiondescription_29 = OptionDescription(name="services", doc="services", children=[optiondescription_30], properties=frozenset({"hidden"}))
optiondescription_27 = OptionDescription(name="1", doc="1", children=[optiondescription_28, optiondescription_29])
option_4 = StrOption(name="mode_conteneur_actif", doc="Description", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"normal"}))
optiondescription_32 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_3], properties=frozenset({"normal"}))
option_20 = FilenameOption(name="name", doc="name", default="/etc/file")
option_21 = StrOption(name="source", doc="source", default="file")
option_19 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_18 = OptionDescription(name="file", doc="file", children=[option_20, option_21, option_19])
option_24 = FilenameOption(name="name", doc="name", default="/etc/file2")
option_25 = StrOption(name="source", doc="source", default="file2")
option_23 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_22 = OptionDescription(name="file2", doc="file2", children=[option_24, option_25, option_23])
optiondescription_22.impl_set_information('engine', "jinja")
optiondescription_17 = OptionDescription(name="files", doc="files", children=[optiondescription_18, optiondescription_22])
option_16 = BoolOption(name="activate", doc="activate", default=True)
option_26 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_34 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_17, option_16, option_26])
optiondescription_34.impl_set_information('type', "service")
optiondescription_33 = OptionDescription(name="services", doc="services", children=[optiondescription_34], properties=frozenset({"hidden"}))
optiondescription_31 = OptionDescription(name="2", doc="2", children=[optiondescription_32, optiondescription_33])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_27, optiondescription_31])
