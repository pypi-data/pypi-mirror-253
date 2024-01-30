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
option_3 = StrOption(name="my_var", doc="my_var", default="no", properties=frozenset({"mandatory", "normal"}))
option_4 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_5 = BoolOption(name="server_deployed", doc="server_deployed", default=False, properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="général", children=[option_3, option_4, option_5], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_8 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "normal"}))
option_9 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default="none", properties=frozenset({"mandatory", "normal"}))
option_10 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_7 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_8, option_9, option_10], properties=frozenset({"normal"}))
optiondescription_6 = OptionDescription(name="extra", doc="extra", children=[optiondescription_7], properties=frozenset({"normal"}))
option_13 = StrOption(name="description", doc="description", default="test", properties=frozenset({"mandatory", "normal"}))
optiondescription_12 = OptionDescription(name="external", doc="external", children=[option_13], properties=frozenset({"normal"}))
optiondescription_11 = OptionDescription(name="extra1", doc="extra1", children=[optiondescription_12], properties=frozenset({"normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_6, optiondescription_11])
