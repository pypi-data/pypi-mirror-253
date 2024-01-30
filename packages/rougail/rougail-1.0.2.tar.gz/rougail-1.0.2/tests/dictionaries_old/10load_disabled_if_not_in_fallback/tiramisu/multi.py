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
option_2 = StrOption(name="condition", doc="No change", default="no", properties=frozenset({"mandatory", "normal"}))
option_3 = StrOption(name="disable_variable", doc="No change", default="no", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2, option_3], properties=frozenset({"normal"}))
optiondescription_22 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_11 = FilenameOption(name="name", doc="name", default="/tmp/file1")
option_12 = StrOption(name="source", doc="source", default="file1")
option_10 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_9 = OptionDescription(name="file1", doc="file1", children=[option_11, option_12, option_10])
optiondescription_8 = OptionDescription(name="files", doc="files", children=[optiondescription_9])
option_7 = BoolOption(name="activate", doc="activate", default=True)
option_13 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_24 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_8, option_7, option_13])
optiondescription_24.impl_set_information('type', "service")
optiondescription_23 = OptionDescription(name="services", doc="services", children=[optiondescription_24], properties=frozenset({"hidden"}))
optiondescription_21 = OptionDescription(name="1", doc="1", children=[optiondescription_22, optiondescription_23])
option_5 = StrOption(name="condition", doc="No change", default="no", properties=frozenset({"mandatory", "normal"}))
option_6 = StrOption(name="disable_variable", doc="No change", default="no", properties=frozenset({"mandatory", "normal"}))
optiondescription_4 = OptionDescription(name="general", doc="general", children=[option_5, option_6], properties=frozenset({"normal"}))
optiondescription_26 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_4], properties=frozenset({"normal"}))
option_18 = FilenameOption(name="name", doc="name", default="/tmp/file1")
option_19 = StrOption(name="source", doc="source", default="file1")
option_17 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_16 = OptionDescription(name="file1", doc="file1", children=[option_18, option_19, option_17])
optiondescription_15 = OptionDescription(name="files", doc="files", children=[optiondescription_16])
option_14 = BoolOption(name="activate", doc="activate", default=True)
option_20 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_28 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_15, option_14, option_20])
optiondescription_28.impl_set_information('type', "service")
optiondescription_27 = OptionDescription(name="services", doc="services", children=[optiondescription_28], properties=frozenset({"hidden"}))
optiondescription_25 = OptionDescription(name="2", doc="2", children=[optiondescription_26, optiondescription_27])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_21, optiondescription_25])
