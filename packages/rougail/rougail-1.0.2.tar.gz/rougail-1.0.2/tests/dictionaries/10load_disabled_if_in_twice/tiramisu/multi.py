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
dict_env['disabled_1.rougail.my_var2'] = "{% if my_var1 is not defined %}\nmy_var1 is undefined!\n{% elif my_var1 == \"no\" %}\nmy_var1 is no\n{% endif %}\n"
dict_env['disabled_1.rougail.my_var3'] = "{% if my_var2 is not defined %}\nmy_var2 is undefined!\n{% elif my_var2 == \"no\" %}\nmy_var2 is no\n{% endif %}\n"
dict_env['disabled_2.rougail.my_var2'] = "{% if my_var1 is not defined %}\nmy_var1 is undefined!\n{% elif my_var1 == \"no\" %}\nmy_var1 is no\n{% endif %}\n"
dict_env['disabled_2.rougail.my_var3'] = "{% if my_var2 is not defined %}\nmy_var2 is undefined!\n{% elif my_var2 == \"no\" %}\nmy_var2 is no\n{% endif %}\n"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.filters = func
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"mandatory", "standard"}))
option_4 = StrOption(name="my_var2", doc="my_var2", default="no", properties=frozenset({"mandatory", "standard", Calculation(func['jinja_to_property'], Params((ParamValue("disabled")), kwargs={'__internal_jinja': ParamValue("disabled_1.rougail.my_var2"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'my_var1': ParamOption(option_3, notraisepropertyerror=True)}), help_function=func['jinja_to_property_help'])}))
option_5 = StrOption(name="my_var3", doc="my_var3", default="no", properties=frozenset({"mandatory", "standard", Calculation(func['jinja_to_property'], Params((ParamValue("disabled")), kwargs={'__internal_jinja': ParamValue("disabled_1.rougail.my_var3"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'my_var2': ParamOption(option_4, notraisepropertyerror=True)}), help_function=func['jinja_to_property_help'])}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[option_3, option_4, option_5], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2], properties=frozenset({"standard"}))
option_8 = StrOption(name="my_var1", doc="my_var1", default="no", properties=frozenset({"mandatory", "standard"}))
option_9 = StrOption(name="my_var2", doc="my_var2", default="no", properties=frozenset({"mandatory", "standard", Calculation(func['jinja_to_property'], Params((ParamValue("disabled")), kwargs={'__internal_jinja': ParamValue("disabled_2.rougail.my_var2"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'my_var1': ParamOption(option_8, notraisepropertyerror=True)}), help_function=func['jinja_to_property_help'])}))
option_10 = StrOption(name="my_var3", doc="my_var3", default="no", properties=frozenset({"mandatory", "standard", Calculation(func['jinja_to_property'], Params((ParamValue("disabled")), kwargs={'__internal_jinja': ParamValue("disabled_2.rougail.my_var3"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'my_var2': ParamOption(option_9, notraisepropertyerror=True)}), help_function=func['jinja_to_property_help'])}))
optiondescription_7 = OptionDescription(name="rougail", doc="rougail", children=[option_8, option_9, option_10], properties=frozenset({"standard"}))
optiondescription_6 = OptionDescription(name="2", doc="2", children=[optiondescription_7], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_6])
