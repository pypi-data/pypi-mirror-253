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
dict_env['rougail.general.leader.follower1'] = "{{ \"valfill\" | calc_val }}"
dict_env['rougail.general.leader.follower2'] = "{{ rougail.general.leader.follower1 | calc_val }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"mandatory", "normal"}))
option_5 = StrOption(name="leader", doc="leader", multi=True, properties=frozenset({"normal", "notempty"}))
option_6 = StrOption(name="follower1", doc="follower1", multi=True, default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue(rougail.general.leader.follower1), '__internal_type': ParamValue(string), '__internal_multi': ParamValue(True)})), properties=frozenset({"normal"}))
option_7 = StrOption(name="follower2", doc="follower2", multi=True, default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue(rougail.general.leader.follower2), '__internal_type': ParamValue(string), '__internal_multi': ParamValue(True), 'rougail.general.leader.follower1': ParamOption(option_6)})), properties=frozenset({"expert"}))
optiondescription_4 = Leadership(name="leader", doc="leader", children=[option_5, option_6, option_7], properties=frozenset({"normal"}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3, optiondescription_4], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
