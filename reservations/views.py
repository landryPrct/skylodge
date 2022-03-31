from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    #     listes de Chambre
    chambres = Chambre.objects.all()
    if not chambres:
        messages.warning(request, "Pas de Chambre trouves")
    return render(request, 'chambres.html', {'form': form,'chambres':chambres})

