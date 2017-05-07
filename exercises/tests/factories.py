from factory.django import DjangoModelFactory
from exercises.models.exercise import Exercise


class ExerciseFactory(DjangoModelFactory):

    class Meta:
        model = Exercise
