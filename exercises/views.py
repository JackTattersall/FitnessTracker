from django.shortcuts import render


def start_workout(request):
    return render(request, 'start_workout.html')
