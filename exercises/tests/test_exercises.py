from django.test import TestCase
from exercises.tests.factories import ExerciseFactory, SessionFactory


class ExercisesTests(TestCase):

    def test_exercise_string_function(self):
        self.exercise_one = ExerciseFactory(name='press-ups')
        self.assertEqual(str(self.exercise_one), 'press-ups')

