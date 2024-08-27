import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'products.tasks.send_spam_every_5_second',
        'schedule': 5.0,
 }
}