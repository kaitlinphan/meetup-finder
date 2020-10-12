from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
    ]


# Register your models here.
admin.site.register(Event)