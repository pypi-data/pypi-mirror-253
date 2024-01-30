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
dict_env['extra.ejabberd.day'] = "{{ \"non\" | calc_multi_condition(condition_1=__activer_ejabberd, match=\"none\", mismatch=\"daily\") }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
option_4 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "normal"}))
optiondescription_2 = OptionDescription(name="extra", doc="extra", children=[option_3, option_4], properties=frozenset({"normal"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"normal"}))
option_7 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "normal"}))
option_8 = ChoiceOption(name="day", doc="day", values=('none', 'daily', 'weekly', 'monthly'), default=Calculation(func.jinja_to_function, Params((), kwargs={'__internal_jinja': ParamValue(extra.ejabberd.day), '__internal_type': ParamValue(choice), '__internal_multi': ParamValue(False)})), properties=frozenset({"mandatory", "normal"}))
option_9 = ChoiceOption(name="mode", doc="mode", values=('pre', 'post'), default="pre", properties=frozenset({"mandatory", "normal"}))
optiondescription_6 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_7, option_8, option_9], properties=frozenset({"normal"}))
optiondescription_5 = OptionDescription(name="extra", doc="extra", children=[optiondescription_6], properties=frozenset({"normal"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_5])
