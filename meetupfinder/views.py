  
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone




def welcome(request):
    return render(request, 'app/welcome.html', {'name': request.user.get_username()})
