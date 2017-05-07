from django.shortcuts import render
from .models.workout import Workout, Exercise


def start_workout(request):
    workouts = Workout.objects.latest('created')
    exercises = Exercise.objects.filter(workout_exercises__pk=workouts.id)
    return render(request, 'start_workout.html', context={'exercises': exercises})
