from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


# events model
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    venue = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=0)


# bookings model

# users model
