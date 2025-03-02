import os
import time

import mysql.connector
import requests
from dotenv import load_dotenv

load_dotenv()
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}

ENDPOINT_URL = "https://example.com/api/metrics"
MACHINE_ID = os.getenv("MACHINE_ID", "machine_id_01")


def fetch_metrics():
    response = requests.get(ENDPOINT_URL, timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def save_to_db(data):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    sql = """
    INSERT INTO metrics_systemmetrics (machine_id, cpu, mem, disk, uptime)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(
        sql, (MACHINE_ID, data["cpu"], data["mem"], data["disk"], data["uptime"])
    )
    conn.commit()
    cursor.close()
    conn.close()


while True:
    metrics = fetch_metrics()
    if metrics:
        save_to_db(metrics)
    time.sleep(900)
