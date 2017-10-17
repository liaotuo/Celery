#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import leijun as leijun_task

def leijun(request):
    leijun_task.delay()
    return HttpResponse(u"[ task is running in background ]")
