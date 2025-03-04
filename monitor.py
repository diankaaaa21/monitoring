import os
import time

import django
from django.utils import timezone
from dotenv import load_dotenv

# Загрузка настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoring.settings")
django.setup()

from metrics.models import SystemMetrics
from metrics.services.data_fetcher import fetch_metrics
from metrics.services.incident_checker import check_incidents

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}


def save_to_db(machine_id, data):

    SystemMetrics.objects.create(
        machine_id=machine_id,
        cpu=data["cpu"],
        mem=data["mem"],
        disk=data["disk"],
        uptime=data["uptime"],
        timestamp=timezone.now(),
    )


def monitor():
    while True:
        for machine_id in range(1, 31):
            metrics = fetch_metrics(machine_id)
            if metrics:
                save_to_db(machine_id, metrics)
        check_incidents()
        time.sleep(900)


if __name__ == "__main__":
    monitor()
