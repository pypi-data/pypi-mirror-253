import json
import os.path
import random
import string

import pytest

from src.data_polyglot import LocalStorage

FILE_PATH = os.path.dirname(__file__)
TEMP_TEST_DATA_PATH = os.path.join(FILE_PATH, 'storage/temp_test_data')

if not os.path.exists(TEMP_TEST_DATA_PATH):
    os.makedirs(TEMP_TEST_DATA_PATH)


class LocalStorageMock(LocalStorage):
    def __init__(self, file_path):
        super().__init__(file_path)

    @property
    def data(self):
        return self._data


@pytest.fixture(scope='session', autouse=True)
def delete_temp_file():
    yield
    files = os.listdir(TEMP_TEST_DATA_PATH)
    for f in files:
        os.remove(os.path.join(TEMP_TEST_DATA_PATH, f))


def get_random_string(length: int) -> str:
    letters = string.ascii_letters + string.digits
    text = ''.join(random.choice(letters) for _ in range(length))
    return text


def create_file(name_prefix: str, file_content: dict):
    file_name = name_prefix + get_random_string(5) + '.json'
    file_path = os.path.join(TEMP_TEST_DATA_PATH, file_name)
    with open(file_path, mode='w') as f:
        json.dump(file_content, f, indent=4)
    return file_path


def compare_dictionaries(origin: dict, compare: dict):
    diff = {}
    for k, v in origin.items():
        if k in compare:
            compare_value = compare[k]
            if isinstance(v, dict):
                result = compare_dictionaries(v, compare_value)
                if result != {}:
                    diff.update({k: result})
            else:
                if v != compare_value:
                    diff.update({k: compare_value})
        else:
            diff.update({k: v})
    return diff


class TestLocalStorageInit:
    def test_init_file_doesnt_exist_create_on_init(self):
        file_path = os.path.join(TEMP_TEST_DATA_PATH, 'create_on_init' + get_random_string(5) + '.json')
        LocalStorage(file_path)
        file_created = os.path.exists(file_path)
        assert file_created

    def test_on_init_file_exists_no_error_is_thrown(self):
        file_path = create_file('file_exists', {})
        storage = LocalStorage(file_path)
        assert storage


class TestLocalStorageRead:
    @pytest.mark.parametrize('data_path', [
        'env',
        '/env',
        'env/',
        '/env/',
        'env/item',
        '/env/item',
        '/env/item/',
        '/env//item/',
        '/env/item with spaces',
        '/env / item with spaces',
    ])
    def test_read_valid_path_error_not_raised(self, data_path):
        file_path = create_file('read_path', {
            'env': {
                'item': {
                    'name': 'test',
                    'id': 1234
                },
                'item with spaces': {'name': 'test'}
            }})
        storage = LocalStorage(file_path)
        try:
            storage.read(data_path)
        except KeyError:
            pytest.fail(reason=f'Expected to be able to read the following path: "{data_path}"')

    def test_read_path_does_not_exist_raises_error(self):
        file_path = create_file('read_key_missing', {
            'env': {
                'item': {
                    'name': 'test_venue',
                    'id': 1234
                }}})
        data_path = 'env/venue/something'
        storage = LocalStorage(file_path)
        with pytest.raises(KeyError):
            storage.read(data_path)

    @pytest.mark.parametrize('data_path, data_type, expected_result', [
        ('/name', str, 'test read'),
        ('/id', int, 4321),
        ('/price', float, 2.99),
        ('/is_active', bool, False),
        ('/list_test', list, [456, 123]),
        ('/dict_test', dict, {'another_key': 'another value'}),
        ('/env/item/name', str, 'read test'),
        ('/env/item/id', int, 1234),
        ('/env/item/price', float, 1.99),
        ('/env/item/is_active', bool, True),
        ('/env/item/list_test', list, [123, 456]),
        ('/env/item/dict_test', dict, {'some_key': 'value'}),
    ])
    def test_read_value_correctly(self, data_path, data_type, expected_result):
        file_path = create_file('read_value', {
            'env': {
                'item': {
                    'name': 'read test',
                    'id': 1234,
                    'price': 1.99,
                    'is_active': True,
                    'list_test': [123, 456],
                    'dict_test': {'some_key': 'value'}
                }},
            'name': 'test read',
            'id': 4321,
            'price': 2.99,
            'is_active': False,
            'list_test': [456, 123],
            'dict_test': {'another_key': 'another value'}
        })
        storage = LocalStorage(file_path)
        data = storage.read(data_path)
        assert isinstance(data, data_type)
        assert data == expected_result


class TestLocalStorageIsKeyPresent:
    def test_key_present_returns_true(self):
        file_path = create_file('key_present', {
            'env': {
                'item': {
                    'name': 'test_venue',
                    'id': 1234
                }}})
        data_path = 'env/item/id'
        storage = LocalStorage(file_path)
        exists = storage.is_key_present(data_path)
        assert exists

    def test_key_absent_returns_false(self):
        file_path = create_file('key_absent', {
            'env': {
                'item': {
                    'name': 'test_venue',
                    'id': 1234
                }}})
        data_path = 'env/item/something'
        storage = LocalStorage(file_path)
        exists = storage.is_key_present(data_path)
        assert not exists


