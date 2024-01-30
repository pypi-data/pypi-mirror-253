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
option_2 = StrOption(name="condition", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help)}))
option_4 = StrOption(name="mode_conteneur_actif2", doc="No change", default="non", properties=frozenset({"mandatory", "normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_2, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help)}))
optiondescription_1 = OptionDescription(name="general", doc="general", children=[option_2, option_3, option_4], properties=frozenset({"normal"}))
optiondescription_32 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_1], properties=frozenset({"normal"}))
option_13 = FilenameOption(name="name", doc="name", default="/tmp/file1")
option_14 = StrOption(name="source", doc="source", default="file1")
option_12 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_2, notraisepropertyerror=True), 'expected_0': ParamValue("oui")})))
optiondescription_11 = OptionDescription(name="file1", doc="file1", children=[option_13, option_14, option_12])
option_17 = FilenameOption(name="name", doc="name", default="/tmp/file2")
option_18 = StrOption(name="source", doc="source", default="file2")
option_16 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_2, notraisepropertyerror=True), 'expected_0': ParamValue("oui")})))
optiondescription_15 = OptionDescription(name="file2", doc="file2", children=[option_17, option_18, option_16])
optiondescription_10 = OptionDescription(name="files", doc="files", children=[optiondescription_11, optiondescription_15])
option_9 = BoolOption(name="activate", doc="activate", default=True)
option_19 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_34 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_10, option_9, option_19])
optiondescription_34.impl_set_information('type', "service")
optiondescription_33 = OptionDescription(name="services", doc="services", children=[optiondescription_34], properties=frozenset({"hidden"}))
optiondescription_31 = OptionDescription(name="1", doc="1", children=[optiondescription_32, optiondescription_33])
option_6 = StrOption(name="condition", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
option_7 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_6, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help)}))
option_8 = StrOption(name="mode_conteneur_actif2", doc="No change", default="non", properties=frozenset({"mandatory", "normal", Calculation(func.calc_value, Params(ParamValue('disabled'), kwargs={'condition': ParamOption(option_6, notraisepropertyerror=True), 'expected': ParamValue("oui")}), func.calc_value_property_help)}))
optiondescription_5 = OptionDescription(name="general", doc="general", children=[option_6, option_7, option_8], properties=frozenset({"normal"}))
optiondescription_36 = OptionDescription(name="rougail", doc="Rougail", children=[optiondescription_5], properties=frozenset({"normal"}))
option_24 = FilenameOption(name="name", doc="name", default="/tmp/file1")
option_25 = StrOption(name="source", doc="source", default="file1")
option_23 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_6, notraisepropertyerror=True), 'expected_0': ParamValue("oui")})))
optiondescription_22 = OptionDescription(name="file1", doc="file1", children=[option_24, option_25, option_23])
option_28 = FilenameOption(name="name", doc="name", default="/tmp/file2")
option_29 = StrOption(name="source", doc="source", default="file2")
option_27 = BoolOption(name="activate", doc="activate", default=Calculation(func.calc_value, Params((ParamValue(False)), kwargs={'default': ParamValue(True), 'condition_0': ParamOption(option_6, notraisepropertyerror=True), 'expected_0': ParamValue("oui")})))
optiondescription_26 = OptionDescription(name="file2", doc="file2", children=[option_28, option_29, option_27])
optiondescription_21 = OptionDescription(name="files", doc="files", children=[optiondescription_22, optiondescription_26])
option_20 = BoolOption(name="activate", doc="activate", default=True)
option_30 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_38 = OptionDescription(name="test_service", doc="test.service", children=[optiondescription_21, option_20, option_30])
optiondescription_38.impl_set_information('type', "service")
optiondescription_37 = OptionDescription(name="services", doc="services", children=[optiondescription_38], properties=frozenset({"hidden"}))
optiondescription_35 = OptionDescription(name="2", doc="2", children=[optiondescription_36, optiondescription_37])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_31, optiondescription_35])
