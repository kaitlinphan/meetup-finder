import datetime

from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField('Title',max_length=200)
    location = models.CharField('Location', max_length=150)
    info = models.TextField()
    image = models.FilePathField()