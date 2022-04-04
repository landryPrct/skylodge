from django.contrib.auth.models import User
from django.db import models


class Chambre(models.Model):
    CHAMBRE_STATUS = (
        ("disponible", "Disponible"),
        ("non-disponible", "Non-disponible"),
    )

    CHAMBRE_TYPE = (
        ("VIP", "VIP"),
        ("semi-VIP", "Semi-VIP"),
    )
    chambre_type = models.CharField(max_length=30, choices=CHAMBRE_TYPE)
    chambre_status = models.CharField(max_length=20, choices=CHAMBRE_STATUS)
    prix = models.IntegerField()
    chambre_numero = models.IntegerField()

    def __str__(self):
        return str(self.chambre_numero)

class Reservation(models.Model):
    debut_sejour=models.DateField(auto_now=False)
    fin_sejour=models.DateField(auto_now=False)
    chambre=models.ForeignKey(Chambre,on_delete=models.CASCADE)
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    date_operation=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.client.username)