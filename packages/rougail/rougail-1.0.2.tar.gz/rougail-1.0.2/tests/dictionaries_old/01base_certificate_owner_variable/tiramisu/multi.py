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
option_1 = UsernameOption(name="owner", doc="owner", default="example", properties=frozenset({"mandatory", "normal"}))
option_2 = DomainnameOption(name="server_name", doc="server_name", default="example.net", type='domainname', allow_ip=False, properties=frozenset({"mandatory", "normal"}))
optiondescription_22 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2], properties=frozenset({"normal"}))
option_9 = SymLinkOption(name="domain", opt=option_2)
option_10 = StrOption(name="name", doc="name", default="certificate")
option_11 = SymLinkOption(name="owner", opt=option_1)
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="certificate", doc="certificate", children=[option_9, option_10, option_11, option_8])
optiondescription_7.impl_set_information('authority', "authority")
optiondescription_7.impl_set_information('format', "cert_key")
optiondescription_7.impl_set_information('type', "client")
optiondescription_6 = OptionDescription(name="certificates", doc="certificates", children=[optiondescription_7])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_12 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_24 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_6, option_5, option_12])
optiondescription_24.impl_set_information('type', "service")
optiondescription_23 = OptionDescription(name="services", doc="services", children=[optiondescription_24], properties=frozenset({"hidden"}))
optiondescription_21 = OptionDescription(name="1", doc="1", children=[optiondescription_22, optiondescription_23])
option_3 = UsernameOption(name="owner", doc="owner", default="example", properties=frozenset({"mandatory", "normal"}))
option_4 = DomainnameOption(name="server_name", doc="server_name", default="example.net", type='domainname', allow_ip=False, properties=frozenset({"mandatory", "normal"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[option_3, option_4], properties=frozenset({"normal"}))
option_17 = SymLinkOption(name="domain", opt=option_4)
option_18 = StrOption(name="name", doc="name", default="certificate")
option_19 = SymLinkOption(name="owner", opt=option_3)
option_16 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_15 = OptionDescription(name="certificate", doc="certificate", children=[option_17, option_18, option_19, option_16])
optiondescription_15.impl_set_information('authority', "authority")
optiondescription_15.impl_set_information('format', "cert_key")
optiondescription_15.impl_set_information('type', "client")
optiondescription_14 = OptionDescription(name="certificates", doc="certificates", children=[optiondescription_15])
option_13 = BoolOption(name="activate", doc="activate", default=True)
option_20 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_28 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_14, option_13, option_20])
optiondescription_28.impl_set_information('type', "service")
optiondescription_27 = OptionDescription(name="services", doc="services", children=[optiondescription_28], properties=frozenset({"hidden"}))
optiondescription_25 = OptionDescription(name="2", doc="2", children=[optiondescription_26, optiondescription_27])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_21, optiondescription_25])
