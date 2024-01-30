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
option_3 = StrOption(name="source_var", doc="Description", default="file", properties=frozenset({"mandatory", "normal"}))
option_4 = StrOption(name="mode_conteneur_actif", doc="Description", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3, option_4], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_9 = FilenameOption(name="name", doc="name", default="/etc/file")
option_10 = SymLinkOption(name="source", opt=option_3)
option_11 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_8 = OptionDescription(name="rougail_general_source_var", doc="rougail_general_source_var", children=[option_9, option_10, option_11])
optiondescription_7 = OptionDescription(name="files", doc="files", children=[optiondescription_8])
option_12 = BoolOption(name="activate", doc="activate", default=True)
option_13 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_6 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_7, option_12, option_13])
optiondescription_6.impl_set_information('type', "service")
optiondescription_5 = OptionDescription(name="services", doc="services", children=[optiondescription_6], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_5])
