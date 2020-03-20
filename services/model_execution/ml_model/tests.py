from django.test import SimpleTestCase, Client
from ml_model.views.forecast import forecast_weather

# Create your tests here.


class ModelExecutionApiTest(SimpleTestCase):
    def test_get_forecast_weather(self):
        content = {
            "subscription": "projects/falana-dhimka/subscriptions/model_execute_sub",
            "message": {
                "data": "eyJuX2RheXNfYWZ0ZXIiOiA3LCAibGF0aXR1ZGUiOiAiMzkuMTY1MzMiLCAibG9uZ2l0dWRlIjogIi04Ni41MjYzOSIsICJzZXNzaW9uX2lkIjogMzE1N30=",
                "messageId": "3",
                "attributes": {},
            },
        }
        response = self.client.post(
            "/dark/forecast", content, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
