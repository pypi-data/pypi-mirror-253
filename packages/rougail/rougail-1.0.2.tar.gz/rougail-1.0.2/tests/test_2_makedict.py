from os.path import isfile, join, isdir
from pytest import fixture
from os import listdir, mkdir, environ
from json import dump, load, dumps, loads
from pathlib import Path

environ['TIRAMISU_LOCALE'] = 'en'

from tiramisu import Config
from tiramisu.error import PropertiesOptionError


dico_dirs = 'tests/dictionaries'


test_ok = set()

for test in listdir(dico_dirs):
    if isdir(join(dico_dirs, test)):
        if isdir(join(dico_dirs, test, 'tiramisu')):
            test_ok.add(test)

debug = False
#debug = True
excludes = set([])
excludes = set([
    '80leadership_subfamily',
    '80valid_enum_variables',
])

#excludes = set(['01base_file_utfchar'])
test_ok -= excludes
#test_ok = ['01base_domainname_params']


test_ok = list(test_ok)
test_ok.sort()


@fixture(scope="module", params=test_ok)
def test_dir(request):
    return request.param


def launch_flattener(test_dir,
                     filename,
                     ):
    makedict_dir = join(test_dir, 'makedict')
    makedict_file = join(makedict_dir, 'base.json')
    makedict_before = join(makedict_dir, 'before.json')
    makedict_after = join(makedict_dir, 'after.json')
    informations_file = join(test_dir, 'informations.json')
    mandatory_file = Path(makedict_dir) / 'mandatory.json'

    modulepath = test_dir.replace('/', '.') + f'.tiramisu.{filename}'
    mod = __import__(modulepath)
    for token in modulepath.split(".")[1:]:
        mod = getattr(mod, token)
    config = Config(mod.option_0)
    # change default rights
    ro_origin = config.property.default('read_only', 'append')
    ro_append = frozenset(ro_origin - {'force_store_value'})
    rw_origin = config.property.default('read_write', 'append')
    rw_append = frozenset(rw_origin - {'force_store_value'})
    config.property.setdefault(ro_append, 'read_only', 'append')
    config.property.setdefault(rw_append, 'read_write', 'append')

    config.information.set('test_information', 'value')
    config.property.read_only()
    config.property.remove('mandatory')
    config.information.set('info', 'value')
    if isfile(informations_file):
        with open(informations_file) as informations:
            for key, value in load(informations).items():
                if filename == 'base':
                    config.option(key).information.set('test_information', value)
                else:
                    for root in ['1', '2']:
                        config.option(f'{root}.{key}').information.set('test_information', value)
    #
    config_dict = config.value.dict()
    if filename == 'base':
        if not isdir(makedict_dir):
            mkdir(makedict_dir)
        if not isfile(makedict_file) or debug:
            with open(makedict_file, 'w') as fh:
                dump(config_dict, fh, indent=4)
                fh.write('\n')
    else:
        config_dict_prefix = {'1': {}, '2': {}}
        for key, value in config_dict.items():
            prefix, path = key.split('.', 1)
            if value and isinstance(value, list) and isinstance(value[0], dict):
                new_value = []
                for dct in value:
                    new_dct = {}
                    for k, v in dct.items():
                        k = k.split('.', 1)[-1]
                        new_dct[k] = v
                    new_value.append(new_dct)
                value = new_value
            config_dict_prefix[prefix][path] = value
        assert loads(dumps(config_dict_prefix['1'])) == loads(dumps(config_dict_prefix['2']))
        config_dict = config_dict_prefix['1']
    if not isfile(makedict_file):
        raise Exception('dict is not empty')
    with open(makedict_file, 'r') as fh:
        assert load(fh) == loads(dumps(config_dict)), f"error in file {makedict_file}"
    #
    value_owner(makedict_before, config, filename)
    # deploy
    ro = config.property.default('read_only', 'append')
    ro = frozenset(list(ro) + ['force_store_value'])
    config.property.setdefault(ro, 'read_only', 'append')
    rw = config.property.default('read_write', 'append')
    rw = frozenset(list(rw) + ['force_store_value'])
    config.property.setdefault(rw, 'read_write', 'append')
    config.property.add('force_store_value')
    #
    value_owner(makedict_after, config, filename)
    #
    mandatory(mandatory_file, config.value.mandatory(), filename)


def value_owner(makedict_value_owner, config, filename):
    ret = {}
    for key in config.option.list(recursive=True):
        path = key.path()
        if not key.issymlinkoption() and key.isfollower():
            value = []
            owner = []
            for idx in range(0, key.value.len()):
                try:
                    option = config.option(path, idx)
                    value.append(option.value.get())
                    owner.append(option.owner.get())
                except PropertiesOptionError as err:
                    value.append(str(err))
                    owner.append('error')
        else:
            value = key.value.get()
            owner = key.owner.get()
        ret[path] = {'owner': owner,
                     'value': value,
                     }
    if filename == 'base':
        if not isfile(makedict_value_owner) or debug:
            with open(makedict_value_owner, 'w') as fh:
                dump(ret, fh, indent=4)
                fh.write('\n')
    else:
        ret_prefix = {'1': {}, '2': {}}
        for key, value in ret.items():
            prefix, path = key.split('.', 1)
            ret_prefix[prefix][path] = value
        assert loads(dumps(ret_prefix['1'])) == loads(dumps(ret_prefix['2']))
        ret = ret_prefix['1']
    with open(makedict_value_owner, 'r') as fh:
        assert load(fh) == loads(dumps(ret)), f"error in file {makedict_value_owner}"


def mandatory(mandatory_file, mandatories, filename):
    ret = [opt.path() for opt in mandatories]
    if not mandatory_file.is_file():
        with mandatory_file.open('w') as fh:
            dump(ret, fh)
    if filename != 'base':
        ret_prefix = {'1': [], '2': []}
        for key in ret:
            prefix, path = key.split('.', 1)
            ret_prefix[prefix].append(path)
        assert ret_prefix['1'] == ret_prefix['2']
        ret = ret_prefix['1']
    with mandatory_file.open() as fh:
        assert load(fh) == ret, f"error in file {mandatory_file}"


def test_dictionary(test_dir):
    test_dir = join(dico_dirs, test_dir)
    launch_flattener(test_dir, 'base')


def test_dictionary_multi(test_dir):
    test_dir = join(dico_dirs, test_dir)
    launch_flattener(test_dir, 'multi')
