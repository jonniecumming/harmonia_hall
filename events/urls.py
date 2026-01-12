from django.urls import path

from .views import EventListView

# URL patterns for events app
urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
]
