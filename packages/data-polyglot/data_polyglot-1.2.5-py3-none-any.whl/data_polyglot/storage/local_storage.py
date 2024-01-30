import json
import os
from typing import Any, List

from src.data_polyglot.storage.storage import Storage


class LocalStorage(Storage):
    """
    Store your test data names and IDs locally in a JSON file.
    Use URL path format to read, write, update and delete data.
    Easy transition from local storage to external microservice.

    Example:
        storage = LocalStorage(config.FILE_PATH)
        default_item = storage.read('/inventory/default_item/name')

    Create scripts to seed your data in the test environment.
        storage = LocalStorage(config.FILE_PATH)
        inventory_page = InventoryPage(config.TEST_ENVIRONMENT)
        item_name = inventory_page.create_item(name='Please do not delete!')
        storage.create('/inventory/default_item/name', item_name)
    """
    def __init__(self, file_path: str):
        # check if json file exists before creating a new file.
        if not os.path.isfile(file_path):
            with open(file_path, mode='w') as f:
                json.dump({}, f)
            print(f'\ndata_polyglot::LocalStorage - Created file "{file_path}"\n')

        self._file_path = file_path

        # load file content
        with open(file_path, mode="r") as r:
            self._data: dict = json.load(r)

    @staticmethod
    def _path_to_args(path: str):
        if path[0] == '/':
            path = path[1:]
        if path[-1] == '/':
            path = path[:-1]

        path = os.path.normpath(path)
        args = path.split(os.sep)
        args = [a.strip() for a in args]
        return args

    def _dump_data_to_file(self):
        with open(self._file_path, mode='w') as file:
            json.dump(self._data, file, indent=4)

    def create(self, path: str, value: Any):
        """
        Write data to file.
        :param path: path for the value to be stored, example 'sysadmin/templates/default_template'
        :param value: basic data types, like str, int, float, bool, list, dict
        :raises ValueError: if path already exists.
        """
        args = self._path_to_args(path)

        def _create(data: dict, path_args: List[str], create_value) -> dict:
            result = {}
            for arg in path_args:
                if arg not in data:
                    if len(path_args) == 1:
                        result.update({arg: create_value})
                        return result
                    else:
                        path_args = path_args[1:]
                        r = _create({}, path_args, create_value)
                        result.update({arg: r})
                        return result
                else:
                    if len(path_args) == 1:
                        raise ValueError('Error: Cannot create value, data already exists')
                    path_args = path_args[1:]
                    r = _create(data[arg], path_args, create_value)
                    result.update(data)
                    result[arg].update(r)
                    result[arg] = dict(sorted(result[arg].items()))
                    return result

        new_data = _create(self._data, args, value)
        self._data.update(new_data)
        if len(args) == 1:
            self._data = dict(sorted(self._data.items()))
        self._dump_data_to_file()

    def update(self, path: str, value: Any):
        """
        Update data in the file.
        :param path: path for the value to update, example '/inventory/item_with_tax'
        :param value: basic data types, like str, int, float, bool, list, dict
        :raises ValueError: if path does not exist.
        """
        if not self.is_key_present(path):
            raise ValueError(f'Error: Path "{path}" does not exist.')

        args = self._path_to_args(path)

        def _update(data: dict, path_args: list, update_value: Any) -> dict:
            result = {}
            for key, val in data.items():
                if key == path_args[0] and len(path_args) > 1:
                    r = _update(data[key], path_args[1:], update_value)
                    result.update({key: r})
                elif key == path_args[0] and len(path_args) == 1:
                    result.update({key: update_value})
                else:
                    result.update({key: val})
            return result

        self._data = _update(self._data, args, value)
        self._dump_data_to_file()

    def read(self, path: str):
        """
        Read data from file.
        :param path: path to read the value from, example '/default_template/id'
        :raises KeyError: when could not find data in the specified path.
        """
        args = self._path_to_args(path)
        temp = self._data
        for arg in args:
            if arg not in temp:
                message = f'Error: Could not find "{arg}" in path "{path}" to read data.'
                raise KeyError(message)
            else:
                temp = temp[arg]
        return temp

    def is_key_present(self, path: str) -> bool:
        """
        Return True if path is valid, False - path is invalid.
        :param path: path for the value to be stored, example '/default_template/id'
        """
        args = self._path_to_args(path)
        temp = self._data
        for arg in args:
            if arg not in temp:
                return False
            else:
                temp = temp[arg]
        return True

    def delete(self, path: str):
        """
        Delete values in the specified path (including the last key).
        Does not raise error if path is invalid, nothing happens.
        :param path: path to delete, example '/default_template/id'
        """
        args = self._path_to_args(path)

        def _delete(data: dict, delete_key_args: list) -> dict:
            result = {}
            for key, val in data.items():
                if key == delete_key_args[0] and len(delete_key_args) > 1:
                    r = _delete(data[key], delete_key_args[1:])
                    result.update({key: r})
                elif key == delete_key_args[0] and len(delete_key_args) == 1:
                    pass
                else:
                    result.update({key: val})
            return result

        self._data = _delete(self._data, args)
        self._dump_data_to_file()
