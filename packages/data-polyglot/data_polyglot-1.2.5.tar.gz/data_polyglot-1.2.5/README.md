# data_polyglot
The goal of this project is to create a set of tools to help write API tests faster.

List of tools:
- [JSON Serializer](#json-serializer)
- [Table Data](#tabledata-class)
- [Local Storage](#local-storage)

## JSON Serializer
Create models for payload and response with fewer lines of code then alternative packages.
Leverage the power of autocomplete to access variables. 
C# does it with Newtonsoft, it's time we get a similar convenient way of serialization.

    class SomeData(Serializable):
        name: str = serialize('name')
        item_id: int = serialize('id')

    payload = SomeData()
    payload.name = 'some item name'
    payload.item_id = 123

    data = payload.to_json()
    # data would be { 'name': 'some item name', 'id': 123 }

    response = requests.get('https://example.com/items')
    response_data = SomeData.from_json(response.json())

Note the use of type hinting.

### serialize(key_name, required, default_value, custom_converter) for to_json()

- **key_name**: Key in a dictionary when creating payload (JSON attribute).
- **required**: Set False will not add field to the payload if value is None.
                Set True will add None field as null.
- **default_value**: If value was not assigned to the class variable use this default value.
- **custom_converter**: A function to convert class variable to another type, 
                like `datetime` into string.

Example of custom_converter:

    # Assign datetime to a class variable 'date'. It will be converted to a string.
    date = serialize('date', custom_converter=lambda date: date.strftime('%Y-%m-%d'))

### serialize(key_name, required, default_value, custom_converter) for from_json()

- **key_name**: JSON attribute to parse from the dictionary.
- **required**: Set False will not raise an error if field is missing in response, but will assign None
                Set True will rase an error if field is missing in response.
- **default_value**: If field is missing in response assign specified default value (require flag ignored)
- **custom_converter**: A function to convert variable to another type, 
                for example, string to datetime.

Example of custom_converter:

    # Assuming the datetime sting has a pattern '%Y-%m-%d', parse the field and convert to datetime.
    date: datetime = serialize('date', custom_converter=lambda date: datetime.strptime(date, '%Y-%m-%d'))

**NOTE!** `from_json` can process a `list` and return a list of serialized object, 
BUT it doesn't hint that it's a list. Either do type hinting on returned value, 
or process list yourself.
    
    # process list without type hinting
    expected_list = [ResponseExampleModel.from_json(j_obj) for j_obj in response.json()]

    # process list with type hinting
    expected_list: List[ResponseExampleModel] = ResponseExampleModel.from_json(response.json())

### Nested classes
It's very common to nest JSON objects inside the payload or the response. Here's how to do it:

    # Create an object that would be nested following instructions provided above.
    class NestedObject(Serializable):
        argument1: str = serialize('arg1')

    class Payload(Serializable):
        nested_obj = NestedObject.nest('nested object')

This structure will correspond with the following schema:

    {
        "nested object": {
            "arg1": "string"
        }
    }
        
If nested object is expected to be of type `list`, then it's crucial to specify type hint:
    
    class Payload(Serializable):
        nested_obj: List[NestedObject] = NestedObject.nest('nested object') 

- Using `to_json` when `.nest('key_name', required=True)` raise error if class is None.
- Using `to_json` when `.nest('key_name', required=False)` set json property to null if class is None.
- Using `from_json` when `.nest('key_name', required=True)` raise error when did not find the field.
- Using `from_json` when `.nest('key_name', required=False)` set class variable to None if did not find the field.

### to_json_text()
Uses `to_json` method to create json structure and then turn it into a string. 
Valuable when you have a payload that expects part of the json to be nested inside the string of a JSON property.

### Error Reporting
We want to write as few models as possible, so when we see the similarities between responses we would
instinctively want to share one model between them. As feature development goes on we may see changes
in responses that leads to breaking change in our automation framework.
When this happens an error message will show exactly what and where a property broke.

Errors in `custom_converter` will also raise a meaningful exception.

## TableData class
A wrapper around API response for the table content to be rendered on the front-end.
Includes common table operations such as 'filter records by column name',
'get column value by row index'.
Your response would look something like this:

    {
        "page": 0,
        "per_page": 50,
        "table": [
            {"name": "item1", "price": 1.99, "quantity": 10 },
            {"name": "item2", "price": 2.99, "quantity": 5 },
            {"name": "item3", "price": 3.99, "quantity": 7 },
        ]
    }

In this case just pass down the table into the class during instantiation:

    table = TableData(response.json()['table'])

You can also use `TableData` class in conjunction with [Serializable class](#json-serializer).
The example bellow demonstrates how to do that with the response example above: 

    class TableResponseModel(Serializable):
        page: int = Serializable.serialize('page')
        per_page: int = Serializable.serialize('per_page')
        table: TableData = Serializable.serialize('table', custom_converter=lambda j_arr: TableData(j_arr))

Example how to use table data:
    
    table = TableData(response.json()['table'])
    table = table.filter_by_column_name('type', 'food')
    value = table.get_column_value_by_row_index(0, 'name')

You can also extend `TableData` class and create methods to wrap column name, 
so you don't have to hardcode strings in your tests.


## Local Storage
Store your test data locally in a JSON file using `LocalStorage` class.
Useful when connecting data seeding scripts with test running scripts. 
Create, read, update and delete data as if it was an external microservice, providing path to data as an endpoint. 
In case the project ever grows to have the need for an external microservice to store test data - 
it would be a fast transition.

To start:
- Initialize local storage by providing the file path. If file doesn't exist, new file will be created.
- Save simple data types, dictionaries, and lists using `create` method.
- Read data in the specified path using `read` method.

Example:

    file_path = os.path.dirname(os.path.abspath(__file__))

    storage = LocalStorage(file_path)
    storage.create('/inventory/item_1/name', 'Do not delete!')
    item_name = storage.read('/inventory/item_1/name')

    storage.update('/inventory/item_1/name', 'Do not delete 1!')
    exists = storage.is_key_present('/inventory/item_1/name')
    storage.delete('/inventory/item_1/name')
