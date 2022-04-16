from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reservations.forms import AjoutChambreForm, AjoutReservationForm
from reservations.models import Chambre, Reservation


def home(request):
    if request.method == 'POST':
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        if len(Reservation.objects.all())==0:
            searchResult=Chambre.objects.all()
        else:
            searchResult= Chambre.objects.raw(
                'SELECT  "c"."id","c"."prix","c"."chambre_status","c"."chambre_type" FROM "reservations_chambre" AS "c" WHERE "c"."id" NOT IN ( SELECT "r"."chambre_id" FROM "reservations_reservation" AS "r" WHERE "'+fromdate+'" BETWEEN "r"."debut_sejour"  AND "r"."fin_sejour" OR "'+todate+'" BETWEEN "r"."debut_sejour"  AND "r"."fin_sejour" AND "r"."debut_sejour" BETWEEN "'+fromdate+'" AND "'+todate+'" AND "r"."fin_sejour" BETWEEN "'+fromdate+'" AND "'+todate+'") ORDER BY "c"."id"')


        count_result=len(searchResult)
        if count_result==0:
            messages.warning(request,"Desole,les chambres non-disponibles!")
        else:
            messages.success(request,str(count_result)+" chambres disponibles!")
        return render(request, 'accueil.html', {'data': searchResult, 'count': count_result})
    else:
        return render(request, 'accueil.html')


@login_required
def panel(request):
    if not request.user.is_staff:
        return HttpResponse("Acces refusee")

    total_chambres = len(Chambre.objects.all())
    chambres_disponible = len(Chambre.objects.all().filter(chambre_status='disponible'))

    if total_chambres != 0:
        if chambres_disponible != 0:
            disponible_percent = int(chambres_disponible / total_chambres * 100)
    else:
        disponible_percent = 1

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

    chambres = Chambre.objects.all()  # listes de Chambre
    total_chambres = len(chambres)
    if not chambres:

        messages.warning(request, "Pas de Chambre trouves")

    return HttpResponse(
        render(request, 'chambres.html', {'form': form, 'chambres': chambres, 'total_chambres': total_chambres}))


@login_required
def ajout_reservations(request,pk):
    if  request.user.is_staff:
        messages.warning(request, "Ouff! vous n'est pas un Client.. connectez-vous")
        return render(request, 'accueil.html')
    chambre_id=get_object_or_404(Chambre,pk=pk)

    if request.method == 'POST':
        form = AjoutReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = request.user
            reservation.chambre = chambre_id
            reservation.save()
            return redirect('home')

    else:
        form = AjoutReservationForm()
    #     listes de reservations
    reservations = Reservation.objects.all()
    # if not reservations:
    #     messages.warning(request, "Pas de Chambre trouves")

    return render(request, 'reservation.html', {'form': form, 'reservations': reservations, 'chambre_id': chambre_id,})

@login_required
def listReservation(request):
    if not  request.user.is_staff:
        messages.warning(request, "Ouff! vous n'est pas un Staff.. connectez-vous")
        return render(request, 'accueil.html')
    listReservations=Reservation.objects.all()
    if listReservations ==0:
        messages.warning(request, "Pas de Reservation trouves")
    return render(request,'listReservations.html',{'reservations':listReservations})

@login_required
def mesReservation(request):
    if  request.user.is_staff:
        messages.warning(request, "Ouff! vous n'est pas un Client.. connectez-vous")
        return render(request, 'accueil.html')

    mesReservations=Reservation.objects.all()
    if mesReservations == 0:
        messages.warning(request, "Pas de Reservations trouvees")
    return render(request,'mesReservations.html',{'reservations':mesReservations})
