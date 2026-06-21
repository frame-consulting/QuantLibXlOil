# API Reference

This section lists the QuantLib functions made available to Excel.


## Blackformula


[qlBlackFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L21)(option_type: qOptionType, strike: float, forward: float, std_dev: float, discount: float = 1.0, displacement: float = 0.0, trigger = None)


[qlBlackFormulaImpliedStdDev](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L50)(option_type: qOptionType, strike: float, forward: float, price: float, discount: float = 1.0, displacement: float = 0.0, guess: float = ql.nullDouble(), accuracy: float = 1e-6, max_iterations: int = 100, trigger = None)


[qlBlackFormulaImpliedStdDevLiRS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L91)(option_type: qOptionType, strike: float, forward: float, price: float, discount: float = 1.0, displacement: float = 0.0, guess: float = ql.nullDouble(), omega: float = 1.0, accuracy: float = 1e-6, max_iterations: int = 100, trigger = None)


[qlBachelierBlackFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L129)(option_type: qOptionType, strike: float, forward: float, std_dev: float, discount: float = 1.0, trigger = None)


[qlBachelierBlackFormulaImpliedVol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L152)(option_type: qOptionType, strike: float, forward: float, time_to_expiry: float, price: float, discount: float = 1.0, trigger = None)


[qlBachelierBlackFormulaImpliedVolChoi](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L178)(option_type: qOptionType, strike: float, forward: float, time_to_expiry: float, price: float, discount: float = 1.0, trigger = None)


[qlBlackDeltaCalculator](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L204)(option_type: qOptionType, delta_type: qDeltaVolQuoteDeltaType, spot: float, domestic_discount: float, foreign_discount: float, std_dev: float, trigger = None)


[qlBlackDeltaCalculatorDeltaFromStrike](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L226)(calculator: ql.BlackDeltaCalculator, strike: float, trigger = None)


[qlBlackDeltaCalculatorStrikeFromDelta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L242)(calculator: ql.BlackDeltaCalculator, delta: float, trigger = None)


[qlBlackDeltaCalculatorAtmStrike](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/blackformula.py#L258)(calculator: ql.BlackDeltaCalculator, atm_type: qDeltaVolQuoteAtmType, trigger = None)


## Bonds


[qBondPriceType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L32)(bond_price_type: str)


[qCallabilityType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L37)(callability_type: str)


[qlBondPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L49)(amount: float, price_type: qBondPriceType)


[qlCallability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L62)(price: ql.BondPrice, callability_type: qCallabilityType, date: qDate, trigger = None)


[qlSoftCallability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L78)(price: ql.BondPrice, callability_type: qCallabilityType, date: qDate, trigger = None)


[qlBondPriceAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L91)(bond_price: ql.BondPrice, trigger = None)


[qlBondPriceType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L102)(bond_price: ql.BondPrice, trigger = None)


[qlBondPriceIsValid](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L116)(bond_price: ql.BondPrice, trigger = None)


[qlCallabilityPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L127)(callability: ql.Callability, trigger = None)


[qlCallabilityType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L138)(callability: ql.Callability, trigger = None)


[qlCallabilityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L152)(callability: ql.Callability, trigger = None)


[qlBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L168)(settlement_days: int, calendar: qCalendar, face_amount: float, maturity_date: qDate, cashflows: ql.Leg, issue_date: qDate = ql.Date(), trigger = None)


[qlBond2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L197)(settlement_days: int, calendar: qCalendar, issue_date: qDate = ql.Date(), coupons = ql.Leg(), trigger = None)


[qlBondNextCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L215)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondPreviousCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L227)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondNextCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L241)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondPreviousCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L255)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondSettlementDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L268)(bond: ql.Bond, trigger = None)


[qlBondSettlementDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L280)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondIsTradable](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L294)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L305)(bond: ql.Bond, trigger = None)


[qlBondMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L316)(bond: ql.Bond, trigger = None)


[qlBondIssueDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L327)(bond: ql.Bond, trigger = None)


[qlBondCashFlows](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L338)(bond: ql.Bond, trigger = None)


[qlBondRedemption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L349)(bond: ql.Bond, trigger = None)


[qlBondRedemptions](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L360)(bond: ql.Bond, trigger = None)


[qlBondCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L371)(bond: ql.Bond, trigger = None)


[qlBondNotionals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L383)(bond: ql.Bond, trigger = None)


[qlBondNotional](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L395)(bond: ql.Bond, date: qDate = ql.Date(), trigger = None)


[qlBondCleanPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L406)(bond: ql.Bond, trigger = None)


[qlBondCleanPrice2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L422)(bond: ql.Bond, yield_: float, dc: qDayCounter, compounding: qCompounding, frequency: qFrequency = ql.Annual, settlement: qDate = ql.Date(), trigger = None)


[qlBondDirtyPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L441)(bond: ql.Bond, trigger = None)


[qlBondDirtyPrice2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L457)(bond: ql.Bond, yield_: float, dc: qDayCounter, compounding: qCompounding, frequency: qFrequency, settlement: qDate = ql.Date(), trigger = None)


[qlBondYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L481)(bond: ql.Bond, dc: qDayCounter, compounding: qCompounding, freq: qFrequency, accuracy: float = 1.0e-8, max_evaluations: int = 100, trigger = None)


[qlBondYield2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L508)(bond: ql.Bond, price: ql.BondPrice, dc: qDayCounter, compounding: qCompounding, freq: qFrequency, settlement: qDate = ql.Date(), accuracy: float = 1.0e-8, max_evaluations: int = 100, guess: float = 0.05, trigger = None)


[qlBondAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L533)(bond: ql.Bond, settlement: qDate = ql.Date(), trigger = None)


[qlBondSettlementValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L546)(bond: ql.Bond, trigger = None)


[qlBondSettlementValue2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L558)(bond: ql.Bond, clean_price: float, trigger = None)


[qlBondCleanPriceFromZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L576)(bond: ql.Bond, discount_curve: ql.YieldTermStructureHandle, z_spread: float = 0.002, dc: qDayCounter = ql.Actual365Fixed(), compounding: qCompounding = ql.Compounded, freq: qFrequency = ql.Annual, settlement_date: qDate = ql.Date(), trigger = None)


[qlBondsinkingSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L603)(bond: ql.Bond, start_date: qDate, bond_length: qPeriod, frequency: qFrequency, payment_calendar: qCalendar, trigger = None)


[qlBondSinkingNotionals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L626)(bond: ql.Bond, bond_length: qPeriod, frequency: qFrequency, coupon_rate: float, initial_notional: float, trigger = None)


[qlZeroCouponBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L649)(settlement_days: int, calendar: qCalendar, face_amount: float, maturity_date: qDate, business_day_convention: qBusinessDayConvention = ql.Following, redemption: float = 100.0, issue_date: qDate = ql.Date(), trigger = None)


[qlFixedRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L689)(settlement_days: int, face_amount: float, schedule: ql.Schedule, coupons: xlo.Array(dims=1), payment_day_counter: qDayCounter, business_day_convention: qBusinessDayConvention = ql.Following, redemption: float = 100.0, issue_date: qDate = ql.Date(), payment_calendar: qCalendar = ql.NullCalendar(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, trigger = None)


[qlAmortizingFixedRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L740)(settlement_days: int, notionals: xlo.Array(dims=1), schedule: ql.Schedule, coupons: xlo.Array(dims=1), accrual_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, issue_date: qDate = ql.Date(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, redemption = 100, trigger = None)


[qlAmortizingFloatingRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L797)(settlement_days: int, notional: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.IborIndex, accrual_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, fixing_days: int = 0, gearings: xlo.Array(dims=1) = [1.0], spreads: xlo.Array(dims=1) = [0.0], caps = None, floors = None, in_arrears: bool = False, issue_date: qDate = ql.Date(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, redemptions = 100.0, payment_lag: int = 0, trigger = None)


[qlFloatingRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L867)(settlement_days: int, face_amount: float, schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, fixing_days: int = 0, gearings: xlo.Array(dims=1) = [1.0], spreads: xlo.Array(dims=1) = [0.0], caps = None, floors = None, in_arrears: bool = False, redemption: float = 100.0, issue_date: qDate = ql.Date(), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, trigger = None)


[qlCmsRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L931)(settlement_days: int, face_amount: float, schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter, payment_convention: qBusinessDayConvention, fixing_days: int, gearings: xlo.Array(dims=1), spreads: xlo.Array(dims=1), caps: xlo.Array(dims=1), floors: xlo.Array(dims=1), in_arrears: bool = False, redemption: float = 100.0, issue_date: qDate = ql.Date(), trigger = None)


[qlAmortizingCmsRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L986)(settlement_days: int, notionals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, fixing_days: int = 0, gearings: xlo.Array(dims=1) = [0.0], spreads: xlo.Array(dims=1) = [0.0], caps: xlo.Array(dims=1) = None, floors: xlo.Array(dims=1) = None, in_arrears: bool = False, issue_date: qDate = ql.Date(), trigger = None)


[qlBondSetDiscountingEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1027)(bond: ql.Bond, discount_curve: ql.YieldTermStructureHandle, trigger = None)


[qlCallableBondCallability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1039)(callable_bond: ql.CallableBond, Trigger = None)


[qlCallableBondImpliedVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1055)(callable_bond: ql.CallableBond, target_price: ql.BondPrice, discount_curve: ql.YieldTermStructure, accuracy: float, max_evaluations: int, min_vol: float, max_vol: float, trigger = None)


[qlCallableBondOAS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1090)(callable_bond: ql.CallableBond, clean_price: float, engine_ts: ql.YieldTermStructure, dc: qDayCounter, compounding: qCompounding, freq: qFrequency, settlement_date: qDate = ql.Date(), accuracy: float = 1e-10, max_iterations: int = 100, guess: float = 0.0, trigger = None)


[qlCallableBondCleanPriceOAS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1128)(callable_bond: ql.CallableBond, oas: float, engine_ts: ql.YieldTermStructure, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, settlement_date: qDate = ql.Date(), trigger = None)


[qlCallableBondEffectiveDuration](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1160)(callable_bond: ql.CallableBond, oas: float, engine_ts: ql.YieldTermStructure, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, bump: float = 2e-4, trigger = None)


[qlCallableBondEffectiveConvexity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1192)(callable_bond: ql.CallableBond, oas: float, engine_ts: ql.YieldTermStructure, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, bump: float = 2e-4, trigger = None)


[qlCallableFixedRateBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1231)(settlement_days: int, face_amount: float, schedule: ql.Schedule, coupons: xlo.Array(dims=1), accrual_day_counter: qDayCounter, payment_convention: qBusinessDayConvention, redemption: float, issue_date: qDate, put_call_schedule: xlo.Array(dims=1), ex_coupon_period: qPeriod = ql.Period(), ex_coupon_calendar: qCalendar = ql.NullCalendar(), ex_coupon_convention: qBusinessDayConvention = ql.Unadjusted, ex_coupon_end_of_month: bool = False, trigger = None)


[qlCallableZeroCouponBond](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1279)(settlement_days: int, face_amount: float, calendar: qCalendar, maturity_date: qDate, day_counter: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, redemption: float = 100.0, issue_date: qDate = ql.Date(), put_call_schedule: xlo.Array(dims=1) = None, trigger = None)


[qlBlackCallableFixedRateBondEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/bonds.py#L1315)(callable_bond: ql.CallableBond, fwd_yield_vol: qQuoteHandle, discount_curve: ql.YieldTermStructure, trigger = None)


## Calendars


[qCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L113)(calendarname: str)


[qBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L118)(conventionname: str)


[qJointCalendarRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L123)(rule_name: str)


[qlCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L139)(calendar_name: str, trigger = None)


[qlCalendarisWeekend](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L150)(calendar: qCalendar, weekday: qWeekday, trigger = None)


[qlCalendarStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L161)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L172)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsBusinessDay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L183)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L194)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L205)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L216)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarAddHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L227)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarRemoveHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L238)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarResetAddedAndRemovedHolidays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L247)(calendar: qCalendar, trigger = None)


