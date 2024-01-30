from tiramisu import *
from tiramisu.setting import ALLOWED_LEADER_PROPERTIES
ALLOWED_LEADER_PROPERTIES.add("basic")
ALLOWED_LEADER_PROPERTIES.add("standard")
ALLOWED_LEADER_PROPERTIES.add("advanced")
from importlib.machinery import SourceFileLoader as _SourceFileLoader
from importlib.util import spec_from_loader as _spec_from_loader, module_from_spec as _module_from_spec
global func
func = {'calc_value': calc_value}

def _load_functions(path):
    global _SourceFileLoader, _spec_from_loader, _module_from_spec, func
    loader = _SourceFileLoader('func', path)
    spec = _spec_from_loader(loader.name, loader)
    func_ = _module_from_spec(spec)
    loader.exec_module(func_)
    for function in dir(func_):
        if function.startswith('_'):
            continue
        func[function] = getattr(func_, function)
_load_functions('tests/dictionaries/../eosfunc/test.py')
from jinja2 import StrictUndefined, DictLoader
from jinja2.sandbox import SandboxedEnvironment
from rougail.annotator.variable import CONVERT_OPTION
from tiramisu.error import ValueWarning
def jinja_to_function(__internal_jinja, __internal_type, __internal_multi, **kwargs):
    global ENV, CONVERT_OPTION
    kw = {}
    for key, value in kwargs.items():
        if '.' in key:
            c_kw = kw
            path, var = key.rsplit('.', 1)
            for subkey in path.split('.'):
                c_kw = c_kw.setdefault(subkey, {})
            c_kw[var] = value
        else:
            kw[key] = value
    values = ENV.get_template(__internal_jinja).render(kw, **func).strip()
    convert = CONVERT_OPTION[__internal_type].get('func', str)
    if __internal_multi:
        return [convert(val) for val in values.split()]
    values = convert(values)
    return values if values != '' and values != 'None' else None
def variable_to_property(prop, value):
    return prop if value else None
def jinja_to_property(prop, **kwargs):
    value = func['jinja_to_function'](**kwargs)
    return func['variable_to_property'](prop, value is not None)
def jinja_to_property_help(prop, **kwargs):
    value = func['jinja_to_function'](**kwargs)
    return (prop, f'"{prop}" ({value})')
def valid_with_jinja(warnings_only=False, **kwargs):
    global ValueWarning
    value = func['jinja_to_function'](**kwargs)
    if value:
       if warnings_only:
           raise ValueWarning(value)
       else:
           raise ValueError(value)
func['jinja_to_function'] = jinja_to_function
func['jinja_to_property'] = jinja_to_property
func['jinja_to_property_help'] = jinja_to_property_help
func['variable_to_property'] = variable_to_property
func['valid_with_jinja'] = valid_with_jinja
dict_env = {}
from rougail.tiramisu import ConvertDynOptionDescription
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.filters = func
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="varname", doc="varname", multi=True, default=["val1", "val2"], default_multi="val1", properties=frozenset({"mandatory", "notempty", "standard"}))
option_5 = StrOption(name="my_dyn_var", doc="my_dyn_var", default=Calculation(func['calc_value'], Params((ParamSuffix()))), properties=frozenset({"standard"}))
optiondescription_4 = ConvertDynOptionDescription(name="my_dyn_family_", doc="Describe ", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_3, notraisepropertyerror=True)))), children=[option_5], properties=frozenset({"standard"}))
option_6 = StrOption(name="all_dyn_var", doc="all_dyn_var", default=Calculation(func['calc_value'], Params((ParamDynOption(option_5, 'my_dyn_family_val1.my_dyn_var', optiondescription_4)))), properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[option_3, optiondescription_4, option_6], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_9 = StrOption(name="varname", doc="varname", multi=True, default=["val1", "val2"], default_multi="val1", properties=frozenset({"mandatory", "notempty", "standard"}))
option_11 = StrOption(name="my_dyn_var", doc="my_dyn_var", default=Calculation(func['calc_value'], Params((ParamSuffix()))), properties=frozenset({"standard"}))
optiondescription_10 = ConvertDynOptionDescription(name="my_dyn_family_", doc="Describe ", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_9, notraisepropertyerror=True)))), children=[option_11], properties=frozenset({"standard"}))
option_12 = StrOption(name="all_dyn_var", doc="all_dyn_var", default=Calculation(func['calc_value'], Params((ParamDynOption(option_11, 'my_dyn_family_val1.my_dyn_var', optiondescription_10)))), properties=frozenset({"standard"}))
optiondescription_8 = OptionDescription(name="rougail", doc="rougail", children=[option_9, optiondescription_10, option_12], properties=frozenset({"standard"}))
optiondescription_7 = OptionDescription(name="2", doc="2", children=[optiondescription_8], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_7])
