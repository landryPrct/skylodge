
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from reservations.forms import AjoutChambreForm, AjoutReservationForm, EditReservationForm, AjoutCategorieForm, iHelaClientAccountForm
from reservations.models import Chambre, Reservation,Categorie
from django.contrib.auth.models import User
from accounts.ihela_api  import ihela_bank_list,ihela_api_bill_initiate,ihela_api_customer_lookup
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime,date
from uuid import uuid4

def home(request):

    if request.user.is_staff:
        return redirect('/admin')
    else:
        booking = []
        if request.method == 'POST':
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            if fromdate == '' and todate == '':
                messages.info(request, "Désolé,les champs sont vide !")
                return render(request, "accueil.html")
            elif todate<=fromdate:
                messages.info(request, "Désolé, Veuillez choisir correctement les dates !")
                return render(request, "accueil.html")


            if Reservation.objects.count() == 0:
                searchResult = Chambre.objects.all()
            else:
                # for finding the reserved rooms on this time period for excluding from the query set
                for each_reservation in Reservation.objects.all():
                    if str(each_reservation.debut_sejour) < str(fromdate) and str(each_reservation.fin_sejour) < str(
                            todate):
                             pass
                    elif str(each_reservation.debut_sejour) > str(fromdate) and str(
                            each_reservation.fin_sejour) > str(todate) :
                             pass

                    elif (each_reservation.status !="True"):
                             pass
                    else:
                        booking.append(each_reservation.chambre.id)
                searchResult = Chambre.objects.all().exclude(id__in=booking)
                



            count_result = searchResult.count()




            if count_result == 0:
                messages.info(request, "Désolé,Aucune chambre disponibles pour cette période!")
            else:
                messages.success(request, str(count_result) + " Chambre(s) disponible(s) pour cette période!!")
            return render(request, 'accueil.html', {'data': searchResult, 'count': count_result,"fromdate":fromdate, "todate":todate})
        else:
            return render(request, 'accueil.html')




@login_required
def panel(request):
    if not request.user.is_staff:
        return HttpResponse("Accès refusée")
    total_user = User.objects.filter(is_staff=False).count()
    total_chambres = len(Chambre.objects.all())
    total_reservation = len(Reservation.objects.all())
    chambres_disponible = len(Chambre.objects.all().filter(chambre_status='disponible'))

    if total_chambres != 0:
        if chambres_disponible != 0:
            disponible_percent = int(chambres_disponible / total_chambres * 100)
    else:
        disponible_percent = 1

    response = render(request, 'staff/panel.html', {
        'total_user': total_user,
        'total_chambres': total_chambres,
        'total_reservation': total_reservation,
        'chambres_disponible': chambres_disponible,
        'disponible_percent': disponible_percent,
    })
    return HttpResponse(response)


@login_required
def ajoutCategorie(request):
    if not request.user.is_staff:
        return HttpResponse("Accès refusée")

    if request.method == 'POST':
        form = AjoutCategorieForm(request.POST)
        if not form.is_valid():
            messages.warning(request, 'Veillez complétez tous les champs')
        elif form.is_valid():
            categorie = form.save(commit=False)


            if Categorie.objects.filter(type=form.cleaned_data['type']).exists():

                messages.info(request,'cette categorie existe déjà')
            # elif Chambre.objects.all().count()==14:
            #     messages.success(request, "Opps,Sky Lodge n'a que 14 Chambres")
            else:
                categorie.save()
            messages.success(request, 'Categorie bien enregistrée')
            return redirect('categorie')


    else:
        form = AjoutCategorieForm()

    categories = Categorie.objects.all()  # listes de Chambre
    total_categorie= len(categories)
    if not categories:
        messages.warning(request, "Pas de categorie trouvées")

    return HttpResponse(
        render(request, 'categorie.html', {'form': form, 'categorie': categories, 'total_categorie': total_categorie}))

@login_required
def update_categorie(request, pk):
    categorie = Categorie.objects.get(pk=pk)
    form = AjoutCategorieForm(instance=categorie)

    if request.method == 'POST':
        form = AjoutCategorieForm(request.POST, instance=categorie)
        if not form.is_valid():
            messages.warning(request, 'Veillez complétez tous les champs')
        elif form.is_valid():
            categorie = form.save(commit=False)
            categorie.save()
            messages.info(request, 'Bien Modifié')
            return redirect('categorie')

    return render(request, 'update_categorie.html', {'form': form})

