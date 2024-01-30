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
option_1 = DomainnameOption(name="server_name", doc="server_name", default="example.net", type='domainname', allow_ip=False, properties=frozenset({"mandatory", "normal"}))
optiondescription_20 = OptionDescription(name="rougail", doc="Rougail", children=[option_1], properties=frozenset({"normal"}))
option_7 = SymLinkOption(name="domain", opt=option_1)
option_8 = StrOption(name="name", doc="name", default="certificate")
option_9 = UsernameOption(name="owner", doc="owner", default="example")
option_6 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_1, notraisepropertyerror=True), 'expected_0': ParamValue("example.net")})))
optiondescription_5 = OptionDescription(name="certificate", doc="certificate", children=[option_7, option_8, option_9, option_6])
optiondescription_5.impl_set_information('authority', "authority")
optiondescription_5.impl_set_information('format', "cert_key")
optiondescription_5.impl_set_information('type', "client")
optiondescription_4 = OptionDescription(name="certificates", doc="certificates", children=[optiondescription_5])
option_3 = BoolOption(name="activate", doc="activate", default=True)
option_10 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_22 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_4, option_3, option_10])
optiondescription_22.impl_set_information('type', "service")
optiondescription_21 = OptionDescription(name="services", doc="services", children=[optiondescription_22], properties=frozenset({"hidden"}))
optiondescription_19 = OptionDescription(name="1", doc="1", children=[optiondescription_20, optiondescription_21])
option_2 = DomainnameOption(name="server_name", doc="server_name", default="example.net", type='domainname', allow_ip=False, properties=frozenset({"mandatory", "normal"}))
optiondescription_24 = OptionDescription(name="rougail", doc="Rougail", children=[option_2], properties=frozenset({"normal"}))
option_15 = SymLinkOption(name="domain", opt=option_2)
option_16 = StrOption(name="name", doc="name", default="certificate")
option_17 = UsernameOption(name="owner", doc="owner", default="example")
option_14 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_2, notraisepropertyerror=True), 'expected_0': ParamValue("example.net")})))
optiondescription_13 = OptionDescription(name="certificate", doc="certificate", children=[option_15, option_16, option_17, option_14])
optiondescription_13.impl_set_information('authority', "authority")
optiondescription_13.impl_set_information('format', "cert_key")
optiondescription_13.impl_set_information('type', "client")
optiondescription_12 = OptionDescription(name="certificates", doc="certificates", children=[optiondescription_13])
option_11 = BoolOption(name="activate", doc="activate", default=True)
option_18 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_26 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_12, option_11, option_18])
optiondescription_26.impl_set_information('type', "service")
optiondescription_25 = OptionDescription(name="services", doc="services", children=[optiondescription_26], properties=frozenset({"hidden"}))
optiondescription_23 = OptionDescription(name="2", doc="2", children=[optiondescription_24, optiondescription_25])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_19, optiondescription_23])
