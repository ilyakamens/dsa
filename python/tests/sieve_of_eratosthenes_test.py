# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/8/14'

import unittest
from primes.sieve_of_eratosthenes import *


class SieveOfEratosthenesTestCase(unittest.TestCase):
    """Test cases for getting primes using the Sieve of Eratosthenes"""

    def test_get_sieve(self):
        """Tests get_sieve()"""
        self.assertEqual(get_sieve(1), None)
        self.assertEqual(get_sieve(2), [False, False, True])
        self.assertEqual(get_sieve(10), [False, False, True, True, False, True, False, True, False, False, False])

    def test_get_primes(self):
        """Tests get_primes()"""
        self.assertEqual(get_primes(1), [])
        self.assertEqual(get_primes(2), [2])
        self.assertEqual(get_primes(10), [2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()
