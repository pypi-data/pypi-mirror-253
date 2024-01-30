import pytest
from src.data_polyglot import TableData, Serializable


class TestTableDataCount:
    def test_count_single_row_correctly(self):
        data = [{'name': 'banana'}]
        table = TableData(data)

        assert table.count() == 1

    def test_count_multiple_rows_correctly(self):
        data = [{'name': 'banana'}, {'name': 'apple'}, {'name': 'zucchini'}]
        table = TableData(data)

        assert table.count() == 3

    def test_count_empty_table_correctly(self):
        data = []
        table = TableData(data)

        assert table.count() == 0

    def test_count_using_len_correctly(self):
        data = [{'name': 'banana'}, {'name': 'apple'}, {'name': 'zucchini'}]
        table = TableData(data)

        assert len(table) == 3


class TestTableDataToString:
    def test_to_string_no_records(self):
        data = []
        table = TableData(data)

        assert table.to_string() == '[]'

    def test_to_string_multiple_records(self):
        data = [
            {'name': 'banana', 'price': 0.25},
            {'name': 'apple', 'price': 0.59},
            {'name': 'zucchini', 'price': 1.99},
        ]
        table = TableData(data)

        assert table.to_string() == ("\ndict_keys(['name', 'price'])\n"
                                     "dict_values(['banana', 0.25])\n"
                                     "dict_values(['apple', 0.59])\n"
                                     "dict_values(['zucchini', 1.99])\n")

    def test_to_string_using_str_method(self):
        data = [
            {'name': 'banana', 'price': 0.25},
            {'name': 'apple', 'price': 0.59},
            {'name': 'zucchini', 'price': 1.99},
        ]
        table = TableData(data)

        assert "dict_keys(['name', 'price'])" in str(table)


class TestTableDataIsColumnPresent:
    def test_is_column_present_found_column_return_true(self):
        data = [{'name': 'banana'}]
        table = TableData(data)

        is_present = table.is_column_present(0, 'name')
        assert is_present

    def test_is_column_present_not_found_return_false(self):
        data = [{'name': 'banana'}]
        table = TableData(data)

        is_present = table.is_column_present(0, 'description')
        assert not is_present

    def test_is_column_present_index_out_out_bounds(self):
        data = [{'name': 'banana'}]
        table = TableData(data)

        with pytest.raises(IndexError) as ex:
            table.is_column_present(1, 'description')

        error_message = ex.value.args[0]
        assert error_message == 'Error: provided row index "1" is out of bounds. Total records: "1"'

    def test_is_column_present_no_records_raise_error(self):
        data = []
        table = TableData(data)

        with pytest.raises(IndexError) as ex:
            table.is_column_present(0, 'description')

        error_message = ex.value.args[0]
        assert error_message == 'Error: table does not have any record'


