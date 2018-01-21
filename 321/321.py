#!/usr/bin/python

inputdata = """
00:00
01:30
12:05
14:01
20:29
21:00"""

nums = {
        0: 'oh', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight',  9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty',
        30: 'thirty', 40:'forty', 50: 'fifty', }


def englishify(t):
    """
takes a str of form HH:mm, returns the english equivelent.
for example: englishify('01:30') -> "It's one thirty am"
englishify('14:32') -> "It's two thirty two pm"
"""

    hour, minutes = t.split(':')
    hour = int(hour)
    hour_word = nums[hour % 12 if hour not in [12, 0] else 12]
    am_pm = 'PM' if hour > 12 else 'AM'

    minutes_word = ''
    if int(minutes) == 0:
        minutes_word = 'oh clock'
    else:
        try:
            if minutes[0] == '0':
                minutes_word += nums[0] + ' '
            minutes_word += nums[int(minutes)]
        except KeyError:
            minutes_word += nums[int(minutes[0])*10] + " "
            minutes_word += nums[int(minutes[1])]
    return f"It's {hour_word} {minutes_word} {am_pm}"


for x in inputdata.split():
    print(x, englishify(x))
