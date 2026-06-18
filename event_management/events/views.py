from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.models import Sum

from .models import Event, Booking
from .forms import RegisterForm, EventForm, BookingForm


# =====================================
# HOME PAGE
# =====================================

def home(request):

    events = Event.objects.all().order_by('-id')

    return render(
        request,
        'home.html',
        {
            'events': events
        }
    )


# =====================================
# EVENT LIST
# =====================================

def event_list(request):

    events = Event.objects.all()

    return render(
        request,
        'event_list.html',
        {
            'events': events
        }
    )


# =====================================
# EVENT DETAIL
# =====================================

def event_detail(request, id):

    event = get_object_or_404(
        Event,
        id=id
    )

    return render(
        request,
        'event_detail.html',
        {
            'event': event
        }
    )


# =====================================
# REGISTER
# =====================================

def register(request):

    if request.method == 'POST':

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            user = User.objects.create_user(

                username=form.cleaned_data[
                    'username'
                ],

                email=form.cleaned_data[
                    'email'
                ],

                password=form.cleaned_data[
                    'password'
                ]
            )

            login(
                request,
                user
            )

            return redirect(
                'home'
            )

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )


# =====================================
# LOGIN
# =====================================

def user_login(request):

    error = None

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                'home'
            )

        else:

            error = "Invalid credentials"

    return render(
        request,
        'login.html',
        {
            'error': error
        }
    )
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_ticket(request, id):

    booking = Booking.objects.get(id=id)

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = f'attachment; filename="ticket_{booking.id}.pdf"'

    p = canvas.Canvas(response)

    p.drawString(
        100,
        800,
        f"Booking ID: {booking.id}"
    )

    p.drawString(
        100,
        780,
        f"Event: {booking.event.title}"
    )

    p.drawString(
        100,
        760,
        f"User: {booking.user.username}"
    )

    p.drawString(
        100,
        740,
        f"Venue: {booking.event.venue}"
    )

    p.drawString(
        100,
        720,
        f"Tickets: {booking.quantity}"
    )

    p.save()

    return response


# =====================================
# LOGOUT
# =====================================

def user_logout(request):

    logout(request)

    return redirect(
        'home'
    )
    
# =====================================
# CREATE EVENT
# =====================================

@login_required
def create_event(request):

    if request.method == 'POST':

        form = EventForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            event = form.save()

            print(
                "Event Created Successfully:",
                event
            )

            return redirect(
                'event_list'
            )

        else:

            print(
                "FORM ERRORS:"
            )

            print(
                form.errors
            )

    else:

        form = EventForm()

    return render(
        request,
        'create_event.html',
        {
            'form': form
        }
    )


# =====================================
# BOOK TICKET
# =====================================

@login_required
def book_ticket(request, id):

    event = get_object_or_404(
        Event,
        id=id
    )

    if request.method == 'POST':

        form = BookingForm(
            request.POST
        )

        if form.is_valid():

            quantity = form.cleaned_data[
                'quantity'
            ]

            if quantity > event.available_tickets:

                return render(
                    request,
                    'book_ticket.html',
                    {
                        'event': event,
                        'form': form,
                        'error':
                        'Tickets not available'
                    }
                )

            booking = form.save(
                commit=False
            )

            booking.user = request.user
            booking.event = event

            booking.save()

            event.available_tickets -= quantity

            event.save()

            return redirect(
                'booking_success',
                booking.id
            )

    else:

        form = BookingForm()

    return render(
        request,
        'book_ticket.html',
        {
            'event': event,
            'form': form
        }
    )


# =====================================
# BOOKING SUCCESS
# =====================================

@login_required
def booking_success(request, id):

    booking = get_object_or_404(
        Booking,
        id=id
    )

    return render(
        request,
        'booking_success.html',
        {
            'booking': booking
        }
    )


# =====================================
# MY BOOKINGS
# =====================================

@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'my_bookings.html',
        {
            'bookings': bookings
        }
    )


# =====================================
# DASHBOARD
# =====================================

@login_required
def dashboard(request):

    total_tickets = Booking.objects.aggregate(
        total=Sum('quantity')
    )['total'] or 0

    context = {

        'total_events':
        Event.objects.count(),

        'total_bookings':
        Booking.objects.count(),

        'total_tickets':
        total_tickets,

        'total_users':
        User.objects.count(),

        'recent_events':
        Event.objects.order_by('-id')[:5]

    }

    return render(
        request,
        'dashboard.html',
        context
    )
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def create_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('event_list')

    else:
        form = EventForm()

    return render(
        request,
        'create_event.html',
        {'form': form}
    )
    
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )

@staff_member_required
def edit_event(request, pk):

    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':

        form = EventForm(
            request.POST,
            request.FILES,
            instance=event
        )

        if form.is_valid():

            form.save()

            return redirect(
                'event_detail',
                id=event.id
            )

    else:

        form = EventForm(instance=event)

    return render(
        request,
        'create_event.html',
        {'form': form}
    )

@staff_member_required
def delete_event(request, pk):

    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':

        event.delete()

        return redirect('event_list')

    return render(
        request,
        'delete_event.html',
        {'event': event}
    )
from events.models import Event

event = Event.objects.last()

print(event.location)