from django.core.urlresolvers import reverse
from rest_framework import status
from exercises.tests.factories import ExerciseFactory, SessionFactory, WorkoutFactory, \
    SessionsValuesFactory, WorkoutTypeFactory
from api.tests.api.test_api_base import ApiTestBase
from exercises.models.workout import WorkoutType, Workout
import simplejson


class WorkoutViewSetTests(ApiTestBase):
    """Test session api endpoint"""
    def setUp(self):
        super(WorkoutViewSetTests, self).setUp()

        # Exercises
        self.exercise_1 = ExerciseFactory(name='press-ups')

        # Sessions
        self.session_1 = SessionFactory(exercise_id=self.exercise_1.id)

        # WorkoutType
        self.workout_type_1 = WorkoutTypeFactory(id=1, name='yoga')

        # Workout
        self.workout_1 = WorkoutFactory(id=1)

        # SessionValues
        self.session_value_1 = SessionsValuesFactory(value=66,
                                                     exercise_fields_id=1,
                                                     session_id=self.session_1.id)

    # API VIEWS TESTS #

    # test authentication
    def test_detail_authentication(self):
        self.detail_authentication('api:workout-detail', self.workout_1.id, 'workout')

    def test_list_authentication(self):
        self.list_authentication('api:workout-list', 'workout')

    def test_post_authentication(self):
        self.valid_workout_data = {
            'is_complete': False,
            'workout_type_name': 'yoga'
        }
        self.post_authentication('api:workout-list', self.valid_workout_data, 'workout')

    # test POST requires workout_type_name only
    def test_workout_type_name_required(self):
        self.invalid_workout_data = {
            'is_compete': False,
        }
        self._require_login()
        response = self.client.post(reverse('api:workout-list'), self.invalid_workout_data)
        self.assertEqual(response.content, b'{"workout_type_name":["This field is required."]}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Workout.objects.count(), 1)

    def test_post_requires_workout_type_exists(self):
        self.invalid_workout_data = {
            'workout_type_name': 'dorris'
        }
        self._require_login()
        response = self.client.post(reverse('api:workout-list'), self.invalid_workout_data)
        self.assertEqual(response.content, b'{"detail":"Not found."}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Workout.objects.count(), 1)

    def test_post_valid_data_creates_new_workout(self):
        self.valid_workout_data = {
            'workout_type_name': 'yoga'
        }
        self._require_login()
        response = self.client.post(reverse('api:workout-list'), self.valid_workout_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 2)

    def test_post_valid_data_updates_workout_type(self):
        # test workout_type_1 has no workout associated with it
        with self.assertRaises(Workout.DoesNotExist):
            self.workout_type_1.workout

        # post valid data
        self.valid_workout_data = {
            'workout_type_name': 'yoga'
        }
        self._require_login()
        response = self.client.post(reverse('api:workout-list'), self.valid_workout_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # retrieve workout_type_1 after post
        self.workout_type_1 = WorkoutType.objects.get(name='yoga')
        # retrieve the workout created id (from the response)
        self.created_workout_id = simplejson.loads(response.content).pop('id')
        # assert workout_type_1 now references new workout
        self.assertEqual(self.workout_type_1.workout.id, self.created_workout_id)
