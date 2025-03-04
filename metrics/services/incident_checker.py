from datetime import datetime, timedelta

from django.utils import timezone

from metrics.models import Incident, SystemMetrics

CPU_THRESHOLD = 85
MEM_THRESHOLD = 90
DISK_THRESHOLD = 95


def check_incidents():

    now = timezone.now()

    cpu_metrics = SystemMetrics.objects.filter(
        cpu__gt=CPU_THRESHOLD, timestamp__gte=now - timedelta(minutes=30)
    )
    if cpu_metrics.exists():
        Incident.objects.create(
            metric_type="CPU",
            value=cpu_metrics.latest("timestamp").cpu,
            timestamp=cpu_metrics.latest("timestamp").timestamp,
            description="CPU threshold exceeded 85% for more than 30 minutes.",
        )

    mem_metrics = SystemMetrics.objects.filter(
        mem__gt=MEM_THRESHOLD, timestamp__gte=now - timedelta(minutes=30)
    )
    if mem_metrics.exists():
        Incident.objects.create(
            metric_type="Memory",
            value=mem_metrics.latest("timestamp").mem,
            timestamp=mem_metrics.latest("timestamp").timestamp,
            description="Memory threshold exceeded 90% for more than 30 minutes.",
        )

    disk_metrics = SystemMetrics.objects.filter(
        disk__gt=DISK_THRESHOLD, timestamp__gte=now - timedelta(hours=2)
    )
    if disk_metrics.exists():
        Incident.objects.create(
            metric_type="Disk",
            value=disk_metrics.latest("timestamp").disk,
            timestamp=disk_metrics.latest("timestamp").timestamp,
            description="Disk threshold exceeded 95% for more than 2 hours.",
        )
