from django.shortcuts import render  # noqa: F401 (noqa tells the linter to ignore unused import)
from django.views.generic import ListView

from .models import Event
# Create your views here.


class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

# query to fetch all events in db will go here
