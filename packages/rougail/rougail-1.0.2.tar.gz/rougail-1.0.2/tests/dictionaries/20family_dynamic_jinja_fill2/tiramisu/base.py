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
dict_env['default_rougail.new.newvar'] = "{{ rougail.val1_dyn.vardyn }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.filters = func
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="varname", doc="varname", multi=True, default=["val1", "val2"], default_multi="val1", properties=frozenset({"mandatory", "notempty", "standard"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3], properties=frozenset({"standard"}))
option_5 = StrOption(name="vardyn", doc="vardyn", default="val", properties=frozenset({"mandatory", "standard"}))
optiondescription_4 = ConvertDynOptionDescription(name="{{ suffix }}_dyn", doc="{{ suffix }}_dyn", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_3, notraisepropertyerror=True)))), children=[option_5], properties=frozenset({"standard"}))
option_7 = StrOption(name="newvar", doc="newvar", default=Calculation(func['jinja_to_function'], Params((), kwargs={'__internal_jinja': ParamValue("default_rougail.new.newvar"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'rougail.val1_dyn.vardyn': ParamDynOption(option_5, 'val1_dyn.vardyn', optiondescription_4)})), properties=frozenset({"standard"}))
optiondescription_6 = OptionDescription(name="new", doc="new", children=[option_7], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2, optiondescription_4, optiondescription_6], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
