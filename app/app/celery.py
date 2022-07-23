import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_2s': {
        'task': 'broadcast.tasks.get_joke',
        'schedule': 2.0
    }
}

""" Para inicializar o processo e preciso chamar a função celery -A app beat/worker -l INFO"""

app.autodiscover_tasks()