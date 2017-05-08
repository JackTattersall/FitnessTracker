from django.shortcuts import render
from .models.workout import Workout, Exercise


def start_workout(request):

    workout = Workout.objects.latest('created')

    exercises = workout.exercises.all()
    return render(request, 'start_workout.html', context={'exercises': exercises,
                                                          'workout': workout})
