from django.test import TestCase
from exercises.exercise_tests.factories import ExerciseFactory


class ExercisesTests(TestCase):

    def test_string_function(self):
        self.exercise_one = ExerciseFactory(name='press-ups')
        self.assertEqual(str(self.exercise_one), 'press-ups')

