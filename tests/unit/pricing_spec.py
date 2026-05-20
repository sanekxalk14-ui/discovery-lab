import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

import unittest
from shop.pricing import final_price_cents

class TestFinalPrice(unittest.TestCase):


    def test_basic_scenario(self):
        result = final_price_cents(1000, 10, 20)
        self.assertEqual(result, 1080)

    def test_discount_100(self):
        result = final_price_cents(1000, 100, 20)
        self.assertEqual(result, 0)

    def test_tax_100(self):
        result = final_price_cents(1000, 0, 100)
        self.assertEqual(result, 2000)

    def test_no_discount_no_tax(self):
        result = final_price_cents(500)
        self.assertEqual(result, 500)

    def test_invalid_type_none(self):
        with self.assertRaises(TypeError):
            final_price_cents(None)

    def test_negative_base(self):
        with self.assertRaises(ValueError):
            final_price_cents(-100)

    def test_discount_over_100(self):
        with self.assertRaises(ValueError):
            final_price_cents(1000, 150)

    def test_tax_over_100(self):
        with self.assertRaises(ValueError):
            final_price_cents(1000, 10, 150)