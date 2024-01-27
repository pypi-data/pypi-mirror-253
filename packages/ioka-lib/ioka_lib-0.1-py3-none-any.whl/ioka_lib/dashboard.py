from dotenv import load_dotenv
from .base import BaseAPI
load_dotenv()
import requests

class Dashboard(BaseAPI):
    def search_dashboard_payments(self, from_dt, to_dt, page=1, limit=10):

        query_params = f"page={page}&limit={limit}"
        if from_dt is not None:
            query_params += f"&from_dt={from_dt}"
        if to_dt is not None:
            query_params += f"&to_dt={to_dt}"

        return self._send_request("GET", f"dashboard/payments?{query_params}")

    def export_dashboard_payments(self, from_dt, to_dt, page=1, limit=10):
        query_params = f"page={page}&limit={limit}"
        if from_dt is not None:
            query_params += f"&from_dt={from_dt}"
        if to_dt is not None:
            query_params += f"&to_dt={to_dt}"

        response = self._send_request_for_file("GET", f"dashboard/payments/export?{query_params}")

        if response.status_code == 200:
            with open("dashboard_payments.xlsx", "wb") as f:
                f.write(response.content)
            return "File downloaded successfully"
        else:
            return "Error downloading file"

    def _send_request_for_file(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "API-KEY": self.api_key,
        }
        response = requests.request(method, url, headers=headers, json=data)

        return response