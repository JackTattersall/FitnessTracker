from factory.django import DjangoModelFactory
from exercises.models.exercise import Exercise
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
