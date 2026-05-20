import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import unittest
from shop.pricing import final_price_cents

class TestIntegrationPricing(unittest.TestCase):


    def test_chain_calculations(self):
        prices = [1000, 2000, 3000]
        results = []
        for price in prices:
            result = final_price_cents(price, 10, 20)
            results.append(result)
        self.assertEqual(results, [1080, 2160, 3240])

    def test_multiple_scenarios(self):
        scenarios = [
            (1000, 0, 0),
            (2000, 50, 10),
            (500, 25, 15),
        ]
        expected = [1000, 1100, 431]
        results = [final_price_cents(*s) for s in scenarios]
        self.assertEqual(results, expected)