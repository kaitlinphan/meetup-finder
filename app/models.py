import datetime

from django.db import models
from django.utils import timezone


class EventManager(models.Manager):
    def create_event(self, title, location, info, image):
        event = self.create(title=title, location=location, info=info, image=image)
        return event


class Event(models.Model):
    title = models.CharField('Title',max_length=200)
    location = models.CharField('Location', max_length=150)
    info = models.TextField()
    image = models.FilePathField(path=None)

    objects = EventManager()
