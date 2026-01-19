from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone

from .models import Event, Booking
from .forms import BookingForm


# Mixin for booking capacity validation
class BookingValidationMixin:
    """Mixin to validate booking capacity"""

    def validate_booking_capacity(self, form, event, exclude_booking=None):
        """Check if enough tickets are available"""
        tickets_requested = form.cleaned_data['number_of_tickets']
        available = event.get_available_seats(exclude_booking=exclude_booking)

        if tickets_requested > available:
            if available == 0:
                form.add_error('number_of_tickets', 'This event is fully booked. No tickets are available.')
            else:
                form.add_error('number_of_tickets', f'You requested {tickets_requested} tickets but only {available} ticket(s) available. Please reduce your quantity.')
            return False
        return True


# home view
class HomeView(ListView):
    model = Event
    template_name = "events/index.html"
    context_object_name = "events"
    paginate_by = 6

    def get_queryset(self):
        """Only show published events from today onwards"""
        today = timezone.now().date()
        return Event.objects.filter(
            status=1,
            date__gte=today
        ).order_by('date', 'time')


# list view for events
class EventListView(ListView):
    model = Event
    template_name = "events/whats_on.html"
    context_object_name = "events"
    paginate_by = 6

    def get_queryset(self):
        """Only show published events from today onwards"""
        today = timezone.now().date()
        return Event.objects.filter(
            status=1,
            date__gte=today
        ).order_by('date', 'time')


# event detail view
class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        """Only allow viewing published events"""
        return Event.objects.filter(status=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context['available_seats'] = event.get_available_seats()
        context['form'] = BookingForm()
        return context


# create booking view
class BookingCreateView(LoginRequiredMixin, BookingValidationMixin, SuccessMessageMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "events/booking_form.html"
    success_url = reverse_lazy('bookings')

    def get_success_message(self, cleaned_data):
        booking = self.object
        total = booking.get_total_cost()
        return f'✓ Booking confirmed! You have reserved {booking.number_of_tickets} ticket(s) for {booking.event.title}. This will be payable on entry. Total: £{total}'

    def get_object(self):
        """Get the event from the URL slug"""
        return Event.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """Add event and available seats to context"""
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context['event'] = event
        context['available_seats'] = event.get_available_seats()
        return context

    def form_valid(self, form):
        """Check capacity and prevent duplicate bookings"""
        event = self.get_object()

        # Check if user already has a booking for this event
        existing_booking = Booking.objects.filter(
            user=self.request.user,
            event=event
        ).exists()

        if existing_booking:
            form.add_error(None, 'You already have a booking for this event. Please edit your existing booking to change the number of tickets.')
            return self.form_invalid(form)

        if not self.validate_booking_capacity(form, event):
            return self.form_invalid(form)

        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.event = event
        booking.save()

        # Store booking in self.object so get_success_message can access it
        self.object = booking

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
class BookingUpdateView(LoginRequiredMixin, BookingValidationMixin, SuccessMessageMixin, UpdateView):
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
        context['available_seats'] = event.get_available_seats(exclude_booking=booking)
        return context

    def form_valid(self, form):
        """Validate capacity and store booking for success message"""
        booking = self.get_object()
        event = booking.event

        # Validate capacity (exclude current booking from calculation)
        if not self.validate_booking_capacity(form, event, exclude_booking=booking):
            return self.form_invalid(form)

        # Save the form and store in self.object for get_success_message
        self.object = form.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """Display success message with updated ticket count and total cost"""
        booking = self.object
        total = booking.get_total_cost()
        return f'✓ Booking updated! You now have {booking.number_of_tickets} ticket(s) for {booking.event.title}. This will be payable on entry. Total: £{total}'


# delete booking view
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = "events/booking_confirm_delete.html"
    success_url = reverse_lazy('bookings')

    def get_queryset(self):
        """Only allow users to delete their own bookings"""
        return Booking.objects.filter(user=self.request.user)


# about view
class AboutView(TemplateView):
    template_name = "about.html"
