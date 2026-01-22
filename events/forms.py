from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and updating event bookings."""

    class Meta:
        model = Booking
        fields = ["number_of_tickets"]

    def clean_number_of_tickets(self):
        """Validate tickets: non-empty, positive, and within limit (max 10)."""
        number_of_tickets = self.cleaned_data.get("number_of_tickets")

        if number_of_tickets is None:
            raise forms.ValidationError("Please enter a number of tickets.")

        if number_of_tickets <= 0:
            raise forms.ValidationError(
                "Number of tickets must be at least 1."
            )

        if number_of_tickets > 10:
            raise forms.ValidationError("Maximum 10 tickets per booking.")

        return number_of_tickets
