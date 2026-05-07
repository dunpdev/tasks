from celery import shared_task
from time import sleep

@shared_task
def notify_user(message):
    print(f"Notification: {message}")
    sleep(5) 
    print("Notification sent!")