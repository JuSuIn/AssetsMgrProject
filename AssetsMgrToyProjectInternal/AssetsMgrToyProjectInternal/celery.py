from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


#django basic setting load
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssetsMgrToyProjectInternal.settings')

app = Celery('AssetsMgrToyProjectInternal')

#Celery Django setting amalgamation load
app.config_from_object('django.conf:settings',namespace='CELERY')

# Django app task module automation
app.autodiscover_tasks()

# celery beat Cycle settings
app.conf.beat_schedule = {
    'run_debug_task_every_3_seconds': {
    #'add-every-30-seconds': {
        'task' : 'AsStock.tasks.debug_task',
        'schedule': 3.0,  # 3초마다 실행
        'args' : (1,2), #원하는 인자 전달
        #'schedule' : crontab(minute='*/30'), #30 minutes
    },
}

@app.task(bind=True)
def debug_task(self,x,y):
    print(f"Request: {self.request!r}")
    print(f"Arguments: {x}, {y}")
    return x + y
