from django.contrib import admin
from .models import Event, Booking
from django_summernote.admin import SummernoteModelAdmin


class EventAdmin(SummernoteModelAdmin):
    """Customized admin for Event model with rich text editing."""

    list_display = (
        "title",
        "date",
        "time",
        "venue",
        "capacity",
        "get_total_tickets_sold",
        "price",
        "status",
    )
    list_filter = ("status", "date", "venue")
    search_fields = ("title", "venue", "description")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)
    readonly_fields = ("get_total_tickets_sold",)

    fieldsets = (
        ("Event Details", {
            "fields": ("title", "slug", "venue", "date", "time")}),
        ("Pricing & Capacity", {"fields": ("price", "capacity")}),
        ("Content", {"fields": ("summary", "description", "event_image")}),
        ("Settings", {"fields": ("status",)}),
    )


class BookingAdmin(admin.ModelAdmin):
    """Customized admin for Booking model with filtering and search."""

    list_display = ("id", "user", "event", "number_of_tickets", "booking_date")
    list_filter = ("booking_date", "event")
    search_fields = ("user__username", "event__title")
    readonly_fields = ("booking_date",)


admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
