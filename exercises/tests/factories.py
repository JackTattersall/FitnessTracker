from factory.django import DjangoModelFactory
from factory import RelatedFactory, SubFactory
from exercises.models.exercise import Exercise, Session, SessionValues
from exercises.models.workout import Workout, WorkoutType, WorkoutTypeFields
from django.contrib.auth.models import User
import factory
import datetime


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    # Defaults (can be overrided)
    username = 'john.doe'
    email = 'john.doe@example.com'


class WorkoutTypeFactory(DjangoModelFactory):
    id = factory.sequence(lambda n: n)

    class Meta:
        model = WorkoutType


class WorkoutFactory(DjangoModelFactory):
    class Meta:
        model = Workout

    workout_type = SubFactory(WorkoutTypeFactory)


class SessionFactory(DjangoModelFactory):
    exercise_id = factory.sequence(lambda n: n)
    workout_id = factory.sequence(lambda n: n)

    class Meta:
        model = Session


class ExerciseFactory(DjangoModelFactory):

    class Meta:
        model = Exercise


class WorkoutTypeFieldsFactroy(DjangoModelFactory):

    class Meta:
        model = WorkoutTypeFields


class SessionsValuesFactory(DjangoModelFactory):

    class Meta:
        model = SessionValues

