from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from exercises.tests.factories import WorkoutFactory, ExerciseFactory, WorkoutsExercisesFactroy, SessionFactory, ExercisesSessionsFactory
import simplejson


class ExerciseViewSetTests(APITestCase):
    """Test exercise api endpoint"""
    def setUp(self):
        # Workout
        self.workout_1 = WorkoutFactory(id=1)

        # Exercises
        self.exercise_1 = ExerciseFactory(name='press-ups')
        self.exercise_2 = ExerciseFactory(name='sit-ups')

        # User to authenticate against
        self.test_user = User.objects.create_user('test_user', 'test@test.com', 'testing')

    # Login function
    def _require_login(self):
        self.client.login(username='test_user', email='test@test.com', password='testing')

    # API VIEWS TESTS #

    # test authentication
    def test_detail_authentication(self):
        # act
        # not authenticated
        response = self.client.get(reverse('api:exercise-detail', kwargs={'pk': self.exercise_1.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg='not authenticated')

        # authenticated
        self._require_login()
        response = self.client.get(reverse('api:exercise-detail', kwargs={'pk': self.exercise_1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg='authenticated')

    def test_list_authentication(self):
        # act
        # not authenticated
        response = self.client.get(reverse('api:exercise-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg='not authenticated')

        # authenticated
        self._require_login()
        response = self.client.get(reverse('api:exercise-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg='authenticated')

    def test_post_authentication(self):
        # act
        # not authenticated
        response = self.client.post(reverse('api:exercise-list'), {'name': 'squats'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg='not authenticated')

        # authenticated
        self._require_login()
        response = self.client.post(reverse('api:exercise-list'), {'name': 'squats'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg='authenticated')

    def test_exercises_by_workout(self):
        # arrange
        WorkoutsExercisesFactroy(workout=self.workout_1, exercise=self.exercise_1)

        # act
        self._require_login()
        response = self.client.get(reverse('api:exercise-list') + '?workout={}'.format(self.workout_1.id))
        response_data = simplejson.loads(response.content)
        print(response_data)

        # assert
        self.assertEqual(response_data['results'][0]['name'], self.exercise_1.name)
        self.assertEqual(len(response_data['results']), 1)

        # act workout with id 999 doesnt exist
        response = self.client.get(reverse('api:exercise-list') + '?workout={}'.format(999))

        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # API SERIALIZERS TESTS

    def test_post_including_session_data(self):
        # arrange
        self.session = SessionFactory(reps=1, sets=2, weight=3)
        ExercisesSessionsFactory(exercise=self.exercise_1, session=self.session)

        # act
        self._require_login()
        response = self.client.post(reverse('api:exercise-list'), {
                                                                   'name': 'press-ups',
                                                                   'sessions': [
                                                                        1,
                                                                        2,
                                                                        3
                                                                   ]})
        print(simplejson.loads(response.content))
        self.assertContains(response, 'reps', status_code=201)

