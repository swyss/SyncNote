# src/utils/log_stream.py

import time

def stream_logs(logfile="logs/syncnote.log"):
    """Stream logs from the log file."""
    try:
        with open(logfile, "r") as file:
            file.seek(0, 2)  # Move to the end of the file
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                print(f"\033[94m{line.strip()}\033[0m")
    except Exception as e:
        print(f"\033[91m[ERROR] Failed to stream logs: {e}\033[0m")
