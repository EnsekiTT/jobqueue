from celery import Celery
import time
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def task(message):
    time.sleep(10) #時間のかかるタスクのフリをする
    return "Hello {0}".format(message) 
