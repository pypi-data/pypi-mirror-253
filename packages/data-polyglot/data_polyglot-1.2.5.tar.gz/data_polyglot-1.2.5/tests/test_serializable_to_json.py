import datetime
from typing import List

import pytest

from src.data_polyglot import Serializable, serialize


class TestSerializableToJsonSimpleTypes:
    def test_to_json_serialize_string(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = '5'
        data = j_obj.to_json()
        assert data == {'name': '5'}

    def test_to_json_serialize_int(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = 5
        data = j_obj.to_json()
        assert data == {'name': 5}

    def test_to_json_serialize_float(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = 5.5
        data = j_obj.to_json()
        assert data == {'name': 5.5}

    def test_to_json_serialize_list(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = [5.5]
        data = j_obj.to_json()
        assert data == {'name': [5.5]}

    def test_to_json_serialize_dict(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = {'var': 5.5}
        data = j_obj.to_json()
        assert data == {'name': {'var': 5.5}}

    def test_to_json_serialize_multiple_values(self):
        class JObj(Serializable):
            some_name1 = serialize('name')
            some_name2 = serialize('id')
            some_name3 = serialize('cost')

        j_obj = JObj()
        j_obj.some_name1 = 'item'
        j_obj.some_name2 = 123
        j_obj.some_name3 = 1.5

        data = j_obj.to_json()
        assert data == {'name': 'item', 'id': 123, 'cost': 1.5}


class TestSerializableToJsonDefaultValue:
    def test_to_json_default_specified_in_method(self):
        class JObj(Serializable):
            some_name = serialize('name', default_value=3)

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {'name': 3}

    def test_to_json_default_specified_in_init(self):
        class JObj(Serializable):
            def __init__(self):
                self.some_name = 7
            some_name = serialize('name')

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {'name': 7}

    def test_to_json_default_specified_in_init_overrides_method(self):
        class JObj(Serializable):
            def __init__(self):
                self.some_name = 7
            some_name = serialize('name', default_value='value')

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {'name': 7}


class TestSerializableToJsonPropertyRequired:
    def test_to_json_not_included_when_not_required(self):
        class JObj(Serializable):
            some_name = serialize('name', required=False)

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {}

    def test_to_json_not_required_default_value_assigned(self):
        class JObj(Serializable):
            some_name = serialize('name', required=False, default_value='nested')

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {'name': 'nested'}

    def test_to_json_required_no_data_set_to_none(self):
        class JObj(Serializable):
            some_name = serialize('name', required=True)

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {'name': None}

    def test_to_json_required_no_data_set_to_default(self):
        class JObj(Serializable):
            some_name = serialize('name', required=True, default_value='nested')

        j_obj = JObj()
        data = j_obj.to_json()
        assert data == {'name': 'nested'}


class TestSerializableToJsonNestedClass:
    def test_to_json_nested_obj_serialized(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_property = NestedJObj.nest('count')

        j_obj = JObj()
        j_obj.some_property.argument1 = 44

        data = j_obj.to_json()
        assert data == {'count': {'arg1': 44}}

    def test_to_json_nested_obj_instantiated_outside(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_property = NestedJObj.nest('count')

        j_obj = JObj()
        nested = NestedJObj()
        nested.argument1 = 44
        j_obj.some_property = nested

        data = j_obj.to_json()
        assert data == {'count': {'arg1': 44}}

    def test_to_json_nested_obj_serialized_multiple_vals_in_nested(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')
            argument2 = serialize('arg2')
            argument3 = serialize('arg3')

        class JObj(Serializable):
            some_property = NestedJObj.nest('count')

        j_obj = JObj()
        j_obj.some_property.argument1 = 44
        j_obj.some_property.argument2 = 'val'
        j_obj.some_property.argument3 = []

        data = j_obj.to_json()
        assert data == {'count': {'arg1': 44, 'arg2': 'val', 'arg3': []}}

    def test_to_json_nested_within_nested(self):
        class NestedJObjLvl2(Serializable):
            argument1 = serialize('deeper')

        class NestedJObjLvl1(Serializable):
            inside = NestedJObjLvl2.nest('lvl')

        class JObj(Serializable):
            some_property = NestedJObjLvl1.nest('item')

        j_obj = JObj()
        j_obj.some_property.inside.argument1 = 999

        data = j_obj.to_json()
        assert data == {'item': {'lvl': {'deeper': 999}}}

    def test_to_json_nested_obj_with_properties_serialized(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_property = NestedJObj.nest('count')
            status = serialize('status')

        j_obj = JObj()
        j_obj.some_property.argument1 = 44
        j_obj.status = 'COMPLETED'

        data = j_obj.to_json()
        assert data == {'count': {'arg1': 44}, 'status': 'COMPLETED'}


class TestSerializableToJsonNestedClassRequired:
    def test_to_json_nested_obj_null_not_required_return_none(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_property = NestedJObj.nest('count', required=False)

        j_obj = JObj()
        j_obj.some_property = None
        data = j_obj.to_json()
        assert data == {'count': None}

    def test_to_json_nested_obj_null_required_raise_error(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_property = NestedJObj.nest('count', required=True)

        j_obj = JObj()
        j_obj.some_property = None
        with pytest.raises(ValueError) as ex:
            j_obj.to_json()
        assert 'Error: required value is None for the key "count"' in ex.value.args[0]


class TestSerializableToJsonListOfObject:
    def test_to_json_list_of_obj_is_serialized(self):
        class NestedJObj(Serializable):
            argument1 = serialize('arg1')

        class JObj(Serializable):
            some_property: List[NestedJObj] = NestedJObj.nest('count', required=False)

        j_obj = JObj()
        j_obj.some_property = []

        n1 = NestedJObj()
        n1.argument1 = 3
        j_obj.some_property.append(n1)

        n2 = NestedJObj()
        n2.argument1 = 5
        j_obj.some_property.append(n2)

        data = j_obj.to_json()
        assert data == {'count': [{'arg1': 3}, {'arg1': 5}]}


class TestSerializableToJsonCustomConverter:
    def test_to_json_serialize_with_custom_converter(self):
        class JObj(Serializable):
            some_name = serialize('name', custom_converter=lambda j: j.strftime('%Y-%m-%d'))

        j_obj = JObj()
        j_obj.some_name = datetime.datetime.now()
        data = j_obj.to_json()
        assert data == {'name': j_obj.some_name.strftime('%Y-%m-%d')}
