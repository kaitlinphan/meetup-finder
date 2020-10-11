from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
]