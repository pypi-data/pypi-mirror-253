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
dict_env['mandatory_rougail.general.mode_conteneur_actif'] = "{% if rougail.general.condition == \"oui\" %}\ncondition is oui\n{% endif %}\n"
dict_env['mandatory_rougail.general.mode_conteneur_actif2'] = "{% if rougail.general.condition == \"oui\" %}\ncondition is oui\n{% endif %}\n"
ENV = SandboxedEnvironment(loader=DictLoader(dict_env), undefined=StrictUndefined)
ENV.filters = func
ENV.compile_templates('jinja_caches', zip=None)
option_3 = StrOption(name="condition", doc="No change", default="non", properties=frozenset({"mandatory", "standard"}))
option_4 = StrOption(name="mode_conteneur_actif", doc="No change", default="non", properties=frozenset({"standard", Calculation(func['jinja_to_property'], Params((ParamValue("mandatory")), kwargs={'__internal_jinja': ParamValue("mandatory_rougail.general.mode_conteneur_actif"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'rougail.general.condition': ParamOption(option_3)}), help_function=func['jinja_to_property_help'])}))
option_5 = StrOption(name="mode_conteneur_actif2", doc="No change", default="non", properties=frozenset({"standard", Calculation(func['jinja_to_property'], Params((ParamValue("mandatory")), kwargs={'__internal_jinja': ParamValue("mandatory_rougail.general.mode_conteneur_actif2"), '__internal_type': ParamValue("string"), '__internal_multi': ParamValue(False), 'rougail.general.condition': ParamOption(option_3)}), help_function=func['jinja_to_property_help'])}))
optiondescription_2 = OptionDescription(name="general", doc="general", children=[option_3, option_4, option_5], properties=frozenset({"standard"}))
optiondescription_1 = OptionDescription(name="rougail", doc="rougail", children=[optiondescription_2], properties=frozenset({"standard"}))
option_0 = OptionDescription(name="baseoption", doc="baseoption", children=[optiondescription_1])
