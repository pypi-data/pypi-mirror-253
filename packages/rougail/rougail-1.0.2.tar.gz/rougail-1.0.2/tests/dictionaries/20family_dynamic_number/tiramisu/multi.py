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
dict_env['default_1.rougail.new.newvar'] = "{{ rougail.dyn1.vardyn | calc_val }}"
dict_env['default_2.rougail.new.newvar'] = "{{ rougail.dyn1.vardyn | calc_val }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.filters = func
ENV.compile_templates('jinja_caches', zip=None)
option_4 = IntOption(name="varname", doc="No change", multi=True, default=[1, 2], default_multi=1, properties=frozenset({"mandatory", "notempty", "standard"}))
optiondescription_3 = OptionDescription(name="general", doc="general", children=[option_4], properties=frozenset({"standard"}))
option_6 = StrOption(name="vardyn", doc="No change", default="val", properties=frozenset({"mandatory", "standard"}))
optiondescription_5 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_4, notraisepropertyerror=True)))), children=[option_6], properties=frozenset({"standard"}))
option_8 = StrOption(name="newvar", doc="No change", default=Calculation(func['jinja_to_function'], Params((), kwargs={'__internal_jinja': ParamValue("default_1.rougail.new.newvar"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'rougail.dyn1.vardyn': ParamDynOption(option_6, 'dyn1.vardyn', optiondescription_5)})), properties=frozenset({"mandatory", "standard"}))
optiondescription_7 = OptionDescription(name="new", doc="new", children=[option_8], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3, optiondescription_5, optiondescription_7], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_12 = IntOption(name="varname", doc="No change", multi=True, default=[1, 2], default_multi=1, properties=frozenset({"mandatory", "notempty", "standard"}))
optiondescription_11 = OptionDescription(name="general", doc="general", children=[option_12], properties=frozenset({"standard"}))
option_14 = StrOption(name="vardyn", doc="No change", default="val", properties=frozenset({"mandatory", "standard"}))
optiondescription_13 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func['calc_value'], Params((ParamOption(option_12, notraisepropertyerror=True)))), children=[option_14], properties=frozenset({"standard"}))
option_16 = StrOption(name="newvar", doc="No change", default=Calculation(func['jinja_to_function'], Params((), kwargs={'__internal_jinja': ParamValue("default_2.rougail.new.newvar"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'rougail.dyn1.vardyn': ParamDynOption(option_14, 'dyn1.vardyn', optiondescription_13)})), properties=frozenset({"mandatory", "standard"}))
optiondescription_15 = OptionDescription(name="new", doc="new", children=[option_16], properties=frozenset({"standard"}))
optiondescription_10 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_11, optiondescription_13, optiondescription_15], properties=frozenset({"standard"}))
optiondescription_9 = OptionDescription(name="2", doc="2", children=[optiondescription_10], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_9])
