from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .models import Event, Booking
from .forms import BookingForm
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
    context_object_name = "events"


# event detail view
class EventDetailView(ListView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"


# bookings view
class BookingsView(ListView):
    model = Booking
    template_name = "events/bookings.html"
    context_object_name = "bookings"


# create booking view
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "events/booking_form.html"
    success_url = reverse_lazy('bookings')

    def get_object(self):
        """Get the event from the URL slug"""
        return Event.objects.get(slug=self.kwargs['slug'])

    def form_valid(self, form):
        """Check capacity before saving booking"""
        event = self.get_object()
        tickets_requested = form.cleaned_data['number_of_tickets']

        # Count already booked tickets for this event
        booked = Booking.objects.filter(event=event).aggregate(
            total=Sum('number_of_tickets')
        )['total'] or 0

        # Check if tickets available
        if booked + tickets_requested > event.capacity:
            form.add_error('number_of_tickets', 'Not enough tickets available. Only {} tickets left.'.format(
                    event.capacity - booked
                ))
            return self.form_invalid(form)

        # Save booking with user and event
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.event = event
        booking.save()

        return super().form_valid(form)
