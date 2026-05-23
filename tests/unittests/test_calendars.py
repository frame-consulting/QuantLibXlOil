from quantlibxloil.date import qPeriod, qlPeriod


def test_qCalendar():
    from quantlibxloil.calendars import _qCalendar
    calendar = _qCalendar("TARGET")
    assert calendar is not None

def test_qBusinessDayConvention():
    from quantlibxloil.calendars import _qBusinessDayConvention
    convention = _qBusinessDayConvention("Following")
    assert convention is not None

def test_qJointCalendarRule():
    from quantlibxloil.calendars import _qJointCalendarRule
    rule = _qJointCalendarRule("JOINHOLIDAYS")
    assert rule is not None

def test_qlCalenndar_Argentina():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Argentina")
    assert calendar is not None

def test_qlCalendar_Australia():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Australia")
    assert calendar is not None 

def test_qlCalendar_Botswana():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Botswana")
    assert calendar is not None

def test_qlCalendar_Brazil():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Brazil")
    assert calendar is not None

def test_qlCalendar_Canada():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Canada")
    assert calendar is not None 

def test_qlCalendar_Chile():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Chile")
    assert calendar is not None

def test_qlCalendar_China():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("China")
    assert calendar is not None

def test_qlCalendar_CzechRepublic():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("CzechRepublic")
    assert calendar is not None

def test_qlCalendar_Denmark():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Denmark")
    assert calendar is not None

def test_qlCalendar_Finland():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Finland")
    assert calendar is not None

def test_qlCalendar_France():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("France")
    assert calendar is not None

def test_qlCalendar_Germany():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Germany")
    assert calendar is not None 

def test_qlCalendar_HongKong():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("HongKong")
    assert calendar is not None 

def test_qlCalendar_Hungary():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Hungary")
    assert calendar is not None 

def test_qlCalendar_Iceland():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Iceland")
    assert calendar is not None

def test_qlCalendar_India():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("India")
    assert calendar is not None 

def test_qlCalendar_Indonesia():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Indonesia")
    assert calendar is not None

def test_qlCalendar_Israel():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Israel")
    assert calendar is not None

def test_qlCalendar_Italy():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Italy")
    assert calendar is not None 

def test_qlCalendar_Japan():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Japan")
    assert calendar is not None

def test_qlCalendar_Mexico():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Mexico")
    assert calendar is not None

def test_qlCalendar_Newzealand():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("NewZealand")
    assert calendar is not None

def test_qlCalendar_Norway():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Norway")
    assert calendar is not None

def test_qlCalendar_Poland():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Poland")
    assert calendar is not None     

def test_qlCalendar_Romania():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Romania")
    assert calendar is not None

def test_qlCalendar_Russia():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Russia")
    assert calendar is not None

def test_qlCalendar_SaudiArabia():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("SaudiArabia")
    assert calendar is not None

def test_qlCalendar_Singapore():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Singapore")
    assert calendar is not None

def test_qlCalendar_Singapore():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("SouthAfrica")
    assert calendar is not None

def test_qlCalendar_Slovakia():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Slovakia")
    assert calendar is not None

def test_qlCalendar_SouthAfrica():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("SouthAfrica")
    assert calendar is not None

def test_qlCalendar_SouthKorea():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("SouthKorea")
    assert calendar is not None

def test_qlCalendar_Sweden():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Sweden")
    assert calendar is not None

def test_qlCalendar_Switzerland():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Switzerland")
    assert calendar is not None

def test_qlCalendar_Taiwan():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Taiwan")
    assert calendar is not None

def test_qlCalendar_Target():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("TARGET")
    assert calendar is not None

def test_qlCalendar_Thailand():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Thailand")
    assert calendar is not None 

def test_qlCalendar_Turkey():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Turkey")
    assert calendar is not None

def test_qlCalendar_Ukraine():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Ukraine")
    assert calendar is not None

'''
def test_qlCalendar_UnitedStates():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("UNITEDSTATES")
    assert calendar is not None
'''
    
def test_qlCalendar_UnitedKingdom():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("UnitedKingdom")
    assert calendar is not None

def test_qlCalendar_NullCalendar():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("NullCalendar")
    assert calendar is not None

def test_qlCalendar_Weekendsonly():
    from quantlibxloil.calendars import qlCalendar
    calendar = qlCalendar("Weekendsonly")
    assert calendar is not None 

def test_qlCalendarisWeekend():
    from quantlibxloil.calendars import qlCalendar, qlCalendarisWeekend
    from quantlibxloil.date import qlDateWeekday, qlDate, qWeekday
    calendar = qlCalendar("TARGET") 
    date = qlDate(2026,5,29) #This is a Friday 
    weekday = qlDateWeekday(date)    
    assert qlCalendarisWeekend(calendar, qWeekday.__wrapped__(weekday)) == False

def test_qlCalendarStartOfMonth():
    from quantlibxloil.calendars import qlCalendar, qlCalendarStartOfMonth
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29)
    assert qlCalendarStartOfMonth(calendar, date) == qlDate(2026,5,4)

def test_qlCalendarEndOfMonth():
    from quantlibxloil.calendars import qlCalendar, qlCalendarEndOfMonth
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29)
    assert qlCalendarEndOfMonth(calendar, date) == qlDate(2026,5,29)

def test_qlCalendarIsBusinessDay():
    from quantlibxloil.calendars import qlCalendar, qlCalendarIsBusinessDay
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) #This is a Friday 
    assert qlCalendarIsBusinessDay(calendar, date) == True    

