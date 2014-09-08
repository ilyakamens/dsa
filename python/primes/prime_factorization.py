# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/7/14'

from primes import sieve_of_eratosthenes

def prime_facts_trial_division(n):
    """Return a map of prime factors to the number of times each one appears.

    :param n:   The number we're computing the prime factorization of
    :return:    None if n < 1, a map of 1:1 if n == 1, otherwise a map of each
                prime factor to the number of times it appeared
    """
    if n < 1:
        return None
    if n == 1:
        return {1: 1}

    primes = sieve_of_eratosthenes.get_primes(int(n**0.5) + 1)
    prime_factors = {}

    for prime in primes:
        if prime**2 > n:
            break
        while n % prime == 0:
            if prime not in prime_factors:
                prime_factors[prime] = 1
            else:
                prime_factors[prime] += 1

            n /= prime

    if n > 1:
        prime_factors[n] = 1

    return prime_factors