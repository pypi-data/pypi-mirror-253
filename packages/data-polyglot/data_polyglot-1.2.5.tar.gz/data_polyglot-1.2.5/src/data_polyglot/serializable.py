import inspect
from typing import Union
from . import constants


def serialize(key_name: str, required: bool = True, default_value=None, custom_converter=None):
    """
    A function to define a serializable field. Example:
        class Payload(Serializable):
            name: str = serialize('name')
            item_id: int = serialize('id')

    :param key_name: use this as attribute name in JSON.
    :param required: When using 'to_json' and set to True, then object with value None is added,
                        otherwise it is not added to payload
                    When using 'from_json' and set to True, then raise an error
                        if required field is missing from response, otherwise set model value to None.
    :param default_value: if value is None then use specified default value
    :param custom_converter: a function to apply to a model value when making payload,
                    or a function to apply to a response value.
                    For example convert datetime to string, or from string to a datetime.
    """
    def _serialize(self=None):
        return {constants.PROP_KEY_NAME: key_name, constants.PROP_REQUIRED: required,
                constants.PROP_DEFAULT_VALUE: default_value, constants.PROP_CUSTOM_CONVERTER: custom_converter}

    return _serialize


class KeyErrorMessage(str):
    """
    Workaround to print multi-line messages with KeyError exception
    """
    def __repr__(self): return str(self)


