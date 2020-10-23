
from .models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
    ]


# Register your models here.
admin.site.register(Event)