from django.test import TestCase
from exercises.tests.factories import WorkoutFactory, WorkoutTypeFactory
from exercises.models.workout import WorkoutType


class WorkoutTest(TestCase):
    def setUp(self):
        self.workout1 = WorkoutFactory(workout_type=WorkoutTypeFactory(name='yoga'))

    def test_relationship(self):
        self.assertIsInstance(self.workout1.workout_type, WorkoutType)
