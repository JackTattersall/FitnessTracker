from django.db import models
from exercises.models.workout import Workout, WorkoutTypeFields


class Exercise(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return self.name


class Session(models.Model):
    is_complete = models.BooleanField(default=False)
    completed = models.DateTimeField(null=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout_type_fields = models.ForeignKey(WorkoutTypeFields, on_delete=models.CASCADE)

    class Meta:
        db_table = 'session'

    def __str__(self):
        return str('exercise {}'.format(self.exercise.name))



