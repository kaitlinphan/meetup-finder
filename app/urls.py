from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_index, name='event_index'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
<<<<<<< HEAD
    path('create/', views.create_event, name='create_event'),
=======

    path('<int:pk>/register/', views.register, name='register'),
>>>>>>> bm2pr
]