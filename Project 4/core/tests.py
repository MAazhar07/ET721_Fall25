from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirects to login if not logged in