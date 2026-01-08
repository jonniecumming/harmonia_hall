from django.db import models

# Create your models here.

# events model
class Event(models.Model):
    title = models.VarCharField(max_length=200)
    venue = models.VarCharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    capacity = models.IntegerField()
    price = models.number.DecimalField(max_digits=5, decimal_places=2)


# bookings model

# users model