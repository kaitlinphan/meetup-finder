from django.contrib import admin
from .models import Event
from .models import Map
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
    ]

class MapAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

# Register your models here.
admin.site.register(Event)