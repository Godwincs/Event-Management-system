from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('events/', views.event_list, name='event_list'),

    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('event/<int:id>/', views.event_detail, name='event_detail'),

    path('book/<int:id>/', views.book_ticket, name='book_ticket'),

    path(
        'booking-success/<int:id>/',
        views.booking_success,
        name='booking_success'
    ),

    path(
        'my-bookings/',
        views.my_bookings,
        name='my_bookings'
    ),
    path(
    'event/<int:pk>/edit/',
    views.edit_event,
    name='edit_event'
),

path(
    'event/<int:pk>/delete/',
    views.delete_event,
    name='delete_event'
),

    path(
        'create-event/',
        views.create_event,
        name='create_event'
    ),
 
    path(
    'logout/',
    views.user_logout,
    name='logout'
),
    path(
    'download-ticket/<int:id>/',
    views.download_ticket,
    name='download_ticket'
),
]