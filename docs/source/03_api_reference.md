# API Reference

This section lists the QuantLib functions made available to Excel.


## Bonds


[qBondPriceType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L32)(bond_price_type: str)


[qCallabilityType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L37)(callability_type: str)


[qlBondPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L49)(amount: float, price_type: qBondPriceType)


[qlCallability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L62)(price: ql.BondPrice, callability_type: qCallabilityType, date: qDate, trigger = None)


[qlSoftCallability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L78)(price: ql.BondPrice, callability_type: qCallabilityType, date: qDate, trigger = None)


[qlBondPriceAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L91)(bond_price: ql.BondPrice, trigger = None)


[qlBondPriceType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L103)(bond_price: ql.BondPrice, trigger = None)


[qlBondPriceIsValid](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L117)(bond_price: ql.BondPrice, trigger = None)


[qlCallabilityPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L128)(callability: ql.Callability, trigger = None)


[qlCallabilityType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L140)(callability: ql.Callability, trigger = None)


[qlCallabilityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L154)(callability: ql.Callability, trigger = None)


[qlBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L170)(settlement_days: int, calendar: qCalendar, face_amount: float, maturity_date: qDate, cashflows: ql.Leg, issue_date: qDate = ql.Date(), trigger = None)


[qlBond2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L199)(settlement_days: int, calendar: qCalendar, issue_date: qDate = ql.Date(), coupons = ql.Leg(), trigger = None)


[qlBondNextCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L217)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondPreviousCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L229)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondNextCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L243)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondPreviousCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L257)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondSettlementDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L270)(bond: ql.Bond, trigger = None)


[qlBondSettlementDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L282)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondIsTradable](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L296)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L307)(bond: ql.Bond, trigger = None)


[qlBondMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L318)(bond: ql.Bond, trigger = None)


[qlBondIssueDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L329)(bond: ql.Bond, trigger = None)


[qlBondCashFlows](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L340)(bond: ql.Bond, trigger = None)


[qlBondRedemption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L351)(bond: ql.Bond, trigger = None)


[qlBondRedemptions](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L362)(bond: ql.Bond, trigger = None)


[qlBondCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L373)(bond: ql.Bond, trigger = None)


[qlBondNotionals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L385)(bond: ql.Bond, trigger = None)


[qlBondNotional](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L397)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondCleanPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L408)(bond: ql.Bond, trigger = None)


[qlBondCleanPrice2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L424)(bond: ql.Bond, yield_: float, dc: qDayCounter, compounding: qCompounding, frequency: qFrequency = ql.Annual, settlement: qDate = ql.Date(), trigger = None)


[qlBondDirtyPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L443)(bond: ql.Bond, trigger = None)


[qlBondDirtyPrice2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L459)(bond: ql.Bond, yield_: float, dc: qDayCounter, compounding: qCompounding, frequency: qFrequency, settlement: qDate = ql.Date(), trigger = None)


[qlBondYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L483)(bond: ql.Bond, dc: qDayCounter, compounding: qCompounding, freq: qFrequency, accuracy: float = 1.0e-8, max_evaluations: int = 100, trigger = None)


[qlBondYield2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L510)(bond: ql.Bond, price: ql.BondPrice, dc: qDayCounter, compounding: qCompounding, freq: qFrequency, settlement: qDate = ql.Date(), accuracy: float = 1.0e-8, max_evaluations: int = 100, guess: float = 0.05, trigger = None)


[qlBondAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L535)(bond: ql.Bond, settlement: qDate = ql.Date(), trigger = None)


[qlBondSettlementValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L548)(bond: ql.Bond, trigger = None)


[qlBondSettlementValue2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L560)(bond: ql.Bond, clean_price: float, trigger = None)


[qlBondCleanPriceFromZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L578)(bond: ql.Bond, discount_curve: ql.YieldTermStructureHandle, z_spread: float = 0.002, dc: qDayCounter = ql.Actual365Fixed(), compounding: qCompounding = ql.Compounded, freq: qFrequency = ql.Annual, settlement_date: qDate = ql.Date(), trigger = None)


[qlBondsinkingSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L605)(bond: ql.Bond, start_date: qDate, bond_length: qPeriod, frequency: qFrequency, payment_calendar: qCalendar, trigger = None)


[qlBondSinkingNotionals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L628)(bond: ql.Bond, bond_length: qPeriod, frequency: qFrequency, coupon_rate: float, initial_notional: float, trigger = None)


[qlZeroCouponBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L651)(settlement_days: int, calendar: qCalendar, face_amount: float, maturity_date: qDate, business_day_convention: qBusinessDayConvention = ql.Following, redemption: float = 100.0, issue_date: qDate = ql.Date(), trigger = None)


[qlFixedRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L691)(settlement_days: int, face_amount: float, schedule: ql.Schedule, coupons: xlo.Array(dims=1), payment_day_counter: qDayCounter, business_day_convention: qBusinessDayConvention = ql.Following, redemption: float = 100.0, issue_date: qDate = ql.Date(), payment_calendar: qCalendar = ql.NullCalendar(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, trigger = None)


[qlAmortizingFixedRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L742)(settlement_days: int, notionals: xlo.Array(dims=1), schedule: ql.Schedule, coupons: xlo.Array(dims=1), accrual_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, issue_date: qDate = ql.Date(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, redemption = 100, trigger = None)


[qlAmortizingFloatingRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L799)(settlement_days: int, notional: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.IborIndex, accrual_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, fixing_days: int = 0, gearings: xlo.Array(dims=1) = [1.0], spreads: xlo.Array(dims=1) = [0.0], caps = None, floors = None, in_arrears: bool = False, issue_date: qDate = ql.Date(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, redemptions = 100.0, payment_lag: int = 0, trigger = None)


[qlFloatingRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L869)(settlement_days: int, face_amount: float, schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, fixing_days: int = 0, gearings: xlo.Array(dims=1) = [1.0], spreads: xlo.Array(dims=1) = [0.0], caps = None, floors = None, in_arrears: bool = False, redemption: float = 100.0, issue_date: qDate = ql.Date(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, trigger = None)


[qlCmsRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L933)(settlement_days: int, face_amount: float, schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter, payment_convention: qBusinessDayConvention, fixing_days: int, gearings: xlo.Array(dims=1), spreads: xlo.Array(dims=1), caps: xlo.Array(dims=1), floors: xlo.Array(dims=1), in_arrears: bool = False, redemption: float = 100.0, issue_date: qDate = ql.Date(), trigger = None)


[qlAmortizingCmsRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L988)(settlement_days: int, notionals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, fixing_days: int = 0, gearings: xlo.Array(dims=1) = [0.0], spreads: xlo.Array(dims=1) = [0.0], caps: xlo.Array(dims=1) = None, floors: xlo.Array(dims=1) = None, in_arrears: bool = False, issue_date: qDate = ql.Date(), trigger = None)


[qlBondSetDiscountingEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1029)(bond: ql.Bond, discount_curve: ql.YieldTermStructureHandle, trigger = None)


## Calendars


[qCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L107)(calendarname: str)


[qBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L112)(conventionname: str)


[qJointCalendarRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L117)(rule_name: str)


[qlCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L133)(calendar_name: str, trigger = None)


[qlCalendarisWeekend](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L144)(calendar: qCalendar, weekday: qWeekday, trigger = None)


[qlCalendarStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L155)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L166)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsBusinessDay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L177)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L188)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L199)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L210)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarAddHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L221)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarRemoveHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L232)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarResetAddedAndRemovedHolidays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L241)(calendar: qCalendar, trigger = None)


