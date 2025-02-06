from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Incident


@api_view(["GET"])
def get_incidents(request):
    incidents = Incident.objects.all().order_by("-timestamp").values()
    return Response({"incidents": list(incidents)})
