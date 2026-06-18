from django.contrib import admin
from .models import Event, Booking, Contact


# =====================================
# EVENT ADMIN
# =====================================

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'venue',
        'date',
        'time',
        'total_tickets',
        'available_tickets',
        'created_at'
    )

    search_fields = (
        'title',
        'venue'
    )

    list_filter = (
        'date',
        'venue'
    )

    ordering = (
        'date',
        'time'
    )


# =====================================
# BOOKING ADMIN
# =====================================

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'event',
        'quantity',
        'booking_date'
    )

    search_fields = (
        'user__username',
        'event__title'
    )

    list_filter = (
        'booking_date',
    )

    ordering = (
        '-booking_date',
    )


# =====================================
# CONTACT ADMIN
# =====================================

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'subject',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )

    list_filter = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )


# =====================================
# ADMIN PANEL CUSTOMIZATION
# =====================================

admin.site.site_header = "Event Management Admin Panel"

admin.site.site_title = "Event Management"

admin.site.index_title = "Welcome to Event Management Dashboard"