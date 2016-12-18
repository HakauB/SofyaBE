from __future__ import absolute_import, unicode_literals
from celery import shared_task

# Example
@shared_task
def add(x, y):
    return x + y
