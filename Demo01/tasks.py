# coding=utf-8
from celery import Celery
# celery 的相关配置
celery = Celery('tasks', broker='redis://localhost:6379/0')
# 具体任务(执行两个数相加)
@celery.task
def add(x, y):
    return x + y