[qlCalendarAdjust](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L254)(calendar: qCalendar, date: qDate, convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCalendarAdvance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L275)(calendar: qCalendar, date: qDate, n: int, unit: qTimeUnit, convention: qBusinessDayConvention = ql.Following, end_of_month: bool = False, trigger = None)


[qlCalendarAdvance2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L298)(calendar: qCalendar, date: qDate, period: qPeriod, convention: qBusinessDayConvention = ql.Following, end_of_month: bool = False, trigger = None)


[qlCalendarBusinessDaysBetween](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L320)(calendar: qCalendar, from_date: qDate, to_date: qDate, include_first: bool = True, include_last: bool = False, trigger = None)


[qlCalendarHolidayList](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L338)(calendar: qCalendar, from_date: qDate, to_date: qDate, trigger = None)


[qlCalendarBusinessDayList](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L351)(calendar: qCalendar, from_date: qDate, to_date: qDate, trigger = None)


[qlCalendarName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L364)(calendar: qCalendar, trigger = None)


[qlCalendarEmpty](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L375)(calendar: qCalendar, trigger = None)


[qlCalendarJointCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L388)(calendar1: qCalendar, calendar2: qCalendar, rule: qJointCalendarRule = ql.JoinHolidays)


[qlCalendarJointCalendar2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L406)(calendar1: qCalendar, calendar2: qCalendar, calendar3: qCalendar, rule: qJointCalendarRule = ql.JoinHolidays, trigger = None)


## Calibratedmodel


[qlCalibratedModelCalibrate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L38)(model: ql.CalibratedModel, calibration_helpers: xlo.Array(dims=1), optimization_method: ql.OptimizationMethod, end_criteria: ql.EndCriteria, constraint: ql.Constraint = ql.NoConstraint(), weights: xlo.Array(dims=1) = [], fix_parameters: xlo.Array(dims=1) = [], trigger = None)


[qlCalibratedModelParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L67)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelSetParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L82)(model: ql.CalibratedModel, params: xlo.Array(dims=1), trigger = None)


[qlCalibratedModelValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L100)(model: ql.CalibratedModel, params: xlo.Array(dims=1), calibration_helpers: xlo.Array(dims=1), trigger = None)


[qlCalibratedModelConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L116)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelEndCriteria](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L128)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelProblemValues](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L140)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelProblemValuesFunctionEvaluation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L152)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L164)(model: ql.CalibratedModel, trigger = None)


## Calibrationhelpers


[qBlackCalibrationHelperErrorType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L28)(s: str)


[qlBlackCalibrationHelperSetPricingEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L40)(helper: ql.BlackCalibrationHelper, engine: ql.PricingEngine, trigger = None)


[qlBlackCalibrationHelperMarketValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L56)(helper: ql.BlackCalibrationHelper, trigger = None)


[qlBlackCalibrationHelperModelValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L70)(helper: ql.BlackCalibrationHelper, trigger = None)


[qlBlackCalibrationHelperImpliedVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L89)(helper: ql.BlackCalibrationHelper, target_value: float, accuracy: float = 1.0e-8, max_evaluations: int = 100, min_volatility: float = 1.0e-8, max_volatility: float = 4.0, trigger = None)


[qlBlackCalibrationHelperBlackPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L111)(helper: ql.BlackCalibrationHelper, volatility: float, trigger = None)


[qlBlackCalibrationHelperVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L126)(helper: ql.BlackCalibrationHelper, trigger = None)


[qlBlackCalibrationHelperVolatilityType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L140)(helper: ql.BlackCalibrationHelper, trigger = None)


[qlBlackCalibrationHelperCalibrationError](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L154)(helper: ql.BlackCalibrationHelper, trigger = None)


[qlSwaptionHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L185)(exercise, swap_length, volatility: qQuoteHandle, index: ql.IborIndex, fixed_leg_tenor: qPeriod, fixed_leg_day_counter: qDayCounter, floating_leg_day_counter: qDayCounter, term_structure: ql.YieldTermStructureHandle, error_type: qBlackCalibrationHelperErrorType = ql.BlackCalibrationHelper.RelativePriceError, strike: float = ql.nullDouble(), nominal: float = 1.0, volatility_type: qVolatilityType = ql.ShiftedLognormal, shift: float = 0.0, settlement_days: int = ql.nullInt(), averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlCapHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L250)(length: qPeriod, volatility: qQuoteHandle, index: ql.IborIndex, fixed_leg_frequency: qFrequency, fixed_leg_day_counter: qDayCounter, include_first_swaplet: bool, term_structure: ql.YieldTermStructureHandle, error_type: qBlackCalibrationHelperErrorType = ql.BlackCalibrationHelper.RelativePriceError, volatility_type: qVolatilityType = ql.ShiftedLognormal, shift: float = 0.0, trigger = None)


[qlHestonModelHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibrationhelpers.py#L292)(maturity: qPeriod, calendar: qCalendar, s0: float, strike_price: float, volatility: qQuoteHandle, risk_free_rate: ql.YieldTermStructureHandle, dividend_yield: ql.YieldTermStructureHandle, error_type: qBlackCalibrationHelperErrorType = ql.BlackCalibrationHelper.RelativePriceError, trigger = None)


## Cashflows


[qDurationType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L54)(duration_type: str)


[qRateAveragingType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L59)(averaging_type: str)


[qlSimpleCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L71)(amount: float, date: qDate, trigger = None)


[qlRedemption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L83)(amount: float, date: qDate, trigger = None)


[qlAmortizingPayment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L95)(amount: float, date: qDate, trigger = None)


[qlIndexedCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L113)(notional: float, index: ql.Index, base_date: qDate, fixing_date: qDate, payment_date: qDate, growth_only: bool = False, trigger = None)


[qlCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L134)(cashflow: ql.CashFlow, trigger = None)


[qlCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L145)(cashflow: ql.CashFlow, trigger = None)


[qlCashFlowHasOccurred](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L157)(cashflow: ql.CashFlow, ref_date: qDate = ql.Date(), trigger = None)


[qlAsIndexedCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L170)(cashflow: ql.CashFlow, trigger = None)


[qlAsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L181)(cashflow: ql.CashFlow, trigger = None)


[qlCouponNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L192)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L203)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L214)(coupon: ql.Coupon, trigger = None)


[qlCouponReferencePeriodStart](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L225)(coupon: ql.Coupon, trigger = None)


[qlCouponReferencePeriodEnd](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L236)(coupon: ql.Coupon, trigger = None)


[qlCouponExCouponDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L247)(coupon: ql.Coupon, trigger = None)


[qlCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L258)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L269)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L280)(coupon: ql.Coupon, trigger = None)


[qlCouponDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L291)(coupon: ql.Coupon, trigger = None)


[qlCouponAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L303)(coupon: ql.Coupon, date: qDate, trigger = None)


[qlAsFixedRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L314)(cashflow: ql.CashFlow, trigger = None)


[qlAsFloatingRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L325)(cashflow: ql.CashFlow, trigger = None)


[qlFloatingRateCouponFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L338)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L351)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponIsInArrears](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L362)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponGearing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L375)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L386)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L397)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponAdjustedFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L410)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L423)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L437)(coupon: ql.FloatingRateCoupon, discount_curve: ql.YieldTermStructureHandle, trigger = None)


[qlFloatingRateCouponIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L452)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponSetPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L466)(coupon: ql.FloatingRateCoupon, pricer: ql.FloatingRateCouponPricer, trigger = None)


