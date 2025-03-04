import os

import requests
from dotenv import load_dotenv

load_dotenv()

MOCK_API_URL = os.getenv("MOCK_API_URL", "http://localhost:8000/api/mock-metrics/")


def fetch_metrics(machine_id):

    try:
        response = requests.get(f"{MOCK_API_URL}?machine_id={machine_id}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error while requesting metrics for the machine. {machine_id}: {e}")
        return None
