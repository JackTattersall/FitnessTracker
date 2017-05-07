from django.conf.urls import url, include
from base import views

urlpatterns = [
    url('^$', views.dashboard, name='dashboard'),
]
