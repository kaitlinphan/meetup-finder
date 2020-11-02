import datetime

from django.db import models
from django.utils import timezone
from django_google_maps import fields as map_fields
# from geoposition.fields import GeopositionField


class Event(models.Model):
    title = models.CharField('Title',max_length=200)
    location = models.CharField('Location', max_length=150)
    info = models.TextField()
    image = models.FilePathField()

class Map(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

# class PointOfInterest(models.Model):
#     name = models.CharField(max_length=100)
#     position = GeopositionField()