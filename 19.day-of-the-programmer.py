
def is_leap(type_calendar, year):
    #leap = False
    if type_calendar == 'julian':
        if year % 4 == 0:
            leap = True
    elif type_calendar == 'gregorian':
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                leap = True
            elif year % 100 != 0 and year % 400 != 0:
                leap = True
            elif year % 100 != 0 and year % 400 == 0:
                leap = False
    return leap


def dayOfProgrammer(year):
    monthsYear = {
        "January": 31,
        "February": 29,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    sumDays = 0
    monthRequired = 0
    wantedDay = 0
    dayProgrammer = 256
    if year >= 1700 and year <= 1917:
        typeYear = is_leap('julian', year)
        return f'Julian year is {typeYear} = {year}'
    elif year >= 1919 and year <= 2700:
        typeYear = is_leap('gregorian', year)
        for month in monthsYear:
            print(f'month: {month}  ----->  days: {monthsYear[month]}')

        return f'Gregorian year {typeYear} = {year}'


year = 2016
diaProgra = dayOfProgrammer(year)
print(diaProgra)
