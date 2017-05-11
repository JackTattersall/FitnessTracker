from factory.django import DjangoModelFactory
from factory import RelatedFactory, SubFactory
from exercises.models.exercise import Exercise, Session, ExerciseSession
from exercises.models.workout import Workout, WorkoutType, WorkoutExercise
from django.contrib.auth.models import User
import factory
import datetime


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


class SessionFactory(DjangoModelFactory):
    created = datetime.datetime.now()

    class Meta:
        model = Session


class WorkoutsExercisesFactroy(DjangoModelFactory):
    workout = factory.SubFactory(Workout)
    exercise = factory.SubFactory(Exercise)

    class Meta:
        model = WorkoutExercise


class ExercisesSessionsFactory(DjangoModelFactory):
    exercise = factory.SubFactory(Exercise)
    session = factory.SubFactory(SessionFactory)

    class Meta:
        model = ExerciseSession

