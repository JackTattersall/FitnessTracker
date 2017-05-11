from django.test import TestCase, Client
from django.urls import reverse


class ViewsTest(TestCase):

    def test_start_workout_view(self):
        self.client = Client()
        response = self.client.get(reverse('exercises:start_workout'))
        self.assertContains(response, 'Workout')
