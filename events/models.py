from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


# events model
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    venue = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['date', 'time']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.date} at {self.time}'


# bookings model
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    number_of_tickets = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking by {self.user.username} for {self.event.title} - {self.number_of_tickets} tickets'

# users model
