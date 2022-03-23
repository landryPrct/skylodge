from django.db import models
import math
from django.contrib.auth.models import User

from django.utils import timezone


# Create your models here.
class Chambre(models.Model):
    numero_chambre= models.IntegerField(unique=True, default=1)  # numero de la chambre
    description = models.CharField(max_length=100, default="Bienvenus")  #
    priX = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return str(self.numero_chambre)


class Reservation(models.Model):  # la Reservation
    reserver_par = models.ForeignKey(User, related_name='reservation', on_delete=models.CASCADE)  # le client
    chambre = models.ForeignKey(Chambre, related_name='reservation', on_delete=models.CASCADE)
    reserve_a = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.reserver_par)


class Paiement(models.Model):
    payer_par = models.ForeignKey(User, related_name='paiements', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.payer_par)
