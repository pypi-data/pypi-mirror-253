from urllib.parse import  urlencode
import re
from dotenv import load_dotenv
from .base import BaseAPI
from .payments import validate_luhn

load_dotenv()


class Customers(BaseAPI):
    def get_customers(self, limit=10, page=1, to_dt=None, from_dt=None):
        params = {'limit': limit, 'page': page}

        if to_dt is not None:
            params['to_dt'] = to_dt
        if from_dt is not None:
            params['from_dt'] = from_dt
        query_string = urlencode(params)
        return self._send_request("GET", f"customers?{query_string}")

    def get_customer_by_id(self, customer_id):
        return self._send_request("GET", f"customers/{customer_id}")

    def create_customer(self, email, phone, external_id):

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")

        customer_data = {
            "email": email,
            "phone": phone,
            "external_id": external_id,
        }
        return self._send_request("POST", f"customers", data=customer_data)

    def get_customer_events(self,customer_id):
        return self._send_request("GET", f"customers/{customer_id}/events")

    def delete_customer_by_id(self, customer_id):
        return self._send_request("DELETE", f"customers/{customer_id}")



    class Cards(BaseAPI):
        @staticmethod
        def validate_pan(pan):
            return re.match(r'^\d{12,19}$', pan) is not None and validate_luhn(pan)

        @staticmethod
        def validate_exp(exp):
            return re.match(r'^\d{2}/\d{2}$', exp) is not None

        @staticmethod
        def validate_cvc(cvc):
            return re.match(r'^\d{3,4}$', cvc) is not None

        def create_binding(self, customer_id, pan, exp, cvc):
            if not self.validate_pan(pan):
                raise ValueError("Invalid PAN")
            if not self.validate_exp(exp):
                raise ValueError("Invalid Expiration Date")
            if not self.validate_cvc(cvc):
                raise ValueError("Invalid CVC")

            card_data = {
                "pan": pan,
                "exp": exp,
                "cvc": cvc,
            }

            return self._send_request("POST", f"customers/{customer_id}/bindings", data=card_data)

        def get_cards(self, customer_id):
            return self._send_request("GET", f"customers/{customer_id}/cards")

        def get_card_by_id(self, customer_id, card_id):
            return self._send_request("GET", f"customers/{customer_id}/cards/{card_id}")

        def delete_card_by_id(self, customer_id, card_id):
            return self._send_request("DELETE", f"customers/{customer_id}/cards/{card_id}")


