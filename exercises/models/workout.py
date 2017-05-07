from django.db import models


class WorkoutType(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)


class Workout(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)

