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
option_2 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2], properties=frozenset({"normal"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_8 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_7 = OptionDescription(name="test_service", doc="test.service", children=[option_8])
optiondescription_7.impl_set_information('name', "test.service")
optiondescription_7.impl_set_information('source', "test.service")
optiondescription_6 = OptionDescription(name="overrides", doc="overrides", children=[optiondescription_7])
option_5 = BoolOption(name="activate", doc="activate", default=True)
option_9 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_28 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_6, option_5, option_9])
optiondescription_28.impl_set_information('type', "service")
option_13 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_12 = OptionDescription(name="test2_service", doc="test2.service", children=[option_13])
optiondescription_12.impl_set_information('engine', "jinja")
optiondescription_12.impl_set_information('name', "test2.service")
optiondescription_12.impl_set_information('source', "test2.service")
optiondescription_11 = OptionDescription(name="overrides", doc="overrides", children=[optiondescription_12])
option_10 = BoolOption(name="activate", doc="activate", default=True)
option_14 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_29 = OptionDescription(name="test2_service", doc="test2.service", children=[optiondescription_11, option_10, option_14])
optiondescription_29.impl_set_information('type', "service")
optiondescription_27 = OptionDescription(name="services", doc="services", children=[optiondescription_28, optiondescription_29], properties=frozenset({"hidden"}))
optiondescription_25 = OptionDescription(name="1", doc="1", children=[optiondescription_26, optiondescription_27])
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"normal"}))
optiondescription_31 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_3], properties=frozenset({"normal"}))
option_18 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_17 = OptionDescription(name="test_service", doc="test.service", children=[option_18])
optiondescription_17.impl_set_information('name', "test.service")
optiondescription_17.impl_set_information('source', "test.service")
optiondescription_16 = OptionDescription(name="overrides", doc="overrides", children=[optiondescription_17])
option_15 = BoolOption(name="activate", doc="activate", default=True)
option_19 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_33 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_16, option_15, option_19])
optiondescription_33.impl_set_information('type', "service")
option_23 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_22 = OptionDescription(name="test2_service", doc="test2.service", children=[option_23])
optiondescription_22.impl_set_information('engine', "jinja")
optiondescription_22.impl_set_information('name', "test2.service")
optiondescription_22.impl_set_information('source', "test2.service")
optiondescription_21 = OptionDescription(name="overrides", doc="overrides", children=[optiondescription_22])
option_20 = BoolOption(name="activate", doc="activate", default=True)
option_24 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_34 = OptionDescription(name="test2_service", doc="test2.service", children=[optiondescription_21, option_20, option_24])
optiondescription_34.impl_set_information('type', "service")
optiondescription_32 = OptionDescription(name="services", doc="services", children=[optiondescription_33, optiondescription_34], properties=frozenset({"hidden"}))
optiondescription_30 = OptionDescription(name="2", doc="2", children=[optiondescription_31, optiondescription_32])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_25, optiondescription_30])
