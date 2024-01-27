from urllib.parse import urlparse

from dotenv import load_dotenv
from .base import BaseAPI
load_dotenv()

class Webhooks(BaseAPI):
    VALID_EVENTS = {
        "ORDER_EXPIRED", "PAYMENT_DECLINED", "PAYMENT_ACTION_REQUIRED",
        "PAYMENT_APPROVED", "PAYMENT_CAPTURED", "CAPTURE_DECLINED",
        "PAYMENT_CANCELLED", "CANCEL_DECLINED", "REFUND_APPROVED",
        "REFUND_DECLINED", "SPLIT_APPROVED", "SPLIT_DECLINED",
        "SPLIT_REFUND_APPROVED", "SPLIT_REFUND_DECLINED", "CHECK_APPROVED",
        "CHECK_DECLINED", "INSTALLMENT_ISSUED", "INSTALLMENT_REJECTED",
        "CARD_APPROVED", "CARD_DECLINED"
    }

    def _is_valid_url(self, url):
        try:
            result = urlparse(url)
            return result.scheme and result.netloc and 1 <= len(url) <= 2083
        except ValueError:
            return False

    def _is_valid_events(self, events):
        return all(event in self.VALID_EVENTS for event in events)

    def get_webhooks(self):
        return self._send_request("GET", "webhooks")

    def get_webhook_by_id(self, webhook_id):
        return self._send_request("GET", f"webhooks/{webhook_id}")

    def create_webhook(self, url, events):
        if not self._is_valid_url(url):
            raise ValueError("Invalid URL provided")
        if not self._is_valid_events(events):
            raise ValueError("Invalid events provided")

        webhook_data = {"url": url, "events": events}
        return self._send_request("POST", "webhooks", data=webhook_data)

    def update_webhook_by_id(self, webhook_id, events):
        if not self._is_valid_events(events):
            raise ValueError("Invalid events provided")
        webhook_data = {
            "events": events,
        }
        return self._send_request("PATCH", f"webhooks/{webhook_id}", data=webhook_data)

    def delete_webhook_by_id(self, webhook_id):
        return self._send_request("DELETE", f"webhooks/{webhook_id}")


