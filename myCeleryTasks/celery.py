from __future__ import absolute_import
from celery import Celery

app = Celery('myCeleryTasks', include=['myCeleryTasks.tasks'])
app.config_from_object('myCeleryTasks.config')