[qlCappedFlooredCouponIsCapped](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L482)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponIsFloored](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L493)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponCap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L506)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L517)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponEffectiveCap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L528)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponEffectiveFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L541)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlOvernightIndexedCouponAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L554)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponCanApplyTelescopicFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L567)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponApplyObservationShift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L580)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponCompoundSpreadDaily](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L593)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponLockoutDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L606)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponRateComputationStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L619)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponRateComputationEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L632)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponValueDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L645)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponFixingDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L658)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponInterestDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L671)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponDt](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L684)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponIndexFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L697)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponEffectiveIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L710)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponEffectiveSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L723)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponUnderlying](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L736)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponNakedOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L750)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponDailyCapFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L764)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L778)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L792)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L806)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L820)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlAsOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L834)(cashflow: ql.CashFlow, trigger = None)


[qlAsCappedFlooredOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L847)(cashflow: ql.CashFlow, trigger = None)


[qlAsMultipleResetsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L860)(cashflow: ql.CashFlow, trigger = None)


[qlFixedRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L881)(payment_date: qDate, nominal: float, rate: float, day_counter: qDayCounter, start_date: qDate, end_date: qDate, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlIborCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L925)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlCappedFlooredIborCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L981)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, spread: float = 0.0, cap: float = ql.nullDouble(), floor: float = ql.nullDouble(), ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1040)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, overnight_index: ql.OvernightIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, lookback_days: int = ql.nullInt(), lockout_days: int = 0, apply_observation_shift: bool = False, compound_spread: bool = False, trigger = None)


[qlCappedFlooredOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1090)(underlying: ql.OvernightIndexedCoupon, cap: float = ql.nullDouble(), floor: float = ql.nullDouble(), naked_option: bool = False, daily_cap_floor: bool = False, trigger = None)


[qlCmsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1122)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.SwapIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlCmsSpreadCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1174)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.SwapSpreadIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlRangeAccrualFloatersCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1227)(payment_date: qDate, nominal: float, index: ql.IborIndex, start_date: qDate, end_date: qDate, fixing_days: int, day_counter: qDayCounter, gearing: float, spread: float, ref_period_start: qDate, ref_period_end: qDate, observations_schedule: ql.Schedule, lower_trigger: float, upper_trigger: float, trigger = None)


[qlMultipleResetsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1280)(payment_date: qDate, nominal: float, reset_schedule: ql.Schedule, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, coupon_spread: float = 0.0, rate_spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlBlackIborCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1320)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), trigger = None)


[qlCompoundingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1331)(trigger = None)


[qlArithmeticAveragedOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1346)(mean_reversion: float = 0.03, volatility: float = 0.0, by_approx: bool = False, trigger = None)


[qlBlackCompoundingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1365)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), effective_volatility_input: bool = False, trigger = None)


[qlBlackAveragingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1383)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), effective_volatility_input: bool = False, trigger = None)


[qlCompoundingMultipleResetsPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1397)(trigger = None)


[qlAveragingMultipleResetsPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1407)(trigger = None)


[qlSetCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1419)(leg: xlo.Array(dims=1), pricer: ql.FloatingRateCouponPricer, trigger = None)


[qlFixedRateLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1437)(schedule: ql.Schedule, day_counter: qDayCounter, nominals: xlo.Array(dims=1), coupon_rates: xlo.Array(dims=1), payment_adjustment: qBusinessDayConvention = ql.Following, trigger = None)


[qlIborLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1471)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, fixing_days = (), gearings: xlo.Array(dims=1) = None, spreads: xlo.Array(dims=1) = None, caps: xlo.Array(dims=1) = None, floors: xlo.Array(dims=1) = None, is_in_arrears: bool = False, trigger = None)


[qlOvernightLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1515)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.OvernightIndex, payment_day_counter: qDayCounter = ql.Actual360(), payment_convention: qBusinessDayConvention = ql.Following, gearings: xlo.Array(dims=1) = None, spreads: xlo.Array(dims=1) = None, telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlCmsLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1551)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCmsZeroLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1579)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCmsSpreadLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1607)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapSpreadIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlMultipleResetsLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1634)(full_reset_schedule: ql.Schedule, index: ql.IborIndex, resets_per_coupon: int, nominals: xlo.Array(dims=1), trigger = None)


[qlRangeAccrualLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1657)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter = ql.Actual360(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCashFlowsStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1681)(leg: xlo.Array(dims=1), trigger = None)


[qlCashFlowsMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1692)(leg: xlo.Array(dims=1), trigger = None)


[qlCashFlowsPreviousCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1705)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1725)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsPreviousCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1745)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1765)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsPreviousCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1785)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1805)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccrualPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1825)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccrualDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1845)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1865)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1885)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1905)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpv](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1927)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1955)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1986)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2024)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, z_spread: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2060)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBpsFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2088)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBpsFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2119)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvBps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2153)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAtmRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2183)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), npv: float = ql.nullDouble(), trigger = None)


[qlCashFlowsYieldRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2216)(leg: xlo.Array(dims=1), npv: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), accuracy: float = 1.0e-10, max_iterations: int = 10000, guess: float = 0.05, trigger = None)


[qlCashFlowsDurationFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2256)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, duration_type: qDurationType, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsDurationFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2286)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, duration_type: qDurationType, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsConvexityFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2323)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsConvexityFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2357)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBasisPointValueFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2386)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBasisPointValueFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2420)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2450)(leg: xlo.Array(dims=1), npv: float, discount_curve: ql.YieldTermStructure, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), accuracy: float = 1.0e-10, max_iterations: int = 100, guess: float = 0.0, trigger = None)


[qlDurationTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2488)(duration_type: qDurationType, trigger = None)


[qlRateAveragingTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2499)(averaging_type: qRateAveragingType, trigger = None)


## Currencies


[qCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L130)(code: str)


[qlCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L147)(name: str, code: str, numerical_code: int, symbol: str, fraction_symbol: str, fractions_per_unit: int, rounding: ql.Rounding, trigger = None)


[qlCurrencyName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L176)(currency: qCurrency, trigger = None)


[qlCurrencyCode](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L187)(currency: qCurrency, trigger = None)


[qlCurrencyNumericalCode](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L198)(currency: qCurrency, trigger = None)


[qlCurrencySymbol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L209)(currency: qCurrency, trigger = None)


[qlCurrencyFractionSymbol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L220)(currency: qCurrency, trigger = None)


[qlCurrencyFractionsPerUnit](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L231)(currency: qCurrency, trigger = None)


[qlCurrencyRounding](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L242)(currency: qCurrency, trigger = None)


[qlCurrencyTriangulationCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L253)(currency: qCurrency, trigger = None)


## Date


[qDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L81)(serialnumber)


[qFrequency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L86)(s: str)


[qPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L91)(s: str)


[qTimeUnit](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L96)(s: str)


[qWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L101)(s: str)


[qlPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L123)(n: int, unit: qTimeUnit, trigger = None)


[qlPeriodLength](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L134)(period: qPeriod, trigger = None)


[qlPeriodUnits](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L145)(period: qPeriod, trigger = None)


[qlPeriodFrequency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L156)(period: qPeriod, trigger = None)


[qlPeriodNormalized](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L167)(period: qPeriod, trigger = None)


[qlDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L180)(year: int, month: int, day: int, trigger = None)


[qlDateWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L191)(date: qDate, trigger = None)


[qlDateDayOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L202)(date: qDate, trigger = None)


[qlDateDayOfYear](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L213)(date: qDate, trigger = None)


[qlDateMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L224)(date: qDate, trigger = None)


[qlDateYear](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L235)(date: qDate, trigger = None)


