from django.contrib import admin
from django.contrib.auth.models import Group
from reservations.models import Chambre, Reservation,Categorie


admin.site.site_header = 'Sky Lodge Administration '
admin.site.register(Chambre)
admin.site.register(Reservation)
admin.site.register(Categorie)
admin.site.unregister(Group)
