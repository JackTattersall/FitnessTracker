from django.conf.urls import url, include
from exercises.views import start_workout

urlpatterns = [
    url(r'', start_workout, name='start_workout'),
]
