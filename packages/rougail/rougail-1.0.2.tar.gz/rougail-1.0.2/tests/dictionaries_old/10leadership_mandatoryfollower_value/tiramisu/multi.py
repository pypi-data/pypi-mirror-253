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
option_4 = NetmaskOption(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", multi=True, properties=frozenset({"normal"}))
option_5 = NetworkOption(name="nut_monitor_host", doc="Adresse IP du réseau de l'esclave", multi=True, default_multi="192.168.0.0", properties=frozenset({"mandatory", "normal"}))
optiondescription_3 = Leadership(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", children=[option_4, option_5], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="general", doc="général", children=[option_2, optiondescription_3], properties=frozenset({"normal"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
optiondescription_11 = OptionDescription(name="1", doc="1", children=[optiondescription_12])
option_7 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_9 = NetmaskOption(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", multi=True, properties=frozenset({"normal"}))
option_10 = NetworkOption(name="nut_monitor_host", doc="Adresse IP du réseau de l'esclave", multi=True, default_multi="192.168.0.0", properties=frozenset({"mandatory", "normal"}))
optiondescription_8 = Leadership(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", children=[option_9, option_10], properties=frozenset({"normal"}))
optiondescription_6 = OptionDescription(name="general", doc="général", children=[option_7, optiondescription_8], properties=frozenset({"normal"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_6], properties=frozenset({"normal"}))
optiondescription_13 = OptionDescription(name="2", doc="2", children=[optiondescription_14])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_11, optiondescription_13])
