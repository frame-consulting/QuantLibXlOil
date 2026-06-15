# QuantLib-Python Wrappers for Excel

This folder contains wrapper functions for QuantLib object creation and method calls.

We follow the file structure of the [QuantLib-SWIG](https://github.com/lballabio/QuantLib-SWIG/tree/master/SWIG) interface specification to ensure transparency what the functions do.

The current implementation includes the functionality of [QuantLib-SWIG 1.41](https://github.com/lballabio/QuantLib-SWIG/releases).

## Implementation Guidelines

We apply the following guidelines for function implementation to ensure consistency across the Excel interface.

The guidelines aim at mimicking the classical [QuantLibXL](https://github.com/eehlers/QuantLibAddin-Old/tree/master/QuantLibAddin/gensrc/metadata/functions) interface. If necessary or if it is deemed an improvement, we deviate from the QuantLibXL interface.

### Code Formatter and Layout

The code is formatted using [Black Formatter](https://github.com/psf/black) with the default settings. We use the latest version of the relevant [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter).

Furthermore, the code is organised as follows:
First come the import statements, sorted alphabetically, then the enumerations and enumerated Classes, followed by the [argument converter functions](#argument-converter-functions) and returner functions, and finally the remaining functions and constructors in the same order as in the corresponding SWIG files.

### Function Names

We use lower camel case function names with `ql` as prefix.

Constructor function are identified by the class name, e.g., `Schedule`. We do not use `CreateSomeObject`, `MakeSomeObject` unless the SWIG interface specifies that function.

Class member functions are identified by the class name concatenated with member function name. Class name corresponds to the class where the function is declared.

### Function Argument Names and Types

Function argument names follow the names of the SWIG interface names. All function argument names are snake_case.

Argument types are specified as type annotations. Build-in types (`str`, `int`, `float`, `bool`) are used directly. Argument types should always be specified, except in cases where this would conflict with the Swig implementation.

Dates from Excel are supplied as serial numbers. We use the `qDate` argument [converter function](https://xloil.readthedocs.io/en/stable/xlOil_Python/TypeConversion.html#custom-type-conversion) for type annotation.

QuantLib object types are used directly as type annotations. User-created QuantLib object are stored in the xlOil cache and are supplied by xlOil as objects to the function.

For enumerations and enumerated classes (e.g. calendars, day count conventions) we also use converter functions.

Lists of inputs are specified as `xlo.Array(dims=1)`. This is applied for any underlying object types. Note that type checking and error handling is advised in the interface function. 
To convert lists, general converter functions such as `to_float_list` should be used, which convert various input types into a list of floating-point numbers. Such functions should be implemented in `utilities.py`. 

### Return Types

Function results are returned as is. The type of the function result should be specified. The specified type should be a QuantLib type or a build-in type.

If the result type has a custom [argument converter functions](#argument-converter-functions) then a corresponding custom return [type conversion](https://xloil.readthedocs.io/en/stable/xlOil_Python/TypeConversion.html#custom-return-conversion) should be implemented as well.

Return type converters are use the function name prefix `x`, e.g., `xDate(...)` for conversion from `ql.Date` to excel serial number.

### Function Annotations

xlOil function annotations are specified as follows:

```
@xlo.func(
    help='One-line docstring.',
    args={
        'arg_one': 'Help on argument one parameter.',
        'arg_two': 'Help on argument two parameter.',
    },
    group=EXCEL_GROUP_NAME,
    )
def qlFunctionName(arg_one : Type1, arg_two : Type2, trigger = None):
    ...
    return some_thing
```

The arguments `help` and `args` are shown in Excel in the *Insert Function* (*fx*) dialog.

Use Excel help strings for function and arguments equal/similar as in the classical [QuantLibXL](https://github.com/eehlers/QuantLibAddin-Old/tree/master/QuantLibAddin/gensrc/metadata/functions) interface.

Help string is a capitalised sentence finished with punctuation.

Excel argument names `arg_one` and `arg_two` equal function argument names. This is required to populate the help string to Excel.

No Python docstring or Python docstring equals the Excel help string.

### Additional Trigger Function Argument

Functions should include an additional `trigger` argument as specified in the section above.

QuantLib functions (may) depend on session data and QuantLib's internal state. As a consequence, updates may not be propagated through Excel's dependency tree.

For example, the `Index.fixing(...)` method depends on the session-specific `evaluationDate`. However,  Excel cannot recognise a change in `evaluationDate` and re-calculate an `Index.fixing(...)`.

Another example is the method `Instrument.NPV()`. This method requires a preceding call of `Instrument.setPricingEngine(engine)`. However, Excel on its own cannot determine that the pricing engine needs to be linked to the instrument before an NPV can be calculated. 

To mitigate above limitation, the `trigger` argument allows specifying additional input cells. That way, the QuantLib dependencies can be reflected in Excel's dependency graph by the user.

### Enumerations and Enumerated Classes

QuantLib uses various enumerations, e.g., for business day conventions (`Preceding`, `ModifiedFollowing`, `Following`) and volatility types (`Normal`, `ShiftedLognormal`).

Similarly, class objects may specify behaviour of functions. Typical examples are `DayCounter` and `Calendar`.

Enumerations and enumerated classes are represented by string identifiers in Excel.

The string identifiers are mapped to QuantLib objects via (constant) dictionaries as follows.

```
QL_TYPE_NAME = {
    'STRINGIDENTIER' : ql.Type1,
    'STRINGIDENTIER' : ql.Type2,
    ...
}
```

Here, `TYPE_NAME` represents the QuantLib type, e.g. `BUSINESS_DAY_CONVENTION`, `CALENDAR`. Camel case names are replaced by upper case names with underscores.

Dictionary keys are upper case.

Dictionary entries are ordered alphabetically by key.

Several identifiers may point to the same QuantLib object, e.g. `MODIFIEDFOLLOWING` and `MF` may point to `ql.ModifiedFollowing` business day convention.

Text identifiers follow the [QuantLibXL enumerations specification](https://github.com/eehlers/QuantLibAddin-Old/tree/master/QuantLibAddin/gensrc/metadata/enumerations).

### Argument Converter Functions

[Argument converters](https://xloil.readthedocs.io/en/stable/xlOil_Python/TypeConversion.html#custom-type-conversion) are specified by `@xlo.converter()` decorator.

Argument converter functions typically take an input string (from Excel) and convert it into a QuantLib class object or QuantLib enumeration (int) object.

Argument converters also need to handle default values for QuantLib wrapper functions. Default values typically are QuantLib class object or QuantLib enumeration

We use the following pattern and naming conventions for argument converters.

```
def _qSomeQuantLibType(s : string) -> ql.SomeQuantLibType
    if isinstance(s, ql.SomeQuantLibType):
        return s
    [do actual conversion]
    return quantlib_object

@xlo.converter()
def qSomeQuantLibType(s : string) -> ql.SomeQuantLibType
    return _qSomeQuantLibType(s)

def qlSomeQuantLibFunction(arg : qSomeQuantLibType = ql.SomeDefault())
    ...
    return
```

The similarities in prefixes `_q`, `q` and `ql.` and the common use of `SomeQuantLibType` naming aims at improving AI coding support.

Note that the decorated functions `qSomeQuantLibType` are accessible in Python via the \_\_wrapped\_\_ attribute. The functions attribute allow for testing conversions and manually calling conversions (if necessary).

## Testing

Each function should be covered by a test [here](../../tests/).

Details on test case specification are documented [here](../../tests/README.md).
