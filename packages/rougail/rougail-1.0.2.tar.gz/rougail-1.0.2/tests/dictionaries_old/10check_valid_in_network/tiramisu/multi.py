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
option_2 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"mandatory", "normal"}))
option_3 = IPOption(name="adresse_ip_eth0", doc="Adresse IP de la carte", private_only=True, warnings_only=True, properties=frozenset({"basic", "mandatory"}))
option_4 = NetmaskOption(name="adresse_netmask_eth0", doc="Masque de sous réseau de la carte", properties=frozenset({"basic", "mandatory"}))
option_5 = IPOption(name="adresse_ip", doc="IP", validators=[Calculation(func.valid_in_network, Params((ParamSelfOption(whole=False), ParamOption(option_3), ParamOption(option_4))), warnings_only=True)], private_only=True, warnings_only=True, properties=frozenset({"basic", "mandatory"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2, option_3, option_4, option_5], properties=frozenset({"basic"}))
optiondescription_12 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"basic"}))
optiondescription_11 = OptionDescription(name="1", doc="1", children=[optiondescription_12])
option_7 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"mandatory", "normal"}))
option_8 = IPOption(name="adresse_ip_eth0", doc="Adresse IP de la carte", private_only=True, warnings_only=True, properties=frozenset({"basic", "mandatory"}))
option_9 = NetmaskOption(name="adresse_netmask_eth0", doc="Masque de sous réseau de la carte", properties=frozenset({"basic", "mandatory"}))
option_10 = IPOption(name="adresse_ip", doc="IP", validators=[Calculation(func.valid_in_network, Params((ParamSelfOption(whole=False), ParamOption(option_8), ParamOption(option_9))), warnings_only=True)], private_only=True, warnings_only=True, properties=frozenset({"basic", "mandatory"}))
optiondescription_6 = OptionDescription(name="general", doc="general", children=[option_7, option_8, option_9, option_10], properties=frozenset({"basic"}))
optiondescription_14 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_6], properties=frozenset({"basic"}))
optiondescription_13 = OptionDescription(name="2", doc="2", children=[optiondescription_14])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_11, optiondescription_13])
