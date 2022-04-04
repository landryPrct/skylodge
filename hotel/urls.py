"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from reservations import views as reservations_views

urlpatterns = [
    path('', reservations_views.home, name='home'),

    # path('home', reservations_views.ajout_reservations, name='home'),
    path('hotel/user/room/<int:pk>/reservation', reservations_views.ajout_reservations, name='reservation'),

    path('admin/', admin.site.urls),
    path('hotel/signup/user', accounts_views.user_signup, name='user_signup'),
    path('hotel/signup/staff', accounts_views.staff_signup, name='staff_signup'),
    path('hotel/login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('hotel/staff/chambres', reservations_views.ajoutChambre, name='chambres'),
    path('hotel/staff/panel', reservations_views.panel, name='panel'),
    # path('hotel/user/reservation', reservations_views.ajout_reservations, name='reservation'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
