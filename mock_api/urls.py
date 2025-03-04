from django.urls import path

from .views import mock_metrics

urlpatterns = [
    path("api/mock-metrics/", mock_metrics, name="mock_metrics"),
]
