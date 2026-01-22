from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone

from .models import Event, Booking
from .forms import BookingForm


# Mixin for booking capacity validation
class BookingValidationMixin:
    """
    Mixin providing ticket capacity validation.

    Validates that requested tickets don't exceed availability and adds
    form errors if booking violates capacity constraints.
    """

    def validate_booking_capacity(
        self, form, event, exclude_booking=None
    ):
        """
        Validate sufficient tickets are available for booking.

        Args:
            form: BookingForm instance with cleaned data
            event: Event being booked
            exclude_booking: Booking to exclude from
            capacity check (for updates)

        Returns:
            bool: True if capacity valid, False with form errors if not
        """
        tickets_requested = form.cleaned_data["number_of_tickets"]
        available = event.get_available_seats(
            exclude_booking=exclude_booking
        )

        if tickets_requested > available:
            if available == 0:
                form.add_error(
                    "number_of_tickets",
                    "This event is fully booked. " "No tickets are available.",
                )
            else:
                form.add_error(
                    "number_of_tickets",
                    f"You requested {tickets_requested} tickets but "
                    f"only {available} ticket(s) available. "
                    "Please reduce your quantity.",
                )
            return False
        return True


# home view
class HomeView(ListView):
    """Display upcoming events on homepage with carousel."""

    model = Event
    template_name = "events/index.html"
    context_object_name = "events"
    paginate_by = 6

    def get_queryset(self):
        """Return published events from today onwards, ordered by date."""
        today = timezone.now().date()
        return Event.objects.filter(
            status=1, date__gte=today
        ).order_by("date", "time")

    def get_context_data(self, **kwargs):
        """Add next 5 upcoming events for carousel to context."""
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context["carousel_events"] = Event.objects.filter(
            status=1, date__gte=today
        ).order_by("date", "time")[:5]
        return context


# list view for events
class EventListView(ListView):
    """Display all upcoming events in paginated list."""

    model = Event
    template_name = "events/whats_on.html"
    context_object_name = "events"
    paginate_by = 6

    def get_queryset(self):
        """Return published events from today onwards, ordered by date."""
        today = timezone.now().date()
        return Event.objects.filter(
            status=1, date__gte=today
        ).order_by("date", "time")


# event detail view
class EventDetailView(DetailView):
    """Display full event details and booking form."""

    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        """Return only published events."""
        return Event.objects.filter(status=1)

    def get_context_data(self, **kwargs):
        """Add available seats and blank booking form to context."""
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context["available_seats"] = event.get_available_seats()
        context["form"] = BookingForm()
        return context


# create booking view
class BookingCreateView(
    LoginRequiredMixin,
    BookingValidationMixin,
    SuccessMessageMixin,
    CreateView,
):
    """Create a new booking for an event.

    Validates user authentication, ticket availability, and
    prevents duplicate bookings.
    """

    model = Booking
    form_class = BookingForm
    template_name = "events/booking_form.html"
    success_url = reverse_lazy("bookings")

    def get_success_message(self, cleaned_data):
        """Return confirmation message with booking details and total cost."""
        booking = self.object
        total = booking.get_total_cost()
        return (
            f"✓ Booking confirmed! You have reserved "
            f"{booking.number_of_tickets} ticket(s) for "
            f"{booking.event.title}. This will be payable on "
            f"entry. Total: £{total}"
        )

    def get_object(self):
        """Retrieve the event by slug from URL parameters."""
        return Event.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        """Add event and available seats to context."""
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context["event"] = event
        context["available_seats"] = event.get_available_seats()
        return context

    def form_valid(self, form):
        """Validate booking, prevent duplicates, and assign user and event."""
        event = self.get_object()

        # Prevent duplicate bookings - users can only update existing ones
        existing_booking = Booking.objects.filter(
            user=self.request.user, event=event
        ).exists()

        if existing_booking:
            form.add_error(
                None,
                "You already have a booking for this event. "
                "Please edit your existing booking to change "
                "the number of tickets.",
            )
            return self.form_invalid(form)

        if not self.validate_booking_capacity(form, event):
            return self.form_invalid(form)

        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.event = event
        booking.save()

        self.object = booking

        return super().form_valid(form)


# bookings view
class BookingsView(LoginRequiredMixin, ListView):
    """Display user's bookings and allow editing/deletion."""

    model = Booking
    template_name = "events/bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        """Return bookings for the logged-in user only."""
        return Booking.objects.filter(user=self.request.user)


# update booking view
class BookingUpdateView(
    LoginRequiredMixin,
    BookingValidationMixin,
    SuccessMessageMixin,
    UpdateView,
):
    """Update an existing booking's ticket quantity.

    Validates availability excluding current booking to allow reducing tickets.
    """

    model = Booking
    form_class = BookingForm
    template_name = "events/booking_form.html"
    success_url = reverse_lazy("bookings")

    def get_queryset(self):
        """Return only the current user's bookings."""
        return Booking.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        """Add available seats (excluding current booking) to context."""
        context = super().get_context_data(**kwargs)
        booking = self.get_object()
        event = booking.event
        context["available_seats"] = event.get_available_seats(
            exclude_booking=booking
        )
        return context

    def form_valid(self, form):
        """Validate capacity and save updated booking quantity."""
        booking = self.get_object()
        event = booking.event

        # Exclude current booking from availability check to allow reductions
        if not self.validate_booking_capacity(
            form, event, exclude_booking=booking
        ):
            return self.form_invalid(form)

        self.object = form.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """Return updated booking confirmation with new total."""
        booking = self.object
        total = booking.get_total_cost()
        return (
            f"✓ Booking updated! You now have "
            f"{booking.number_of_tickets} ticket(s) for "
            f"{booking.event.title}. This will be payable on "
            f"entry. Total: £{total}"
        )


# delete booking view
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a booking after confirmation."""

    model = Booking
    template_name = "events/booking_confirm_delete.html"
    success_url = reverse_lazy("bookings")

    def get_queryset(self):
        """Return only the current user's bookings."""
        return Booking.objects.filter(user=self.request.user)


# about view
class AboutView(TemplateView):
    """Display static about page."""

    template_name = "about.html"
