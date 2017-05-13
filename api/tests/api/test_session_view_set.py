from django.core.urlresolvers import reverse
from rest_framework import status
from exercises.tests.factories import ExerciseFactory, SessionFactory, WorkoutFactory, SessionsValuesFactory
from api.tests.api.test_api_base import ApiTestBase
from exercises.models.exercise import Exercise


class SessionViewSetTests(ApiTestBase):
    """Test session api endpoint"""
    def setUp(self):
        super(SessionViewSetTests, self).setUp()

        # Exercises
        self.exercise_1 = ExerciseFactory(name='press-ups')

        # Sessions
        self.session_1 = SessionFactory(exercise_id=self.exercise_1.id)

        # Workout
        self.workout_1 = WorkoutFactory(id=1)

        # SessionValues
        self.session_value_1 = SessionsValuesFactory(value=66,
                                                     workout_type_fields_id=1,
                                                     session_id=self.session_1.id)

    # API VIEWS TESTS #

    # test authentication
    def test_detail_authentication(self):
        self.detail_authentication('api:session-detail', self.session_1.id, 'session')

    def test_list_authentication(self):
        self.list_authentication('api:session-list', 'session')

    def test_post_authentication(self):
        self.valid_session_data = {
            "exercise_name": "press-ups",
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
        self.assertContains(response, 'press-ups', status_code=201)
        self.assertEqual(Exercise.objects.count(), 1)

    def test_post_session_including_new_exercise_name(self):
        self.valid_session_data = {
            "exercise_name": "jump-ups",
            "workout": 1
        }
        self._require_login()
        response = self.client.post(reverse('api:session-list'), self.valid_session_data)
        self.assertContains(response, 'jump-ups', status_code=201)
        self.assertEqual(Exercise.objects.count(), 2)

    def test_post_session_workout_required(self):
        self.valid_session_data = {
            "exercise_name": "jump-ups"
        }
        self._require_login()
        response = self.client.post(reverse('api:session-list'), self.valid_session_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response, 'workout', status_code=400)
        self.assertNotContains(response, 'exercise', status_code=400)

    def test_post_session_exercise_name_required(self):
        self.valid_session_data = {
            "workout": 1
        }
        self._require_login()
        response = self.client.post(reverse('api:session-list'), self.valid_session_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertContains(response, 'exercise', status_code=400)
        self.assertNotContains(response, 'workout', status_code=400)



