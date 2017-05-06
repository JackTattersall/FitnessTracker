from factory.django import DjangoModelFactory
from exercises.models.model_exercise import Exercise


class ExerciseFactory(DjangoModelFactory):

    class Meta:
        model = Exercise
