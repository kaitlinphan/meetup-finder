from django.shortcuts import render, redirect, get_object_or_404
from app.models import Event, RegisteredEvents
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.forms import EventForm


# Create your views here.
def event_index(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'app/event_index.html', context)


def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    context = {
        'event': event
    }
    return render(request, 'app/event_detail.html', context)


def create_event(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:event_index'))
    else:
        form = EventForm()
        context = {
            'form': form,
            'logged_in': True
        }
        return render(request, 'app/create_event.html', context)


def register(request, event_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    event = get_object_or_404(Event, pk=event_id)
    # adds event to list of registered events
    if RegisteredEvents.objects.filter(event=event, user=request.user).exists():
        context = {
            'event': event,
            'error_message': "Already registered!",
            'logged_in': True
        }
        return render(request, 'app/event_detail.html', context)
    registered_event = RegisteredEvents(event=event, user=request.user)
    registered_event.save()
    return HttpResponseRedirect(reverse('app:profile'))


def unregister(request, event_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    event = get_object_or_404(Event, pk=event_id)
    # removes event from list of registered events
    RegisteredEvents.objects.filter(event=event, user=request.user).delete()
    return HttpResponseRedirect(reverse('app:profile'))


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    registered_events = RegisteredEvents.objects.filter(user=request.user)
    context = {
        'events': registered_events,
    }
    return render(request, 'app/profile.html', context)


def search(request):
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        events_check_info = Event.objects.filter(info__icontains=query_string)
        events_check_title = Event.objects.filter(title__icontains=query_string)
        events_check_date = Event.objects.filter(day__icontains=query_string)
        events = events_check_info | events_check_title | events_check_date
        return render(request, 'app/event_index.html', {'events': events})
    else:
        events = Event.objects.all()
        return render(request, 'app/event_index.html', {'events': events})