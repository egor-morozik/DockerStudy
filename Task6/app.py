import time
from datetime import datetime

while True:
    with open("/app/logs/log.txt", "a") as f:
        f.write(f"Log: {datetime.now()}\n")
    time.sleep(10)