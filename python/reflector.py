# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/7/14'

from primes import prime_factorization

"""
Given positive integer n > 1, we define function r() as follows :

r(8) = 9       || explanation:    8 -> 2^3 -> 3^2 -> 9
r(3888) = 2000 ||             3888 -> (2^4)*(3^5) -> (5^3)*(4^2) -> 2000

In effect, r(n) creates the prime factorization, then inverts the primes with the powers.

If r(r(n)) == n, n is a "reflector".  For example :

r(r(8)) = r(r(2^3)) = r(3^2) = 2^3  = 8
r(r(3888)) = r(r((2^4)*(3^5))) = r((5^3)*(4^2)) = (2^4)*(3^5) = 3888
"""


def get_reflected_prime_factors(n):
    """Return a dictionary of prime factors mapped to their
    frequency, but reversed.

    :param n:   The number we want the reversed prime factorization for
    :return:    e.x.
                n = 9
                prime factors = {3: 2} (3^2 = 9)
                reversal = {2: 3}
    """
    reflection = None

    prime_factors = prime_factorization.prime_facts_trial_division(n)
    if prime_factors:
        reflection = {}
        for prime_factor in prime_factors:
            reflection[prime_factors[prime_factor]] = prime_factor

    return reflection


def get_reflection(n):
    """Return the reflection of n. The reflection is defined
    as x = a^b -> b^a = y.

    :param n:   The number we want the reflection of
    :return:    e.x.
                n = 8 = 2^3 -> 3^2 = 9
    """
    reflection = None

    reflected_prime_factors = get_reflected_prime_factors(n)
    if reflected_prime_factors:
        reflection = 1
        for prime_factor in reflected_prime_factors:
            reflection *= int(prime_factor) ** int(reflected_prime_factors[prime_factor])

    return reflection


def is_reflector(n):
    """Return True if n is a reflector, and False otherwise.
    A number is a reflector if reflection(reflection(n)) == n

    :param n:   The number we're checking is a reflector
    :return:
    """
    return get_reflection(get_reflection(n)) == n