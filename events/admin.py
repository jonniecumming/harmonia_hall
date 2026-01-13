from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# Add events model here when created
admin.site.register(Event)
