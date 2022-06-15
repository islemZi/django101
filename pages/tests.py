from urllib import response
from django.test import SimpleTestCase

# Create your tests here.
class MicCheck(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
    def test_signin_page(self):
        response = self.client.get('/Signin/')
        self.assertEqual(response.status_code,200)
