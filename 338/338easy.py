#!/usr/bin/python

import datetime as dt

inputdata = """2017 10 30
2016 2 29
2015 2 28
29 4 12
570 11 30
1066 9 25
1776 7 4
1933 1 30
1953 3 6
2100 1 9
2202 12 15
7032 3 26"""


def dayofweek(date):
    y, m, d = date.split(' ')
    # datetime requires a 4-digit year.
    y = '0'*(4-len(str(y))) + y
    date = f'{y} {m} {d}'
    try:
        dateobj = dt.datetime.strptime(date, '%Y %M %d')
    except ValueError:
        return None
    return dateobj.strftime('%A')


assert(dayofweek('2202 12 15') == 'Wednesday')
