from celery import shared_task

@shared_task(bind=True)
def debug_task(self,x,y):
    print(f"Request: {self.request!r}")
    print(f"Arguments: {x}, {y}")
    return x + y