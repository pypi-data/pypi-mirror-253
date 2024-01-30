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
optiondescription_36 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_9 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_10 = StrOption(name="source", doc="source", default="mailname")
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="mailname", doc="mailname", children=[option_9, option_10, option_8])
option_13 = FilenameOption(name="name", doc="name", default="/etc/eole/mailname")
option_14 = StrOption(name="source", doc="source", default="mailname")
option_12 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_11 = OptionDescription(name="mailname_1", doc="mailname_1", children=[option_13, option_14, option_12])
option_17 = FilenameOption(name="name", doc="name", default="/rougail.conf")
option_18 = StrOption(name="source", doc="source", default="rougail.conf")
option_16 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_15 = OptionDescription(name="rougail_conf", doc="rougail.conf", children=[option_17, option_18, option_16])
optiondescription_6 = OptionDescription(name="files", doc="files", children=[optiondescription_7, optiondescription_11, optiondescription_15])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_19 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_38 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_6, option_5, option_19])
optiondescription_38.impl_set_information('type', "service")
optiondescription_37 = OptionDescription(name="services", doc="services", children=[optiondescription_38], properties=frozenset({"hidden"}))
optiondescription_35 = OptionDescription(name="1", doc="1", children=[optiondescription_36, optiondescription_37])
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="oui", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_3 = OptionDescription(name="general", doc="général", children=[option_4], properties=frozenset({"normal"}))
optiondescription_40 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_3], properties=frozenset({"normal"}))
option_24 = FilenameOption(name="name", doc="name", default="/etc/mailname")
option_25 = StrOption(name="source", doc="source", default="mailname")
option_23 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_22 = OptionDescription(name="mailname", doc="mailname", children=[option_24, option_25, option_23])
option_28 = FilenameOption(name="name", doc="name", default="/etc/eole/mailname")
option_29 = StrOption(name="source", doc="source", default="mailname")
option_27 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_26 = OptionDescription(name="mailname_1", doc="mailname_1", children=[option_28, option_29, option_27])
option_32 = FilenameOption(name="name", doc="name", default="/rougail.conf")
option_33 = StrOption(name="source", doc="source", default="rougail.conf")
option_31 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_30 = OptionDescription(name="rougail_conf", doc="rougail.conf", children=[option_32, option_33, option_31])
optiondescription_21 = OptionDescription(name="files", doc="files", children=[optiondescription_22, optiondescription_26, optiondescription_30])
option_20 = BoolOption(name="activate", doc="activate", default=True)
option_34 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_42 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_21, option_20, option_34])
optiondescription_42.impl_set_information('type', "service")
optiondescription_41 = OptionDescription(name="services", doc="services", children=[optiondescription_42], properties=frozenset({"hidden"}))
optiondescription_39 = OptionDescription(name="2", doc="2", children=[optiondescription_40, optiondescription_41])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_35, optiondescription_39])
