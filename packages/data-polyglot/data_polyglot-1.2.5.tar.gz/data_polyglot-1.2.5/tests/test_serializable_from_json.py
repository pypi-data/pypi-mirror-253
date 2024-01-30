from datetime import datetime
from typing import List

import pytest

from src.data_polyglot import Serializable, serialize

@pytest.fixture()
def test_json():
    j = {
        'name': 'some name',
        'id': 123,
        'date': '2023-05-19',
        'cost': '1.00',
        'rate': 0.01,
        'metadata': None,
        'more_params': {
            'arg1': 5,
            'arg2': 'another param'
        },
        'extra_params': {
            'arg1': 7,
            'arg2': 'extra param',
            'value': 10
        },
        'multi_level': {
            'var': 'lvl1',
            'nested': {
                'val': 'lvl2'
            }
        },
        'list_of_strings': ['text1', 'text2', 'text3'],
        # list of objects
    }
    return j


class TestSerializableFromJsonKeyArg:
    def test_from_json_parse_string(self, test_json):
        class JObj(Serializable):
            name = serialize('name')

        j_obj = JObj.from_json(test_json)
        assert j_obj.name == 'some name'

    def test_from_json_parse_int(self, test_json):
        class JObj(Serializable):
            item_name = serialize('id')

        j_obj = JObj.from_json(test_json)
        assert j_obj.item_name == 123

    def test_from_json_parse_float(self, test_json):
        class JObj(Serializable):
            rate = serialize('rate')

        j_obj = JObj.from_json(test_json)
        assert j_obj.rate == 0.01

    def test_from_json_parse_list_of_strings(self, test_json):
        class JObj(Serializable):
            some_list = serialize('list_of_strings')

        j_obj = JObj.from_json(test_json)
        assert type(j_obj.some_list) == list
        assert j_obj.some_list[0] == 'text1'

    def test_from_json_parse_dictionary(self, test_json):
        class JObj(Serializable):
            some_dict = serialize('more_params')

        j_obj = JObj.from_json(test_json)
        assert type(j_obj.some_dict) == dict
        assert j_obj.some_dict['arg1'] == 5

    def test_from_json_parse_null(self, test_json):
        class JObj(Serializable):
            some_value = serialize('metadata')

        j_obj = JObj.from_json(test_json)
        assert j_obj.some_value is None

    def test_from_json_child_init_override_does_not_break_parsing(self, test_json):
        class JObj(Serializable):
            def __init__(self):
                self.v = 5
            rate = serialize('rate')

        j_obj = JObj.from_json(test_json)
        assert j_obj.rate == 0.01

    def test_from_json_child_init_override_attr_in_init_does_not_break_parsing(self, test_json):
        class JObj(Serializable):
            def __init__(self):
                self.rate = 5
            rate = serialize('rate')

        j_obj = JObj.from_json(test_json)
        assert j_obj.rate == 0.01

    def test_from_json_multiple_properties_are_parsed(self, test_json):
        class JObj(Serializable):
            name = serialize('name')
            item_id = serialize('id')
            cost = serialize('cost')

        j_obj = JObj.from_json(test_json)
        assert j_obj.name == 'some name'
        assert j_obj.item_id == 123
        assert j_obj.cost == '1.00'


class TestSerializableFromJsonRequiredArg:
    def test_from_json_required_param_not_required_set_to_none(self, test_json):
        class JObj(Serializable):
            name = serialize('does not exist', required=False)

        j_obj = JObj.from_json(test_json)
        assert j_obj.name is None

    def test_from_json_required_param_missing_raise_error(self, test_json):
        class JObj(Serializable):
            name = serialize('does not exist', required=True)

        with pytest.raises(KeyError) as ex:
            JObj.from_json(test_json)

        assert f'Error: could not find the key "does not exist"' in ex.value.args[0]

    def test_from_json_nested_obj_error_when_missing_json_key_but_required(self, test_json):
        class NestedJObj1(Serializable):
            some_value = serialize('arg1')

        class JObj(Serializable):
            value = NestedJObj1.nest('does not exist', required=True)

        with pytest.raises(KeyError) as ex:
            JObj.from_json(test_json)

        assert f'Error: could not find the key "does not exist"' in ex.value.args[0]

    def test_from_json_nested_obj_not_required_missing_json_key_is_none(self, test_json):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_class_property = NestedJObj.nest('does not exist', required=False)

        j_obj = JObj.from_json(test_json)
        assert j_obj.some_class_property is None

    def test_from_json_nested_obj_not_required_json_value_is_null_return_none(self, test_json):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_class_property = NestedJObj.nest('metadata', required=False)

        j_obj = JObj.from_json(test_json)
        assert j_obj.some_class_property is None

    def test_from_json_nested_obj_required_json_value_is_null_raise_error(self, test_json):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_class_property = NestedJObj.nest('metadata', required=True)

        with pytest.raises(KeyError) as ex:
            JObj.from_json(test_json)

        assert f'Error: value is Null for the key "metadata"' in ex.value.args[0]


