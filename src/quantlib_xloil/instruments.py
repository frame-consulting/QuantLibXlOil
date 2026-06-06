import QuantLib as ql
import xloil as xlo

from .config import EXCEL_GROUP_NAME
from .ratehelpers import qQuoteHandle


# Instrument interfaces

@xlo.func(
    help='Return the NPV of a QuantLib Instrument.',
    args={
        'instrument': 'QuantLib Instrument.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlInstrumentNPV(instrument: ql.Instrument, trigger=None) -> float:
    return instrument.NPV()


@xlo.func(
    help='Return the error estimate of a QuantLib Instrument.',
    args={
        'instrument': 'QuantLib Instrument.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlInstrumentErrorEstimate(instrument: ql.Instrument, trigger=None) -> float:
    return instrument.errorEstimate()

@xlo.func(
    help='Return whether a QuantLib Instrument is expired.',
    args={
        'instrument': 'QuantLib Instrument.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlInstrumentIsExpired(instrument: ql.Instrument, trigger=None) -> bool:
    return instrument.isExpired()


@xlo.func(
    help='Set the pricing engine for a QuantLib Instrument.',
    args={
        'instrument': 'QuantLib Instrument.',
        'engine': 'QuantLib PricingEngine.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlInstrumentSetPricingEngine(
    instrument: ql.Instrument,
    engine: ql.PricingEngine,
    trigger=None,
) -> bool:
    instrument.setPricingEngine(engine)
    return True


# basic instruments

@xlo.func(
    help='Create a QuantLib Stock from a QuoteHandle.',
    args={
        'quote': 'QuantLib QuoteHandle.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlStock(quote: qQuoteHandle, trigger=None) -> ql.Stock:
    return ql.Stock(quote)


@xlo.func(
    help='Create a QuantLib CompositeInstrument from an array of Instruments.',
    args={
        'instruments': 'Array of QuantLib Instruments.',
        'multipliers': 'Optional array of multipliers for each instrument.',
    },
    group=EXCEL_GROUP_NAME,
)
def qlCompositeInstrument(
    instruments: xlo.Array(dims=1),
    multipliers: xlo.Array(dims=1) = None,
    trigger = None,
) -> ql.CompositeInstrument:
    if multipliers is None:
        multipliers = [1.0] * len(instruments)
    elif len(multipliers) == 1:
        multipliers = [multipliers[0]] * len(instruments)
    elif len(multipliers) != len(instruments):
        raise ValueError("Length of multipliers must be 1 or equal to length of instruments.")
    # Apply multipliers to instruments
    composite = ql.CompositeInstrument()
    for i, m in zip(instruments, multipliers):
        composite.add(i, m)
    return composite
