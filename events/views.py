from django.shortcuts import render
from django.views.generic import ListView

from .models import Event, Booking
# Create your views here.


# home view
class HomeView(ListView):
    model = Event
    template_name = "events/index.html"
    paginate_by = 6


# list view for events
class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"


# list view for what's on
class WhatsOnView(ListView):
    model = Event
    template_name = "events/whats_on.html"
    context_object_name = "whats_on"


# bookings view
class BookingsView(ListView):
    model = Booking
    template_name = "events/bookings.html"
    context_object_name = "bookings"
