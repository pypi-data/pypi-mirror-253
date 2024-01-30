from pytest import raises
import logging

from rougail import Rougail, RougailConfig
from rougail.error import DictConsistencyError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def test_mode_invalid_default():
    # default variable mode is not in modes_level
    RougailConfig['dictionaries_dir'] = ['tests/personalize_mode/dictionary']
    RougailConfig['modes_level'] = ('level1', 'level2')
    eolobj = Rougail()
    with raises(DictConsistencyError) as err:
        eolobj.converted.annotate()
    assert err.value.errno == 72


def test_mode_invalid_default_family():
    # default family mode is not in modes_level
    RougailConfig['dictionaries_dir'] = ['tests/personalize_mode/dictionary']
    RougailConfig['modes_level'] = ('level1', 'level2')
    RougailConfig['default_variable_mode'] = 'level1'
    eolobj = Rougail()
    with raises(DictConsistencyError) as err:
        eolobj.converted.annotate()
    assert err.value.errno == 73


def test_personalize_mode():
    RougailConfig['dictionaries_dir'] = ['tests/personalize_mode/dictionary']
    RougailConfig['modes_level'] = ('level1', 'level2')
    RougailConfig['default_variable_mode'] = 'level1'
    RougailConfig['default_family_mode'] = 'level1'
    RougailConfig['tiramisu_cache'] = None
    eolobj = Rougail()
    eolobj.get_config()


def test_personalize_mode_unknown():
    # a variable has an unknown mode
    RougailConfig['dictionaries_dir'] = ['tests/personalize_mode/dictionary']
    RougailConfig['modes_level'] = ('level1',)
    RougailConfig['default_variable_mode'] = 'level1'
    RougailConfig['default_family_mode'] = 'level1'
    eolobj = Rougail()
    with raises(DictConsistencyError) as err:
        eolobj.converted.annotate()
    assert err.value.errno == 71


def test_personalize_annotate_twice():
    RougailConfig['dictionaries_dir'] = ['tests/personalize_mode/dictionary']
    RougailConfig['modes_level'] = ('level1', 'level2')
    RougailConfig['default_variable_mode'] = 'level1'
    RougailConfig['default_family_mode'] = 'level1'
    eolobj = Rougail()
    eolobj.converted.annotate()
    with raises(DictConsistencyError) as err:
        eolobj.converted.annotate()
    assert err.value.errno == 85
