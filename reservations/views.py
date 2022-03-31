from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from reservations.forms import AjoutChambreForm
from reservations.models import Chambre


def home(request):
    return render(request, 'home.html', {})


@login_required
def ajoutChambre(request):
    if not request.user.is_staff:
        return HttpResponse("Acces refusee")

    if request.method == 'POST':
        form = AjoutChambreForm(request.POST)
        if form.is_valid():
            chambre = form.save(commit=False)

            chambre.save()

            return redirect('home')
    else:
        form = AjoutChambreForm()
    return render(request, 'ajout_Chambre.html', {'form': form})

