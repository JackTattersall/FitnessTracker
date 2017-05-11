"""urlconf for the base application"""
from rest_framework import routers
from django.conf.urls import url, include

from .api import *

router = routers.DefaultRouter()
router.register(r'exercise', ExerciseViewSet, 'exercise')
router.register(r'session', SessionViewSet, 'session')
router.register(r'workout', WorkoutViewSet, 'workout')
router.register(r'workout-type', WorkoutTypeViewSet, 'workout-type')
router.register(r'workout-type-fields', WorkoutTypeFieldsViewSet, 'workout-type-fields')

urlpatterns = [
    # API views
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
