#!/usr/bin/python
# given a string, return list of repeats and frequencies.


def analyse(data):
    data = str(data)
    lookup = dict()
    # the lower limit for chunk length has to be our string len / 2
    # in order for the chunk to possibly repeat. + 0.5 clears a rounding
    # error with odd-length strings here.
    for chunk_len in range(1, int(len(data) + 1 / 2)):
        # slide over data taking slices of chunk_len until end.
        for start in range(len(data) - chunk_len):
            chunk = data[start:start + chunk_len]
            lookup[chunk] = data.count(chunk)
    return {k: v for k, v in lookup.items() if v > 1}


d = '11325992321982432123259'
print(analyse(d))

print(analyse('333'))
print(analyse('33'))
