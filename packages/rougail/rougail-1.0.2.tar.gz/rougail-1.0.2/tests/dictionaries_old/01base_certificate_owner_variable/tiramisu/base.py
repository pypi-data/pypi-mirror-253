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
option_2 = UsernameOption(name="owner", doc="owner", default="example", properties=frozenset({"mandatory", "normal"}))
option_3 = DomainnameOption(name="server_name", doc="server_name", default="example.net", type='domainname', allow_ip=False, properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[option_2, option_3], properties=frozenset({"normal"}))
option_8 = StrOption(name="name", doc="name", default="certificate")
option_9 = SymLinkOption(name="owner", opt=option_2)
option_10 = SymLinkOption(name="domain", opt=option_3)
option_11 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="certificate", doc="certificate", children=[option_8, option_9, option_10, option_11])
optiondescription_7.impl_set_information('authority', "authority")
optiondescription_7.impl_set_information('format', "cert_key")
optiondescription_7.impl_set_information('type', "client")
optiondescription_6 = OptionDescription(name="certificates", doc="certificates", children=[optiondescription_7])
option_12 = BoolOption(name="activate", doc="activate", default=True)
option_13 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_5 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_6, option_12, option_13])
optiondescription_5.impl_set_information('type', "service")
optiondescription_4 = OptionDescription(name="services", doc="services", children=[optiondescription_5], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_4])
