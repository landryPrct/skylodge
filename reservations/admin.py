from django.contrib import admin
from django.contrib.auth.models import Group
from reservations.models import Chambre, Reservation, Categorie, Payment
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp, EmailAddress


class cha(admin.ModelAdmin):
    list_display = ['chambre_status', 'categorie', "chambre_numero"]


class res(admin.ModelAdmin):
    list_display = ["id", 'debut_sejour', 'fin_sejour', 'client', 'chambre', 'status', "date_operation","payment_status" ]


class pay(admin.ModelAdmin):
    list_display = ["date_de_payment",
                    "reservation",
                    "amount",
                    "reference",
                    "client",
                    "bill_reference", ]

class cat(admin.ModelAdmin):
    list_display = ['type', "prix"]


admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)


admin.site.site_header = 'Sky Lodge Administration '
admin.site.index_title = "Welcome Sky Lodge Administration  "
admin.site.register(Chambre, cha)
admin.site.register(Reservation, res)
admin.site.register(Categorie, cat)
admin.site.register(Payment, pay)
admin.site.unregister(Group)
