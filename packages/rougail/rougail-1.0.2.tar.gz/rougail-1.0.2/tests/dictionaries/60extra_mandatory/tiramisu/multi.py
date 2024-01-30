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
dict_env['default_1.extra.ejabberd.day'] = "{{ \"non\" | calc_multi_condition(condition_1=__activer_ejabberd, match=\"none\", mismatch=\"daily\") }}"
dict_env['default_2.extra.ejabberd.day'] = "{{ \"non\" | calc_multi_condition(condition_1=__activer_ejabberd, match=\"none\", mismatch=\"daily\") }}"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.filters = func
ENV.compile_templates('jinja_caches', zip=None)
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
option_5 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
optiondescription_3 = OptionDescription(name="general", doc="général", children=[option_4, option_5], properties=frozenset({"standard"}))
optiondescription_2 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_3], properties=frozenset({"standard"}))
option_8 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "standard"}))
option_9 = ChoiceOption(name="day", doc="day", values=("none", "daily", "weekly", "monthly"), default=Calculation(func['jinja_to_function'], Params((), kwargs={'__internal_jinja': ParamValue("default_1.extra.ejabberd.day"), '__internal_type': ParamValue("choice"), '__internal_multi': ParamValue(False), '__activer_ejabberd': ParamOption(option_5, notraisepropertyerror=True)})), properties=frozenset({"mandatory", "standard"}))
option_10 = ChoiceOption(name="mode", doc="mode", values=("pre", "post"), default="pre", properties=frozenset({"mandatory", "standard"}))
option_11 = StrOption(name="var1", doc="var1", properties=frozenset({"basic", "mandatory"}))
optiondescription_7 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_8, option_9, option_10, option_11], properties=frozenset({"basic"}))
optiondescription_6 = OptionDescription(name="extra", doc="extra", children=[optiondescription_7], properties=frozenset({"basic"}))
optiondescription_1 = OptionDescription(name="1", doc="1", children=[optiondescription_2, optiondescription_6], properties=frozenset({"basic"}))
option_15 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
option_16 = StrOption(name="activer_ejabberd", doc="No change", default="non", properties=frozenset({"force_default_on_freeze", "frozen", "hidden", "mandatory", "standard"}))
optiondescription_14 = OptionDescription(name="general", doc="général", children=[option_15, option_16], properties=frozenset({"standard"}))
optiondescription_13 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_14], properties=frozenset({"standard"}))
option_19 = StrOption(name="description", doc="description", default="Exportation de la base de ejabberd", properties=frozenset({"mandatory", "standard"}))
option_20 = ChoiceOption(name="day", doc="day", values=("none", "daily", "weekly", "monthly"), default=Calculation(func['jinja_to_function'], Params((), kwargs={'__internal_jinja': ParamValue("default_2.extra.ejabberd.day"), '__internal_type': ParamValue("choice"), '__internal_multi': ParamValue(False), '__activer_ejabberd': ParamOption(option_16, notraisepropertyerror=True)})), properties=frozenset({"mandatory", "standard"}))
option_21 = ChoiceOption(name="mode", doc="mode", values=("pre", "post"), default="pre", properties=frozenset({"mandatory", "standard"}))
option_22 = StrOption(name="var1", doc="var1", properties=frozenset({"basic", "mandatory"}))
optiondescription_18 = OptionDescription(name="ejabberd", doc="ejabberd", children=[option_19, option_20, option_21, option_22], properties=frozenset({"basic"}))
optiondescription_17 = OptionDescription(name="extra", doc="extra", children=[optiondescription_18], properties=frozenset({"basic"}))
optiondescription_12 = OptionDescription(name="2", doc="2", children=[optiondescription_13, optiondescription_17], properties=frozenset({"basic"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1, optiondescription_12])
