from django.contrib.auth.models import User
from django.db import models


class Categorie(models.Model):
    type = models.CharField(max_length=30)
    prix = models.IntegerField()

    def __str__(self):
        return str(self.type)


class Chambre(models.Model):
    CHAMBRE_STATUS = (
        ("disponible", "Disponible"),
        ("non-disponible", "Non-disponible"),
    )
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    chambre_status = models.CharField(max_length=20, choices=CHAMBRE_STATUS)
    chambre_numero = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.chambre_numero)


class Reservation(models.Model):
    RES_STATUS = (
        ("True","True"),
        ("False","False")
        )
    PAID =  "P"
    NOT_PAID = "N"

    RESERVATION_STATUS =  (("PAID","P"),("NOT_PAID","N"))

    debut_sejour = models.DateField(auto_now=False)
    fin_sejour = models.DateField(auto_now=False)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=100,choices=RES_STATUS,default=True)
    date_operation = models.DateTimeField(auto_now_add=True)
    reservation_status = models.CharField(max_length=1,default=PAID)

    def __str__(self):
        return str(self.client.username)

class Payment(models.Model):
    date_de_payment = models.DateField(auto_now=True)
    reservation = models.ForeignKey(Reservation)
    amount = models.IntegerField()
    reference = models.CharField(unique=True,max_length=200)
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.client + self.reference
