from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField('Title', max_length=200)
    location = models.CharField('Location', max_length=150)
    info = models.TextField()
    image = models.ImageField(upload_to="images")


class RegisteredEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
