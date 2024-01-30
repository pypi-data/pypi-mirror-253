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
option_2 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="général", children=[option_2], properties=frozenset({"normal"}))
optiondescription_10 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_6 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_12 = OptionDescription(name="testsrv_service", doc="testsrv.service", children=[option_5, option_6])
optiondescription_12.impl_set_information('target', "test")
optiondescription_12.impl_set_information('engine', "none")
optiondescription_12.impl_set_information('type', "service")
optiondescription_11 = OptionDescription(name="services", doc="services", children=[optiondescription_12], properties=frozenset({"hidden"}))
optiondescription_9 = OptionDescription(name="1", doc="1", children=[optiondescription_10, optiondescription_11])
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_3 = OptionDescription(name="general", doc="général", children=[option_4], properties=frozenset({"normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_3], properties=frozenset({"normal"}))
option_7 = BoolOption(name="activate", doc="activate", default=True)
option_8 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_16 = OptionDescription(name="testsrv_service", doc="testsrv.service", children=[option_7, option_8])
optiondescription_16.impl_set_information('target', "test")
optiondescription_16.impl_set_information('engine', "none")
optiondescription_16.impl_set_information('type', "service")
optiondescription_15 = OptionDescription(name="services", doc="services", children=[optiondescription_16], properties=frozenset({"hidden"}))
optiondescription_13 = OptionDescription(name="2", doc="2", children=[optiondescription_14, optiondescription_15])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_9, optiondescription_13])