def test_qlClendarIsHoliday():
    from quantlibxloil.calendars import qlCalendar, qlCalendarIsHoliday
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsHoliday(calendar, date) == False

def test_qlCalendarIsEndOfMonth():
    from quantlibxloil.calendars import qlCalendar, qlCalendarIsEndOfMonth
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsEndOfMonth(calendar, date) == True

def test_qlCalendarIsStartOfMonth():
    from quantlibxloil.calendars import qlCalendar, qlCalendarIsStartOfMonth
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsStartOfMonth(calendar, date) == False

def test_qlCalendarHolidayList():
    from quantlibxloil.calendars import qlCalendar, qlCalendarHolidayList
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date_from =qlDate(2026,1,1)
    date_to = qlDate(2026,1,5)    
    holidays = qlCalendarHolidayList(calendar, date_from, date_to)
    assert holidays == [qlDate(2026,1,1)] 

def test_qlCalendarBusinessDayList():
    from quantlibxloil.calendars import qlCalendar, qlCalendarBusinessDayList
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date_from =qlDate(2026,1,1)
    date_to = qlDate(2026,1,5)    
    business_days = qlCalendarBusinessDayList(calendar, date_from, date_to)
    assert business_days == [qlDate(2026,1,2), qlDate(2026,1,5)] 

def test_qlCalendarAddHoliday():
    from quantlibxloil.calendars import qlCalendar, qlCalendarAddHoliday, qlCalendarIsHoliday, qlCalendarResetAddedAndRemovedHolidays
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,5,29) 
    assert qlCalendarIsHoliday(calendar, date) == False
    qlCalendarAddHoliday(calendar, date)
    assert qlCalendarIsHoliday(calendar, date) == True
    qlCalendarResetAddedAndRemovedHolidays(calendar)

def test_qlCalendarRemoveHoliday():
    from quantlibxloil.calendars import qlCalendar, qlCalendarRemoveHoliday, qlCalendarIsHoliday, qlCalendarResetAddedAndRemovedHolidays
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,1) 
    assert qlCalendarIsHoliday(calendar, date) == True
    qlCalendarRemoveHoliday(calendar, date)
    assert qlCalendarIsHoliday(calendar, date) == False
    qlCalendarResetAddedAndRemovedHolidays(calendar)

def test_qlCalendarResetAddedAndRemovedHolidays():
    from quantlibxloil.calendars import qlCalendar, qlCalendarAddHoliday, qlCalendarResetAddedAndRemovedHolidays, qlCalendarIsHoliday, qlCalendarRemoveHoliday
    from quantlibxloil.date import qlDate
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
    from quantlibxloil.calendars import qlCalendar, qlCalendarAdjust, qBusinessDayConvention
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,31) #This is a Saturday
    convention = qBusinessDayConvention.__wrapped__("Following")
    adjusted_date = qlCalendarAdjust(calendar, date, convention)
    assert adjusted_date == qlDate(2026,2,2) #This is the following Monday

def test_qlCalendarAdvance():
    from quantlibxloil.calendars import qlCalendar, qlCalendarAdvance, qBusinessDayConvention, qTimeUnit
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,31) #This is a Saturday
    n = 10
    unit = qTimeUnit.__wrapped__("DAYS")
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance(calendar, date, n, unit, convention)
    assert advanced_date == qlDate(2026,2,13)

def test_qlCalendarAdvance2():
    from quantlibxloil.calendars import qlCalendar, qlCalendarAdvance2, qBusinessDayConvention
    from quantlibxloil.date import qlDate, qlPeriod
    import QuantLib as ql
    calendar = qlCalendar("TARGET")
    date = qlDate(2026,1,31) #This is a Saturday
    period = qlPeriod(3, ql.Months)
    convention = qBusinessDayConvention.__wrapped__("Following")
    advanced_date = qlCalendarAdvance2(calendar, date, period, convention)
    assert advanced_date == qlDate(2026,4,30)

def test_qlCalendarBusinessDaysBetween():
    from quantlibxloil.calendars import qlCalendar, qlCalendarBusinessDaysBetween
    from quantlibxloil.date import qlDate
    calendar = qlCalendar("TARGET")
    from_date = qlDate(2026,1,1) 
    to_date = qlDate(2026,1,5) 
    assert qlCalendarBusinessDaysBetween(calendar, from_date, to_date) == 1
    assert qlCalendarBusinessDaysBetween(calendar, from_date, to_date, True, True) == 2

def test_qlCalendarName():
    from quantlibxloil.calendars import qlCalendar, qlCalendarName
    calendar = qlCalendar("TARGET")
    assert qlCalendarName(calendar) == "TARGET"

def test_qlCalendarEmpty():
    from quantlibxloil.calendars import qlCalendar, qlCalendarEmpty
    calendar = qlCalendar("TARGET")
    assert qlCalendarEmpty(calendar) == False

def test_qlCalendarJointCalendar():
    from quantlibxloil.calendars import qlCalendar, qlCalendarJointCalendar, qJointCalendarRule
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    rule = qJointCalendarRule.__wrapped__("JOINHOLIDAYS")
    joint_calendar = qlCalendarJointCalendar(calendar1, calendar2, rule)
    assert joint_calendar is not None

def test_qlCalendarJointCalendar2():
    from quantlibxloil.calendars import qlCalendar, qlCalendarJointCalendar
    calendar1 = qlCalendar("TARGET")
    calendar2 = qlCalendar("UnitedKingdom")
    calendar3 = qlCalendar("Sweden")
    joint_calendar = qlCalendarJointCalendar(calendar1, calendar2, calendar3)
    assert joint_calendar is not None