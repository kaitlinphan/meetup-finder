import datetime

from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField('Title',max_length=200)
    location = models.CharField('Location', max_length=150)
    info = models.TextField()
    starts = models.DateTimeField('Starts')
    ends = models.DateTimeField('Ends')
    pub_date = models.DateTimeField('pub_date')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'