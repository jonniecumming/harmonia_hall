from django.contrib import admin
from .models import Event, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


# Customize Event admin
class EventAdmin(SummernoteModelAdmin):

    list_display = ("title", "date", "time", "venue", "capacity", "price", "status")
    list_filter = ("status", "date", "venue")
    search_fields = ("title", "venue", "description")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("description",)

    fieldsets = (
        ("Event Details", {"fields": ("title", "slug", "venue", "date", "time")}),
        ("Pricing & Capacity", {"fields": ("price", "capacity")}),
        ("Content", {"fields": ("summary", "description", "event_image")}),
        ("Settings", {"fields": ("status",)}),
    )


# Customize Booking admin
class BookingAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "event", "number_of_tickets", "booking_date")
    list_filter = ("booking_date", "event")
    search_fields = ("user__username", "event__title")
    readonly_fields = ("booking_date",)


admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
