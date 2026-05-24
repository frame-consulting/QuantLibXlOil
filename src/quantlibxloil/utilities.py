
def first_key(d : dict, value, default_value=None):
    """Returns the first key of a dictionary that has the specified value."""
    for k, v in d.items():
        if v == value:
            return k
    if not default_value:
        raise ValueError(f"Value {value} not found in dictionary.")
    return first_key(d, default_value, default_value=None)

UNKNOWN_KEY = "UNKNOWN"
UNKNOWN_VALUE = -1

def enum_value(string : str, enum_dict : dict):
    """Converts a string to an enum value using the provided dictionary."""
    if isinstance(string, int):  # handle default values
        return string
    if isinstance(string, str):
        string = string.strip().upper()
        if string in enum_dict:
            return enum_dict[string]
    raise ValueError(f"Cannot convert {string} using {str(enum_dict)}.")
