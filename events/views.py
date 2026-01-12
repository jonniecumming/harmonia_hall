from django.shortcuts import render
from django.views.generic import ListView

from .models import Event
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

# query to fetch all events in db will go here
