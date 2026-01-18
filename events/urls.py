from django.urls import path

from .views import BookingCreateView, BookingsView, EventDetailView, EventListView, HomeView, BookingUpdateView, BookingDeleteView

# URL patterns for events app
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookings/', BookingsView.as_view(), name='bookings'),
    path('bookings/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking-update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<slug:slug>/book/', BookingCreateView.as_view(), name='book-event'),
]