@login_required
def delete_categorie(request, pk):
    item = Categorie.objects.get(pk=pk)
    item.delete()
    messages.info(request, 'Categorie supprimée ')
    return redirect('categorie')


@login_required
def ajoutChambre(request):
    if not request.user.is_staff:
        return HttpResponse("Accès refusée")

    if request.method == 'POST':
        form = AjoutChambreForm(request.POST)
        if not form.is_valid():
            messages.warning(request, 'Veillez complétez tous les champs')
        elif form.is_valid():
            chambre = form.save(commit=False)


            if Chambre.objects.filter(chambre_numero=form.cleaned_data['chambre_numero']).exists():

                messages.info(request,'cette numéro de chambre existe')
            elif Chambre.objects.all().count()==14:
                messages.success(request, "Opps,Sky Lodge n'a que 14 Chambres")
            else:

                chambre.save()
            messages.success(request, 'Chambre bien enregistrée')
            return redirect('chambres')


    else:
        form = AjoutChambreForm()

    chambres = Chambre.objects.all()  # listes de Chambre
    total_chambres = len(chambres)
    if not chambres:
        messages.warning(request, "Pas de Chambre trouvées")

    return HttpResponse(
        render(request, 'chambres.html', {'form': form, 'chambres': chambres, 'total_chambres': total_chambres}))

@login_required
def listUsers(request):

    listUser= User.objects.all()
    if listUser== 0:
        messages.warning(request, "Aucun utilisateur Enregistré")
    return render(request, 'staff/listUser.html', {'users': listUser})



@login_required
def ajout_reservations(request, pk, fromdate, todate):

    if request.user.is_staff:
        messages.warning(request, "Ouff! vous n'est pas un Client.. connectez-vous")
        return render(request, 'accueil.html')
    chambre = get_object_or_404(Chambre, pk=pk)
    categorie=get_object_or_404(Categorie,chambre=chambre.id)
    res_id=0
  
   
    fromdate=fromdate
    todate=todate
  
       
    
    # convert string to date object
    d1 = datetime.strptime(fromdate, "%Y-%m-%d")
    d2 = datetime.strptime(todate, "%Y-%m-%d")


    # difference between dates in timedelta
    delta = d2 - d1

    days = delta.days

    amount= days * categorie.prix




    if request.method == 'POST':
        form = AjoutReservationForm(request.POST)
        if not form.is_valid():
            messages.warning(request, 'Veillez complétez tous les champs')
        elif form.is_valid():
            reservation = form.save(commit=False)
            reservation.client = request.user
            reservation.chambre = chambre
            reservation.debut_sejour=fromdate
            reservation.fin_sejour=todate

            
            reservation.save()
            
            res_id=Reservation.objects.filter(client=request.user.id).order_by('-id')[0]
            
            res_id= res_id.id
         

            messages.success(request, 'Félicitations , bien réserver')


            return redirect("pay_opt", latest=res_id ,amount=amount  )
        #
    else:
        form = AjoutReservationForm()
    #     listes de reservations
    reservations = Reservation.objects.all()
    if reservations.count()==0:
        messages.warning(request, "Pas de réservations trouvées")
    ctx = {'form': form,'reservations': reservations, 'chambre': chambre, "fromdate":fromdate,"todate":todate,"days":days,"categorie":categorie,"amount":amount,"latest":res_id}
    return render(request,'reservation.html',ctx )




@login_required
def update_chambre(request, pk):
    chambre_id = Chambre.objects.get(pk=pk)
    form = AjoutChambreForm(instance=chambre_id)

    if request.method == 'POST':
        form = AjoutChambreForm(request.POST, instance=chambre_id)
        if not form.is_valid():
            messages.warning(request, 'Veillez complétez tous les champs')
        elif form.is_valid():
            chambre = form.save(commit=False)
            chambre.save()
            messages.info(request, 'Bien annulée')
            return redirect('chambres')

    return render(request, 'update_chambre.html', {'form': form})





@login_required
def delete_chambre(request, pk):
    item = Chambre.objects.get(pk=pk)
    item.delete()
    messages.info(request, 'Bien supprimer')
    return redirect('chambres')





