from tiramisu import *
from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("standard")
ALLOWED_LEADER_PROPERTIES.add("advanced")
from importlib.machinery import SourceFileLoader as _SourceFileLoader
from importlib.util import spec_from_loader as _spec_from_loader, module_from_spec as _module_from_spec
global func
func = {'calc_value': calc_value}

def _load_functions(path):
    global _SourceFileLoader, _spec_from_loader, _module_from_spec, func
    loader = _SourceFileLoader('func', path)
    spec = _spec_from_loader(loader.name, loader)
    func_ = _module_from_spec(spec)
    loader.exec_module(func_)
    for function in dir(func_):
        if function.startswith('_'):
            continue
        func[function] = getattr(func_, function)
_load_functions('tests/dictionaries/../eosfunc/test.py')
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
option_6 = NetmaskOption(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", multi=True, properties=frozenset({"standard"}))
option_7 = NetworkOption(name="nut_monitor_host", doc="Adresse IP du réseau de l'esclave", multi=True, default_multi="192.168.0.0", properties=frozenset({"mandatory", "standard"}))
optiondescription_5 = Leadership(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", children=[option_6, option_7], properties=frozenset({"standard"}))
optiondescription_3 = OptionDescription(name="general", doc="général", children=[option_4, optiondescription_5], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_11 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
option_13 = NetmaskOption(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", multi=True, properties=frozenset({"standard"}))
option_14 = NetworkOption(name="nut_monitor_host", doc="Adresse IP du réseau de l'esclave", multi=True, default_multi="192.168.0.0", properties=frozenset({"mandatory", "standard"}))
optiondescription_12 = Leadership(name="nut_monitor_netmask", doc="Masque de l'IP du réseau de l'esclave", children=[option_13, option_14], properties=frozenset({"standard"}))
optiondescription_10 = OptionDescription(name="general", doc="général", children=[option_11, optiondescription_12], properties=frozenset({"standard"}))
optiondescription_9 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_10], properties=frozenset({"standard"}))
optiondescription_8 = OptionDescription(name="2", doc="2", children=[optiondescription_9], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_8])
