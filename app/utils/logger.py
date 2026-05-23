
import datetime

def log(msg):
    # logger simple
    print(f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {msg}")
