from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.event_index, name='event_index'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create_event'),
    path('profile/', views.profile, name='profile'),

    path('<int:event_id>/register/', views.register, name='register'),
    path('<int:event_id>/unregister/', views.unregister, name='unregister'),
]