class TestSerializableFromJsonDefaultArg:
    def test_from_json_default_param_set_return_default_value(self, test_json):
        class JObj(Serializable):
            name = serialize('does not exist', required=False, default_value=111)

        j_obj = JObj.from_json(test_json)
        assert j_obj.name is 111

    def test_from_json_default_param_set_implicitly_not_required(self, test_json):
        class JObj(Serializable):
            name = serialize('does not exist', default_value=111)

        j_obj = JObj.from_json(test_json)
        assert j_obj.name is 111

    def test_from_json_default_param_set_and_required_overrides_required(self, test_json):
        class JObj(Serializable):
            name = serialize('does not exist', required=True, default_value=111)

        j_obj = JObj.from_json(test_json)
        assert j_obj.name is 111


class TestSerializableFromJsonCustomSerialArg:
    def test_from_json_custom_converter_string_from_int(self, test_json):
        class JObj(Serializable):
            name = serialize('id', custom_converter=lambda j: str(j))

        j_obj = JObj.from_json(test_json)
        assert j_obj.name == '123'

    def test_from_json_custom_converter_date_from_string(self, test_json):
        class JObj(Serializable):
            date = serialize('date', custom_converter=lambda j: datetime.strptime(j, '%Y-%m-%d'))

        j_obj = JObj.from_json(test_json)
        assert j_obj.date == datetime.strptime('2023-05-19', '%Y-%m-%d')

    def test_from_json_custom_converter_error_while_parsing(self, test_json):
        class JObj(Serializable):
            cost = serialize('cost', custom_converter=lambda j: int(j))

        with pytest.raises(ValueError) as ex:
            JObj.from_json(test_json)
        assert 'Error: an exception occurred while converting parsed value' in ex.value.args[0]


class TestSerializableFromJsonNestedObjects:
    def test_from_json_parses_nested_json_object(self, test_json):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_class_property = NestedJObj.nest('more_params')

        j_obj = JObj.from_json(test_json)
        assert j_obj.some_class_property.argument1 == 5

    def test_from_json_parses_property_and_nested_json_object(self, test_json):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            rate = serialize('rate')
            some_class_property = NestedJObj.nest('more_params')

        j_obj = JObj.from_json(test_json)
        assert j_obj.some_class_property.argument1 == 5
        assert j_obj.rate == 0.01

    def test_from_json_parses_nested_within_nested_json_objects(self, test_json):
        class NestedJObjLvl2(Serializable):
            some_value = serialize('val')

        class NestedJObjLvl1(Serializable):
            inside = NestedJObjLvl2.nest('nested')

        class JObj(Serializable):
            lvl1 = NestedJObjLvl1.nest('multi_level')

        j_obj = JObj.from_json(test_json)
        assert j_obj.lvl1.inside.some_value == 'lvl2'

    def test_from_json_multiple_nested_obj(self, test_json):
        class NestedJObj1(Serializable):
            some_value = serialize('arg1')

        class NestedJObj2(Serializable):
            another_value = serialize('arg1')

        class JObj(Serializable):
            first = NestedJObj1.nest('more_params')
            second = NestedJObj2.nest('extra_params')

        j_obj = JObj.from_json(test_json)
        assert j_obj.first.some_value == 5
        assert j_obj.second.another_value == 7


class TestSerializableFromJsonListOfObjects:
    def test_from_json_parse_nested_list_of_objects(self):
        test_data = {'ls': [
            {'name': 'obj1'},
            {'name': 'obj2'}
        ]}

        class NestedJObj(Serializable):
            name = serialize('name')

        class JObj(Serializable):
            some_list_of_classes: List[NestedJObj] = NestedJObj.nest('ls')

        j_obj = JObj.from_json(test_data)
        assert type(j_obj.some_list_of_classes) == list
        assert len(j_obj.some_list_of_classes) == 2
        assert j_obj.some_list_of_classes[0].name == 'obj1'
        assert j_obj.some_list_of_classes[1].name == 'obj2'

    def test_from_json_parse_empty_list_of_object(self):
        test_data = {'ls': []}

        class NestedJObj(Serializable):
            name = serialize('name')

        class JObj(Serializable):
            some_list_of_classes: List[NestedJObj] = NestedJObj.nest('ls')

        j_obj = JObj.from_json(test_data)
        assert type(j_obj.some_list_of_classes) == list
        assert len(j_obj.some_list_of_classes) == 0

    def test_from_json_parse_list_not_dict_raises_error(self):
        test_data = {'ls': [1, 2, 3]}

        class NestedJObj(Serializable):
            name = serialize('name')

        class JObj(Serializable):
            some_list_of_classes: List[NestedJObj] = NestedJObj.nest('ls')

        with pytest.raises(ValueError) as ex:
            JObj.from_json(test_data)
        assert 'Error: argument must be a dict or a list of dict' in ex.value.args[0]

    def test_from_json_parse_list_of_object(self):
        test_data = [{'arg1': 3}, {'arg1': 5}]

        class JObj(Serializable):
            some_property = serialize('arg1')

        j_arr = JObj.from_json(test_data)
        assert type(j_arr) == list
        assert len(j_arr) == 2
        assert j_arr[0].some_property == 3
        assert j_arr[1].some_property == 5
