#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import time

def check_health():

    # --- CPU usage ---
    if psutil.cpu_percent(interval=1) > 80:
        return "CPU usage is over 80%"

    # --- Disk space ---
    total, used, free = shutil.disk_usage("/")
    free_percent = free / total * 100
    if free_percent < 20:
        return "Available disk space is lower than 20%"

    # --- Memory ---
    mem = psutil.virtual_memory()
    available_mb = mem.available / (1024 * 1024)
    if available_mb < 100:
        return "Available memory is less than 100MB"

    ip = socket.gethostbyname("localhost")
    if ip != "127.0.0.1":
        return "localhost cannot be resolved to 127.0.0.1"

    return None


if __name__ == "__main__":
    # code that runs only when the file is executed directly

    while True:
        problem = check_health()
        if problem:
            sender = "automation@example.com"
            receiver = "student@example.com"
            subject = "Error - " + problem
            body = "Please check the system and resolve the issue as soon as possible."
            message = emails.generate_error_report(sender, receiver, subject, body)
            emails.send(message)
        time.sleep(60)   # wait 60 seconds

