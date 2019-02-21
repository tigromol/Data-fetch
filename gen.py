from datetime import timedelta, datetime, date
import calendar

def gen_next_day(startDate, endDate, step=1):
    sdate = datetime.strptime(startDate, '%d.%m.%Y')
    edate = datetime.strptime(endDate, '%d.%m.%Y')
    while sdate < edate:
        sdate = sdate + timedelta(days=step)
        yield sdate

def gen_next_month(start_date, end_date, step=1):
    sdate = datetime.strptime(start_date, '%d.%m.%Y')
    edate = datetime.strptime(end_date, '%d.%m.%Y')
    while sdate < edate:
        sdate = add_month(sdate, step)
        yield sdate

def add_month(orig_date, count):
    new_year = orig_date.year
    new_month = orig_date.month + count
    if new_month > 12:
        new_year += 1
        new_month -= 12

    last_day_of_month = calendar.monthrange(new_year, new_month)[1]
    new_day = min(orig_date.day, last_day_of_month)

    return orig_date.replace(year=new_year, month=new_month, day=new_day)