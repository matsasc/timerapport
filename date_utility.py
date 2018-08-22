import datetime
import calendar
from datetime import date, datetime, timedelta

def generate_week_number(d=date.today().day, m=date.today().month, y=date.today().year):   
    return "{0:0>2}".format(date(y,m,d).isocalendar()[1])

def generate_weeks(m=date.today().month, y=date.today().year):
    weeks = []
    for week in calendar.monthcalendar(y, m):
        week_days = list(filter(lambda x: x > 0, week))
        weeks.append(week_days)
    return weeks

def week_range(m=date.today().month, y=date.today().year):
    week_values = []
    for week in generate_weeks(m,y):        
        week_number = generate_week_number(week[0],m,y)
        date_range = "{0:0>2}/{2:0>2} - {1:0>2}/{2:0>2} - {3:0>4}".format(week[0],week[-1], m, y)
        week_values.append((week_number , date_range, "0"))
    return week_values

def today():
    return [date.today().day, date.today().month, date.today().year]

def last_day(m=date.today().month, y=date.today().year):
    return "{}".format(generate_weeks(m,y)[-1][-1])

def last_date(m=date.today().month, y=date.today().year):
    return "{0:0>2}/{1:0>2} - {2:0>4}".format(last_day(m,y),m,y)

def month_range(m=date.today().month, y=date.today().year):
    return "{0:0>2}/{2:0>2} - {1:0>2}/{2:0>2} - {3:0>4}".format(1,last_day(m,y), m, y)