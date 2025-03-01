from django.urls import path

from .views import get_incidents

urlpatterns = [
    path("api/incidents/", get_incidents, name="get_incidents"),
]