[qlDateIsLeap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L246)(year: int, trigger = None)


[qlDateMinDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L254)(trigger = None)


[qlDateMaxDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L262)(trigger = None)


[qlDateTodaysDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L270)(trigger = None)


[qlDateStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L280)(date: qDate, trigger = None)


[qlDateEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L290)(date: qDate, trigger = None)


[qlDateIsStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L300)(date: qDate, trigger = None)


[qlDateIsEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L310)(date: qDate, trigger = None)


[qlDateNextWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L321)(date: qDate, weekday: qWeekday, trigger = None)


[qlDateNthWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L334)(n: int, weekday: qWeekday, month: int, year: int, trigger = None)


[qlDateParserParseFormatted](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L347)(date_string: str, format_string: str, trigger = None)


[qlDateParserParseISO](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L359)(date_string: str, trigger = None)


[qlPeriodParserParse](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L369)(period_string: str, trigger = None)


## Daycounters


[qDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L52)(s: str)


[qlDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L68)(daycounter_name: str, trigger = None)


[qlDayCounterDayCount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L81)(daycounter: qDayCounter, start_date: qDate, end_date: qDate, trigger = None)


[qlDayCounterYearFraction](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L98)(daycounter: qDayCounter, start_date: qDate, end_date: qDate, ref_start_date: qDate = ql.Date(), ref_end_date: qDate = ql.Date(), trigger = None)


[qlDayCounterName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L116)(daycounter: qDayCounter, trigger = None)


[qlDayCounterEmpty](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L127)(daycounter: qDayCounter, trigger = None)


[qlDayCounterYearFractionToDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L140)(daycounter: qDayCounter, ref_date: qDate, year_fraction: float, trigger = None)


## Dividends


[qlFixedDividend](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/dividends.py#L14)(amount: float, date: qDate, trigger = None)


[qlFractionalDividend](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/dividends.py#L23)(amount: float, date: qDate, trigger = None)


[qlDividendVector](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/dividends.py#L37)(dividend_dates: xlo.Array(dims=1), dividend_amounts: xlo.Array(dims=1), trigger = None)


## Exercise


[qExerciseType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L22)(s: str)


[qlExerciseType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L36)(exercise: ql.Exercise, trigger = None)


[qlExerciseDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L48)(exercise: ql.Exercise, idx: int, trigger = None)


[qlExerciseDateAt](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L60)(exercise: ql.Exercise, idx: int, trigger = None)


[qlExerciseDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L71)(exercise: ql.Exercise, trigger = None)


[qlEuropeanExercise](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L83)(date: qDate, trigger = None)


[qlBermudanExercise](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L92)(dates: xlo.Array(dims=1), trigger = None)


[qlAmericanExercise](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L104)(first_date: qDate, last_date: qDate, trigger = None)


[qlRebatedExercise](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L121)(exercise: ql.Exercise, rebates: xlo.Array(dims=1), rebate_settlement_days: int, rebate_payment_calendar: qCalendar = ql.NullCalendar(), rebate_payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlSwingExercise](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/exercise.py#L143)(dates: xlo.Array(dims=1), trigger = None)


## Grid


[qlTimeGrid](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/grid.py#L16)(end_time: float, steps: int, trigger = None)


[qlTimeGridFromTimes](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/grid.py#L25)(times: xlo.Array(dims=1), trigger = None)


[qlTimeGridWithMandatoryTimes](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/grid.py#L37)(mandatory_times: xlo.Array(dims=1), steps: int, trigger = None)


[qlTimeGridTimes](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/grid.py#L48)(grid: ql.TimeGrid, trigger = None)


## Indexes


[qlIndexManagerHistories](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L18)(trigger = None)


[qlIndexManagerClearHistories](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L26)(trigger = None)


[qlIndexName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L41)(index: ql.Index, trigger = None)


[qlIndexFixingCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L52)(index: ql.Index, trigger = None)


[qlIndexIsValidFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L64)(index: ql.Index, date: qDate, trigger = None)


[qlIndexHasHistoricalFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L76)(index: ql.Index, date: qDate, trigger = None)


[qlIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L89)(index: ql.Index, date: qDate, forecast_todays_fixing = False, trigger = None)


[qlIndexPastFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L103)(index: ql.Index, date: qDate, trigger = None)


[qlIndexAddFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L117)(index: ql.Index, date: qDate, value: float, force_overwrite: bool = False, trigger = None)


[qlIndexAddFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L138)(index: ql.Index, dates: xlo.Array(dims=1), values: xlo.Array(dims=1), force_overwrite: bool = False, trigger = None)


[qlIndexTimeSeries](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L158)(index: ql.Index, trigger = None)


[qlIndexClearFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L169)(index: ql.Index, trigger = None)


[qlInterestRateIndexFamilyName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L184)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L195)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L206)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L218)(index: ql.InterestRateIndex, value_date: qDate, trigger = None)


[qlInterestRateIndexCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L231)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L244)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L258)(index: ql.InterestRateIndex, value_date: qDate, trigger = None)


[qlInterestRateIndexValueDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L272)(index: ql.InterestRateIndex, fixing_date: qDate, trigger = None)


[qlIborIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L296)(family_name: str, tenor: qPeriod, settlement_days: int, currency: qCurrency, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, day_counter: qDayCounter, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCdor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L329)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlBbsw](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L345)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlBkbm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L361)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuribor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L377)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuribor365](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L393)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJibar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L409)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlMosprime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L425)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlNZDLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L441)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlPribor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L457)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlRobor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L473)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlShibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L489)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L505)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTHBFIX](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L521)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlWibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L537)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlZibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L553)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlAUDLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L569)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCADLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L585)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCHFLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L601)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlDKKLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L617)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEURLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L633)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlGBPLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L649)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJPYLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L665)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSEKLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L681)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTRLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L697)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlUSDLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L713)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlOvernightIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L736)(family_name: str, settlement_days: int, currency: qCurrency, calendar: qCalendar, day_counter: qDayCounter, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlAonia](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L757)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCdi](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L771)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCorra](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L785)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlDestr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L799)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEonia](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L813)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEstr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L827)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlFedFunds](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L841)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlKofr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L855)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlNzocr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L869)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSaron](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L883)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSofr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L897)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSonia](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L911)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSwestr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L925)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTonar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L939)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSwapIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L965)(family_name: str, tenor: qPeriod, settlement_days: int, currency: qCurrency, calendar: qCalendar, fixed_leg_tenor: qPeriod, fixed_leg_convention: qBusinessDayConvention, fixed_leg_day_counter: qDayCounter, ibor_index: ql.IborIndex, discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuriborSwapIsdaFixA](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1014)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuriborSwapIsdaFixB](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1035)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuriborSwapIfrFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1056)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEurLiborSwapIsdaFixA](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1077)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEurLiborSwapIsdaFixB](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1098)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEurLiborSwapIfrFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1119)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlChfLiborSwapIsdaFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1140)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlGbpLiborSwapIsdaFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1161)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJpyLiborSwapIsdaFixAm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1182)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJpyLiborSwapIsdaFixPm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1203)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlUsdLiborSwapIsdaFixAm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1224)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlUsdLiborSwapIsdaFixPm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1245)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSwapSpreadIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1271)(family_name: str, swap_index1: ql.SwapIndex, swap_index2: ql.SwapIndex, gearing1: float = 1.0, gearing2: float = -1.0, trigger = None)


[qlSwapIndexForecastFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1290)(swap_index: ql.SwapIndex, fixing_date: qDate)


[qlEquityIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1309)(name: str, fixing_calendar: qCalendar, currency: qCurrency, spot_price: float, disc_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), div_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


