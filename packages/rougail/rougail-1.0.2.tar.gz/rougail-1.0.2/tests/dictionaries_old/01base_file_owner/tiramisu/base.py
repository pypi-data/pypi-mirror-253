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
option_3 = StrOption(name="mode_conteneur_actif", doc="Description", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_8 = FilenameOption(name="name", doc="name", default="/etc/file")
option_9 = FilenameOption(name="source", doc="source", default="/etc/file")
option_10 = UsernameOption(name="owner", doc="owner", default="nobody")
option_11 = UsernameOption(name="group", doc="group", default="nobody")
option_12 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="file", doc="file", children=[option_8, option_9, option_10, option_11, option_12])
option_14 = FilenameOption(name="name", doc="name", default="/etc/file2")
option_15 = FilenameOption(name="source", doc="source", default="/etc/file2")
option_16 = UsernameOption(name="owner", doc="owner", default="nobody")
option_17 = UsernameOption(name="group", doc="group", default="nobody")
option_18 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_13 = OptionDescription(name="file2", doc="file2", children=[option_14, option_15, option_16, option_17, option_18])
optiondescription_13.impl_set_information('engine', "jinja")
optiondescription_6 = OptionDescription(name="files", doc="files", children=[optiondescription_7, optiondescription_13])
option_19 = BoolOption(name="activate", doc="activate", default=True)
option_20 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_5 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_6, option_19, option_20])
optiondescription_5.impl_set_information('type', "service")
optiondescription_4 = OptionDescription(name="services", doc="services", children=[optiondescription_5], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_4])
