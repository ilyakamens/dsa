# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/6/14'


def get_sieve(n):
    """Uses Eratosthenes's algorithm to determine whether each number
    from 0 - n is prime.

    :param n:   The max number to determine if it's prime
    :return:    None if n < 2, otherwise an array of booleans, where each
                boolean represents whether the number (index) is prime.
                e.g.:
                   0      1      2     3     4      5     6      7     8      9      10
                [False, False, True, True, False, True, False, True, False, False, False]
    """
    if n < 2:
        return None

    nums = [False, False]   # We know 0 and 1 aren't prime
    nums += [True] * (n - 1)    # Assume the rest are true

    # for i = 2 ... √n
    for i in xrange(2, int(n**0.5) + 1):
        if nums[i]:
            # for j = i^2, i^2 + i, i^2 + 2i, i^2 + 3i...
            for j in xrange(i**2, n + 1, i):
                nums[j] = False

    return nums


def get_primes(n):
    """Return the list of primes up to and including n.
    :param n:   The highest number that could be in the list.
    :return:    The empty list if n < 2, otherwise a list of primes up to n
                e.g. [2, 3, 5, 7, etc.]
    """
    sieve = get_sieve(n)
    return [i for i in xrange(2, n + 1) if sieve[i]]