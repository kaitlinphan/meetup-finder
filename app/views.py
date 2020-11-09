from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Event

from app.forms import EventForm


from userAccount.models import User

import datetime


# Create your views here.
class HomeView(generic.ListView):
    template_name = 'app/home.html'
    context_object_name = 'event_list'

def event_index(request):
    user_email = request.user.get_username()
    user = User.objects.get(pk=user_email)
    user.save()

    events = Event.objects.all()
    context = {
        'events': events,
        'user' : user.username
    }
    return render(request, 'app/event_index.html', context)

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    context = {
        'event': event
    }
    return render(request, 'app/event_detail.html', context)

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(event_index)
    else:
        form = EventForm()
    return render(request, 'app/create_event.html', {'form': form})

from django.forms import ModelForm
def register(request, pk):
    event = Event.objects.get(pk=pk)
    
    user_email = request.user.get_username()
    
    user = User.objects.get(pk=user_email)
    
    user_name = user.username

    qset = user.EVENTS.filter(pk=event.pk)

    if not qset:
        user.EVENTS.add(event)
    user.save()
    

    context = {
        'events': user.EVENTS.all(),
        'user' : user_name
    }
    return render(request, 'app/welcome.html', context)