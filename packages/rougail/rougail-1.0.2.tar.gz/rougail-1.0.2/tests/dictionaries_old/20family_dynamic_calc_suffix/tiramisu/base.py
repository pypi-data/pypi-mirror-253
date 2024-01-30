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
dict_env['rougail.dyn.vardyn'] = "{{ __suffix | calc_val }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="varname", doc="No change", multi=True, default=['val1', 'val2'], default_multi="val1", properties=frozenset({"mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3], properties=frozenset({"normal"}))
option_5 = StrOption(name="vardyn", doc="No change", default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue(rougail.dyn.vardyn), '__internal_type': ParamValue(string), '__internal_multi': ParamValue(False), '__suffix': ParamSuffix()})), properties=frozenset({"normal"}))
optiondescription_4 = ConvertDynOptionDescription(name="dyn", doc="dyn", suffixes=Calculation(func.calc_value, Params((ParamOption(option_3, notraisepropertyerror=True)))), children=[option_5], properties=frozenset({"normal"}))
option_7 = StrOption(name="newvar", doc="No change", properties=frozenset({"normal"}))
optiondescription_6 = OptionDescription(name="new", doc="new", children=[option_7], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2, optiondescription_4, optiondescription_6], properties=frozenset({"normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
