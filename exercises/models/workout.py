from django.db import models
from exercises.models.exercise import Exercise


class WorkoutType(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)


class Workout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through=u'WorkoutExercise', related_name=u'workout_exercises')


class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise)
    workout = models.ForeignKey(Workout)






