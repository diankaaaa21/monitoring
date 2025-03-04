from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Incident


@csrf_exempt
def incident_list(request):
    incidents = Incident.objects.order_by("-timestamp")[:50].values()
    return render(request, "metrics/incident_list.html", {"incidents": incidents})