class Serializable:
    """
    Model for payload or response should extend this class.
    Described variables using `serialize` function.
    When creating a payload, assign values to the class and used `to_json()` that will convert class to the JSON object.
    When deserializing response use `from_json( <response.json()> )` function to parse all values and assign to the model.
    Example usage:

        class ItemDetails(Serializable):
            color: str = serialize('color')
            weight: float = serialize('weight')

        class Payload(Serializable):
            item_id: int = serialize('id', required=True)
            name: str = serialize('name')
            price: float = serialize('price', default=9.99)
            creation_date: str = serialize('date', custom_converter=lambda date: date.strftime('%Y-%m-%d'))
            item_details = ItemDetails.nest('itemDetails')

        After the values have been assigned, `to_json()` would create the following:
        {
            'id': 123,
            'name': 'some name',
            'price': 1.1,
            date: '2023-10-23',  # note the custom_converter changing datetime variable to string (assuming you used datetime)
            'itemDetails': {
                'color': 'red',
                'weight': 5.5
            }
        }
    """
    @staticmethod
    def __get_class_methods(prop_class, is_instance):
        return prop_class.__dir__() if is_instance else prop_class.__dict__

    @staticmethod
    def __get_class_attribute(prop_class, attr, is_instance):
        return prop_class.__getattribute__(attr) if is_instance else prop_class.__getattribute__(prop_class, attr)

    @staticmethod
    def __create_meta(prop_class, is_instance):
        __metadata = {constants.PROP_VARIABLE: {}, constants.PROP_CLASS: {}}
        content = Serializable.__get_class_methods(prop_class, is_instance)

        for attr in content:
            value = Serializable.__get_class_attribute(prop_class, attr, is_instance)

            if 'serialize.' in str(value) and attr != 'serialize':
                v = value()
                if v[constants.PROP_DEFAULT_VALUE] is not None:
                    v[constants.PROP_REQUIRED] = False
                __metadata[constants.PROP_VARIABLE].update({attr: v})
            elif inspect.isclass(value) and issubclass(value, Serializable):
                nested_class = '_Serializable__nested' in value.__dict__.keys()
                if nested_class:
                    key_name = value.__nested[constants.PROP_KEY_NAME]
                    required = value.__nested[constants.PROP_REQUIRED]
                    __metadata[constants.PROP_CLASS].update({attr: {constants.PROP_KEY_NAME: key_name,
                                                                    constants.PROP_REQUIRED: required}})
        return __metadata

    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls, *args, **kwargs)
        inst.__metadata = Serializable.__create_meta(inst, True)
        return inst

    @classmethod
    def __from_json_obj(cls, j_obj: dict):
        if isinstance(j_obj, list):
            raise ValueError(f'Error: expected json object, got json array instead.\n{j_obj}')

        data = cls()
        for prop_name, prop_params in data.__metadata[constants.PROP_VARIABLE].items():
            j_key = prop_params[constants.PROP_KEY_NAME]
            required = prop_params[constants.PROP_REQUIRED]
            default_value = prop_params[constants.PROP_DEFAULT_VALUE]
            custom_converter = prop_params[constants.PROP_CUSTOM_CONVERTER]

            if j_key not in j_obj:
                if not required:
                    value = None if default_value is None else default_value
                else:
                    error_message = f'Error: could not find the key "{j_key}" assigned to prop "{prop_name}".\n' \
                                    f'Class property: {prop_name} | Attributes: {str(prop_params)}\n' \
                                    f'Object Content: {j_obj}'
                    raise KeyError(KeyErrorMessage(error_message))
            else:
                value = j_obj[j_key]
                if custom_converter is not None:
                    try:
                        value = custom_converter(value)
                    except ValueError as verr:
                        error_message = f'Error: an exception occurred while converting parsed value\n' \
                                        f'Class property: {prop_name} | JSON key: {j_key} | Original value: {value} | '\
                                        f'Original value type: {type(value)}\n' \
                                        f'Inner exception: {verr.args}\n' \
                                        f'Object Content: {j_obj}'
                        raise ValueError(error_message)
            data.__setattr__(prop_name, value)

        for prop_class, prop_class_params in data.__metadata[constants.PROP_CLASS].items():
            if prop_class != '__class__':
                property_class = data.__getattribute__(prop_class)
                j_key = prop_class_params[constants.PROP_KEY_NAME]
                required = prop_class_params[constants.PROP_REQUIRED]
                if j_key not in j_obj:
                    if required:
                        error_message = f'Error: could not find the key "{j_key}" assigned to prop "{prop_class}".\n' \
                                        f'Class property: {prop_class} | Attributes: {str(prop_class_params)}\n' \
                                        f'Object Content: {j_obj}'
                        raise KeyError(KeyErrorMessage(error_message))
                    else:
                        data.__setattr__(prop_class, None)
                else:
                    j = j_obj[j_key]
                    if j is not None:
                        value = property_class.from_json(j)
                        data.__setattr__(prop_class, value)
                    else:
                        if not required:
                            data.__setattr__(prop_class, None)
                        else:
                            error_message = f'Error: value is Null for the key "{j_key}" assigned to prop "{prop_class}".\n' \
                                            f'Class property: {prop_class} | Attributes: {str(prop_class_params)}\n' \
                                            f'Object Content: {j_obj}'
                            raise KeyError(error_message)
        return data

    @staticmethod
    def __dict_to_json_text(source: dict) -> str:
        json_text = '{'
        count_down = len(source.items())
        for key, value in source.items():
            if type(value) == str:
                j_property = f'"{key}": "{value}"'
            elif type(value) == int or type(value) == float:
                j_property = f'"{key}": {value}'
            elif value is None:
                j_property = f'"{key}": null'
            elif type(value) == bool:
                j_property = f'"{key}": {str(value).lower()}'
            elif type(value) == dict:
                j_property = f'"{key}": {Serializable.__dict_to_json_text(value)}'
            elif type(value) == list:
                j_property = f'"{key}": {Serializable.__list_to_json_text(value)}'
            else:
                raise ValueError(f'Error: cannot convert type "{type(value)}" to json text')
            if count_down > 1:
                j_property += ','
            count_down -= 1
            json_text += j_property
        json_text += '}'
        return json_text

    @staticmethod
    def __list_to_json_text(data: list) -> str:
        json_text = '['
        if len(data) > 0:
            if type(data[0]) == str:
                j_arr = '"' + str.join('", "', data) + '"'
            elif type(data[0]) == int or type(data[0]) == float:
                j_arr = str.join(', ', [str(d) for d in data])
            elif type(data[0]) == bool:
                j_arr = str.join(', ', [str(d) for d in data]).lower()
            elif type(data[0]) == dict:
                j_arr = [Serializable.__dict_to_json_text(d) for d in data]
                j_arr = str.join(', ', j_arr)
            elif type(data[0]) == list:
                j_arr = [Serializable.__list_to_json_text(d) for d in data]
                j_arr = str.join(', ', j_arr)
            else:
                raise ValueError(f'Error: cannot convert type "{type(data[0])}" to json text')
            json_text += j_arr
        json_text += ']'
        return json_text

    @staticmethod
    def serialize(key_name: str, required: bool = True, default_value=None, custom_converter=None):
        """
        A function to define a serializable field.
        :param key_name: use this as attribute name in JSON.
        :param required: When using 'to_json' and set to True, then object with value None is added,
                            otherwise it is not added to payload
                        When using 'from_json' and set to True, then raise an error
                            if required field is missing from response, otherwise set model value to None.
        :param default_value: if value is None then use specified default value
        :param custom_converter: a function to apply to a model value when making payload,
                        or a function to apply to a response value.
                        For example convert datetime to string, or from string to a datetime.
        """
        return serialize(key_name, required, default_value, custom_converter)
    
    @classmethod
    def nest(cls, key_name: str, required: bool = True):
        """
        Use this method when assigning a nested JSON object. Example:
            class NestedJObj(Serializable):
                argument1: str = serialize('arg1')

            class JObj(Serializable):
                some_class_property = NestedJObj.nest('more_params')

            would have the following schema:
            {
                "more_params": {
                    "arg1": "string"
                }
            }

        :param key_name: use this as attribute name in JSON.
        :param required: When using 'to_json' and set to True, then class with value None is added as null,
                            otherwise it is not added to the payload
                        When using 'from_json' and set to True, then raise an error
                            if required class is missing from response, otherwise set model value to None.
        """
        cls.__nested = {constants.PROP_KEY_NAME: key_name, constants.PROP_REQUIRED: required}
        cls.__metadata = Serializable.__create_meta(cls, False)
        return cls

    def to_json(self):
        """
        Serialize class to a dictionary that can be used by `requests` library.
        :return: class variables converted into the JSON dictionary based on the `serialize` parameters
        """
        j_obj = {}
        props = self.__metadata[constants.PROP_VARIABLE]
        classes = self.__metadata[constants.PROP_CLASS]
        for prop_class, prop_class_params in classes.items():
            if prop_class != '__class__':
                required = prop_class_params[constants.PROP_REQUIRED]
                cl = self.__getattribute__(prop_class)
                if cl is None:
                    if required:
                        error_message = f'Error: required value is None for the key "{prop_class_params[constants.PROP_KEY_NAME]}" ' \
                                        f'assigned to prop "{prop_class}".\n' \
                                        f'Class property: {prop_class} | Attributes: {str(prop_class_params)}\n' \
                                        f'Object Content: {j_obj}'
                        raise ValueError(error_message)
                    else:
                        j_obj.update({prop_class_params[constants.PROP_KEY_NAME]: None})
                elif inspect.isclass(cl) and issubclass(cl, Serializable):
                    new_cl = cl()
                    new_cl.__setattr__('_Serializable__metadata', cl.__metadata)
                    data = cl.to_json(new_cl)
                    j_obj.update({prop_class_params[constants.PROP_KEY_NAME]: data})
                elif type(cl) == list:
                    data = []
                    if len(cl) != 0:
                        if issubclass(type(cl[0]), Serializable):
                            for nested_class in cl:
                                n = nested_class.to_json()
                                data.append(n)
                        else:
                            error_message = f'Error: cannot serialize "{prop_class}". Attributes: {str(prop_class_params)}\n'
                            raise ValueError(error_message)
                    j_obj.update({prop_class_params[constants.PROP_KEY_NAME]: data})
                else:
                    data = cl.to_json()
                    j_obj.update({prop_class_params[constants.PROP_KEY_NAME]: data})

        for prop_name, prop_params in props.items():
            required = prop_params[constants.PROP_REQUIRED]
            default_value = prop_params[constants.PROP_DEFAULT_VALUE]
            value = self.__getattribute__(prop_name)
            v = value
            if inspect.ismethod(value) or inspect.isfunction(value):
                if required:
                    v = default_value
                else:
                    if default_value is not None:
                        v = default_value
                    else:
                        continue
            if prop_params[constants.PROP_CUSTOM_CONVERTER] is not None:
                try:
                    v = prop_params[constants.PROP_CUSTOM_CONVERTER](value)
                except ValueError as verr:
                    error_message = f'Error: an exception occurred while converting variable\n' \
                                    f'Class property: {prop_name} | JSON key: {prop_params[constants.PROP_KEY_NAME]} | Original value: {value} | ' \
                                    f'Original value type: {type(value)}\n' \
                                    f'Inner exception: {verr.args}\n' \
                                    f'Object Content: {j_obj}'
                    raise ValueError(error_message)

            j_obj.update({prop_params[constants.PROP_KEY_NAME]: v})

        return j_obj

    def to_json_text(self) -> str:
        """
        Turn json dictionary or list of dictionaries into the string.
        Use it if you find some payload nesting a JSON as string.
        :return: dictionary or list of dictionaries converted into a string.
        """
        data = self.to_json()
        json_text = ''
        if type(data) == dict:
            json_text += self.__dict_to_json_text(data)
        elif type(data) == list:
            json_text += self.__list_to_json_text(data)
        return json_text

    @classmethod
    def from_json(cls, json: Union[list, dict]):
        """
        Deserialize JSON response after it's been converted to a list or a dictionary using `response.json()`
        :param json: either a List of dictionaries, or a Dictionary with json objects.
        :return: assign all values to class variables based on `serialize` parameters, and return itself.
        """
        if type(json) == dict:
            return cls.__from_json_obj(json)
        else:
            data = []
            if len(json) != 0:
                if type(json[0]) == dict:
                    for j_obj in json:
                        data.append(cls.__from_json_obj(j_obj))
                else:
                    error_message = f'Error: argument must be a dict or a list of dict, got "{type(json)}" instead.\n' \
                                    f'Content: {json}'
                    raise ValueError(error_message)
            return data
