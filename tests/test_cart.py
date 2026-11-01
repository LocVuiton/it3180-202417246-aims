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
    def test_sort_by_title(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))

        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["Aladdin", "Star Wars", "The Lion King"],
        )

    def test_sort_by_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))

        cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in cart.items],
            [18.99, 19.95, 24.95],
        )


if __name__ == "__main__":
    unittest.main()