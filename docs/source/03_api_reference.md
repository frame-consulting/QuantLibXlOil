# API Reference

This section lists the QuantLib functions made available to Excel.


## Calendars


[qCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L89)(calendarname: str)


[qBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L100)(conventionname: str)


[qJointCalendarRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L108)(rule_name: str)


[qlCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L119)(calendar_name: str, trigger = None)


[qlCalendarisWeekend](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L129)(calendar: qCalendar, weekday: qWeekday, trigger = None)


[qlCalendarStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L141)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L152)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsBusinessDay](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L163)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L173)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L183)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarIsStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L193)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarAddHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L203)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarRemoveHoliday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L213)(calendar: qCalendar, date: qDate, trigger = None)


[qlCalendarResetAddedAndRemovedHolidays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L221)(calendar: qCalendar, trigger = None)


[qlCalendarAdjust](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L235)(calendar: qCalendar, date: qDate, convention: qBusinessDayConvention = "Following", trigger = None)


[qlCalendarAdvance](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L250)(calendar: qCalendar, date: qDate, n: int, unit: qTimeUnit, convention: qBusinessDayConvention = "Following", end_of_month: bool = False, trigger = None)


[qlCalendarAdvance2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L264)(calendar: qCalendar, date: qDate, period: qPeriod, convention: qBusinessDayConvention = "Following", end_of_month: bool = False, trigger = None)


[qlCalendarBusinessDaysBetween](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L279)(calendar: qCalendar, from_date: qDate, to_date: qDate, include_first: bool = True, include_last: bool = False, trigger = None)


[qlCalendarHolidayList](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L289)(calendar: qCalendar, from_date: qDate, to_date: qDate, trigger = None)


[qlCalendarBusinessDayList](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L300)(calendar: qCalendar, from_date: qDate, to_date: qDate, trigger = None)


[qlCalendarName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L310)(calendar: qCalendar, trigger = None)


[qlCalendarEmpty](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L320)(calendar: qCalendar, trigger = None)


[qlCalendarJointCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L332)(calendar1: qCalendar, calendar2: qCalendar, rule: qJointCalendarRule = "JOINHOLIDAYS")


[qlCalendarJointCalendar2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/calendars.py#L345)(calendar1: qCalendar, calendar2: qCalendar, calendar3: qCalendar, rule: qJointCalendarRule = "JOINHOLIDAYS", trigger = None)


## Cashflows


[qDurationType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L75)(duration_type: str)


[qRateAveragingType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L80)(averaging_type: str)


[qlSimpleCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L92)(amount: float, date: qDate, trigger = None)


[qlRedemption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L104)(amount: float, date: qDate, trigger = None)


[qlAmortizingPayment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L116)(amount: float, date: qDate, trigger = None)


[qlIndexedCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L132)(notional: float, index: ql.Index, base_date: qDate, fixing_date: qDate, payment_date: qDate, growth_only: bool = False, trigger = None)


[qlCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L151)(cashflow: ql.CashFlow, trigger = None)


[qlCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L162)(cashflow: ql.CashFlow, trigger = None)


[qlCashFlowHasOccurred](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L174)(cashflow: ql.CashFlow, ref_date: qDate = ql.Date(), trigger = None)


[qlAsIndexedCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L185)(cashflow: ql.CashFlow, trigger = None)


[qlAsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L196)(cashflow: ql.CashFlow, trigger = None)


[qlCouponNominal](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L207)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L218)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L229)(coupon: ql.Coupon, trigger = None)


[qlCouponReferencePeriodStart](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L240)(coupon: ql.Coupon, trigger = None)


[qlCouponReferencePeriodEnd](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L251)(coupon: ql.Coupon, trigger = None)


[qlCouponExCouponDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L262)(coupon: ql.Coupon, trigger = None)


[qlCouponRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L273)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L284)(coupon: ql.Coupon, trigger = None)


[qlCouponAccrualDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L295)(coupon: ql.Coupon, trigger = None)


[qlCouponDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L306)(coupon: ql.Coupon, trigger = None)


[qlCouponAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L318)(coupon: ql.Coupon, date: qDate, trigger = None)


[qlAsFixedRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L329)(cashflow: ql.CashFlow, trigger = None)


[qlAsFloatingRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L340)(cashflow: ql.CashFlow, trigger = None)


[qlFloatingRateCouponFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L351)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L362)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponIsInArrears](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L373)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponGearing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L384)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L395)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L406)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponAdjustedFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L417)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L428)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponPrice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L440)(coupon: ql.FloatingRateCoupon, discount_curve: ql.YieldTermStructureHandle, trigger = None)


[qlFloatingRateCouponIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L455)(coupon: ql.FloatingRateCoupon, trigger = None)


[qlFloatingRateCouponSetPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L467)(coupon: ql.FloatingRateCoupon, pricer: ql.FloatingRateCouponPricer, trigger = None)


[qlCappedFlooredCouponIsCapped](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L483)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponIsFloored](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L494)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponCap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L505)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L516)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponEffectiveCap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L527)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlCappedFlooredCouponEffectiveFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L538)(coupon: ql.CappedFlooredCoupon, trigger = None)


[qlOvernightIndexedCouponAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L549)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponCanApplyTelescopicFormula](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L560)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponApplyObservationShift](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L571)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponCompoundSpreadDaily](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L582)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponLockoutDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L593)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponRateComputationStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L604)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponRateComputationEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L615)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponValueDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L626)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponFixingDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L637)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponInterestDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L648)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponDt](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L659)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponIndexFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L670)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponEffectiveIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L681)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlOvernightIndexedCouponEffectiveSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L692)(coupon: ql.OvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponUnderlying](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L703)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponNakedOption](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L717)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponDailyCapFloor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L731)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponAveragingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L745)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponCompoundSpreadDaily](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L759)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponEffectiveCapletVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L773)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlCappedFlooredOvernightIndexedCouponEffectiveFloorletVolatility](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L787)(coupon: ql.CappedFlooredOvernightIndexedCoupon, trigger = None)


[qlAsOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L801)(cashflow: ql.CashFlow, trigger = None)


[qlAsCappedFlooredOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L812)(cashflow: ql.CashFlow, trigger = None)


[qlAsMultipleResetsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L823)(cashflow: ql.CashFlow, trigger = None)


[qlFixedRateCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L842)(payment_date: qDate, nominal: float, rate: float, day_counter: qDayCounter, start_date: qDate, end_date: qDate, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlIborCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L886)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlCappedFlooredIborCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L942)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, spread: float = 0.0, cap: float = ql.nullDouble(), floor: float = ql.nullDouble(), ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1001)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, overnight_index: ql.OvernightIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, lookback_days: int = ql.nullInt(), lockout_days: int = 0, apply_observation_shift: bool = False, compound_spread: bool = False, trigger = None)


[qlCappedFlooredOvernightIndexedCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1051)(underlying: ql.OvernightIndexedCoupon, cap: float = ql.nullDouble(), floor: float = ql.nullDouble(), naked_option: bool = False, daily_cap_floor: bool = False, trigger = None)


[qlCmsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1081)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.SwapIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlCmsSpreadCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1133)(payment_date: qDate, nominal: float, start_date: qDate, end_date: qDate, fixing_days: int, index: ql.SwapSpreadIndex, gearing: float = 1.0, spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), is_in_arrears: bool = False, ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlRangeAccrualFloatersCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1186)(payment_date: qDate, nominal: float, index: ql.IborIndex, start_date: qDate, end_date: qDate, fixing_days: int, day_counter: qDayCounter, gearing: float, spread: float, ref_period_start: qDate, ref_period_end: qDate, observations_schedule: ql.Schedule, lower_trigger: float, upper_trigger: float, trigger = None)


[qlMultipleResetsCoupon](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1239)(payment_date: qDate, nominal: float, reset_schedule: ql.Schedule, fixing_days: int, index: ql.IborIndex, gearing: float = 1.0, coupon_spread: float = 0.0, rate_spread: float = 0.0, ref_period_start: qDate = ql.Date(), ref_period_end: qDate = ql.Date(), day_counter: qDayCounter = ql.Actual365Fixed(), ex_coupon_date: qDate = ql.Date(), trigger = None)


[qlBlackIborCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1279)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), trigger = None)


[qlCompoundingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1290)(trigger = None)


[qlArithmeticAveragedOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1303)(mean_reversion: float = 0.03, volatility: float = 0.0, by_approx: bool = False, trigger = None)


[qlBlackCompoundingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1320)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), effective_volatility_input: bool = False, trigger = None)


[qlBlackAveragingOvernightIndexedCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1336)(volatility: ql.OptionletVolatilityStructureHandle = ql.OptionletVolatilityStructureHandle(), effective_volatility_input: bool = False, trigger = None)


[qlCompoundingMultipleResetsPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1348)(trigger = None)


[qlAveragingMultipleResetsPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1356)(trigger = None)


[qlSetCouponPricer](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1368)(leg: xlo.Array(dims=1), pricer: ql.FloatingRateCouponPricer, trigger = None)


[qlFixedRateLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1384)(schedule: ql.Schedule, day_counter: qDayCounter, nominals, coupon_rates, payment_adjustment: qBusinessDayConvention = ql.Following, trigger = None)


[qlIborLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1412)(nominals, schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, fixing_days = (), gearings = (), spreads = (), caps = (), floors = (), is_in_arrears: bool = False, trigger = None)


[qlOvernightLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1456)(nominals, schedule: ql.Schedule, index: ql.OvernightIndex, payment_day_counter: qDayCounter = ql.Actual360(), payment_convention: qBusinessDayConvention = ql.Following, gearings = (), spreads = (), telescopic_value_dates: bool = False, averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlCmsLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1492)(nominals, schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCmsZeroLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1514)(nominals, schedule: ql.Schedule, index: ql.SwapIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCmsSpreadLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1536)(nominals, schedule: ql.Schedule, index: ql.SwapSpreadIndex, payment_day_counter: qDayCounter = ql.Actual365Fixed(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlMultipleResetsLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1557)(full_reset_schedule: ql.Schedule, index: ql.IborIndex, resets_per_coupon: int, nominals, trigger = None)


[qlRangeAccrualLeg](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1578)(nominals, schedule: ql.Schedule, index: ql.IborIndex, payment_day_counter: qDayCounter = ql.Actual360(), payment_convention: qBusinessDayConvention = ql.Following, trigger = None)


[qlCashFlowsStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1596)(leg: xlo.Array(dims=1), trigger = None)


[qlCashFlowsMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1607)(leg: xlo.Array(dims=1), trigger = None)


[qlCashFlowsPreviousCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1620)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlowDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1638)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsPreviousCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1656)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlowAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1674)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsPreviousCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1692)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNextCashFlow](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1710)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccrualPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1728)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccrualDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1746)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1764)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1782)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAccruedAmount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1800)(leg: xlo.Array(dims=1), include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpv](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1820)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1842)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1867)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvFromZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1905)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, z_spread: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1941)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBpsFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1962)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBpsFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L1987)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsNpvBps](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2021)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsAtmRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2045)(leg: xlo.Array(dims=1), discount_curve: ql.YieldTermStructureHandle, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), npv: float = ql.nullDouble(), trigger = None)


[qlCashFlowsYieldRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2071)(leg: xlo.Array(dims=1), npv: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), accuracy: float = 1.0e-10, max_iterations: int = 10000, guess: float = 0.05, trigger = None)


[qlCashFlowsDurationFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2111)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, duration_type: qDurationType, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsDurationFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2135)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, duration_type: qDurationType, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsConvexityFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2172)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsConvexityFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2206)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBasisPointValueFromRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2229)(leg: xlo.Array(dims=1), _yield: float, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsBasisPointValueFromInterestRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2263)(leg: xlo.Array(dims=1), interest_rate: ql.InterestRate, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), trigger = None)


[qlCashFlowsZSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2287)(leg: xlo.Array(dims=1), npv: float, discount_curve: ql.YieldTermStructure, day_counter: qDayCounter, compounding: qCompounding, frequency: qFrequency, include_settlement_date_flows: bool, settlement_date: qDate = ql.Date(), npv_date: qDate = ql.Date(), accuracy: float = 1.0e-10, max_iterations: int = 100, guess: float = 0.0, trigger = None)


[qlDurationTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2325)(duration_type: qDurationType, trigger = None)


