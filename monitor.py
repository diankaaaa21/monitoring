# import datetime
# import os
# import time
#
# import mysql.connector
# from dotenv import load_dotenv
#
# load_dotenv()
#
# DB_CONFIG = {
#     "host": os.getenv("DB_HOST"),
#     "user": os.getenv("MYSQL_USER"),
#     "password": os.getenv("MYSQL_PASSWORD"),
#     "database": os.getenv("MYSQL_DATABASE"),
#     "port": os.getenv("DB_PORT", "3306"),
# }
#
# THRESHOLDS = {"cpu": 85, "mem": 90, "disk": 95}
#
#
# def check_incidents():
#     conn = mysql.connector.connect(**DB_CONFIG)
#     cursor = conn.cursor(dictionary=True)
#
#     query = "SELECT * FROM metrics_systemmetrics ORDER BY timestamp DESC LIMIT 30"
#     cursor.execute(query)
#     metrics = cursor.fetchall()
#
#     for metric in metrics:
#         for param, limit in THRESHOLDS.items():
#             value = int(metric[param].strip("%"))
#             if value > limit:
#                 cursor.execute(
#                     """
#                     INSERT INTO metrics_incident (machine_id, parameter, value, threshold, duration)
#                     VALUES (%s, %s, %s, %s, 30)
#                 """,
#                     (metric["machine_id"], param, value, limit),
#                 )
#
#     conn.commit()
#     cursor.close()
#     conn.close()
#
#
# while True:
#     check_incidents()
#     time.sleep(900)
