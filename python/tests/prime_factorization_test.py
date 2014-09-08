# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/8/14'

import unittest
from primes.prime_factorization import *

class PrimeFactorizationTestCase(unittest.TestCase):
    """Tests for prime factorization"""

    def test_trial_division(self):
        """Prime factorization tests using trial division"""
        self.assertEqual(prime_facts_trial_division(0), None)
        self.assertEqual(prime_facts_trial_division(1), {1: 1})
        self.assertEqual(prime_facts_trial_division(2), {2: 1})
        self.assertEqual(prime_facts_trial_division(3), {3: 1})
        self.assertEqual(prime_facts_trial_division(4), {2: 2})
        self.assertEqual(prime_facts_trial_division(5), {5: 1})
        self.assertEqual(prime_facts_trial_division(6), {2: 1, 3: 1})
        self.assertEqual(prime_facts_trial_division(7), {7: 1})
        self.assertEqual(prime_facts_trial_division(8), {2: 3})
        self.assertEqual(prime_facts_trial_division(9), {3: 2})
        self.assertEqual(prime_facts_trial_division(100), {2: 2, 5: 2})


if __name__ == '__main__':
    unittest.main()
