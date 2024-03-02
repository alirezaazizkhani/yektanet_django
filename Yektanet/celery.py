import os
from celery import Celery
from celery.schedules import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Yektanet.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
#app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task1': {
        'task': 'mangement_advertiser.tasks.calculate_clicks_hour',
        'schedule': timedelta(seconds=3600),  
    },
    'task2': {
        'task': 'mangement_advertiser.tasks.calculate_views_hour',  
        'schedule': timedelta(seconds=3600),  
    },
    'task3': {
        'task': 'mangement_advertiser.tasks.calculate_clicks_days',  
        'schedule': timedelta(seconds=3600*24),  
    },
    'task4': {
        'task': 'mangement_advertiser.tasks.calculate_views_days',  
        'schedule': timedelta(seconds=3600*24),  
    },
}