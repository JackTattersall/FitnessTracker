from django.db import models
from exercises.models.workout import Workout


class Exercise(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return self.name


class Session(models.Model):
    is_complete = models.BooleanField(default=False)
    completed = models.DateTimeField(null=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='session')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='session', null=True)

    class Meta:
        db_table = 'session'

    def __str__(self):
        return str('exercise {}'.format(self.exercise.name))


class ExerciseFields(models.Model):
    exercise = models.ManyToManyField(Exercise, related_name='exercise_fields')
    name = models.CharField(max_length=255, null=False)
    units_of_measure = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'exercise_fields'


class SessionValues(models.Model):
    value = models.CharField(max_length=255)
    exercise_fields = models.ForeignKey(ExerciseFields,
                                        on_delete=models.CASCADE,
                                        related_name='session_values',
                                        default=0)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session_values')

    class Meta:
        db_table = 'session_values'