## Instruments


[qlInstrumentNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/instruments.py#L17)(instrument: ql.Instrument, trigger = None)


[qlInstrumentErrorEstimate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/instruments.py#L28)(instrument: ql.Instrument, trigger = None)


[qlInstrumentIsExpired](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/instruments.py#L39)(instrument: ql.Instrument, trigger = None)


[qlInstrumentSetPricingEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/instruments.py#L51)(instrument: ql.Instrument, engine: ql.PricingEngine, trigger = None)


[qlStock](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/instruments.py#L70)(quote: qQuoteHandle, trigger = None)


[qlCompositeInstrument](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/instruments.py#L82)(instruments: xlo.Array(dims=1), multipliers: xlo.Array(dims=1) = None, trigger = None)


## Interpolatedyieldcurves


[qlInterpolatedYieldCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L63)(dates: xlo.Array(dims=1), discounts: xlo.Array(dims=1), daycounter: qDayCounter, calendar: qCalendar, traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlDiscountCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L110)(dates: xlo.Array(dims=1), discounts: xlo.Array(dims=1), daycounter: qDayCounter = ql.Actual365Fixed(), calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlForwardCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L133)(dates: xlo.Array(dims=1), forwards: xlo.Array(dims=1), daycounter: qDayCounter = ql.Actual365Fixed(), calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlZeroCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L156)(dates: xlo.Array(dims=1), zerorates: xlo.Array(dims=1), daycounter: qDayCounter = ql.Actual365Fixed(), calendar: qCalendar = ql.NullCalendar(), trigger = None)


## Localvolatilities


[qFixedLocalVolSurfaceExtrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/localvolatilities.py#L22)(s: str)


[qlLocalConstantVol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/localvolatilities.py#L35)(reference_date: qDate, volatility: float, day_counter: qDayCounter, trigger = None)


[qlLocalVolSurface](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/localvolatilities.py#L55)(black_vol_tsh: ql.BlackVolTermStructureHandle, risk_free_ytsh: ql.YieldTermStructureHandle, dividend_ytsh: ql.YieldTermStructureHandle, underlying: qQuoteHandle, trigger = None)


[qlNoExceptLocalVolSurface](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/localvolatilities.py#L79)(black_vol_tsh: ql.BlackVolTermStructureHandle, risk_free_ytsh: ql.YieldTermStructureHandle, dividend_ytsh: ql.YieldTermStructureHandle, underlying: qQuoteHandle, illegal_local_vol_overwrite: float, trigger = None)


[qlFixedLocalVolSurface](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/localvolatilities.py#L117)(reference_date: qDate, dates: xlo.Array(dims=1), strikes: xlo.Array(dims=1), local_vol_matrix: xlo.Array(dims=2), day_counter: qDayCounter, interpolation_str: str = "LINEAR", lowerExtrapolation: qFixedLocalVolSurfaceExtrapolation = ql.FixedLocalVolSurface.ConstantExtrapolation, upperExtrapolation: qFixedLocalVolSurfaceExtrapolation = ql.FixedLocalVolSurface.ConstantExtrapolation, trigger = None)


## Optimizers


[qEndCriteriaType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L24)(s: str)


[qlNoConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L35)(trigger = None)


[qlPositiveConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L43)(trigger = None)


[qlBoundaryConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L55)(lower: float, upper: float, trigger = None)


[qlCompositeConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L69)(constraint_1: ql.Constraint, constraint_2: ql.Constraint, trigger = None)


[qlNonhomogeneousBoundaryConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L83)(lower: xlo.Array(dims=1), upper: xlo.Array(dims=1), trigger = None)


[qlEndCriteria](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L105)(max_iterations: int, max_stationary_state_iterations: int, root_epsilon: float, function_epsilon: float, gradient_norm_epsilon: float, trigger = None)


[qlEndCriteriaSucceded](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L130)(end_criteria: ql.EndCriteria, ec_type: qEndCriteriaType, trigger = None)


[qlLevenbergMarquardt](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/optimizers.py#L146)(epsfcn: float = 1.0e-8, xtol: float = 1.0e-8, gtol: float = 1.0e-8, use_cost_functions_jacobian: bool = False, trigger = None)


## Parameter


[qlParameterParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L15)(parameter: ql.Parameter, trigger = None)


[qlParameterSetParam](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L28)(parameter: ql.Parameter, idx: int, x: float, trigger = None)


[qlParameterTestParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L48)(parameter: ql.Parameter, params: xlo.Array(dims=1), trigger = None)


[qlParameterSize](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L60)(parameter: ql.Parameter, trigger = None)


[qlParameterAtTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L72)(parameter: ql.Parameter, t: float, trigger = None)


[qlParameterConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L81)(parameter: ql.Parameter, trigger = None)


[qlNullParameter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L93)(trigger = None)


[qlConstantParameter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L102)(constraint: ql.Constraint, value: float = None, trigger = None)


[qlPiecewiseConstantParameter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L122)(times: xlo.Array(dims=1), constraint: ql.Constraint = ql.NoConstraint(), trigger = None)


## Payoffs


[qOptionType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L19)(option_type: str)


[qlPayoffValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L31)(payoff: ql.Payoff, price: float, trigger = None)


[qlTypePayoffOptionType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L42)(payoff: ql.TypePayoff, trigger = None)


[qlStrikedTypePayoffStrike](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L53)(payoff: ql.StrikedTypePayoff, trigger = None)


[qlPlainVanillaPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L65)(option_type: qOptionType, strike: float, trigger = None)


[qlAsPlainVanillaPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L78)(payoff: ql.Payoff, trigger = None)


[qlPercentageStrikePayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L90)(option_type: qOptionType, moneyness: float, trigger = None)


[qlCashOrNothingPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L105)(option_type: qOptionType, strike: float, cash_payoff: float, trigger = None)


[qlAssetOrNothingPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L122)(option_type: qOptionType, strike: float, trigger = None)


[qlSuperSharePayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L137)(option_type: qOptionType, strike: float, increment: float, trigger = None)


[qlGapPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L155)(option_type: qOptionType, strike: float, strike_payoff: float, trigger = None)


[qlVanillaForwardPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/payoffs.py#L172)(option_type: qOptionType, strike: float, trigger = None)


## Piecewiseyieldcurve


[qlYieldTermStructureHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L50)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L67)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveTimes](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L81)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveData](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L95)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveAsYts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L115)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseYieldCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L163)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseYieldCurveWithJumpsAsYts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L203)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, jumps: xlo.Array(dims=1), jump_dates: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseYieldCurveWithJumps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L260)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, jumps: xlo.Array(dims=1), jump_dates: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseSpreadYieldCurveAsYts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L301)(base_curve: ql.YieldTermStructureHandle, instruments: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseSpreadYieldCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L347)(base_curve: ql.YieldTermStructureHandle, instruments: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


## Quantlib_


[qlVersion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/quantlib_.py#L13)(trigger = None)


[qlHexVersion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/quantlib_.py#L21)(trigger = None)


## Ratehelpers


[qFuturesType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L34)(s: str)


[qPillarChoice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L39)(s: str)


[qQuoteHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L44)(rate)


[qlRateHelperQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L64)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperLatestDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L75)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperEarliestDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L86)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L97)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperLatestRelevantDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L108)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperPillarDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L119)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperImpliedQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L131)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperQuoteError](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L143)(rate_helper: ql.RateHelper, trigger = None)


[qlDepositRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L160)(rate: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, daycounter: qDayCounter, trigger = None)


[qlDepositRateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L189)(rate: qQuoteHandle, index: ql.IborIndex, trigger = None)


[qlDepositRateHelper3](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L204)(rate: qQuoteHandle, fixing_date: qDate, index: ql.IborIndex, trigger = None)


[qlFRARateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L227)(rate: qQuoteHandle, month_to_start: int, month_to_end: int, fixing_days: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, day_counter: qDayCounter, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L268)(rate: qQuoteHandle, month_to_start: int, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelper3](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L295)(rate: qQuoteHandle, imm_offset_start: int, imm_offset_end: int, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelper4](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L328)(rate: qQuoteHandle, period_to_start: qPeriod, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelperForDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L356)(rate: qQuoteHandle, start_date: qDate, end_date: qDate, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFuturesRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L392)(price: qQuoteHandle, ibor_start_date: qDate, n_months: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, day_counter: qDayCounter, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), type: qFuturesType = ql.Futures.IMM, trigger = None)


[qlFuturesRateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L429)(price: qQuoteHandle, ibor_start_date: qDate, ibor_end_date: qDate, day_counter: qDayCounter, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), type: qFuturesType = ql.Futures.IMM, trigger = None)


[qlFuturesRateHelper3](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L454)(price: qQuoteHandle, ibor_start_date: qDate, index: ql.IborIndex, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), type: qFuturesType = ql.Futures.IMM, trigger = None)


[qlFuturesRateConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L474)(futures_rate_helper: ql.FuturesRateHelper, trigger = None)


[qlSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L501)(rate: qQuoteHandle, tenor: qPeriod, calendar: qCalendar, fixed_frequency: qFrequency, fixed_convention: qBusinessDayConvention, fixed_daycount: qDayCounter, ibor_index: ql.IborIndex, spread: float = 0.0, fwd_start: qPeriod = ql.Period(0, ql.Days), discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), settlement_days: int = 0, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), end_of_month: bool = False, with_indexed_coupons: bool = False, trigger = None)


[qlSwapRateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L554)(rate: qQuoteHandle, index: ql.SwapIndex, spread: float = 0.0, fwd_start: qPeriod = ql.Period(0, ql.Days), discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), end_of_month: bool = False, with_indexed_coupons: bool = False, trigger = None)


[qlSwapRateForDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L602)(rate: qQuoteHandle, start_date: qDate, end_date: qDate, calendar: qCalendar, fixed_frequencies: qFrequency, business_day_convention: qBusinessDayConvention, day_counter: qDayCounter, index: ql.IborIndex, spread: float = 0.0, discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), pillar: ql.Pillar = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), end_of_month: bool = False, with_indexed_coupons: bool = False, trigger = None)


[qlSwapRateHelperSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L644)(swap_rate_helper: ql.SwapRateHelper, trigger = None)


[qlSwapRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L655)(swap_rate_helper: ql.SwapRateHelper, trigger = None)


[qlOISRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L767)(settlement_days: int, tenor: qPeriod, fixed_rate: qQuoteHandle, overnight_index: ql.OvernightIndex, discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), telescopic_value_dates: bool = False, payment_lag: int = 0, payment_convention: qBusinessDayConvention = ql.Following, payment_frequency: qFrequency = ql.Annual, payment_calendar: qCalendar = ql.NullCalendar(), forward_start: qPeriod = ql.Period(0, ql.Days), overnight_spread: float = 0.0, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), averaging_method: qRateAveragingType = ql.RateAveraging.Compound, end_of_month: bool = None, fixed_payment_frequency: qFrequency = ql.NoFrequency, fixed_calendar: qCalendar = ql.NullCalendar(), look_back_days: int = 0, lock_out_days: int = 0, apply_observation_shift: bool = False, pricer: ql.FloatingRateCouponPricer = None, rule: qDateGenerationRule = ql.DateGeneration.Backward, overnight_calendar: qCalendar = ql.NullCalendar(), convention: qBusinessDayConvention = ql.ModifiedFollowing, trigger = None)


[qlOISRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L919)(ois_rate_helper: ql.OISRateHelper, trigger = None)


[qlFxSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L942)(fwd_point: qQuoteHandle, spot_fx: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, is_fx_base_currency_collateral_currency: bool, collateral_curve: ql.YieldTermStructureHandle, trading_calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlFxSwapRateHelperForDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L982)(fwd_point: qQuoteHandle, spot_fx: qQuoteHandle, start_date: qDate, end_date: qDate, is_fx_base_currency_collateral_currency: bool, collateral_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlFxSwapRateHelperSpot](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1008)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1021)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1034)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1047)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1061)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1074)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperIsFxBaseCurrencyCollateralCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1087)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperTradingCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1100)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperAdjustmentCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1113)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlOvernightIndexFutureRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1131)(price: qQuoteHandle, value_date: qDate, maturity_date: qDate, index: ql.OvernightIndex, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlOvernightIndexFutureRateHelperConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1152)(overnight_index_future_rate_helper: ql.OvernightIndexFutureRateHelper, trigger = None)


[qlSofrFutureRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1171)(price: qQuoteHandle, reference_month: int, reference_year: int, frequency: qFrequency, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), trigger = None)


[qlConstNotionalCrossCurrencySwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1206)(fixed_rate: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, fixed_frequency: qFrequency, fixed_day_count: qDayCounter, float_index: ql.IborIndex, collateral_curve: ql.YieldTermStructureHandle, collateral_on_fixed_leg: bool, payment_lag: int = 0, trigger = None)


[qlConstNotionalCrossCurrencyBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1256)(basis: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_currency_index: ql.IborIndex, quote_currency_index: ql.IborIndex, collateral_curve: ql.YieldTermStructureHandle, is_fx_base_currency_collateral_currency: bool, is_basis_on_fx_base_currency_leg: bool, payment_frequency: qFrequency = ql.NoFrequency, payment_lag: int = 0, trigger = None)


[qlMtMCrossCurrencyBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1309)(basis: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_currency_index: ql.IborIndex, quote_currency_index: ql.IborIndex, collateral_curve: ql.YieldTermStructureHandle, is_fx_base_currency_collateral_currency: bool, is_basis_on_fx_base_currency_leg: bool, is_fx_base_currency_leg_resettable: bool, payment_frequency: qFrequency = ql.NoFrequency, payment_lag: int = 0, trigger = None)


[qlIborIborBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1360)(basis: qQuoteHandle, tenor: qPeriod, settlement_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_index: ql.IborIndex, other_index: ql.IborIndex, discount_handle: ql.YieldTermStructureHandle, bootstrap_base_curve: bool, trigger = None)


[qlIborIborBasisSwapRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1394)(ibor_ibor_basis_swap_rate_helper: ql.IborIborBasisSwapRateHelper, trigger = None)


[qlOvernightIborBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1415)(basis: qQuoteHandle, tenor: qPeriod, settlement_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_index: ql.IborIndex, other_index: ql.IborIndex, discount_handle: ql.YieldTermStructureHandle, trigger = None)


[qlOvernightIborBasisSwapRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1447)(overnight_ibor_basis_swap_rate_helper: ql.OvernightIborBasisSwapRateHelper, trigger = None)


## Rounding


[qRoundingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/rounding.py#L28)(method: str)


[qlRounding](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/rounding.py#L41)(method: qRoundingMethod, precision: int, digit: int = 5, trigger = None)


[qlRoundingApply](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/rounding.py#L55)(rounding: ql.Rounding, value: float, trigger = None)


## Scheduler


[qDateGenerationRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L33)(rule: str)


[qlSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L53)(effective_date: qDate, termination_date: qDate, tenor: qPeriod, calendar: qCalendar, convention: qBusinessDayConvention, termination_date_convention: qBusinessDayConvention, date_generation_rule: qDateGenerationRule, end_of_month: bool, first_date: qDate = ql.Date(), last_date: qDate = ql.Date(), trigger = None)


[qlScheduleFromDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L89)(dates: xlo.Array(dims=1), calendar: qCalendar = ql.NullCalendar(), convention: qBusinessDayConvention = ql.Unadjusted, trigger = None)


[qlScheduleDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L111)(schedule: ql.Schedule, trigger = None)


[qlSchedulePreviousDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L123)(schedule: ql.Schedule, ref_date: qDate, trigger = None)


[qlScheduleNextDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L137)(schedule: ql.Schedule, ref_date: qDate, trigger = None)


[qlScheduleHasIsRegular](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L148)(schedule: ql.Schedule, trigger = None)


[qlScheduleIsRegular](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L160)(schedule: ql.Schedule, i: int, trigger = None)


[qlScheduleIsRegular2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L171)(schedule: ql.Schedule, trigger = None)


[qlScheduleCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L182)(schedule: ql.Schedule, trigger = None)


[qlScheduleStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L193)(schedule: ql.Schedule, trigger = None)


[qlScheduleEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L204)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L215)(schedule: ql.Schedule, trigger = None)


[qlScheduleTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L226)(schedule: ql.Schedule, trigger = None)


[qlScheduleBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L237)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasTerminationDateBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L250)(schedule: ql.Schedule, trigger = None)


[qlScheduleTerminationDateBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L263)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L280)(schedule: ql.Schedule, trigger = None)


[qlScheduleRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L291)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L302)(schedule: ql.Schedule, trigger = None)


[qlScheduleEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L313)(schedule: ql.Schedule, trigger = None)


[qlScheduleAfter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L325)(schedule: ql.Schedule, truncation_date: qDate, trigger = None)


[qlScheduleUntil](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L339)(schedule: ql.Schedule, truncation_date: qDate, trigger = None)


[qlMakeSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L364)(effective_date = None, termination_date = None, tenor = None, frequency = None, calendar = None, convention = None, terminal_date_convention = None, rule = None, forwards = False, backwards = False, end_of_month = None, first_date = None, next_to_last_date = None, trigger = None)


## Settings


[qlSettingsGetEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L12)(trigger = None)


[qlSettingsSetEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L23)(date: qDate, trigger = None)


[qlSettingsGetEnforcesTodaysHistoricFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L32)(trigger = None)


[qlSettingsSetEnforcesTodaysHistoricFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L43)(enforces: bool, trigger = None)


[qlSettingsGetIncludeReferenceDateEvents](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L52)(trigger = None)


[qlSettingsSetIncludeReferenceDateEvents](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L63)(include: bool, trigger = None)


[qlSettingsGetIncludeTodaysCashFlows](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L72)(trigger = None)


[qlSettingsSetIncludeTodaysCashFlows](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L83)(include: bool, trigger = None)


[qlSettingsAnchorEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L92)(trigger = None)


[qlSettingsResetEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L101)(trigger = None)


## Stochasticprocess


[qGJRGARCHProcessDiscretization](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L57)(discretization: str)


[qHestonProcessDiscretization](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L62)(discretization: str)


[qlStochasticProcessSize](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L73)(process: ql.StochasticProcess, trigger = None)


[qlStochasticProcessFactors](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L84)(process: ql.StochasticProcess, trigger = None)


[qlStochasticProcessInitialValues](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L95)(process: ql.StochasticProcess, trigger = None)


[qlStochasticProcessDrift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L110)(process: ql.StochasticProcess, t: float, x: xlo.Array(dims=1), trigger = None)


[qlStochasticProcessDiffusion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L125)(process: ql.StochasticProcess, t: float, x: xlo.Array(dims=1), trigger = None)


[qlStochasticProcessExpectation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L141)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger = None)


[qlStochasticProcessStdDeviation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L161)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger = None)


[qlStochasticProcessCovariance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L181)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger = None)


[qlStochasticProcessEvolve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L202)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, dw: xlo.Array(dims=1), trigger = None)


[qlStochasticProcess1DX0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L222)(process: ql.StochasticProcess1D, trigger = None)


[qlStochasticProcess1DDrift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L235)(process: ql.StochasticProcess1D, t: float, x: float, trigger = None)


[qlStochasticProcess1DDiffusion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L250)(process: ql.StochasticProcess1D, t: float, x: float, trigger = None)


[qlStochasticProcess1DExpectation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L266)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger = None)


[qlStochasticProcess1DStdDeviation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L282)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger = None)


[qlStochasticProcess1DVariance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L298)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger = None)


[qlStochasticProcess1DEvolve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L315)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, dw: float, trigger = None)


[qlStochasticProcess1DApply](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L335)(process: ql.StochasticProcess1D, x0: float, dx: float, trigger = None)


[qlGeneralizedBlackScholesProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L352)(s0: qQuoteHandle, dividend_ts: ql.YieldTermStructureHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, local_vol_ts: ql.LocalVolTermStructureHandle = None, trigger = None)


[qlGeneralizedBlackScholesProcessStateVariable](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L374)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessDividendYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L387)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessRiskFreeRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L400)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessBlackVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L413)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessLocalVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L426)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlBlackScholesProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L441)(s0: qQuoteHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlBlackScholesMertonProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L460)(s0: qQuoteHandle, dividend_ts: ql.YieldTermStructureHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlBlackProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L479)(s0: qQuoteHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlGarmanKohlagenProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L498)(s0: qQuoteHandle, foreign_risk_free_ts: ql.YieldTermStructureHandle, domestic_risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlMerton76Process](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L523)(state_variable: qQuoteHandle, dividend_ts: ql.YieldTermStructureHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, jump_intensity: qQuoteHandle, mean_log_jump: qQuoteHandle, jump_volatility: qQuoteHandle, trigger = None)


[qlStochasticProcessArray](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L552)(array: xlo.Array(dims=1), correlation: xlo.Array(dims=2), trigger = None)


[qlGeometricBrownianMotionProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L571)(initial_value: float, mu: float, sigma: float, trigger = None)


[qlVarianceGammaProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L592)(s0: qQuoteHandle, dividend_yield: ql.YieldTermStructureHandle, risk_free_rate: ql.YieldTermStructureHandle, sigma: float, nu: float, theta: float, trigger = None)


[qlHestonProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L619)(risk_free_ts: ql.YieldTermStructureHandle, dividend_ts: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, kappa: float, theta: float, sigma: float, rho: float, discretization: qHestonProcessDiscretization = ql.HestonProcess.QuadraticExponentialMartingale, trigger = None)


[qlHestonProcessS0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L643)(process: ql.HestonProcess, trigger = None)


[qlHestonProcessDividendYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L654)(process: ql.HestonProcess, trigger = None)


[qlHestonProcessRiskFreeRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L667)(process: ql.HestonProcess, trigger = None)


[qlBatesProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L690)(risk_free_rate: ql.YieldTermStructureHandle, dividend_yield: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, kappa: float, theta: float, sigma: float, rho: float, lambda_parameter: float, nu: float, delta: float, trigger = None)


[qlHullWhiteProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L728)(risk_free_ts: ql.YieldTermStructureHandle, a: float, sigma: float, trigger = None)


[qlHullWhiteForwardProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L746)(risk_free_ts: ql.YieldTermStructureHandle, a: float, sigma: float, trigger = None)


[qlHullWhiteForwardProcessAlpha](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L763)(process: ql.HullWhiteForwardProcess, t: float, trigger = None)


