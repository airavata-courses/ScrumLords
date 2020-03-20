from django.test import SimpleTestCase, Client

# Create your tests here.

class ManagerApiTest(SimpleTestCase):
    def test_health_check(self):
        response = self.client.get("/ht")
        self.assertEqual(response.status_code, 200)

    def test_ready_check(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
