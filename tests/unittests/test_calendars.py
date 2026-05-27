from quantlib_xloil.date import qPeriod, qlPeriod


def test_qCalendar():
    from quantlib_xloil.calendars import _qCalendar
    calendar = _qCalendar("TARGET")
    assert calendar is not None

def test_qBusinessDayConvention():
    from quantlib_xloil.calendars import _qBusinessDayConvention
    convention = _qBusinessDayConvention("Following")
    assert convention is not None

def test_qJointCalendarRule():
    from quantlib_xloil.calendars import _qJointCalendarRule
    rule = _qJointCalendarRule("JOINHOLIDAYS")
    assert rule is not None

def test_qlCalenndar_Argentina():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Argentina")
    assert calendar is not None

def test_qlCalendar_Australia():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Australia")
    assert calendar is not None 

def test_qlCalendar_Botswana():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Botswana")
    assert calendar is not None

def test_qlCalendar_Brazil():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Brazil")
    assert calendar is not None

def test_qlCalendar_Canada():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Canada")
    assert calendar is not None 

def test_qlCalendar_Chile():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Chile")
    assert calendar is not None

def test_qlCalendar_China():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("China")
    assert calendar is not None

def test_qlCalendar_CzechRepublic():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("CzechRepublic")
    assert calendar is not None

def test_qlCalendar_Denmark():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Denmark")
    assert calendar is not None

def test_qlCalendar_Finland():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Finland")
    assert calendar is not None

def test_qlCalendar_France():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("France")
    assert calendar is not None

def test_qlCalendar_Germany():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Germany")
    assert calendar is not None 

def test_qlCalendar_HongKong():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("HongKong")
    assert calendar is not None 

def test_qlCalendar_Hungary():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Hungary")
    assert calendar is not None 

def test_qlCalendar_Iceland():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Iceland")
    assert calendar is not None

def test_qlCalendar_India():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("India")
    assert calendar is not None 

def test_qlCalendar_Indonesia():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Indonesia")
    assert calendar is not None

def test_qlCalendar_Israel():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Israel")
    assert calendar is not None

def test_qlCalendar_Italy():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Italy")
    assert calendar is not None 

def test_qlCalendar_Japan():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Japan")
    assert calendar is not None

def test_qlCalendar_Mexico():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Mexico")
    assert calendar is not None

def test_qlCalendar_Newzealand():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("NewZealand")
    assert calendar is not None

def test_qlCalendar_Norway():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Norway")
    assert calendar is not None

def test_qlCalendar_Poland():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Poland")
    assert calendar is not None     

def test_qlCalendar_Romania():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Romania")
    assert calendar is not None

def test_qlCalendar_Russia():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Russia")
    assert calendar is not None

def test_qlCalendar_SaudiArabia():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("SaudiArabia")
    assert calendar is not None

def test_qlCalendar_Singapore():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Singapore")
    assert calendar is not None

def test_qlCalendar_Singapore():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("SouthAfrica")
    assert calendar is not None

def test_qlCalendar_Slovakia():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Slovakia")
    assert calendar is not None

def test_qlCalendar_SouthAfrica():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("SouthAfrica")
    assert calendar is not None

def test_qlCalendar_SouthKorea():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("SouthKorea")
    assert calendar is not None

def test_qlCalendar_Sweden():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Sweden")
    assert calendar is not None

def test_qlCalendar_Switzerland():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Switzerland")
    assert calendar is not None

def test_qlCalendar_Taiwan():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Taiwan")
    assert calendar is not None

def test_qlCalendar_Target():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("TARGET")
    assert calendar is not None

def test_qlCalendar_Thailand():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Thailand")
    assert calendar is not None 

def test_qlCalendar_Turkey():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Turkey")
    assert calendar is not None

def test_qlCalendar_Ukraine():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Ukraine")
    assert calendar is not None

'''
def test_qlCalendar_UnitedStates():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("UNITEDSTATES")
    assert calendar is not None
'''
    
def test_qlCalendar_UnitedKingdom():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("UnitedKingdom")
    assert calendar is not None

def test_qlCalendar_NullCalendar():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("NullCalendar")
    assert calendar is not None

def test_qlCalendar_Weekendsonly():
    from quantlib_xloil.calendars import qlCalendar
    calendar = qlCalendar("Weekendsonly")
    assert calendar is not None 

def test_qlCalendarisWeekend():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarisWeekend
    from quantlib_xloil.date import qlDateWeekday, qlDate, qWeekday
    calendar = qlCalendar("TARGET") 
    date = qlDate(2026,5,29) #This is a Friday 
    weekday = qlDateWeekday(date)    
    assert qlCalendarisWeekend(calendar, qWeekday.__wrapped__(weekday)) == False

def test_qlCalendarStartOfMonth():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarStartOfMonth
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29)
    assert qlCalendarStartOfMonth(calendar, date) == qlDate(2026,5,4)

def test_qlCalendarEndOfMonth():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarEndOfMonth
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29)
    assert qlCalendarEndOfMonth(calendar, date) == qlDate(2026,5,29)

