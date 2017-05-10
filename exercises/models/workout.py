from django.db import models
from exercises.models.exercise import Exercise
import datetime


class WorkoutType(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'FITNESS_workout_type'


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    completed = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through=u'WorkoutExercise', related_name=u'workouts')

    class Meta:
        db_table = 'FITNESS_workout'


class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise)
    workout = models.ForeignKey(Workout)

    class Meta:
        db_table = 'FITNESS_workouts_exercises'






