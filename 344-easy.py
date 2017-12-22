#!/usr/bin/python
from itertools import groupby
import timeit


def avg(lst):
    return sum(lst) / len(lst)


def baumSweet(n):
    """
    return a number n's value in the Baum-Sweet sequence.
    b_n = 1 if the binary representation of n contains no block of
    consecutive 0s of odd length.
    b_n = 0 otherwise.
    """
    # str replaces all groups of 2 zeroes. returns false if any are left.
    sweet = not ('0' in bin(int(n))[2:].replace('00', ''))

    if sweet:
        return 1
    else:
        return 0


def baumSwGrp(n):
    # version 2, using groupby, a bit faster maybe, but not really that fast
    # at scale. actual bit math might be faster?
    binary = bin(int(n))[2:]

    def keyfunc(x):
        return x is '0'

    grps = groupby(binary, keyfunc)
    for k, g in grps:
        if k is True:  # if this grp is 0s
            # print(f'n:{n} b:{binary} k:{k} g:{g}')

            if len(list(g)) % 2:  # is odd length
                return 0
    return 1


def cmpAlgos():
    # the following code shows that the string replacement algorithm
    # is up to 70% faster (0.00029 to 0.000100) than the groupby algorithm
    OG_times = []
    refactor_times = []
    for n in range(10000, 100000):
        # running our functions over some test data
        # to compare time performance. run 10x per n
        original = timeit.timeit('baumSweet({})'.format(n),
                                 setup='from __main__ import baumSweet',
                                 number=10)
        grpbyMethod = timeit.timeit('baumSwGrp({})'.format(n),
                                    setup='from __main__ import baumSwGrp',
                                    number=10)
        OG_times.append(original)
        refactor_times.append(grpbyMethod)
        #    print(f'n:{n}\toriginal:{original:.5f}\tgroupby:{grpbyMethod:.5f}\n')
    print('OG function: {:.6f}\tgroupby:{:.6f}'.format(
        avg(OG_times), avg(refactor_times)
    ))
