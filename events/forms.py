from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["number_of_tickets"]

    def clean_number_of_tickets(self):
        """Validate that number of tickets is positive"""
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
