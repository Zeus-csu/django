from django.test import TestCase, SimpleTestCase
# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/page/home')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/page/about')
        self.assertEqual(response.status_code,200)
    
    def test_contact_page_status_code(self):
        response = self.client.get('/page/contact')
        self.assertEqual(response.status_code,200)

    def test_feedback_page_status_code(self):
        response = self.client.get('/page/feedback')
        self.assertEqual(response.status_code,200)