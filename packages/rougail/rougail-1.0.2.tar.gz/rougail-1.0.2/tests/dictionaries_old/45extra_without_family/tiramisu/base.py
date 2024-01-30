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
dict_env['extra.my_var'] = "{{ \"non\" | calc_multi_condition }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.compile_templates('jinja_caches', zip=None)
option_2 = StrOption(name="my_var", doc="my_var", default="rougail", properties=frozenset({"mandatory", "normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[option_2], properties=frozenset({"normal"}))
option_4 = StrOption(name="my_var", doc="my_var", default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue(extra.my_var), '__internal_type': ParamValue(string), '__internal_multi': ParamValue(False)})), properties=frozenset({"normal"}))
optiondescription_3 = OptionDescription(name="extra", doc="extra", children=[option_4], properties=frozenset({"normal"}))
option_9 = FilenameOption(name="name", doc="name", default="/etc/file")
option_10 = FilenameOption(name="source", doc="source", default="/etc/file")
option_11 = BoolOption(name="activate", doc="activate", default=True)
optiondescription_8 = OptionDescription(name="file", doc="file", children=[option_9, option_10, option_11])
optiondescription_7 = OptionDescription(name="files", doc="files", children=[optiondescription_8])
option_12 = BoolOption(name="activate", doc="activate", default=True)
option_13 = BoolOption(name="manage", doc="manage", default=True)
optiondescription_6 = OptionDescription(name="test_service", doc="test_service", children=[optiondescription_7, option_12, option_13])
optiondescription_6.impl_set_information('type', "service")
optiondescription_5 = OptionDescription(name="services", doc="services", children=[optiondescription_6], properties=frozenset({"hidden", "normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_3, optiondescription_5])
