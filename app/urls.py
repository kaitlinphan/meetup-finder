from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('', views.event_index, name='event_index'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create_event'),
]