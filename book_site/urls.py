"""
URL configuration for book_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.conf.urls.static import static
from django.conf import settings

from lending import views
from lending.views import profile_view, profile_update

def force_google_redirect(request):
    return redirect('https://accounts.google.com/o/oauth2/auth?client_id=1017901213595-g6r3svb5t7uemf100dcs5bn3autpv271.apps.googleusercontent.com&redirect_uri=http://127.0.0.1:8000/auth/complete/google-oauth2/&response_type=code&scope=email')

def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/lending/login/')

urlpatterns = [
    path('', lambda request: redirect('lending:index')),
    path('admin/', admin.site.urls),
    path('lending/', include("lending.urls")),
    path('auth/', include('social_django.urls', namespace='social')),
    path('force-login/', force_google_redirect, name='force-google-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/lending/login/'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('my-requests/', views.my_book_requests, name='my_book_requests'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path("return/<int:pk>/", views.return_book, name="return_book"),
    path('notifications/mark-as-read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path("my-books/", views.my_books, name="my_books"),
    path('requests/<int:pk>/cancel/', views.cancel_request, name='cancel_request'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
