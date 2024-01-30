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
from jinja2 import StrictUndefined, DictLoader
from jinja2.sandbox import SandboxedEnvironment
from rougail.annotator.variable import CONVERT_OPTION
def jinja_to_function(__internal_jinja, __internal_type, __internal_multi, **kwargs):
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
    values = ENV.get_template(__internal_jinja).render(kw)
    convert = CONVERT_OPTION[__internal_type].get('func', str)
    if __internal_multi:
        return [convert(val) for val in values.split(',')]
    return convert(values)
def valid_with_jinja(value, **kwargs):
    kwargs[kwargs.pop('__internal_key')] = value
    value = jinja_to_function(__internal_type='string', __internal_multi=False, **kwargs)
    if value:
        raise ValueError(value)
func.jinja_to_function = jinja_to_function
func.valid_with_jinja = valid_with_jinja
dict_env = {}
dict_env['1.rougail.int1'] = "{% if bool %}1{% else %}2{% endif %}"
dict_env['1.rougail.int2'] = "{% if not bool %}3{% else %}4{% endif %}"
dict_env['2.rougail.int1'] = "{% if bool %}1{% else %}2{% endif %}"
dict_env['2.rougail.int2'] = "{% if not bool %}3{% else %}4{% endif %}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.compile_templates('jinja_caches', zip=None)
option_1 = BoolOption(name="bool", doc="bool", default=True, properties=frozenset({"mandatory", "normal"}))
option_2 = IntOption(name="int1", doc="int1", default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue("1.rougail.int1"), '__internal_type': ParamValue("number"), '__internal_multi': ParamValue(False), 'bool': ParamOption(option_1)})), properties=frozenset({"normal"}))
option_3 = IntOption(name="int2", doc="int2", default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue("1.rougail.int2"), '__internal_type': ParamValue("number"), '__internal_multi': ParamValue(False), 'bool': ParamOption(option_1)})), properties=frozenset({"normal"}))
optiondescription_8 = OptionDescription(name="rougail", doc="Rougail", children=[option_1, option_2, option_3], properties=frozenset({"normal"}))
optiondescription_7 = OptionDescription(name="1", doc="1", children=[optiondescription_8])
option_4 = BoolOption(name="bool", doc="bool", default=True, properties=frozenset({"mandatory", "normal"}))
option_5 = IntOption(name="int1", doc="int1", default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue("2.rougail.int1"), '__internal_type': ParamValue("number"), '__internal_multi': ParamValue(False), 'bool': ParamOption(option_4)})), properties=frozenset({"normal"}))
option_6 = IntOption(name="int2", doc="int2", default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue("2.rougail.int2"), '__internal_type': ParamValue("number"), '__internal_multi': ParamValue(False), 'bool': ParamOption(option_4)})), properties=frozenset({"normal"}))
optiondescription_10 = OptionDescription(name="rougail", doc="Rougail", children=[option_4, option_5, option_6], properties=frozenset({"normal"}))
optiondescription_9 = OptionDescription(name="2", doc="2", children=[optiondescription_10])
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_7, optiondescription_9])
