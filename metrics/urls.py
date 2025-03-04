from django.urls import path

from .views import incident_list

urlpatterns = [
    path("incidents/", incident_list, name="incident_list"),
]
