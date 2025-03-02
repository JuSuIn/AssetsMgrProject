from celery import shared_task

#ex worker
@shared_task
def my_task():
    print("Task is executed!")