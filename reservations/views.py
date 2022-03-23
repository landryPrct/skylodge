from django.shortcuts import render
from .models import Chambre, Reservation, Paiement
from django.views.generic import ListView


# Create your views here.


class ChambreView(ListView):
    model = Chambre
    context_object_name = 'chambres'
    template_name = 'home.html'