[qlCalendarAdjust](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L260)(calendar: qCalendar, date: qDate, convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCalendarAdvance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L281)(calendar: qCalendar, date: qDate, n: int, unit: qTimeUnit, convention: qBusinessDayConvention = ql.Following, end_of_month: bool = False, trigger = None)


[qlCalendarAdvance2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L304)(calendar: qCalendar, date: qDate, period: qPeriod, convention: qBusinessDayConvention = ql.Following, end_of_month: bool = False, trigger = None)


[qlCalendarBusinessDaysBetween](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L326)(calendar: qCalendar, from_date: qDate, to_date: qDate, include_first: bool = True, include_last: bool = False, trigger = None)


[qlCalendarHolidayList](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L344)(calendar: qCalendar, from_date: qDate, to_date: qDate, trigger = None)


[qlCalendarBusinessDayList](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L357)(calendar: qCalendar, from_date: qDate, to_date: qDate, trigger = None)


[qlCalendarName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L370)(calendar: qCalendar, trigger = None)


[qlCalendarEmpty](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L381)(calendar: qCalendar, trigger = None)


[qlCalendarJointCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L394)(calendar1: qCalendar, calendar2: qCalendar, rule: qJointCalendarRule = ql.JoinHolidays)


[qlCalendarJointCalendar2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L412)(calendar1: qCalendar, calendar2: qCalendar, calendar3: qCalendar, rule: qJointCalendarRule = ql.JoinHolidays, trigger = None)


## Calibratedmodel


[qlCalibratedModelCalibrate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L24)(model: ql.CalibratedModel, calibration_helpers: xlo.Array(dims=1), optimization_method: ql.OptimizationMethod, end_criteria: ql.EndCriteria, constraint: ql.Constraint = ql.NoConstraint(), weights: xlo.Array(dims=1) = [], fix_parameters: xlo.Array(dims=1) = [], trigger = None)


[qlCalibratedModelParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L53)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelSetParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L68)(model: ql.CalibratedModel, params: xlo.Array(dims=1), trigger = None)


[qlCalibratedModelValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L87)(model: ql.CalibratedModel, params: xlo.Array(dims=1), calibration_helpers: xlo.Array(dims=1), trigger = None)


[qlCalibratedModelConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L103)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelEndCriteria](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L115)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelProblemValues](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L127)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelProblemValuesFunctionEvaluation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L139)(model: ql.CalibratedModel, trigger = None)


[qlCalibratedModelHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calibratedmodel.py#L151)(model: ql.CalibratedModel, trigger = None)


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


[qDurationType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L43)(duration_type: str)


[qRateAveragingType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L48)(averaging_type: str)


[qlSimpleCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L60)(amount: float, date: qDate, trigger = None)


[qlRedemption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L72)(amount: float, date: qDate, trigger = None)


[qlAmortizingPayment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L84)(amount: float, date: qDate, trigger = None)


[qlIndexedCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L102)(notional: float, index: ql.Index, base_date: qDate, fixing_date: qDate, payment_date: qDate, growth_only: bool = False, trigger = None)


[qlCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L123)(cashflow: ql.CashFlow, trigger = None)


[qlCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L134)(cashflow: ql.CashFlow, trigger = None)


[qlCashFlowHasOccurred](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L146)(cashflow: ql.CashFlow, ref_date: qDate = ql.Date(), trigger = None)


[qlAsIndexedCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L159)(cashflow: ql.CashFlow, trigger = None)


[qlAsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L170)(cashflow: ql.CashFlow, trigger = None)


[qlCouponNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L181)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L192)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L203)(coupon: ql.Coupon, trigger = None)


[qlCouponReferencePeriodStart](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L214)(coupon: ql.Coupon, trigger = None)


[qlCouponReferencePeriodEnd](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L225)(coupon: ql.Coupon, trigger = None)


[qlCouponExCouponDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L236)(coupon: ql.Coupon, trigger = None)


[qlCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L247)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L258)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L269)(coupon: ql.Coupon, trigger = None)


[qlCouponDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L280)(coupon: ql.Coupon, trigger = None)


[qlCouponAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L292)(coupon: ql.Coupon, date: qDate, trigger = None)


[qlAsFixedRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L303)(cashflow: ql.CashFlow, trigger = None)


[qlAsFloatingRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L314)(cashflow: ql.CashFlow, trigger = None)


[qlFloatingRateCouponFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L327)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L340)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponIsInArrears](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L351)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponGearing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L364)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L375)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L386)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponAdjustedFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L399)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L412)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L426)(coupon: ql.FloatingRateCoupon, discount_curve: ql.YieldTermStructureHandle, trigger = None)


[qlFloatingRateCouponIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L441)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponSetPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L455)(coupon: ql.FloatingRateCoupon, pricer: ql.FloatingRateCouponPricer, trigger = None)


[qlCappedFlooredCouponIsCapped](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L471)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponIsFloored](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L482)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponCap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L495)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L506)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponEffectiveCap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L517)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponEffectiveFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L530)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlOvernightIndexedCouponAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L543)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponCanApplyTelescopicFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L556)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponApplyObservationShift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L569)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponCompoundSpreadDaily](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L582)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponLockoutDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L595)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponRateComputationStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L608)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponRateComputationEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L621)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponValueDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L634)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponFixingDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L647)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponInterestDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L660)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponDt](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L673)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponIndexFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L686)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponEffectiveIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L699)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponEffectiveSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L712)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponUnderlying](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L725)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponNakedOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L739)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponDailyCapFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L753)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L767)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L781)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L795)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L809)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlAsOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L823)(cashflow: ql.CashFlow, trigger = None)


[qlAsCappedFlooredOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L836)(cashflow: ql.CashFlow, trigger = None)


[qlAsMultipleResetsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L849)(cashflow: ql.CashFlow, trigger = None)


[qlFixedRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L870)(payment_date: qDate, nominal: float, rate: float, day_counter: qDayCounter, start_date: qDate, end_date: qDate, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlIborCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L914)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlCappedFlooredIborCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L970)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, spread: float = 0.0, cap: float = ql.nullDouble(), floor: float = ql.nullDouble(), ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1029)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, overnight_index: ql.OvernightIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, lookback_days: int = ql.nullInt(), lockout_days: int = 0, apply_observation_shift: bool = False, compound_spread: bool = False, trigger = None)


[qlCappedFlooredOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1079)(underlying: ql.OvernightIndexedCoupon, cap: float = ql.nullDouble(), floor: float = ql.nullDouble(), naked_option: bool = False, daily_cap_floor: bool = False, trigger = None)


[qlCmsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1111)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.SwapIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlCmsSpreadCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1163)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.SwapSpreadIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlRangeAccrualFloatersCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1216)(payment_date: qDate, nominal: float, index: ql.IborIndex, start_date: qDate, end_date: qDate, fixing_days: int, day_counter: qDayCounter, gearing: float, spread: float, ref_period_start: qDate, ref_period_end: qDate, observations_schedule: ql.Schedule, lower_trigger: float, upper_trigger: float, trigger = None)


[qlMultipleResetsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1269)(payment_date: qDate, nominal: float, reset_schedule: ql.Schedule, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, coupon_spread: float = 0.0, rate_spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlBlackIborCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1309)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), trigger = None)


[qlCompoundingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1320)(trigger = None)


[qlArithmeticAveragedOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1335)(mean_reversion: float = 0.03, volatility: float = 0.0, by_approx: bool = False, trigger = None)


[qlBlackCompoundingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1354)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), effective_volatility_input: bool = False, trigger = None)


[qlBlackAveragingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1372)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), effective_volatility_input: bool = False, trigger = None)


[qlCompoundingMultipleResetsPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1386)(trigger = None)


[qlAveragingMultipleResetsPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1396)(trigger = None)


[qlSetCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1408)(leg: xlo.Array(dims=1), pricer: ql.FloatingRateCouponPricer, trigger = None)


[qlFixedRateLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1426)(schedule: ql.Schedule, day_counter: qDayCounter, nominals: xlo.Array(dims=1), coupon_rates: xlo.Array(dims=1), payment_adjustment: qBusinessDayConvention = ql.Following, trigger = None)


[qlIborLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1460)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, fixing_days = (), gearings: xlo.Array(dims=1) = None, spreads: xlo.Array(dims=1) = None, caps: xlo.Array(dims=1) = None, floors: xlo.Array(dims=1) = None, is_in_arrears: bool = False, trigger = None)


[qlOvernightLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1504)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.OvernightIndex, payment_day_counter: qDayCounter = ql.Actual360(), payment_convention: qBusinessDayConvention = ql.Following, gearings: xlo.Array(dims=1) = None, spreads: xlo.Array(dims=1) = None, telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlCmsLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1540)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCmsZeroLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1568)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCmsSpreadLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1596)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.SwapSpreadIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlMultipleResetsLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1623)(full_reset_schedule: ql.Schedule, index: ql.IborIndex, resets_per_coupon: int, nominals: xlo.Array(dims=1), trigger = None)


[qlRangeAccrualLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1646)(nominals: xlo.Array(dims=1), schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter = ql.Actual360(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCashFlowsStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1670)(leg: xlo.Array(dims=1), trigger = None)


[qlCashFlowsMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1681)(leg: xlo.Array(dims=1), trigger = None)


[qlCashFlowsPreviousCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1694)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1714)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsPreviousCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1734)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1754)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsPreviousCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1774)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1794)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccrualPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1814)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccrualDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1834)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1854)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1874)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1894)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpv](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1916)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1944)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1975)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2013)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, z_spread: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2049)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBpsFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2077)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBpsFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2108)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvBps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2142)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAtmRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2172)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), npv: float = ql.nullDouble(), trigger = None)


[qlCashFlowsYieldRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2205)(leg: xlo.Array(dims=1), npv: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), accuracy: float = 1.0e-10, max_iterations: int = 10000, guess: float = 0.05, trigger = None)


[qlCashFlowsDurationFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2245)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, duration_type: qDurationType, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsDurationFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2275)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, duration_type: qDurationType, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsConvexityFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2312)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsConvexityFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2346)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBasisPointValueFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2375)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBasisPointValueFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2409)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2439)(leg: xlo.Array(dims=1), npv: float, discount_curve: ql.YieldTermStructure, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), accuracy: float = 1.0e-10, max_iterations: int = 100, guess: float = 0.0, trigger = None)


[qlDurationTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2477)(duration_type: qDurationType, trigger = None)


[qlRateAveragingTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2488)(averaging_type: qRateAveragingType, trigger = None)


## Credit


[qProtectionSide](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/credit.py#L21)(s: str)


## Creditdefaultswap


[qCreditDefaultSwapPricingModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L44)(s: str)


[qIsdaCdsEngineNumericalFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L53)(s: str)


[qIsdaCdsEngineAccrualBias](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L62)(s: str)


[qIsdaCdsEngineForwardsInCouponPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L71)(s: str)


[qlClaimAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L89)(claim: ql.Claim, default_date: qDate, notional: float, recovery_rate: float, trigger = None)


[qlFaceValueClaim](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L103)(trigger = None)


[qlFaceValueAccrualClaim](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L116)(bond: ql.Bond, trigger = None)


[qlCreditDefaultSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L142)(protection_side: qProtectionSide, notional: float, spread: float, schedule: ql.Schedule, payment_convention: qBusinessDayConvention, day_counter: qDayCounter, settles_accrual: bool = True, pays_at_default: bool = True, protection_start_date: qDate = ql.Date(), claim: ql.Claim = None, last_period_day_counter: str = None, rebates_accrual: bool = True, trade_date: qDate = ql.Date(), trigger = None)


[qlCreditDefaultSwapWithUpfront](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L202)(protection_side: qProtectionSide, notional: float, upfront: float, spread: float, schedule: ql.Schedule, payment_convention: qBusinessDayConvention, day_counter: qDayCounter, settles_accrual: bool = True, pays_at_default: bool = True, protection_start_date: qDate = ql.Date(), upfront_date: qDate = ql.Date(), claim: ql.Claim = None, last_period_day_counter: str = None, rebates_accrual: bool = True, trade_date: qDate = ql.Date(), cash_settlement_days: int = 3, trigger = None)


[qlCreditdefaultswapSide](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L253)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapNotional](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L264)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapRunningSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L275)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapUpfront](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L286)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditdefaultSwapSettlesAccrual](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L297)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditdefaultswapPaysAtDefaultTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L308)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapCoupons](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L321)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapProtectionStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L334)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapProtectionEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L347)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapRebatesAccrual](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L360)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultswapUpfrontPayment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L371)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapAccrualRebate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L384)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapTradeDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L397)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapCashSettlementDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L408)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapFairUpfront](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L421)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapFairSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L432)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapCouponLegBPS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L443)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapUpfrontBPS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L454)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapCouponLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L465)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapDefaultLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L476)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapUpfrontNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L487)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapAccrualRebateNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L498)(cds: ql.CreditDefaultSwap, trigger = None)


[qlCreditDefaultSwapImpliedHazardRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L517)(cds: ql.CreditDefaultSwap, target_npv: float, discount_curve: ql.YieldTermStructureHandle, day_counter: qDayCounter, recovery_rate: float = 0.40, accuracy: float = 1e-6, model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.Midpoint, trigger = None)


[qlCreditDefaultSwapConventionalSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L543)(cds: ql.CreditDefaultSwap, conventional_recovery: float, discount_curve: ql.YieldTermStructureHandle, day_counter: qDayCounter, model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.ISDA, trigger = None)


[qlMakeCreditDefaultSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L558)(maturity: str | float, running_spread: float, upfront_rate = None, side = None, notional = None, coupon_tenor = None, day_counter = None, last_period_day_counter = None, date_generation_rule = None, cash_settlement_days = None, pricing_engine = None, trade_date = None, trigger = None)


[qlCdsMaturity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L613)(trade_date: qDate, tenor: qPeriod, date_generation_rule: qDateGenerationRule, trigger = None)


[qlMidPointCdsEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L631)(default_curve: ql.DefaultProbabilityTermStructureHandle, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, trigger = None)


[qlIntegralCdsEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L651)(integration_step: qPeriod, default_curve: ql.DefaultProbabilityTermStructureHandle, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool = False, trigger = None)


[qlIsdaCdsEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L681)(default_curve: ql.DefaultProbabilityTermStructureHandle, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool = False, numerical_fix: qIsdaCdsEngineNumericalFix = ql.IsdaCdsEngine.Taylor, accrual_bias: qIsdaCdsEngineAccrualBias = ql.IsdaCdsEngine.HalfDayBias, forwards_in_coupon_period: qIsdaCdsEngineForwardsInCouponPeriod = ql.IsdaCdsEngine.Piecewise, trigger = None)


[qlCdsOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L711)(cds: ql.CreditDefaultSwap, exercise: ql.Exercise, knocks_out: bool = True, trigger = None)


[qlBlackCdsOptionEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/creditdefaultswap.py#L730)(default_curve: ql.DefaultProbabilityTermStructureHandle, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, vol: qQuoteHandle, trigger = None)


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


## Defaultprobability


[qlDefaultProbabilityTermStructureDefaultProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L26)(ts: ql.DefaultProbabilityTermStructureHandle, date: qDate, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureDefaultProbabilityFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L44)(ts: ql.DefaultProbabilityTermStructureHandle, time: float, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureDefaultProbability2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L63)(ts: ql.DefaultProbabilityTermStructureHandle, date_one: qDate, date_two: qDate, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureDefaultProbabilityFromTime2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L83)(ts: ql.DefaultProbabilityTermStructureHandle, time_one: float, time_two: float, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureSurvivalProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L102)(ts: ql.DefaultProbabilityTermStructureHandle, date: qDate, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureSurvivalProbabilityFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L120)(ts: ql.DefaultProbabilityTermStructureHandle, time: float, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureDefaultDensity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L138)(ts: ql.DefaultProbabilityTermStructureHandle, date: qDate, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureDefaultDensityFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L156)(ts: ql.DefaultProbabilityTermStructureHandle, time: float, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureHazardRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L174)(ts: ql.DefaultProbabilityTermStructureHandle, date: qDate, extrapolate: bool = False, trigger = None)


[qlDefaultProbabilityTermStructureHazardRateFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L192)(ts: ql.DefaultProbabilityTermStructureHandle, time: float, extrapolate: bool = False, trigger = None)


[qlFlatHazardRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L213)(reference_date: qDate, hazard_rate: qQuoteHandle, day_counter: qDayCounter, trigger = None)


[qlHazardRateCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L233)(dates: xlo.Array(dims=1), hazard_rates: xlo.Array(dims=1), day_counter: qDayCounter, calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlDefaultDensityCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L256)(dates: xlo.Array(dims=1), default_densities: xlo.Array(dims=1), day_counter: qDayCounter, calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlSurvivalProbabilityCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L279)(dates: xlo.Array(dims=1), survival_probabilities: xlo.Array(dims=1), day_counter: qDayCounter, calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlDefaultProbabilityHelperQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L305)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperLatestDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L318)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperEarliestDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L331)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperMaturity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L344)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperLatestRelevantDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L357)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperPillarDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L370)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperImpliedQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L383)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlDefaultProbabilityHelperQuoteError](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L397)(helper: ql.DefaultProbabilityHelper, trigger = None)


[qlSpreadCdsHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L426)(spread: qQuoteHandle, tenor: qPeriod, settlement_days: int, calendar: qCalendar, frequency: qFrequency, payment_convention: qBusinessDayConvention, date_generation: qDateGenerationRule, day_counter: qDayCounter, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, settles_accrual: bool = True, pays_at_default: bool = True, start_date: qDate = ql.Date(), last_period_day_counter: str = None, rebates_accrual: bool = True, model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.Midpoint, trigger = None)


[qlUpfrontCdsHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L494)(upfront: qQuoteHandle, spread: float, tenor: qPeriod, settlement_days: int, calendar: qCalendar, frequency: qFrequency, payment_convention: qBusinessDayConvention, date_generation: qDateGenerationRule, day_counter: qDayCounter, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, upfront_settlement_days: int = 0, settles_accrual: bool = True, pays_at_default: bool = True, start_date: qDate = ql.Date(), last_period_day_counter: str = None, rebates_accrual: bool = True, model: qCreditDefaultSwapPricingModel = ql.CreditDefaultSwap.Midpoint, trigger = None)


[qlPiecewiseFlatHazardRateAsDts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L551)(reference_date: qDate, helpers: xlo.Array(dims=1), day_counter: qDayCounter, trigger = None)


[qlPiecewiseFlatHazardRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L573)(reference_date: qDate, helpers: xlo.Array(dims=1), day_counter: qDayCounter, trigger = None)


[qlRiskyBondEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/defaultprobability.py#L596)(default_curve: ql.DefaultProbabilityTermStructureHandle, recovery_rate: float, discount_curve: ql.YieldTermStructureHandle, trigger = None)


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


## Options


[qCashDividendModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L185)(s: str)


[qBinomialEngineType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L194)(s: str)


[qMCTraits](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L203)(s: str)


[qLsmBasisSystemPolynomialType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L212)(s: str)


[qAnalyticHestonComplexLogFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L221)(s: str)


[qAnalyticPTDHestonComplexLogFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L230)(s: str)


[qAnalyticHestonEngineIntegration](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L249)(name: str)


[qFdmSchemeType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L291)(s: str)


[qFdmSchemeDesc](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L300)(s: str)


[qFdBlackScholesCashDividendModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L309)(s: str)


[qQdPlusSolverType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L318)(s: str)


[qQdFpFixedPointEquation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L327)(s: str)


[qQdFpIterationScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L340)(s: str)


[qDeltaVolQuoteDeltaType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L349)(s: str)


[qDeltaVolQuoteAtmType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L358)(s: str)


[qlOptionTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L369)(option_type: qOptionType, trigger = None)


[qlOptionPayoff](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L383)(option: ql.Option, trigger = None)


[qlOptionExercise](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L394)(option: ql.Option, trigger = None)


[qlOneAssetOptionDelta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L408)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionDeltaForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L419)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionElasticity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L430)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionGamma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L441)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionTheta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L452)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionThetaPerDay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L463)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionVega](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L474)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L485)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionDividendRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L496)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionStrikeSensitivity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L507)(option: ql.OneAssetOption, trigger = None)


[qlOneAssetOptionITMCashProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L518)(option: ql.OneAssetOption, trigger = None)


[qlVanillaOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L535)(payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger = None)


[qlVanillaOptionImpliedVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L555)(option: ql.VanillaOption, target_value: float, process: ql.GeneralizedBlackScholesProcess, dividends: xlo.Array(dims=1) = None, accuracy: float = 1.0e-4, max_evaluations: int = 100, min_vol: float = 1.0e-4, max_vol: float = 4.0, trigger = None)


[qlEuropeanOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L590)(payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger = None)


[qlForwardVanillaOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L609)(moneyness: float, reset_date: qDate, payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger = None)


[qlQuantoVanillaOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L627)(payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger = None)


[qlQuantoVanillaOptionQVega](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L640)(option: ql.QuantoVanillaOption, trigger = None)


[qlQuantoVanillaOptionQRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L651)(option: ql.QuantoVanillaOption, trigger = None)


[qlQuantoVanillaOptionQLambda](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L662)(option: ql.QuantoVanillaOption, trigger = None)


[qlQuantoForwardVanillaOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L676)(moneyness: float, reset_date: qDate, payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger = None)


[qlMultiAssetOptionDelta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L696)(option: ql.MultiAssetOption, trigger = None)


[qlMultiAssetOptionGamma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L707)(option: ql.MultiAssetOption, trigger = None)


[qlMultiAssetOptionTheta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L718)(option: ql.MultiAssetOption, trigger = None)


[qlMultiAssetOptionVega](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L729)(option: ql.MultiAssetOption, trigger = None)


[qlMultiAssetOptionRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L740)(option: ql.MultiAssetOption, trigger = None)


[qlMultiAssetOptionDividendRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L751)(option: ql.MultiAssetOption, trigger = None)


[qlMargrabeOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L767)(q1: int, q2: int, exercise: ql.Exercise, trigger = None)


[qlMargrabeOptionDelta1](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L780)(option: ql.MargrabeOption, trigger = None)


[qlMargrabeOptionDelta2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L791)(option: ql.MargrabeOption, trigger = None)


[qlMargrabeOptionGamma1](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L802)(option: ql.MargrabeOption, trigger = None)


[qlMargrabeOptionGamma2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L813)(option: ql.MargrabeOption, trigger = None)


[qlTwoAssetCorrelationOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L827)(option_type: qOptionType, strike1: float, strike2: float, exercise: ql.Exercise, trigger = None)


[qlCompoundOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L850)(mother_payoff: ql.StrikedTypePayoff, mother_exercise: ql.Exercise, daughter_payoff: ql.StrikedTypePayoff, daughter_exercise: ql.Exercise, trigger = None)


[qlSimpleChooserOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L871)(choosing_date: qDate, strike: float, exercise: ql.Exercise, trigger = None)


[qlComplexChooserOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L888)(choosing_date: qDate, strike_call: float, strike_put: float, exercise_call: ql.Exercise, exercise_put: ql.Exercise, trigger = None)


[qlHolderExtensibleOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L913)(option_type: qOptionType, premium: float, second_expiry_date: qDate, second_strike: float, payoff: ql.StrikedTypePayoff, exercise: ql.Exercise, trigger = None)


[qlWriterExtensibleOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L942)(payoff1: ql.PlainVanillaPayoff, exercise1: ql.Exercise, payoff2: ql.PlainVanillaPayoff, exercise2: ql.Exercise, trigger = None)


[qlAnalyticEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L965)(process: ql.GeneralizedBlackScholesProcess, discount_curve: ql.YieldTermStructureHandle = None, trigger = None)


[qlAnalyticDividendEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L983)(process: ql.GeneralizedBlackScholesProcess, dividends: xlo.Array(dims=1), trigger = None)


[qlCashDividendEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1002)(process: ql.GeneralizedBlackScholesProcess, dividends: xlo.Array(dims=1), cash_dividend_model: qCashDividendModel = ql.CashDividendEuropeanEngine.Spot, trigger = None)


[qlIntegralEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1020)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlForwardEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1033)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlQuantoEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1049)(process: ql.GeneralizedBlackScholesProcess, foreign_risk_free_rate: ql.YieldTermStructureHandle, exchange_rate_volatility: ql.BlackVolTermStructureHandle, correlation: qQuoteHandle, trigger = None)


[qlQuantoForwardEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1071)(process: ql.GeneralizedBlackScholesProcess, foreign_risk_free_rate: ql.YieldTermStructureHandle, exchange_rate_volatility: ql.BlackVolTermStructureHandle, correlation: qQuoteHandle, trigger = None)


[qlBaroneAdesiWhaleyApproximationEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1094)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlBjerksundStenslandApproximationEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1108)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlJuQuadraticApproximationEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1122)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticDigitalAmericanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1136)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticEuropeanMargrabeEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1155)(process1: ql.GeneralizedBlackScholesProcess, process2: ql.GeneralizedBlackScholesProcess, correlation: float, trigger = None)


[qlAnalyticAmericanMargrabeEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1173)(process1: ql.GeneralizedBlackScholesProcess, process2: ql.GeneralizedBlackScholesProcess, correlation: float, trigger = None)


[qlAnalyticCompoundOptionEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1189)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticSimpleChooserEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1202)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticComplexChooserEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1215)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticHolderExtensibleOptionEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1228)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticWriterExtensibleOptionEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1242)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlAnalyticTwoAssetCorrelationEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1258)(process1: ql.GeneralizedBlackScholesProcess, process2: ql.GeneralizedBlackScholesProcess, correlation: qQuoteHandle, trigger = None)


[qlHestonModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1277)(process: ql.HestonProcess, trigger = None)


[qlHestonModelHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1288)(model: ql.HestonModel, trigger = None)


[qlHestonModelHandleCurrentLink](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1299)(model_handle: ql.HestonModelHandle, trigger = None)


[qlHestonModelTheta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1312)(model: ql.HestonModel, trigger = None)


[qlHestonModelKappa](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1323)(model: ql.HestonModel, trigger = None)


[qlHestonModelSigma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1334)(model: ql.HestonModel, trigger = None)


[qlHestonModelRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1345)(model: ql.HestonModel, trigger = None)


[qlHestonModelV0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1356)(model: ql.HestonModel, trigger = None)


[qlHestonModelProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1367)(model: ql.HestonModel, trigger = None)


[qlPiecewiseTimeDependentHestonModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1386)(risk_free_rate: ql.YieldTermStructureHandle, dividend_yield: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, theta: ql.Parameter, kappa: ql.Parameter, sigma: ql.Parameter, rho: ql.Parameter, time_grid: ql.TimeGrid, trigger = None)


[qlPiecewiseTimeDependentHestonModelTheta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1411)(model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger = None)


[qlPiecewiseTimeDependentHestonModelKappa](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1425)(model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger = None)


[qlPiecewiseTimeDependentHestonModelSigma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1439)(model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger = None)


[qlPiecewiseTimeDependentHestonModelRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1453)(model: ql.PiecewiseTimeDependentHestonModel, t: float, trigger = None)


[qlPiecewiseTimeDependentHestonModelV0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1466)(model: ql.PiecewiseTimeDependentHestonModel, trigger = None)


[qlPiecewiseTimeDependentHestonModelS0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1479)(model: ql.PiecewiseTimeDependentHestonModel, trigger = None)


[qlAnalyticHestonEngineIntegrationGaussLaguerre](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1495)(integration_order: int = 128, trigger = None)


[qlAnalyticHestonEngineIntegrationNumberOfEvaluations](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1509)(integration: ql.AnalyticHestonEngine_Integration, trigger = None)


[qlAnalyticHestonEngineIntegrationIsAdaptive](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1523)(integration: ql.AnalyticHestonEngine_Integration, trigger = None)


[qlAnalyticHestonEngineIntegrationAndersenPiterbargIntegrationLimit](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1540)(c_inf: float, epsilon: float, v0: float, t: float, trigger = None)


[qlAnalyticHestonEngineOptimalAlpha](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1560)(t: float, engine: ql.AnalyticHestonEngine, trigger = None)


[qlAnalyticHestonEngineOptimalAlphaValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1576)(optimal_alpha: ql.AnalyticHestonEngine_OptimalAlpha, strike: float, trigger = None)


[qlAnalyticHestonEngineOptimalAlphaBounds](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1592)(optimal_alpha: ql.AnalyticHestonEngine_OptimalAlpha, strike: float, trigger = None)


[qlAnalyticHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1613)(model: ql.HestonModel, integration_order: int = 144, rel_tolerance: float = None, abs_tolerance: float = None, max_evaluations: int = None, complex_log_formula: qAnalyticHestonComplexLogFormula = ql.AnalyticHestonEngine.Gatheral, integration: qAnalyticHestonEngineIntegration = None, andersen_piterbarg_epsilon: float = 1.0e-8, trigger = None)


[qlAnalyticHestonEngineNumberOfEvaluations](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1651)(engine: ql.AnalyticHestonEngine, trigger = None)


[qlCOSHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1666)(model: ql.HestonModel, l: float = 16.0, n: int = 200, trigger = None)


[qlExponentialFittingHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1682)(model: ql.HestonModel, control_variate: qAnalyticHestonComplexLogFormula = ql.AnalyticHestonEngine.OptimalCV, scaling: float = ql.nullDouble(), alpha: float = -0.5, trigger = None)


[qlAnalyticPDFHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1701)(model: ql.HestonModel, gauss_lobatto_eps: float = 1.0e-6, gauss_lobatto_integration_order: int = 10000, trigger = None)


[qlAnalyticHestonForwardEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1720)(process: ql.HestonProcess, integration_order: int = 144, trigger = None)


[qlAnalyticPTDHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1741)(model: ql.PiecewiseTimeDependentHestonModel, integration_order: int = 144, rel_tolerance: float = None, abs_tolerance: float = None, max_evaluations: int = None, complex_log_formula: qAnalyticPTDHestonComplexLogFormula = ql.AnalyticPTDHestonEngine.Gatheral, integration: qAnalyticHestonEngineIntegration = None, andersen_piterbarg_epsilon: float = 1.0e-8, trigger = None)


[qlAnalyticHestonHullWhiteEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1785)(heston_model: ql.HestonModel, hull_white_model: ql.HullWhite, integration_order: int = 144, rel_tolerance: float = None, max_evaluations: int = None, trigger = None)


[qlAnalyticH1HWEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1814)(heston_model: ql.HestonModel, hull_white_model: ql.HullWhite, rho_sr: float, integration_order: int = 144, rel_tolerance: float = None, max_evaluations: int = None, trigger = None)


[qlBinomialVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1844)(process: ql.GeneralizedBlackScholesProcess, engine_type: qBinomialEngineType, steps: int, trigger = None)


[qlFdmSchemeDesc](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1865)(scheme_type: qFdmSchemeType = ql.FdmSchemeDesc.DouglasType, theta: float = 0.5, mu: float = 0.0, trigger = None)


[qlFdmSchemeDescByName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1881)(scheme_desc: qFdmSchemeDesc, trigger = None)


[qlFdmQuantoHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1898)(domestic_ts: ql.YieldTermStructureHandle, foreign_ts: ql.YieldTermStructureHandle, fx_vol_ts: ql.BlackVolTermStructureHandle, equity_fx_correlation: float, exchange_rate_atm_level: float, trigger = None)


[qlFdBlackScholesVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L1931)(process: ql.GeneralizedBlackScholesProcess, dividends: xlo.Array(dims=1) = None, quanto_helper: ql.FdmQuantoHelper = None, t_grid: int = 100, x_grid: int = 100, damping_steps: int = 0, scheme_desc: ql.FdmSchemeDesc = None, local_vol: bool = False, illegal_local_vol_overwrite: float = -ql.nullDouble(), cash_dividend_model: qFdBlackScholesCashDividendModel = ql.FdBlackScholesVanillaEngine.Spot, trigger = None)


[qlFdBlackScholesShoutEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2008)(process: ql.GeneralizedBlackScholesProcess, dividends: xlo.Array(dims=1) = None, t_grid: int = 100, x_grid: int = 100, damping_steps: int = 0, scheme_desc: ql.FdmSchemeDesc = None, trigger = None)


[qlFdOrnsteinUhlenbeckVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2042)(process: ql.OrnsteinUhlenbeckProcess, discount_curve: ql.YieldTermStructureHandle, dividends: xlo.Array(dims=1) = None, t_grid: int = 100, x_grid: int = 100, damping_steps: int = 0, epsilon: float = 1.0e-4, scheme_desc: ql.FdmSchemeDesc = None, trigger = None)


[qlFdBatesVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2090)(model: ql.BatesModel, dividends: xlo.Array(dims=1) = None, t_grid: int = 100, x_grid: int = 100, v_grid: int = 50, damping_steps: int = 0, scheme_desc: ql.FdmSchemeDesc = None, trigger = None)


[qlFdHestonVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2129)(model: ql.HestonModel, dividends: xlo.Array(dims=1) = None, quanto_helper: ql.FdmQuantoHelper = None, t_grid: int = 100, x_grid: int = 100, v_grid: int = 50, damping_steps: int = 0, scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(), leverage_fct: ql.LocalVolTermStructureHandle = None, mixing_factor: float = 1.0, trigger = None)


[qlFdCEVVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2211)(f0: float, alpha: float, beta: float, discount_curve: ql.YieldTermStructureHandle, t_grid: int = 50, x_grid: int = 400, damping_steps: int = 0, scaling_factor: float = 1.0, eps: float = 1.0e-4, scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Douglas(), trigger = None)


[qlFdSabrVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2257)(f0: float, alpha: float, beta: float, nu: float, rho: float, discount_curve: ql.YieldTermStructureHandle, t_grid: int = 50, f_grid: int = 400, x_grid: int = 50, damping_steps: int = 0, scaling_factor: float = 1.0, eps: float = 1.0e-4, scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(), trigger = None)


[qlFdHestonHullWhiteVanillaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2307)(model: ql.HestonModel, hull_white_process: ql.HullWhiteProcess, corr_equity_short_rate: float, dividends: xlo.Array(dims=1) = None, t_grid: int = 50, x_grid: int = 100, v_grid: int = 40, r_grid: int = 20, damping_steps: int = 0, control_variate: bool = True, scheme_desc: ql.FdmSchemeDesc = ql.FdmSchemeDesc.Hundsdorfer(), trigger = None)


[qlMCEuropeanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2369)(process: ql.GeneralizedBlackScholesProcess, traits: qMCTraits, time_steps: int = ql.nullInt(), time_steps_per_year: int = ql.nullInt(), brownian_bridge: bool = False, antithetic_variate: bool = False, required_samples: int = ql.nullInt(), required_tolerance: float = ql.nullDouble(), max_samples: int = ql.nullInt(), seed: int = 0, trigger = None)


[qlMCAmericanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2417)(process: ql.GeneralizedBlackScholesProcess, traits: qMCTraits, time_steps: int = ql.nullInt(), time_steps_per_year: int = ql.nullInt(), antithetic_variate: bool = False, control_variate: bool = False, required_samples: int = ql.nullInt(), required_tolerance: float = ql.nullDouble(), max_samples: int = ql.nullInt(), seed: int = 0, polynom_order: int = 2, polynom_type: qLsmBasisSystemPolynomialType = ql.LsmBasisSystem.Monomial, n_calibration_samples: int = 2048, antithetic_variate_calibration: bool = None, seed_calibration: int = ql.nullInt(), trigger = None)


[qlMCDigitalEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2470)(process: ql.GeneralizedBlackScholesProcess, traits: qMCTraits, time_steps: int = ql.nullInt(), time_steps_per_year: int = ql.nullInt(), brownian_bridge: bool = False, antithetic_variate: bool = False, required_samples: int = ql.nullInt(), required_tolerance: float = ql.nullDouble(), max_samples: int = ql.nullInt(), seed: int = 0, trigger = None)


[qlMCEuropeanHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2512)(process: ql.HestonProcess, traits: qMCTraits, time_steps: int = ql.nullInt(), time_steps_per_year: int = ql.nullInt(), antithetic_variate: bool = False, required_samples: int = ql.nullInt(), required_tolerance: float = ql.nullDouble(), max_samples: int = ql.nullInt(), seed: int = 0, trigger = None)


[qlMCForwardEuropeanBSEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2553)(process: ql.GeneralizedBlackScholesProcess, traits: qMCTraits, time_steps: int = ql.nullInt(), time_steps_per_year: int = ql.nullInt(), brownian_bridge: bool = False, antithetic_variate: bool = False, required_samples: int = ql.nullInt(), required_tolerance: float = ql.nullDouble(), max_samples: int = ql.nullInt(), seed: int = 0, trigger = None)


[qlMCForwardEuropeanHestonEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2596)(process: ql.HestonProcess, traits: qMCTraits, time_steps: int = ql.nullInt(), time_steps_per_year: int = ql.nullInt(), antithetic_variate: bool = False, required_samples: int = ql.nullInt(), required_tolerance: float = ql.nullDouble(), max_samples: int = ql.nullInt(), seed: int = 0, control_variate: bool = False, trigger = None)


[qlQdPlusAmericanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2637)(process: ql.GeneralizedBlackScholesProcess, interpolation_points: int = 8, solver_type: qQdPlusSolverType = ql.QdPlusAmericanEngine.Halley, eps: float = 1.0e-6, max_iter: int = ql.nullInt(), trigger = None)


[qlQdFpLegendreScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2660)(l: int, m: int, n: int, p: int, trigger = None)


[qlQdFpLegendreTanhSinhScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2676)(l: int, m: int, n: int, eps: float, trigger = None)


[qlQdFpTanhSinhIterationScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2691)(m: int, n: int, eps: float, trigger = None)


[qlQdFpAmericanEngineFastScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2701)(trigger = None)


[qlQdFpAmericanEngineAccurateScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2709)(trigger = None)


[qlQdFpAmericanEngineHighPrecisionScheme](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2717)(trigger = None)


[qlQdFpAmericanEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2730)(process: ql.GeneralizedBlackScholesProcess, iteration_scheme: qQdFpIterationScheme = ql.QdFpAmericanEngine.accurateScheme(), fixed_point_equation: qQdFpFixedPointEquation = ql.QdFpAmericanEngine.Auto, trigger = None)


[qlAnalyticCEVEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2752)(f0: float, alpha: float, beta: float, discount_curve: ql.YieldTermStructureHandle, trigger = None)


[qlBatesModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2769)(process: ql.BatesProcess, trigger = None)


[qlBatesEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2783)(model: ql.BatesModel, integration_order: int = 144, rel_tolerance: float = None, max_evaluations: int = None, trigger = None)


[qlVarianceGammaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2802)(process: ql.VarianceGammaProcess, trigger = None)


[qlFFTVarianceGammaEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2816)(process: ql.VarianceGammaProcess, log_strike_spacing: float = 0.001, trigger = None)


[qlGJRGARCHModel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2831)(process: ql.GJRGARCHProcess, trigger = None)


[qlAnalyticGJRGARCHEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2842)(model: ql.GJRGARCHModel, trigger = None)


[qlBlackCalculator](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2863)(payoff: ql.StrikedTypePayoff, forward: float, std_dev: float, discount: float = 1.0, trigger = None)


[qlBlackCalculatorValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2880)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorDelta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2892)(calculator: ql.BlackCalculator, spot: float, trigger = None)


[qlBlackCalculatorGamma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2906)(calculator: ql.BlackCalculator, spot: float, trigger = None)


[qlBlackCalculatorVega](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2920)(calculator: ql.BlackCalculator, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorTheta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2935)(calculator: ql.BlackCalculator, spot: float, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorThetaPerDay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2950)(calculator: ql.BlackCalculator, spot: float, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2964)(calculator: ql.BlackCalculator, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorDividendRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2978)(calculator: ql.BlackCalculator, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorDeltaForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L2991)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorGammaForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3004)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorElasticity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3018)(calculator: ql.BlackCalculator, spot: float, trigger = None)


[qlBlackCalculatorElasticityForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3031)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorITMCashProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3044)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorITMAssetProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3057)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorStrikeSensitivity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3070)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorStrikeGamma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3083)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorAlpha](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3094)(calculator: ql.BlackCalculator, trigger = None)


[qlBlackCalculatorVanna](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3107)(calculator: ql.BlackCalculator, spot: float, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorVolga](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3121)(calculator: ql.BlackCalculator, maturity: float = 1.0, trigger = None)


[qlBlackCalculatorBeta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3134)(calculator: ql.BlackCalculator, trigger = None)


[qlBachelierCalculator](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3151)(payoff: ql.StrikedTypePayoff, forward: float, std_dev: float, discount: float = 1.0, trigger = None)


[qlBachelierCalculatorValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3168)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorDelta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3182)(calculator: ql.BachelierCalculator, spot: float, trigger = None)


[qlBachelierCalculatorGamma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3196)(calculator: ql.BachelierCalculator, spot: float, trigger = None)


[qlBachelierCalculatorVega](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3210)(calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorTheta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3225)(calculator: ql.BachelierCalculator, spot: float, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorThetaPerDay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3240)(calculator: ql.BachelierCalculator, spot: float, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3254)(calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorDividendRho](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3268)(calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorDeltaForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3281)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorGammaForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3294)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorElasticity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3308)(calculator: ql.BachelierCalculator, spot: float, trigger = None)


[qlBachelierCalculatorElasticityForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3321)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorITMCashProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3334)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorITMAssetProbability](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3347)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorStrikeSensitivity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3360)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorStrikeGamma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3373)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorAlpha](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3386)(calculator: ql.BachelierCalculator, trigger = None)


[qlBachelierCalculatorVanna](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3400)(calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorVolga](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3414)(calculator: ql.BachelierCalculator, maturity: float = 1.0, trigger = None)


[qlBachelierCalculatorBeta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3427)(calculator: ql.BachelierCalculator, trigger = None)


[qlDeltaVolQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3446)(delta: float, vol: qQuoteHandle, maturity: float, delta_type: qDeltaVolQuoteDeltaType, trigger = None)


[qlDeltaVolQuoteAtm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3471)(vol: qQuoteHandle, delta_type: qDeltaVolQuoteDeltaType, maturity: float, atm_type: qDeltaVolQuoteAtmType)


[qlDeltaVolQuoteDelta](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3492)(quote: ql.DeltaVolQuote, trigger = None)


[qlDeltaVolQuoteMaturity](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3503)(quote: ql.DeltaVolQuote, trigger = None)


[qlDeltaVolQuoteDeltaType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3514)(quote: ql.DeltaVolQuote, trigger = None)


[qlDeltaVolQuoteAtmType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3525)(quote: ql.DeltaVolQuote, trigger = None)


[qlDeltaVolQuoteValue](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3536)(quote: ql.DeltaVolQuote, trigger = None)


[qlDeltaVolQuoteIsValid](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/options.py#L3547)(quote: ql.DeltaVolQuote, trigger = None)


## Parameter


[qlParameterParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L15)(parameter: ql.Parameter, trigger = None)


[qlParameterSetParam](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L28)(parameter: ql.Parameter, idx: int, x: float, trigger = None)


[qlParameterTestParams](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L48)(parameter: ql.Parameter, params: xlo.Array(dims=1), trigger = None)


[qlParameterSize](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L60)(parameter: ql.Parameter, trigger = None)


[qlParameterAtTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L72)(parameter: ql.Parameter, t: float, trigger = None)


[qlParameterConstraint](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L81)(parameter: ql.Parameter, trigger = None)


[qlNullParameter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L93)(trigger = None)


[qlConstantParameter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L102)(constraint: ql.Constraint, value: float = None, trigger = None)


[qlPiecewiseConstantParameter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/parameter.py#L123)(times: xlo.Array(dims=1), values: xlo.Array(dims=1), constraint: ql.Constraint = ql.NoConstraint(), trigger = None)


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


[qlYieldTermStructureHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L39)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L56)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveTimes](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L70)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveData](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L84)(curve: ql.YieldTermStructure, trigger = None)


[qlPiecewiseYieldCurveAsYts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L104)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseYieldCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L154)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseYieldCurveWithJumpsAsYts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L194)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, jumps: xlo.Array(dims=1), jump_dates: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseYieldCurveWithJumps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L255)(reference_date: qDate, instruments: xlo.Array(dims=1), daycounter: qDayCounter, jumps: xlo.Array(dims=1), jump_dates: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseSpreadYieldCurveAsYts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L296)(base_curve: ql.YieldTermStructureHandle, instruments: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlPiecewiseSpreadYieldCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/piecewiseyieldcurve.py#L342)(base_curve: ql.YieldTermStructureHandle, instruments: xlo.Array(dims=1), traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


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


[qGJRGARCHProcessDiscretization](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L46)(discretization: str)


[qHestonProcessDiscretization](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L51)(discretization: str)


[qlStochasticProcessSize](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L62)(process: ql.StochasticProcess, trigger = None)


[qlStochasticProcessFactors](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L73)(process: ql.StochasticProcess, trigger = None)


[qlStochasticProcessInitialValues](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L84)(process: ql.StochasticProcess, trigger = None)


[qlStochasticProcessDrift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L99)(process: ql.StochasticProcess, t: float, x: xlo.Array(dims=1), trigger = None)


[qlStochasticProcessDiffusion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L114)(process: ql.StochasticProcess, t: float, x: xlo.Array(dims=1), trigger = None)


[qlStochasticProcessExpectation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L130)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger = None)


[qlStochasticProcessStdDeviation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L150)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger = None)


