from datetime import datetime, timedelta
from calendar import monthrange
from dateutil.relativedelta import relativedelta

def get_trimesters(actual_date:  datetime = datetime.now(), should_include_list = False):
    if(should_include_list):
        return get_all_trimesters(actual_date)
    else: 
        return get_trimester_limit(actual_date)

def get_semesters(actual_date:  datetime = datetime.now(), should_include_list = False):
    if(should_include_list):
        return get_all_semesters(actual_date)
    else: 
        return get_semester_limit(actual_date)

def get_months(actual_date:  datetime = datetime.now(), should_include_list = False):
    if(should_include_list):
        return get_all_months(actual_date)
    else: 
        return get_month_limit(actual_date)

def get_weeks(actual_date:  datetime = datetime.now(), should_include_list = False):
    if(should_include_list):
        return get_all_weeks(actual_date)
    else: 
        return get_week_limit(actual_date)

def get_days(actual_date:  datetime = datetime.now(), should_include_list = False):
    return get_day_limit(actual_date)

def get_all_months(actual_date:  datetime = datetime.now()):
    actual_month = get_month_limit(actual_date)
    actual_date = actual_month[0] - timedelta(days= 1)
    past_year = actual_month[0] - relativedelta(years= 1)
    res = [actual_month]
    while(actual_date > past_year):
        actual_month = get_month_limit(actual_date)
        actual_date = actual_month[0] - timedelta(days= 1)
        res.append(actual_month)
    return res

def get_all_weeks(actual_date:  datetime = datetime.now()):
    print(actual_date)
    actual_week = get_week_limit(actual_date)
    print(actual_week)
    actual_date = actual_week[0] - timedelta(days= 1)
    past_year = actual_week[0] - relativedelta(years= 1)
    res = [actual_week]
    while(actual_date > past_year):
        actual_week = get_week_limit(actual_date)
        print(actual_week)
        actual_date = actual_week[0] - timedelta(days= 1)
        print(actual_date)
        res.append(actual_week)
    return res

def get_day_limit(actual_date:  datetime = datetime.now()):
    intial_date = datetime(
        actual_date.year, actual_date.month, actual_date.day, 0, 0, 0)
    final_date = datetime(
        actual_date.year, actual_date.month, actual_date.day, 23, 59, 59)
    return intial_date, final_date


def get_semester_limit(actual_date:  datetime = datetime.now()):
    month = actual_date.month
    if(month < 7):
        initial_date = datetime(actual_date.year, 1, 1, 0, 0, 0)
        date_range = monthrange(actual_date.year, 6)
        final_date = datetime(actual_date.year, 6,  date_range[1], 23, 59, 59)
        return initial_date, final_date
    else:
        initial_date = datetime(actual_date.year, 7, 1, 0, 0, 0)
        final_date = datetime(actual_date.year, 12,  31, 23, 59, 59)
        return initial_date, final_date

def get_all_semesters(actual_date:  datetime = datetime.now()):
    actual_semester = get_semester_limit(actual_date)
    last_day_of_past =actual_semester[0] + timedelta(-1)
    past_semester  = get_semester_limit(last_day_of_past)
    return actual_semester, past_semester

def get_month_limit(actual_date:  datetime = datetime.now()):
    year = actual_date.year
    month = actual_date.month
    date_range = monthrange(year, month)
    initial_date = datetime(year, month, 1, 0, 0, 0)
    final_date = datetime(year, month, date_range[1], 23, 59, 59)
    return initial_date, final_date


def get_week_limit(actual_date:  datetime = datetime.now()):
    week = actual_date.isocalendar()[1]
    year = actual_date.year
    if(week == 53):
        week = 52
        year -=1
    initial_date = datetime.fromisocalendar(year, week, 1)
    final_date = datetime.fromisocalendar(year, week, 7)
    return initial_date, final_date


def get_trimester_limit(actual_date:  datetime = datetime.now()):
    actual_trimester = get_trimester_number_from_date(actual_date)
    year = actual_date.year
    return get_trimester(actual_trimester, year)


def get_all_trimesters(actual_date:  datetime = datetime.now()):
    actual_trimester = get_trimester_number_from_date(actual_date)
    year = actual_date.year
    res = [get_trimester(actual_trimester, year)]
    for _ in range(4):
        h = get_past_trimester(actual_date)
        actual_date = h[0]
        res.append(h)
    return res


def get_trimester_number_from_date(actual_date:  datetime):
    acutal_month = actual_date.month
    return int((acutal_month-1)/3 + 1)


def get_past_trimester(actual_date:  datetime):
    actual_trimester = get_trimester_number_from_date(actual_date)
    year = actual_date.year
    past_trimester = actual_trimester - 1
    if(past_trimester == 0):
        past_trimester = 4
        year -= 1
    return get_trimester(past_trimester, year)


def get_trimester(number, year):
    number = number - 1
    initial_date = datetime(year, 1 + (number * 3), 1, 0, 0, 0)
    final = 3 + (number * 3)
    date_range = monthrange(year, final)
    final_date = datetime(year, final, date_range[1], 23, 59, 59)
    return initial_date, final_date

def parse_date(date, f="%Y-%m-%d"):
    date = str(date).replace('"', '').replace("T", " ")
    date = date[0:12]
    #2021-06-12T23:46:03+00:00
    res = datetime.strptime(date, f)
    return res
