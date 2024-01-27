from dotenv import load_dotenv
from .base import BaseAPI
load_dotenv()
import re


def validate_luhn(pan):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(pan)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0
class Payments(BaseAPI):
    def get_payment_by_id(self, order_id, payment_id):
        return self._send_request("GET", f"orders/{order_id}/payments/{payment_id}")

    @staticmethod
    def validate_pan(pan):
        return re.match(r'^\d{12,19}$', pan) is not None and validate_luhn(pan)

    @staticmethod
    def validate_exp(exp):
        return re.match(r'^\d{2}/\d{2}$', exp) is not None

    @staticmethod
    def validate_cvc(cvc):
        return re.match(r'^\d{3,4}$', cvc) is not None

    @staticmethod
    def validate_holder(holder):
        return holder is not None and holder.strip() != ""

    @staticmethod
    def validate_save(save):
        return isinstance(save, bool)

    def create_card_payment(self, order_id, pan, exp, holder, cvc, save):
        if not self.validate_pan(pan):
            raise ValueError("Invalid PAN")
        if not self.validate_exp(exp):
            raise ValueError("Invalid Expiration Date")
        if not self.validate_cvc(cvc):
            raise ValueError("Invalid CVC")
        if not self.validate_holder(holder):
            raise ValueError("Invalid Card Holder Name")
        if not self.validate_save(save):
            raise ValueError("Invalid Save Option")

        payment_data = {
            "pan": pan,
            "exp": exp,
            "cvc": cvc,
            "holder": holder,
            "save": save
        }

        return self._send_request("POST", f"orders/{order_id}/payments/card", data=payment_data)

    def create_card_payment_card_id(self, order_id, card_id):

        card_data = {
            "card_id": card_id
        }

        return self._send_request("POST", f"orders/{order_id}/payments/card", data=card_data)

