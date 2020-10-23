from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Event
import datetime

# Create your views here.
class HomeView(generic.ListView):
    template_name = 'app/home.html'
    context_object_name = 'event_list'

def event_index(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'app/event_index.html', context)

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    context = {
        'event': event
    }
    return render(request, 'app/event_detail.html', context)



def register(request, pk):
    event = Event.objects.get(pk=pk)
    context = {
        'event': event
    }
    return render(request, 'app/welcome.html', context)