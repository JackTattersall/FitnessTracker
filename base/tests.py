from django.test import TestCase, Client
from django.urls import reverse


class ViewsTest(TestCase):

    def test_dashboard_view(self):
        self.client = Client()
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, 'Dashboard')
