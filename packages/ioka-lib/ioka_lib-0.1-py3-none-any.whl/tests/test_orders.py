import unittest
from unittest.mock import patch
from ioka_lib.orders import Orders

api_key = "your_test_api_key"

class TestCreateOrder(unittest.TestCase):

    @patch('ioka_lib.Orders._send_request')
    def test_create_order_valid(self, mock_send_request):
        mock_send_request.return_value = {'status': 'success'}
        orders = Orders(api_key)
        response = orders.create_order(100, "KZT", "AUTO")
        mock_send_request.assert_called_with("POST", "orders", data={"amount": 100, "currency": "KZT", "capture_method": "AUTO"})
        self.assertEqual(response, mock_send_request.return_value)

    def test_create_order_invalid_amount(self):
        orders = Orders(api_key)
        with self.assertRaises(ValueError):
            orders.create_order(99, "KZT", "AUTO")

    def test_create_order_invalid_currency(self):
        orders = Orders(api_key)
        with self.assertRaises(ValueError):
            orders.create_order(100, "lplp", "AUTO")

    def test_create_order_invalid_capture_method(self):
        orders = Orders(api_key)
        with self.assertRaises(ValueError):
            orders.create_order(100, "KZT", "INVALID_METHOD")


if __name__ == '__main__':
    unittest.main()