import json
import os
import random
from datetime import datetime, timedelta


os.makedirs("sample_logs", exist_ok=True)

methods = ["GET", "POST", "PUT", "DELETE"]
paths = [
    "/api/users",
    "/api/login",
    "/api/report",
    "/api/payment",
    "/api/upload",
]
statuses = [200, 201, 400, 401, 404, 500]
ips = [
    "192.168.1.1",
    "10.0.0.1",
    "172.16.0.5",
]



def random_timestamp():