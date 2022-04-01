from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from reservations.forms import AjoutChambreForm
from reservations.models import Chambre


def home(request):
    return render(request, 'home.html', {})


@login_required
def panel(request):
    global total_chambres

    if not request.user.is_staff:
        return HttpResponse("Acces refusee")

    total_chambres = len(Chambre.objects.all())
    chambres_disponible = len(Chambre.objects.all().filter(chambre_status='disponible'))
    disponible_percent = int(chambres_disponible / total_chambres * 100)

    response = render(request, 'staff/panel.html', {
        'total_chambres': total_chambres,
        'chambres_disponible': chambres_disponible,
        'disponible_percent': disponible_percent,
    })

    return HttpResponse(response)





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

    return HttpResponse(
        render(request, 'chambres.html', {'form': form, 'chambres': chambres}))
