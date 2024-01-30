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
option_2 = FilenameOption(name="file_name", doc="file_name", multi=True, default=['/etc/mailname', '/etc/mailname2'], default_multi="/etc/mailname", properties=frozenset({"mandatory", "normal"}))
option_3 = FilenameOption(name="file_name2", doc="file_name2", multi=True, default=['/etc/mailname3', '/etc/mailname4'], default_multi="/etc/mailname3", properties=frozenset({"mandatory", "normal"}))
option_4 = StrOption(name="var", doc="var", multi=True, default=['mailname', 'mailname2'], default_multi="mailname", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[option_2, option_3, option_4], properties=frozenset({"normal"}))
option_9 = FilenameOption(name="name", doc="name", default="rougail.file_name")
option_10 = FilenameOption(name="source", doc="source", default="rougail.file_name")
option_11 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_8 = OptionDescription(name="mailname", doc="mailname", children=[option_9, option_10, option_11])
option_13 = FilenameOption(name="name", doc="name", default="rougail.file_name2")
option_14 = FilenameOption(name="source", doc="source", default="rougail.file_name2")
option_15 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_12 = OptionDescription(name="mailname2", doc="mailname2", children=[option_13, option_14, option_15])
optiondescription_12.impl_set_information('engine', "jinja")
optiondescription_7 = OptionDescription(name="files", doc="files", children=[optiondescription_8, optiondescription_12])
option_16 = BoolOption(name="activate", doc="activate", default=True)
option_17 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_6 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_7, option_16, option_17])
optiondescription_6.impl_set_information('type', "service")
optiondescription_5 = OptionDescription(name="services", doc="services", children=[optiondescription_6], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_5])
