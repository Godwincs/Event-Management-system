from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [

    # Admin Panel
    path(
        'admin/',
        admin.site.urls
    ),

    # Event App URLs
    path(
        '',
        include('events.urls')
    ),

    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]


# Media Files

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )