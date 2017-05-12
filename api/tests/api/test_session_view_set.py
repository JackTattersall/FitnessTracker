from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from exercises.tests.factories import ExerciseFactory, SessionFactory, WorkoutFactory
from api.tests.api.test_api_base import ApiTestBase
import simplejson


class SessionViewSetTests(ApiTestBase):
    """Test session api endpoint"""
    def setUp(self):
        super(SessionViewSetTests, self).setUp()

        # Sessions
        self.session_1 = SessionFactory()

        # Exercises
        self.exercise_1 = ExerciseFactory(name='press-ups')

        # Workout
        self.workout_1 = WorkoutFactory(id=1)

    # API VIEWS TESTS #

    # test authentication
    def test_detail_authentication(self):
        self.detail_authentication('api:session-detail', self.session_1.id, 'session')

    def test_list_authentication(self):
        self.list_authentication('api:session-list', 'session')

    def test_post_authentication(self):
        self.valid_session_data = {
            "is_complete": True,
            "workout": 1
        }
        self.post_authentication('api:session-list', self.valid_session_data, 'session')

    def test_post_session_including_existing_exercise_name(self):
        self.valid_session_data = {
            "exercise_name": "press-ups",
            "workout": 1
        }
        self._require_login()
        response = self.client.post(reverse('api:session-list'), self.valid_session_data)
        print(simplejson.loads(response.content))
        self.assertContains(response, 'press-ups', status_code=201)

