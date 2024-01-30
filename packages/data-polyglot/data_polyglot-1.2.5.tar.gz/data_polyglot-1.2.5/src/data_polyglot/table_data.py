from typing import List


class TableData:
    """
    A wrapper around standard response to present a table to the user on the front-end.
    Create this class with the list of dictionaries where each dictionary is a table row
    with key as column name and value as cell value.
    """
    def __init__(self, table_data: List[dict]):
        """
        Instantiate TableData.
        param table_data: A list of dictionaries where each dictionary is a table row
        with key as column name and value as cell value. Example as a typical table response:
        {
            "page": 0,
            "per_page": 50,
            "table": [
                {"name": "item1", "price": 1.99, "quantity": 10 },
                {"name": "item2", "price": 2.99, "quantity": 5 },
                {"name": "item3", "price": 3.99, "quantity": 7 },
            ]
        }
        you would want to use instantiate this class with value of a "table".
        table = TableData(response.json()['table'])
        """
        self._table_data = table_data

    def count(self) -> int:
        """
        Return record count of the table.
        """
        return len(self._table_data)

    def __len__(self):
        return self.count()

    def to_string(self) -> str:
        """
        Return table content as string.
        """
        if self.count() > 0:
            text = f'\n{self._table_data[0].keys()}\n'
            for record in self._table_data:
                text += f'{record.values()}\n'
        else:
            text = '[]'
        return text

    def __str__(self):
        return self.to_string()

    def _raise_error_if_column_not_present(self, row_index: int, column_name: str):
        column_present = self.is_column_present(row_index, column_name)
        if not column_present:
            message = (f'Error: specified column "{column_name}" does not exist. '
                       f'Available columns are: {self._table_data[0].keys()}')
            raise ValueError(message)

    def is_column_present(self, row_index: int, column_name: str) -> bool:
        """
        :returns: True if column is present. False if column not found.
        :raises IndexError: if table has not records, or if provided index is out of bounds.
        """
        if self.count() == 0:
            raise IndexError('Error: table does not have any record')

        if row_index >= self.count():
            message = f'Error: provided row index "{row_index}" is out of bounds. Total records: "{self.count()}"'
            raise IndexError(message)
        is_present = column_name in self._table_data[row_index]
        return is_present

    def get_column_value_by_row_index(self, row_index: int, column_name: str):
        """
        :returns: the value of the column on a specified row.
        :param row_index: index of the row where to search the value
        :param column_name: name of the column to search for value
        :raises IndexError: if table is emtpy, or index out of bounds
        :raises ValueError: if column was not found.
        """
        self._raise_error_if_column_not_present(row_index, column_name)
        record = self._table_data[row_index][column_name]
        return record

    def get_column_value_first_row(self, column_name: str):
        """
        :returns: Column value of the first row.
        :raises IndexError: if table is emtpy, or index out of bounds
        :raises ValueError: if column was not found.
        """
        return self.get_column_value_by_row_index(0, column_name)

    def get_column_value_last_row(self, column_name: str):
        """
        :returns: Column value of the last row.
        :raises IndexError: if table is emtpy, or index out of bounds
        :raises ValueError: if column was not found.
        """
        return self.get_column_value_by_row_index(self.count() - 1, column_name)

    def get_all_column_values(self, column_name: str) -> list:
        """
        :returns: A list of values in a given column.
        :raises IndexError: if table is emtpy, or index out of bounds
        :raises ValueError: if column was not found.
        """
        self._raise_error_if_column_not_present(0, column_name)
        result = []
        for i in range(self.count()):
            value = self.get_column_value_by_row_index(i, column_name)
            result.append(value)
        return result

    def filter_by_column_name(self, column_name: str, value, partial_match: bool = True, ignore_case: bool = True):
        """
        Filter table using specified column and expected value.
        :param column_name: Name of the column to filter records
        :param value: filter out all records that don't match the value
        :param partial_match: If True match value partially. False - expected full match. Only applies to string type.
        :param ignore_case: If True ignore value case. False - expected to match the case. Only applies to string type.
        :returns: TableData class with filtered records.
        :raises ValueError: if column is not found.
        """
        if len(self._table_data) > 0:
            self._raise_error_if_column_not_present(0, column_name)
            result = []
            for record in self._table_data:
                cell_value = record[column_name]
                if ignore_case:
                    if isinstance(cell_value, str):
                        cell_value = cell_value.lower()
                        value = value.lower()
                if partial_match and isinstance(cell_value, str):
                    if value in cell_value:
                        result.append(record)
                else:
                    if value == cell_value:
                        result.append(record)

            return TableData(result)
        else:
            return TableData([])

    def sort(self, column_name: str, ascending: bool):
        """
        Sort records in the current table.
        :param column_name: Which values to use for sorting the table
        :param ascending: if True sort records in ascending order (a-z), otherwise sort in descending order (z-a)
        """
        if self.count() > 0:
            self._raise_error_if_column_not_present(0, column_name)
        self._table_data.sort(key=lambda row: row[column_name], reverse=not ascending)
        return self
