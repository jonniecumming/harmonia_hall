from django.urls import path

from .views import BookingsView, EventDetailView, EventListView, HomeView, WhatsOnView

# URL patterns for events app
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('bookings/', BookingsView.as_view(), name='bookings'),
    path('whats-on/', WhatsOnView.as_view(), name='whats-on'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event-detail'),
]