@login_required
def listReservation(request):
    listReservations = Reservation.objects.all().filter(status= "True")
    if listReservations.count()== 0:
        messages.info(request, "Pas de Réservation trouvées")
    return render(request, 'listReservations.html', {'reservations': listReservations})

@login_required
def historiqueReservations(request):
    history = Reservation.objects.all().filter(status="False")
    if history.count()== 0:
        messages.info(request, "Pas Historique ! ")
    return render(request, 'historique.html', {'history': history})






@login_required
def update_reservation(request, pk):
    res = Reservation.objects.get(pk=pk)
    form = EditReservationForm(instance=res)

    if request.method == 'POST':
        form = EditReservationForm(request.POST, instance=res)
        if not form.is_valid():
            messages.warning(request, 'Veillez complétez tous les champs')
        elif form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            messages.info(request, 'Bien Modifié')
            return redirect('list-reservations')

    return render(request, 'update_reservation.html', {'form': form,"res":res,})

@login_required
def delete_reservation(request, pk):
    item = Reservation.objects.get(pk=pk)
    item.delete()
    messages.info(request, 'Réservation annulée ')
    return redirect('list-reservations')


@login_required
def delete_history(request, pk):
    item = Reservation.objects.get(pk=pk)
    item.delete()
    messages.info(request, 'Historique suprimé ')
    return redirect('history')


@login_required
def payment_options(request,amount,latest):
    reservation=latest
    amount=amount
    payment_options = ihela_bank_list()
    ctx = {"bank_list": payment_options,"reservation":reservation,"amount":amount}
    return render(request,"payment_options.html",ctx)

@login_required
def pay_with_ihela(request,amount,bank_slug,pk):
    REDIRECT_URL="https://skylodge.ubuviz.com/skylodge/reservations"
    try:
        res = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
         messages.info(request, 'Pas de résrevations trouvée; ')
    url=''
    if request.method == "POST":
        form = iHelaClientAccountForm(request.POST)

        if form.is_valid():
            client = form.save(commit=False)

            account = request.POST.get('account',None)
            if account:
                customer = ihela_api_customer_lookup(bank_slug,account)

                if customer['name']:
                    description = "reservation chambre {}".format(res.chambre)
                    date_ref = datetime.now().strftime("%y%m%d")
                    ref_number = uuid4().hex[:5]
                    reference = "REV-"+date_ref+ref_number
                    # bank_client=bank_slug
                    # bank=bank_slug
                    redirect_uri=REDIRECT_URL
                    init_bill = ihela_api_bill_initiate(amount,customer["account_number"],description,reference,redirect_uri=REDIRECT_URL)
                    if isinstance(init_bill,dict):
                        print(amount,customer["account_number"],description,reference,redirect_uri)
                    else:
                        print("init bill",init_bill,amount,customer["account_number"],description,reference)

                    # init_bill=init_bill['bill']
                    
                    # for bill in  init_bill.bill:
                    #     url=bill.marchant.merchant.confirmation_uri

                    print("**************************************",init_bill
                    )

                 

                    client.reservation = res
                    client.amount = amount
                    client.reference = reference
                    client.client=request.user
                    

                    client.save()
                    url=init_bill["bill"]["confirmation_uri"]
                    messages.info(request,customer['name'] + " Vous venez de payer "+ str(amount) + " FBU :" + reference  )
                    return redirect(url)

            else:
            
                messages.info(request,"no!" )

        else:
            print(form.errors.as_data())
            messages.info(request,"vide!" )
            

    ctx={"amount":amount}
    return render(request,"pay_ihela.html",ctx)


def ihela_webhook(request):
    pass
    # return render("")


class iHelaCallbackAPIView(APIView):

    def post(self,request):
        merchant_reference = self.request.data.get("merchant_reference",None)
        bill_code = self.request.data.get("bill_code",None)
        error = self.request.data.get("error",None)
        error_message = self.request.data.get("error_message",None)
        payment_reference = self.request.data.get("payment_reference",None)

        try:
            payment = Payment.objects.get(reference=merchant_reference)
            if error == False:
                reservation = payment.reservation
                reservation.reservation_status = reservation.PAID
                reservation.save()
                payment.bill_reference = payment_reference
                payment.save()
                return Response({"error":False,"error_message":"Success"})
            elif error == True:
                return Response({"error":True,"error_message":"Failed"})

        except Payment.DoesNotExist:
            pass

        return Response({})


def ihela_transaction_verification(request):
    pass