[qlHullWhiteForwardProcessMT](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L779)(process: ql.HullWhiteForwardProcess, s: float, t: float, t_measure: float, trigger = None)


[qlHullWhiteForwardProcessB](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L798)(process: ql.HullWhiteForwardProcess, s: float, t: float, trigger = None)


[qlHullWhiteForwardProcessSetForwardMeasureTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L812)(process: ql.HullWhiteForwardProcess, t: float, trigger = None)


[qlG2Process](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L830)(a: float, sigma: float, b: float, eta: float, rho: float, trigger = None)


[qlG2ForwardProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L852)(a: float, sigma: float, b: float, eta: float, rho: float, trigger = None)


[qlG2ForwardProcessSetForwardMeasureTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L871)(process: ql.G2ForwardProcess, t: float, trigger = None)


[qlGsrProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L888)(times: xlo.Array(dims=1), vols: xlo.Array(dims=1), reversions: xlo.Array(dims=1), t: float = 60.0, trigger = None)


[qlGsrProcessSigma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L909)(process: ql.GsrProcess, t: float, trigger = None)


[qlGsrProcessReversion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L922)(process: ql.GsrProcess, t: float, trigger = None)


[qlGsrProcessY](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L935)(process: ql.GsrProcess, t: float, trigger = None)


[qlGsrProcessG](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L950)(process: ql.GsrProcess, t: float, T: float, x: float, trigger = None)


[qlGsrProcessSetForwardMeasureTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L965)(process: ql.GsrProcess, t: float, trigger = None)


[qlOrnsteinUhlenbeckProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L983)(speed: float, vol: float, x0: float = 0.0, level: float = 0.0, trigger = None)


[qlOrnsteinUhlenbeckProcessSpeed](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1000)(process: ql.OrnsteinUhlenbeckProcess, trigger = None)


[qlOrnsteinUhlenbeckProcessVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1013)(process: ql.OrnsteinUhlenbeckProcess, trigger = None)


[qlOrnsteinUhlenbeckProcessLevel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1026)(process: ql.OrnsteinUhlenbeckProcess, trigger = None)


[qlExtendedOrnsteinUhlenbeckProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1043)(speed: float, sigma: float, x0: float, function, int_eps: float = 1.0e-4, trigger = None)


[qlExtendedOrnsteinUhlenbeckProcessConstantFunction](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1061)(x: float)


[qlExtOUWithJumpsProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1077)(process: ql.ExtendedOrnsteinUhlenbeckProcess, Y0: float, beta: float, jump_intensity: float, eta: float, trigger = None)


[qlKlugeExtOUProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1097)(rho: float, kluge: ql.ExtOUWithJumpsProcess, ext_ou: ql.ExtendedOrnsteinUhlenbeckProcess, trigger = None)


[qlGJRGARCHProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1123)(risk_free_rate: ql.YieldTermStructureHandle, dividend_yield: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, omega: float, alpha: float, beta: float, gamma: float, lambda_parameter: float, days_per_year: float = 252.0, discretization: qGJRGARCHProcessDiscretization = ql.GJRGARCHProcess.FullTruncation, trigger = None)


[qlGJRGARCHProcessS0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1159)(process: ql.GJRGARCHProcess, trigger = None)


[qlGJRGARCHProcessDividendYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1170)(process: ql.GJRGARCHProcess, trigger = None)


[qlGJRGARCHProcessRiskFreeRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1183)(process: ql.GJRGARCHProcess, trigger = None)


## Termstructures


[qCompounding](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L29)(compounding: str)


[qlTermStructureDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L40)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureTimeFromReference](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L54)(ytsh: ql.YieldTermStructureHandle, date: qDate, trigger = None)


[qlTermStructureCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L67)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureReferenceDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L80)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureMaxDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L93)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureMaxTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L104)(ytsh: ql.YieldTermStructureHandle)


[qlTermStructureEnableExrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L115)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureDisableExrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L127)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureAllowsExtrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L139)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlYieldTermStructureDiscount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L157)(ytsh: ql.YieldTermStructureHandle, date: qDate, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureDiscountFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L175)(ytsh: ql.YieldTermStructureHandle, time: float, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureZeroRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L196)(ytsh: ql.YieldTermStructureHandle, date: qDate, daycounter: qDayCounter, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureZeroRateFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L219)(ytsh: ql.YieldTermStructureHandle, time: float, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureForwardRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L243)(ytsh: ql.YieldTermStructureHandle, date1: qDate, date2: qDate, daycounter: qDayCounter, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureForwardRateFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L270)(ytsh: ql.YieldTermStructureHandle, time1: float, time2: float, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlFlatForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L297)(reference_date: qDate, forward_rate: float, daycounter: qDayCounter = ql.Actual365Fixed(), compounding: qCompounding = ql.Continuous, frequency: qFrequency = ql.NoFrequency, calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlImpliedTermStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L323)(ytsh: ql.YieldTermStructureHandle, reference_date: qDate, trigger = None)


[qlZeroSpreadedTermStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L346)(base: ql.YieldTermStructureHandle, spread: float, compounding: qCompounding = ql.Compounded, frequency: qFrequency = ql.NoFrequency, daycounter: qDayCounter = ql.Actual365Fixed(), trigger = None)


[qlForwardSpreadedTermStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L369)(base: ql.YieldTermStructureHandle, spread: float, trigger = None)


[qlCompositeZeroYieldStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L391)(curve1: ql.YieldTermStructureHandle, curve2: ql.YieldTermStructureHandle, operator: str, trigger = None)


## Volatilities


[qVolatilityType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L24)(s: str)


[qlBlackVolTermStructureMinStrike](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L36)(vol_tsh: ql.BlackVolTermStructureHandle, trigger = None)


[qlBlackVolTermStructureMaxStrike](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L48)(vol_tsh: ql.BlackVolTermStructureHandle, trigger = None)


[qlBlackVolTermStructureBlackVol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L65)(vol_tsh: ql.BlackVolTermStructureHandle, expiry_date: qDate, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackVolFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L86)(vol_tsh: ql.BlackVolTermStructureHandle, expiry_time: float, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackVariance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L107)(vol_tsh: ql.BlackVolTermStructureHandle, expiry_date: qDate, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackVarianceFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L128)(vol_tsh: ql.BlackVolTermStructureHandle, expiry_time: float, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackForwardVol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L150)(vol_tsh: ql.BlackVolTermStructureHandle, date_start: qDate, date_end: qDate, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackForwardVolFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L173)(vol_tsh: ql.BlackVolTermStructureHandle, time_start: float, time_end: float, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackForwardVariance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L196)(vol_tsh: ql.BlackVolTermStructureHandle, date_start: qDate, date_end: qDate, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackVolTermStructureBlackForwardVarianceFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L219)(vol_tsh: ql.BlackVolTermStructureHandle, time_start: float, time_end: float, strike: float, extrapolate: bool = False, trigger = None)


[qlBlackConstantVol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L241)(reference_date: qDate, calendar: qCalendar, volatility: float, day_counter: qDayCounter, trigger = None)


[qlLocalVolTermStructureLocalVol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L266)(vol_tsh: ql.LocalVolTermStructureHandle, expiry_date: qDate, strike: float, extrapolate: bool = False, trigger = None)


[qlLocalVolTermStructureLocalVolFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/volatilities.py#L287)(vol_tsh: ql.LocalVolTermStructureHandle, expiry_time: float, strike: float, extrapolate: bool = False, trigger = None)


