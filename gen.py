from datetime import timedelta,datetime,date

def gen(startDate, endDate, step=timedelta(days=1), inclusive=True):
    sdate = datetime.strptime(startDate, '%d.%m.%Y')
    edate = datetime.strptime(endDate, '%d.%m.%Y')
    if step.days > 0:
        while sdate < edate:
            sdate = sdate + step
            yield sdate
    if inclusive and sdate == edate:
        yield sdate