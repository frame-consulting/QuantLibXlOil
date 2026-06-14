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
