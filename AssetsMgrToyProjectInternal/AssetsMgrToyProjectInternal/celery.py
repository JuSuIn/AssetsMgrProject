import os
from celery import Celery

#django basic setting load
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AssetsMgrToyProjectInternal.settings')

app = Celery('AssetsMgrToyProjectInternal')

#Celery Django setting amalgamation load
app.config_from_object('django.conf:settings',namespace='CELERY')

# Django app task module automation
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self,x,y):
    print(f"Request: {self.request!r}")
    print(f"Arguments: {x}, {y}")
    return x + y
