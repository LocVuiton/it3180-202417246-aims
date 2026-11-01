import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTest(unittest.TestCase):
    def test_reject_dvd_beyond_limit(self):
        cart = Cart()

        for index in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {index + 1}")
            self.assertTrue(cart.add_dvd(dvd))

        overflow_dvd = DigitalVideoDisc("DVD 21")

        self.assertFalse(cart.add_dvd(overflow_dvd))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()