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
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="général", children=[option_3], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_8 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_9 = FilenameOption(name="source", doc="source", default="/etc/mailname")
option_10 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="mailname", doc="mailname", children=[option_8, option_9, option_10])
option_12 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_13 = FilenameOption(name="source", doc="source", default="/etc/mailname")
option_14 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_11 = OptionDescription(name="mailname_new", doc="mailname_new", children=[option_12, option_13, option_14])
optiondescription_6 = OptionDescription(name="files", doc="files", children=[optiondescription_7, optiondescription_11])
option_15 = BoolOption(name="activate", doc="activate", default=True)
option_16 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_5 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_6, option_15, option_16])
optiondescription_5.impl_set_information('type', "service")
optiondescription_4 = OptionDescription(name="services", doc="services", children=[optiondescription_5], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_4])
