# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/8/14'

import unittest

from primes.reflector import *


class ReflectorTestCase(unittest.TestCase):

    def test_get_reflected_prime_factors(self):
        reflected_prime_factors = get_reflected_prime_factors(-1)
        self.assertEqual(reflected_prime_factors, None)

        reflected_prime_factors = get_reflected_prime_factors(0)
        self.assertEqual(reflected_prime_factors, None)

        reflected_prime_factors = get_reflected_prime_factors(1)
        self.assertEqual(reflected_prime_factors, {1: 1})

        reflected_prime_factors = get_reflected_prime_factors(2)
        self.assertEqual(reflected_prime_factors, {1: 2})

        reflected_prime_factors = get_reflected_prime_factors(9)
        self.assertEqual(reflected_prime_factors, {2: 3})

        reflected_prime_factors = get_reflected_prime_factors(50)
        self.assertEqual(reflected_prime_factors, {2: 5, 1: 2})

    def test_get_reflection(self):
        reflection = get_reflection(0)
        self.assertEqual(reflection, None)

        reflection = get_reflection(1)
        self.assertEqual(reflection, 1)

        reflection = get_reflection(2)
        self.assertEqual(reflection, 1)

        reflection = get_reflection(4)
        self.assertEqual(reflection, 4)

        reflection = get_reflection(8)
        self.assertEqual(reflection, 9)

        reflection = get_reflection(9)
        self.assertEqual(reflection, 8)

        reflection = get_reflection(50)
        self.assertEqual(reflection, 32)

    def test_is_reflector(self):
        self.assertEqual(is_reflector(0), False)
        self.assertEqual(is_reflector(1), True)
        self.assertEqual(is_reflector(2), False)
        self.assertEqual(is_reflector(4), True)
        self.assertEqual(is_reflector(8), True)
        self.assertEqual(is_reflector(9), True)
        self.assertEqual(is_reflector(10), False)
        self.assertEqual(is_reflector(3888), True)

if __name__ == '__main__':
    unittest.main()
