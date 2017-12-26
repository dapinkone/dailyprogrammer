#!/usr/bin/python


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
