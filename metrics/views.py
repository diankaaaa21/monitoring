from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Incident


@api_view(["GET"])
def get_incidents(request):
    try:
        incidents = Incident.objects.all().values()
        return Response({"incidents": list(incidents)})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
