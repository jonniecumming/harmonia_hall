from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


# event detail view
class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        booked = Booking.objects.filter(event=event).aggregate(
            total=Sum('number_of_tickets')
        )['total'] or 0
        context['available_seats'] = event.capacity - booked
        context['form'] = BookingForm()
        return context


# create booking view
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "events/booking_form.html"
    success_url = reverse_lazy('bookings')

    def get_object(self):
        """Get the event from the URL slug"""
        return Event.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """Add event and available seats to context"""
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        booked = Booking.objects.filter(event=event).aggregate(
            total=Sum('number_of_tickets')
        )['total'] or 0
        available_seats = event.capacity - booked

        context['event'] = event
        context['available_seats'] = available_seats
        return context

    def form_valid(self, form):
        """Check capacity before saving booking"""
        event = self.get_object()
        tickets_requested = form.cleaned_data['number_of_tickets']

        """Count already booked tickets for this event"""
        booked = Booking.objects.filter(event=event).aggregate(
            total=Sum('number_of_tickets')
        )['total'] or 0

        """Check if tickets available"""
        if booked + tickets_requested > event.capacity:
            form.add_error('number_of_tickets', 'Not enough tickets available. Only {} tickets left.'.format(
                    event.capacity - booked
                ))
            return self.form_invalid(form)

        """Save booking with user and event"""
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.event = event
        booking.save()

        return super().form_valid(form)


# bookings view
class BookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "events/bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        """Return bookings for the logged-in user"""
        return Booking.objects.filter(user=self.request.user)


# update booking view
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "events/booking_form.html"
    success_url = reverse_lazy('bookings')

    def get_queryset(self):
        """Only allow users to edit their own bookings"""
        return Booking.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """Add available seats to context"""
        context = super().get_context_data(**kwargs)
        booking = self.get_object()
        event = booking.event
        
        # Calculate available seats (excluding this booking's current tickets)
        booked = Booking.objects.filter(event=event).exclude(
            id=booking.id
        ).aggregate(total=Sum('number_of_tickets'))['total'] or 0
        available_seats = event.capacity - booked
        
        context['available_seats'] = available_seats
        return context

    def form_valid(self, form):
        """Validate capacity before saving"""
        booking = self.get_object()
        event = booking.event
        new_tickets = form.cleaned_data['number_of_tickets']

        # Get bookings for this event EXCLUDING this booking
        booked = Booking.objects.filter(event=event).exclude(
            id=booking.id
        ).aggregate(total=Sum('number_of_tickets'))['total'] or 0

        # Check if new total exceeds capacity
        if booked + new_tickets > event.capacity:
            form.add_error('number_of_tickets', 'Not enough tickets available. Only {} tickets left.'.format(
                    event.capacity - booked
                ))
            return self.form_invalid(form)

        return super().form_valid(form)


# delete booking view
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = "events/booking_confirm_delete.html"
    success_url = reverse_lazy('bookings')

    def get_queryset(self):
        """Only allow users to delete their own bookings"""
        return Booking.objects.filter(user=self.request.user)
