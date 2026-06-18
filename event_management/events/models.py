from django.db import models
from django.contrib.auth.models import User


# =====================================
# EVENT MODEL
# =====================================

class Event(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()
   
    venue = models.CharField(
        max_length=200
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()

    time = models.TimeField()

    total_tickets = models.PositiveIntegerField(
        default=0
    )

    available_tickets = models.PositiveIntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to='event_images/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.title


# =====================================
# BOOKING MODEL
# =====================================

class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    quantity = models.PositiveIntegerField()

    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    qr_code = models.ImageField(
        upload_to='qr_codes/',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.event.title}"
        )


# =====================================
# CONTACT MODEL (OPTIONAL)
# =====================================

class Contact(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name