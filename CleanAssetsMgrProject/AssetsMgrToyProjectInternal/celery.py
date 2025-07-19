from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssetsMgrToyProjectInternal.settings')

#celery app instance setting
app = Celery('AssetsMgrToyProjectInternal')

# django setting celery and transmission
app.config_from_object('django.conf:settings',namespace='CELERY')

#task.py asynchronous worker automation search setting
app.autodiscover_tasks()
