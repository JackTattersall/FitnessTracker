from django.db import models


class WorkoutType(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'workout_type'


class Workout(models.Model):
    completed = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, related_name='workout', null=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        db_table = 'workout'








