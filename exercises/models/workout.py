from django.db import models
from exercises.models.exercise import Exercise
import datetime


class WorkoutType(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'FITNESS_workout_type'


def get_date():
    date = datetime.datetime.now()
    return 'workout {}-{}-{}-{}h{}m{}s'.format(date.day, date.month, date.year, date.hour, date.min, date.second)


class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default=get_date(), max_length=255)
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






