from pathlib import Path
from pytest import fixture, raises
from shutil import rmtree
from rougail import Rougail, RougailConfig

doc = Path('doc')
tests = Path('tests')
tmp = tests / 'tmp'
RougailConfig['dictionaries_dir'] = [str(tmp)]
RougailConfig['functions_file'] = str(tests / 'eosfunc' / 'test.py')


scripts = {}
for filename in doc.glob('*/*.md'):
    filename = str(filename)
    with open(filename) as fh:
        yaml = False
        redefine = False
        new_script = ''
        for line in fh.readlines():
            if new_script and line == '```\n':
                scripts.setdefault(filename, [])
                if redefine:
                    scripts[filename][-1].append(new_script)
                else:
                    scripts[filename].append([new_script])
                yaml = False
                redefine = False
            if yaml:
                if line.strip() == 'redefine: true':
                    redefine = True
                new_script += line
            if line == '```yml\n':
                yaml = True
                new_script = ''
scripts_list = [(filename, script) for filename, scripts_ in scripts.items() for script in scripts_]


@fixture(scope="module", params=scripts_list)
def test_dir(request):
    return request.param


def test_scripts(test_dir):
    if tmp.is_dir():
        rmtree(tmp)
    tmp.mkdir()
    for idx, content in enumerate(test_dir[1]):
        if not content.startswith('---'):
            raise Exception(f'not a valid template in {test_dir[0]}')
        filename = tmp / f'0{idx}-base.yml'
        with open(filename, 'w') as fh:
            fh.write(content)
    rougail = Rougail()
    try:
        config = rougail.get_config()
        config.value.dict()
    except Exception as err:
        #rmtree(tmp)
        raise Exception(f'error in {test_dir[0]}: {err}') from err
    rmtree(tmp)