def test_qlCalendarIsBusinessDay():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarIsBusinessDay
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) #This is a Friday 
    assert qlCalendarIsBusinessDay(calendar, date) == True    

def test_qlClendarIsHoliday():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarIsHoliday
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsHoliday(calendar, date) == False

def test_qlCalendarIsEndOfMonth():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarIsEndOfMonth
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsEndOfMonth(calendar, date) == True

def test_qlCalendarIsStartOfMonth():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarIsStartOfMonth
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsStartOfMonth(calendar, date) == False

def test_qlCalendarHolidayList():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarHolidayList
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date_from =qlDate(2026,1,1)
    date_to = qlDate(2026,1,5)    
    holidays = qlCalendarHolidayList(calendar, date_from, date_to)
    assert holidays == [qlDate(2026,1,1)] 

def test_qlCalendarBusinessDayList():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarBusinessDayList
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date_from =qlDate(2026,1,1)
    date_to = qlDate(2026,1,5)    
    business_days = qlCalendarBusinessDayList(calendar, date_from, date_to)
    assert business_days == [qlDate(2026,1,2), qlDate(2026,1,5)] 

def test_qlCalendarAddHoliday():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarAddHoliday, qlCalendarIsHoliday, qlCalendarResetAddedAndRemovedHolidays
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsHoliday(calendar, date) == False
    qlCalendarAddHoliday(calendar, date)
    assert qlCalendarIsHoliday(calendar, date) == True
    qlCalendarResetAddedAndRemovedHolidays(calendar)

def test_qlCalendarRemoveHoliday():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarRemoveHoliday, qlCalendarIsHoliday, qlCalendarResetAddedAndRemovedHolidays
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,1) 
    assert qlCalendarIsHoliday(calendar, date) == True
    qlCalendarRemoveHoliday(calendar, date)
    assert qlCalendarIsHoliday(calendar, date) == False
    qlCalendarResetAddedAndRemovedHolidays(calendar)

def test_qlCalendarResetAddedAndRemovedHolidays():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarAddHoliday, qlCalendarResetAddedAndRemovedHolidays, qlCalendarIsHoliday, qlCalendarRemoveHoliday
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date_added = qlDate(2026,5,29) 
    date_removed = qlDate(2026,1,1) 
    assert qlCalendarIsHoliday(calendar, date_added) == False
    assert qlCalendarIsHoliday(calendar, date_removed) == True
    qlCalendarAddHoliday(calendar, date_added)
    qlCalendarRemoveHoliday(calendar, date_removed)
    assert qlCalendarIsHoliday(calendar, date_added) == True
    assert qlCalendarIsHoliday(calendar, date_removed) == False
    qlCalendarResetAddedAndRemovedHolidays(calendar)
    assert qlCalendarIsHoliday(calendar, date_added) == False
    assert qlCalendarIsHoliday(calendar, date_removed) == True


def test_qlCalendarAdjust():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarAdjust, qBusinessDayConvention
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,31) #This is a Saturday
    convention = qBusinessDayConvention.__wrapped__("Following")
    adjusted_date = qlCalendarAdjust(calendar, date, convention)
    assert adjusted_date == qlDate(2026,2,2) #This is the following Monday

def test_qlCalendarAdvance():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarAdvance, qBusinessDayConvention, qTimeUnit
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,31) #This is a Saturday
    n = 10
    unit = qTimeUnit.__wrapped__("DAYS")
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance(calendar, date, n, unit, convention)
    assert advanced_date == qlDate(2026,2,13)

def test_qlCalendarAdvance2():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarAdvance2, qBusinessDayConvention
    from quantlib_xloil.date import qlDate, qlPeriod
    import QuantLib as ql
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,31) #This is a Saturday
    period = qlPeriod(3, ql.Months)
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance2(calendar, date, period, convention)
    assert advanced_date == qlDate(2026,4,30)

def test_qlCalendarBusinessDaysBetween():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarBusinessDaysBetween
    from quantlib_xloil.date import qlDate
    calendar = qlCalendar("TARGET")
    from_date = qlDate(2026,1,1) 
    to_date = qlDate(2026,1,5) 
    assert qlCalendarBusinessDaysBetween(calendar, from_date, to_date) == 1
    assert qlCalendarBusinessDaysBetween(calendar, from_date, to_date, True, True) == 2

def test_qlCalendarName():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarName
    calendar = qlCalendar("TARGET")
    assert qlCalendarName(calendar) == "TARGET"

def test_qlCalendarEmpty():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarEmpty
    calendar = qlCalendar("TARGET")
    assert qlCalendarEmpty(calendar) == False

def test_qlCalendarJointCalendar():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarJointCalendar, qJointCalendarRule
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    rule = qJointCalendarRule.__wrapped__("JOINHOLIDAYS")
    joint_calendar = qlCalendarJointCalendar(calendar1, calendar2, rule)
    assert joint_calendar is not None

def test_qlCalendarJointCalendar2():
    from quantlib_xloil.calendars import qlCalendar, qlCalendarJointCalendar
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    calendar3 = qlCalendar("Sweden")
    joint_calendar = qlCalendarJointCalendar(calendar1, calendar2, calendar3)
    assert joint_calendar is not None