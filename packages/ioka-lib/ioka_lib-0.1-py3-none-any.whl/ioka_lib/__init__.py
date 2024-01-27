from .orders import Orders
from .payments import Payments
from .customers import Customers
from .webhooks import Webhooks
from .dashboard import Dashboard
from .base import BaseAPI


class IokaLib:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_api = BaseAPI(api_key)

        self.Orders = Orders(api_key)
        self.Payments = Payments(api_key)
        self.Webhooks = Webhooks(api_key)
        self.Dashboard = Dashboard(api_key)
        self.Customers = Customers(api_key)
        self.Cards = Customers.Cards(api_key)
