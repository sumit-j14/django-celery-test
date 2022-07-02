# these are the basic celery.py settings

from __future__ import absolute_import
import os
from celery import Celery
from celery.utils.time import timezone
from django.conf import settings

# here you have to enter the main project folder name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
app = Celery('django_celery')

# below lines for changing the defualt time zone
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

# Celery Beat Settings

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))