class TestLocalStorageCreate:
    @pytest.mark.parametrize('data_path, data_type, value', [
        ('/name', str, 'test write'),
        ('/id', int, 4321),
        ('/price', float, 2.99),
        ('/is_active', bool, False),
        ('/list_test', list, [456, 123]),
        ('/dict_test', dict, {'another_key': 'another value'}),
        ('/env/item/name', str, 'write test'),
        ('/env/item/id', int, 1234),
        ('/env/item/price', float, 1.99),
        ('/env/item/is_active', bool, True),
        ('/env/item/list_test', list, [123, 456]),
        ('/env/item/dict_test', dict, {'some_key': 'value'}),
    ])
    def test_create_writes_data_into_file(self, data_path, data_type, value):
        file_path = create_file('create_writes_string_data', {})
        storage = LocalStorage(file_path)
        storage.create(data_path, value)
        data = storage.read(data_path)
        assert isinstance(data, data_type)
        assert data == value

    @pytest.mark.parametrize('data_path, value, expected_difference', [
        ('new_key', 'new value', {'new_key': 'new value'}),
        ('env/new_item_name', 'new item name', {'env': {'new_item_name': 'new item name'}}),
        ('env/item3/name', 'new item', {'env': {'item3': {'name': 'new item'}}}),
        ('env/item3/dict', {'k': 'v'}, {'env': {'item3': {'dict': {'k': 'v'}}}}),
    ])
    def test_create_does_not_delete_existing_data(self, data_path, value, expected_difference):
        content = {
            'env': {
                'item1': {
                    'name': 'read test',
                    'id': 1234,
                    'price': 1.99,
                    'is_active': True,
                    'list_test': [123, 456],
                    'dict_test': {'some_key': 'value'}
                },
                'item2': {
                    'name': 'random text',
                    'id': 2233,
                    'price': 5.99,
                    'is_active': False,
                    'list_test': [1233, 4564],
                    'dict_test': {'some_key1': 'value1'}
                },
            },
            'name': 'test read',
            'id': 4321,
            'price': 2.99,
            'is_active': False,
            'list_test': [456, 123],
            'dict_test': {'another_key': 'another value'}
        }
        file_path = create_file('read_value', content)
        storage = LocalStorageMock(file_path)
        storage.create(data_path, value)

        difference = compare_dictionaries(storage.data, content)
        assert difference == expected_difference

    def test_create_while_key_exists_raise_error(self):
        file_path = create_file('create_does_not_delete', {
            'env': {
                'inventory': {
                    'item1': {
                        'name': 'some venue'
                    },
                    'item2': {
                        'name': 'test venue'
                    }}}})
        data_path = 'env/inventory/item1/name'

        storage = LocalStorage(file_path)
        with pytest.raises(ValueError):
            storage.create(data_path, 'another venue')

    @pytest.mark.parametrize('data_path, read_path', [
        ('env b', None),
        ('env a/inventory b', 'env a'),
        ('env a/inventory a/item b', 'env a/inventory a'),
    ])
    def test_create_orders_keys_alphabetically(self, data_path, read_path):
        file_path = create_file('create_ordered', {
            'env a': {
                'inventory a': {
                    'item a': {'name': 'some item'},
                    'item c': {'name': 'some item'},
                },
                'inventory c': {
                    'item a': {'name': 'some item'},
                },
            },
            'env c': {
                'inventory a': {
                    'item a': {'name': 'some item'},
                },
            },
        })
        storage = LocalStorageMock(file_path)
        storage.create(data_path, 'some value')
        data = storage.data if read_path is None else storage.read(read_path)
        assert list(data.keys()) == list(sorted(data.keys()))


