from django.urls import path

from .views import BookingCreateView, BookingsView, EventDetailView, EventListView, HomeView

# URL patterns for events app
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookings/', BookingsView.as_view(), name='bookings'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('whats-on/', EventListView.as_view(), name='whats-on'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<slug:slug>/book/', BookingCreateView.as_view(), name='book-event'),
]
