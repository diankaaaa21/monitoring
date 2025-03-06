import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def mock_metrics(_request):
    data = {
        "cpu": round(random.uniform(10, 90), 2),
        "mem": round(random.uniform(20, 80), 2),
        "disk": round(random.uniform(30, 95), 2),
        "uptime": random.randint(10000, 99999),
    }
    return JsonResponse(data)
