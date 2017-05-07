from factory.django import DjangoModelFactory
from factory import RelatedFactory, SubFactory
from exercises.models.exercise import Exercise
from exercises.models.workout import Workout, WorkoutType
from django.contrib.auth.models import User


class ExerciseFactory(DjangoModelFactory):

    class Meta:
        model = Exercise


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    # Defaults (can be overrided)
    username = 'john.doe'
    email = 'john.doe@example.com'


class WorkoutTypeFactory(DjangoModelFactory):
    class Meta:
        model = WorkoutType


class WorkoutFactory(DjangoModelFactory):
    class Meta:
        model = Workout

    workout_type = SubFactory(WorkoutTypeFactory)