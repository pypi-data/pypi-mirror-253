from shutil import rmtree  #, copyfile, copytree
from os import getcwd, makedirs
from os.path import isfile, join, isdir
from pytest import fixture, raises
from os import listdir
from json import load

from rougail import RougailUpgrade, RougailConfig
from rougail.error import DictConsistencyError

#================================================
class Variable:
    description: str
#================================================
#================================================


dico_dirs = 'tests/dictionaries_old'
dest_dir = 'tmp'


test_ok = set()

for test in listdir(dico_dirs):
    if isdir(join(dico_dirs, test)):
        test_ok.add(test)

excludes = set([])
test_ok -= excludes
#test_ok = ['10load_disabled_if_in_fill']

ORI_DIR = getcwd()

debug = False
#debug = True

test_ok = list(test_ok)
test_ok.sort()
if isdir(dest_dir):
    rmtree(dest_dir)
makedirs(dest_dir)
#copyfile(join(dico_dirs, '__init__.py'), join(dest_dir, '__init__.py'))
#RougailConfig['variable_namespace'] = 'configuration'


@fixture(scope="module", params=test_ok)
def test_dir(request):
    return request.param


def launch_test(test_dir, ext):
    result_dest_dir = join(dico_dirs, test_dir.rsplit('/', 1)[1], 'result')
    new_dest_dir = join(dico_dirs, test_dir.rsplit('/', 1)[1], dest_dir)
    #FIXME
    if isdir(new_dest_dir):
        rmtree(new_dest_dir)
    rougailconfig = RougailConfig.copy()
    rougailconfig_dest = RougailConfig.copy()
    rougailconfig_dest['functions_file'] = join(dico_dirs, '../eosfunc/test.py')
    rougailconfig['dictionaries_dir'] = join(test_dir, 'xml')
    rougailconfig_dest['dictionaries_dir'] = join(new_dest_dir, 'rougail')
    rougailconfig_dest['services_dir'] = join(new_dest_dir, 'services')
    rougailconfig['extra_dictionaries'] = {}
    rougailconfig_dest['extra_dictionaries'] = {}
    if isdir(join(test_dir, ext, 'extra_dirs')):
        extras = listdir(join(test_dir, ext, 'extra_dirs'))
        extras.sort()
        for extra in extras:
            subfolder = join(test_dir, ext, 'extra_dirs', extra)
            if isdir(subfolder):
                rougailconfig['extra_dictionaries'][extra] = [subfolder]
                rougailconfig_dest['extra_dictionaries'][extra] = [join(new_dest_dir, extra)]
    upgrade = RougailUpgrade(rougailconfig=rougailconfig)
    upgrade.load_dictionaries(join(new_dest_dir, 'rougail'),
                              extra_dstfolder=new_dest_dir,
                              services_dstfolder=join(new_dest_dir, 'services'),
                              )
    ori_lists = set()
    find_files(result_dest_dir,
               [],
               ori_lists,
               )
    new_lists = set()
    find_files(new_dest_dir,
               [],
               new_lists,
               )
    assert ori_lists == new_lists
    for file in ori_lists:
        ori_filename = join(result_dest_dir, file)
        src_filename = join(new_dest_dir, file)
        with open(ori_filename) as fh:
            ori_file = fh.read()
        with open(src_filename) as fh:
            src_file = fh.read()
        assert ori_file == src_file, f'file {ori_filename} and {src_filename} are differents'
    #
    rmtree(new_dest_dir)


def find_files(dirname: str,
               root: list,
               files: set,
               ) -> None:
    for filename in listdir(dirname):
        abs_dirname = join(dirname, filename)
        root_file = root + [filename]
        if isdir(join(dirname, filename)):
            find_files(abs_dirname,
                       root_file,
                       files,
                       )
        else:
            files.add(join(*root_file))


def test_dictionary(test_dir):
    assert getcwd() == ORI_DIR
    test_dir = join(dico_dirs, test_dir)
# FIXME   for ext in ['xml', 'yml']:
#        launch_test(test_dir, ext)
    launch_test(test_dir, 'xml')
    assert getcwd() == ORI_DIR
