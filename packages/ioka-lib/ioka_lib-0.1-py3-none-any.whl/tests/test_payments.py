import unittest
from ioka_lib import Payments


class TestPayments(unittest.TestCase):

    def setUp(self):
        api_key = "your_test_api_key"
        self.payments = Payments(api_key)

    def test_validate_pan_valid(self):
        self.assertTrue(self.payments.validate_pan("5555555555555599"))

    def test_create_card_payment_invalid_pan(self):
        with self.assertRaises(ValueError):
            self.payments.create_card_payment("ord_f0dhMVncPe", "000", "12/24", "John Doe", "123", False)

    def test_create_card_payment_invalid_exp(self):
        with self.assertRaises(ValueError):
            self.payments.create_card_payment("ord_f0dhMVncPe", "5555555555555599", "9824", "John Doe", "123", False)



if __name__ == '__main__':
    unittest.main()