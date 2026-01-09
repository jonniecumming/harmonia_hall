from django.db import models
from django.contrib.auth.models import User  # noqa: F401 (noqa tells the Flake8 to ignore unused import for now)
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


# events model
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    venue = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.date} at {self.time}'

# bookings model


# users model
