from django.test import SimpleTestCase, Client
from data_retrieval.views.data_retrieve import retrieve_historical_data

# Create your tests here.


class DataRetrievalApiTest(SimpleTestCase):
    def test_get_forecast_weather(self):
        content = {
            "subscription": "projects/falana-dhimka/subscriptions/data_retrieval_sub",
            "message": {
                "data": "eyJzZXNzaW9uX2lkIjogMzE1NywgIm5fZGF5c19iZWZvcmUiOiA1LCAibl9kYXlzX2FmdGVyIjogNywgImxhdGl0dWRlIjogIjM5LjE2NTMzIiwgImxvbmdpdHVkZSI6ICItODYuNTI2MzkifQ==",
                "messageId": "1",
                "attributes": {},
            },
        }
        response = self.client.post(
            "/dark/history", content, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
