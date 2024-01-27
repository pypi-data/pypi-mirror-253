import abc
import copy
from dataclasses import is_dataclass, fields, asdict
from typing import Type, Optional, get_type_hints, Mapping, Any, MutableMapping

from dacite.cache import cache
from dacite.config import Config
from dacite.core import _build_value, T
from dacite.data import Data
from dacite.dataclasses import (
    get_default_value_for_field,
    DefaultValueNotFoundError,
    get_fields,
    is_frozen,
)
from dacite.exceptions import (
    ForwardReferenceError,
    WrongTypeError,
    MissingValueError,
    DaciteFieldError,
    UnexpectedDataError,
)
from dacite.types import (
    is_instance,
)
from jsonargparse._util import import_object


# Adapted from dataclasses.asdict
def asdict(obj, dict_factory=dict):
    if is_dataclass(obj):
        result = []
        for f in fields(obj):
            value = asdict(getattr(obj, f.name), dict_factory)
            result.append((f.name, value))
        if isinstance(obj, abc.ABC):
            return dict_factory([
                ("class_path", ".".join([obj.__module__, obj.__class__.__name__])),
                ("init_args", dict_factory(result))
            ])
        else:
            return dict_factory(result)
    elif isinstance(obj, tuple) and hasattr(obj, '_fields'):
        return type(obj)(*[asdict(v, dict_factory) for v in obj])
    elif isinstance(obj, (list, tuple)):
        return type(obj)(asdict(v, dict_factory) for v in obj)
    elif isinstance(obj, dict):
        return type(obj)((asdict(k, dict_factory),
                          asdict(v, dict_factory))
                         for k, v in obj.items())
    else:
        return copy.deepcopy(obj)


# Adapted from https://github.com/konradhalas/dacite/blob/v1.8.1/dacite/core.py
def from_dict(data_class: Type[T], data: Data, config: Optional[Config] = None) -> T:
    """Create a data class instance from a dictionary.

    :param data_class: a data class type
    :param data: a dictionary of a input data
    :param config: a configuration of the creation process
    :return: an instance of a data class
    """
    init_values: MutableMapping[str, Any] = {}
    post_init_values: MutableMapping[str, Any] = {}
    config = config or Config()
    try:
        data_class_hints = cache(get_type_hints)(data_class, localns=config.hashable_forward_references)
    except NameError as error:
        raise ForwardReferenceError(str(error))
    data_class_fields = cache(get_fields)(data_class)
    if config.strict:
        extra_fields = set(data.keys()) - {f.name for f in data_class_fields}
        if extra_fields:
            raise UnexpectedDataError(keys=extra_fields)

    for field in data_class_fields:
        field_type = data_class_hints[field.name]
        if field.name in data:
            try:
                field_data = data[field.name]
                if (isinstance(field_data, Mapping)
                        and len(field_data) == 2
                        and 'class_path' in field_data
                        and 'init_args' in field_data):
                    field_type = import_object(field_data['class_path'])
                    field_data = field_data['init_args']
                value = _build_value(type_=field_type, data=field_data, config=config)
            except DaciteFieldError as error:
                error.update_path(field.name)
                raise
            if config.check_types and not is_instance(value, field_type):
                raise WrongTypeError(field_path=field.name, field_type=field_type, value=value)
        else:
            try:
                value = get_default_value_for_field(field, field_type)
            except DefaultValueNotFoundError:
                if not field.init:
                    continue
                raise MissingValueError(field.name)
        if field.init:
            init_values[field.name] = value
        elif not is_frozen(data_class):
            post_init_values[field.name] = value
    instance = data_class(**init_values)
    for key, value in post_init_values.items():
        setattr(instance, key, value)
    return instance
