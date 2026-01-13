from django.urls import path

from .views import EventListView, BookingsView, HomeView

# URL patterns for events app
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('bookings/', BookingsView.as_view(), name='bookings'),
]
