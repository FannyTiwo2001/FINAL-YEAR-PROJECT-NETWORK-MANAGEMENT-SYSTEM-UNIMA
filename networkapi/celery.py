from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','networkapi.settings')

app = Celery('networkapi')

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()