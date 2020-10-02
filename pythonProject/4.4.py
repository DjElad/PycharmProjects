def gen_secs():
    i = 0
    while i < 60:
        yield i
        i += 1


def gen_minutes():
    i = 0
    while i < 60:
        yield i
        i += 1


def gen_hours():
    i = 0
    while i < 24:
        yield i
        i += 1


def gen_time():
    for hh in gen_hours():
        for mm in gen_minutes():
            for ss in gen_secs():
                yield "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)


def gen_years(start=2019):
    yield start
    while start < 2100:
        start += 1
        yield start


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month == 2:
        if leap_year:
            for day in range(1, 30):
                yield day
        else:
            for day in range(1, 29):
                yield day
    elif month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        for day in range(1, 32):
            yield day
    elif month == (4 or 6 or 9 or 11):
        for day in range(1, 31):
            yield day


def gen_date():
    for year in gen_years():
        if year % 4 == 0 and not year % 100 == 0:
            leap_year = True
        else:
            leap_year = False
        for month in gen_months():
            for day in gen_days(month, leap_year):
                date = "{:02d}:{:02d}:{:02d}".format(day, month, year)
                for time in gen_time():
                    yield date, time


dates = gen_date()
count = 0
for i in dates:
    count += 1
    if count % 1000000 == 0:
        print(i)
