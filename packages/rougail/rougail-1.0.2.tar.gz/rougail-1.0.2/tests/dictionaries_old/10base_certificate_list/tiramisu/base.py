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
option_2 = DomainnameOption(name="server_name", doc="server_name", default="example.net", type='domainname', allow_ip=False, properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[option_2], properties=frozenset({"normal"}))
option_7 = StrOption(name="name", doc="name", default="certificate")
option_8 = UsernameOption(name="owner", doc="owner", default="example")
option_9 = SymLinkOption(name="domain", opt=option_2)
option_10 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_6 = OptionDescription(name="certificate", doc="certificate", children=[option_7, option_8, option_9, option_10])
optiondescription_6.impl_set_information('authority', "authority")
optiondescription_6.impl_set_information('format', "cert_key")
optiondescription_6.impl_set_information('type', "client")
optiondescription_5 = OptionDescription(name="certificates", doc="certificates", children=[optiondescription_6])
option_11 = BoolOption(name="activate", doc="activate", default=True)
option_12 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_4 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_5, option_11, option_12])
optiondescription_4.impl_set_information('type', "service")
optiondescription_3 = OptionDescription(name="services", doc="services", children=[optiondescription_4], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_3])
