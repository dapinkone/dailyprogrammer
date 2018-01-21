from random import randint
from timeit import timeit
from collections import ChainMap


def patches_OG(lines):
    # @PatchesPrime gets cred this version as 'solve';
    # I just renamed and removed his comments/docstring for brevity.
    ranges = list()
    for line in lines.split('\n'):
        ints = tuple(map(int, line.split()))
        ranges.append(range(*ints))
    ranges = set([y for x in ranges for y in x])
    return len(ranges)


def cheeky(lines): # @PatchesPrime credit for this one too.
    '''How short can I make solve?'''
    # Hahahahaha come at me bro
    return len(set([y for x in [range(*tuple(map(int, line.split())))
                                for line in lines.split('\n')] for y in x]))


def refactor(lines):
    s = set()
    for line in lines.split('\n'):
        s.update(set(range(*map(int, line.split()))))
    return len(s)


def gen_data(size=10_000, pairs=20):
    # generate a random dataset, which follows the rules from 347-easy
    lines = list()
    for i in range(pairs):
        start = randint(0, size)
        stop = randint(start, size)
        if start == stop:
            start = start - 1
        line = "{} {}".format(start, stop)
        lines.append(line)
    return "\n".join(lines)


def time_funcs(funcs, size=100_000, pairs=20):
    d = gen_data(size=size, pairs=pairs)
    players = dict()
    for func in funcs:
        scope = dict(ChainMap(locals(), globals()))
        func_time = timeit('func(d)', globals=scope, number=1)
        players[func.__name__] = func_time
    sorted_players = sorted(players.items(), key=lambda x: x[1])

    print(f'r:{size}/{pairs}\t', end='')
    print(" ".join([f'{p}:{t}' for p, t in sorted_players]))
    return sorted_players


def exhaustive_tests():
    results = dict()
    for size in range(1000, 10000, 1000):
        for pairs in range(2, size, size // 20):
            results[(size, pairs)] = time_funcs([refactor, patches_OG, cheeky],
                                               size, pairs)
    return results


# times()
bonus = '''15 18
13 16
9 12
3 4
17 20
9 11
17 18
4 5
5 6
4 5
5 6
13 16
2 3
15 17
13 14'''

time_funcs([refactor, patches_OG, cheeky], size=100, pairs=10)
