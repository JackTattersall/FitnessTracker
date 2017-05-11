from django.test import TestCase
from exercises.tests.factories import ExerciseFactory, SessionFactory


class ExercisesTests(TestCase):

    def test_exercise_string_function(self):
        self.exercise_one = ExerciseFactory(name='press-ups')
        self.assertEqual(str(self.exercise_one), 'press-ups')


class SessionTests(TestCase):

    def test_session_string_function(self):
        self.session_one = SessionFactory(reps=1,
                                          sets=1,
                                          weight=1,)

        self.assertEqual(str(self.session_one), 'reps = 1 sets = 1 weight = 1')