from os import environ

from celery import Celery
from celery.schedules import crontab


def make_celery():
    celery = Celery(
        "TASKS",
        # backend=environ.get('BACKEND', 'db+postgresql://user:password@host:port/database'),
        broker=environ.get('BROKER', 'redis://redis:6379/0'),
    )
    return celery


app = make_celery()
app.conf.timezone = 'America/Sao_Paulo'
app.conf.enable_utc = True
app.conf.beat_schedule = {
    'add-every-min': {
        'task': 'task.ping',
        'schedule': crontab(minute='*/1')
    },
    'add-every-half-hour': {
        'task': 'task.print_on_terminal',
        'schedule': crontab(minute='*/30'),
        'args': ('Cool', 'Every 30m')
    },
    'add-every-midnight': {
        'task': 'task.check_db',
        'schedule': crontab(hour=10, minute=31)
    }
}
