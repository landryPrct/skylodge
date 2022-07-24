"""skylodge URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from reservations import views as reservations_views

urlpatterns = [
    path('', reservations_views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('users/', reservations_views.listUsers, name='list-user'),
    # path('home', reservations_views.ajout_reservations, name='home'),
    path('skylodge/user/room/<int:pk>/reservation/<str:fromdate>/<str:todate>', reservations_views.ajout_reservations, name='reservation'),

    path('admin/', admin.site.urls),
    path('skylodge/signup/user', accounts_views.user_signup, name='user_signup'),
    path('skylodge/signup/staff', accounts_views.staff_signup, name='staff_signup'),
    path('skylodge/login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('skylodge/staff/panel', reservations_views.panel, name='panel'),

    path('skylodge/historique', reservations_views.historiqueReservations, name='history'),
    path('skylodge/reservation/delete/<int:pk>', reservations_views.delete_history, name='del-history'),

    path('skylodge/reservations', reservations_views.listReservation, name='list-reservations'),
    path('skylodge/reservation/edit/<int:pk>', reservations_views.update_reservation, name='update_reservation'),
    path('skylodge/reservation/delete/<int:pk>', reservations_views.delete_reservation, name='del-reservation'),

    path('skylodge/categories', reservations_views.ajoutCategorie, name='categorie'),
    path('skylodge/categorie/edit/<int:pk>', reservations_views.update_categorie, name='update_categorie'),
    path('skylodge/categorie/delete/<int:pk>', reservations_views.delete_categorie, name='del-categorie'),

    path('skylodge/chambres', reservations_views.ajoutChambre, name='chambres'),
    path('skylodge/chambre/edit/<int:pk>', reservations_views.update_chambre, name='update_chambre'),
    path('skylodge/chambre/delete/<int:pk>', reservations_views.delete_chambre, name='del-chambre'),


    path('skylodge/res/payment_opt/<int:latest>/<int:amount>',reservations_views.payment_options, name='pay_opt'),
    path('skylodge/res/pay_ihela/<slug:bank_slug>/<int:amount>/<int:pk>',reservations_views.pay_with_ihela, name='pay_ihela')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
