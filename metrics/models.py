from django.db import models


class SystemMetrics(models.Model):
    machine_id = models.CharField(max_length=50)
    cpu = models.IntegerField()
    mem = models.CharField(max_length=10)
    disk = models.CharField(max_length=10)
    uptime = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = "metrics_systemmetrics"


class Incident(models.Model):
    machine_id = models.CharField(max_length=50)
    parameter = models.CharField(max_length=10)
    value = models.CharField(max_length=10)
    threshold = models.CharField(max_length=10)
    duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        db_table = "metrics_incident"
