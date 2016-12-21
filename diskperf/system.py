#!/usr/bin/env python
# -*- encoding: UTF8 -*-

"""
  report CPU & memory info on the "data" thread/process
  to the server at approximately 10 second intervals.

  process
  cpu
  memory
"""
from celery import Celery


app = Celery('tasks', broker='pyamqp://guest@localhost//')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='America/Denver',
    enable_utc=True,
)


@app.task
def add(x, y):
    return x + y

