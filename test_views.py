import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from metrics.models import Incident


@pytest.mark.django_db
def test_get_incidents():
    Incident.objects.create(description="Test incident")
    client = APIClient()
    url = reverse("get_incidents")
    response = client.get(url)
    assert response.status_code == 200
    assert "incidents" in response.data
