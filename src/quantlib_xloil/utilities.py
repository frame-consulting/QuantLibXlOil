import numpy as np
import QuantLib as ql


def first_key(d: dict, value, default_value=None):
    """Returns the first key of a dictionary that has the specified value."""
    for k, v in d.items():
        if v == value:
            return k
    if not default_value:
        raise ValueError(f"Value {value} not found in dictionary.")
    return first_key(d, default_value, default_value=None)


UNKNOWN_KEY = "UNKNOWN"
UNKNOWN_VALUE = -1


def enum_value(key: str, enum_dict: dict, value_type=int):
    """Converts a string to an enum value using the provided dictionary."""
    if isinstance(key, value_type):  # handle default values
        return key
    if isinstance(key, str):
        key = key.strip().upper()
        if key in enum_dict:
            return enum_dict[key]
    raise ValueError(f"Cannot convert {key} using {str(enum_dict)}.")


def enum_instance(key, enum_dict: dict, value_type):
    """Converts a string to an instance using a dictionary of classes/factories."""
    if isinstance(key, value_type):
        return key
    if isinstance(key, str):
        key = key.strip().upper()
        if key in enum_dict:
            return enum_dict[key]()  # Call factory to create instance
    # Extract clean type name (e.g., "Currency" from "QuantLib.QuantLib.Currency")
    type_name = getattr(value_type, "__name__", str(value_type))
    type_name = type_name.split(".")[-1] if "." in type_name else type_name
    raise ValueError(f"Unknown {type_name.lower()}: {key}")


def enum_class(key, enum_dict: dict, value_type):
    """Converts a string to a class using a dictionary of classes."""
    if isinstance(key, value_type):
        return key
    if isinstance(key, str):
        key = key.strip().upper()
        if key in enum_dict:
            return enum_dict[key]
    type_name = getattr(value_type, "__name__", str(value_type)).split(".")[-1]
    raise ValueError(f"Unknown {type_name.lower()}: {key}")


def to_float_list(values) -> list[float]:
    if values is None:
        return []
    if isinstance(values, (int, float)):
        return [float(values)]
    if isinstance(values, (list, tuple)):
        return [float(v) for v in values]
    if isinstance(values, np.ndarray):
        return values.astype(float).ravel().tolist()
    try:
        return [float(v) for v in list(values)]
    except Exception:
        raise ValueError(f"Cannot convert {values} to list of floats.")


def to_float_matrix(values) -> list[list[float]]:
    if values is None:
        return []
    if isinstance(values, np.ndarray):
        return values.astype(float).tolist()
    if isinstance(values, ql.Matrix):
        return [
            [float(values[i][j]) for j in range(values.columns())]
            for i in range(values.rows())
        ]
    return [[float(v) for v in row] for row in values]


def to_int_list(values) -> list[int]:
    if values is None:
        return []
    if isinstance(values, (int, float)):
        return [int(values)]
    if isinstance(values, (list, tuple)):
        return [int(v) for v in values]
    if isinstance(values, np.ndarray):
        return values.astype(int).ravel().tolist()
    raise ValueError(f"Cannot convert {values} to list of ints.")


def to_bool_list(values) -> list[bool]:
    if values is None:
        return []
    if isinstance(values, (bool, int, float, np.generic)):
        return [bool(values)]
    if isinstance(values, (list, tuple)):
        return [bool(v) for v in values]
    if isinstance(values, np.ndarray):
        return values.astype(bool).ravel().tolist()
    try:
        return [bool(v) for v in list(values)]
    except Exception:
        raise ValueError(f"Cannot convert {values!r} to list of bools.")


def to_object_list(values, object_type=object) -> tuple[object, ...]:
    if values is None:
        return ()
    if isinstance(values, object_type):
        return (values,)
    if isinstance(values, (list, tuple)):
        return tuple(cf for cf in values)
    if isinstance(values, np.ndarray):
        return tuple(values.ravel().tolist())
    raise ValueError(f"Cannot convert {values} to tuple of type {object_type}.")
