import datetime
import xloil as xlo

_EXCEL_GROUP_NAME = "QuantLibXlOil - Alias Repository"

_REPOSITORY = {}

_ENV_ALIAS = "ALIAS"
_ENV_OBJ = "OBJECT"
_ENV_VERSION = "VERSION"
_ENV_CREATED = "CREATED"
_ENV_UPDATED = "UPDATED"

_ALIAS_DELIMITER = "#"


def _normalised_alias(alias: str):
    if not isinstance(alias, str):
        raise TypeError("alias {} must be a string".format(alias))
    return alias.strip().upper().split(_ALIAS_DELIMITER)[0]


def _alias_suffix(alias: str):
    if not isinstance(alias, str):
        raise TypeError("alias {} must be a string".format(alias))
    parts = alias.strip().upper().split(_ALIAS_DELIMITER)
    if len(parts) == 1:
        return None
    if len(parts) != 2:
        raise ValueError("alias {} must be of the form 'name#suffix'".format(alias))
    suffix = parts[1]
    try:
        suffix = int(suffix)
    except ValueError:
        raise ValueError("alias {} suffix must be an integer".format(alias))
    if suffix < 0:
        raise ValueError("alias {} suffix must be a non-negative integer".format(alias))
    return suffix


def _envelope(alias, obj):
    e = {
        _ENV_ALIAS: alias,
        _ENV_OBJ: obj,
        _ENV_VERSION: 0,
        _ENV_CREATED: datetime.datetime.now(),
        _ENV_UPDATED: datetime.datetime.now(),
    }
    return e


def _set(alias: str, obj):
    alias = _normalised_alias(alias)
    if not alias in _REPOSITORY:
        # create
        _REPOSITORY[alias] = _envelope(alias, obj)
    else:
        current_obj_type = type(_REPOSITORY[alias][_ENV_OBJ])
        new_obj_type = type(obj)
        if current_obj_type != new_obj_type:
            raise TypeError(
                "Alias {} already exists with current type: {}. Cannot update with new type: {}. Delete the existing alias first or use a different alias.".format(
                    alias, current_obj_type, new_obj_type
                )
            )
        # update
        _REPOSITORY[alias][_ENV_OBJ] = obj
        _REPOSITORY[alias][_ENV_VERSION] += 1
        _REPOSITORY[alias][_ENV_UPDATED] = datetime.datetime.now()
    #
    return (
        _REPOSITORY[alias][_ENV_ALIAS]
        + _ALIAS_DELIMITER
        + str(_REPOSITORY[alias][_ENV_VERSION])
    )


def _get(alias: str):
    suf = _alias_suffix(alias)
    alias = _normalised_alias(alias)
    if not alias in _REPOSITORY:
        raise KeyError("Key {} not found in repository".format(alias))
    if suf is not None:
        if suf != _REPOSITORY[alias][_ENV_VERSION]:
            raise KeyError(
                "Key {} version {} not found in repository".format(alias, suf)
            )
    return _REPOSITORY[alias][_ENV_OBJ]


def _get_envelope(alias: str):
    suf = _alias_suffix(alias)
    alias = _normalised_alias(alias)
    if not alias in _REPOSITORY:
        raise KeyError("Key {} not found in repository".format(alias))
    if suf is not None:
        if suf != _REPOSITORY[alias][_ENV_VERSION]:
            raise KeyError(
                "Key {} version {} not found in repository".format(alias, suf)
            )
    env = _REPOSITORY[alias]
    return [[k, env[k]] for k in env]


def _delete(alias: str):
    alias = _normalised_alias(alias)
    if not alias in _REPOSITORY:
        raise KeyError("Key {} not found in repository".format(alias))
    del _REPOSITORY[alias]
    return True


def _get_repository():
    header = [
        _ENV_ALIAS,
        _ENV_OBJ,
        _ENV_VERSION,
        _ENV_CREATED,
        _ENV_UPDATED,
    ]
    table = [header]
    for alias, env in _REPOSITORY.items():
        row = [
            env[_ENV_ALIAS],
            env[_ENV_OBJ],
            env[_ENV_VERSION],
            env[_ENV_CREATED],
            env[_ENV_UPDATED],
        ]
        table.append(row)
    return table


def _clear_repository():
    _REPOSITORY.clear()
    return True


@xlo.func(
    help="Set an object in the Object Dictionary",
    args={
        "alias": "The alias to set the object under",
        "obj": "The object to set",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlAliasSet(alias: str, obj, trigger=None) -> str:
    return _set(alias, obj)


@xlo.func(
    help="Get an object from the Object Dictionary",
    args={
        "alias": "The alias to get the object from",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlAliasGet(alias: str, trigger=None):
    return _get(alias)


@xlo.func(
    help="Get an envelope from the Object Dictionary",
    args={
        "alias": "The alias to get the envelope from",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlAliasEnvelope(alias: str, trigger=None):
    return _get_envelope(alias)


@xlo.func(
    help="Delete an object from the Object Dictionary",
    args={
        "alias": "The alias of the object to delete",
    },
    group=_EXCEL_GROUP_NAME,
)
def qlAliasDelete(alias: str, trigger=None) -> bool:
    return _delete(alias)


@xlo.func(
    help="Get the entire Object Dictionary repository",
    group=_EXCEL_GROUP_NAME,
)
def qlAliasGetRepository(trigger=None):
    return _get_repository()


@xlo.func(
    help="Clear the entire Object Dictionary repository",
    group=_EXCEL_GROUP_NAME,
)
def qlAliasClearRepository(trigger=None) -> bool:
    return _clear_repository()
