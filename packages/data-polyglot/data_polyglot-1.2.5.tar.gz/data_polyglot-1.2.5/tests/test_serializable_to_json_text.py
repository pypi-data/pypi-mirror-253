from src.data_polyglot import Serializable, serialize


class TestSerializableToJsonTextSimpleTypes:
    def test_to_json_text_serialize_string(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = '5'
        data = j_obj.to_json_text()
        assert data == '{"name": "5"}'

    def test_to_json_text_serialize_int(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = 5
        data = j_obj.to_json_text()
        assert data == '{"name": 5}'

    def test_to_json_text_serialize_float(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = 5.5
        data = j_obj.to_json_text()
        assert data == '{"name": 5.5}'

    def test_to_json_text_serialize_bool(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = True
        data = j_obj.to_json_text()
        assert data == '{"name": true}'

    def test_to_json_text_serialize_none(self):
        class JObj(Serializable):
            some_name = serialize('name', required=True)

        j_obj = JObj()
        data = j_obj.to_json_text()
        assert data == '{"name": null}'

    def test_to_json_text_serialize_list_of_str(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = ['a', 'b']
        data = j_obj.to_json_text()
        assert data == '{"name": ["a", "b"]}'

    def test_to_json_text_serialize_list_of_int(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = [1, 2]
        data = j_obj.to_json_text()
        assert data == '{"name": [1, 2]}'

    def test_to_json_text_serialize_list_of_float(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = [1.1, 2.44]
        data = j_obj.to_json_text()
        assert data == '{"name": [1.1, 2.44]}'

    def test_to_json_text_serialize_list_of_bool(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = [True, False]
        data = j_obj.to_json_text()
        assert data == '{"name": [true, false]}'

    def test_to_json_text_serialize_list_of_lists(self):
        class JObj(Serializable):
            some_name = serialize('name')

        j_obj = JObj()
        j_obj.some_name = [[1, 2], ["a", "b"], []]
        data = j_obj.to_json_text()
        assert data == '{"name": [[1, 2], ["a", "b"], []]}'
