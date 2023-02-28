import time
from celery import shared_task, task

@shared_task
def send_mass_emails(rec):
    print(rec)
    print('started sleep mode')
    print('wake up from sleep')
    return

@task
def send_scheduled_email():
    pass
