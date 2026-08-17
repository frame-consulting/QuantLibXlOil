import xloil as xlo

import os
import re

from ..utilities import UNKNOWN_KEY
from .quantlib_xloil_version import qlXlOilVersion

_EXCEL_GROUP_NAME = "QuantLibXlOil - Inspect Code"

QL_DICTIONARIES = {}
QL_FUNCTIONS = {}

_url_to_blob = r"https://github.com/frame-consulting/QuantLibXlOil/blob/"
_path_to_source = r"/src/quantlib_xloil/"


def _source_path():
    m = re.match(r"(.*[a-zA-Z])(.*)(inspect_code\.py)", __file__)
    this_path = m.group(1)
    path_delim = m.group(2)
    return this_path + path_delim + ".." + path_delim


def _souce_file_names():
    source_dir = _source_path()
    return os.listdir(source_dir)


def _intitialise_lists():
    global QL_DICTIONARIES, QL_FUNCTIONS
    if QL_DICTIONARIES and QL_FUNCTIONS:
        # Initialise only once
        return
    source_dir = _source_path()
    source_files = _souce_file_names()
    version = "v" + qlXlOilVersion()
    dictionaries = {}
    functions = {}
    for file_name in source_files:
        if not file_name.endswith(".py") or file_name.startswith("__"):
            continue
        with open(os.path.join(source_dir, file_name), "r") as f:
            for idx, line in enumerate(f):
                # dictionaries
                if line.startswith("QL_") and "=" in line:
                    dict_name = line.split("=")[0].strip()
                    link = (
                        _url_to_blob
                        + version
                        + _path_to_source
                        + file_name
                        + "#L"
                        + str(idx + 1)
                    )
                    #
                    dictionaries[dict_name] = link
                # functions
                if line.startswith("def ql") and "(" in line:
                    func_name = line.split("(")[0].split("def")[1].strip()
                    link = (
                        _url_to_blob
                        + version
                        + _path_to_source
                        + file_name
                        + "#L"
                        + str(idx + 1)
                    )
                    functions[func_name] = link
    QL_DICTIONARIES = dictionaries
    QL_FUNCTIONS = functions


def _dictionary_entries(dict_name: str) -> list:
    if dict_name not in QL_DICTIONARIES:
        raise ValueError(f"Dictionary {dict_name} not found.")
    try:
        import_code = f"from quantlib_xloil import {dict_name}"
        exec(import_code, globals())
    except Exception as e:
        raise ValueError(f"Could not import dictionary {dict_name}: {e}")
    try:
        dictionary = eval(dict_name, globals())
    except Exception as e:
        raise ValueError(f"Could not evaluate dictionary {dict_name}: {e}")
    keys_and_values = []
    if isinstance(dictionary, dict):
        keys = list(dictionary.keys())
        if UNKNOWN_KEY in keys:
            keys.remove(UNKNOWN_KEY)
        keys_and_values = [[str(k), str(dictionary[k])] for k in keys]
    if isinstance(dictionary, list) or isinstance(dictionary, tuple):
        keys = [str(k) for k in dictionary]
        keys_and_values = [[k, None] for k in keys]
    if not keys_and_values:
        raise ValueError(
            f"Dictionary {dict_name} is not a dict, list, or tuple, but {type(dictionary)}."
        )
    keys_and_values.sort(key=lambda x: x[0])
    return keys_and_values


@xlo.func(
    help="Returns a list of available dictionaries in QuantLibXlOil.",
    args={
        "with_links": "Whether to include links to the dictionary definitions.",
        "with_header": "Whether to include a header row.",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlListDictionaries(
    with_links: bool = True, with_header: bool = False, trigger=None
) -> list:
    _intitialise_lists()
    if with_links:
        header = ["Dictionary Name", "Link"]
        result = [[d, QL_DICTIONARIES[d]] for d in QL_DICTIONARIES]
    else:
        header = ["Dictionary Name"]
        result = [[d] for d in QL_DICTIONARIES]
    result.sort(key=lambda x: x[0])
    if with_header:
        result = [header] + result
    return result


@xlo.func(
    help="Returns a list of available functions in QuantLibXlOil.",
    args={
        "with_links": "Whether to include links to the function definitions.",
        "with_header": "Whether to include a header row.",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlListFunctions(
    with_links: bool = True, with_header: bool = False, trigger=None
) -> list:
    _intitialise_lists()
    if with_links:
        header = ["Function Name", "Link"]
        result = [[f, QL_FUNCTIONS[f]] for f in QL_FUNCTIONS]
    else:
        header = ["Function Name"]
        result = [[f] for f in QL_FUNCTIONS]
    result.sort(key=lambda x: x[0])
    if with_header:
        result = [header] + result
    return result


@xlo.func(
    help="Returns a list of keys for a given dictionary in QuantLibXlOil.",
    args={
        "dict_name": "The name of the dictionary.",
        "with_values": "Whether to include the values to the keys.",
        "with_header": "Whether to include a header row.",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlListDictionaryEntries(
    dict_name: str,
    with_values: bool = True,
    with_header: bool = False,
    trigger=None,
) -> list:
    _intitialise_lists()
    entry = _dictionary_entries(dict_name)
    if with_values:
        header = ["Key", "Value"]
        result = entry
    else:
        header = ["Key"]
        result = [[k[0]] for k in entry]
    if with_header:
        result = [header] + result
    return result
