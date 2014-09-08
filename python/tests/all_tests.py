# -*- coding: utf-8 -*-
__author__ = 'ilyakamens'
__date__ = '9/8/14'

from sieve_of_eratosthenes_test import *
from prime_factorization_test import *
from reflector_test import *

class AllTestsTestCase(unittest.TestCase):
    """Test class to run all tests"""

    def test_all(self):
        """Load all the test suites so they can be run"""
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SieveOfEratosthenesTestCase))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PrimeFactorizationTestCase))
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ReflectorTestCase))

if __name__ == '__main__':
    unittest.main()
