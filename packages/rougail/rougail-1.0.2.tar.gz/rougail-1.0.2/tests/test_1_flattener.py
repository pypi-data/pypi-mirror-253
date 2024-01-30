from pytest import fixture, raises
from os import getcwd, listdir, environ, makedirs
from os.path import isfile, join, isdir, dirname
from shutil import rmtree, copyfile
import logging

environ['TIRAMISU_LOCALE'] = 'en'

from rougail import Rougail, RougailConfig
from rougail.error import DictConsistencyError


logger = logging.getLogger()
logger.setLevel(logging.INFO)


dico_dirs = 'tests/dictionaries'

# if test_3_template.py failed, this temporary directory must be removed
tmp_dir = join(dico_dirs, 'tmp')
if isdir(tmp_dir):
    rmtree(tmp_dir)


test_ok = set()
test_raise = set()

for test in listdir(dico_dirs):
    if isdir(join(dico_dirs, test)):
        if isdir(join(dico_dirs, test, 'tiramisu')):
            test_ok.add(test)
        elif test != '__pycache__':
            test_raise.add(test)

excludes = set([])
excludes = set([
    '80leadership_subfamily',
    '80valid_enum_variables',
])
test_ok -= excludes
test_raise -= excludes
#test_ok = ['45multi_family_expert']
#test_ok = []
#test_raise = ['80auto_autofreeze']
#test_raise = []

ORI_DIR = getcwd()

debug = False
#debug = True

test_ok = list(test_ok)
test_raise = list(test_raise)
test_ok.sort()
test_raise.sort()

@fixture(scope="module", params=test_ok)
def test_dir(request):
    return request.param


@fixture(scope="module", params=test_raise)
def test_dir_error(request):
    return request.param


def get_tiramisu_filename(test_dir, subdir, multi):
    if not multi:
        filename = 'base.py'
    else:
        filename = 'multi.py'
    return join(test_dir, subdir, filename)


def load_rougail_object(test_dir, multi=False):
    rougailconfig = RougailConfig.copy()
    rougailconfig['functions_file'] = join(dico_dirs, '../eosfunc/test.py')
    dirs = [join(test_dir, 'dictionaries', 'rougail')]
    subfolder = join(test_dir, 'dictionaries', 'rougail2')
    if isdir(subfolder):
        dirs.append(subfolder)
    rougailconfig['dictionaries_dir'] = dirs
    rougailconfig['extra_dictionaries'] = {}
    extras = listdir(join(test_dir, 'dictionaries'))
    extras.sort()
    for extra in extras:
        if extra in ['rougail', 'rougail2']:
            continue
        subfolder = join(test_dir, 'dictionaries', extra)
        if isdir(subfolder):
            rougailconfig['extra_dictionaries'][extra] = [subfolder]
    rougailconfig['tiramisu_cache'] = get_tiramisu_filename(test_dir, 'tmp', multi)
    return Rougail(rougailconfig)


def save(test_dir, eolobj, multi=False):
    tiramisu_tmp = get_tiramisu_filename(test_dir, 'tmp', multi)
    tiramisu_tmp_dir = dirname(tiramisu_tmp)
    if isdir(tiramisu_tmp_dir):
        rmtree(tiramisu_tmp_dir)
    makedirs(tiramisu_tmp_dir)
    tiramisu_objects = eolobj.get_config()
    tiramisu_file = get_tiramisu_filename(test_dir, 'tiramisu', multi)
    tiramisu_dir = dirname(tiramisu_file)
    if isdir(tiramisu_dir):
        if not isfile(tiramisu_file) or debug:
            copyfile(tiramisu_tmp, tiramisu_file)
        with open(tiramisu_tmp, 'r') as fh:
            tiramisu_objects = fh.read()
        with open(tiramisu_file, 'r') as fh:
            tiramisu_objects_ori = fh.read()
        assert tiramisu_objects == tiramisu_objects_ori
    if isdir(tiramisu_tmp_dir):
        rmtree(tiramisu_tmp_dir)


def test_dictionary(test_dir):
    assert getcwd() == ORI_DIR
    test_dir_ = join(dico_dirs, test_dir)
    eolobj = load_rougail_object(test_dir_)
    if not eolobj:
        return
    save(test_dir_, eolobj)
    assert getcwd() == ORI_DIR


def test_dictionary_multi(test_dir):
    assert getcwd() == ORI_DIR
    test_dir_ = join(dico_dirs, test_dir)
    eolobj = load_rougail_object(test_dir_, multi=True)
    if not eolobj:
        return
    eolobj.add_path_prefix('1')
    eolobj.add_path_prefix('2')
    save(test_dir_, eolobj, multi=True)
    assert getcwd() == ORI_DIR


#def test_error_dictionary(test_dir_error):
#    assert getcwd() == ORI_DIR
#    test_dir = join(dico_dirs, test_dir_error)
#    errno = []
#    eolobj = load_rougail_object(test_dir)
#    if eolobj is None:
#        return
#    for i in listdir(test_dir):
#        if i.startswith('errno_'):
#            errno.append(int(i.split('_')[1]))
#    if not errno:
#        errno.append(0)
#    with raises(DictConsistencyError) as err:
#        launch_flattener(eolobj)
#        save(test_dir, eolobj)
#        msg = str(err)
#    assert err.value.errno in errno, f'expected errno: {errno}, errno: {err.value.errno}, msg: {err}'
#    assert getcwd() == ORI_DIR