class TestTableDataGetColumnValue:
    def test_get_column_value_by_row_index_return_correct_value(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        value = table.get_column_value_by_row_index(1, 'price')
        assert value == 0.59

    def test_get_column_value_by_row_index_empty_table_raise_error(self):
        data = []

        table = TableData(data)
        with pytest.raises(IndexError) as ex:
            table.get_column_value_by_row_index(0, 'price')
        assert ex.value.args[0] == "Error: table does not have any record"

    def test_get_column_value_by_row_index_out_of_bounds_raise_error(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        with pytest.raises(IndexError) as ex:
            table.get_column_value_by_row_index(4, 'price')
        assert ex.value.args[0] == 'Error: provided row index "4" is out of bounds. Total records: "3"'

    def test_get_column_value_by_row_index_column_not_found_raise_error(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        with pytest.raises(ValueError) as ex:
            table.get_column_value_by_row_index(0, 'description')
        assert ex.value.args[0] == ("Error: specified column \"description\" does not exist. "
                                    "Available columns are: dict_keys(['name', 'price', 'quantity'])")

    def test_get_column_value_first_row_successfully(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        value = table.get_column_value_first_row('quantity')
        assert value == 3

    def test_get_column_value_first_row_empty_table_raise_error(self):
        data = []

        table = TableData(data)
        with pytest.raises(IndexError) as ex:
            table.get_column_value_first_row('quantity')
        assert ex.value.args[0] == 'Error: table does not have any record'

    def test_get_column_value_last_row_successfully(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        value = table.get_column_value_last_row('quantity')
        assert value == 4

    def test_get_column_value_last_row_empty_table_raise_error(self):
        data = []

        table = TableData(data)
        with pytest.raises(IndexError) as ex:
            table.get_column_value_last_row('quantity')
        assert ex.value.args[0] == 'Error: table does not have any record'

    def test_get_column_value_last_row_single_row_successfully(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
        ]

        table = TableData(data)
        value = table.get_column_value_last_row('quantity')
        assert value == 3

    def test_get_all_column_values_successfully(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        value = table.get_all_column_values('quantity')
        assert value == [3, 5, 4]


class TestTableDataFilterByColumn:
    def test_filter_by_column_name_successfully(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
        ]

        table = TableData(data)
        table = table.filter_by_column_name('name', 'apple')
        assert table.count() == 1
        assert table.get_column_value_first_row('name') == 'apple'

    def test_filter_by_column_name_partial_match(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
            {'name': 'pineapple', 'price': 3.99, 'quantity': 4},
        ]

        table = TableData(data)
        table = table.filter_by_column_name('name', 'apple')
        assert table.count() == 2
        assert table.get_column_value_first_row('name') == 'apple'
        assert table.get_column_value_last_row('name') == 'pineapple'

    def test_filter_by_column_name_ignore_case(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
            {'name': 'pineapple', 'price': 3.99, 'quantity': 4},
        ]

        table = TableData(data)
        table = table.filter_by_column_name('name', 'Apple')
        assert table.count() == 2
        assert table.get_column_value_first_row('name') == 'apple'
        assert table.get_column_value_last_row('name') == 'pineapple'

    def test_filter_by_column_name_ignore_case_set_to_false(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
            {'name': 'Apple', 'price': 3.99, 'quantity': 4},
        ]

        table = TableData(data)
        table = table.filter_by_column_name('name', 'Apple', ignore_case=False)
        assert table.count() == 1
        assert table.get_column_value_first_row('name') == 'Apple'
        assert table.get_column_value_first_row('price') == 3.99

    def test_filter_by_column_name_partial_match_ignore_case_not_throwing_error_on_integers(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
            {'name': 'Apple', 'price': 3.99, 'quantity': 4},
        ]

        table = TableData(data)
        table = table.filter_by_column_name('quantity', 4, partial_match=True, ignore_case=True)
        assert table.count() == 2
        assert table.get_column_value_first_row('name') == 'zucchini'
        assert table.get_column_value_last_row('name') == 'Apple'

    def test_filter_by_column_name_partial_match_false(self):
        data = [
            {'name': 'banana', 'price': 0.25, 'quantity': 3},
            {'name': 'apple', 'price': 0.59, 'quantity': 5},
            {'name': 'zucchini', 'price': 1.99, 'quantity': 4},
            {'name': 'pineapple', 'price': 3.99, 'quantity': 4},
        ]

        table = TableData(data)
        table = table.filter_by_column_name('name', 'Apple', partial_match=False)
        assert table.count() == 1
        assert table.get_column_value_first_row('name') == 'apple'


class TestTableDataSorting:
    def test_sort_ascending(self):
        data = [
            {'name': 'banana'},
            {'name': 'apple'},
            {'name': 'zucchini'},
        ]

        table = TableData(data)
        table.sort('name', ascending=True)

        first_row = table.get_column_value_first_row('name')
        last_row = table.get_column_value_last_row('name')
        assert first_row == 'apple'
        assert last_row == 'zucchini'

    def test_sort_descending(self):
        data = [
            {'name': 'banana'},
            {'name': 'apple'},
            {'name': 'zucchini'},
        ]

        table = TableData(data)
        table.sort('name', ascending=False)

        first_row = table.get_column_value_first_row('name')
        last_row = table.get_column_value_last_row('name')
        assert first_row == 'zucchini'
        assert last_row == 'apple'

    def test_sort_single_record(self):
        data = [
            {'name': 'banana'},
        ]

        table = TableData(data)
        table.sort('name', ascending=False)

        first_row = table.get_column_value_first_row('name')
        last_row = table.get_column_value_last_row('name')
        assert first_row == 'banana'
        assert last_row == 'banana'

    def test_sort_empty_table_error_not_raised(self):
        data = []

        table = TableData(data)
        table.sort('name', ascending=False)

    def test_sort_column_not_found_raise_error(self):
        data = [
            {'name': 'banana'},
            {'name': 'apple'},
            {'name': 'zucchini'},
        ]

        table = TableData(data)
        with pytest.raises(ValueError) as ex:
            table.sort('description', ascending=False)

        assert ex.value.args[0] == ('Error: specified column "description" does not exist. '
                                    'Available columns are: dict_keys([\'name\'])')


def test_table_data_supports_inheritance():
    class CustomizedTable(TableData):
        def get_column_value_by_name(self, row_index):
            return self.get_column_value_by_row_index(row_index, 'name')

    data = [
        {'name': 'banana'},
        {'name': 'apple'},
        {'name': 'zucchini'},
    ]

    table = CustomizedTable(data)
    value = table.get_column_value_by_name(0)
    assert value == 'banana'


def test_table_data_can_work_with_serializable():
    class TableResponse(Serializable):
        page: int = Serializable.serialize('page')
        per_page: int = Serializable.serialize('per_page')
        table: TableData = Serializable.serialize('table', custom_converter=lambda j_arr: TableData(j_arr))

    response_data = {
            "page": 0,
            "per_page": 50,
            "table": [
                {"name": "item1", "price": 1.99, "quantity": 10},
                {"name": "item2", "price": 2.99, "quantity": 5},
                {"name": "item3", "price": 3.99, "quantity": 7},
            ]
    }

    deserialized = TableResponse.from_json(response_data)
    assert deserialized.page == 0
    assert deserialized.per_page == 50
    assert isinstance(deserialized.table, TableData)
    assert deserialized.table.count() == 3
    assert deserialized.table.get_column_value_first_row('name') == 'item1'