[qlRateAveragingTypeName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/cashflows.py#L2336)(averaging_type: qRateAveragingType, trigger = None)


## Currencies


[qCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L130)(code: str)


[qlCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L147)(name: str, code: str, numerical_code: int, symbol: str, fraction_symbol: str, fractions_per_unit: int, rounding: ql.Rounding, trigger = None)


[qlCurrencyName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L176)(currency: qCurrency, trigger = None)


[qlCurrencyCode](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L186)(currency: qCurrency, trigger = None)


[qlCurrencyNumericalCode](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L196)(currency: qCurrency, trigger = None)


[qlCurrencySymbol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L206)(currency: qCurrency, trigger = None)


[qlCurrencyFractionSymbol](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L216)(currency: qCurrency, trigger = None)


[qlCurrencyFractionsPerUnit](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L226)(currency: qCurrency, trigger = None)


[qlCurrencyRounding](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L236)(currency: qCurrency, trigger = None)


[qlCurrencyTriangulationCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/currencies.py#L246)(currency: qCurrency, trigger = None)


## Date


[qWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L62)(s: str)


[qFrequency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L66)(s: str)


[qTimeUnit](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L70)(s: str)


[qPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L74)(s: str)


[qlPeriod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L89)(n: int, unit: qTimeUnit, trigger = None)


[qlPeriodLength](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L99)(period: qPeriod, trigger = None)


[qlPeriodUnits](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L109)(period: qPeriod, trigger = None)


[qlPeriodFrequency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L119)(period: qPeriod, trigger = None)


[qlPeriodNormalized](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L129)(period: qPeriod, trigger = None)


[qDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L140)(serialnumber)


[qlDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L157)(year: int, month: int, day: int, trigger = None)


[qlDateWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L167)(date: qDate, trigger = None)


[qlDateDayOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L177)(date: qDate, trigger = None)


[qlDateDayOfYear](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L187)(date: qDate, trigger = None)


[qlDateMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L197)(date: qDate, trigger = None)


[qlDateYear](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L207)(date: qDate, trigger = None)


[qlDateIsLeap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L217)(year: int, trigger = None)


[qlDateMinDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L224)(trigger = None)


[qlDateMaxDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L231)(trigger = None)


[qlDateTodaysDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L238)(trigger = None)


[qlDateStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L247)(date: qDate, trigger = None)


[qlDateEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L256)(date: qDate, trigger = None)


[qlDateIsStartOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L265)(date: qDate, trigger = None)


[qlDateIsEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L274)(date: qDate, trigger = None)


[qlDateNextWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L284)(date: qDate, weekday: qWeekday, trigger = None)


[qlDateNthWeekday](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L296)(n: int, weekday: qWeekday, month: int, year: int, trigger = None)


[qlDateParserParseFormatted](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L307)(date_string: str, format_string: str, trigger = None)


[qlDateParserParseISO](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L316)(date_string: str, trigger = None)


[qlPeriodParserParse](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/date.py#L325)(period_string: str, trigger = None)


## Daycounters


[qDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L33)(s: str)


[qlDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L47)(daycounter_name: str, trigger = None)


[qlDayCounterDayCount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L59)(daycounter: qDayCounter, start_date: qDate, end_date: qDate, trigger = None)


[qlDayCounterYearFraction](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L74)(daycounter: qDayCounter, start_date: qDate, end_date: qDate, ref_start_date: qDate = ql.Date(), ref_end_date: qDate = ql.Date(), trigger = None)


[qlDayCounterName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L84)(daycounter: qDayCounter, trigger = None)


[qlDayCounterEmpty](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L93)(daycounter: qDayCounter, trigger = None)


[qlDayCounterYearFractionToDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/daycounters.py#L106)(daycounter: qDayCounter, ref_date: qDate, year_fraction: float, trigger = None)


## Indexes


[qlIndexManagerHistories](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L16)(trigger = None)


[qlIndexManagerClearHistories](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L23)(trigger = None)


[qlIndexName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L36)(index: ql.Index, trigger = None)


[qlIndexFixingCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L47)(index: ql.Index, trigger = None)


[qlIndexIsValidFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L59)(index: ql.Index, date: qDate, trigger = None)


[qlIndexHasHistoricalFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L71)(index: ql.Index, date: qDate, trigger = None)


[qlIndexFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L84)(index: ql.Index, date: qDate, forecast_todays_fixing = False, trigger = None)


[qlIndexPastFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L96)(index: ql.Index, date: qDate, trigger = None)


[qlIndexAddFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L110)(index: ql.Index, date: qDate, value: float, force_overwrite: bool = False, trigger = None)


[qlIndexAddFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L125)(index: ql.Index, dates: xlo.Array(dims=1), values: xlo.Array(dims=1), force_overwrite: bool = False, trigger = None)


[qlIndexTimeSeries](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L145)(index: ql.Index, trigger = None)


[qlIndexClearFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L156)(index: ql.Index, trigger = None)


[qlInterestRateIndexFamilyName](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L170)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L181)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L192)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexFixingDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L204)(index: ql.InterestRateIndex, value_date: qDate, trigger = None)


[qlInterestRateIndexCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L215)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L226)(index: ql.InterestRateIndex, trigger = None)


[qlInterestRateIndexMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L238)(index: ql.InterestRateIndex, value_date: qDate, trigger = None)


[qlInterestRateIndexValueDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L250)(index: ql.InterestRateIndex, fixing_date: qDate, trigger = None)


[qlIborIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L272)(family_name: str, tenor: qPeriod, settlement_days: int, currency: qCurrency, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, day_counter: qDayCounter, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCdor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L305)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlBbsw](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L316)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlBkbm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L327)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuribor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L338)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuribor365](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L349)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJibar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L360)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlMosprime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L371)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlNZDLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L382)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlPribor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L393)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlRobor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L404)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlShibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L415)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L426)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTHBFIX](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L437)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlWibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L448)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlZibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L459)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlAUDLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L470)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCADLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L481)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCHFLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L492)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlDKKLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L503)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEURLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L514)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlGBPLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L525)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJPYLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L536)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSEKLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L547)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTRLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L558)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlUSDLibor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L569)(tenor: qPeriod, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlOvernightIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L587)(family_name: str, settlement_days: int, currency: qCurrency, calendar: qCalendar, day_counter: qDayCounter, projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlAonia](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L612)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCdi](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L622)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlCorra](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L632)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlDestr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L642)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEonia](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L652)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEstr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L662)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlFedFunds](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L672)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlKofr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L682)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlNzocr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L692)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSaron](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L702)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSofr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L712)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSonia](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L722)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSwestr](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L732)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlTonar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L742)(projection_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSwapIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L764)(family_name: str, tenor: qPeriod, settlement_days: int, currency: qCurrency, calendar: qCalendar, fixed_leg_tenor: qPeriod, fixed_leg_convention: qBusinessDayConvention, fixed_leg_day_counter: qDayCounter, ibor_index: ql.IborIndex, discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuriborSwapIsdaFixA](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L812)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuriborSwapIsdaFixB](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L827)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEuriborSwapIfrFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L842)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEurLiborSwapIsdaFixA](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L857)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEurLiborSwapIsdaFixB](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L872)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlEurLiborSwapIfrFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L887)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlChfLiborSwapIsdaFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L902)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlGbpLiborSwapIsdaFix](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L917)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJpyLiborSwapIsdaFixAm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L932)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlJpyLiborSwapIsdaFixPm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L947)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlUsdLiborSwapIsdaFixAm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L962)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlUsdLiborSwapIsdaFixPm](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L977)(swap_tenor: qPeriod, proj_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), discount_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlSwapSpreadIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L997)(family_name: str, swap_index1: ql.SwapIndex, swap_index2: ql.SwapIndex, gearing1: float = 1.0, gearing2: float = -1.0, trigger = None)


[qlSwapIndexForecastFixing](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1015)(swap_index: ql.SwapIndex, fixing_date: qDate)


[qlEquityIndex](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/indexes.py#L1033)(name: str, fixing_calendar: qCalendar, currency: qCurrency, spot_price: float, disc_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), div_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


## Interpolatedyieldcurves


[qlInterpolatedYieldCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L62)(dates: xlo.Array(dims=1), discounts: xlo.Array(dims=1), daycounter: qDayCounter, calendar: qCalendar, traits: str, interpolator: str, mixed_interpolation_behavior: str = None, mixed_interpolation_n: int = None, trigger = None)


[qlDiscountCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L103)(dates: xlo.Array(dims=1), discounts: xlo.Array(dims=1), daycounter: qDayCounter = ql.Actual365Fixed(), calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlForwardCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L125)(dates: xlo.Array(dims=1), forwards: xlo.Array(dims=1), daycounter: qDayCounter = ql.Actual365Fixed(), calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlZeroCurve](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/interpolatedyieldcurves.py#L147)(dates: xlo.Array(dims=1), zerorates: xlo.Array(dims=1), daycounter: qDayCounter = ql.Actual365Fixed(), calendar: qCalendar = ql.NullCalendar(), trigger = None)


## Quantlib_


[qlVersion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/quantlib_.py#L12)(trigger = None)


[qlHexVersion](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/quantlib_.py#L20)(trigger = None)


## Ratehelpers


[qPillarChoice](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L28)(s: str)


[qFuturesType](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L35)(s: str)


[qQuoteHandle](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L39)(rate: str)


[qlRateHelperQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L57)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperLatestDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L67)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperEarliestDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L77)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperMaturityDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L87)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperLatestRelevantDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L97)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperPillarDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L107)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperImpliedQuote](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L118)(rate_helper: ql.RateHelper, trigger = None)


[qlRateHelperQuoteError](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L129)(rate_helper: ql.RateHelper, trigger = None)


[qlDepositRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L145)(rate: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, daycounter: qDayCounter, trigger = None)


[qlDepositRateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L173)(rate: qQuoteHandle, index: ql.IborIndex, trigger = None)


[qlDepositRateHelper3](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L192)(rate: qQuoteHandle, fixing_date: qDate, index: ql.IborIndex, trigger = None)


[qlFRARateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L221)(rate: qQuoteHandle, month_to_start: int, month_to_end: int, fixing_days: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, day_counter: qDayCounter, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L261)(rate: qQuoteHandle, month_to_start: int, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelper3](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L292)(rate: qQuoteHandle, imm_offset_start: int, imm_offset_end: int, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelper4](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L324)(rate: qQuoteHandle, period_to_start: qPeriod, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFRARateHelperForDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L356)(rate: qQuoteHandle, start_date: qDate, end_date: qDate, index: ql.IborIndex, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), use_indexed_coupon: bool = True, trigger = None)


[qlFuturesRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L391)(price: qQuoteHandle, ibor_start_date: qDate, n_months: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, day_counter: qDayCounter, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), type: qFuturesType = ql.IMM, trigger = None)


[qlFuturesRateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L427)(price: qQuoteHandle, ibor_start_date: qDate, ibor_end_date: qDate, day_counter: qDayCounter, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), type: qFuturesType = ql.IMM, trigger = None)


[qlFuturesRateHelper3](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L456)(price: qQuoteHandle, ibor_start_date: qDate, index: ql.IborIndex, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), type: qFuturesType = ql.IMM, trigger = None)


[qlFuturesRateConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L479)(futures_rate_helper: ql.FuturesRateHelper, trigger = None)


[qlSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L503)(rate: qQuoteHandle, tenor: qPeriod, calendar: qCalendar, fixed_frequency: qFrequency, fixed_convention: qBusinessDayConvention, fixed_daycount: qDayCounter, ibor_index: ql.IborIndex, spread: float = 0.0, fwd_start: qPeriod = ql.Period(0, ql.Days), discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), settlement_days: int = 0, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), end_of_month: bool = False, with_indexed_coupons: bool = False, trigger = None)


[qlSwapRateHelper2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L555)(rate: qQuoteHandle, index: ql.SwapIndex, spread: float = 0.0, fwd_start: qPeriod = ql.Period(0, ql.Days), discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), end_of_month: bool = False, with_indexed_coupons: bool = False, trigger = None)


[qlSwapRateForDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L602)(rate: qQuoteHandle, start_date: qDate, end_date: qDate, calendar: qCalendar, fixed_frequencies: qFrequency, business_day_convention: qBusinessDayConvention, day_counter: qDayCounter, index: ql.IborIndex, spread: float = 0.0, discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), pillar: ql.Pillar = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), end_of_month: bool = False, with_indexed_coupons: bool = False, trigger = None)


[qlSwapRateHelperSpread](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L643)(swap_rate_helper: ql.SwapRateHelper, trigger = None)


[qlSwapRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L653)(swap_rate_helper: ql.SwapRateHelper, trigger = None)


[qlOISRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L762)(settlement_days: int, tenor: qPeriod, fixed_rate: qQuoteHandle, overnight_index: ql.OvernightIndex, discounting_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), telescopic_value_dates: bool = False, payment_lag: int = 0, payment_convention: qBusinessDayConvention = ql.Following, payment_frequency: qFrequency = ql.Annual, payment_calendar: qCalendar = ql.NullCalendar, forward_start: qPeriod = ql.Period(0, ql.Days), overnight_spread: float = 0.0, pillar: qPillarChoice = ql.Pillar.LastRelevantDate, custom_pillar_date: qDate = ql.Date(), averaging_method: qRateAveragingType = ql.RateAveraging.Compound, end_of_month: bool = None, fixed_payment_frequency: qFrequency = ql.NoFrequency, fixed_calendar: qCalendar = ql.NullCalendar, look_back_days: int = 0, lock_out_days: int = 0, apply_observation_shift: bool = False, pricer: ql.FloatingRateCouponPricer = None, rule: qDateGenerationRule = ql.DateGeneration.Backward, overnight_calendar: qCalendar = ql.NullCalendar, convention: qBusinessDayConvention = ql.ModifiedFollowing, trigger = None)


[qlOISRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L912)(ois_rate_helper: ql.OISRateHelper, trigger = None)


[qlFxSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L932)(fwd_point: qQuoteHandle, spot_fx: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, business_day_convention: qBusinessDayConvention, end_of_month: bool, is_fx_base_currency_collateral_currency: bool, collateral_curve: ql.YieldTermStructureHandle, trading_calendar: qCalendar = ql.NullCalendar, trigger = None)


[qlFxSwapRateHelperForDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L971)(fwd_point: qQuoteHandle, spot_fx: qQuoteHandle, start_date: qDate, end_date: qDate, is_fx_base_currency_collateral_currency: bool, collateral_curve: ql.YieldTermStructureHandle = ql.YieldTermStructureHandle(), trigger = None)


[qlFxSwapRateHelperSpot](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L996)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1006)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperFixingDays](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1016)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1026)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1037)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1047)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperIsFxBaseCurrencyCollateralCurrency](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1057)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperTradingCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1067)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlFxSwapRateHelperAdjustmentCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1077)(fx_swap_rate_helper: ql.FxSwapRateHelper, trigger = None)


[qlOvernightIndexFutureRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1092)(price: qQuoteHandle, value_date: qDate, maturity_date: qDate, index: ql.OvernightIndex, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), averaging_method: qRateAveragingType = ql.RateAveraging.Compound, trigger = None)


[qlOvernightIndexFutureRateHelperConvexityAdjustment](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1117)(overnight_index_future_rate_helper: ql.OvernightIndexFutureRateHelper, trigger = None)


[qlSofrFutureRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1133)(price: qQuoteHandle, reference_month: int, reference_year: int, frequency: qFrequency, convexity_adjustment: qQuoteHandle = ql.QuoteHandle(), trigger = None)


[qlConstNotionalCrossCurrencySwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1167)(fixed_rate: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, fixed_frequency: qFrequency, fixed_day_count: qDayCounter, float_index: ql.IborIndex, collateral_curve: ql.YieldTermStructureHandle, collateral_on_fixed_leg: bool, payment_lag: int = 0, trigger = None)


[qlConstNotionalCrossCurrencyBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1216)(basis: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_currency_index: ql.IborIndex, quote_currency_index: ql.IborIndex, collateral_curve: ql.YieldTermStructureHandle, is_fx_base_currency_collateral_currency: bool, is_basis_on_fx_base_currency_leg: bool, payment_frequency: qFrequency = ql.NoFrequency, payment_lag: int = 0, trigger = None)


[qlMtMCrossCurrencyBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1268)(basis: qQuoteHandle, tenor: qPeriod, fixing_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_currency_index: ql.IborIndex, quote_currency_index: ql.IborIndex, collateral_curve: ql.YieldTermStructureHandle, is_fx_base_currency_collateral_currency: bool, is_basis_on_fx_base_currency_leg: bool, is_fx_base_currency_leg_resettable: bool, payment_frequency: qFrequency = ql.NoFrequency, payment_lag: int = 0, trigger = None)


[qlIborIborBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1318)(basis: qQuoteHandle, tenor: qPeriod, settlement_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_index: ql.IborIndex, other_index: ql.IborIndex, discount_handle: ql.YieldTermStructureHandle, bootstrap_base_curve: bool, trigger = None)


[qlIborIborBasisSwapRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1351)(ibor_ibor_basis_swap_rate_helper: ql.IborIborBasisSwapRateHelper, trigger = None)


[qlOvernightIborBasisSwapRateHelper](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1369)(basis: qQuoteHandle, tenor: qPeriod, settlement_days: int, calendar: qCalendar, convention: qBusinessDayConvention, end_of_month: bool, base_index: ql.IborIndex, other_index: ql.IborIndex, discount_handle: ql.YieldTermStructureHandle, trigger = None)


