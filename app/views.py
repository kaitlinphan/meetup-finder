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

def create_event(request):
    message = ""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Event submitted!"
    else:
        message = "Fill out all fields before submitting."
    return render(request, 'app/create_event.html', {'form': EventForm(), 'message': message})

from django.forms import ModelForm
def register(request, pk):
    event = Event.objects.get(pk=pk)
    
    user_email = request.user.get_username()
    user = User.objects.get(pk=user_email)


    qset = user.EVENTS.filter(pk=event.pk)

    if not qset:
        user.EVENTS.add(event)
        user.save()
    
    
    '''
    is_in = False
    if (event in user.EVENTS):  
        is_in = True

    if (not is_in):
        user.EVENTS.add(event)
        user.save()'''
    
    
    

    context = {
        'events': user.EVENTS.all()
    }
    return render(request, 'app/welcome.html', context)