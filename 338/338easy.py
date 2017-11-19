#!/usr/bin/python

import datetime as dt


def dayofweek(date):
    year, month, day = date.split(' ')
    # datetime requires a 4-digit year.
    year = year.zfill(4)
    date = f'{year} {month} {day}'

    try:
        dateobj = dt.datetime.strptime(date, '%Y %m %d')
    except ValueError:
        return None
    return dateobj.strftime('%A')


def test_dayofweek():
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

    answers = "Monday Monday Saturday Thursday Friday Tuesday\
     Thursday Monday Friday Saturday Wednesday Monday"

    lookup = dict(zip(inputdata.splitlines(), answers.split()))

    for k, v in lookup.items():
        try:
            assert(dayofweek(k) == v)
        except AssertionError:  # elaborate in case of a fail.
            print(f"Failed Test: dayofweek({k}) == {v}: {dayofweek(k)}")


test_dayofweek()
