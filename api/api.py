from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializers import ExerciseSerializer, SessionSerializer, WorkoutSerializer, ExerciseFieldsSerializer,\
    WorkoutTypeSerializer, SessionValuesSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from exercises.models.exercise import Exercise, Session, SessionValues, ExerciseFields
from exercises.models.workout import Workout, WorkoutType
from django.core.exceptions import ObjectDoesNotExist


class SessionValuesViewSet(viewsets.ModelViewSet):
    serializer_class = SessionValuesSerializer
    queryset = SessionValues.objects.all()


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()

    # def get_queryset(self):
    #     queryset = Workout.objects.all()
    #
    #     term = self.request.query_params.get('term', None)
    #     if term == 'latest/':
    #         queryset = queryset.filter(is_complete=True).order_by('-created')
    #         if queryset:
    #             queryset = [queryset[0]]
    #
    #     return queryset


class WorkoutTypeViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutTypeSerializer
    queryset = WorkoutType.objects.all()


class ExerciseFieldsViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseFieldsSerializer
    queryset = ExerciseFields.objects.all()


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


# class ExerciseViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing Exercise instances.
#     """
#     serializer_class = ExerciseSerializer
#
#     def get_queryset(self):
#         queryset = Exercise.objects.all()
#
#         if self.request.query_params.get('workout'):
#             workout_id = int(self.request.query_params.get('workout'))
#             workout = get_object_or_404(Workout, id=workout_id)
#             queryset = workout.exercises.all()
#
#         return queryset
#
#
# class SessionViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing Session instances.
#     """
#     serializer_class = SessionSerializer
#
#     def get_queryset(self):
#         queryset = Session.objects.all()
#
#         return queryset
#
#
# class WorkoutViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing Workout instances.
#     """
#     serializer_class = WorkoutSerializer
#
#     def get_queryset(self):
#         queryset = Workout.objects.all()
#
#         if self.request.query_params.get('latest'):
#             workout = Workout.objects.latest('created')
#             if not workout.completed:
#                 queryset = [Workout.objects.latest('created'), ]
#
#         return queryset
#
#
# # class WorkoutExerciseViewSet(viewsets.ModelViewSet):
# #     """
# #     A viewset for viewing and editing WorkoutsExercises instances.
# #     """
# #     serializer_class = WorkoutExerciseSerializer
# #
# #     def get_queryset(self):
# #         queryset = WorkoutExercise.objects.all()
# #
# #         return queryset
