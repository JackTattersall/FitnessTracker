from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from exercises.tests.factories import ExerciseFactory
from api.tests.api.test_api_base import ApiTestBase


class ExerciseViewSetTests(ApiTestBase):
    """Test exercise api endpoint"""
    def setUp(self):
        super(ExerciseViewSetTests, self).setUp()

        # Exercises
        self.exercise_1 = ExerciseFactory(name='press-ups')

    # API VIEWS TESTS #

    # test authentication
    def test_detail_authentication(self):
        self.detail_authentication('api:exercise-detail', self.exercise_1.id, 'exercise')

    def test_list_authentication(self):
        self.list_authentication('api:exercise-list', 'exercise')

    def test_post_authentication(self):
        self.post_authentication('api:exercise-list', {'name': 'squats'}, 'exercise')