class TestLocalStorageUpdate:
    @pytest.mark.parametrize('data_path, data_type, value', [
        ('env', str, 'name'),
        ('env', int, 123),
        ('env', float, 1.23),
        ('env', bool, True),
        ('env', dict, {'name': 'some name'}),
        ('env', list, [123, 456]),
        ('env/inventory', str, 'name'),
        ('env/inventory', int, 123),
        ('env/inventory', float, 1.23),
        ('env/inventory', bool, True),
        ('env/inventory', dict, {'name': 'some name'}),
        ('env/inventory', list, [123, 456]),
        ('env/inventory/item/name', str, 'new name'),
    ])
    def test_update_value(self, data_path, data_type, value):
        content = {
            'env': {
                'inventory': {
                    'item': {'name': 'some item'}
                }
            }
        }
        file_path = create_file('update_data', content)
        storage = LocalStorage(file_path)
        storage.update(data_path, value)
        data = storage.read(data_path)
        assert isinstance(data, data_type)
        assert data == value

    @pytest.mark.parametrize('data_path', [
        'env1',
        'env/inventory1',
        'env/inventory/item1',
    ])
    def test_update_invalid_path_raises_error(self, data_path):
        content = {
            'env': {
                'inventory': {
                    'item': {'name': 'some item'}
                }
            }
        }
        file_path = create_file('update_data', content)
        storage = LocalStorage(file_path)
        with pytest.raises(ValueError):
            storage.update(data_path, 'value')

    @pytest.mark.parametrize('data_path, value, valid_path', [
        ('env_1', 'value', ['env_1', 'env_2/inventory_1/item_1', 'env_2/inventory_2/item_2']),
        ('env_2', 'value', ['env_2', 'env_1/inventory_1/item_1', 'env_1/inventory_2/item_2']),
        ('env_1/inventory_1', 'value', ['env_1/inventory_1', 'env_1/inventory_2/item_2', 'env_2/inventory_1/item_2']),
        ('env_1/inventory_2', 'value', ['env_1/inventory_2', 'env_1/inventory_1/item_2', 'env_2/inventory_1/item_2']),
        ('env_2/inventory_2', 'value', ['env_2/inventory_2', 'env_1/inventory_1/item_2', 'env_1/inventory_1/item_2']),
        ('env_1/inventory_1/item_1', 'value', ['env_1/inventory_1/item_1', 'env_2/inventory_1/item_2']),
        ('env_1/inventory_2/item_2', 'value', ['env_2/inventory_2/item_2', 'env_1/inventory_1/item_1']),

    ])
    def test_update_does_not_delete_existing_data(self, data_path, value, valid_path):
        content = {
            'env_1': {
                'inventory_1': {
                    'item_1': {'name': 'some item 1'},
                    'item_2': {'name': 'some item 2'},
                },
                'inventory_2': {
                    'item_1': {'name': 'some item 1'},
                    'item_2': {'name': 'some item 2'},
                }
            },
            'env_2': {
                'inventory_1': {
                    'item_1': {'name': 'some item 1'},
                    'item_2': {'name': 'some item 2'},
                },
                'inventory_2': {
                    'item_1': {'name': 'some item 1'},
                    'item_2': {'name': 'some item 2'},
                }
            }
        }
        file_path = create_file('update_data', content)
        storage = LocalStorage(file_path)
        storage.update(data_path, value)
        for p in valid_path:
            assert storage.is_key_present(p), f'Path "{p}" should be valid'

    @pytest.mark.parametrize('update_path, update_value', [
        ('env/inventory/item_1', {'name': 'item name 1'}),
        ('env/inventory/item_2', {'name': 'item name 2'}),
        ('env/inventory/item_3', {'name': 'item name 3'}),
    ])
    def test_update_does_not_rearrange_data_subdirectory(self, update_path, update_value):
        content = {
            'env': {
                'inventory': {
                    'item_1': {
                        'name': 'item name 1'
                    },
                    'item_2': {
                        'name': 'item name 2'
                    },
                    'item_3': {
                        'name': 'item name 3'
                    }}}}
        file_path = create_file('update_data', content)

        storage = LocalStorage(file_path)
        storage.update(update_path, update_value)
        assert storage.read('env/inventory') == content['env']['inventory']

    @pytest.mark.parametrize('update_path, update_value', [
        ('item_1', {'name': 'item name 1'}),
        ('item_2', {'name': 'item name 2'}),
        ('item_3', {'name': 'item name 3'}),
    ])
    def test_update_does_not_rearrange_data_root(self, update_path, update_value):
        content = {
            'item_1': {
                'name': 'item name 1'
            },
            'item_2': {
                'name': 'item name 2'
            },
            'item_3': {
                'name': 'item name 3'
            }
        }
        file_path = create_file('update_data', content)

        storage = LocalStorage(file_path)
        storage.update(update_path, update_value)
        assert storage.read(update_path) == content[update_path]


class TestLocalStorageDelete:
    @pytest.mark.parametrize("data_path, valid_path", [
        ("env_1", ["env_2", "env_2/inventory_1/item_1/name"]),
        ("env_1/inventory_1", ["env_1", "env_2/inventory_1", "env_1/inventory_2/item_1/name"]),
        ("env_1/inventory_1/item_1", ["env_1/inventory_2", "env_1/inventory_1", "env_1/inventory_1/item_2/name"]),
        ("env_1/inventory_1/item_1/name", ["env_1/inventory_1/item_1", "env_1/inventory_1/item_2/name"]),
    ])
    def test_delete(self, data_path, valid_path):
        content = {
            'env_1': {
                'inventory_1': {
                    'item_1': {'name': 'some item a'},
                    'item_2': {'name': 'some item b'},
                },
                'inventory_2': {
                    'item_1': {'name': 'some item c'},
                    'item_2': {'name': 'some item d'},
                }
            },
            'env_2': {
                'inventory_1': {
                    'item_1': {'name': 'some item e'},
                    'item_2': {'name': 'some item f'},
                },
                'inventory_2': {
                    'item_1': {'name': 'some item g'},
                    'item_2': {'name': 'some item h'},
                }
            }
        }
        file_path = create_file('delete_data', content)
        storage = LocalStorage(file_path)
        storage.delete(data_path)
        assert not storage.is_key_present(data_path), 'Data should be deleted'
        for p in valid_path:
            assert storage.is_key_present(p), f'Expected to "{p}" path to remain'
