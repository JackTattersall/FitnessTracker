from .serializers import ExerciseSerializer, SessionSerializer, WorkoutSerializer, WorkoutExerciseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from exercises.models.exercise import Exercise, Session
from exercises.models.workout import Workout, WorkoutExercise


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Exercise instances.
    """
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        queryset = Exercise.objects.all()

        if self.request.query_params.get('workout'):
            workout_id = int(self.request.query_params.get('workout'))
            workout = Workout.objects.get(id=workout_id)
            queryset = workout.exercises.all()

        return queryset


class SessionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Session instances.
    """
    serializer_class = SessionSerializer

    def get_queryset(self):
        queryset = Session.objects.all()

        return queryset


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Workout instances.
    """
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        queryset = Workout.objects.all()

        if self.request.query_params.get('latest'):
            workout = Workout.objects.latest('created')
            if not workout.completed:
                queryset = [Workout.objects.latest('created'), ]

        return queryset


class WorkoutExerciseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing WorkoutsExercises instances.
    """
    serializer_class = WorkoutExerciseSerializer

    def get_queryset(self):
        queryset = WorkoutExercise.objects.all()

        return queryset