[qlOvernightIborBasisSwapRateHelperSwap](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/ratehelpers.py#L1400)(overnight_ibor_basis_swap_rate_helper: ql.OvernightIborBasisSwapRateHelper, trigger = None)


## Rounding


[qRoundingMethod](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/rounding.py#L24)(method: str)


[qlRounding](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/rounding.py#L37)(method: qRoundingMethod, precision: int, digit: int = 5, trigger = None)


[qlRoundingApply](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/rounding.py#L49)(rounding: ql.Rounding, value: float, trigger = None)


## Scheduler


[qDateGenerationRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L33)(rule: str)


[qlSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L53)(effective_date: qDate, termination_date: qDate, tenor: qPeriod, calendar: qCalendar, convention: qBusinessDayConvention, termination_date_convention: qBusinessDayConvention, date_generation_rule: qDateGenerationRule, end_of_month: bool, first_date: qDate = ql.Date(), last_date: qDate = ql.Date(), trigger = None)


[qlScheduleFromDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L89)(dates: xlo.Array(dims=1), calendar: qCalendar = ql.NullCalendar(), convention: qBusinessDayConvention = ql.Unadjusted, trigger = None)


[qlScheduleDates](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L110)(schedule: ql.Schedule, trigger = None)


[qlSchedulePreviousDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L122)(schedule: ql.Schedule, ref_date: qDate, trigger = None)


[qlScheduleNextDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L134)(schedule: ql.Schedule, ref_date: qDate, trigger = None)


[qlScheduleHasIsRegular](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L145)(schedule: ql.Schedule, trigger = None)


[qlScheduleIsRegular](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L157)(schedule: ql.Schedule, i: int, trigger = None)


[qlScheduleIsRegular2](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L168)(schedule: ql.Schedule, trigger = None)


[qlScheduleCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L179)(schedule: ql.Schedule, trigger = None)


[qlScheduleStartDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L190)(schedule: ql.Schedule, trigger = None)


[qlScheduleEndDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L201)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L212)(schedule: ql.Schedule, trigger = None)


[qlScheduleTenor](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L223)(schedule: ql.Schedule, trigger = None)


[qlScheduleBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L234)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasTerminationDateBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L245)(schedule: ql.Schedule, trigger = None)


[qlScheduleTerminationDateBusinessDayConvention](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L256)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L267)(schedule: ql.Schedule, trigger = None)


[qlScheduleRule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L278)(schedule: ql.Schedule, trigger = None)


[qlScheduleHasEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L289)(schedule: ql.Schedule, trigger = None)


[qlScheduleEndOfMonth](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L300)(schedule: ql.Schedule, trigger = None)


[qlScheduleAfter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L312)(schedule: ql.Schedule, truncation_date: qDate, trigger = None)


[qlScheduleUntil](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L324)(schedule: ql.Schedule, truncation_date: qDate, trigger = None)


[qlMakeSchedule](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/scheduler.py#L347)(effective_date = None, termination_date = None, tenor = None, frequency = None, calendar = None, convention = None, terminal_date_convention = None, rule = None, forwards = False, backwards = False, end_of_month = None, first_date = None, next_to_last_date = None, trigger = None)


## Settings


[qlSettingsGetEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L11)(trigger = None)


[qlSettingsSetEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L21)(date: qDate, trigger = None)


[qlSettingsGetEnforcesTodaysHistoricFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L29)(trigger = None)


[qlSettingsSetEnforcesTodaysHistoricFixings](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L39)(enforces: bool, trigger = None)


[qlSettingsGetIncludeReferenceDateEvents](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L47)(trigger = None)


[qlSettingsSetIncludeReferenceDateEvents](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L57)(include: bool, trigger = None)


[qlSettingsGetIncludeTodaysCashFlows](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L65)(trigger = None)


[qlSettingsSetIncludeTodaysCashFlows](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L75)(include: bool, trigger = None)


[qlSettingsAnchorEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L83)(trigger = None)


[qlSettingsResetEvaluationDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/settings.py#L91)(trigger = None)


## Termstructures


[qlTermStructureDayCounter](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L21)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureTimeFromReference](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L32)(ytsh: ql.YieldTermStructureHandle, date: qDate, trigger = None)


[qlTermStructureCalendar](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L42)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureReferenceDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L52)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureMaxDate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L62)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureMaxTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L72)(ytsh: ql.YieldTermStructureHandle)


[qlTermStructureEnableExrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L82)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureDisableExrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L93)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qlTermStructureAllowsExtrapolation](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L104)(ytsh: ql.YieldTermStructureHandle, trigger = None)


[qCompounding](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L124)(compounding: str)


[qlYieldTermStructureDiscount](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L136)(ytsh: ql.YieldTermStructureHandle, date: qDate, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureDiscountFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L153)(ytsh: ql.YieldTermStructureHandle, time: float, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureZeroRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L173)(ytsh: ql.YieldTermStructureHandle, date: qDate, daycounter: qDayCounter, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureZeroRateFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L195)(ytsh: ql.YieldTermStructureHandle, time: float, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureForwardRate](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L218)(ytsh: ql.YieldTermStructureHandle, date1: qDate, date2: qDate, daycounter: qDayCounter, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlYieldTermStructureForwardRateFromTime](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L242)(ytsh: ql.YieldTermStructureHandle, time1: float, time2: float, compounding: qCompounding, frequency: qFrequency, extrapolate: bool = False, trigger = None)


[qlFlatForward](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L268)(reference_date: qDate, forward_rate: float, daycounter: qDayCounter = ql.Actual365Fixed(), compounding: qCompounding = ql.Compounded, frequency: qFrequency = ql.NoFrequency, calendar: qCalendar = ql.NullCalendar(), trigger = None)


[qlImpliedTermStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L291)(ytsh: ql.YieldTermStructureHandle, reference_date: qDate, trigger = None)


[qlZeroSpreadedTermStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L312)(base: ql.YieldTermStructureHandle, spread: float, compounding: qCompounding = ql.Compounded, frequency: qFrequency = ql.NoFrequency, daycounter: qDayCounter = ql.Actual365Fixed(), trigger = None)


[qlForwardSpreadedTermStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L333)(base: ql.YieldTermStructureHandle, spread: float, trigger = None)


[qlCompositeZeroYieldStructure](https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/termstructures.py#L357)(curve1: ql.YieldTermStructureHandle, curve2: ql.YieldTermStructureHandle, operator: str, trigger = None)