[qlStochasticProcessCovariance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L170)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, trigger = None)


[qlStochasticProcessEvolve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L191)(process: ql.StochasticProcess, t0: float, x0: xlo.Array(dims=1), dt: float, dw: xlo.Array(dims=1), trigger = None)


[qlStochasticProcess1DX0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L211)(process: ql.StochasticProcess1D, trigger = None)


[qlStochasticProcess1DDrift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L224)(process: ql.StochasticProcess1D, t: float, x: float, trigger = None)


[qlStochasticProcess1DDiffusion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L239)(process: ql.StochasticProcess1D, t: float, x: float, trigger = None)


[qlStochasticProcess1DExpectation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L255)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger = None)


[qlStochasticProcess1DStdDeviation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L271)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger = None)


[qlStochasticProcess1DVariance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L287)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, trigger = None)


[qlStochasticProcess1DEvolve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L304)(process: ql.StochasticProcess1D, t0: float, x0: float, dt: float, dw: float, trigger = None)


[qlStochasticProcess1DApply](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L324)(process: ql.StochasticProcess1D, x0: float, dx: float, trigger = None)


[qlGeneralizedBlackScholesProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L341)(s0: qQuoteHandle, dividend_ts: ql.YieldTermStructureHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, local_vol_ts: ql.LocalVolTermStructureHandle = None, trigger = None)


[qlGeneralizedBlackScholesProcessStateVariable](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L363)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessDividendYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L376)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessRiskFreeRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L389)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessBlackVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L402)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlGeneralizedBlackScholesProcessLocalVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L415)(process: ql.GeneralizedBlackScholesProcess, trigger = None)


[qlBlackScholesProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L430)(s0: qQuoteHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlBlackScholesMertonProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L449)(s0: qQuoteHandle, dividend_ts: ql.YieldTermStructureHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlBlackProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L468)(s0: qQuoteHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlGarmanKohlagenProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L487)(s0: qQuoteHandle, foreign_risk_free_ts: ql.YieldTermStructureHandle, domestic_risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, trigger = None)


[qlMerton76Process](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L512)(state_variable: qQuoteHandle, dividend_ts: ql.YieldTermStructureHandle, risk_free_ts: ql.YieldTermStructureHandle, vol_ts: ql.BlackVolTermStructureHandle, jump_intensity: qQuoteHandle, mean_log_jump: qQuoteHandle, jump_volatility: qQuoteHandle, trigger = None)


[qlStochasticProcessArray](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L541)(array: xlo.Array(dims=1), correlation: xlo.Array(dims=2), trigger = None)


[qlGeometricBrownianMotionProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L561)(initial_value: float, mu: float, sigma: float, trigger = None)


[qlVarianceGammaProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L582)(s0: qQuoteHandle, dividend_yield: ql.YieldTermStructureHandle, risk_free_rate: ql.YieldTermStructureHandle, sigma: float, nu: float, theta: float, trigger = None)


[qlHestonProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L609)(risk_free_ts: ql.YieldTermStructureHandle, dividend_ts: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, kappa: float, theta: float, sigma: float, rho: float, discretization: qHestonProcessDiscretization = ql.HestonProcess.QuadraticExponentialMartingale, trigger = None)


[qlHestonProcessS0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L633)(process: ql.HestonProcess, trigger = None)


[qlHestonProcessDividendYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L644)(process: ql.HestonProcess, trigger = None)


[qlHestonProcessRiskFreeRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L657)(process: ql.HestonProcess, trigger = None)


[qlBatesProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L680)(risk_free_rate: ql.YieldTermStructureHandle, dividend_yield: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, kappa: float, theta: float, sigma: float, rho: float, lambda_parameter: float, nu: float, delta: float, trigger = None)


[qlHullWhiteProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L718)(risk_free_ts: ql.YieldTermStructureHandle, a: float, sigma: float, trigger = None)


[qlHullWhiteForwardProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L736)(risk_free_ts: ql.YieldTermStructureHandle, a: float, sigma: float, trigger = None)


[qlHullWhiteForwardProcessAlpha](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L753)(process: ql.HullWhiteForwardProcess, t: float, trigger = None)


[qlHullWhiteForwardProcessMT](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L769)(process: ql.HullWhiteForwardProcess, s: float, t: float, t_measure: float, trigger = None)


[qlHullWhiteForwardProcessB](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L788)(process: ql.HullWhiteForwardProcess, s: float, t: float, trigger = None)


[qlHullWhiteForwardProcessSetForwardMeasureTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L802)(process: ql.HullWhiteForwardProcess, t: float, trigger = None)


[qlG2Process](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L820)(a: float, sigma: float, b: float, eta: float, rho: float, trigger = None)


[qlG2ForwardProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L842)(a: float, sigma: float, b: float, eta: float, rho: float, trigger = None)


[qlG2ForwardProcessSetForwardMeasureTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L861)(process: ql.G2ForwardProcess, t: float, trigger = None)


[qlGsrProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L878)(times: xlo.Array(dims=1), vols: xlo.Array(dims=1), reversions: xlo.Array(dims=1), t: float = 60.0, trigger = None)


[qlGsrProcessSigma](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L899)(process: ql.GsrProcess, t: float, trigger = None)


[qlGsrProcessReversion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L912)(process: ql.GsrProcess, t: float, trigger = None)


[qlGsrProcessY](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L925)(process: ql.GsrProcess, t: float, trigger = None)


[qlGsrProcessG](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L940)(process: ql.GsrProcess, t: float, T: float, x: float, trigger = None)


[qlGsrProcessSetForwardMeasureTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L955)(process: ql.GsrProcess, t: float, trigger = None)


[qlOrnsteinUhlenbeckProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L973)(speed: float, vol: float, x0: float = 0.0, level: float = 0.0, trigger = None)


[qlOrnsteinUhlenbeckProcessSpeed](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L990)(process: ql.OrnsteinUhlenbeckProcess, trigger = None)


[qlOrnsteinUhlenbeckProcessVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1003)(process: ql.OrnsteinUhlenbeckProcess, trigger = None)


[qlOrnsteinUhlenbeckProcessLevel](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1016)(process: ql.OrnsteinUhlenbeckProcess, trigger = None)


[qlExtendedOrnsteinUhlenbeckProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1033)(speed: float, sigma: float, x0: float, function, int_eps: float = 1.0e-4, trigger = None)


[qlExtendedOrnsteinUhlenbeckProcessConstantFunction](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1051)(x: float)


[qlExtOUWithJumpsProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1067)(process: ql.ExtendedOrnsteinUhlenbeckProcess, Y0: float, beta: float, jump_intensity: float, eta: float, trigger = None)


[qlKlugeExtOUProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1087)(rho: float, kluge: ql.ExtOUWithJumpsProcess, ext_ou: ql.ExtendedOrnsteinUhlenbeckProcess, trigger = None)


[qlGJRGARCHProcess](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1113)(risk_free_rate: ql.YieldTermStructureHandle, dividend_yield: ql.YieldTermStructureHandle, s0: qQuoteHandle, v0: float, omega: float, alpha: float, beta: float, gamma: float, lambda_parameter: float, days_per_year: float = 252.0, discretization: qGJRGARCHProcessDiscretization = ql.GJRGARCHProcess.FullTruncation, trigger = None)


[qlGJRGARCHProcessS0](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1149)(process: ql.GJRGARCHProcess, trigger = None)


[qlGJRGARCHProcessDividendYield](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1160)(process: ql.GJRGARCHProcess, trigger = None)


[qlGJRGARCHProcessRiskFreeRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/stochasticprocess.py#L1173)(process: ql.GJRGARCHProcess, trigger = None)


## Swap


[qSwapType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L70)(swap_type: str | int | float)


[qlSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L82)(first_leg: xlo.Array(dims=1), second_leg: xlo.Array(dims=1), trigger = None)


[qlSwap2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L100)(legs: xlo.Array(dims=1), payer: xlo.Array(dims=1), trigger = None)


[qlSwapNumberOfLegs](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L117)(swap: ql.Swap, trigger = None)


[qlSwapStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L128)(swap: ql.Swap, trigger = None)


[qlSwapMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L139)(swap: ql.Swap, trigger = None)


[qlSwapLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L151)(swap: ql.Swap, i: int, trigger = None)


[qlSwapLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L163)(swap: ql.Swap, j: int, trigger = None)


[qlSwapLegBPS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L175)(swap: ql.Swap, k: int, trigger = None)


[qlSwapStartDiscounts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L187)(swap: ql.Swap, j: int, trigger = None)


[qlSwapEndDiscounts](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L199)(swap: ql.Swap, j: int, trigger = None)


[qlSwapNpvDateDiscount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L210)(swap: ql.Swap, trigger = None)


[qlSwapPayer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L222)(swap: ql.Swap, j: int, trigger = None)


[qlFixedVsFloatingSwapType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L233)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L247)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapNominals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L261)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedNominals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L275)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L289)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L303)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedDayCount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L317)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFloatingNominals](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L331)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFloatingSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L345)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapIborIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L359)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L373)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFloatingDayCount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L387)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapPaymentConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L401)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L415)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFloatingLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L429)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedLegBPS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L443)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFixedLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L457)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFairRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L471)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFloatingLegBPS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L485)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFloatingLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L499)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlFixedVsFloatingSwapFairSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L513)(swap: ql.FixedVsFloatingSwap, trigger = None)


[qlVanillaSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L537)(type: qSwapType, nominal: float, fixed_schedule: ql.Schedule, fixed_rate: float, fixed_day_count: qDayCounter, float_schedule: ql.Schedule, index: ql.IborIndex, spread: float, floating_day_count: qDayCounter, payment_convention: qBusinessDayConvention = ql.Following, with_indexed_coupons: Optional[bool] = None, trigger = None)


[qlMakeVanillaSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L607)(swap_tenor: qPeriod, ibor_index: ql.IborIndex, fixed_rate = None, forward_start: qPeriod = ql.Period(0, ql.Days), receive_fixed = None, swap_type = None, nominal = None, settlement_days = None, effective_date = None, termination_date = None, date_generation_rule = None, payment_convention = None, fixed_leg_tenor = None, fixed_leg_calendar = None, fixed_leg_convention = None, fixed_leg_termination_date_convention = None, fixed_leg_date_gen_rule = None, fixed_leg_end_of_month = None, fixed_leg_first_date = None, fixed_leg_next_to_last_date = None, fixed_leg_day_count = None, floating_leg_tenor = None, floating_leg_calendar = None, floating_leg_convention = None, floating_leg_termination_date_convention = None, floating_leg_date_gen_rule = None, floating_leg_end_of_month = None, floating_leg_first_date = None, floating_leg_next_to_last_date = None, floating_leg_day_count = None, floating_leg_spread = None, discounting_term_structure = None, pricing_engine = None, indexed_coupons = None, at_par_coupons = None, trigger = None)


[qlNonstandardSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L785)(type: qSwapType, fixed_nominal: xlo.Array(dims=1), floating_nominal: xlo.Array(dims=1), fixed_schedule: ql.Schedule, fixed_rate: xlo.Array(dims=1), fixed_day_count: qDayCounter, float_schedule: ql.Schedule, index: ql.IborIndex, gearing: xlo.Array(dims=1), spread: xlo.Array(dims=1), float_day_count: qDayCounter, intermediate_capital_exchange: bool = False, final_capital_exchange: bool = False, payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlNonstandardSwapType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L827)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFixedNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L838)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFloatingNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L849)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFixedSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L860)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFixedRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L873)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFixedDayCount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L884)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFloatingSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L897)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapIborIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L910)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L921)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapGearing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L932)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapSpreads](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L943)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapGearings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L954)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFloatingDayCount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L965)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapPaymentConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L978)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFixedLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L989)(swap: ql.NonstandardSwap, trigger = None)


[qlNonstandardSwapFloatingLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1000)(swap: ql.NonstandardSwap, trigger = None)


[qlDiscountingSwapEngine](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1014)(discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool = False, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlDiscountingSwapEngine2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1038)(discount_curve: ql.YieldTermStructureHandle, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlAssetSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1069)(pay_fixed_rate: bool, bond: ql.Bond, bond_clean_price: float, index: ql.IborIndex, spread: float, float_schedule: ql.Schedule = ql.Schedule(), floating_day_count: qDayCounter = ql.Actual360(), par_asset_swap: bool = True, gearing: float = 1.0, non_par_repayment: float = 0, deal_maturity: qDate = ql.Date(), trigger = None)


[qlAssetSwapFairCleanPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1105)(swap: ql.AssetSwap, trigger = None)


[qlAssetSwapFairSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1116)(swap: ql.AssetSwap, trigger = None)


[qlFloatFloatSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1148)(type: qSwapType, nominal1: xlo.Array(dims=1), nominal2: xlo.Array(dims=1), schedule1: ql.Schedule, index1: ql.InterestRateIndex, day_count1: qDayCounter, schedule2: ql.Schedule, index2: ql.InterestRateIndex, day_count2: qDayCounter, intermediate_capital_exchange: bool = False, final_capital_exchange: bool = False, gearing1: xlo.Array(dims=1) = None, spread1: xlo.Array(dims=1) = None, capped_rate1: xlo.Array(dims=1) = None, floored_rate1: xlo.Array(dims=1) = None, gearing2: xlo.Array(dims=1) = None, spread2: xlo.Array(dims=1) = None, capped_rate2: xlo.Array(dims=1) = None, floored_rate2: xlo.Array(dims=1) = None, payment_convention1: qBusinessDayConvention = ql.Following, payment_convention2: qBusinessDayConvention = ql.Following, trigger = None)


[qlOvernightIndexedSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1218)(type: qSwapType, nominal: float, schedule: ql.Schedule, fixed_rate: float, fixed_dc: qDayCounter, index: ql.OvernightIndex, spread: float = 0.0, payment_lag: int = 0, payment_adjustment: qBusinessDayConvention = ql.Following, payment_calendar: qCalendar = ql.NullCalendar(), telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, lookback_days: int = 0, lockout_days: int = 0, apply_observation_shift: bool = False, trigger = None)


[qlOvernightIndexedSwap2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1278)(type: qSwapType, fixed_nominals: xlo.Array(dims=1), fixed_schedule: ql.Schedule, fixed_rate: float, fixed_dc: qDayCounter, overnight_nominals: xlo.Array(dims=1), overnight_schedule: ql.Schedule, overnight_index: ql.OvernightIndex, spread: float = 0.0, payment_lag: int = 0, payment_adjustment: qBusinessDayConvention = ql.Following, payment_calendar: qCalendar = ql.NullCalendar(), telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, lookback_days: int = 0, lockout_days: int = 0, apply_observation_shift: bool = False, trigger = None)


[qlOvernightIndexedSwapOvernightLegBPS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1326)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapOvernightLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1339)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapPaymentFrequency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1352)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapOvernightIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1363)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapOvernightLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1376)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1389)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapLookbackDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1400)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapLockoutDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1413)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlOvernightIndexedSwapApplyObservationShift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1426)(swap: ql.OvernightIndexedSwap, trigger = None)


[qlMakeOIS](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1478)(swap_tenor: qPeriod, overnight_index: ql.OvernightIndex, fixed_rate: float = None, fwd_start: qPeriod = ql.Period(0, ql.Days), receive_fixed = None, swap_type = None, nominal = None, settlement_days = None, effective_date = None, termination_date = None, date_generation_rule = None, fixed_leg_rule = None, overnight_leg_rule = None, payment_frequency = None, fixed_leg_payment_frequency = None, overnight_leg_payment_frequency = None, payment_adjustment_convention = None, payment_lag = None, payment_calendar = None, calendar = None, fixed_leg_calendar = None, overnight_leg_calendar = None, convention = None, fixed_leg_convention = None, overnight_leg_convention = None, termination_date_convention = None, fixed_leg_termination_date_convention = None, overnight_leg_termination_date_convention = None, end_of_month = None, fixed_leg_end_of_month = None, overnight_leg_end_of_month = None, fixed_leg_day_count = None, overnight_leg_spread = None, discounting_term_structure = None, telescopic_value_dates = None, averaging_method = None, lookback_days = None, lockout_days = None, pricing_engine = None, trigger = None)


[qlOvernightIndexedSwapIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1680)(family_name: str, tenor: qPeriod, settlement_days: int, currency: qCurrency, overnight_index: ql.OvernightIndex, telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlOvernightIndexedSwapIndexOvernightIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1708)(index: ql.OvernightIndexedSwapIndex, trigger = None)


[qlOvernightIndexedSwapIndexUnderlyingSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1722)(index: ql.OvernightIndexedSwapIndex, fixing_date: qDate, trigger = None)


[qlAsOvernightSwapIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1736)(index: ql.InterestRateIndex, trigger = None)


[qlZeroCouponSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1757)(type: qSwapType, base_nominal: float, start_date: qDate, maturity_date: qDate, fixed_payment: float, ibor_index: ql.IborIndex, payment_calendar: qCalendar, payment_convention: qBusinessDayConvention = ql.Following, payment_delay: int = 0, trigger = None)


[qlZeroCouponSwap2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1798)(type: qSwapType, base_nominal: float, start_date: qDate, maturity_date: qDate, fixed_rate: float, fixed_day_counter: qDayCounter, ibor_index: ql.IborIndex, payment_calendar: qCalendar, payment_convention: qBusinessDayConvention = ql.Following, payment_delay: int = 0, trigger = None)


[qlZeroCouponSwapType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1832)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapBaseNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1843)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapIborIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1854)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFixedLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1865)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFloatingLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1876)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFixedPayment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1887)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFixedLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1898)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFloatingLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1909)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFairFixedPayment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1920)(swap: ql.ZeroCouponSwap, trigger = None)


[qlZeroCouponSwapFairFixedRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1932)(swap: ql.ZeroCouponSwap, day_counter: qDayCounter, trigger = None)


[qlEquityTotalReturnSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L1955)(type: qSwapType, nominal: float, schedule: ql.Schedule, equity_index: ql.EquityIndex, interest_rate_index: ql.IborIndex, day_counter: qDayCounter, margin: float, gearing: float = 1.0, payment_calendar: qCalendar = ql.NullCalendar(), payment_convention: qBusinessDayConvention = ql.Unadjusted, payment_delay: int = 0, trigger = None)


[qlEquityTotalReturnSwap2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2001)(type: qSwapType, nominal: float, schedule: ql.Schedule, equity_index: ql.EquityIndex, interest_rate_index: ql.OvernightIndex, day_counter: qDayCounter, margin: float, gearing: float = 1.0, payment_calendar: qCalendar = ql.NullCalendar(), payment_convention: qBusinessDayConvention = ql.Unadjusted, payment_delay: int = 0, trigger = None)


[qlEquityTotalReturnSwapType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2037)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2048)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapEquityIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2061)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapInterestRateIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2074)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2087)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2100)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapMargin](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2113)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapGearing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2126)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapPaymentCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2139)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapPaymentConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2152)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapPaymentDelay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2165)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapEquityLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2178)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapInterestRateLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2191)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapEquityLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2204)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapInterestRateLegNPV](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2217)(swap: ql.EquityTotalReturnSwap, trigger = None)


[qlEquityTotalReturnSwapFairMargin](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/swap.py#L2230)(swap: ql.EquityTotalReturnSwap, trigger = None)


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


